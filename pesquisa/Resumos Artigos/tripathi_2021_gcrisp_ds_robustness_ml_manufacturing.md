# Resumo de Artigo Externo: Tripathi et al. (2021) — GCRISP-DS: Robustez em Modelos de ML

## Referência Completa
**Autores:** Tripathi, S.; Muhr, D.; Brunner, M.; Jodlbauer, H.; Dehmer, M.; Emmert-Streib, F.
**Título:** Ensuring the Robustness and Reliability of Data-Driven Knowledge Discovery Models in Production and Manufacturing.
**Ano:** 2021
**Journal:** Frontiers in Artificial Intelligence, Vol. 4, Art. 576892.
**DOI:** [10.3389/frai.2021.576892](https://doi.org/10.3389/frai.2021.576892)
**Caminho Local:** `d:\PROJETOS\PRODUTO_MESTRADO\docs\artigos\Artigos Encontrados\frai-04-576892.pdf`

## Resumo
Artigo de revisão metodológica focado na robustez e confiabilidade de modelos de *Machine Learning* aplicados à produção e manufatura. Os autores revisam criticamente o framework **CRISP-DM** (Cross-Industry Standard Process for Data Mining) e propõem a sua evolução: o **GCRISP-DS** (Generalized CRISP-DS), que inclui interações dinâmicas entre fases, validações iterativas de qualidade de dados e garantias de generalização do modelo.

## Principais Tópicos
- **CRISP-DM → GCRISP-DS:** A proposta responde a limitações reais do CRISP-DM original: ele é muito linear e não prevê retornos iterativos quando problemas de qualidade de dados ou overfitting são detectados entre fases.
- **Robustez como Meta Central:** O artigo define "robustez" como a capacidade de um modelo de MA manter desempenho estável frente a variações nos dados de entrada — um critério central ao avaliar modelos treinados no seu dataset do RU.
- **Modelo Baseado em Dados:** Detalha o pipeline completo de descoberta de conhecimento — muito similar ao seu pipeline nos Notebooks 00 ao 07 — validando cada etapa como necessária para garantir a confiabilidade do sistema preditivo.

## Pertinência para o Projeto
**Alta (Fundamentação Metodológica).** É o artigo que justifica, no capítulo de Metodologia da sua Dissertação, por que o seu pipeline de ML segue um método científico rigoroso e robusto. O conceito de GCRISP-DS valida formalmente a sua abordagem iterativa de desenvolvimento de modelos (CRISP-ML(Q) no caso do seu projeto), e o foco em "robustez" explica por que você compara múltiplos algoritmos antes de escolher o modelo final. Já é citado no seu relato SINGEP 2025 (Tripathi et al., 2021).
