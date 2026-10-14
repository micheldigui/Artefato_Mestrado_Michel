---
title: "Oversampling e Bootstrap da Classe Minoritária"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "AI-Assisted_Statistics_for_Data_Scientists_3E_-_Peter_Bruce"
tags: [conceito, rede/machine-learning, data-augmentation, dados-desbalanceados]
---

# Oversampling e Bootstrap da Classe Minoritária

## Definição
Reamostragem que aumenta a presença da classe rara no treino. No oversampling aleatório, observações minoritárias são selecionadas com reposição; bootstrap repete sorteios com reposição para formar registros de treino.

## Como funciona
Ajusta-se a frequência da classe no conjunto de treino pela duplicação/reseleção de registros existentes. A distribuição alterada é usada para ajustar o classificador; validação e teste mantêm a prevalência real do problema.

## Quando usar
Como baseline simples para classificação desbalanceada, comparado com pesos de classe, undersampling e SMOTE. A escolha deve refletir custos de erros e métricas por classe.

## Limitações
Não cria diversidade informacional nova: cópias repetidas podem aumentar sobreajuste. Se executado antes da divisão, amostras repetidas podem vazar para validação/teste. Não é solução geral para regressão nem para aumentar observações temporais independentes.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Imbalanced_Data|Dados desbalanceados]]
- [[redes/machine-learning/conceitos/SMOTE|SMOTE]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-validation]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipeline sem vazamento]]

## Evidências
Bruce et al., *AI-Assisted Statistics for Data Scientists*, 3ª ed., seções “Oversampling and Up/Down Weighting” e “Data Generation”: oversampling por linhas sorteadas com reposição, bootstrap da classe rara e comparação com pesos de classe.
