# Resumo de Produção Própria: Souza et al. (2025) — SIMPROF

## Referência Completa
**Autores:** Souza, M. S.; Arima, C. H.; Orsi, R. N.; Souza, P. A.
**Título:** Análise Exploratória de Dados para Previsão da Demanda de Refeições e Redução do Desperdício Alimentar em Instituição de Ensino.
**Ano:** 2025
**Evento:** XX Simpósio dos Programas Profissionais de Pós-Graduação (SIMPROF) — São Paulo/SP, 04-06 nov. 2025.
**Caminho Local:** `d:\PROJETOS\PRODUTO_MESTRADO\docs\artigos\Meus Artigos\Relato-Tecnico_2025_SIMPROF.pdf`

## Resumo
Este é o **relato técnico mais avançado da produção própria**, apresentado no SIMPROF 2025 como evolução do trabalho anterior (SIMPROFI 2024). O estudo detalha toda a **Análise Exploratória de Dados (EDA)** realizada sobre o dataset do RU, cobrindo:
- Pré-processamento de dados brutos (consumo, reservas, cardápios, clima)
- Agregação para granularidade diária
- Vetorização de cardápios com **Word2Vec**
- Decomposição sazonal (aditiva vs. multiplicativa) — modelo multiplicativo superior (MAPE 12,49%)
- Identificação da **distribuição bimodal** da demanda (dias letivos vs. não letivos)
- Validação das **reservas como preditor primário** da demanda

## Principais Tópicos
- **Metodologia CRISP-ML(Q):** Adotada como framework do ciclo de vida de ML.
- **Padrão Semanal e Sazonalidade:** Picos claros nos dias úteis; padrão muito distinto entre semanas letivas e não-letivas.
- **Correlação Reservas × Consumo:** Confirmada como a variável de maior poder preditivo do dataset.
- **Conclusão sobre Algoritmos:** Os dados indicaram necessidade de modelos não-lineares (Random Forest, XGBoost) para capturar as complexidades da série.

## Pertinência para o Projeto
**Essencial — Produção Própria.** É o relato técnico mais atual do seu portfólio científico. Representa o estado do projeto à época do SIMPROF 2025, consolidando todos os resultados da EDA (Notebooks 03 e 04) e justificando a escolha de algoritmos avançados para os notebooks seguintes. **Deve ser citado como obra própria na seção de Referências e no Referencial Teórico da Dissertação.**
