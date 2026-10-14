---
title: "Extração de Atributos de Imagens"
type: "conceito"
network: "machine-learning"
area: "Feature Engineering"
status: "rascunho"
source_ids:
  - "ZHENG-CASARI-2018"
  - "OZDEMIR-2022"
  - "DUBOUE-2020"
  - "SOHAIL-2025"
tags:
  - conceito
  - feature-engineering
  - visao-computacional
---

# Extração de Atributos de Imagens

## Definição

Conversão de pixels em atributos úteis para classificação, busca, detecção ou previsão visual. Pode usar descritores definidos manualmente ou representações aprendidas por redes neurais.

## Famílias de representação

- **Pixels e canais:** intensidades, cor e espaços RGB/HSV/LAB; simples, mas sensíveis a posição, iluminação e variações de captura.
- **Pré-processamento e estrutura local:** suavização, filtros, gradientes, bordas e operações morfológicas, escolhidos conforme ruído e geometria.
- **Descritores manuais:** histogramas, HOG, SIFT e LBP para forma, orientação, pontos de interesse e textura.
- **Representações aprendidas:** embeddings/intermediárias de CNNs; extração congelada ou ajuste fino, com custo e quantidade de dados diferentes.
- **Aumento de dados:** transformações realistas no treino para ampliar variação; não substitui novas amostras independentes nem uma partição por sujeito/cena quando necessária.

## Cuidados

Escolha resolução, canais e transformação segundo a invariância necessária. Faça a partição por unidade independente (por exemplo, pessoa, peça, câmera ou lote) antes de augmentar imagens. Compare descritores simples com representação aprendida, inspecione erros por subgrupo e não interprete uma projeção visual como prova de separabilidade.

## Conexões
- [[redes/machine-learning/conceitos/Transformacoes_Fotometricas_de_Imagens|Transformações fotométricas]]
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]

- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Analise_Multivariada_Exploratoria|Análise Multivariada Exploratória]]
- [[redes/machine-learning/conceitos/Redução_de_Dimensionalidade|Redução de Dimensionalidade]]
- [[redes/machine-learning/conceitos/PCA__Principal_Component_Analysis_|PCA]]
- [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais|Deep Learning e Redes Neurais]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipelines de Feature Engineering sem Vazamento]]

## Evidências nas fontes

Zheng e Casari (2018), cap. 8; Ozdemir (2022), cap. 6; Duboue (2020), cap. 9; Sohail (2025), caps. 2–3 e 5–6.


