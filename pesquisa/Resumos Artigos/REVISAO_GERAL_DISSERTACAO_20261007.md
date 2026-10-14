# Revisão geral da dissertação — ajustes manuais

Arquivo revisado: `Dissertacao_Michel_qualificacao_resultados_parciais_20261006.docx`, na versão disponível em 7 de outubro de 2026.

Foram lidos o texto integral, as 30 tabelas e quadros, as referências e os sete comentários existentes. Também foram inspecionadas as 22 imagens incorporadas. O documento não foi alterado. A matriz foi consultada apenas para leitura.

**Limite da revisão:** não foi possível renderizar as páginas, pois o runtime disponível não contém o executável do LibreOffice. Por isso, não foi verificada a paginação final, a quebra das tabelas, o alinhamento nas páginas nem a contagem de folhas. Os achados de conteúdo abaixo são independentes dessa limitação. Não houve novo cálculo de métricas nem auditoria completa do código.

## O que já está adequado

- A nova tabela de R² foi inserida na seção 5.7 como Tabela 4. Os dez valores transcritos correspondem aos valores apresentados no diagnóstico separado e no guia anterior.
- O R² já aparece na fundamentação (2.4.1) e na metodologia (3.5), com distinção entre resultado agregado e média semanal.
- As cinco referências acrescentadas para discutir R² já estão na lista final: Abelson, Funder e Ozer, Posch et al., Salganik et al. e Shmueli.
- Estão identificadas as duas janelas: preparo, de três a sete dias; compras, de dez a quatorze dias. O texto informa que os testes históricos da janela curta não validam a janela longa.
- A previsão pura, as margens moderada e conservadora e a combinação para preparo estão descritas em 4.8 e na Figura 6. A combinação já contém dez refeições de margem.
- A distinção entre excesso/déficit potenciais e resultados efetivos do serviço foi preservada na discussão e nas considerações parciais.
- A diferença entre setembro retrospectivo e emissões realmente anteriores às refeições de outubro está explicitada.
- As legendas das tabelas e a lista de tabelas já seguem a nova sequência de 1 a 11. Restam seis chamadas no corpo do texto com a numeração anterior.

## 1. Correções necessárias

### 1.1 Quantidade de referências — seção 3.2

**Localizar o início:** “A matriz disponível reúne 76 registros de trabalho.”

**Substituir o parágrafo inteiro por:**

A matriz atualizada reúne 81 registros bibliográficos de trabalho. A classificação expressa a relevância atribuída às fontes para a pesquisa; não corresponde à contagem de registros recuperados, duplicatas ou exclusões durante a busca. A distribuição está apresentada na Tabela 1.

**Início do próximo elemento:** “Tabela 1 - Classificação dos registros na matriz de literatura”.

### 1.2 Quantidades da Tabela 1

**Localizar:** “Tabela 1 - Classificação dos registros na matriz de literatura”.

**Substituir as quantidades pelos valores abaixo:**

| Classificação | Quantidade | Função na dissertação |
|---|---:|---|
| Aproveitar fortemente | 23 | Base principal para fundamentação e discussão. |
| Aproveitar parcialmente | 32 | Apoio conceitual, contextual ou metodológico. |
| Apoio pontual | 24 | Técnicas, limitações e trabalhos futuros. |
| Não aproveitar, salvo apoio muito pontual | 2 | Fora do núcleo do referencial. |
| Total analisado | 81 | Registros da matriz. |

Fonte: Elaborado pelo autor (2026).

**Conferência:** 23 + 32 + 24 + 2 = 81. A distribuição anterior era 21 + 31 + 22 + 2 = 76. Foram acrescentados cinco registros: dois de aproveitamento forte, um parcial e dois de apoio pontual.

**Terminologia:** use “registros bibliográficos” ou “referências da matriz”, pois a matriz inclui diferentes tipos de documentos. Não substitua por “81 artigos citados”. A lista final da dissertação contém 45 entradas; ela reúne as fontes citadas no texto, enquanto a matriz documenta o conjunto mais amplo de leituras. Essa diferença, por si só, não é um erro.

### 1.3 Registrar o complemento do levantamento para o R² — seção 3.2

**Local de inserção:** após a fonte da Tabela 1 e antes do parágrafo que começa com “A partir desse mapeamento, o referencial foi organizado em eixos temáticos”.

