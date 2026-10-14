"""
Módulo de Armazenamento e Gestão de Dados Operacionais
Garante que os arquivos históricos permaneçam imutáveis e armazena novos registros
em 'dados/producao/'.
"""

import os
import pandas as pd
import numpy as np
from datetime import datetime

PRODUCAO_DIR = "dados/producao"
SILVER_CONSUMO = "dados/silver/silver_consumo.parquet"
SILVER_FATO = "dados/silver/silver_fato_diaria.parquet"
NOVOS_CONSUMOS = f"{PRODUCAO_DIR}/novos_consumos.parquet"
PLANEJAMENTO_NUTRI = f"{PRODUCAO_DIR}/planejamento_nutri.parquet"
PREDICOES_HISTORICO = f"{PRODUCAO_DIR}/historico_predicoes.parquet"
CSV_CONSUMO_ATUALIZADO = f"{PRODUCAO_DIR}/consumo_diario_atualizado.csv"

os.makedirs(PRODUCAO_DIR, exist_ok=True)

def carregar_historico_consumo():
    """Carrega o histórico base de consumo e junta com novos lançamentos operacionais."""
    if os.path.exists(SILVER_CONSUMO):
        df_hist = pd.read_parquet(SILVER_CONSUMO)[["data", "data_iso", "consumo"]].copy()
        df_hist["data_dt"] = pd.to_datetime(df_hist["data_iso"])
    else:
        df_hist = pd.DataFrame(columns=["data_dt", "data", "data_iso", "consumo"])
    
    if os.path.exists(NOVOS_CONSUMOS):
        df_novos = pd.read_parquet(NOVOS_CONSUMOS)
        if "data_dt" not in df_novos.columns and "data_iso" in df_novos.columns:
            df_novos["data_dt"] = pd.to_datetime(df_novos["data_iso"])
        df_combinado = pd.concat([df_hist, df_novos], ignore_index=True)
        df_combinado = df_combinado.drop_duplicates(subset=["data_iso"], keep="last").sort_values("data_dt").reset_index(drop=True)
        return df_combinado
    return df_hist.sort_values("data_dt").reset_index(drop=True)

def consultar_consumo_por_data(data_str):
    """
    Retorna o valor de consumo registrado para a data especificada ('YYYY-MM-DD' ou 'DD/MM/YYYY').
    Retorna None se a data não possuir registro no histórico.
    """
    df_hist = carregar_historico_consumo()
    dt = pd.to_datetime(data_str)
    data_iso = dt.strftime("%Y-%m-%d")
    reg = df_hist[df_hist["data_iso"] == data_iso]
    if not reg.empty:
        return float(reg.iloc[-1]["consumo"])
    return None

def salvar_consumo_diario(data_str, consumo_val):
    """
    Salva ou atualiza o consumo real apurado em uma data específica.
    data_str: 'YYYY-MM-DD' ou 'DD/MM/YYYY'
    consumo_val: int/float
    Sincroniza automaticamente a base Parquet e o arquivo CSV em 'dados/producao/'.
    """
    dt = pd.to_datetime(data_str)
    data_iso = dt.strftime("%Y-%m-%d")
    data_formatada = dt.strftime("%d/%m/%Y")
    
    novo_reg = pd.DataFrame([{
        "data_dt": dt,
        "data": data_formatada,
        "data_iso": data_iso,
        "consumo": float(consumo_val)
    }])
    
    if os.path.exists(NOVOS_CONSUMOS):
        df_novos = pd.read_parquet(NOVOS_CONSUMOS)
        df_novos = pd.concat([df_novos, novo_reg], ignore_index=True).drop_duplicates(subset=["data_iso"], keep="last")
    else:
        df_novos = novo_reg
    
    df_novos.to_parquet(NOVOS_CONSUMOS, index=False)
    
    # Atualiza o arquivo CSV sincronizado com todo o histórico consolidado
    df_completo = carregar_historico_consumo()
    df_completo[["data", "data_iso", "consumo"]].to_csv(CSV_CONSUMO_ATUALIZADO, index=False, encoding="utf-8-sig")
    
    return True

def carregar_planejamento_nutricionista():
    """Retorna o histórico de planejamento semanal inserido pela nutricionista."""
    if os.path.exists(PLANEJAMENTO_NUTRI):
        return pd.read_parquet(PLANEJAMENTO_NUTRI).sort_values("data_iso").reset_index(drop=True)
    return pd.DataFrame(columns=["data_iso", "data", "dia_semana", "prato_principal", "proteina_tipo", "preparo_tipo", "planejado_nutri"])

def salvar_planejamento_semanal(df_semana):
    """
    Salva ou atualiza a grade de planejamento semanal (segunda a sexta).
    df_semana deve conter colunas: data_iso, data, dia_semana, prato_principal, proteina_tipo, preparo_tipo, planejado_nutri
    """
    if os.path.exists(PLANEJAMENTO_NUTRI):
        df_atual = pd.read_parquet(PLANEJAMENTO_NUTRI)
        df_unificado = pd.concat([df_atual, df_semana], ignore_index=True).drop_duplicates(subset=["data_iso"], keep="last")
    else:
        df_unificado = df_semana
    
    df_unificado.to_parquet(PLANEJAMENTO_NUTRI, index=False)
    return True

def salvar_predicoes_geradas(df_predicoes):
    """Armazena o histórico das previsões operacionais emitidas pelo artefato."""
    df_predicoes["timestamp_execucao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(PREDICOES_HISTORICO):
        df_hist = pd.read_parquet(PREDICOES_HISTORICO)
        df_final = pd.concat([df_hist, df_predicoes], ignore_index=True)
    else:
        df_final = df_predicoes
    df_final.to_parquet(PREDICOES_HISTORICO, index=False)
    return True
