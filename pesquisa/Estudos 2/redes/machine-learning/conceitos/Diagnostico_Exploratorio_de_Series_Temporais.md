---
title: "Diagnóstico Exploratório de Séries Temporais"
type: "conceito"
network: "machine-learning"
area: "EDA temporal"
status: "rascunho"
source_ids:
  - "ATWAN-2022"
  - "OLULEYE-2023"
  - "CASTRO-2026"
tags:
  - conceito
  - eda
  - series-temporais
---

# Diagnóstico Exploratório de Séries Temporais

## Definição

É a investigação da ordem, frequência, lacunas, tendência, sazonalidade, dependência e mudanças de regime em observações temporais antes de escolher um modelo ou previsão. A ordem temporal faz parte dos dados: uma visualização embaralhada não preserva a estrutura.

## Estratégias

1. Validar timestamp, fuso, duplicidade, granularidade, calendário e intervalos ausentes.
2. Traçar série completa e segmentos; comparar padrões entre entidades sem misturar frequências.
3. Resumir por hora/dia/semana/mês só quando a agregação fizer sentido; registrar perda de detalhe.
4. Inspecionar tendência e sazonalidade; decompor em componentes quando adequado.
5. Usar suavização para visualizar trajetória, e ACF/PACF para examinar dependência serial; diagnósticos não são prova de um mecanismo.
6. Investigar estabilidade/estacionariedade e mudanças de regime; testar transformação ou diferenciação com propósito explícito.
7. Procurar observações anômalas e padrões de ausência ao longo do tempo; interpolação não deve atravessar regimes sem justificativa.
8. Separar treino e avaliação cronologicamente conforme horizonte e operação.

## Relação com modelos

Tendência, sazonalidade e autocorrelação orientam comparar baselines sazonais, modelos estatísticos de série e modelos supervisionados com lags/calendário. Uma série com eventos recorrentes por entidade pode precisar de split temporal e por grupo. A EDA define hipóteses para comparar, não seleciona ARIMA, Prophet, boosting ou rede neural sem avaliação.

## Limitações

Frequência irregular, calendários, feriados, mudanças de definição e dados revisados podem criar padrões artificiais. Decomposição depende de especificação. ACF/PACF e testes de estacionariedade têm pressupostos. Interpolação pode suavizar extremos e inventar valores; não trate como observação real.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]

- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Suavizacao_e_Comparacao_de_Sequencias|Suavização e Comparação de Sequências]]
- [[redes/machine-learning/conceitos/Tratamento_de_Missing_Values|Tratamento de Missing Values]]
- [[redes/machine-learning/conceitos/Metodos_de_Deteccao_de_Outliers|Métodos de Detecção de Outliers]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]

## Evidência nas fontes

Atwan (2022), capítulos 7–9 e 14: ausências/interpolação, z-score e método de Tukey, visualização, reamostragem, decomposição, transformação de potência, ACF e testes de autocorrelação/estacionariedade. Oluleye (2023), capítulo 7: padrões, decomposição, suavização, estacionariedade e diferenciação. Castro (2026), capítulo 6.1: objetivos, descritiva e visualização temporal, médias móveis e decomposição sazonal.

## Perguntas de revisão

1. Qual frequência e fuso representam a coleta?
2. Há tendência, sazonalidade, autocorrelação ou mudança de regime?
3. O horizonte e o split de validação reproduzem a previsão real?
4. A interpolação ou transformação introduz informação futura?

