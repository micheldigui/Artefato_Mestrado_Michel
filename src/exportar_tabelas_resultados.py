"""
Script de Exportação e Consolidação dos Resultados Operacionais (CSV e Parquet)
Projeto: Artefato de Previsão de Demanda de Refeições — IFSP Campus Itaquaquecetuba
Mestrado Profissional em Educação Profissional e Tecnológica (ProfEPT / Gestão Pública)
"""

import os
import pandas as pd
import numpy as np

# Configurar diretórios de saída
DIR_DADOS_GOLD = "dados/gold/resultados_experimentos"
DIR_REPORTS = "reports/tabelas"

os.makedirs(DIR_DADOS_GOLD, exist_ok=True)
os.makedirs(DIR_REPORTS, exist_ok=True)

print("[INFO] Iniciando consolidação dos resultados dos experimentos...")

# -------------------------------------------------------------
# 1. Carregar Dados de 2026 (Predições Walk-Forward t+1)
# -------------------------------------------------------------
pred_path = "dados/gold/predicoes_detalhadas_walk_forward.parquet"
df_pred = pd.read_parquet(pred_path)
df_t1 = df_pred[df_pred["horizonte"] == "Semana_t1"].copy()

df_ridge = df_t1[(df_t1["algoritmo"] == "Ridge") & (df_t1["cenario"] == "Cenario_3_Com_Nutricionista")][["data_iso", "y_real", "y_pred"]].rename(columns={"y_pred": "pred_ia"})
df_nutri = df_t1[df_t1["algoritmo"] == "Estimativa_Nutricionista_Pura"][["data_iso", "y_pred"]].rename(columns={"y_pred": "reserva_nutri"})
df_2026 = pd.merge(df_ridge, df_nutri, on="data_iso").sort_values("data_iso").reset_index(drop=True)
df_2026["data_dt"] = pd.to_datetime(df_2026["data_iso"])

# -------------------------------------------------------------
# 2. Métricas de Avaliação
# -------------------------------------------------------------
def avaliar_estrategia(y_true, y_pred, nome):
    yt = np.array(y_true)
    yp = np.maximum(0, np.array(y_pred))
    
    sobra = np.sum(np.maximum(0, yp - yt))
    falta = np.sum(np.maximum(0, yt - yp))
    dias_falta = np.sum(yt > yp)
    total_dias = len(yt)
    pct_dias_falta = (dias_falta / total_dias) * 100
    pct_protecao = 100 - pct_dias_falta
    mae = np.mean(np.abs(yt - yp))
    rmse = np.sqrt(np.mean((yt - yp)**2))
    
    # Custo financeiro baseado em R$ 8,50 por refeição
    custo_sobra = sobra * 8.50
    custo_falta_estimado = falta * (8.50 * 2.5) # Custo social/pedagógico ponderado
    
    return {
        "politica": nome,
        "total_dias_avaliados": total_dias,
        "potencial_sobra_refeicoes": int(sobra),
        "potencial_falta_refeicoes": int(falta),
        "total_desvios_refeicoes": int(sobra + falta),
        "dias_com_falta": int(dias_falta),
        "taxa_dias_falta_pct": round(pct_dias_falta, 1),
        "indice_protecao_aluno_pct": round(pct_protecao, 1),
        "mae": round(mae, 2),
        "rmse": round(rmse, 2),
        "custo_desperdicio_sobra_rs": round(custo_sobra, 2),
        "custo_social_falta_rs": round(custo_falta_estimado, 2)
    }

# -------------------------------------------------------------
# 3. Políticas de Decisão e Margens de Segurança
# -------------------------------------------------------------
residuos_positivos = np.maximum(0, df_2026["y_real"] - df_2026["pred_ia"])
delta_p75 = np.percentile(residuos_positivos, 75)
delta_p85 = np.percentile(residuos_positivos, 85)
delta_p90 = np.percentile(residuos_positivos, 90)

