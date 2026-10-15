import pandas as pd
import numpy as np
import glob
import os

# Procurar base gold consolidada
gold_files = glob.glob(r'f:\PROJETOS\ARTEFATO\dados\gold\*.parquet') + glob.glob(r'f:\PROJETOS\ARTEFATO\dados\gold\*.csv')
print("Arquivos em dados/gold:")
for f in gold_files:
    print(f"  {f}")

# Se houver base gold, ler e calcular médias
df_gold = None
for f in gold_files:
    if 'consumo' in f.lower() or 'refeicoes' in f.lower() or 'base' in f.lower():
        df_gold = pd.read_parquet(f) if f.endswith('.parquet') else pd.read_csv(f)
        print(f"Lida base: {f} com shape {df_gold.shape}")
        break

if df_gold is None and len(gold_files) > 0:
    df_gold = pd.read_parquet(gold_files[0]) if gold_files[0].endswith('.parquet') else pd.read_csv(gold_files[0])
    print(f"Lida base: {gold_files[0]} com shape {df_gold.shape}")

if df_gold is not None:
    print("\nColunas da base:", df_gold.columns.tolist()[:25])
    # 1. Média por dia da semana
    if 'dia_semana' in df_gold.columns and 'consumo' in df_gold.columns:
        print("\nMédia de consumo por dia da semana (toda a base):")
        print(df_gold.groupby('dia_semana')['consumo'].agg(['count', 'mean']))
    
    # 2. Média por ano
    if 'ano' in df_gold.columns and 'consumo' in df_gold.columns:
        print("\nMédia de consumo por ano:")
        print(df_gold.groupby('ano')['consumo'].agg(['count', 'mean']))
