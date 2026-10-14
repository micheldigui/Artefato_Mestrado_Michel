# Resumo de Produção Própria: Souza et al. (2025) — SINGEP-CIK

## Referência Completa
**Autores:** Souza, M. S.; Arima, C. H.; Orsi, R. N.
**Título:** Gestão de Suprimentos em Sistemas Produtivos: Uma Abordagem Preditiva com Ciência de Dados e Inteligência Artificial.
**Ano:** 2025
**Evento:** XIII SINGEP-CIK – UNINOVE – São Paulo/SP – 22 a 24 de outubro de 2025.
**Caminho Local:** `d:\PROJETOS\PRODUTO_MESTRADO\docs\artigos\Meus Artigos\Relato-Tecnico_2025_SINGEP_CN.pdf`

## Resumo
Artigo de versão mais madura e completa do projeto de Dissertação, apresentado no SINGEP 2025. Aqui o foco muda do EDA (SIMPROF) para a **apresentação do produto tecnológico completo**: o sistema preditivo end-to-end implantado na cadeia de suprimentos do RU. O artigo detalha a situação-problema central (planejamento reativo de sexta-feira com apenas 3 dias de antecedência), a metodologia de construção do modelo e os seus resultados, incluindo a arquitetura **híbrida residual** com Ensemble Learning (Ridge + ExtraTrees + Voting + Stacking).

## Principais Tópicos
- **Situação-Problema Documentada:** A empresa terceirizada responsável pelo preparo só recebia a previsão de demanda às sextas-feiras para a semana seguinte — prazo excessivamente curto que forçava superprodução ou compras emergenciais.
- **Dataset:** 15.279 registros individuais consolidados em granularidade diária (78 dias letivos).
- **Variáveis Utilizadas:** histórico de demanda, calendário acadêmico (dias letivos, feriados, eventos), dados meteorológicos (temperatura e precipitação).
- **Arquitetura de Modelos:** Comitê de modelos (Ensemble): Ridge + ExtraTrees + Gradient Boosting + XGBoost, com estratégia de **Modelo Híbrido Residual** (linear captura tendência global; árvore aprende os resíduos).
- **Resultado:** Sistema proativo com antecedência superior, capaz de reduzir desperdício em até 30% (validado por literaturas citadas).

## Pertinência para o Projeto
**Essencial — Produção Própria (A mais completa até o momento).** É o artigo que demonstra o produto tecnológico em funcionamento e serve como pré-print da sua Dissertação. **Deve ser a principal autocitação do trabalho.** Toda a arquitetura metodológica aqui descrita (híbrido residual, ensemble, features climáticas + calendário) é o que seus notebooks 07b-07i implementam computacionalmente.
