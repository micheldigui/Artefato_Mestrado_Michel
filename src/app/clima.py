"""
Módulo de Integração Meteorológica em Tempo Real
Busca a previsão do tempo para os próximos 14 dias nas coordenadas do campus
utilizando a API pública Open-Meteo, com fallback seguro.
"""

import requests
import pandas as pd
import numpy as np

# Coordenadas geográficas da instituição de ensino (Campus Itaquaquecetuba / SP)
LATITUDE = -23.4862
LONGITUDE = -46.3483

def obter_previsao_clima_futura(dias_frente=14):
    """
    Obtém previsões de chuva acumulada (mm) e temperatura máxima (°C) para os próximos N dias.
    Retorna dataframe com colunas: ['data_iso', 'precipitation_sum', 'temperature_2m_max', 'wind_gusts_10m_max']
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "daily": ["precipitation_sum", "temperature_2m_max", "wind_gusts_10m_max"],
        "timezone": "America/Sao_Paulo",
        "forecast_days": min(dias_frente, 16)
    }
    
    try:
        resp = requests.get(url, params=params, timeout=6)
        if resp.status_code == 200:
            data = resp.json()
            daily = data.get("daily", {})
            df_clima = pd.DataFrame({
                "data_iso": daily.get("time", []),
                "precipitation_sum": daily.get("precipitation_sum", []),
                "temperature_2m_max": daily.get("temperature_2m_max", []),
                "wind_gusts_10m_max": daily.get("wind_gusts_10m_max", [])
            })
            # Trata nulos eventuais
            df_clima["precipitation_sum"] = df_clima["precipitation_sum"].fillna(0.0)
            df_clima["temperature_2m_max"] = df_clima["temperature_2m_max"].fillna(24.5)
            df_clima["wind_gusts_10m_max"] = df_clima["wind_gusts_10m_max"].fillna(20.0)
            return df_clima
    except Exception as e:
        print(f"[AVISO] Não foi possível consultar API Open-Meteo ({e}). Utilizando médias sazonais.")
    
    # Fallback seguro com médias históricas do campus
    hoje = pd.Timestamp.now()
    datas_futuras = [(hoje + pd.Timedelta(days=i)).strftime("%Y-%m-%d") for i in range(dias_frente)]
    return pd.DataFrame({
        "data_iso": datas_futuras,
        "precipitation_sum": [2.5] * dias_frente,
        "temperature_2m_max": [24.0] * dias_frente,
        "wind_gusts_10m_max": [18.0] * dias_frente
    })