politicas = [
    ("1. IA Pura (Ridge)", df_2026["pred_ia"]),
    (f"2. IA + Conformal P75 (+{delta_p75:.0f} ref)", df_2026["pred_ia"] + delta_p75),
    (f"3. IA + Conformal P85 (+{delta_p85:.0f} ref)", df_2026["pred_ia"] + delta_p85),
    (f"4. IA + Conformal P90 (+{delta_p90:.0f} ref)", df_2026["pred_ia"] + delta_p90),
    ("5. Modelo Híbrido Ótimo (50% IA + 50% Nutricionista)", 0.5 * df_2026["pred_ia"] + 0.5 * df_2026["reserva_nutri"]),
    ("6. Modelo Híbrido + Conformal P85 (+12 ref)", 0.5 * df_2026["pred_ia"] + 0.5 * df_2026["reserva_nutri"] + 12),
    ("7. Quantitativo Nutricionista (Benchmark Humano 2026)", df_2026["reserva_nutri"])
]

res_politicas = [avaliar_estrategia(df_2026["y_real"], p[1], p[0]) for p in politicas]
df_tabela_politicas = pd.DataFrame(res_politicas)

# -------------------------------------------------------------
# 4. Fronteira de Pareto (Variação de Alpha)
# -------------------------------------------------------------
alphas = np.linspace(0.0, 1.0, 41)
res_pareto = []

for a in alphas:
    p_hib = a * df_2026["pred_ia"] + (1 - a) * df_2026["reserva_nutri"]
    met = avaliar_estrategia(df_2026["y_real"], p_hib, f"Alpha_{a:.3f}")
    met["alpha"] = round(a, 3)
    met["pct_ia"] = round(a * 100, 1)
    met["pct_nutricionista"] = round((1 - a) * 100, 1)
    res_pareto.append(met)

df_tabela_pareto = pd.DataFrame(res_pareto)

# -------------------------------------------------------------
# 5. Simulação de Monte Carlo Diária (2026)
# -------------------------------------------------------------
np.random.seed(42)
N_SIM = 1000
residuos_modelo = df_2026["y_real"] - df_2026["pred_ia"]
simulacoes = np.zeros((len(df_2026), N_SIM))

for i, y_base in enumerate(df_2026["pred_ia"]):
    erros = np.random.choice(residuos_modelo, size=N_SIM, replace=True)
    simulacoes[i, :] = np.maximum(0, y_base + erros)

df_previsoes_detalhadas = df_2026.copy()
df_previsoes_detalhadas["pred_ia_conformal_p85"] = np.round(df_2026["pred_ia"] + delta_p85, 1)
df_previsoes_detalhadas["pred_hibrido_50_50"] = np.round(0.5 * df_2026["pred_ia"] + 0.5 * df_2026["reserva_nutri"], 1)
df_previsoes_detalhadas["mc_p10_minimo"] = np.round(np.percentile(simulacoes, 10, axis=1), 1)
df_previsoes_detalhadas["mc_p50_mediana"] = np.round(np.percentile(simulacoes, 50, axis=1), 1)
df_previsoes_detalhadas["mc_p80_prudencial"] = np.round(np.percentile(simulacoes, 80, axis=1), 1)
df_previsoes_detalhadas["mc_p95_teto_seguranca"] = np.round(np.percentile(simulacoes, 95, axis=1), 1)

# Desvios operacionais da nutricionista vs IA
df_previsoes_detalhadas["sobra_ia_pura"] = np.maximum(0, df_previsoes_detalhadas["pred_ia"] - df_previsoes_detalhadas["y_real"])
df_previsoes_detalhadas["falta_ia_pura"] = np.maximum(0, df_previsoes_detalhadas["y_real"] - df_previsoes_detalhadas["pred_ia"])
df_previsoes_detalhadas["sobra_nutricionista"] = np.maximum(0, df_previsoes_detalhadas["reserva_nutri"] - df_previsoes_detalhadas["y_real"])
df_previsoes_detalhadas["falta_nutricionista"] = np.maximum(0, df_previsoes_detalhadas["y_real"] - df_previsoes_detalhadas["reserva_nutri"])
df_previsoes_detalhadas["sobra_hibrido"] = np.maximum(0, df_previsoes_detalhadas["pred_hibrido_50_50"] - df_previsoes_detalhadas["y_real"])
df_previsoes_detalhadas["falta_hibrido"] = np.maximum(0, df_previsoes_detalhadas["y_real"] - df_previsoes_detalhadas["pred_hibrido_50_50"])

