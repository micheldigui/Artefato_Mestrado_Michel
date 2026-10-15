"""
Módulo do Pipeline Analítico e Inferência Preditiva
Prepara os atributos e executa os modelos campeões da pesquisa (Ridge, Híbrido 50/50 e Conformal Prediction)
com margens conformais calibradas, gerando previsões para as semanas t+1 e t+2 e expondo as features geradas.
"""

import os
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from datetime import datetime, timedelta

try:
    from storage import carregar_historico_consumo, carregar_planejamento_nutricionista, salvar_predicoes_geradas, carregar_fato_diaria_completa
    from clima import obter_previsao_clima_futura
except ImportError:
    from .storage import carregar_historico_consumo, carregar_planejamento_nutricionista, salvar_predicoes_geradas, carregar_fato_diaria_completa
    from .clima import obter_previsao_clima_futura

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
GOLD_DATASET = os.path.join(ROOT_DIR, "dados", "gold", "gold_dataset_ml_limpo.parquet")

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
    """
    if origem_dt is None:
        origem_dt = datetime.now()
    
    cur = origem_dt + timedelta(days=1)
    dias = []
    while len(dias) < num_dias:
        if cur.weekday() < 5:  # 0 a 4 = seg a sex
            dias.append(cur)
        cur += timedelta(days=1)
    return dias

def construir_dataset_treino():
    """
    Prepara a base histórica para treino dos modelos supervisionados com corte estrito de qualificação.
    """
    if not os.path.exists(GOLD_DATASET):
        raise FileNotFoundError(f"Arquivo de treino não encontrado: {GOLD_DATASET}")
    
    df_gold = pd.read_parquet(GOLD_DATASET).copy()
    if "data_iso" in df_gold.columns:
        df_gold = df_gold[df_gold["data_iso"] <= "2026-08-31"].copy()
    
    # Colunas preditivas essenciais comprovadas na pesquisa
    features_numericas = [
        "consumo_lag_5", "consumo_lag_10", "media_movel_5d",
        "precipitation_sum", "temperature_2m_max"
    ]
    
    for col in features_numericas:
        if col not in df_gold.columns:
            if "consumo" in df_gold.columns:
                df_gold[col] = df_gold["consumo"].median()
            else:
                df_gold[col] = 160.0
        else:
            med = df_gold["consumo"].median() if "consumo" in df_gold.columns else 160.0
            df_gold[col] = df_gold[col].fillna(med)
            
    if "data_dt" not in df_gold.columns and "data_iso" in df_gold.columns:
        df_gold["data_dt"] = pd.to_datetime(df_gold["data_iso"])

    for d in range(5):
        col_name = f"is_dia_sem_{d}"
        if col_name not in df_gold.columns:
            df_gold[col_name] = (df_gold["data_dt"].dt.dayofweek == d).astype(int)
            
    for prot in ["bovina", "frango", "suina", "peixe", "ovo"]:
        col_name = f"is_prot_{prot}"
        if col_name not in df_gold.columns:
            if "proteina_tipo" in df_gold.columns:
                df_gold[col_name] = df_gold["proteina_tipo"].astype(str).str.lower().str.contains(prot, na=False).astype(int)
            else:
                df_gold[col_name] = 0
                
    return df_gold

def treinar_modelos(df_treino):
    """Treina os estimadores oficiais da pesquisa."""
    cols_features = [
        "consumo_lag_5", "consumo_lag_10", "media_movel_5d",
        "precipitation_sum", "temperature_2m_max",
        "is_dia_sem_0", "is_dia_sem_1", "is_dia_sem_2", "is_dia_sem_3", "is_dia_sem_4",
        "is_prot_bovina", "is_prot_frango", "is_prot_suina", "is_prot_peixe", "is_prot_ovo"
    ]
    
    X = df_treino[cols_features].values
    y = df_treino["consumo"].values
    
    # 1. Ridge Regression (Modelo Campeão Linear da Pesquisa com L2)
    modelo_ridge = Ridge(alpha=10.0, random_state=42)
    modelo_ridge.fit(X, y)
    
    # 2. Lasso Regression (L1 Esparso)
    modelo_lasso = Lasso(alpha=0.5, random_state=42)
    modelo_lasso.fit(X, y)

    # 3. Regressão Linear Simples
    modelo_linear = LinearRegression()
    modelo_linear.fit(X, y)
    
    return modelo_ridge, modelo_lasso, modelo_linear, cols_features

def executar_pipeline_previsao(
    horizonte_alvo="todos",
    usar_clima=True,
    usar_cardapio=True,
    usar_nutri=True,
    modelo_escolhido="Híbrido 50/50 (Campeão)",
    peso_ia=0.5,
    tipo_margem="Conformal P85 (+18 ref / Padrão Pesquisa)",
    margem_adicional=0
):
    """
    Executa a inferência para os horizontes futuros com flexibilidade de seleção de dados
    e retorna tanto a tabela de previsões consolidadas quanto a matriz de features geradas.
    """
    df_consumo_hist = carregar_historico_consumo()
    df_planejamento = carregar_planejamento_nutricionista()
    df_clima_futuro = obter_previsao_clima_futura(dias_frente=16) if usar_clima else pd.DataFrame()
    df_treino = construir_dataset_treino()
    
    modelo_ridge, modelo_lasso, modelo_linear, cols_features = treinar_modelos(df_treino)
    
    datas_uteis = obter_proximos_dias_uteis(num_dias=10)
    
    ultimos_consumos = df_consumo_hist.dropna(subset=["consumo"]).sort_values("data_dt")
    serie_consumo = ultimos_consumos["consumo"].values
    media_recente_5d = float(np.mean(serie_consumo[-5:])) if len(serie_consumo) >= 5 else 167.2
    media_recente_10d = float(np.mean(serie_consumo[-10:])) if len(serie_consumo) >= 10 else 165.0
    mediana_temp = float(df_treino["temperature_2m_max"].median()) if "temperature_2m_max" in df_treino.columns else 24.5
    
    def pegar_ultimo_consumo_dia_semana(dia_sem, defasagem_semanas=1):
        df_dia = ultimos_consumos[ultimos_consumos["data_dt"].dt.dayofweek == dia_sem]
        if len(df_dia) >= defasagem_semanas:
            return float(df_dia.iloc[-defasagem_semanas]["consumo"])
        return media_recente_5d

    linhas_pred = []
    linhas_features = []
    
    for idx, dt in enumerate(datas_uteis):
        data_iso = dt.strftime("%Y-%m-%d")
        data_formatada = dt.strftime("%d/%m/%Y")
        dia_sem_num = dt.weekday()
        dia_sem_nome = DIAS_SEMANA_PT[dia_sem_num]
        horizonte = "Semana_t1" if idx < 5 else "Pos_Semana_t2"
        
        if horizonte_alvo != "todos" and horizonte != horizonte_alvo:
            continue
        
        # Clima previsto para o dia
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
            
        # Planejamento da nutricionista e cardápio
        plan_row = df_planejamento[df_planejamento["data_iso"] == data_iso]
        if not plan_row.empty and usar_cardapio:
            prato = plan_row.iloc[0].get("prato_principal", "Cardápio Escolar Regular")
            prot = str(plan_row.iloc[0].get("proteina_tipo", "frango")).lower()
            preparo = str(plan_row.iloc[0].get("preparo_tipo", "assado"))
        else:
            prato = "Padrão Escolar Regular"
            prot = "frango"
            preparo = "assado"
            
        if usar_nutri:
            if not plan_row.empty and pd.notna(plan_row.iloc[0].get("planejado_nutri")) and float(plan_row.iloc[0].get("planejado_nutri", 0)) > 0:
                val_nutri = float(plan_row.iloc[0].get("planejado_nutri"))
            else:
                val_nutri = 182.7 # Média institucional da nutricionista apurada na qualificação
        else:
            val_nutri = None
            
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
        
        pred_ridge = float(modelo_ridge.predict(X_instancia)[0])
        pred_lasso = float(modelo_lasso.predict(X_instancia)[0])
        pred_linear = float(modelo_linear.predict(X_instancia)[0])
        
        # Seleção do estimador de IA conforme escolha do usuário
        if "Ridge" in modelo_escolhido:
            pred_ia_base = pred_ridge
        elif "Lasso" in modelo_escolhido:
            pred_ia_base = pred_lasso
        elif "Linear" in modelo_escolhido:
            pred_ia_base = pred_linear
        else:
            # Híbrido ou Ridge como padrão
            pred_ia_base = pred_ridge

        # Combinação Híbrida se nutricionista estiver presente
        if val_nutri is not None and usar_nutri:
            p_ia = float(peso_ia)
            p_nutri = 1.0 - p_ia
            pred_base = p_ia * pred_ia_base + p_nutri * val_nutri
            margem_padrao_auditada = 12.0 # Margem ótima calibrada para o modelo híbrido
        else:
            pred_base = pred_ia_base
            margem_padrao_auditada = 18.0 # Margem conformal P85 auditada para IA Pura (15,1% falta)
            
        # Aplicação da política de margem
        if "P85" in tipo_margem:
            margem_valor = margem_padrao_auditada
        elif "P75" in tipo_margem:
            margem_valor = 10.0
        elif "P90" in tipo_margem:
            margem_valor = 29.0
        elif "Pura" in tipo_margem:
            margem_valor = 0.0
        elif "Personalizada" in tipo_margem:
            margem_valor = float(margem_adicional)
        else:
            margem_valor = margem_padrao_auditada
            
        pred_final = max(0, pred_base + margem_valor)
        
        # Alertas operacionais inteligentes
        alertas = []
        if dia_sem_num == 4:
            alertas.append("Sexta-feira: retração sistemática de comparecimento (~20% menor)")
        if usar_clima and precip >= 10.0:
            alertas.append(f"Chuva prevista ({precip:.1f} mm): risco de evasão discente")
        if usar_cardapio:
            if "bovina" in prot or "feijoada" in prato.lower():
                alertas.append("Cardápio com proteína bovina: alta atratividade histórica")
            elif "peixe" in prot or "ovo" in prot:
                alertas.append("Proteína com menor atratividade histórica")
            
        linhas_pred.append({
            "data_dt": dt,
            "data": data_formatada,
            "data_iso": data_iso,
            "dia_semana": dia_sem_nome,
            "horizonte": "Semana t+1 (Preparo)" if horizonte == "Semana_t1" else "Semana t+2 (Compras)",
            "prato_principal": prato if usar_cardapio else "Cardápio Neutro",
            "proteina_tipo": prot.capitalize() if usar_cardapio else "Geral",
            "preparo_tipo": preparo.capitalize() if usar_cardapio else "Geral",
            "chuva_mm": round(precip, 1) if usar_clima else 0.0,
            "temp_max_c": round(temp_max, 1) if usar_clima else round(mediana_temp, 1),
            "estimativa_nutri": round(val_nutri) if val_nutri is not None else None,
            "ia_pura": round(pred_ia_base),
            "pred_base_combinada": round(pred_base),
            "margem_aplicada": round(margem_valor),
            "recomendacao_final": round(pred_final),
            "alertas": "; ".join(alertas) if alertas else "Operação normal dentro da média"
        })

        # Registrar matriz de features geradas para visualização
        linhas_features.append({
            "Data": data_formatada,
            "Dia": dia_sem_nome,
            "Horizonte": "t+1" if horizonte == "Semana_t1" else "t+2",
            "Lag 5d (ref)": round(lag_5, 1),
            "Lag 10d (ref)": round(lag_10, 1),
            "Média Móvel 5d": round(media_recente_5d, 1),
            "Chuva (mm)": round(precip, 1),
            "Temp Máx (°C)": round(temp_max, 1),
            "Proteína": prot.capitalize(),
            "Nutri Planejado": round(val_nutri, 1) if val_nutri is not None else "N/A"
        })
        
    df_resultado = pd.DataFrame(linhas_pred)
    df_features = pd.DataFrame(linhas_features)
    salvar_predicoes_geradas(df_resultado)
    return df_resultado, df_features
