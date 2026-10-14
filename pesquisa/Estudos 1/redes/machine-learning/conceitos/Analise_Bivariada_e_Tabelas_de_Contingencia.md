---
title: "Análise Bivariada e Tabelas de Contingência"
type: "conceito"
network: "machine-learning"
area: "EDA e relações entre variáveis"
status: "rascunho"
source_ids:
  - "TUKEY-1977"
  - "CASTRO-2026"
  - "OLULEYE-2023"
tags:
  - conceito
  - eda
  - analise-bivariada
---

# Análise Bivariada e Tabelas de Contingência

## Definição

Análise bivariada descreve como duas variáveis variam em conjunto. O método depende dos tipos: associação numérica, comparação de medida entre categorias ou dependência entre categorias. A tabela de contingência cruza frequências de categorias e permite examinar proporções condicionais, sempre com denominador explícito.

## Técnicas

- Numérica × numérica: scatterplot, Pearson para associação linear e Spearman para associação monotônica baseada em postos; inspecione forma, grupos e extremos antes do coeficiente.
- Numérica × categórica: box/violin/ECDF por grupo, pontos individuais quando a amostra permitir e resumos com tamanho de cada grupo.
- Categórica × categórica: crosstab, contagens, percentuais por linha/coluna e mapas de calor.
- Comparação de grupos: gráficos paralelos/condicionais e resíduos de modelos simples para encontrar desvios sistemáticos.

## Como interpretar

Primeiro verifique unidades, amostra e padrão dos pontos. Depois escolha um resumo compatível com a forma e reporte tamanho amostral. Correlação é uma medida de associação e pode ocultar curvatura, subgrupos, restrição de faixa, valores influentes e relações não lineares. Tabelas com totais iguais podem ter distribuições condicionais diferentes.

## Limitações

Associação não implica causa; confundimento e seleção podem explicar padrões. Pearson não resume bem associação não linear; Spearman também não encontra toda estrutura. Crosstabs ficam esparsas com muitas categorias. Ajuste múltiplas comparações e preserve hipóteses formuladas antes de inspecionar muitas combinações.

## Relações

- [[redes/machine-learning/conceitos/Visualizacao_Exploratoria_e_Codificacao_Visual|Visualização Exploratória e Codificação Visual]]
- [[redes/machine-learning/conceitos/Estatisticas_Resistentes_e_Formas_de_Distribuicao|Estatísticas Resistentes e Formas de Distribuição]]
- [[redes/machine-learning/conceitos/Reexpressao_de_Variaveis|Reexpressão de Variáveis]]
- [[redes/machine-learning/conceitos/Analise_Multivariada_Exploratoria|Análise Multivariada Exploratória]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]

## Evidência nas fontes

Castro (2026), capítulo 3 (contingência, associação, covariância/correlação) e capítulo 5 (scatter, pairplot, heatmap). Oluleye (2023), capítulo 5 (scatter, crosstab, pivot, pairplot e correlação). Tukey (1977), capítulos 4–6 e 10–14, cobre comparação de grupos, gráficos de relação, reexpressão, resíduos e análises por duas ou mais direções.

## Perguntas de revisão

1. Quais são os tipos das duas variáveis e qual representação corresponde a cada uma?
2. A associação é linear, monotônica, por grupo ou condicionada a outra variável?
3. Os denominadores e tamanhos de grupo estão visíveis?
4. Que confundidor, seleção ou agrupamento pode explicar a associação?
