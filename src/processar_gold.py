"""
Módulo de Processamento da Camada Gold (Feature Store e Engenharia de Atributos)
Projeto: Artefato de Previsão de Demanda de Refeições - IFSP Campus Itaquaquecetuba
Mestrado Profissional

Transforma dados higienizados da Camada Silver em um Feature Store pronto para Machine Learning:
1. Lags autoregressivos (dia anterior, mesma semana passada, semana retrasada).
2. Estatísticas móveis (médias móveis de 5, 10 e 20 dias úteis, volatilidade e amplitude).
3. Transformações cíclicas e sazonais (seno/cosseno de dia da semana e mês).
4. Codificação estruturada de cardápio (proteínas, preparos e atratividade).
5. Engenharia de variáveis meteorológicas (chuva, frio, calor, vento, sensação térmica).
6. Segmentação de treino, validação e inferência multi-horizonte (t+1 e t+2).
"""

import os
import pandas as pd
import numpy as np

SILVER_PATH = "dados/silver/silver_fato_diaria.parquet"
GOLD_DIR = "dados/gold"

def construir_features_gold():
    print("[*] Carregando dados integrados da Camada Silver...")
    df = pd.read_parquet(SILVER_PATH)
    df["data_dt"] = pd.to_datetime(df["data_iso"])
    df = df.sort_values("data_dt").reset_index(drop=True)
    
    # -------------------------------------------------------------
    # 1. LAGS AUTORREGRESSIVOS E MÉDIAS MÓVEIS (MEMÓRIA TEMPORAL)
    # -------------------------------------------------------------
    print("[*] Construindo lags e estatísticas móveis...")
    
    # Filtrar apenas dias com consumo real para criar defasagens na sequência letiva
    df_consumo = df[df["consumo"].notna()].sort_values("data_dt").copy()
    
    # Lags em sequência de dias úteis com refeição
    df_consumo["lag_1_dia_letivo"] = df_consumo["consumo"].shift(1)
    df_consumo["lag_2_dia_letivo"] = df_consumo["consumo"].shift(2)
    df_consumo["lag_5_dias_letivos"] = df_consumo["consumo"].shift(5)   # ~1 semana útil atrás
    df_consumo["lag_10_dias_letivos"] = df_consumo["consumo"].shift(10) # ~2 semanas úteis atrás
    
    # Estatísticas móveis (baseadas nos dias letivos anteriores - shift 1 para não vazar o dia atual)
    df_consumo["media_movel_5d"] = df_consumo["consumo"].rolling(5).mean().shift(1)
    df_consumo["desvio_movel_5d"] = df_consumo["consumo"].rolling(5).std().shift(1)
    df_consumo["min_movel_5d"] = df_consumo["consumo"].rolling(5).min().shift(1)
    df_consumo["max_movel_5d"] = df_consumo["consumo"].rolling(5).max().shift(1)
    df_consumo["amplitude_movel_5d"] = df_consumo["max_movel_5d"] - df_consumo["min_movel_5d"]
    
    df_consumo["media_movel_10d"] = df_consumo["consumo"].rolling(10).mean().shift(1)
    df_consumo["media_movel_20d"] = df_consumo["consumo"].rolling(20).mean().shift(1)
    
    # Lags por tempo calendário (mesmo dia da semana 7 e 14 dias corridos atrás)
    df_cal_lags = df[["data_dt", "consumo"]].dropna().copy()
    
    df_lag7 = df_cal_lags.copy()
    df_lag7["data_dt"] = df_lag7["data_dt"] + pd.Timedelta(days=7)
    df_lag7 = df_lag7.rename(columns={"consumo": "consumo_mesmo_dia_sem_passada"})
    
    df_lag14 = df_cal_lags.copy()
    df_lag14["data_dt"] = df_lag14["data_dt"] + pd.Timedelta(days=14)
    df_lag14 = df_lag14.rename(columns={"consumo": "consumo_mesmo_dia_sem_retrasada"})
    
    # Merge das features temporais
    cols_roll = [
        "data_iso", "lag_1_dia_letivo", "lag_2_dia_letivo", "lag_5_dias_letivos", "lag_10_dias_letivos",
        "media_movel_5d", "desvio_movel_5d", "min_movel_5d", "max_movel_5d", "amplitude_movel_5d",
        "media_movel_10d", "media_movel_20d"
    ]
    df = pd.merge(df, df_consumo[cols_roll], on="data_iso", how="left")
    df = pd.merge(df, df_lag7, on="data_dt", how="left")
    df = pd.merge(df, df_lag14, on="data_dt", how="left")
    
    # -------------------------------------------------------------
    # 2. ENGENHARIA DE CALENDÁRIO E TRANSFORMAÇÕES CÍCLICAS
    # -------------------------------------------------------------
    print("[*] Codificando atributos de calendário e sazonalidade...")
    df["dia_da_semana_num"] = df["data_dt"].dt.dayofweek  # 0=Segunda ... 4=Sexta
    df["dia_do_mes"] = df["data_dt"].dt.day
    df["semana_do_ano"] = df["data_dt"].dt.isocalendar().week.astype(int)
    
    # Dummies de dias úteis
    for d_num, d_nome in enumerate(["segunda", "terca", "quarta", "quinta", "sexta"]):
        df[f"is_{d_nome}"] = (df["dia_da_semana_num"] == d_num).astype(int)
    df["is_sabado"] = (df["dia_da_semana_num"] == 5).astype(int)
    
    # Transformações trigonométricas cíclicas (para modelos lineares e redes)
    df["sin_dia_semana"] = np.sin(2 * np.pi * df["dia_da_semana_num"] / 7)
    df["cos_dia_semana"] = np.cos(2 * np.pi * df["dia_da_semana_num"] / 7)
    df["sin_mes"] = np.sin(2 * np.pi * df["mes"] / 12)
    df["cos_mes"] = np.cos(2 * np.pi * df["mes"] / 12)
    
    # Posição no mês
    df["is_inicio_mes"] = (df["dia_do_mes"] <= 10).astype(int)
    df["is_fim_mes"] = (df["dia_do_mes"] >= 21).astype(int)
    
    # Tipo de evento acadêmico
    eventos_principais = ["aula_regular", "acolhimento", "sabado_letivo", "conselho_classe", "encerramento_etapa"]
    for ev in eventos_principais:
        df[f"evento_{ev}"] = (df["evento_tipo"] == ev).astype(int)
        
    # -------------------------------------------------------------
    # 3. ENGENHARIA DO CARDÁPIO (ONE-HOT E SCORES DE ATRATIVIDADE)
    # -------------------------------------------------------------
    print("[*] Codificando atributos de cardápio e atratividade...")
    
    # Dummies de proteína
    proteinas = ["frango", "bovina", "suina", "peixe", "feijoada", "mista"]
    for p in proteinas:
        df[f"proteina_{p}"] = (df["proteina_tipo"] == p).astype(int)
        
    # Dummies de preparo
    preparos = ["ao_molho_ou_refogado", "assado", "cozido_ou_refogado", "cremoso_ou_ensopado", "massa_ou_montado", "grelhado", "empanado_ou_a_milanesa", "churrasco_ou_espeto"]
    for pr in preparos:
        col_clean = pr.replace("_ou_", "_").replace("_a_", "_")
        df[f"preparo_{col_clean}"] = (df["preparo_tipo"] == pr).astype(int)
        
    # Scores históricos de atratividade (blindados contra vazamento de dados de teste de 2026)
    df_treino_hist = df[df["ano"] < 2026]
    media_hist_consumo = df_treino_hist["consumo"].mean()
    
    score_prot_map = df_treino_hist.groupby("proteina_tipo")["consumo"].mean().to_dict()
    df["score_atratividade_proteina"] = df["proteina_tipo"].map(score_prot_map).fillna(media_hist_consumo)
    
    score_prep_map = df_treino_hist.groupby("preparo_tipo")["consumo"].mean().to_dict()
    df["score_atratividade_preparo"] = df["preparo_tipo"].map(score_prep_map).fillna(media_hist_consumo)
    
    # -------------------------------------------------------------
    # 4. ENGENHARIA DE FEATURES METEOROLÓGICAS (CLIMA E MOBILIDADE)
    # -------------------------------------------------------------
    print("[*] Construindo features de sensibilidade meteorológica...")
    df["amplitude_termica"] = df["temperature_2m_max"] - df["temperature_2m_min"]
    df["is_chuva_forte"] = (df["precipitation_sum"] >= 10.0).astype(int)
    df["is_chuva_persistente"] = (df["precipitation_hours"] >= 6.0).astype(int)
    df["is_dia_frio"] = (df["temperature_2m_max"] <= 18.0).astype(int)
    df["is_dia_muito_quente"] = (df["temperature_2m_max"] >= 30.0).astype(int)
    df["is_vento_forte"] = (df["wind_speed_10m_max"] >= 20.0).astype(int)
    
    # Índice de severidade climática (combina chuva e vento para mobilidade CPTM)
    df["indice_adversidade_climatica"] = (
        (df["precipitation_sum"] / 10.0) * 0.5 +
        (df["precipitation_hours"] / 6.0) * 0.3 +
        (df["wind_speed_10m_max"] / 20.0) * 0.2
    ).clip(0, 5)
    
    # -------------------------------------------------------------
    # 5. REGIME DE RESERVA E ESTIMATIVA DA NUTRICIONISTA
    # -------------------------------------------------------------
    df["is_regime_nutricionista"] = (df["regime_reserva"] == "nutricionista_estimativa").astype(int)
    # Estimativa calibrada: no regime 2026, subtrai o viés médio histórico conservador (+15.4 ref)
    df["estimativa_nutricionista_calibrada"] = np.where(
        df["is_regime_nutricionista"] == 1,
        (df["reservas"] - 15.4).clip(lower=0),
        df["reservas"]
    )
    
    # -------------------------------------------------------------
    # 6. FILTRO DE TREINAMENTO SEGURO (DATA QUALITY MASK)
    # -------------------------------------------------------------
    # Dias válidos para treino: dias letivos com consumo regular, sem greve, sem apagão/dispensa, sem enchente extrema
    df["is_treino_valido"] = (
        (df["is_dia_letivo"] == True) &
        (df["consumo"].notna()) &
        (df["status_qualidade_registro"] == "REGULAR") &
        (df["flag_greve"] == False)
    ).astype(int)
    
    # Partição temporal (Split para Machine Learning sem vazamento):
    # - Treino: 2023, 2024 e 2025
    # - Validação: 2026 até agosto
    # - Teste / Out-of-Time: Setembro e Outubro de 2026
    def definir_particao(row):
        if row["is_treino_valido"] == 0:
            return "EXCLUIDO_TREINO"
        if row["ano"] < 2026:
            return "TREINO"
        elif row["mes"] <= 8:
            return "VALIDACAO"
        else:
            return "TESTE"
            
    df["split_modelagem"] = df.apply(definir_particao, axis=1)
    
    return df

