---
title: "Redimensionamento e Zoom de Imagens"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Deep_Learning_with_PyTorch_2Ed_Final_-_Howard_Huang"
  - "AI_and_ML_for_Coders_Applying_Core_ML_-_Suddhasatwa_Bhaumik"
tags: [conceito, rede/machine-learning, data-augmentation, imagens]
---

# Redimensionamento e Zoom de Imagens

## Definição
Redimensionamento altera as dimensões da imagem; zoom aleatório amplia ou reduz o campo de visão aparente em torno de uma região. Em augmentation, a escala varia moderadamente entre exemplos de treino.

## Como funciona
Escolhe-se um fator de escala e reamostra-se a imagem para o tamanho requerido pelo modelo. A interpolação e o tratamento das bordas afetam o resultado. Huang aplica escalas aleatórias a volumes; Bhaumik mostra `zoom_range` em `ImageDataGenerator`.

## Quando usar
Quando diferenças realistas de distância, tamanho aparente ou resolução ocorrerem no uso. Redimensionamento fixo também pode ser necessário para padronizar formato, mas por si só não cria diversidade aleatória.

## Limitações
Escala excessiva pode cortar o objeto, remover detalhes ou criar artefatos de interpolação. Não confunda normalização/reescala dos valores de pixel com zoom geométrico: são transformações distintas.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Recorte_Aleatorio_de_Imagens|Recorte aleatório de imagens]]
- [[redes/machine-learning/conceitos/Normalização_e_Padronização|Normalização e Padronização]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de atributos de imagens]]

## Evidências
Huang, *Deep Learning with PyTorch*, 2ª ed., cap. 14, seção 14.6.1, pp. 411–412; Bhaumik, *AI and ML for Coders*, exemplo `ImageDataGenerator` (`zoom_range=0.2`).
