---
title: "ADASYN (Adaptive Synthetic Sampling)"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Hands_on_Machine_Learning_with_scikit_-_Tarek_Amr"
  - "Mastering_NLP_From_Foundations_to_Agents_2E_-_Lior_Gazit"
tags: [conceito, rede/machine-learning, data-augmentation, dados-desbalanceados]
---

# ADASYN (Adaptive Synthetic Sampling)

## Definição
Método adaptativo de oversampling sintético para classificação desbalanceada que concentra a geração de exemplos minoritários em regiões mais difíceis de aprender, especialmente perto de fronteiras locais.

## Como funciona
Estima-se a dificuldade local dos exemplos minoritários a partir da vizinhança; aloca-se mais geração sintética às regiões com maior presença de vizinhos de outras classes. Como no SMOTE, a qualidade depende da geometria e separabilidade dos dados.

## Quando usar
Como alternativa comparativa ao RandomOverSampler e SMOTE em classificação, quando se quer focar regiões difíceis e há exemplos suficientes para estimar vizinhanças locais.

## Limitações
Pode concentrar exemplos em ruído, outliers ou fronteiras ambíguas e piorar a sobreposição de classes. Exige escala/representação adequada e deve ser aplicado dentro de cada fold de treino. Não é técnica genérica para regressão ou séries temporais.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Imbalanced_Data|Dados desbalanceados]]
- [[redes/machine-learning/conceitos/SMOTE|SMOTE]]
- [[redes/machine-learning/conceitos/Oversampling_e_Bootstrap|Oversampling e bootstrap]]
- [[redes/machine-learning/conceitos/K-Nearest_Neighbors__KNN_|K-Nearest Neighbors]]

## Evidências
Amr, *Hands-on Machine Learning with scikit-learn*, seção “Oversampling the minority class”, compara RandomOverSampler, SMOTE e ADASYN; Gazit, *Mastering NLP: From Foundations to Agents*, descreve ADASYN como extensão de SMOTE que gera mais pontos sintéticos em regiões de fronteira difíceis.
