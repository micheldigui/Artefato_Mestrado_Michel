import os
import pandas as pd
import glob

print("=== TABELAS EM reports/dissertacao_selecao/tabelas ===")
for f in glob.glob(r'f:\PROJETOS\ARTEFATO\reports\dissertacao_selecao\tabelas\*.csv'):
    print(f"\n--- {os.path.basename(f)} ---")
    df = pd.read_csv(f)
    print(df.to_string())

print("\n=== TABELAS EM reports/tabelas ===")
for f in glob.glob(r'f:\PROJETOS\ARTEFATO\reports\tabelas\*.csv'):
    print(f"\n--- {os.path.basename(f)} ---")
    df = pd.read_csv(f)
    print(df.to_string())
