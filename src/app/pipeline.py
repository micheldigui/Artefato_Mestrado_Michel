"""
Módulo do Pipeline Analítico e Inferência Preditiva
Prepara os atributos e executa os modelos campeões da pesquisa (Lasso, Ridge e Híbrido)
com margens conformais calibradas, gerando previsões para as semanas t+1 e t+2.
"""

import os
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from datetime import datetime, timedelta

try:
    from storage import carregar_historico_consumo, carregar_planejamento_nutricionista, salvar_predicoes_geradas
    from clima import obter_previsao_clima_futura
except ImportError:
    from .storage import carregar_historico_consumo, carregar_planejamento_nutricionista, salvar_predicoes_geradas
    from .clima import obter_previsao_clima_futura

GOLD_DATASET = "dados/gold/gold_dataset_ml_limpo.parquet"

# Mapeamento padrão de dias da semana em português
DIAS_SEMANA_PT = {
    0: "Segunda-feira",
    1: "Terça-feira",
    2: "Quarta-feira",
    3: "Quinta-feira",
    4: "Sexta-feira",
    5: "Sábado",
    6: "Domingo"
}

def obter_proximos_dias_uteis(origem_dt=None, num_dias=10):
    """
    Retorna lista de datas úteis futuras (segunda a sexta).
    origem_dt: data de corte (default = hoje).
    """
    if origem_dt is None:
        origem_dt = datetime.now()
    
    # Se hoje é fim de semana, avança para a próxima segunda-feira
    cur = origem_dt + timedelta(days=1)
    dias = []
    while len(dias) < num_dias:
        if cur.weekday() < 5:  # 0 a 4 = seg a sex
            dias.append(cur)
        cur += timedelta(days=1)
    return dias

def construir_dataset_treino():
    """
    Prepara a base histórica para treino dos modelos supervisionados.
    Carrega o dataset Gold preservado e alinha os atributos centrais.
    """
    if not os.path.exists(GOLD_DATASET):
        raise FileNotFoundError(f"Arquivo de treino não encontrado: {GOLD_DATASET}")
    
    df_gold = pd.read_parquet(GOLD_DATASET).copy()
    
    # Colunas preditivas essenciais comprovadas na pesquisa
    features_numericas = [
        "consumo_lag_5", "consumo_lag_10", "media_movel_5d",
        "precipitation_sum", "temperature_2m_max"
    ]
    
    # Se alguma coluna de lag estiver ausente, preenche com médias
    for col in features_numericas:
        if col not in df_gold.columns:
            df_gold[col] = df_gold["consumo"].median()
        else:
            df_gold[col] = df_gold[col].fillna(df_gold["consumo"].median())
            
    # Flags de dia da semana
    for d in range(5):
        col_name = f"is_dia_sem_{d}"
        if col_name not in df_gold.columns:
            df_gold[col_name] = (df_gold["data_dt"].dt.dayofweek == d).astype(int)
            
    # Flags de proteína
    for prot in ["bovina", "frango", "suina", "peixe", "ovo"]:
        col_name = f"is_prot_{prot}"
        if col_name not in df_gold.columns:
            if "proteina_tipo" in df_gold.columns:
                df_gold[col_name] = df_gold["proteina_tipo"].str.lower().str.contains(prot, na=False).astype(int)
            else:
                df_gold[col_name] = 0
                
    return df_gold

def treinar_modelos(df_treino):
    """Treina os estimadores Ridge e Lasso com os hiperparâmetros selecionados na pesquisa."""
    cols_features = [
        "consumo_lag_5", "consumo_lag_10", "media_movel_5d",
        "precipitation_sum", "temperature_2m_max",
        "is_dia_sem_0", "is_dia_sem_1", "is_dia_sem_2", "is_dia_sem_3", "is_dia_sem_4",
        "is_prot_bovina", "is_prot_frango", "is_prot_suina", "is_prot_peixe", "is_prot_ovo"
    ]
    
    X = df_treino[cols_features].values
    y = df_treino["consumo"].values
    
    modelo_ridge = Ridge(alpha=10.0)
    modelo_ridge.fit(X, y)
    
    modelo_lasso = Lasso(alpha=0.5)
    modelo_lasso.fit(X, y)
    
    return modelo_ridge, modelo_lasso, cols_features

