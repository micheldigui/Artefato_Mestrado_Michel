---
title: "Rotação Aleatória de Imagens"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Deep_Learning_with_PyTorch_2Ed_Final_-_Howard_Huang"
  - "AI_and_ML_for_Coders_Applying_Core_ML_-_Suddhasatwa_Bhaumik"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
tags: [conceito, rede/machine-learning, data-augmentation, imagens]
---

# Rotação Aleatória de Imagens

## Definição
Transformação geométrica que gira a imagem por um ângulo sorteado dentro de uma faixa escolhida, criando mudanças de orientação para exemplos de treino.

## Como funciona
Aplica-se uma matriz de rotação e reamostra-se a grade de pixels/voxels. Huang limita a rotação de CT ao plano XY por causa da resolução anisotrópica; Bhaumik também lista rotação como transformação de imagem.

## Quando usar
Quando pequenas mudanças de orientação são plausíveis e não modificam a classe nem a interpretação clínica/operacional.

## Limitações
Ângulos extremos, eixos inadequados, interpolação e regiões de borda podem criar dados artificiais ou alterar o rótulo. Uma transformação válida em fotos comuns pode ser inválida em imagens médicas, documentos ou sinais direcionais.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Translacao_de_Imagens|Translação aleatória de imagens]]
- [[redes/machine-learning/conceitos/Redimensionamento_e_Zoom_de_Imagens|Redimensionamento e zoom]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de atributos de imagens]]

## Evidências
Huang, *Deep Learning with PyTorch*, 2ª ed., cap. 14, seção 14.6.1, pp. 412–413; Bhaumik, *AI and ML for Coders*, exemplo `ImageDataGenerator`; Géron, *Hands-On Machine Learning*, 2ª ed., cap. 14.
