---
title: "Adição de Ruído aos Dados"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Deep_Learning_with_PyTorch_2Ed_Final_-_Howard_Huang"
tags: [conceito, rede/machine-learning, data-augmentation, regularizacao]
---

# Adição de Ruído aos Dados

## Definição
Perturbação aleatória dos valores de uma amostra de treino, por exemplo somando ruído Gaussiano de amplitude controlada, para reduzir dependência de detalhes exatos.

## Como funciona
Gera-se uma amostra de ruído compatível com a forma dos dados e soma-se à entrada. A distribuição, escala e domínio da perturbação devem representar variação plausível do processo de medição.

## Quando usar
Quando ruído semelhante ocorre em dados de uso e o modelo precisa ser robusto a essa variação. Deve ser testado como hipótese experimental isolada e combinado apenas após avaliar seu efeito próprio.

## Limitações
Ruído pode apagar sinal útil, gerar valores impossíveis ou tornar o exemplo irreconhecível. Huang alerta que ruído excessivo dificulta a classificação e, no experimento do capítulo 14, a variante com ruído teve desempenho inferior à versão sem augmentation para os nódulos avaliados.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Overfitting_e_Underfitting|Overfitting e underfitting]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-validation]]

## Evidências
Huang, *Deep Learning with PyTorch*, 2ª ed., cap. 14, seção 14.6.1, pp. 413–417; ruído Gaussiano descrito na seção 14.6.1 e comparação com outras variantes na seção 14.6.2.