**Acrescentar:**

O conjunto inicial de 76 registros foi complementado com cinco trabalhos para apoiar a interpretação do R²: Abelson (1985), Funder e Ozer (2019), Shmueli (2010), Salganik et al. (2020) e Posch et al. (2022). Suas contribuições e limites foram registrados na matriz, com foco na distinção entre ajuste e previsão, na relevância prática das métricas e nas particularidades da demanda em serviços de alimentação.

**Ponto a documentar:** se houver registro da busca complementar, acrescente as bases, os termos e a data efetivamente utilizados. A revisão confirmou a leitura e a inclusão dos PDFs; não permite afirmar que esses cinco trabalhos foram recuperados por todas as bases mencionadas no primeiro parágrafo da seção.

### 1.4 Título da seção 5.7

**Localizar:** “5.7 Por que a análise prioriza MAE, WAPE e indicadores operacionais”.

**Substituir por:**

5.7 R² e interpretação conjunta das métricas preditivas

**Início do próximo parágrafo:** “O coeficiente de determinação (R²) foi incluído como medida complementar”.

O primeiro parágrafo está claro e pode ser mantido. Atualize também a entrada correspondente no sumário.

### 1.5 Cabeçalho da Tabela 4

**Localizar:** “Tabela 4 - R² dos métodos com menores MAE em cada linha de avaliação”.

Na última coluna, **substituir “MAE” por “R²”**. Os números de 0,299 a 0,454 são valores de R²; mantenha-os.

**Após a fonte, acrescentar:**

Nota: R² calculado com as mesmas previsões e datas utilizadas na Tabela 3. Os métodos foram selecionados pelos menores MAE em cada linha. As linhas abrangem conjuntos de datas diferentes.

**Início do próximo parágrafo:** “Na linha-base, CatBoost apresentou R² de 0,333”.

### 1.6 Chamada da comparação pareada — seção 5.8

**Localizar o início:** “Na amostra pareada de 390 datas, as reservas tiveram MAE 28,66 e WAPE 20,76%.”

**Substituir o parágrafo inteiro por:**

Na amostra pareada de 390 datas, as reservas tiveram MAE de 28,66 refeições e WAPE de 20,76%. ExtraTrees com histórico de consumo e calendário teve MAE de 22,89 e WAPE de 16,58%; o ensemble com reservas teve MAE de 20,66 e WAPE de 14,96%. Esses valores se referem ao plano puro arredondado para cima. A escolha dos métodos na própria amostra é exploratória. Os erros e as diferenças potenciais entre planos e consumo estão registrados na Tabela 5.

**Próximo elemento:** “Tabela 5 - Comparação pareada de reservas e previsões em 390 datas”.

### 1.7 Chamada dos pagamentos — seção 5.8

**Localizar o início:** “Além da comparação entre planejamento e consumo, os registros administrativos permitem contextualizar”.

**Substituir o parágrafo inteiro por:**

Além da comparação entre planejamento e consumo, os registros administrativos permitem contextualizar o volume de refeições faturadas e os recursos destinados ao serviço. As quantidades faturadas e os valores pagos à Tryx entre 2023 e 2025 estão registrados na Tabela 6.

**Próximo elemento:** “Tabela 6 - Valores pagos à prestadora de serviços, 2023-2025”.

### 1.8 Chamada da seleção temporal — seção 5.9

**Localizar o início:** “As regras selecionadas e seus resultados estão registrados na Tabela 6.”

**Substituir o parágrafo inteiro por:**

As regras selecionadas e seus resultados estão registrados na Tabela 7. O MAE do plano mede a diferença absoluta média entre a quantidade recomendada, já acrescida da margem, e o consumo observado. As colunas “Indicador do plano” e “Indicador das reservas” apresentam a média diária de excesso potencial mais duas vezes o déficit potencial. A última coluna informa a redução percentual desse indicador em relação às reservas.

**Próximo elemento:** “Tabela 7 - Seleção temporal de modelo e margem sob razão hipotética 2:1”.

### 1.9 Chamada das coortes — seção 5.14

**Localizar o início:** “As avaliações apresentadas examinam aspectos distintos do artefato”.

**Substituir o parágrafo inteiro por:**

