---
title: "Índice de Algoritmos e Modelos de Machine Learning"
type: "indice-de-modelos"
network: "machine-learning"
status: "rascunho"
tags:
  - machine-learning
  - algoritmos
  - index
source: "fontes/referencias-ia-ml/txt/ (53 arquivos; 7 aulas e 46 livros)"
---

# Índice de Algoritmos e Modelos de Machine Learning

> Escopo: inventário de algoritmos e arquiteturas cujo nome foi encontrado nos 53 arquivos de `fontes/referencias-ia-ml/txt/`. A presença indica uma menção no texto extraído; não prova que a fonte desenvolva o método em profundidade. As referências identificam o arquivo `.txt`. A extração não oferece paginação confiável e, por isso, este índice não inventa páginas ou capítulos.

## Como navegar

- Abra uma família abaixo e siga o link para a nota canônica quando ela já existir.
- Termos sem link ainda estão indexados aqui, mas não possuem nota atômica na rede.
- Referências `Axx` apontam para aulas; `Bxx` apontam para livros. O registro completo está na nota de corpus indicada ao fim.
- Leia números de correspondências apenas como resultado de busca literal normalizada, não como medida de importância ou cobertura didática.
- Para ligar o diagnóstico dos dados à escolha de famílias, consulte [[redes/machine-learning/mapa-eda-e-selecao-de-modelos|o mapa de EDA e seleção de modelos]].

## Limites da indexação

- Foram lidos todos os `.txt` em `fontes/referencias-ia-ml/txt/`. O manifesto e a auditoria de cobertura contêm a relação atualizada de fontes e algoritmos.
- A extração/OCR pode duplicar texto, perder equações, nomes ou hierarquia de capítulos; ocorrências precisam ser conferidas na fonte original antes de uso acadêmico.
- A sigla `LDA` é ambígua: foi mantida separada das ocorrências em que a fonte escreve por extenso `Linear Discriminant Analysis` ou `Latent Dirichlet Allocation`.
- A catalogação é restrita aos nomes listados e encontrados; não representa uma revisão crítica nem garante que todo modelo citado nos livros foi detectado.
- Não use este índice como citação final de tese. Consulte o livro/material original e complete autor, edição, editora, ano e página na referência bibliográfica.

## Regressão supervisionada

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| Regressão linear | B01 (79); B02 (57); A03 (60); B04 (2); B06 (3); B08 (1); B10 (17); B11 (2); B13 (19); B14 (16); B15 (29); B16 (60); B17 (19); B18 (14); B20 (2); B21 (19); B22 (52); B23 (11); B24 (1); B25 (35); B26 (72); B29 (1); B30 (2); B31 (1); B32 (23); B33 (1); B35 (3); B36 (2); B38 (8); B42 (7); B43 (1); B44 (25); B45 (47) | [[redes/machine-learning/conceitos/Regressão_Linear | abrir nota]] |
| Regressão polinomial | A03 (3) | — |
| Regressão logística | B01 (84); B02 (23); A01 (1); A02 (1); A03 (1); B04 (4); B12 (32); B13 (36); B14 (52); B15 (56); B16 (53); B17 (30); B18 (15); B22 (12); B23 (1); B24 (3); B25 (38); B26 (62); B27 (8); B28 (1); B32 (29); B36 (4); B37 (1); B38 (6); B42 (1); B43 (3); B44 (16); B45 (1) | [[redes/machine-learning/conceitos/Regressão_Logística | abrir nota]] |
| Ridge (regularização L2) | — | [[redes/machine-learning/conceitos/Regularização_L2__Ridge_ | abrir nota]] |
| Lasso (regularização L1) | — | [[redes/machine-learning/conceitos/Regularização_L1__Lasso_ | abrir nota]] |
| Elastic Net | B04 (1); B14 (9); B16 (14); B32 (1); B38 (6); B44 (1); B45 (4) | — |
| Support Vector Regression (SVR) | B02 (2) | [[redes/machine-learning/conceitos/SVM__Support_Vector_Machines_ | abrir nota]] |

