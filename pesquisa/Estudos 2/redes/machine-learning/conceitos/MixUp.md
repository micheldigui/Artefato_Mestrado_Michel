---
title: "MixUp"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Deep_Learning_with_PyTorch_2Ed_Final_-_Howard_Huang"
tags: [conceito, rede/machine-learning, data-augmentation, regularizacao]
---

# MixUp

## Definição
Técnica de aumento e regularização que forma exemplos interpolados a partir de pares de amostras e combina os alvos na mesma proporção. Em classificação, os alvos tornam-se distribuições ponderadas entre as classes originais.

## Como funciona
Selecionam-se duas amostras e um coeficiente λ entre 0 e 1; a entrada combinada é λx₁ + (1−λ)x₂, e o alvo é λy₁ + (1−λ)y₂. O coeficiente é sorteado, com frequência por uma distribuição Beta. O método cria treinamento para combinações lineares, não variantes naturais de um único exemplo.

## Quando usar
Como experimento em modelos neurais e tarefas em que interpolações de entradas e alvos são úteis para suavizar fronteiras e reduzir confiança excessiva. Compare com treinamento sem MixUp e confira exemplos e métricas na tarefa.

## Limitações
Misturas podem não corresponder a exemplos plausíveis, especialmente em dados tabulares com restrições, imagens médicas ou séries temporais. Rótulos ponderados exigem função de perda compatível. Não extrapole o benefício entre domínios.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Overfitting_e_Underfitting|Overfitting e underfitting]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-validation]]
- [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais|Deep Learning e redes neurais]]

## Evidências
Huang, *Deep Learning with PyTorch*, 2ª ed., cap. 14, exercício 14.8, propõe implementar MixUp para candidatos positivos de nódulos. Para a definição operacional, ver Zhang, Cissé, Dauphin e Lopez-Paz, “mixup: Beyond Empirical Risk Minimization”, ICLR 2018: https://arxiv.org/abs/1710.09412.
