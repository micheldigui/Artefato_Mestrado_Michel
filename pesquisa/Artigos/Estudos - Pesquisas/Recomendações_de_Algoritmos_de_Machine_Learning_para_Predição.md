---
source_file: "Recomendações_de_Algoritmos_de_Machine_Learning_para_Predição.pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Recomendações_de_Algoritmos_de_Machine_Learning_para_Predição.pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "1ff1d4f7ceffc5bc9798444e39fddae7a6efa9d51fa7bcc05ce6b2483dcf698d"
extracted_at: "2026-09-20T00:52:12.485369"
---

## Recomendações de Algoritmos de Machine Learning para Predição de Demanda no IFSP

Com base na análise dos algoritmos mencionados nos artigos ( sintese\_variaveis\_algoritmos.md ) e considerando o objetivo de prever a demanda de refeições com duas semanas de antecedência no contexto do IFSP, sugiro a seguinte abordagem para a seleção e teste de algoritmos:

## Algoritmos Mais Promissores (Recomendação Principal)

Estes algoritmos são frequentemente aplicados com sucesso em problemas de previsão de demanda com características semelhantes (séries temporais com múltiplas variáveis explicativas) e foram mencionados ou são relacionados aos citados na literatura analisada:

## Modelos Baseados em Árvores de Decisão (Gradient Boosting): 1.

- Algoritmos Específicos: XGBoost , LightGBM . ◦
- Justificativa: ◦
- Alto Desempenho: Frequentemente alcançam alta acurácia em competições e problemas práticos de previsão com dados tabulares. ▪
- Flexibilidade com Features: Lidam bem com uma mistura de variáveis numéricas (histórico de demanda, temperatura) e categóricas (dia da semana, tipo de cardápio, eventos, curso, série), além de capturar interações complexas entre elas. ▪
- Robustez: Menos sensíveis a outliers e dados faltantes em comparação com alguns outros métodos. ▪
- Referência na Literatura: XGBoost e LightGBM foram explicitamente mencionados no artigo do IJIRMPS como aplicados à previsão de demanda na cadeia alimentar. ▪
- Horizonte de Previsão: Podem ser estruturados para prever múltiplos passos à frente (como as 2 semanas necessárias), embora isso exija uma estratégia de modelagem específica (ex: previsão direta ou recursiva). ▪
- Considerações: Podem exigir algum ajuste de hiperparâmetros para otimizar o desempenho. ◦
- Random Forest: 2.
- Justificativa: ◦
- Boa Performance e Robustez: Similar aos modelos de gradient boosting em termos de lidar com diferentes tipos de features e nãolinearidades, embora às vezes um pouco menos acurado que XGBoost/ LightGBM. ▪
- Menor Risco de Overfitting (comparado a uma única árvore): A agregação de múltiplas árvores torna o modelo mais estável. ▪
- Referência na Literatura: Mencionado no artigo sobre tecnologias eficientes. ▪
- Interpretabilidade Relativa: É possível obter métricas de importância das variáveis, ajudando a entender quais fatores mais influenciam a predição. ▪
- Considerações: Pode ser computacionalmente mais intensivo que LightGBM para grandes datasets. ◦

## Algoritmos para Baseline ou Abordagens Complementares

- Modelos Estatísticos de Séries Temporais: 1.
- Algoritmos Específicos: SARIMA , Prophet (desenvolvido pelo Facebook, bom para dados com sazonalidade e feriados). ◦
- Justificativa: ◦
- Baseline: Servem como um bom ponto de partida para comparar o desempenho dos modelos de ML mais complexos. Se um modelo de ML não superar significativamente um SARIMA/Prophet bem ajustado, a complexidade adicional pode não ser justificada. ▪
- Interpretabilidade: Geralmente mais fáceis de interpretar e explicar os componentes de tendência e sazonalidade. ▪
- Referência na Literatura: SARIMA foi mencionado no artigo do IJIRMPS. ▪
- Considerações: Podem ter mais dificuldade em incorporar um grande número de variáveis externas (exógenas) de forma eficaz, especialmente se as relações forem não-lineares. O Prophet lida bem com feriados e eventos. ◦

## Redes Neurais (Recorrentes/LSTMs): 2.

- Justificativa: ◦
- Potencial para Alta Acurácia: Excelentes para capturar padrões complexos e dependências temporais longas em dados sequenciais. ▪
- Referência na Literatura: Mencionado genericamente como Deep Learning no artigo da ScienceDirect. ▪

## Considerações: ◦

- Complexidade: Exigem mais dados para treinamento, maior esforço em engenharia de features e ajuste de arquitetura/hiperparâmetros. ▪
- Recursos Computacionais: O treinamento pode ser demorado e exigir hardware mais potente (GPU). ▪
- Menor Interpretabilidade: Geralmente são considerados modelos "caixa-preta". ▪
- Recomendação: Considerar apenas se os modelos baseados em árvores ou Prophet/SARIMA não atingirem a acurácia desejada e houver dados e recursos suficientes. ▪

## Sugestão de Abordagem Prática

- Comece com Modelos Baseados em Árvores: Implemente e avalie XGBoost ou LightGBM , utilizando todas as variáveis relevantes coletadas e criadas (histórico, data, eventos, cardápio, etc.). 1.
- Estabeleça um Baseline: Implemente um modelo SARIMA ou Prophet utilizando principalmente o histórico de demanda e variáveis temporais/eventos como referência de desempenho. 2.
- Compare: Avalie a acurácia (usando métricas apropriadas como MAE, RMSE, MAPE) dos modelos de árvore contra o baseline no horizonte de 2 semanas. 3.
- Itere: Refine as features, ajuste hiperparâmetros dos modelos de árvore. Se a acurácia ainda não for satisfatória, considere explorar Redes Neurais (LSTM). 4.

Essa abordagem equilibra a busca por alta acurácia com a praticidade de implementação e interpretabilidade.