## Classificação supervisionada

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| K-Nearest Neighbors (KNN) | B01 (114); B02 (33); B03 (2); A01 (1); A02 (1); A03 (1); A04 (1); A05 (18); B04 (11); B08 (1); B11 (11); B12 (2); B13 (11); B14 (3); B15 (54); B16 (12); B17 (27); B18 (14); B21 (2); B22 (3); B23 (6); B24 (1); B25 (64); B26 (122); B38 (17); B44 (1); B45 (104) | [[redes/machine-learning/conceitos/K-Nearest_Neighbors__KNN_ | abrir nota]] |
| Árvores de decisão | B01 (25); B02 (101); B03 (1); A01 (1); A02 (1); A03 (1); A05 (51); B04 (39); B05 (49); B11 (5); B12 (2); B13 (7); B14 (15); B15 (59); B16 (97); B17 (52); B18 (54); B19 (1); B21 (61); B22 (6); B23 (32); B24 (2); B25 (96); B26 (78); B27 (2); B31 (2); B32 (43); B36 (5); B38 (11); B40 (3); B41 (6); B43 (15); B44 (27); B45 (2) | [[redes/machine-learning/conceitos/Árvores_de_Decisão | abrir nota]] |
| Random Forest | B01 (128); B02 (70); A04 (2); A05 (28); A07 (2); B04 (8); B08 (4); B12 (26); B13 (8); B14 (136); B15 (46); B16 (42); B17 (38); B18 (62); B21 (4); B22 (2); B23 (18); B24 (6); B25 (24); B26 (84); B27 (12); B28 (20); B30 (2); B32 (40); B38 (10); B43 (18); B44 (30); B45 (10) | [[redes/machine-learning/conceitos/Random_Forest | abrir nota]] |
| Support Vector Machines (SVM) | B02 (3); A01 (1); A02 (1); A03 (1); A04 (1); A05 (43); B04 (41); B05 (15); B06 (1); B08 (1); B13 (11); B14 (12); B15 (70); B16 (127); B17 (2); B18 (4); B21 (32); B22 (61); B23 (3); B24 (4); B25 (36); B26 (92); B30 (3); B32 (13); B36 (1); B38 (3); B43 (5); B45 (15) | [[redes/machine-learning/conceitos/SVM__Support_Vector_Machines_ | abrir nota]] |
| Naive Bayes | B01 (74); B02 (4); A02 (2); A03 (2); B04 (36); B05 (6); B13 (2); B15 (10); B16 (2); B17 (52); B18 (16); B21 (10); B22 (32); B23 (4); B25 (4); B26 (2); B32 (12); B36 (2); B38 (8); B42 (14); B43 (2) | [[redes/machine-learning/conceitos/Naive_Bayes | abrir nota]] |
| Perceptron | B01 (4); B03 (2); B04 (9); B05 (52); B07 (3); B10 (1); B15 (40); B16 (35); B17 (6); B20 (1); B21 (84); B22 (38); B25 (8); B30 (7); B32 (4); B38 (1); B42 (3); B43 (1); B44 (10); B46 (1) | [[redes/machine-learning/conceitos/Perceptron | abrir nota]] |
| Análise Discriminante Linear (Linear Discriminant Analysis) | — | — |

## Modelos de tópicos

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| Latent Dirichlet Allocation (LDA) | B15 (1); B32 (4) | — |
| LDA (sigla sem expansão confirmada no trecho) | — | — |

## Ensembles

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| Bagging | B01 (48); B02 (15); A05 (1); B04 (36); B05 (8); B14 (1); B15 (18); B16 (27); B17 (20); B18 (34); B19 (3); B21 (14); B22 (2); B23 (41); B25 (95); B26 (4); B32 (14); B45 (4) | — |
| AdaBoost | B01 (5); A01 (1); A02 (1); A03 (1); B04 (9); B15 (56); B16 (25); B17 (12); B18 (10); B21 (15); B22 (6); B23 (3); B25 (11); B32 (3); B38 (1) | — |
| Gradient Boosting | B01 (22); B02 (18); B04 (16); B06 (6); B13 (2); B14 (20); B15 (46); B16 (36); B17 (38); B18 (34); B23 (8); B25 (38); B26 (4); B28 (4); B32 (14); B35 (6); B36 (2); B38 (2); B43 (2); B44 (32); B45 (4) | [[redes/machine-learning/conceitos/Gradient_Boosting | abrir nota]] |
| XGBoost | B01 (84); B02 (36); A05 (22); B04 (10); B06 (4); B14 (2); B15 (34); B16 (14); B18 (50); B19 (6); B23 (32); B24 (36); B25 (6); B26 (24); B28 (2); B31 (2); B33 (26); B35 (22); B36 (4); B37 (14); B44 (78) | [[redes/machine-learning/conceitos/XGBoost | abrir nota]] |
| LightGBM | B14 (1); B18 (17); B19 (2); B24 (3); B25 (38); B26 (1); B31 (5); B33 (6); B36 (6); B37 (1); B38 (8); B44 (1) | — |
| CatBoost | B17 (1); B37 (1); B44 (1) | — |
| Voting / classificação por votação | — | — |
| Stacking | B01 (1); B02 (1); B03 (18); B04 (20); B05 (3); B07 (7); B09 (2); B10 (1); B13 (24); B15 (8); B16 (19); B17 (4); B18 (1); B20 (1); B21 (13); B23 (17); B25 (4); B26 (2); B32 (8); B35 (6); B39 (3); B45 (1); B46 (1) | — |