def executar_pipeline_previsao(
    horizonte_alvo="todos",
    usar_clima=True,
    usar_cardapio=True,
    usar_nutri=True,
    peso_ia=0.5,
    tipo_margem="Recomendada da Pesquisa",
    margem_adicional=0
):
    """
    Executa a inferência para os horizontes futuros com flexibilidade de seleção de dados:
    - horizonte_alvo: 'todos', 'Semana_t1' (curta) ou 'Pos_Semana_t2' (longa)
    - usar_clima: True/False (ativa/desativa previsão meteorológica Open-Meteo)
    - usar_cardapio: True/False (ativa/desativa efeito de proteínas e atratividade do cardápio)
    - usar_nutri: True/False (ativa/desativa combinação híbrida com a nutricionista)
    - peso_ia: proporção da IA no modelo híbrido (0.0 a 1.0)
    - tipo_margem: 'Recomendada da Pesquisa', 'Moderada (+10 ref)', 'Prudencial (+19 ref)', 'Predição Pura (+0 ref)', 'Personalizada'
    """
    # 1. Carrega dados
    df_consumo_hist = carregar_historico_consumo()
    df_planejamento = carregar_planejamento_nutricionista()
    df_clima_futuro = obter_previsao_clima_futura(dias_frente=16) if usar_clima else pd.DataFrame()
    df_treino = construir_dataset_treino()
    
    # 2. Treina modelos
    modelo_ridge, modelo_lasso, cols_features = treinar_modelos(df_treino)
    
    # 3. Determina as 10 datas úteis futuras
    datas_uteis = obter_proximos_dias_uteis(num_dias=10)
    
    # Últimos consumos conhecidos para cálculo de lags
    ultimos_consumos = df_consumo_hist.dropna(subset=["consumo"]).sort_values("data_dt")
    serie_consumo = ultimos_consumos["consumo"].values
    media_recente_5d = float(np.mean(serie_consumo[-5:])) if len(serie_consumo) >= 5 else 150.0
    mediana_temp = float(df_treino["temperature_2m_max"].median()) if "temperature_2m_max" in df_treino.columns else 23.0
    
    # Lags por dia da semana
    def pegar_ultimo_consumo_dia_semana(dia_sem, defasagem_semanas=1):
        df_dia = ultimos_consumos[ultimos_consumos["data_dt"].dt.dayofweek == dia_sem]
        if len(df_dia) >= defasagem_semanas:
            return float(df_dia.iloc[-defasagem_semanas]["consumo"])
        return media_recente_5d

    linhas_pred = []
    
    for idx, dt in enumerate(datas_uteis):
        data_iso = dt.strftime("%Y-%m-%d")
        data_formatada = dt.strftime("%d/%m/%Y")
        dia_sem_num = dt.weekday()
        dia_sem_nome = DIAS_SEMANA_PT[dia_sem_num]
        horizonte = "Semana_t1" if idx < 5 else "Pos_Semana_t2"
        
        # Filtra pelo horizonte alvo se solicitado
        if horizonte_alvo != "todos" and horizonte != horizonte_alvo:
            continue
        
        # Clima previsto para o dia (se ativado pelo usuário)
        if usar_clima and not df_clima_futuro.empty:
            clima_row = df_clima_futuro[df_clima_futuro["data_iso"] == data_iso]
            if not clima_row.empty:
                precip = float(clima_row.iloc[0]["precipitation_sum"])
                temp_max = float(clima_row.iloc[0]["temperature_2m_max"])
            else:
                precip = 0.0
                temp_max = mediana_temp
        else:
            precip = 0.0
            temp_max = mediana_temp
            
        # Planejamento da nutricionista para a data (se preenchido e ativado)
        plan_row = df_planejamento[df_planejamento["data_iso"] == data_iso]
        if not plan_row.empty and usar_cardapio:
            prato = plan_row.iloc[0].get("prato_principal", "Cardápio Regular")
            prot = plan_row.iloc[0].get("proteina_tipo", "frango").lower()
            preparo = plan_row.iloc[0].get("preparo_tipo", "assado")
        else:
            prato = "Padrão Escolar Regular"
            prot = "frango"
            preparo = "assado"
            
        if usar_nutri:
            if not plan_row.empty and pd.notna(plan_row.iloc[0].get("planejado_nutri")) and float(plan_row.iloc[0].get("planejado_nutri", 0)) > 0:
                val_nutri = float(plan_row.iloc[0].get("planejado_nutri"))
            else:
                # Estimativa de referência da nutricionista caso não haja lançamento específico para o dia
                val_nutri = 170.0
        else:
            val_nutri = None
            
        # Features do dia
        lag_5 = pegar_ultimo_consumo_dia_semana(dia_sem_num, defasagem_semanas=1)
        lag_10 = pegar_ultimo_consumo_dia_semana(dia_sem_num, defasagem_semanas=2)
        
        vetor_X = {
            "consumo_lag_5": lag_5,
            "consumo_lag_10": lag_10,
            "media_movel_5d": media_recente_5d,
            "precipitation_sum": precip,
            "temperature_2m_max": temp_max,
            "is_dia_sem_0": 1 if dia_sem_num == 0 else 0,
            "is_dia_sem_1": 1 if dia_sem_num == 1 else 0,
            "is_dia_sem_2": 1 if dia_sem_num == 2 else 0,
            "is_dia_sem_3": 1 if dia_sem_num == 3 else 0,
            "is_dia_sem_4": 1 if dia_sem_num == 4 else 0,
            "is_prot_bovina": 1 if ("bovina" in prot and usar_cardapio) else 0,
            "is_prot_frango": 1 if ("frango" in prot and usar_cardapio) else 0,
            "is_prot_suina": 1 if ("suina" in prot and usar_cardapio) else 0,
            "is_prot_peixe": 1 if ("peixe" in prot and usar_cardapio) else 0,
            "is_prot_ovo": 1 if ("ovo" in prot and usar_cardapio) else 0
        }
        
        X_instancia = np.array([[vetor_X[c] for c in cols_features]])
        
        # Previsão pontual do modelo Lasso (Campeão) e Ridge
        pred_lasso = float(modelo_lasso.predict(X_instancia)[0])
        pred_ridge = float(modelo_ridge.predict(X_instancia)[0])
        pred_ia_pura = (pred_lasso + pred_ridge) / 2.0
        
        # Combinação Híbrida se nutricionista estiver ativada
        if val_nutri is not None and usar_nutri:
            p_ia = float(peso_ia)
            p_nutri = 1.0 - p_ia
            pred_base = p_ia * pred_ia_pura + p_nutri * val_nutri
            margem_rec_padrao = 12.0 # Margem residual ótima para modelo híbrido da pesquisa
        else:
            pred_base = pred_ia_pura
            margem_rec_padrao = 19.0 # Margem prudencial P85 da pesquisa
            
        # Aplicação da política de margem selecionada pelo usuário
        if tipo_margem == "Recomendada da Pesquisa":
            margem_valor = margem_rec_padrao
        elif tipo_margem == "Moderada (+10 ref)":
            margem_valor = 10.0
        elif tipo_margem == "Prudencial (+19 ref)":
            margem_valor = 19.0
        elif tipo_margem == "Predição Pura (+0 ref)":
            margem_valor = 0.0
        elif tipo_margem == "Personalizada":
            margem_valor = float(margem_adicional)
        else:
            margem_valor = margem_rec_padrao
            
        pred_final = pred_base + margem_valor
        
        # Alertas operacionais
        alertas = []
        if dia_sem_num == 4:
            alertas.append("Sexta-feira: retração pedagógica (~28% menor)")
        if usar_clima and precip >= 15.0:
            alertas.append(f"Chuva forte prevista ({precip:.1f}mm): risco de retração de frequência")
        if usar_cardapio:
            if "bovina" in prot or "feijoada" in prato.lower():
                alertas.append("Prato de alta atratividade: tendência de maior comparecimento")
            elif "peixe" in prot or "ovo" in prot:
                alertas.append("Proteína com menor adesão histórica")
            
        linhas_pred.append({
            "data_dt": dt,
            "data": data_formatada,
            "data_iso": data_iso,
            "dia_semana": dia_sem_nome,
            "horizonte": horizonte,
            "prato_principal": prato if usar_cardapio else "Cardápio Neutro",
            "proteina_tipo": prot.capitalize() if usar_cardapio else "Geral",
            "preparo_tipo": preparo.capitalize() if usar_cardapio else "Geral",
            "chuva_mm": round(precip, 1) if usar_clima else 0.0,
            "temp_max_c": round(temp_max, 1) if usar_clima else round(mediana_temp, 1),
            "estimativa_nutri": round(val_nutri) if val_nutri is not None else None,
            "ia_pura": round(pred_ia_pura),
            "pred_base_combinada": round(pred_base),
            "margem_aplicada": round(margem_valor),
            "recomendacao_final": round(pred_final),
            "alertas": "; ".join(alertas) if alertas else "Operação normal"
        })
        
    df_resultado = pd.DataFrame(linhas_pred)
    salvar_predicoes_geradas(df_resultado)
    return df_resultado