# -------------------------------------------------------------
# 6. Comparativo Histórico: Alunos (2023-2025) vs Nutricionista (2026) vs IA
# -------------------------------------------------------------
df_fato = pd.read_parquet("dados/silver/silver_fato_diaria.parquet")
df_alunos = df_fato[df_fato["regime_reserva"] == "aluno_manifestacao"].dropna(subset=["consumo", "reservas"]).copy()

met_alunos = avaliar_estrategia(df_alunos["consumo"], df_alunos["reservas"], "Reserva dos Alunos (2023-2025)")
met_nutri = avaliar_estrategia(df_2026["y_real"], df_2026["reserva_nutri"], "Quantitativo Nutricionista (2026)")
met_ia_pura = avaliar_estrategia(df_2026["y_real"], df_2026["pred_ia"], "IA Pura - Ridge t+1 (2026)")
met_hibrido = avaliar_estrategia(df_2026["y_real"], 0.5 * df_2026["pred_ia"] + 0.5 * df_2026["reserva_nutri"], "Modelo Híbrido 50/50 (2026)")
met_conformal85 = avaliar_estrategia(df_2026["y_real"], df_2026["pred_ia"] + delta_p85, "IA + Conformal P85 (2026)")

df_comparativo_regimes = pd.DataFrame([met_alunos, met_nutri, met_ia_pura, met_hibrido, met_conformal85])

# -------------------------------------------------------------
# 7. Salvar Tabelas em CSV e Parquet nos dois diretórios
# -------------------------------------------------------------
tabelas = {
    "comparativo_politicas_margens_seguranca": df_tabela_politicas,
    "fronteira_pareto_modelo_hibrido": df_tabela_pareto,
    "previsoes_diarias_2026_monte_carlo": df_previsoes_detalhadas,
    "comparativo_regimes_alunos_nutricionista_ia": df_comparativo_regimes
}

for nome, df_obj in tabelas.items():
    # Salvar em gold
    path_gold_csv = f"{DIR_DADOS_GOLD}/{nome}.csv"
    path_gold_parquet = f"{DIR_DADOS_GOLD}/{nome}.parquet"
    df_obj.to_csv(path_gold_csv, index=False, encoding="utf-8-sig")
    df_obj.to_parquet(path_gold_parquet, index=False)
    
    # Salvar em reports/tabelas
    path_rep_csv = f"{DIR_REPORTS}/{nome}.csv"
    path_rep_parquet = f"{DIR_REPORTS}/{nome}.parquet"
    df_obj.to_csv(path_rep_csv, index=False, encoding="utf-8-sig")
    df_obj.to_parquet(path_rep_parquet, index=False)
    
    print(f"[OK] {nome} salvo em CSV e Parquet (Gold e Reports).")

print("\n=== RESUMO DAS POLÍTICAS DE MARGEM DE SEGURANÇA ===")
print(df_tabela_politicas[["politica", "potencial_sobra_refeicoes", "potencial_falta_refeicoes", "taxa_dias_falta_pct", "custo_desperdicio_sobra_rs"]].to_string(index=False))

print("\n=== COMPARATIVO DOS REGIMES (ALUNOS vs NUTRICIONISTA vs IA) ===")
print(df_comparativo_regimes[["politica", "total_dias_avaliados", "potencial_sobra_refeicoes", "potencial_falta_refeicoes", "taxa_dias_falta_pct", "mae"]].to_string(index=False))