As avaliações apresentadas examinam aspectos distintos do artefato: o desempenho dos métodos, a contribuição das fontes de dados e as diferenças potenciais entre planejamento e consumo. Nesta seção, as análises são reunidas conforme seus conjuntos de datas e condições de comparação. A finalidade e o alcance de cada avaliação estão resumidos na Tabela 8.

**Início do próximo parágrafo:** “Na competição, os métodos são comparados dentro de cada linha de dados.”

### 1.10 Chamada dos resultados anuais — seção 5.14

**Localizar o início:** “Os resultados anuais do ExtraTrees e das reservas estão registrados na Tabela 9”.

**Substituir o parágrafo inteiro por:**

Os resultados anuais do ExtraTrees e das reservas estão registrados na Tabela 10, para examinar a variação entre períodos.

**Próximo elemento:** “Tabela 10 - MAE e WAPE anuais das configurações e das reservas”.

### 1.11 Chamada da iteração de aprimoramento — seção 5.16

**Localizar o início:** “O MAE do plano, o indicador médio 2:1 e o déficit potencial acumulado estão registrados na Tabela 10”.

**Substituir o parágrafo inteiro por:**

O MAE do plano, o indicador médio 2:1 e o déficit potencial acumulado estão registrados na Tabela 11, nas mesmas datas de cada ano. O indicador médio combina excesso e déficit potenciais, enquanto a última coluna informa apenas a soma das diferenças dos dias em que o plano ficou abaixo do consumo.

**Próximo elemento:** “Tabela 11 - Iteração de aprimoramento com regra escolhida em 2024”.

### 1.12 Reservas históricas e quantitativo atual — Quadro 2, seção 2.6

**Localizar a linha cuja primeira célula começa com:** “Comparação com o quantitativo institucional nas mesmas datas.”

**Substituir as duas primeiras células por:**

| Questão delimitada nesta pesquisa | Encaminhamento da pesquisa |
|---|---|
| Comparação com as reservas históricas e, na etapa prospectiva, com o quantitativo institucional, nas mesmas datas. | Uso das reservas como referência na avaliação retrospectiva e do quantitativo informado pela nutricionista no acompanhamento prospectivo. |

Mantenha a terceira célula: “Análise e discussão dos resultados.”

**Por quê:** a avaliação histórica não utilizou o quantitativo atual da nutricionista. O restante do documento já faz essa distinção.

### 1.13 Parágrafo após o Quadro 2 — seção 2.6

**Localizar o início:** “No Quadro 2, estão relacionadas as questões de planejamento do restaurante”.

**Substituir o parágrafo inteiro por:**

No Quadro 2, estão relacionadas as questões de planejamento do restaurante e os procedimentos adotados para investigá-las. A avaliação retrospectiva compara previsões e reservas históricas nas mesmas datas e examina cenários de margem. O confronto com os quantitativos informados pela nutricionista permanece previsto para o acompanhamento prospectivo. Também são explicitadas as condições necessárias para adaptar o artefato a outro contexto.

**Início do próximo parágrafo:** “A contribuição pretendida é, portanto, aplicada e integrada.”

### 1.14 Contribuição reivindicada — seção 3.1.2

**Localizar o início:** “A contribuição reivindicada é a especificação e a avaliação contextual de um processo semanal”.

**Substituir o parágrafo inteiro por:**

A contribuição reivindicada é a especificação e a avaliação retrospectiva de um processo semanal de previsão e planejamento, com comparação às reservas históricas e separação entre previsão, plano e resultado do serviço. O confronto com o quantitativo informado pela nutricionista e a avaliação da utilidade das duas janelas permanecem previstos para a etapa prospectiva. A pesquisa não propõe um algoritmo novo nem demonstra superioridade universal; a adaptação a outra instituição exige dados locais e nova avaliação (HEVNER et al., 2004).

**Início do próximo parágrafo:** “Para a futura avaliação de uso, a gestora deverá receber”.

### 1.15 Usos dos quantitativos — seção 4.8

**Localizar o início:** “O quantitativo institucional pode participar da avaliação como referência, entrar como atributo de um modelo histórico”.

**Substituir o parágrafo inteiro por:**

