---
source_file: "Descrição das Colunas do Dataset Adaptado ().pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Descrição das Colunas do Dataset Adaptado ().pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "31e533067b90805ac5b6ca36ba7ccb40c279dd6e2117eebcecc0579b4e20c136"
extracted_at: "2026-09-20T00:50:59.205891"
---

## Descrição das Colunas do Dataset Adaptado ( dref\_adaptado.csv )

Este documento descreve cada coluna presente no arquivo dref\_adaptado.csv , que foi gerado a partir do arquivo dref.xlsx com a adição de variáveis e dados fictícios para fins de teste. O índice do arquivo CSV é a DATA .

## Colunas:

- DATA (Índice): 1.
- Descrição: A data específica (AAAA-MM-DD) à qual todas as informações da linha se referem. ◦
- Origem: Derivada da coluna DATA original, expandida para cobrir todos os dias contínuos dentro do intervalo mínimo e máximo encontrado no dataset original. ◦
- day\_of\_week: 2.
- Descrição: Representa o dia da semana como um número inteiro, onde Segunda-feira é 0 e Domingo é 6. ◦
- Origem: Derivada da coluna DATA (índice). ◦
- month: 3.
- Descrição: Representa o mês do ano como um número inteiro (1 para Janeiro, 12 para Dezembro). ◦
- Origem: Derivada da coluna DATA (índice). ◦
- day\_of\_year: 4.
- Descrição: Representa o dia do ano como um número inteiro (1 a 365 ou 366 em anos bissextos). ◦
- Origem: Derivada da coluna DATA (índice). ◦
- main\_dish: 5.
- Descrição: Indica o tipo principal de refeição oferecida no dia. Os valores foram simplificados para: ◦
- TRADICIONAL : Refeição com opção proteica de carne. ▪
- VEGETARIANO : Refeição com opção proteica sem carne. ▪
- SEM CARDAPIO : Indica dias onde não havia informação de cardápio no dataset original (provavelmente fins de semana ou dias não letivos). ▪
- Origem: Derivada da coluna REFEIÇÃO original. Foi considerada a primeira entrada de refeição para cada dia (simplificação) e os nomes foram padronizados. Dias sem informação foram preenchidos com SEM CARDAPIO . ◦
- max\_temp\_forecast: 6.
- Descrição: Previsão fictícia da temperatura máxima para o dia, em graus Celsius (°C). ◦
- Origem: Dados fictícios gerados aleatoriamente com uma leve variação sazonal (valores tendem a ser maiores nos meses de verão). ◦
- rain\_forecast: 7.
- Descrição: Previsão fictícia de chuva para o dia. Os valores são: ◦
- 1 : Indica que foi previsto chuva. ▪
- 0 : Indica que não foi previsto chuva. ▪
- Origem: Dados fictícios gerados aleatoriamente, com uma probabilidade ligeiramente maior de chuva nos meses de verão. ◦
- event\_type: 8.
- Descrição: Indica o tipo de evento ou característica do dia. Os valores possíveis são: ◦
- NORMAL : Dia letivo comum. ▪
- FERIADO : Feriado nacional (baseado em datas fixas de exemplo). ▪
- EVENTO\_ESCOLAR : Dia com algum evento escolar (gerado aleatoriamente em algumas terças-feiras como exemplo). ▪
- PERIODO\_PROVAS : Dia dentro de uma semana de provas (baseado em um intervalo de datas de exemplo). ▪
- FIM\_DE\_SEMANA : Sábado ou Domingo. ▪
- Origem: Dados fictícios gerados com base em regras aplicadas à DATA e ao day\_of\_week . ◦
- lag\_1d a lag\_7d: 9.
- Descrição: Representam a demanda real ( actual\_demand ) observada nos dias anteriores. lag\_1d é a demanda do dia anterior, lag\_2d é a demanda de dois dias antes, e assim por diante, até 7 dias antes. ◦
- Origem: Derivadas da coluna actual\_demand através de deslocamento temporal (shift). Valores NaN (gerados no início da série) foram preenchidos com 0. ◦
- actual\_demand: 10.
- Descrição: A variável alvo. Representa o número total de refeições efetivamente servidas naquele dia específico. ◦
- Origem: Derivada do dataset original ( dref.xlsx ) contando o número de linhas onde a coluna SERVIDA tinha o valor SERVIDA para cada DATA . Dias sem nenhuma refeição servida (ou sem dados) foram preenchidos com 0. ◦