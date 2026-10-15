# Documentação Técnica e Metodológica — Artefato IFSP Itaquaquecetuba

Este diretório (`docs/`) reúne os registros teóricos, bibliográficos e operacionais desenvolvidos para fundamentar o **Artefato Analítico-Preditivo de Demanda de Refeições do IFSP Campus Itaquaquecetuba**, no âmbito do **Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)** do **Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)**.

---

## Estrutura dos Documentos

| Arquivo | Descrição |
| :--- | :--- |
| [`catalogo_referencias_academicas_abnt.md`](file:///f:/PROJETOS/ARTEFATO/docs/catalogo_referencias_academicas_abnt.md) | **Catálogo completo de referências em padrão ABNT (NBR 6023:2018)** com DOIs/links, síntese dos conceitos, transposição exata para o código e textos prontos para citação na dissertação. |
| [`trajetoria_do_artefato.md`](file:///f:/PROJETOS/ARTEFATO/docs/trajetoria_do_artefato.md) | **Memorial metodológico e trajetória evolutiva completa do artefato**, registrando todas as fases, decisões técnicas, marcos de desenvolvimento e resultados consolidados. |
| [`minuta_capitulo_resultados_dissertacao.md`](file:///f:/PROJETOS/ARTEFATO/docs/minuta_capitulo_resultados_dissertacao.md) | **Minuta textual acadêmica completa do Capítulo de Resultados e Discussão**, pronta para inserção direta no Word/LaTeX, referenciando as 8 figuras e 3 tabelas selecionadas. |
| [`referencias_margens_seguranca_e_modelagem.md`](file:///f:/PROJETOS/ARTEFATO/docs/referencias_margens_seguranca_e_modelagem.md) | **Memorial técnico e formulações matemáticas** das 4 abordagens adotadas: Modelo *Newsvendor*, Predição Conformal Não-Paramétrica, Modelo Híbrido Ponderado ($\alpha \cdot \text{IA} + (1-\alpha) \cdot \text{Nutricionista}$) e Simulação Estocástica de Monte Carlo. |



---

## Rastreabilidade com os Cadernos de Experimentos (`notebooks/`)

1. **`notebooks/01_coleta_clima_api.ipynb`**: Extração de variáveis meteorológicas históricas (Open-Meteo).
2. **`notebooks/02_camada_silver_qualidade_dados.ipynb`**: Limpeza, padronização e higienização dos registros de atendimento (2023-2026).
3. **`notebooks/03_analise_exploratoria_eda.ipynb`**: Análise exploratória descritiva e temporal do consumo.
4. **`notebooks/04_camada_gold_engenharia_features.ipynb`**: Criação de defasagens (*lags*), variáveis de calendário e histórico recente.
5. **`notebooks/05_modelagem_cenarios_e_algoritmos.ipynb`**: Treinamento dos modelos em horizontes $t+1$ (perecíveis) e $t+2$ (secos).
6. **`notebooks/06_avaliacao_visual_e_comparativo_modelos.ipynb`**: Confronto de performance e identificação do algoritmo campeão.
7. **`notebooks/07_experimentos_janelas_temporais_e_habitos.ipynb`**: Avaliação de janelas móveis de hábitos de consumo.
8. **`notebooks/08_margem_seguranca_e_modelo_hibrido.ipynb`**: Modelagem de perda assimétrica, calibração da margem conformal, curva de Pareto do modelo híbrido e simulação de Monte Carlo.
9. **`notebooks/09_analise_efeito_compensatorio_e_regimes.ipynb`**: Decomposição minuciosa do efeito compensatório histórico (2023-2026), dispersão e volatilidade dos erros diários, e confronto executivo dos regimes com o artefato técnico.

