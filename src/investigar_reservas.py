import pandas as pd
import numpy as np

df = pd.read_parquet('dados/gold/gold_dataset_ml_limpo.parquet')
print('Colunas no dataset:', len(df.columns))
print('Anos no dataset:', df['ano'].value_counts().to_dict())

for ano in [2023, 2024, 2025, 2026]:
    sub = df[df['ano'] == ano]
    mae_res = (sub['consumo'] - sub['reservas']).abs().mean()
    bias_res = (sub['reservas'] - sub['consumo']).mean()
    corr = sub['consumo'].corr(sub['reservas'])
    sobra = np.sum(np.maximum(0, sub['reservas'] - sub['consumo']))
    falta = np.sum(np.maximum(0, sub['consumo'] - sub['reservas']))
    print(f"Ano {ano}: N={len(sub)}, Consumo Medio={sub['consumo'].mean():.1f}, Reservas Medio={sub['reservas'].mean():.1f}, Bias={bias_res:.1f}, MAE={mae_res:.1f}, Corr={corr:.3f}, Sobra={sobra:.0f}, Falta={falta:.0f}")