Nos experimentos históricos, as reservas foram utilizadas como referência de comparação e como atributo em configurações ampliadas. Nas novas emissões, o quantitativo informado pela nutricionista será avaliado como referência do processo vigente e poderá ser combinado com a previsão para preparo depois de sua geração. A previsão antecipada para compras utiliza consumo anterior, cardápio e calendário, sem depender do quantitativo futuro. Na sexta-feira seguinte, a estimativa das mesmas refeições é atualizada para preparo, preservando a emissão anterior. A previsão pura e seus cenários permanecem disponíveis quando o quantitativo não é recebido.

**Início do próximo parágrafo:** “As políticas consideradas nas duas janelas estão descritas no Quadro 15.”

### 1.16 Combinação histórica — seção 5.16

**Localizar o início:** “A combinação entre previsão e quantitativo institucional também foi examinada”.

**Substituir o parágrafo inteiro por:**

A combinação entre previsão e reservas históricas também foi examinada, utilizando participações de 25%, 50%, 75% e 100% da previsão, com margens de zero ou dez refeições. A seleção histórica manteve participação de 100% do modelo. Nessa iteração, portanto, a combinação dos dois sinais não apresentou vantagem segundo o critério de seleção adotado.

**Início do próximo parágrafo:** “Em 2026, o quantitativo institucional passou a ter origem diferente”.

### 1.17 Alternativa combinada ausente do Quadro 15 — seção 4.8

O texto e a Figura 6 incluem a alternativa combinada, mas o Quadro 15 lista somente sem margem, moderada, conservadora e contextual.

**Localizar:** “Quadro 15 - Políticas de decisão consideradas no desenvolvimento do artefato”.

**Acrescentar esta linha:**

| Política | Lógica | Uso gerencial |
|---|---|---|
| Combinada para preparo | Soma 25% da previsão sem reservas a 75% do quantitativo recebido, acrescenta dez refeições e arredonda para cima. | Alternativa disponível apenas para preparo, quando o quantitativo é recebido. Já contém margem e não recebe novo acréscimo moderado ou conservador. |

Na linha “Contextual”, substitua o nome da política por **“Contextual — experimental”**, para deixar visível que ela não integra as saídas regulares já descritas. Mantenha a ressalva sobre necessidade de avaliação.

### 1.18 Repetição — seção 3.1.1

**Localizar o início:** “Os apontamentos recebidos no processo de submissão desse mesmo relato foram considerados feedback formativo”.

**Ação:** excluir esse parágrafo inteiro. Seu conteúdo já aparece no parágrafo imediatamente anterior, iniciado por “No relato apresentado ao SINGEP-CIK”.

**Início do próximo parágrafo:** “As produções acadêmicas e as mudanças incorporadas ao projeto estão relacionadas no Quadro 3”.

Essa exclusão também ajuda a atender ao comentário do orientador sobre fragmentação dos parágrafos.

## 2. Sugestões de clareza e coerência científica

### 2.1 Problema de pesquisa — seção 1.2

O problema atual menciona os quantitativos institucionais como comparador, mas os resultados existentes utilizam reservas históricas. Sugiro explicitar os dois momentos.

**Localizar o início:** “Em que medida a integração de consumo histórico, cardápio e calendário”.

**Substituir a pergunta inteira por:**

Em que medida um artefato que integra consumo histórico, cardápio e calendário, com reservas e clima avaliados como fontes adicionais, pode apoiar o planejamento de refeições, considerando o erro em relação às reservas históricas, o excesso e o déficit potenciais e a antecedência para compras e preparo, com posterior avaliação frente aos quantitativos institucionais?

**Início do próximo parágrafo:** “A questão considera a incerteza da demanda”.

### 2.2 Horizonte e unidade de previsão — seção 2.2.1

**Localizar o início:** “Rodrigues et al. (2024), ao estudarem modelos de aprendizado de máquina”.

**Substituir o parágrafo inteiro por:**

Rodrigues et al. (2024), ao estudarem modelos de aprendizado de máquina para previsão de demanda de curto prazo em serviços de alimentação, destacam que a escolha do modelo deve considerar o contexto da aplicação, o horizonte de previsão e a métrica de avaliação. Nesta pesquisa, cada previsão corresponde ao consumo de um almoço, com antecedência de três a sete dias nos testes históricos e de dez a quatorze dias na saída proposta para compras. Uma métrica adequada para comparar algoritmos pode não traduzir, sozinha, o risco de excesso ou insuficiência no planejamento.

**Início do próximo parágrafo:** “Métodos estatísticos e modelos de aprendizado de máquina devem”.

