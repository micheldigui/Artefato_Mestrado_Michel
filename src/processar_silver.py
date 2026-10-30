"""
Módulo de Processamento da Camada Silver
Projeto: Artefato de Previsão de Demanda de Refeições - IFSP Campus Itaquaquecetuba
Mestrado Profissional

Transforma dados brutos da camada Bronze em datasets limpos, padronizados
e auditados na camada Silver, gerando:
1. silver_calendario.parquet / .csv
2. silver_cardapio.parquet / .csv
3. silver_clima.parquet / .csv
4. silver_consumo.parquet / .csv
5. silver_reservas.parquet / .csv
6. silver_fato_diaria.parquet / .csv (tabela unificada diária com flags de qualidade)
"""

import os
import glob
import pandas as pd
import numpy as np

BRONZE_DIR = "dados/bronze"
SILVER_DIR = "dados/silver"

def padronizar_data_col(df):
    """Encontra e padroniza coluna de data para 'data_dt' (datetime) e 'data' (DD/MM/YYYY)."""
    data_cols = [c for c in df.columns if 'data' in c.lower()]
    if not data_cols:
        raise ValueError("Coluna de data não encontrada no dataframe.")
    col_orig = data_cols[0]
    df["data_dt"] = pd.to_datetime(df[col_orig], format="%d/%m/%Y", errors="coerce")
    if df["data_dt"].isna().all():
        # Tenta formato ISO caso seja YYYY-MM-DD
        df["data_dt"] = pd.to_datetime(df[col_orig], errors="coerce")
    df["data"] = df["data_dt"].dt.strftime("%d/%m/%Y")
    df["data_iso"] = df["data_dt"].dt.strftime("%Y-%m-%d")
    return df.drop(columns=[c for c in data_cols if c not in ["data", "data_iso", "data_dt"]])

def processar_calendario():
    print("[*] Processando Calendário Acadêmico (Bronze -> Silver)...")
    files = sorted(glob.glob(f"{BRONZE_DIR}/calendario/*.csv"))
    dfs = []
    for f in files:
        df = pd.read_csv(f, sep=";", encoding="utf-8-sig")
        df = padronizar_data_col(df)
        dfs.append(df[["data_dt", "data", "data_iso", "dia_da_semana", "status_legal", "evento_tipo"]])
    
    df_cal = pd.concat(dfs, ignore_index=True).drop_duplicates(subset=["data_iso"]).sort_values("data_dt")
    
    # Flags de calendário
    df_cal["dia_da_semana_num"] = df_cal["data_dt"].dt.dayofweek  # 0=Segunda, 4=Sexta, 5=Sábado, 6=Domingo
    df_cal["is_fim_de_semana"] = df_cal["dia_da_semana_num"].isin([5, 6])
    df_cal["is_sabado_letivo"] = (df_cal["dia_da_semana_num"] == 5) & (df_cal["evento_tipo"] == "sabado_letivo")
    df_cal["is_dia_letivo"] = (df_cal["status_legal"] == "letivo") | df_cal["is_sabado_letivo"]
    
    # Períodos acadêmicos
    df_cal["ano"] = df_cal["data_dt"].dt.year
    df_cal["mes"] = df_cal["data_dt"].dt.month
    df_cal["semestre"] = np.where(df_cal["mes"] <= 6, 1, 2)
    
    return df_cal

def processar_cardapio():
    print("[*] Processando Cardápio (Bronze -> Silver)...")
    files = sorted(glob.glob(f"{BRONZE_DIR}/cardapio/*.csv"))
    dfs = []
    for f in files:
        # Alguns arquivos podem estar em latin1 ou utf-8
        try:
            df = pd.read_csv(f, sep=";", encoding="utf-8-sig")
        except:
            df = pd.read_csv(f, sep=";", encoding="latin1")
        df = padronizar_data_col(df)
        
        # Mapeamento de colunas
        cols_map = {
            "PRATO_PRINCIPAL": "prato_principal",
            "TIPO_PROTEINA_PRINCIPAL": "proteina_tipo",
            "TIPO_PREPARO_PRINCIPAL": "preparo_tipo",
            "OPCAO_VEGETARIANA": "opcao_vegetariana",
            "GUARNICAO": "guarnicao",
            "SOBREMESA": "sobremesa"
        }
        df = df.rename(columns=cols_map)
        dfs.append(df[["data_dt", "data", "data_iso", "prato_principal", "proteina_tipo", "preparo_tipo", "opcao_vegetariana", "guarnicao", "sobremesa"]])
    
    df_card = pd.concat(dfs, ignore_index=True).drop_duplicates(subset=["data_iso"]).sort_values("data_dt")
    
    # Limpeza textual
    for col in ["prato_principal", "proteina_tipo", "preparo_tipo", "opcao_vegetariana", "guarnicao", "sobremesa"]:
        df_card[col] = df_card[col].astype(str).str.strip().str.lower()
        df_card[col] = df_card[col].replace({"nan": np.nan, "none": np.nan, "": np.nan})
        
    return df_card

