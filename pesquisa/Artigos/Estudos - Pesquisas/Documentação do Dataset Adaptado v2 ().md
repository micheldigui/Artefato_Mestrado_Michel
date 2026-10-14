---
source_file: "Documentação do Dataset Adaptado v2 ().pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Documentação do Dataset Adaptado v2 ().pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "c83b5e01099ecc61066f53d3c657954222b8c256f4c38969553907f6c883d27f"
extracted_at: "2026-09-20T00:51:22.086930"
---

## Documentação do Dataset Adaptado v2 ( dref\_adaptado\_v2.csv )

Este documento descreve as alterações e regras aplicadas na criação do dataset dref\_adaptado\_v2.csv , que visa refletir de forma mais precisa a demanda de refeições considerando dias letivos, fins de semana, feriados e "emendas" de feriados (pontes) em São Paulo, Brasil, para o período coberto pelo arquivo dref.xlsx original (Fevereiro de 2023).

## 1. Objetivo da Adaptação

A principal meta desta versão do dataset é ajustar a demanda ( actual\_demand ) para zero em dias não letivos e garantir que todas as features relacionadas (como lags de demanda, tipo de evento, e cardápio) sejam consistentes com essa realidade. Isso melhora a qualidade dos dados para treinar modelos de predição de demanda.

## 2. Regras Aplicadas e Processo de Criação

O processo seguiu as seguintes etapas:

## 2.1. Identificação do Período do Dataset

O período de datas foi extraído do arquivo dref.xlsx original, compreendendo de 2023-02-06 a 2023-02-28.

## 2.2. Identificação de Dias Sem Aula

Foram considerados como "dias sem aula": * Sábados e Domingos: Todos os sábados e domingos dentro do período foram marcados. * Feriados Nacionais (Brasil): Utilizou-se a biblioteca holidays para identificar os feriados nacionais brasileiros no ano de 2023. Para o período de Fevereiro de 2023, os feriados relevantes de Carnaval (Segunda e Terça-feira) foram considerados. A Quarta-feira de Cinzas (2023-02-22) também foi explicitamente adicionada como um dia não letivo para o contexto escolar, mesmo que tecnicamente possa ser ponto facultativo ou meio período. * Emendas de Feriados (Pontes): * Se um feriado ocorreu em uma terça-feira , a segunda-feira anterior foi considerada "emendada" (ponte) e marcada como dia sem aula, desde que essa segunda-feira não fosse ela mesma um feriado ou fim de semana. * Se um feriado ocorreu em uma quinta-feira , a sexta-feira seguinte foi considerada "emendada" (ponte) e marcada como dia sem aula, desde que essa sexta-feira não fosse ela mesma um feriado ou fim de semana. * No período analisado (Fev/2023), não houve feriados na terça ou quinta que gerassem pontes segundo esta regra e os feriados de Carnaval já cobriam segunda e terça.

## 2.3. Ajuste da Demanda ( actual\_demand )

- A demanda original foi calculada a partir do arquivo dref.xlsx (contando registros com STATUS == "SERVIDA" por dia, ou todas as entradas por dia se a coluna STATUS não existisse). ·
- Para todos os dias identificados como "dias sem aula" (sábados, domingos, feriados, pontes), a coluna actual\_demand foi definida como 0 . ·
- Para os demais dias (dias letivos normais), a actual\_demand manteve o valor original. Se não houvesse consumo registrado em um dia letivo, a demanda também seria 0. ·

## 2.4. Criação da Feature event\_type

Uma coluna event\_type foi criada para categorizar cada dia: * FIM\_DE\_SEMANA : Para sábados e domingos. * FERIADO (Nome do Feriado) : Para os feriados identificados (ex: FERIADO (Carnaval) , FERIADO (Quarta-feira de Cinzas (Considerado Não Letivo)) ). * PONTE\_FERIADO : Para os dias de emenda (não ocorreu no período de Fev/2023). * DIA\_LETIVO\_NORMAL : Para todos os outros dias.

## 2.5. Ajuste de Outras Features para Dias Sem Aula

- main\_dish (Prato Principal): Para os dias identificados como sem aula ( FIM\_DE\_SEMANA , FERIADO , PONTE\_FERIADO ), o main\_dish foi definido como "SEM\_REFEICAO" . ·
- rain\_forecast\_mm (Previsão de Chuva): Para os dias sem aula, a previsão de chuva foi definida como 0 . ·

## 2.6. Recálculo das Features de Lag de Demanda

As features de lag ( lag\_1d - demanda do dia anterior, lag\_7d - demanda de 7 dias antes) foram recalculadas com base na coluna actual\_demand já ajustada (com zeros para dias sem aula). Isso garante que os lags reflitam a demanda real, incluindo os dias sem consumo.

## 2.7. Outras Features Mantidas ou Geradas

- Features de Data: day\_of\_week , month , day\_of\_month , week\_of\_year foram mantidas/geradas. ·
- Features de Clima (Fictícias): max\_temp\_forecast foi mantida com valores fictícios gerados aleatoriamente (exceto rain\_forecast\_mm que foi ajustada como descrito acima). ·
- One-Hot Encoding: As features categóricas main\_dish e event\_type foram transformadas usando one-hot encoding, gerando novas colunas (ex: dish\_Frango Grelhado , event\_DIA\_LETIVO\_NORMAL ). ·

## 3. Estrutura do Arquivo dref\_adaptado\_v2.csv

O arquivo CSV final contém as seguintes colunas (a ordem pode variar ligeiramente):

- date : Data (índice do DataFrame). ·
- actual\_demand : Demanda real de refeições (ajustada para 0 em dias sem aula). ·
- day\_of\_week : Dia da semana (Segunda=0, Domingo=6). ·
- month : Mês. ·
- day\_of\_month : Dia do mês. ·
- week\_of\_year : Semana do ano. ·
- max\_temp\_forecast : Previsão de temperatura máxima (fictícia). ·
- rain\_forecast\_mm : Previsão de chuva em mm (ajustada para 0 em dias sem aula). ·
- lag\_1d : Demanda do dia anterior (baseada na actual\_demand ajustada). ·
- lag\_7d : Demanda de 7 dias antes (baseada na actual\_demand ajustada). ·
- Colunas dish\_* : Resultantes do one-hot encoding da feature main\_dish (ex: dish\_Frango Grelhado , dish\_SEM\_REFEICAO ). ·
- Colunas event\_* : Resultantes do one-hot encoding da feature event\_type (ex: event\_DIA\_LETIVO\_NORMAL , event\_FIM\_DE\_SEMANA , event\_FERIADO (Carnaval) ). ·

Este dataset está mais robusto para modelagem, pois considera explicitamente os dias sem atividades escolares e seu impacto na demanda de refeições.