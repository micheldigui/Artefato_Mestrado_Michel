import pandas as pd
import numpy as np

df = pd.read_parquet(r'f:\PROJETOS\ARTEFATO\dados\gold\gold_dataset_ml_limpo.parquet')

print("=== 1. MÉDIA POR DIA DA SEMANA ===")
# Filtrar dias letivos normais
df_dias = df[df['is_dia_letivo'] == 1]
print(df_dias.groupby('dia_da_semana')['consumo'].agg(['count', 'mean']))

# Média 2023-2025 (triênio)
df_trienio = df_dias[df_dias['ano'] <= 2025]
print("\nMédia dia da semana (2023-2025):")
print(df_trienio.groupby('dia_da_semana')['consumo'].agg(['count', 'mean']))

print("\n=== 2. MÉDIA POR PROTEÍNA (2023-2025) ===")
if 'proteina_tipo' in df.columns:
    print(df_trienio.groupby('proteina_tipo')['consumo'].agg(['count', 'mean']))

print("\n=== 3. MÉDIA POR PREPARO (2023-2025) ===")
if 'preparo_tipo' in df.columns:
    print(df_trienio.groupby('preparo_tipo')['consumo'].agg(['count', 'mean']))

print("\n=== 4. MÉTRICAS DOS MODELOS (metricas_modelos_cenarios.csv) ===")
df_metr = pd.read_csv(r'f:\PROJETOS\ARTEFATO\dados\gold\metricas_modelos_cenarios.csv')
print(df_metr.to_string())