def processar_clima():
    print("[*] Processando Dados Meteorológicos (Bronze -> Silver)...")
    f_hist = f"{BRONZE_DIR}/clima/clima_historico_itaquaquecetuba.csv"
    if not os.path.exists(f_hist):
        raise FileNotFoundError(f"Arquivo de clima histórico não encontrado em {f_hist}")
        
    df_clima = pd.read_csv(f_hist, sep=";", encoding="utf-8-sig")
    df_clima = padronizar_data_col(df_clima)
    
    # Flags climáticas de impacto humano
    df_clima["flag_chuva_forte"] = df_clima["precipitation_sum"] >= 10.0
    df_clima["flag_chuva_persistente"] = df_clima["precipitation_hours"] >= 6.0
    df_clima["flag_dia_frio"] = df_clima["temperature_2m_max"] <= 18.0
    df_clima["flag_dia_muito_quente"] = df_clima["temperature_2m_max"] >= 30.0
    df_clima["flag_vento_forte"] = df_clima["wind_speed_10m_max"] >= 20.0
    
    return df_clima

def processar_consumo():
    print("[*] Processando Consumo Histórico (Bronze -> Silver)...")
    files = sorted(glob.glob(f"{BRONZE_DIR}/consumo/*.csv"))
    dfs = []
    
    # Ordenamos arquivos para garantir que arquivos mais específicos (ex: set/out) sobreponham ou complementem
    for f in files:
        df = pd.read_csv(f, sep=";", encoding="utf-8-sig")
        df = padronizar_data_col(df)
        valid = df[df["consumo"].notna()].copy()
        valid["arquivo_origem"] = os.path.basename(f)
        dfs.append(valid[["data_dt", "data", "data_iso", "consumo", "status_dado", "observacao", "arquivo_origem"]])
        
    df_cons = pd.concat(dfs, ignore_index=True)
    # Em caso de mesma data, prioriza registros com status_dado atípico ou observação detalhada
    df_cons["_peso_prioridade"] = 0
    df_cons.loc[df_cons["observacao"].notna() & (df_cons["observacao"] != ""), "_peso_prioridade"] += 1
    df_cons.loc[df_cons["status_dado"].astype(str).str.strip().str.lower().isin(["atipico", "atípico"]), "_peso_prioridade"] += 2
    df_cons = df_cons.sort_values(by=["data_dt", "_peso_prioridade"]).drop_duplicates(subset=["data_iso"], keep="last").drop(columns=["_peso_prioridade"])
    return df_cons

def processar_reservas():
    print("[*] Processando Reservas e Estimativas (Bronze -> Silver)...")
    files = sorted(glob.glob(f"{BRONZE_DIR}/reservas/*.csv"))
    dfs = []
    for f in files:
        df = pd.read_csv(f, sep=";", encoding="utf-8-sig")
        df = padronizar_data_col(df)
        valid = df[df["reservas"].notna()].copy()
        
        # Regime: 2023-2025 = reserva direta de alunos; 2026+ = estimativa da nutricionista
        ano = int(os.path.basename(f).replace("reservas_", "").replace(".csv", ""))
        valid["regime_reserva"] = "aluno_manifestacao" if ano < 2026 else "nutricionista_estimativa"
        
        dfs.append(valid[["data_dt", "data", "data_iso", "reservas", "regime_reserva"]])
        
    df_res = pd.concat(dfs, ignore_index=True).drop_duplicates(subset=["data_iso"]).sort_values("data_dt")
    return df_res

