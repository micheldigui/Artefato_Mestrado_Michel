"""
Módulo de Enriquecimento e Padronização Gastronômica do Cardápio
Projeto: Artefato de Previsão de Demanda de Refeições - IFSP Campus Itaquaquecetuba
Mestrado Profissional

Classifica pratos com proteínas e técnicas de preparo culinário que constavam
como 'nao_especificado' nos registros brutos.
"""

import os
import re
import pandas as pd

BRONZE_CARDAPIO_DIR = "dados/bronze/cardapio"

def normalizar_texto(t):
    if pd.isna(t):
        return ""
    t = str(t).upper().strip()
    t = re.sub(r'[ÁÀÃÂ]', 'A', t)
    t = re.sub(r'[ÉÊ]', 'E', t)
    t = re.sub(r'[Í]', 'I', t)
    t = re.sub(r'[ÓÔÕ]', 'O', t)
    t = re.sub(r'[Ú]', 'U', t)
    t = re.sub(r'[Ç]', 'C', t)
    return t

REGRAS_PREPARO = {
    'SOBRECOXA': 'assado',
    'CUBOS SUINO': 'ao_molho_ou_refogado',
    'CUBOS DE PERNIL': 'ao_molho_ou_refogado',
    'LOMBO EM CUBOS': 'ao_molho_ou_refogado',
    'ROLE': 'ao_molho_ou_refogado',
    'ISCA DE PEIXE': 'empanado_ou_a_milanesa',
    'FILE DE PEIXE': 'assado',
    'PEIXE': 'assado',
    'ROCAMBOLE': 'assado',
    'FILE SUINO': 'grelhado',
    'FILE DE FRANGO': 'grelhado',
    'HAMBURGUER': 'grelhado',
    'BISTECA': 'grelhado',
    'FRANGO CAIPIRA': 'cozido_ou_refogado',
    'CROCANTE': 'empanado_ou_a_milanesa',
    'CASSOULET': 'cremoso_ou_ensopado',
    'COPA LOMBO': 'assado',
    'COSTELINHA': 'assado',
    'DESFIAD': 'ao_molho_ou_refogado',
    'ISCA': 'ao_molho_ou_refogado',
    'VIENENSE': 'assado',
    'KIBE': 'assado',
    'ARRUMADINHO': 'ao_molho_ou_refogado'
}

REGRAS_PROTEINA = {
    'ARRUMADINHO': 'bovina',
    'VIENENSE': 'bovina',
    'KIBE': 'bovina'
}

def enriquecer_cardapios():
    anos = [2023, 2024, 2025, 2026]
    total_modificados_prot = 0
    total_modificados_prep = 0
    
    print("[*] Iniciando enriquecimento das classificações de cardápio...")
    
    for yr in anos:
        fpath = f"{BRONZE_CARDAPIO_DIR}/cardapio_{yr}.csv"
        df = pd.read_csv(fpath, sep=";", encoding="utf-8-sig")
        col_d = [c for c in df.columns if 'data' in c.lower()][0]
        
        mod_prot = 0
        mod_prep = 0
        
        for idx, row in df.iterrows():
            p_norm = normalizar_texto(row['PRATO_PRINCIPAL'])
            
            # 1. Enriquecer proteína
            if pd.isna(row['TIPO_PROTEINA_PRINCIPAL']) or 'nao_especificad' in str(row['TIPO_PROTEINA_PRINCIPAL']).lower():
                for k, v in REGRAS_PROTEINA.items():
                    if k in p_norm:
                        df.at[idx, 'TIPO_PROTEINA_PRINCIPAL'] = v
                        mod_prot += 1
                        break
                        
            # 2. Enriquecer preparo culinário
            if pd.isna(row['TIPO_PREPARO_PRINCIPAL']) or 'nao_especificad' in str(row['TIPO_PREPARO_PRINCIPAL']).lower():
                for k, v in REGRAS_PREPARO.items():
                    if k in p_norm:
                        df.at[idx, 'TIPO_PREPARO_PRINCIPAL'] = v
                        mod_prep += 1
                        break
                        
        df.to_csv(fpath, sep=";", index=False, encoding="utf-8-sig")
        total_modificados_prot += mod_prot
        total_modificados_prep += mod_prep
        print(f"  [OK] {os.path.basename(fpath)}: {mod_prot} proteínas e {mod_prep} técnicas de preparo classificadas!")
        
    print(f"\n[OK] Enriquecimento concluído com sucesso!")
    print(f"     Total de proteínas enriquecidas: {total_modificados_prot}")
    print(f"     Total de preparos enriquecidos: {total_modificados_prep}")

if __name__ == "__main__":
    enriquecer_cardapios()
