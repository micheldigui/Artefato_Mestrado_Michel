---
title: "Reexpressão de Variáveis"
type: "conceito"
network: "machine-learning"
area: "EDA e transformações"
status: "rascunho"
source_ids:
  - "TUKEY-1977"
  - "ATWAN-2022"
tags:
  - conceito
  - eda
  - transformacoes
---

# Reexpressão de Variáveis

## Definição

Reexpressão transforma a escala de uma ou mais variáveis para tornar padrões mais legíveis, reduzir assimetria extrema, estabilizar variação ou aproximar uma relação de uma forma simples. Tukey descreve comparações orientadas por logs, raízes e recíprocos; séries temporais também podem exigir transformações de potência antes de decomposição/modelagem.

## Como aplicar

1. Inspecione valores válidos, sinal, zeros e significado da unidade.
2. Formule o propósito: facilitar leitura, linearizar associação, estabilizar variância ou preparar um modelo.
3. Compare escala original e reexpressões em gráficos e resíduos; registre parâmetros e inversão da transformação.
4. Ajuste qualquer parâmetro aprendido usando apenas o treino em pipelines preditivos.
5. Interprete resultados de volta na escala de negócio quando possível.

## Exemplos e restrições

- Log pode reduzir assimetria positiva, mas exige tratar zeros/negativos com regra justificada.
- Raiz pode ser adequada para contagens não negativas em certas situações.
- Recíproco altera fortemente valores próximos de zero e não serve com zero sem decisão explícita.
- Diferenciação em séries representa mudanças entre tempos adjacentes e remove informação de nível; registre ordem e alinhamento.

## Limitações

Transformação não corrige amostragem enviesada, outliers inválidos ou relação causal mal definida. A aparência de normalidade não é um objetivo universal. Comparações de erro devem voltar à escala original quando a métrica e a decisão de negócio forem definidas nela.

## Relações

- [[redes/machine-learning/conceitos/Estatisticas_Resistentes_e_Formas_de_Distribuicao|Estatísticas Resistentes e Formas de Distribuição]]
- [[redes/machine-learning/conceitos/Analise_Bivariada_e_Tabelas_de_Contingencia|Análise Bivariada e Tabelas de Contingência]]
- [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|Diagnóstico Exploratório de Séries Temporais]]
- [[redes/machine-learning/conceitos/Normalização_e_Padronização|Normalização e Padronização]]
- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]

## Evidência nas fontes

Tukey (1977), capítulos 3, 5–6, 10–13 e 17, discute reexpressões por logs/raízes/recíprocos e seu uso em relações, ajustes e contagens. Atwan (2022), capítulo 9, inclui transformações de potência e diferenciação no diagnóstico de séries temporais.

## Perguntas de revisão

1. Que problema a reexpressão deve resolver?
2. Há zeros ou valores negativos que tornam a transformação inválida?
3. Como interpretar previsão ou coeficiente na escala original?
4. A transformação foi ajustada somente nos dados de treino?
