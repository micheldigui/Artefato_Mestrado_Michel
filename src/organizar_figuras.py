"""
Script para organizar a pasta reports/figuras em subpastas estruturadas por etapa da pesquisa,
removendo figuras duplicadas e padronizando toda a estrutura para a dissertação.
"""

import os
import shutil

ROOT_FIG = "reports/figuras"

PASTAS = {
    "01_analise_exploratoria": [
        "fig01_serie_temporal_consumo_reservas.png",
        "fig02_decomposicao_anual_medias_moveis.png",
        "fig03_distribuicoes_densidade_anuais.png",
        "fig04_histograma_global_quantis.png",
        "fig05_balanco_anual_falta_sobra.png",
        "fig06_painel_anual_saldo_falta_sobra.png",
        "fig07_dispersao_consumo_reserva_regimes.png",
        "fig08_distribuicao_vies_erro_reserva.png",
        "fig09_discrepancias_severas_outliers.png",
        "fig10_sazonalidade_semanal_por_ano.png",
        "fig11_ciclos_mensais_por_ano.png",
        "fig12_heatmap_dia_semana_mes.png",
        "fig13_consumo_dia_semana_sintese.png",
        "fig14_consumo_por_tipo_evento.png",
        "fig15_taxa_noshow_dia_semana.png",
        "fig16_frequencia_vs_consumo_proteina.png",
        "fig17_consumo_por_tecnica_preparo.png",
        "fig18_ranking_pratos_principais.png",
        "fig19_interacao_proteina_dia_semana.png",
        "fig20_consumo_por_faixa_chuva.png",
        "fig21_duracao_chuva_vento_vs_consumo.png",
        "fig22_temperatura_clima_bivariada.png",
        "fig23_matriz_correlacao_multivariada.png",
        "fig24_sintese_fatores_associacao.png",
        "fig25_autocorrelacao_memoria_temporal.png",
    ],
    "02_engenharia_features": [
        "fig26_ranking_correlacao_features_gold.png",
        "fig27_random_forest_importance.png",
        "fig28_mutual_information_importance.png",
        "fig29_aderencia_lag_mesma_semana.png",
        "fig30_aderencia_media_movel_5d.png",
        "fig31_multicolinearidade_heatmap.png",
        "fig32_atratividade_cardapio_scores.png",
        "fig33_adversidade_climatica_residuos.png",
        "fig34_codificacao_ciclica_calendario.png",
        "fig35_particao_temporal_splits.png",
    ],
    "03_modelagem_cenarios": [
        "fig36_comparativo_mae_rmse_cenarios.png",
        "fig37_comparativo_r2_wape_cenarios.png",
        "fig38_balanco_sobra_falta_modelos.png",
        "fig39_impacto_clima_horizonte_t2.png",
        "fig40_ganho_reforecast_t2_para_t1.png",
        "fig41_evolucao_temporal_regimes_reserva.png",
        "fig42_serie_teste_2026_previsoes_vs_real.png",
        "fig43_distribuicao_erros_residuos.png",
        "fig44_ranking_geral_familias_radar.png",
        "fig45_apoio_decisao_nutricionista.png",
    ],
    "04_top_modelos_confronto": [
        "fig46_top5_comparativo_confronto_reservas.png",
        "fig47_top3_serie_temporal_confronto.png",
        "fig48_top5_balanco_sobra_falta_ordenado.png",
        "fig49_confronto_historico_top_modelos_vs_reservas.png",
    ],
    "05_janelas_temporais_habitos": [
        "fig50_comparativo_janelas_expanding_vs_rolling.png",
        "fig51_evolucao_habito_anual_2024_2025_2026.png",
        "fig52_analise_deriva_habitos_estudantis.png",
    ]
}

# Criar subpastas
for pasta, files in PASTAS.items():
    dir_p = os.path.join(ROOT_FIG, pasta)
    os.makedirs(dir_p, exist_ok=True)
    for f in files:
        src = os.path.join(ROOT_FIG, f)
        dst = os.path.join(dir_p, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copiado: {f} -> {pasta}/")

# Identificar e remover arquivos duplicados/obsoletos na raiz
todas_oficiais = set()
for files in PASTAS.values():
    todas_oficiais.update(files)

arquivos_raiz = [f for f in os.listdir(ROOT_FIG) if os.path.isfile(os.path.join(ROOT_FIG, f))]
for f in arquivos_raiz:
    if f not in todas_oficiais:
        p_remover = os.path.join(ROOT_FIG, f)
        os.remove(p_remover)
        print(f"Removido obsoleto da raiz: {f}")

print("\n[OK] Estrutura de subpastas organizada com sucesso!")
