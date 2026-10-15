# INVENTÁRIO DE SINCRONIZAÇÃO E AUDITORIA DO ARTEFATO
## Marco Temporal Estrito: Qualificação até 31/08/2026

Este inventário formal registra o mapeamento de todos os notebooks, scripts, figuras, tabelas e parágrafos textuais da dissertação que foram auditados e necessitam de sincronização com o documento pericial [`dissertacao/AUDITORIA_QUALIFICACAO_RECALCULO_N73.md`](file:///f:/PROJETOS/ARTEFATO/dissertacao/AUDITORIA_QUALIFICACAO_RECALCULO_N73.md).

**Local do Backup de Segurança Prévio:** `f:\PROJETOS\ARTEFATO\dissertacao\backup_antes_sincronizacao_20261014/`

---

## 1. INVENTÁRIO DE SCRIPTS E NOTEBOOKS AFETADOS

| Caminho do Arquivo | Finalidade Original | Problema Identificado na Auditoria | Ação de Sincronização / Substituto |
| :--- | :--- | :--- | :--- |
| `src/gerar_todas_figuras_dissertacao.py` | Gera todas as 28 figuras da dissertação em `dissertacao/figuras/`. | Usava listas hardcoded na Figura 15 (+0,142 na temperatura); usava N=140 e N=83 nas Figuras 16, 20 e 24; limites de eixos geravam sobreposições em 12.410 e 4.524. | Sincronizar todas as funções para ler diretamente as bases com corte em 31/08/2026 ($N=73, 123, 458, 568$), calcular Figura 15 dinamicamente da Gold, expandir eixos e posicionar legendas sem sobreposição. |
| `notebooks/10_geracao_figuras_dissertacao.ipynb` | Caderno executável oficial que aciona a geração das 28 figuras da dissertação. | Saídas antigas com coorte N=83/140 e listas desatualizadas de geração. | Atualizar células com a nova chamada de geração sincronizada, executar de ponta a ponta e limpar saídas legadas. |
| `notebooks/04_camada_gold_engenharia_features.ipynb` | Engenharia de atributos, Feature Store e correlação de atributos. | Mantinha registros posteriores a 31/08/2026 na análise exploratória geral da Gold ($N=588$). | Atualizar filtro para o corte de qualificação ($N=568$ até 31/08/2026) e sincronizar correlação linear. |
| `notebooks/08_margem_seguranca_e_modelo_hibrido.ipynb` | Modelagem da fronteira de Pareto híbrida, conformal prediction e Monte Carlo. | Continha dados de setembro ($N=83$). | Sincronizar para a coorte pareada de qualificação ($N=73$), salvando previsões em `previsoes_diarias_2026_monte_carlo_n73.csv`. |
| `notebooks/09_analise_efeito_compensatorio_e_regimes.ipynb` | Decomposição do efeito compensatório e balanço histórico de sobras e faltas. | Usava N=140 na Nutricionista e N=83 no Híbrido. | Sincronizar para os recortes auditados ($N=458$ em 2023–25; $N=123$ na Nutricionista; $N=73$ no Híbrido). |

---

## 2. INVENTÁRIO DE FIGURAS AFETADAS NA DISSERTAÇÃO (CAPÍTULO 5)

| Número no DOCX | Legenda Oficial no DOCX | Arquivo Ativo Anterior | Arquivo Substituto Vigente | Recorte Amostral e Ajuste Realizado |
| :---: | :--- | :--- | :--- | :--- |
| **Fig 8** | Perfil semanal por ano letivo | `figura_08_perfil_semanal_por_ano_letivo.png` | `figura_08_perfil_semanal_por_ano_letivo_corrigida.png` | Ano 2026 truncado em 31/08/2026 ($N=123$ datas letivas, média 167,2 ref.). |
| **Fig 11** | Consumo por faixa de precipitação | `figura_11_consumo_por_faixa_precipitacao.png` | `figura_11_consumo_por_faixa_precipitacao.png` (mantida) | Open-Meteo ($N=495$). Imagem mantida; texto P657 ajustado. |
| **Fig 12** | Relação entre temperatura máxima e consumo | `figura_12_relacao_temperatura_maxima_consumo.png` | `figura_12_relacao_temperatura_maxima_consumo.png` (mantida) | Open-Meteo ($N=495$). Reta linear simples ($r=+0,026$). Texto P662 ajustado. |
| **Fig 13** | Funções de autocorrelação temporal | `figura_13_funcoes_autocorrelacao_temporal.png` | `figura_13_funcoes_autocorrelacao_temporal.png` (mantida) | Apenas ACF ($N=495$). Lag 1 = 0,593; Lag 5 = 0,479. Texto P664/P668 ajustado. |
| **Fig 15** | Correlação de atributos com o consumo | `figura_15_correlacao_atributos_consumo_pearson.png` | `figura_15_correlacao_atributos_recalculada_n568.png` | Recalculada dinamicamente da Gold ($N=568$). Temp. Máx = -0,055; Chuva = -0,038. |
| **Fig 16** | Decomposição do efeito compensatório | `figura_16_decomposicao_efeito_compensatorio_atualizada.png` | `figura_16_decomposicao_efeito_compensatorio_corrigida.png` | 3 recortes ($N=458, 123, 73$). Eixo Y até 16.000 e legenda à direita: **12.410** desobstruído. |
| **Fig 17** | Painel anual de sobras e déficits potenciais acumulados (2023 a 2025) | `figura_17_painel_anual_sobras_faltas_atualizada.png` | `figura_17_painel_anual_sobras_faltas_corrigida.png` | Conferido com Tabela 3 ($N=181, 122, 155$). Eixo Y até 5.800 e legenda à esquerda: **4.524** desobstruído. |
| **Fig 18** | Melhor MAE por cenário de informação e horizonte (2026) | `figura_16_melhor_mae_por_cenario_horizonte.png` | `figura_18_melhor_mae_cenarios_recalculada_n73.png` | $N=73$ datas pareadas em todos os 5 cenários, espelhando a Tabela 5. |
| **Fig 19** | Comparação da regressão linear no horizonte t+2, com e sem clima | `figura_17_comparacao_regressao_linear_t2_clima.png` | `figura_19_regressao_linear_t2_com_sem_clima_corrigida.png` | Regressão Linear em $t+2$ com $N=73$: MAE 27,33 vs 25,86 ($R^2$ 0,371 vs 0,394). |
| **Fig 20** | Comparação do MAE entre os horizontes t+2 e t+1 para cinco algoritmos | `figura_18_mae_xgboost_cenario_base_horizonte.png` | `figura_20_comparacao_horizontes_5_algoritmos_corrigida.png` | 5 algoritmos em $t+2$ e $t+1$ com $N=73$ (alinhamento de título e imagem). |
| **Fig 21** | Comparação entre modelos preditivos e nutricionista | `figura_19_comparacao_modelos_vs_nutricionista_t1.png` | `figura_21_ranking_modelos_recalculada_n73.png` | Ranking Top 10 ML + Nutricionista em $N=73$ datas pareadas (inclui XGBoost). |
| **Fig 22** | Sobra e déficit potenciais nas políticas simuladas | `figura_20_sobra_deficit_potenciais_politicas_n83.png` | `figura_22_sobras_faltas_politicas_recalculada_n73.png` | Confronto das 7 políticas operacionais em $N=73$ datas pareadas. |
| **Fig 23** | Fronteira de equilíbrio do modelo híbrido | `figura_21_fronteira_equilibrio_modelo_hibrido.png` | `figura_23_fronteira_hibrido_recalculada_n73.png` | Diferenciação visual de Mínimo Global (20,03) e Operacional 50/50 (20,19) em $N=73$. |
| **Fig 24** | Distribuição estimada dos erros diários de planejamento | `figura_26_distribuicao_erros_diarios_por_regime.png` | `figura_24_distribuicao_erros_diarios_recalculada_n73.png` | Densidade KDE dos resíduos em $N=73$ datas pareadas. |
| **Fig 25** | Efeito das margens de segurança conformal | `figura_22_efeito_margens_seguranca_conformal.png` | `figura_25_margens_seguranca_recalculada_n73.png` | Proteção operacional e sobras para margens P75 a P90 em $N=73$. |
| **Fig 26** | Simulação de faixas de risco operacional | `figura_23_simulacao_faixas_risco_monte_carlo.png` | `figura_26_simulacao_monte_carlo_recalculada_n73.png` | Série Monte Carlo em $N=73$, com teto Y expandido para 295 refeições. |
| **Fig 27** | Custo potencial das sobras e frequência de dias sem déficit potencial | `figura_27_comparativo_custo_sobras_taxa_atendimento.png` | `figura_27_tradeoff_custo_atendimento_recalculada_n73.png` | Trade-off financeiro e de atendimento a R$ 14,00 e R$ 8,50 em $N=73$. |
| **Fig 28** | Comparação histórica consolidada dos períodos e modelos | `figura_28_comparacao_historica_consolidada_periodos_modelos.png` | `figura_28_comparacao_historica_consolidada_recalculada_n73.png` | Painel panorâmico duplo refinado (Proteção e MAE) sem sobreposição ($N=458$ e $N=73$). |

---

## 3. INVENTÁRIO DE TABELAS AFETADAS (CAPÍTULO 5)

| Identificação | Nome / Título | Arquivo CSV Gerado | Período e Amostra | Status e Métricas Auditadas |
| :--- | :--- | :--- | :---: | :--- |
| **Tabela 3** | Balanço histórico anual de reservas discentes (2023–2025) | `dados/silver/silver_fato_diaria.parquet` | 2023 a 2025 ($N=458$) | 2023 (181), 2024 (122), 2025 (155). Sobras = 2.916, Faltas = 9.494, Saldo = -6.578. |
| **Tabela 4** | Quantitativo institucional da nutricionista (2026 até 31/08) | `tabela_4_quantitativo_institucional_2026_recalculada_n123.csv` | 04/02 a 31/08/2026 ($N=123$) | Consumo 167,24, Planejado 182,67, Sobras 2.561, Déficits 663, Saldo +1.898, MAE 26,21. |
| **Tabela 5** | Desempenho dos 5 cenários e horizontes de previsão | `tabela_5_cenarios_horizontes_recalculada_n73.csv` | 19/02 a 31/08/2026 ($N=73$) | Todas as 5 linhas avaliadas estritamente em $N=73$ datas pareadas. |
| **Tabela 6** | Ranking dos 16 modelos supervisionados e benchmark humano | `tabela_6_ranking_modelos_c3_t1_recalculada_n73.csv` | 26/02 a 31/08/2026 ($N=73$) | Ridge em 1º (MAE 21,72); Benchmark Nutricionista MAE 23,37. |
| **Tabela 7** | Comparativo das 7 políticas operacionais e custos | `tabela_7_politicas_margens_recalculada_n73.csv` | 26/02 a 31/08/2026 ($N=73$) | Confronto de sobras, faltas, dias de déficit e custos a R$ 14,00 e R$ 8,50. |
| **Tabela 8** | Síntese histórica e comparativa das alternativas de gestão | `tabela_8_sintese_alternativas_recalculada_n73.csv` | 2023 a 31/08/2026 ($N=458$ e $N=73$) | Confronto integrado dos três paradigmas operacionais. |

---

## 4. INVENTÁRIO DE PARÁGRAFOS TEXTUAIS NO DOCX QUE REQUEREM AJUSTE

| Parágrafo no DOCX | Elemento Vinculado | Problema no Texto Atual | Redação Substituto Auditada |
| :---: | :---: | :--- | :--- |
| **P657** | Figura 11 | Cita 131,2 em vez de 131,4 e omite a faixa de chuva moderada (128,7 ref.). | Inclui as 4 faixas da Open-Meteo: Seco 138,8 ($n=213$), Fraca 131,4 ($n=192$), Moderada 128,7 ($n=58$) e Forte 118,1 ($n=32$). |
| **P662** | Figura 12 | Menciona "ajuste não linear com retração nos extremos", mas a imagem exibe reta linear simples. | Esclarece que o ajuste exibido é uma regressão linear simples com inclinação residual ($r=+0,026$). |
| **P664 / P668** | Figura 13 | P664 cita "ACF e PACF" (imagem só tem ACF). P668 cita r=0,654 no Lag 5 e 0,38 no Lag 1 (valores da matriz Gold tabular). | Ajusta para "Função de autocorrelação simples (ACF)" e cita a ACF temporal da série (Lag 1 = 0,593; Lag 5 = 0,479). |
| **P689** | Figura 15 | Afirma que temperatura máxima exibe "correlação negativa moderada", mas imagem antiga mostrava positiva (+0,142). | Cita as correlações recalculadas da Gold: Lag 5 (+0,64), Sexta (-0,20), Chuva (-0,04) e Temperatura (-0,06). |
| **P705, P710, P718, P721, P722** | Tabela 4 e Figura 16 | Usavam N=140, consumo 167,1, planejado 186,2, saldo +2.670, sobras 3.354, faltas 684, MAE 28,84 e 37,1% dias de déficit. | Sincronizados com o censo até 31/08: $N=123$, consumo 167,24, planejado 182,67, saldo +1.898, sobras 2.561, faltas 663, MAE 26,21 e 39,0% dias déficit. |
| **P748** | Figura 19 | Citava MAE 30,01 e 28,67 ($R^2$ 0,230 e 0,268) em amostra antiga. | Sincronizado para $N=73$: MAE 27,33 vs 25,86 e $R^2$ 0,371 vs 0,394. |
| **P749, P750, P753** | Figura 20 | Anunciava "MAE do XGBoost no cenário-base", mas a imagem continha 5 algoritmos em t+2 vs t+1. | Título e parágrafos retificados para "Comparação do MAE entre os horizontes t+2 e t+1 para cinco algoritmos" em $N=73$. |
| **P788, P792** | Figura 24 | Citava coorte de 83 datas. | Sincronizado para as 73 datas letivas pareadas até 31/08/2026. |