def consolidar_silver_fato_diaria(df_cal, df_card, df_clima, df_cons, df_res):
    print("[*] Construindo Tabela Fato Diária Integrada com Auditoria de Qualidade...")
    
    # Grão mestre: base completa do calendário acadêmico
    m = df_cal.copy()
    
    # Merges
    m = pd.merge(m, df_card.drop(columns=["data", "data_dt"]), on="data_iso", how="left")
    m = pd.merge(m, df_clima.drop(columns=["data", "data_dt", "dia_da_semana"]), on="data_iso", how="left")
    m = pd.merge(m, df_cons.drop(columns=["data", "data_dt"]), on="data_iso", how="left")
    m = pd.merge(m, df_res.drop(columns=["data", "data_dt"]), on="data_iso", how="left")
    
    # Divergência e Razão
    m["diff_consumo_reserva"] = m["consumo"] - m["reservas"]
    m["taxa_comparecimento"] = np.where(m["reservas"] > 0, m["consumo"] / m["reservas"], np.nan)
    
    # -------------------------------------------------------------
    # REGRAS DE AUDITORIA E QUALIDADE DE DADOS (DATA QUALITY FLAGS)
    # -------------------------------------------------------------
    # Flag: Dias Atípicos Identificados na Origem (Bronze) ou em Observações
    m["flag_atipico"] = (
        m["status_dado"].astype(str).str.strip().str.lower().isin(["atipico", "atípico"]) |
        m["observacao"].fillna("").str.lower().str.contains(r"at[ií]pico", regex=True)
    )
    
    # 1. Flag: Consumo Quase Nulo em Dia Letivo (Suspeita de Dispensa / Apagão / Interrupção)
    m["flag_consumo_anormal_baixo"] = (m["is_dia_letivo"] == True) & (m["consumo"].notna()) & (m["consumo"] < 40.0)
    
    # 2. Flag: Eventos Severos Documentados (Greve ou Enchentes/Alagamentos/Atípicos)
    obs_lower = m["observacao"].fillna("").str.lower()
    m["flag_greve"] = m["evento_tipo"].fillna("").str.contains("greve", case=False)
    m["flag_evento_severo"] = (
        obs_lower.str.contains("chuva|enchente|suspens|sem aula", regex=True) |
        m["flag_greve"] |
        m["flag_atipico"]
    )
    
    # 3. Flag: Subnotificação Crônica de Alunos (Consumo muito maior que a reserva)
    m["flag_subnotificacao_reserva"] = (m["regime_reserva"] == "aluno_manifestacao") & (m["diff_consumo_reserva"] > 60.0)
    
    # 4. Flag: Superestimativa Excessiva da Nutricionista
    m["flag_superestimativa_alta"] = (m["regime_reserva"] == "nutricionista_estimativa") & (m["diff_consumo_reserva"] < -60.0)
    
    # 5. Classificação Final de Qualidade do Registro
    def classificar_qualidade(row):
        if not row["is_dia_letivo"]:
            return "NAO_LETIVO"
        if pd.isna(row["consumo"]):
            return "SEM_CONSUMO_REGISTRADO"
        if row["flag_atipico"] or row["flag_evento_severo"]:
            return "EVENTO_EXTREMO_EXTERNO"
        if row["flag_consumo_anormal_baixo"]:
            return "ANOMALIA_DISPENSA_OPERACIONAL"
        if row["flag_subnotificacao_reserva"]:
            return "SUBNOTIFICACAO_CRONICA_ALUNO"
        return "REGULAR"
        
    m["status_qualidade_registro"] = m.apply(classificar_qualidade, axis=1)
    
    # Reordenar colunas com chave temporal primeiro
    first_cols = [
        "data", "data_iso", "dia_da_semana", "ano", "mes", "semestre",
        "is_dia_letivo", "is_fim_de_semana", "is_sabado_letivo", "status_legal", "evento_tipo",
        "consumo", "status_dado", "reservas", "regime_reserva", "diff_consumo_reserva", "taxa_comparecimento",
        "status_qualidade_registro", "flag_greve", "flag_atipico", "flag_consumo_anormal_baixo", "flag_evento_severo",
        "prato_principal", "proteina_tipo", "preparo_tipo", "guarnicao", "sobremesa",
        "precipitation_sum", "precipitation_hours", "temperature_2m_max", "temperature_2m_min", "wind_speed_10m_max",
        "flag_chuva_forte", "observacao"
    ]
    other_cols = [c for c in m.columns if c not in first_cols and c != "data_dt"]
    m = m[first_cols + other_cols].sort_values("data_iso").reset_index(drop=True)
    
    return m

def salvar_camada_silver():
    os.makedirs(SILVER_DIR, exist_ok=True)
    
    df_cal = processar_calendario()
    df_card = processar_cardapio()
    df_clima = processar_clima()
    df_cons = processar_consumo()
    df_res = processar_reservas()
    
    df_fato = consolidar_silver_fato_diaria(df_cal, df_card, df_clima, df_cons, df_res)
    
    # Salvar em Parquet e CSV
    datasets = {
        "silver_calendario": df_cal.drop(columns=["data_dt"]),
        "silver_cardapio": df_card.drop(columns=["data_dt"]),
        "silver_clima": df_clima.drop(columns=["data_dt"]),
        "silver_consumo": df_cons.drop(columns=["data_dt"]),
        "silver_reservas": df_res.drop(columns=["data_dt"]),
        "silver_fato_diaria": df_fato
    }
    
    print("\n[+] Salvando datasets da Camada Silver:")
    for name, df in datasets.items():
        p_parquet = f"{SILVER_DIR}/{name}.parquet"
        p_csv = f"{SILVER_DIR}/{name}.csv"
        df.to_parquet(p_parquet, index=False)
        df.to_csv(p_csv, sep=";", index=False, encoding="utf-8-sig")
        print(f"  [OK] {name}: {len(df)} linhas -> {p_parquet} e {p_csv}")
        
    print("\n[OK] Camada Silver processada com sucesso!")
    return df_fato

if __name__ == "__main__":
    salvar_camada_silver()
