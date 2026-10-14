---
title: "Suavização e Comparação de Sequências"
type: "conceito"
network: "machine-learning"
area: "EDA temporal e comparação de grupos"
status: "rascunho"
source_ids:
  - "TUKEY-1977"
  - "OLULEYE-2023"
tags:
  - conceito
  - eda
  - suavizacao
---

# Suavização e Comparação de Sequências

## Definição

Suavização resume variação local ao longo de uma ordem (tempo, distância ou índice legítimo) para tornar tendência e forma mais legíveis. Comparação de sequências usa gráficos alinhados, medianas, quantis ou suavizadores para examinar diferenças entre grupos ou trajetórias.

## Métodos observados nas fontes

- Medianas móveis, incluindo a mediana de três pontos, e suavizações sucessivas.
- Suavização tipo Hanning e métodos de “rough/smooth” discutidos por Tukey.
- Médias móveis e suavização exponencial em séries no cookbook de Oluleye.
- Gráficos esquemáticos paralelos/“wandering” para comparar grupos e trajetórias em relações x-y.

## Como usar

Confirme uma ordem que tenha significado, defina janela e tratamento de borda, compare dados originais e suavizados e faça facetas por grupo quando necessário. Registre se o filtro é causal ou usa pontos futuros. Use a curva como instrumento exploratório; quando o objetivo for previsão, reconstrua features dentro de validação sem informação futura.

## Limitações

Suavizar pode apagar picos, mudanças abruptas, sazonalidade curta e eventos raros. Janela muito larga distorce timing; janela curta preserva ruído. Não interprete a linha suavizada como dado medido ou evidência causal.

## Relações

- [[redes/machine-learning/conceitos/Analise_Bivariada_e_Tabelas_de_Contingencia|Análise Bivariada e Tabelas de Contingência]]
- [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|Diagnóstico Exploratório de Séries Temporais]]
- [[redes/machine-learning/conceitos/Estatisticas_Resistentes_e_Formas_de_Distribuicao|Estatísticas Resistentes e Formas de Distribuição]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]

## Evidência nas fontes

Tukey (1977), capítulos 7–9 e 16, cobre suavização de sequências, medianas de três, Hanning, séries e comparação de grupos. Oluleye (2023), capítulo 7, inclui médias móveis e suavização exponencial para dados temporais.

## Perguntas de revisão

1. Qual é a ordem e o fenômeno que ela representa?
2. A janela usa observações futuras?
3. Que sinal pode desaparecer com a suavização?
4. A comparação entre grupos mantém a mesma escala e período?
