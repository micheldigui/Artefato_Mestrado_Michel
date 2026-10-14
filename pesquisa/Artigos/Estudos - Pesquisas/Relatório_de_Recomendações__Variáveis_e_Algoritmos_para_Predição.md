---
source_file: "Relatório_de_Recomendações__Variáveis_e_Algoritmos_para_Predição.pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Relatório_de_Recomendações__Variáveis_e_Algoritmos_para_Predição.pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "3ff500366a79997ba53e70520ca7ab550f9c8f2e085a10dfbcff91e960fac050"
extracted_at: "2026-09-20T00:52:48.480947"
---

## Relatório de Recomendações: Variáveis e Algoritmos para Predição de Demanda de Refeições no IFSP Itaquaquecetuba

## Introdução

Este relatório consolida as análises e recomendações sobre variáveis importantes e algoritmos de Machine Learning (ML) promissores para a predição da demanda de refeições no IFSP Campus Itaquaquecetuba. O objetivo é apoiar a iniciativa de prever o quantitativo de refeições com duas semanas de antecedência, visando otimizar a compra de insumos, reduzir o desperdício de alimentos e, consequentemente, diminuir as despesas da instituição. As recomendações baseiam-se na análise dos artigos científicos relevantes identificados anteriormente (listados nos relatórios relatorio\_selecao\_artigos.md e relatorio\_novos\_artigos.md ) e consideram o contexto específico e os dados já

coletados pelo IFSP (data da refeição, código do aluno, série, curso).

## Recomendações de Variáveis Adicionais

## Recomendações de Variáveis Adicionais para Predição de Demanda no IFSP

Com base na análise da literatura (sintetizada em sintese\_variaveis\_algoritmos.md ) e considerando as variáveis que você já coleta ( Data da refeição , Código do aluno , Série , Curso ), recomendo fortemente a coleta e utilização das seguintes variáveis adicionais para melhorar a acurácia da predição de demanda de refeições com duas semanas de antecedência:

## Variáveis Altamente Recomendadas

Estas variáveis tendem a ter um impacto significativo nos modelos preditivos e são frequentemente citadas na literatura:

## Histórico de Demanda Agregada: 1.

- Descrição: Quantidade total de refeições efetivamente reservadas ou servidas em cada dia passado. ◦
- Justificativa: É um dos preditores mais fortes. Padrões passados de consumo são essenciais para prever o futuro. É crucial ter o histórico diário agregado. ◦
- Coleta: Manter um registro diário do número total de reservas confirmadas ou refeições servidas. ◦

## Dia da Semana: 2.

- Descrição: Identificar o dia da semana (segunda, terça, ..., sexta). ◦
- Justificativa: O consumo pode variar significativamente dependendo do dia da semana devido a horários de aulas ou outras rotinas. ◦
- Coleta: Facilmente derivado da Data da refeição . ◦

## Calendário Acadêmico e Eventos: 3.

- Descrição: Marcar dias que são feriados (nacionais, locais, pontos facultativos), início e fim de semestre, períodos de férias, semanas de provas, eventos especiais no campus (palestras, feiras, competições) que possam alterar a presença normal dos alunos. ◦
- Justificativa: Eventos e feriados causam grandes desvios na demanda normal e precisam ser explicitamente informados ao modelo. ◦
- Coleta: Obter o calendário acadêmico oficial e registrar eventos relevantes com antecedência. ◦

## Cardápio Específico (Características Principais): 4.

- Descrição: Registrar informações sobre o prato principal ou características marcantes do cardápio do dia (ex: "Frango Assado", "Feijoada", "Opção Vegetariana Principal", etc.). ◦
- Justificativa: A popularidade de certos pratos influencia diretamente a adesão dos alunos. O modelo pode aprender quais cardápios geram mais ou menos demanda. ◦
- Coleta: Obter o planejamento de cardápios com a mesma antecedência da necessidade de predição (2 semanas). ◦

## Variáveis Recomendadas (Potencialmente Úteis)

Estas variáveis podem agregar valor dependendo da disponibilidade e facilidade de coleta:

## Condições Climáticas (Previstas): 1.

- Descrição: Temperatura máxima prevista, previsão de chuva (sim/não ou intensidade) para o dia da refeição. ◦
- Justificativa: Condições climáticas extremas (muito calor, chuva forte) podem influenciar a decisão dos alunos de permanecer no campus para a refeição. ◦
- Coleta: Utilizar serviços de previsão do tempo que ofereçam dados com 2 semanas de antecedência para Itaquaquecetuba. ◦

## Número de Alunos Esperados no Campus (se disponível): 2.

- Descrição: Alguma estimativa do número total de alunos esperados no campus naquele dia (talvez baseado no total de matriculados por curso/série com aulas naquele dia). ◦
- Justificativa: Modela a população potencial que pode reservar a refeição. ◦
- Coleta: Pode ser derivado dos dados de matrícula e horários, mas pode ser complexo de estimar com precisão. ◦

## Variáveis a Considerar (Menor Prioridade Inicial)

## Turno do Aluno: 1.

- Descrição: Manhã, Tarde, Noite. ◦
- Justificativa: Alunos de diferentes turnos podem ter padrões de consumo distintos. ◦
- Coleta: Provavelmente associado ao Curso ou Série . ◦

## Comparação com Variáveis Atuais

- Data da refeição : Essencial, já coletada. Permite derivar Dia da Semana, Mês, etc. ·
- Código do aluno : Útil para análises individuais, mas para a predição agregada (quantitativo total), o histórico agregado (item 1) é mais direto. Pode ser usado para criar features agregadas por Série ou Curso . ·
- Série e Curso : Já coletadas. Podem ser usadas para identificar padrões de grupos específicos, embora o impacto na predição agregada precise ser avaliado. ·

Próximos Passos: Sugiro focar na coleta e estruturação das variáveis Altamente Recomendadas , especialmente o Histórico de Demanda Agregada e informações do Calendário/Eventos e Cardápio . Estas, combinadas com a data, já formam uma base sólida para iniciar a modelagem preditiva.

## Recomendações de Algoritmos de Machine Learning

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

## Random Forest: 2.

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
- Considerações: ◦
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