def salvar_camada_gold():
    os.makedirs(GOLD_DIR, exist_ok=True)
    
    df_gold = construir_features_gold()
    
    # 1. Feature Store Completa (todos os dias de 2023 a 2026 com todas as features)
    p_comp_parquet = f"{GOLD_DIR}/gold_feature_store_completa.parquet"
    p_comp_csv = f"{GOLD_DIR}/gold_feature_store_completa.csv"
    df_gold.to_parquet(p_comp_parquet, index=False)
    df_gold.to_csv(p_comp_csv, sep=";", index=False, encoding="utf-8-sig")
    print(f"[OK] Feature Store Completa salva: {len(df_gold)} linhas -> {p_comp_parquet}")
    
    # 2. Base de Treino e Avaliação Limpa (dias regulares para ML)
    df_ml = df_gold[df_gold["is_treino_valido"] == 1].copy()
    p_ml_parquet = f"{GOLD_DIR}/gold_dataset_ml_limpo.parquet"
    p_ml_csv = f"{GOLD_DIR}/gold_dataset_ml_limpo.csv"
    df_ml.to_parquet(p_ml_parquet, index=False)
    df_ml.to_csv(p_ml_csv, sep=";", index=False, encoding="utf-8-sig")
    print(f"[OK] Dataset ML Limpo salvo: {len(df_ml)} linhas úteis -> {p_ml_parquet}")
    
    print("\n[RESUMO DA PARTIÇÃO TEMPORAL PARA MACHINE LEARNING]")
    print(df_gold["split_modelagem"].value_counts())
    
    return df_gold, df_ml

if __name__ == "__main__":
    salvar_camada_gold()