O texto atual chama o horizonte de “diário”. A granularidade do alvo é diária; a antecedência é de vários dias.

### 2.3 Abertura sobre métricas — seção 2.4.1

**Localizar o início:** “A escolha das métricas deve estar relacionada ao objetivo da previsão”.

**Substituir o parágrafo inteiro por:**

A escolha das métricas deve considerar o objetivo da previsão e a decisão apoiada pelo modelo. No planejamento de refeições, os erros podem representar riscos distintos de excesso e insuficiência. A avaliação combina medidas do erro preditivo e diferenças potenciais entre quantidade planejada e consumo observado. Efeitos sobre desperdício e atendimento exigem registros específicos do serviço.

**Início do próximo parágrafo:** “Entre as métricas estatísticas, o erro absoluto médio (MAE)”.

### 2.4 Previsão, plano e produção — seção 2.4.1

**Localizar o início:** “Além dos indicadores estatísticos, a avaliação do planejamento deve considerar”.

**Substituir o parágrafo inteiro por:**

Além dos indicadores estatísticos, a avaliação do planejamento considera a diferença entre a quantidade planejada e o consumo observado. Quando o plano supera o consumo, calcula-se excesso potencial; quando fica abaixo, calcula-se déficit potencial. Dois métodos com o mesmo MAE podem distribuir essas diferenças de formas distintas, com maior frequência ou magnitude de excesso em um caso e de déficit em outro. Esses indicadores não medem a quantidade efetivamente produzida nem seus efeitos sobre o serviço.

**Início do próximo parágrafo:** “Além da soma dos desvios, importa observar em quantos dias”.

### 2.5 Utilidade ainda pendente — seção 3.7

**Localizar o início:** “No capítulo de modelo sistêmico, são detalhados os componentes”.

**Substituir o parágrafo inteiro por:**

No capítulo de modelo sistêmico, são detalhados os componentes, os fluxos e a lógica de decisão do artefato. No capítulo de resultados, são apresentados e discutidos os achados da avaliação retrospectiva, com comparação entre alternativas e consumo observado. Esses resultados permitem examinar o desempenho das previsões e os cenários de planejamento; a utilidade das saídas para a gestão ainda depende de acompanhamento prospectivo.

**Próximo título:** “4 MODELO SISTÊMICO DO ARTEFATO”.

### 2.6 Síntese das evidências sobre R² — seção 5.7

O parágrafo atual é cauteloso e pode ser mantido. A versão abaixo explicita que o estudo social não valida um corte para refeições e evita atribuir ação explicativa ao próprio estudo.

**Localizar o início:** “A interpretação desses resultados considera a finalidade preditiva e o contexto de aplicação.”

**Substituir o parágrafo inteiro por, se desejar:**

A interpretação desses resultados considera a finalidade preditiva e o contexto de aplicação. Shmueli (2010) distingue o ajuste explicativo do desempenho em novas observações. Em um estudo com 160 equipes, Salganik et al. (2020) obtiveram R² fora da amostra em torno de 0,20 para alguns desfechos individuais, mesmo com uma base longitudinal extensa, e reconheceram limites na capacidade de previsão. Esse contexto difere da previsão do consumo diário agregado de refeições, e os valores não constituem critérios de aceitação para esta pesquisa. Abelson (1985) e Funder e Ozer (2019) discutem a relevância prática dos resultados em conjunto com proporções de variância e tamanhos de efeito, sem definir um limiar para a previsão de refeições.

**Início do próximo parágrafo:** “No contexto de alimentação coletiva, Posch et al. (2022)”.

**Cuidado preservado:** não classificar R² de 0,333 ou 0,454 como “bom” apenas por se tratar de comportamento humano. A defesa deve considerar o erro em refeições, os comparadores, a estabilidade temporal e os critérios de uso ainda a acordar. O R² de Salganik também usa uma referência no denominador diferente da adotada no diagnóstico desta pesquisa; a comparação é conceitual, não numérica direta.

### 2.7 Acrescentar R² ao Quadro 19 — seção 5.13, opcional

**Localizar:** “Quadro 19 - Síntese dos resultados e limites”.

O quadro pode sintetizar o indicador recém-incluído. Acrescente após “Comparação de métodos”:

| Aspecto avaliado | Evidência principal | Limite de interpretação |
|---|---|---|
| R² das previsões | CatBoost: 0,333 em 400 datas na linha-base. Regressão bayesiana: 0,454 em 415 datas na expandida. | Medida complementar às métricas de erro; as linhas utilizam datas diferentes e o R² não comprova utilidade operacional. |

Não é necessário repetir todos os valores no resumo e nas considerações parciais. A seção 5.7 e a Tabela 4 já atendem à inclusão do indicador.

### 2.8 Explicar “linha-base” e “linha expandida” uma vez

As configurações da ablação estão bem definidas, mas a denominação das duas linhas da competição aparece antes de uma explicação direta e pode ser confundida com a base da ablação.

**Localizar o início:** “A competição de modelos comparou 20 estimadores individuais, nove ensembles e quatro baselines”.

**Providência antes de reescrever:** confira quais atributos foram efetivamente utilizados na competição de cada linha. Os diretórios de resultados denominam a primeira linha “consumo_cardapio_calendario” e a segunda “reservas_consumo_cardapio_calendario_clima”, mas alguns planos citados na dissertação são identificados por condições particulares, como “Historico_Calendario”. O nome do diretório não comprova o conjunto de atributos de cada condição.

Após essa conferência, acrescente neste parágrafo uma frase que defina precisamente as duas linhas e diferencie a competição de métodos da ablação das quatro configurações. Mantenha os denominadores de 400, 415, 432 e 390. Não proponho aqui uma substituição fechada porque esta revisão não reconstruiu os atributos dos candidatos pelo código.

**Início do próximo parágrafo:** “As falhas e previsões fora do domínio plausível foram registradas”.

## 3. Ajustes nas figuras para a próxima geração

As correções abaixo dizem respeito ao conteúdo escrito nas imagens. Não foram feitas alterações nos arquivos das figuras.

### Figura 1 — aplicação da DSR

**Localizar o rodapé:** “A avaliação orienta a revisão do projeto; resultados no serviço permanecem pendentes.”

**Substituir por:**

O pesquisador revisa o projeto com base na avaliação; os efeitos no serviço permanecem pendentes.

Essa redação atende à preferência do orientador por evitar sujeitos abstratos realizando ações humanas.

### Figura 3 — pipeline de dados

**Localizar, na caixa “Resultados e decisão”:** “Erros pareados, margens, custos documentados e riscos potenciais.”

**Substituir por:**

Erros pareados, margens e diferenças potenciais entre plano e consumo.

Os pagamentos documentados são contextualização administrativa; o pipeline não apresenta avaliação de custos decorrentes das previsões.

### Figura 5 — arquitetura sistêmica

**Localizar, na caixa “Módulo de previsão”:** “Modelos sem reservas e com reservas; clima apenas com proveniência temporal.”

**Substituir por:**

Modelos para preparo e compras; reservas e clima restritos aos experimentos históricos.

O quantitativo atual participa da combinação no planejamento, não como entrada dos modelos preparados para acompanhamento. A mudança ajuda a alinhar a imagem com os parágrafos 4.7 e 4.8. Se a figura deve representar exclusivamente a arquitetura histórica, identifique isso na legenda em vez de alterar a caixa.

### Figura 7 — lógica de avaliação gerencial

**Na caixa “Definir a coorte comum”, localizar:** “Mesmas datas com consumo e quantidade institucional conhecida para cada método.”

**Substituir por:**

Mesmas datas com consumo e referência de planejamento disponíveis.

**Na caixa “Medir erro de previsão”, substituir a linha de métricas por:**

MAE, RMSE, WAPE, viés e R²; separar previsão de plano inteiro.

**Na caixa “Interpretar custos”, substituir título e texto por:**

Contextualizar pagamentos

Registros administrativos; não permitem atribuir economia ao artefato.

O texto atual menciona “simulações explícitas” de custos, que não integram os resultados descritos na versão atual.

### Figuras 16 e 17 — nomes dos modelos

Na Figura 16 ainda aparecem nomes internos, como “CatBoost_native” e “Ensemble_top5_validacao_media”. Na Figura 17 aparece “BayesianRidge”, enquanto a tabela usa “Regressão bayesiana”.

Na próxima geração, use os mesmos nomes das tabelas, preservando os números. Na Figura 16, identifique explicitamente os painéis como **“Linha-base — 400 datas”** e **“Linha expandida — 415 datas”**. O número de datas aparece no eixo, mas o nome da linha facilitará a leitura.