## Agrupamento

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| K-Means | B01 (110); B02 (56); B03 (2); A06 (24); B04 (54); B05 (4); B06 (26); B08 (2); B11 (10); B12 (10); B13 (202); B14 (164); B15 (150); B16 (133); B17 (30); B18 (10); B19 (16); B20 (110); B21 (94); B22 (45); B23 (12); B25 (84); B26 (214); B32 (4); B37 (10); B38 (2); B43 (16); B44 (20); B45 (2) | [[redes/machine-learning/conceitos/K-Means_Clustering | abrir nota]] |
| DBSCAN | B02 (24); A01 (1); A02 (1); A03 (1); B04 (13); B06 (2); B11 (29); B14 (42); B15 (33); B16 (31); B17 (11); B24 (9); B25 (9); B26 (58); B38 (8); B44 (1) | [[redes/machine-learning/conceitos/DBSCAN | abrir nota]] |
| OPTICS | B02 (1); B04 (1); B05 (1); B08 (1); B20 (1) | — |
| Mean Shift | B04 (4); B25 (4) | — |
| Clustering hierárquico / aglomerativo | — | [[redes/machine-learning/conceitos/Clustering_Hierárquico | abrir nota]] |
| Gaussian Mixture Models (GMM) | B25 (1) | — |
| Spectral Clustering | B15 (20); B16 (4); B21 (8); B26 (1); B32 (1) | — |

## Redução de dimensionalidade e representação

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| Principal Component Analysis (PCA) | B01 (41); B02 (3); A01 (1); A02 (1); A03 (1); A06 (28); B04 (24); B08 (22); B11 (45); B12 (37); B13 (88); B14 (6); B15 (96); B16 (124); B17 (43); B18 (33); B21 (83); B22 (104); B23 (5); B25 (62); B26 (222); B27 (1); B32 (29); B38 (83); B43 (22) | [[redes/machine-learning/conceitos/PCA__Principal_Component_Analysis_ | abrir nota]] |
| t-SNE | A01 (1); A02 (1); A03 (1); B04 (1); B14 (2); B15 (26); B16 (9); B21 (5); B25 (39); B26 (136); B32 (20); B38 (22); B43 (7) | — |
| UMAP | A01 (1); A02 (1); A03 (1); B04 (1); B18 (71); B26 (180); B32 (9); B38 (12) | — |
| Independent Component Analysis (ICA) | B04 (1); B15 (1); B18 (1); B22 (1); B38 (1) | — |
| Factor Analysis | B02 (1); B09 (1); B11 (26); B13 (3); B15 (21); B20 (2); B21 (21); B22 (6) | — |

## Detecção de anomalias

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| Isolation Forest | B16 (5); B17 (4); B18 (17); B24 (1); B26 (2); B38 (6); B45 (1) | [[redes/machine-learning/conceitos/Detecção_de_Anomalias | abrir nota]] |

