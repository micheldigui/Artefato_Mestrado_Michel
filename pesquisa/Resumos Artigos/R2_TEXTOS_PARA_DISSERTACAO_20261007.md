# R² — textos e localização para a dissertação

Documento conferido: `Dissertacao_Michel_qualificacao_resultados_parciais_20261006.docx`. Os textos abaixo são propostas de substituição manual. O documento não foi alterado.

## 1. Seção principal: 5.7

Localizar o título **“5.7 Por que a análise prioriza MAE, WAPE e indicadores operacionais”**. Substituir o título e os três parágrafos seguintes pelo texto abaixo. O próximo título é **“5.8 Comparação pareada com o planejamento baseado em reservas”**.

### 5.7 R² e interpretação conjunta das métricas preditivas

O coeficiente de determinação (R²) foi calculado como medida complementar a partir das previsões da avaliação temporal. Seu valor corresponde a um menos a razão entre a soma dos erros quadráticos e a soma dos quadrados dos desvios do consumo em relação à média do conjunto avaliado. Um valor de zero corresponde ao erro de uma estimativa constante igual a essa média, enquanto valores negativos indicam erro maior que essa referência matemática. A média do conjunto avaliado não constitui uma previsão disponível antecipadamente. O R² também não representa percentual de previsões corretas nem comprova relações causais entre os atributos e o consumo.

Entre os métodos apresentados na Tabela 3, CatBoost obteve R² de 0,333 na linha-base, com 400 datas, e a regressão bayesiana obteve 0,454 na linha expandida, com 415 datas. Esses valores indicam redução do erro quadrático em relação à referência constante, mas também evidenciam variação do consumo não reproduzida pelas previsões. Como as linhas abrangem datas diferentes, a diferença entre seus R² não isola o efeito do acréscimo de fontes.

A interpretação desses resultados considera a finalidade preditiva e o contexto de aplicação. Shmueli (2010) distingue ajuste explicativo de desempenho em novas observações. Em um estudo de desfechos sociais com 160 equipes, Salganik et al. (2020) encontraram R² fora da amostra em torno de 0,20 para alguns desfechos, mesmo com uma base longitudinal extensa. O estudo evidencia limites de previsão naquele contexto, sem estabelecer que esse valor seja satisfatório para outras aplicações. Abelson (1985) e Funder e Ozer (2019) discutem a importância de avaliar a relevância prática dos resultados junto às proporções de variância e aos tamanhos de efeito. Essas contribuições não definem um limiar de aceitação para a previsão de refeições.

No contexto de alimentação coletiva, Posch et al. (2022) descrevem sazonalidades, mudanças de tendência, lacunas e valores atípicos em séries de demanda de restaurantes e cantinas. Na presente pesquisa, valores de R² inferiores a 0,50 são interpretados junto a MAE, RMSE, WAPE e viés, à variação anual e à comparação com as reservas nas mesmas datas. A magnitude dos erros em refeições permanece relevante para o planejamento. A possível utilidade das previsões, inclusive pela antecedência entregue, depende de avaliação prospectiva.

Excesso e déficit potenciais descrevem diferenças entre os planos simulados e o consumo observado. O acréscimo de margem modifica a quantidade planejada, enquanto o R² da previsão pura permanece associado à estimativa original. Sobras físicas e refeições não atendidas exigem registros próprios e não podem ser inferidas apenas dessas métricas.

## 2. Ajuste correspondente em 3.5

### Localizar

“As métricas preditivas foram MAE, RMSE, WAPE e viés.”

### Substituir apenas essa primeira frase por

“As métricas preditivas foram MAE, RMSE, WAPE, viés e, como medida complementar, R².”

O restante do parágrafo, a partir de **“Para os planos, foram calculados...”**, pode ser mantido.

### Localizar o parágrafo

“O R² não foi adotado como critério central do benchmark; a análise prioriza erro em refeições, erro proporcional e viés, além de indicadores decisórios separados. Essa escolha acompanha a distinção entre explicação e previsão discutida por Shmueli e Koppius (2010).”

### Substituir por

“O R² foi calculado diretamente sobre as previsões de cada conjunto de datas comparáveis, usando a média do consumo desse conjunto como referência no denominador. O resultado agregado não corresponde à média dos R² semanais. Sua interpretação complementa MAE, RMSE, WAPE e viés, preservando a distinção entre previsão e indicadores do plano. A avaliação em observações não utilizadas no treinamento considera a finalidade preditiva do estudo (SHMUELI, 2010).”

