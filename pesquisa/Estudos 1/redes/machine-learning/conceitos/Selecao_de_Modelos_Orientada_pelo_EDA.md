---
title: "Seleção de Modelos Orientada pelo EDA"
type: "conceito"
network: "machine-learning"
area: "Seleção e avaliação de modelos"
status: "rascunho"
tags:
  - conceito
  - machine-learning
  - selecao-de-modelos
source: "Síntese do índice de algoritmos e do mapa EDA desta rede"
---

# Seleção de Modelos Orientada pelo EDA

## Definição

É a prática de usar os achados da análise exploratória para definir uma pequena lista de famílias de modelos e tratamentos plausíveis, e então compará-los em validação que imite o uso real. O EDA orienta quais hipóteses testar; o desempenho validado, as restrições e o custo de erro orientam a escolha.

Não existe uma distribuição univariada que escolha automaticamente um algoritmo vencedor. A distribuição é apenas uma parte do contexto: alvo, volume, dependência, representações, explicabilidade, latência e manutenção também importam.

## Problema que resolve

Reduz busca arbitrária e ajuda a evitar combinações inadequadas, por exemplo KNN sem tratar escalas muito diferentes, acurácia como única métrica em classes raras, ou split aleatório em dados temporais. Também força a comparação com uma baseline e a registrar por que cada família entrou ou saiu da shortlist.

## Fluxo de decisão

1. **Defina a tarefa:** alvo contínuo, classe, ordem temporal, ranking, ausência de rótulo ou anomalia.
2. **Use o grão e a disponibilidade temporal** para determinar features permitidas e esquema de validação.
3. **Use o perfil para propor tratamentos:** imputação, escala, codificação, robustez a extremos, representação ou amostragem.
4. **Escolha baselines e famílias candidatas** que cubram hipóteses distintas, incluindo uma opção simples e interpretável quando útil.
5. **Valide tudo dentro de pipeline:** preprocessing e seleção são ajustados no treino de cada fold.
6. **Compare métrica primária, estabilidade, erros por segmentos, calibração e custo de operação.**
7. **Escolha ou rejeite com justificativa registrada**, mantendo as limitações e as alternativas consideradas.

## Relações entre evidência e candidatos

| Evidência/condição | Candidatos iniciais a comparar | Validação ou ressalva |
|---|---|---|
| Alvo contínuo e relações relativamente simples | Média/mediana como baseline; regressão linear, Ridge/Lasso; árvores/boosting se houver não linearidade. | Avalie resíduos para diagnóstico do modelo linear; normalidade dos preditores não é requisito universal. |
| Alvo binário/multiclasse | Classificador majoritário como baseline; logística regularizada, árvore/ensemble, SVM ou Naive Bayes conforme representação. | Escolha métrica e limiar segundo custos; use estratificação quando compatível com a dependência dos dados. |
| Classes raras | Logística/árvores/ensembles com pesos ou estratégia de treino; avaliar PR-AUC, recall, precisão e calibração. | Pesos, threshold e reamostragem devem ser definidos usando somente os dados de treino/validação. |
| Escalas heterogêneas e geometria por distância | KNN, SVM, K-Means ou PCA com transformação de escala dentro do pipeline. | Escala é parte da hipótese de distância; compare com árvore/boosting sem exigir escala semelhante. |
| Não linearidade e interações | Random Forest/boosting; SVM com kernel quando volume/custo permitem; compare com baseline linear. | Verifique extrapolação, estabilidade e subgrupos; performance não é causalidade. |
| Categóricas raras ou alta cardinalidade | Modelos lineares regularizados, árvores/boosting com estratégia categórica compatível ou codificação dentro do fold. | Trate categorias novas e evite vazamento em target encoding. |
| Contagens/valores não negativos com muitos zeros | Baselines de contagem; Poisson/binomial negativa ou abordagem em duas etapas quando justificadas; comparar árvores. | Verifique dispersão e mecanismo dos zeros; a distribuição observada sozinha não identifica o processo gerador. |
| Séries temporais, usuários ou grupos repetidos | Baseline temporal e modelos adequados ao horizonte; validação cronológica ou por grupo. | Não embaralhe unidades dependentes entre treino e teste se isso não corresponde à implantação. |
| Sem alvo e objetivo de segmentação | K-Means, GMM, hierárquico ou densidade, escolhidos pela geometria e objetivo do grupo. | Avalie estabilidade e utilidade; métricas internas e projeções 2D não provam segmentos reais. |
| Sem alvo e objetivo de anomalia | Isolation Forest, One-Class SVM ou regras de domínio como baselines. | Sem rótulos, avaliação requer revisão/amostra de casos e conhecimento do custo de alertas. |
| Texto esparso e alta dimensão | Naive Bayes, regressão logística ou SVM linear como baselines. | A representação textual e o protocolo de validação podem dominar a escolha do algoritmo. |

## Hipóteses e limitações

- EDA sugere hipóteses, mas não substitui experimento comparativo.
- A busca de modelos também pode sobreajustar ao conjunto de validação; preserve um teste final intocado até a seleção.
- Um modelo com métrica média melhor pode falhar em segmentos críticos, estar mal calibrado ou não cumprir latência/explicabilidade.
- Não escolha modelo por normalidade marginal das features sem verificar os pressupostos específicos do estimador e o objetivo (previsão ou inferência).
- Projeções t-SNE/UMAP ajudam a explorar estrutura visual, mas não devem ser tratadas como prova de separabilidade nem como mecanismo automático de seleção.

## Conexões

- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipelines de Feature Engineering sem Vazamento]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Imbalanced_Data|Imbalanced Data]]
- [[redes/machine-learning/conceitos/Normalização_e_Padronização|Normalização e Padronização]]
- [[redes/machine-learning/indice-algoritmos-modelos|Índice de Algoritmos e Modelos]]

## Famílias de modelos conectadas

- **Supervisionados:** [[redes/machine-learning/conceitos/Regressão_Linear|Regressão Linear]], [[redes/machine-learning/conceitos/Regressão_Logística|Regressão Logística]], [[redes/machine-learning/conceitos/Árvores_de_Decisão|Árvores de Decisão]], [[redes/machine-learning/conceitos/Random_Forest|Random Forest]], [[redes/machine-learning/conceitos/Gradient_Boosting|Gradient Boosting]], [[redes/machine-learning/conceitos/XGBoost|XGBoost]], [[redes/machine-learning/conceitos/SVM__Support_Vector_Machines_|SVM]], [[redes/machine-learning/conceitos/K-Nearest_Neighbors__KNN_|K-Nearest Neighbors (KNN)]] e [[redes/machine-learning/conceitos/Naive_Bayes|Naive Bayes]].
- **Não supervisionados e representação:** [[redes/machine-learning/conceitos/K-Means_Clustering|K-Means]], [[redes/machine-learning/conceitos/DBSCAN|DBSCAN]], [[redes/machine-learning/conceitos/Clustering_Hierárquico|Clustering Hierárquico]] e [[redes/machine-learning/conceitos/PCA__Principal_Component_Analysis_|PCA]].
- **Validação:** [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]].

## Perguntas de revisão

1. Qual achado do EDA apoia cada candidato e qual alternativa simples serve de baseline?
2. O preprocessing foi ajustado exclusivamente dentro do treino de cada fold?
3. A partição representa tempo, grupo e unidade da aplicação?
4. Métrica, limiar, calibração e análise de erros refletem o custo do problema?
5. Que nova evidência faria mudar a escolha?
