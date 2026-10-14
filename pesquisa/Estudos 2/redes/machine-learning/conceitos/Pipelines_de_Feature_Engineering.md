---
title: "Pipelines de Feature Engineering sem Vazamento"
type: "conceito"
network: "machine-learning"
area: "Feature Engineering"
status: "rascunho"
source_ids:
  - "ZHENG-CASARI-2018"
  - "OZDEMIR-2022"
  - "DUBOUE-2020"
  - "CAMPESATO-2024"
  - "CUANTUM-2024"
tags:
  - conceito
  - feature-engineering
  - validacao
---

# Pipelines de Feature Engineering sem Vazamento

## Definição

Encadeamento reproduzível de limpeza, imputação, codificação, transformação, seleção e estimador, ajustado sem acesso aos dados reservados para avaliação. O mesmo contrato de transformação deve valer no treino e no uso.

## Procedimento

1. Defina a unidade e a partição de validação a partir do problema: aleatória/estratificada apenas se independente; grupo ou tempo quando a dependência exigir.
2. Dentro de cada fold, ajuste estatísticas de imputação/escala, categorias conhecidas, vocabulário textual, seleção de atributos e hiperparâmetros somente nos dados de treino.
3. Aplique os parâmetros aprendidos ao fold de validação sem reajustá-los. Componha transformações por coluna sem perder alinhamento ou nomes dos atributos.
4. Para target encoding ou atributos derivados do alvo, use estimativas out-of-fold no treino e parâmetros aprendidos apenas nos alvos do treino.
5. Compare pipeline completo com baseline; registre versão, entradas, saída, métricas, estabilidade, latência e limites.

## Armadilhas

- Normalizar, imputar ou selecionar antes do split transmite informação do conjunto de validação.
- Agregados por entidade ou janela temporal podem incluir o futuro se não houver corte explícito.
- Reamostragem, [[redes/machine-learning/conceitos/Aumento_de_Dados|aumento de dados]], escolha de limiar e construção baseada no alvo também devem ficar dentro da validação.
- Um pipeline reproduzível reduz discrepância de transformação, mas não corrige população inadequada, proxies injustos ou mudança de dados.

## Conexões

- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Tratamento_de_Missing_Values|Tratamento de Missing Values]]
- [[redes/machine-learning/conceitos/One-Hot_Encoding|One-Hot Encoding]]
- [[redes/machine-learning/conceitos/Seleção_de_Atributos__Feature_Selection_|Seleção de Atributos]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]

## Evidências nas fontes

Zheng e Casari (2018), cap. 1; Ozdemir (2022), caps. 1–4; Duboue (2020), cap. 1; Campesato (2024), cap. 1; Cuantum Technologies (2024), cap. 3.