**Início do próximo parágrafo:** “Após a etapa preditiva, a metodologia considerou políticas de margem de segurança.”

## 3. Ajuste conceitual em 2.4.1 — Métricas e consequências operacionais

### Localizar o parágrafo

“O coeficiente de determinação (R²) pode auxiliar na descrição da relação entre os valores observados e as estimativas produzidas pelo modelo. Entretanto, esse indicador não expressa diretamente quantas refeições foram superestimadas ou subestimadas, nem informa o impacto da previsão sobre sobra, falta ou atendimento. Em estudos aplicados, portanto, um R² elevado não garante, por si só, uma decisão operacional mais adequada. A escolha das métricas deve considerar a finalidade preditiva e o contexto de utilização dos resultados (SHMUELI; KOPPIUS, 2010).”

### Substituir por

“O coeficiente de determinação (R²) relaciona o erro quadrático das estimativas à variação dos valores observados em torno de sua média. Na avaliação fora da amostra, pode assumir valores negativos. Sua interpretação deve considerar o conjunto avaliado e a finalidade preditiva, pois o ajuste aos dados de treinamento não garante desempenho em novas observações (SHMUELI, 2010). O indicador complementa as medidas de erro, mas não informa diretamente a quantidade de refeições superestimadas ou subestimadas nem comprova efeitos sobre desperdício ou atendimento.”

**Início do próximo parágrafo:** “A discussão sobre MAE e RMSE também evidencia que diferentes métricas enfatizam aspectos distintos do erro.”

## 4. Coluna de R² para a Tabela 3

Valores obtidos no diagnóstico separado de 06/10/2026, com as mesmas previsões e datas da Tabela 3. Não houve novo treinamento.

| Linha | Método | R² |
|---|---|---:|
| Base | CatBoost | 0,333 |
| Base | ExtraTrees | 0,306 |
| Base | Ensemble top 3 médio | 0,299 |
| Base | Ensemble top 5 mediano | 0,302 |
| Base | Ensemble top 5 médio | 0,304 |
| Expandida | Regressão bayesiana | 0,454 |
| Expandida | Comitê ponderado pelo desempenho anterior | 0,438 |
| Expandida | Comitê dos cinco melhores, com pesos | 0,406 |
| Expandida | Ensemble top 5 médio | 0,406 |
| Expandida | ExtraTrees | 0,385 |

Fonte: `resultados/teste_r2_linhas_modelos_20261006/r2_metodos_tabela3.csv`. O arredondamento para três casas é apenas de apresentação. As duas linhas têm conjuntos de datas diferentes.

## 5. Referências a acrescentar

ABELSON, R. P. A variance explanation paradox: When a little is a lot. **Psychological Bulletin**, v. 97, n. 1, p. 129–133, 1985. DOI: https://doi.org/10.1037/0033-2909.97.1.129.

FUNDER, D. C.; OZER, D. J. Evaluating effect size in psychological research: Sense and nonsense. **Advances in Methods and Practices in Psychological Science**, v. 2, n. 2, p. 156–168, 2019. DOI: https://doi.org/10.1177/2515245919847202.

POSCH, K.; TRUDEN, C.; HUNGERLÄNDER, P.; PILZ, J. A Bayesian approach for predicting food and beverage sales in staff canteens and restaurants. **International Journal of Forecasting**, v. 38, n. 1, p. 321–338, 2022. DOI: https://doi.org/10.1016/j.ijforecast.2021.06.001.

SALGANIK, M. J. et al. Measuring the predictability of life outcomes with a scientific mass collaboration. **Proceedings of the National Academy of Sciences**, v. 117, n. 15, p. 8398–8403, 2020. DOI: https://doi.org/10.1073/pnas.1915006117.

SHMUELI, G. To explain or to predict? **Statistical Science**, v. 25, n. 3, p. 289–310, 2010. DOI: https://doi.org/10.1214/10-STS330.

Na ficha de Funder e Ozer foi registrada a errata de 2020, DOI https://doi.org/10.1177/2515245920979282, incluída no PDF fornecido. As paráfrases acima evitam reproduzir a explicação corrigida. Não usar os limites de correlação r discutidos no artigo como cortes para R² preditivo.
