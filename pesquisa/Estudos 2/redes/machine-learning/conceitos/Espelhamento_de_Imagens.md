---
title: "Espelhamento de Imagens (Flip)"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Deep_Learning_with_PyTorch_2Ed_Final_-_Howard_Huang"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "AI_and_ML_for_Coders_Applying_Core_ML_-_Suddhasatwa_Bhaumik"
tags: [conceito, rede/machine-learning, data-augmentation, imagens]
---

# Espelhamento de Imagens (Flip)

## Definição
Transformação geométrica que inverte uma imagem horizontalmente, verticalmente ou em outro eixo, criando uma orientação espelhada do exemplo.

## Como funciona
A operação troca a posição dos pixels em relação a um eixo. Pode ser aplicada com probabilidade aleatória por exemplo e por época; o rótulo permanece igual somente se a orientação não fizer parte da classe.

## Quando usar
Classificação de imagens em que objetos podem aparecer em orientações espelhadas em produção. Huang descreve flips nos eixos de volumes de tomografia e discute a hipótese anatômica usada; Bhaumik e Géron exemplificam flip horizontal em imagens.

## Limitações
Flip vertical ou esquerda-direita pode alterar significado: letras, dígitos, orientação anatômica, sinalização e objetos assimétricos são exemplos em que a invariância não deve ser presumida. Em imagens médicas, valide a hipótese com conhecimento do domínio.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de atributos de imagens]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipeline sem vazamento]]

## Evidências
Huang, *Deep Learning with PyTorch*, 2ª ed., cap. 14, seção 14.6.1, pp. 410–411; Géron, *Hands-On Machine Learning*, 2ª ed., cap. 14, seção “Data Augmentation”; Bhaumik, *AI and ML for Coders*, exemplo `ImageDataGenerator` com `horizontal_flip=True`.
