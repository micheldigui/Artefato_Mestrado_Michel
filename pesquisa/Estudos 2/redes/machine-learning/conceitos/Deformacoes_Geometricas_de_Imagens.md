---
title: "Deformações Geométricas de Imagens"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Machine_Learning_Hero_Master_Data_-_Cuantum_Technologies"
  - "Artificial Intelligence for Engineers"
tags: [conceito, rede/machine-learning, data-augmentation, imagens]
---

# Deformações Geométricas de Imagens

## Definição
Transformações que modificam a geometria local ou perspectiva de uma imagem, como shear (cisalhamento), perspectiva e deformação elástica.

## Como funciona
Uma grade de coordenadas é deslocada ou projetada e os valores são reamostrados para produzir uma forma alterada. Em tarefas com caixas, pontos-chave ou máscaras, as anotações devem receber exatamente a mesma transformação.

## Quando usar
Quando deformações de forma, ângulo de câmera ou perspectiva aparecem no domínio de uso e preservam a classe/estrutura-alvo.

## Limitações
Pode distorcer anatomia, letras, objetos rígidos ou relações espaciais; transformações em excesso criam artefatos. Para CT ou imagens médicas, avaliar geometria física e anisotropia antes de deformar volumes.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Rotacao_de_Imagens|Rotação de imagens]]
- [[redes/machine-learning/conceitos/Recorte_Aleatorio_de_Imagens|Recorte aleatório de imagens]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de atributos de imagens]]

## Evidências
*Machine Learning Hero Master Data*, seção 3.6.1, inclui shear, mudanças de perspectiva e elastic deformations; *Artificial Intelligence for Engineers*, seção sobre augmentation de imagens, descreve shear e perspective.