## 4. Referências, comentários e acabamento

### 4.1 Ordem das referências

As cinco novas referências foram incluídas. Há um ajuste de ordem: a entrada iniciada por **“FRIEDMAN, J. H.”** deve anteceder **“FUNDER, D. C.; OZER, D. J.”** na lista alfabética.

### 4.2 Dois trabalhos de Souza et al. em 2025

Existem duas entradas de 2025 com os mesmos três primeiros autores: o relato “Análise exploratória...” e o relato “Gestão de suprimentos...”. A abreviação “Souza et al. (2025)” pode dificultar a identificação.

Antes de alterar anos para 2025a/2025b, aplique a regra de desambiguação do manual institucional ao conjunto de autores efetivamente apresentado. Os dois trabalhos têm listas completas de autores diferentes. Uma solução textual simples é identificar o evento/título na primeira menção e manter as formas narrativas completas quando necessário. Não atribuí letras automaticamente nesta revisão.

### 4.3 Comentários ainda existentes

| Comentário | Local | Encaminhamento |
|---|---|---|
| Ficha catalográfica e marcador XXXXX | Ficha catalográfica | Substituir pela ficha oficial quando emitida pela biblioteca. Não inventar código de catalogação. |
| ODS 2 na introdução ou ODS 12 como foco | Seção 1.1 | O texto atual mantém ODS 12 como foco e ODS 2 como contexto em 2.5.2. Essa opção é coerente, mas confirme a preferência de abrangência com o orientador antes de resolver o comentário. |
| Demonstrar contribuição às metas dos ODS | Seção 1.1 | A seção 5.11 já explicita que o estudo não mediu contribuição efetiva à redução do desperdício nem às metas do ODS 2. Mantenha essa delimitação; não acrescente resultado não medido. |
| Unificar parágrafos curtos | Seção 3.1.1, relato SINGEP-CIK | A exclusão do parágrafo repetido indicada em 1.18 atende parte do apontamento. |
| Fonte e alinhamento | Legenda do Quadro 9 | Conferir no Word. A revisão textual não confirma aparência final. |
| Bordas do quadro | Quadro 9 | Conferir no Word e padronizar com os demais quadros. |
| Validar pesos e níveis de proteção | Seção 3.5 | Permanece como providência futura. O texto já trata 2:1 como hipótese e a combinação como candidato; não declarar validação gerencial concluída. |

### 4.4 Atualizações finais no Word

1. Após as alterações, atualize o sumário e as listas de tabelas, figuras e quadros. Não faça substituição global de números de tabelas: as seis chamadas erradas estão identificadas individualmente neste roteiro.
2. Confira as três ocorrências de **“116”** associadas à extensão do trabalho: ficha catalográfica, identificação no resumo e identificação no abstract. Atualize somente depois de fechar a paginação e conferir a convenção institucional de folhas/páginas.
3. Confira a formatação da Tabela 4, pois ela foi recém-inserida. A revisão confirmou o conteúdo, mas não a distribuição nas páginas.
4. Padronize “déficit potencial” ou “falta potencial” no texto e nas legendas. Ambos são definidos, mas “excesso e déficit potenciais” oferece maior consistência e menor chance de leitura como resultado efetivo. Não altere referências ou títulos publicados de terceiros.
5. Se desejar ampliar a lista de siglas para todos os termos recorrentes, confira KNN, SVR, MLP, BERT, Ridge, P90 e os nomes das bibliotecas. R² é um símbolo; sua inclusão pode ser feita em lista de símbolos, conforme o manual adotado. Não há necessidade de tratar cada nome de algoritmo como sigla.

## Ordem sugerida de execução

**Primeiro:** seção 3.2 e Tabela 1; cabeçalho da Tabela 4; seis chamadas das tabelas; distinção entre reservas e quantitativo institucional; linha combinada no Quadro 15; repetição em 3.1.1.

**Depois:** sugestões de clareza, atualização das imagens e revisão dos comentários.

**Por último:** sumário, listas, paginação, referências e inspeção visual no Word/PDF.

Não há necessidade de reescrever integralmente os capítulos 5 e 6. As limitações centrais estão registradas; os ajustes necessários concentram-se em contagem, nomenclatura, remissões, repetição e alinhamento das figuras com o escopo atual.
