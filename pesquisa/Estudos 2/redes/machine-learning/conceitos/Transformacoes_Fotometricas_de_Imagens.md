---
title: "Transformações Fotométricas de Imagens"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Mastering_Computer_Vision_with_Python_-_Sohail"
  - "Artificial Intelligence for Engineers"
tags: [conceito, rede/machine-learning, data-augmentation, imagens]
---

# Transformações Fotométricas de Imagens

## Definição
Alterações controladas de propriedades de intensidade e cor, como brilho, contraste e saturação, para simular condições de iluminação ou captura diferentes.

## Como funciona
Sorteiam-se pequenas mudanças nos canais ou na curva tonal durante o treino. Normalização fixa é pré-processamento; jitter fotométrico aleatório é a transformação de aumento.

## Quando usar
Quando iluminação, exposição ou balanço de cor varia de forma plausível entre treino e uso, e a classe não depende do valor fotométrico alterado.

## Limitações
Variações fortes podem apagar características discriminantes, distorcer cores semanticamente relevantes ou criar dados fora da câmera/domínio real. Defina amplitudes a partir de exemplos observados e confira imagens transformadas.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Redimensionamento_e_Zoom_de_Imagens|Redimensionamento e zoom]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de atributos de imagens]]

## Evidências
*Mastering Computer Vision with Python*, pipeline de treino com `ColorJitter` para brilho, contraste e saturação; *Artificial Intelligence for Engineers*, seção de color augmentation com mudanças de brightness, contrast e saturation.
