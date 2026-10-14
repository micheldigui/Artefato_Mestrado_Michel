---
title: "Construção e Transformação de Atributos Numéricos"
type: "conceito"
network: "machine-learning"
area: "Feature Engineering"
status: "rascunho"
source_ids:
  - "ZHENG-CASARI-2018"
  - "OZDEMIR-2022"
  - "DUBOUE-2020"
  - "CAMPESATO-2024"
tags:
  - conceito
  - feature-engineering
  - transformacao
---

# Construção e Transformação de Atributos Numéricos

## Definição

Conjunto de operações que altera ou combina medidas numéricas para que a representação expresse melhor a hipótese do problema. A técnica deve responder a um sinal observado no EDA ou a uma regra de domínio e ser comparada por validação.

## Estratégias

- **Reexpressão:** log, raiz, Box-Cox ou Yeo-Johnson para escalas assimétricas ou relações multiplicativas, respeitando domínio e zeros.
- **Discretização:** faixas por limites de domínio, largura igual ou quantis; comparar a perda de informação e a estabilidade dos cortes.
- **Escala:** min-max, padronização, escala robusta ou normalização de vetores quando o estimador depende de magnitude ou distância.
- **Construção:** contagens, razões, diferenças, taxas, agregados descritivos e combinações orientadas pelo domínio.
- **Interações e polinômios:** produtos e potências para representar curvatura ou interação em modelos que não as capturam naturalmente.

## Fluxo de uso

1. Observe forma, unidade, caudas, zeros, grupos e relação com o alvo em [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|EDA]].
2. Registre a hipótese e a escala de interpretação esperada.
3. Ajuste parâmetros da transformação apenas no conjunto de treino de cada fold.
4. Compare pipeline base e transformado na mesma validação e métrica.
5. Reavalie resíduos, segmentos, estabilidade e interpretação na unidade original.

## Limitações e armadilhas

- Transformar para obter um gráfico mais simétrico não é, por si só, motivo para melhorar a variável.
- Cortes, interações e polinômios podem perder informação, criar instabilidade ou aumentar sobreajuste.
- Escalar não remove irrelevância, viés de seleção nem vazamento.
- Não remover extremos automaticamente; diferencie erro de medição e variação legítima em [[redes/machine-learning/conceitos/Outliers|Outliers]].

## Conexões

- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Reexpressao_de_Variaveis|Reexpressão de Variáveis]]
- [[redes/machine-learning/conceitos/Normalização_e_Padronização|Normalização e Padronização]]
- [[redes/machine-learning/conceitos/Seleção_de_Atributos__Feature_Selection_|Seleção de Atributos]]
- [[redes/machine-learning/conceitos/PCA__Principal_Component_Analysis_|PCA]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipelines de Feature Engineering sem Vazamento]]

## Evidências nas fontes

Zheng e Casari (2018), cap. 2; Ozdemir (2022), caps. 2–4 e 7; Duboue (2020), caps. 2–3; Campesato (2024), caps. 5–6.
