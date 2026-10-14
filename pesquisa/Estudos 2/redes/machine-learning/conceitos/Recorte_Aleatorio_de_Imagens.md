---
title: "Recorte Aleatório de Imagens"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Deep_Learning_with_PyTorch_2Ed_Final_-_Howard_Huang"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
tags: [conceito, rede/machine-learning, data-augmentation, imagens]
---

# Recorte Aleatório de Imagens

## Definição
Seleção de uma janela espacial da imagem, aleatória ou controlada, para criar uma vista parcial do exemplo. Pode ser redimensionada ao formato de entrada exigido pelo modelo.

## Como funciona
Define-se tamanho e posição da janela; durante o treino, posições diferentes podem gerar vistas distintas. Recorte e redimensionamento são operações relacionadas, mas têm efeitos diferentes: o recorte remove contexto; o redimensionamento altera resolução/escala.

## Quando usar
Quando o objeto mantém sua classe em pequenas mudanças de enquadramento e escala, e quando a inferência também pode receber objetos deslocados ou parcialmente enquadrados.

## Limitações
O recorte pode remover a região que determina o rótulo, produzir exemplos ambíguos ou alterar a proporção do objeto se seguido por deformação. Em detecção/segmentação, as caixas e máscaras também precisam ser transformadas.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Translacao_de_Imagens|Translação aleatória de imagens]]
- [[redes/machine-learning/conceitos/Redimensionamento_e_Zoom_de_Imagens|Redimensionamento e zoom]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de atributos de imagens]]

## Evidências
Huang, *Deep Learning with PyTorch*, 2ª ed., cap. 7, exercício 7.4, propõe implementar random cropping e observar diferenças e efeito no treino; Géron, *Hands-On Machine Learning*, 2ª ed., cap. 14, discute transformações no pipeline de imagens.
