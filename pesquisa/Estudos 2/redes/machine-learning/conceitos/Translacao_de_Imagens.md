---
title: "Translação Aleatória de Imagens"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Deep_Learning_with_PyTorch_2Ed_Final_-_Howard_Huang"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
tags: [conceito, rede/machine-learning, data-augmentation, imagens]
---

# Translação Aleatória de Imagens

## Definição
Deslocamento espacial de uma imagem por um pequeno número de pixels ou voxels nos eixos horizontal e vertical, sem alterar deliberadamente sua escala ou orientação.

## Como funciona
A cada amostra de treino, sorteia-se um deslocamento dentro de limites definidos. A região exposta nas bordas precisa de uma regra explícita de preenchimento, repetição ou recorte. Huang descreve deslocamentos aleatórios sub-voxel com reamostragem/interpolação.

## Quando usar
Quando a posição do objeto dentro do quadro varia em produção ou quando se quer reduzir dependência de centralização perfeita. Géron usa shifts de imagens de dígitos como expansão de treino.

## Limitações
Deslocamentos grandes podem cortar o objeto ou mudar a classe; interpolação pode borrar detalhes e o preenchimento de borda criar artefatos. Verifique amplitudes e bordas visualmente e por desempenho.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Recorte_Aleatorio_de_Imagens|Recorte aleatório de imagens]]
- [[redes/machine-learning/conceitos/Rotacao_de_Imagens|Rotação de imagens]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipeline sem vazamento]]

## Evidências
Huang, *Deep Learning with PyTorch*, 2ª ed., cap. 14, seção 14.6.1, pp. 411–412; Géron, *Hands-On Machine Learning*, 2ª ed., exercício de expansão de imagens de dígitos no cap. 3.
