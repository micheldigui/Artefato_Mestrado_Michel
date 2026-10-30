"""
Módulo de Extração de Dados Meteorológicos (Histórico e Previsão) via API Open-Meteo
Projeto: Artefato de Previsão de Demanda de Refeições
Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)
"""

import os
import requests
import pandas as pd
import numpy as np

from datetime import datetime, date

# Configurações de Localização da Instituição Pública de Ensino (Anonimizado - LGPD)
CAMPUS_CONFIG = {
    "nome": "Instituição Pública de Ensino Federal",
    "latitude": -23.4861,
    "longitude": -46.3483,
    "timezone": "America/Sao_Paulo"
}

def coletar_clima_historico(start_date="2023-01-01", end_date=None):
    """
    Coleta dados meteorológicos históricos diários via Open-Meteo Archive API.
    """
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
        
    print(f"[*] Coletando clima histórico para {CAMPUS_CONFIG['nome']} de {start_date} até {end_date}...")
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": CAMPUS_CONFIG["latitude"],
        "longitude": CAMPUS_CONFIG["longitude"],
        "start_date": start_date,
        "end_date": end_date,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "temperature_2m_mean",
            "apparent_temperature_max",
            "apparent_temperature_min",
            "precipitation_sum",
            "rain_sum",
            "precipitation_hours",
            "wind_speed_10m_max"
        ],
        "timezone": CAMPUS_CONFIG["timezone"]
    }
    
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    
    daily = data["daily"]
    df = pd.DataFrame(daily)
    
    # Padronização de datas
    df["data_iso"] = pd.to_datetime(df["time"]).dt.strftime("%Y-%m-%d")
    df["data"] = pd.to_datetime(df["time"]).dt.strftime("%d/%m/%Y")
    df["dia_da_semana"] = pd.to_datetime(df["time"]).dt.day_name(locale="pt_BR")
    
    # Reordenar colunas
    cols_order = [
        "data", "data_iso", "dia_da_semana",
        "precipitation_sum", "rain_sum", "precipitation_hours",
        "temperature_2m_max", "temperature_2m_min", "temperature_2m_mean",
        "apparent_temperature_max", "apparent_temperature_min",
        "wind_speed_10m_max"
    ]
    df = df[cols_order]
    
    print(f"[+] Histórico coletado com sucesso: {len(df)} registros.")
    return df

def coletar_clima_previsao(forecast_days=16):
    """
    Coleta previsão meteorológica diária para os próximos dias via Open-Meteo Forecast API.
    Atende aos horizontes operacionais t+1 (semana seguinte) e t+2 (semana subsequente).
    """
    print(f"[*] Coletando previsão meteorológica ({forecast_days} dias) para {CAMPUS_CONFIG['nome']}...")
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": CAMPUS_CONFIG["latitude"],
        "longitude": CAMPUS_CONFIG["longitude"],
        "forecast_days": forecast_days,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "temperature_2m_mean",
            "apparent_temperature_max",
            "apparent_temperature_min",
            "precipitation_sum",
            "rain_sum",
            "precipitation_hours",
            "precipitation_probability_max",
            "wind_speed_10m_max"
        ],
        "timezone": CAMPUS_CONFIG["timezone"]
    }
    
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    
    daily = data["daily"]
    df = pd.DataFrame(daily)
    
    # Padronização de datas
    df["data_iso"] = pd.to_datetime(df["time"]).dt.strftime("%Y-%m-%d")
    df["data"] = pd.to_datetime(df["time"]).dt.strftime("%d/%m/%Y")
    df["dia_da_semana"] = pd.to_datetime(df["time"]).dt.day_name(locale="pt_BR")
    
    cols_order = [
        "data", "data_iso", "dia_da_semana",
        "precipitation_probability_max",
        "precipitation_sum", "rain_sum", "precipitation_hours",
        "temperature_2m_max", "temperature_2m_min", "temperature_2m_mean",
        "apparent_temperature_max", "apparent_temperature_min",
        "wind_speed_10m_max"
    ]
    df = df[cols_order]
    
    print(f"[+] Previsão futura coletada com sucesso: {len(df)} dias ({df['data'].iloc[0]} a {df['data'].iloc[-1]}).")
    return df

def salvar_dados():
    os.makedirs("dados/bronze/clima", exist_ok=True)
    
    # 1. Histórico
    df_hist = coletar_clima_historico(start_date="2023-01-01")
    caminho_hist = "dados/bronze/clima/clima_historico_itaquaquecetuba.csv"
    df_hist.to_csv(caminho_hist, sep=";", index=False, encoding="utf-8-sig")
    print(f"[OK] Arquivo salvo: {caminho_hist}")
    
    # 2. Previsão
    df_prev = coletar_clima_previsao(forecast_days=16)
    caminho_prev = "dados/bronze/clima/clima_previsao_16dias.csv"
    df_prev.to_csv(caminho_prev, sep=";", index=False, encoding="utf-8-sig")
    print(f"[OK] Arquivo salvo: {caminho_prev}")
    
    return df_hist, df_prev

if __name__ == "__main__":
    salvar_dados()