## Redes neurais e deep learning

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| Multilayer Perceptron (MLP) | B01 (1); B07 (1); B15 (2); B16 (1); B17 (1); B32 (1); B46 (1) | [[redes/machine-learning/conceitos/Multilayer_Perceptron__MLP_ | abrir nota]] |
| Redes neurais artificiais / Deep Learning | — | [[redes/machine-learning/conceitos/Redes_Neurais_Artificiais | abrir nota]] |
| Convolutional Neural Network (CNN) | B01 (1); B04 (1); B08 (1); B14 (1); B23 (1); B32 (1); B44 (3) | [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais | abrir nota]] |
| Recurrent Neural Network (RNN) | B22 (1); B32 (2); B43 (1); B44 (2); B45 (1) | [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais | abrir nota]] |
| Long Short-Term Memory (LSTM) | B01 (4); B07 (1); B11 (1); B15 (4); B16 (2); B21 (1); B23 (1); B25 (2); B32 (4); B43 (1); B46 (2) | [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais | abrir nota]] |
| Gated Recurrent Unit (GRU) | B02 (1); B15 (4); B16 (2); B21 (1); B32 (3); B45 (2) | [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais | abrir nota]] |
| Transformer / Transformer neural network | — | [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais | abrir nota]] |
| Autoencoders | B01 (2); B02 (2); B03 (1); B07 (3); B08 (1); B12 (21); B14 (1); B15 (34); B16 (125); B17 (1); B20 (1); B21 (12); B23 (11); B24 (2); B26 (1); B27 (1); B32 (1); B38 (2); B43 (7); B45 (1); B46 (4) | [[redes/machine-learning/conceitos/Redes_Neurais_Artificiais | abrir nota]] |
| Variational Autoencoder (VAE) | B07 (1); B15 (2) | — |
| Generative Adversarial Network (GAN) | B04 (1); B21 (1); B32 (3) | — |
| Restricted Boltzmann Machine (RBM) | B04 (1); B15 (1) | — |
| Deep Belief Network (DBN) | B15 (1) | — |

## Aprendizado por reforço

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| Q-Learning | A07 (8); B04 (7); B05 (12); B15 (27); B16 (48); B21 (1); B22 (13); B26 (1); B32 (1); B40 (63); B46 (3) | — |
| SARSA | A01 (1); A02 (1); A03 (1); A07 (1); B04 (6); B15 (23); B21 (16); B22 (12); B26 (1); B40 (83); B46 (3) | — |
| Deep Q-Network (DQN) | B16 (1) | — |
| Policy Gradient | A01 (1); A02 (1); A03 (1); B04 (23); B15 (9); B16 (1); B21 (6); B22 (12); B46 (2) | — |
| Actor-Critic | B03 (1); A07 (1); B04 (10); B15 (13); B16 (15); B21 (2); B22 (2); B40 (32); B46 (3) | — |
| Asynchronous Advantage Actor-Critic (A3C) | B16 (1) | — |
| Value Iteration | B15 (12); B16 (12); B21 (7); B22 (2); B40 (35) | — |
| Policy Iteration | B15 (15); B21 (4); B22 (4); B40 (52); B46 (1) | — |
| Temporal Difference learning (TD, TD(0), TD(λ)) | — | — |

## Regras de associação

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| Apriori | B02 (1); B04 (15); B15 (27); B16 (1); B18 (3); B21 (4) | — |
| FP-Growth | B02 (1); A01 (1); A02 (1); A03 (1) | — |

## Séries temporais

| Modelo/algoritmo | Referências no corpus TXT | Nota canônica |
|---|---|---|
| ARIMA | B02 (4); B08 (1); B15 (16); B16 (2); B18 (1); B19 (6); B23 (6); B28 (2); B32 (1); B36 (2); B43 (4); B44 (14); B45 (146); B46 (3) | — |
| Prophet | B24 (35); B36 (1); B45 (116) | — |

## Registro das fontes

O catálogo de fontes abaixo lista os arquivos de origem sem criar nós de fonte no grafo. A numeração é estável enquanto a ordenação relativa dos arquivos em `txt/` não mudar.

`redes/machine-learning/fontes/Corpus_Aulas_e_Livros_TXT.md`


## Glossário e relações candidatas

As tabelas `glossary_candidates.csv` e `relationship_candidates.csv`, em `fontes/referencias-ia-ml/indexacao/`, organizam pistas extraídas dos 53 textos com stopwords PT/EN, evidência textual, fonte e classe heurística. Coocorrências estão marcadas como inferidas. Confirme cada trecho e conceito antes de incorporá-lo às notas canônicas.
