---
title: "Análise Exploratória de Dados"
type: "conceito"
network: "machine-learning"
area: "Preparação e diagnóstico de dados"
status: "rascunho"
tags:
  - conceito
  - machine-learning
  - eda
source: "Mastering Exploratory Analysis with pandas; laboratório EDA SQL Server"
---

# Análise Exploratória de Dados

## Definição

Análise Exploratória de Dados (EDA) é o processo iterativo de examinar estrutura, qualidade, distribuições e relações de um conjunto de dados antes de fixar uma estratégia analítica ou de modelagem. Combina estatísticas descritivas, tabelas, visualizações e verificações de integridade para entender o que os dados representam e quais hipóteses merecem ser testadas.

EDA não é um algoritmo de Machine Learning, uma prova causal nem uma etapa de limpeza automática. Ela documenta evidências e incertezas para orientar o próximo experimento.

## Problema que resolve

Sem EDA, é fácil modelar o grão errado, confundir nulo com zero, deixar uma chave duplicar linhas, usar informação futura, avaliar com uma partição inadequada ou otimizar uma métrica que não corresponde ao problema. EDA torna essas condições observáveis antes da comparação de modelos.

## Como funciona

1. Defina a pergunta, população, período, unidade de análise, alvo e momento em que a previsão seria feita.
2. Verifique volume, tipos, chaves, duplicatas, cardinalidade, datas, validade e reconciliação de junções.
3. Examine distribuições numéricas, frequências categóricas, nulos, extremos e variações no tempo ou entre grupos.
4. Compare variáveis com o alvo e entre si usando gráficos e estatísticas compatíveis com seus tipos.
5. Converta achados em hipóteses explícitas e experimente modelos candidatos em validação que respeite dependências.
6. Registre fonte, filtros, grão, transformações, métrica, limitações e decisões.

## Entradas e saídas

- **Entradas:** dados em um grão declarado, dicionário de campos quando houver, pergunta de negócio/científica e contexto de coleta.
- **Saídas:** perfil de qualidade, descrição das distribuições e relações, hipóteses, riscos de vazamento/dependência, plano de preprocessing e shortlist de modelos a comparar.

## Hipóteses, limitações e armadilhas

- O conjunto recebido representa a população e o período que se deseja estudar? A EDA não corrige uma amostra enviesada por si só.
- Ausência pode depender de fatores não observados; MCAR/MAR/MNAR são hipóteses sobre o mecanismo, não rótulos inferidos automaticamente por uma tabela de nulos.
- Médias e correlações resumem aspectos limitados; examine mediana, quantis, formas, grupos e contexto.
- Extremos podem ser erros ou eventos válidos. Removê-los sem verificar altera a população analisada.
- Gráficos e associações não demonstram causalidade.
- A inspeção repetida do conjunto de teste influencia decisões e o transforma, na prática, em dado de desenvolvimento.

## Conexões

- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]
- [[redes/machine-learning/conceitos/Tratamento_de_Missing_Values|Tratamento de Missing Values]]
- [[redes/machine-learning/conceitos/Outliers|Outliers]]
- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Construcao_de_Atributos_Numericos|Construção e Transformação de Atributos Numéricos]]
- [[redes/machine-learning/conceitos/Engenharia_de_Atributos_Temporais|Engenharia de Atributos Temporais]]
- [[redes/machine-learning/conceitos/Representacao_de_Texto_para_ML|Representação de Texto para ML]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de Atributos de Imagens]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipelines de Feature Engineering sem Vazamento]]
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados (Data Augmentation)]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Amostragem_e_Representatividade|Amostragem e Representatividade]]
- [[redes/machine-learning/conceitos/Estatisticas_Resistentes_e_Formas_de_Distribuicao|Estatísticas Resistentes e Formas de Distribuição]]
- [[redes/machine-learning/conceitos/Reexpressao_de_Variaveis|Reexpressão de Variáveis]]
- [[redes/machine-learning/conceitos/Visualizacao_Exploratoria_e_Codificacao_Visual|Visualização Exploratória e Codificação Visual]]
- [[redes/machine-learning/conceitos/Analise_Bivariada_e_Tabelas_de_Contingencia|Análise Bivariada e Tabelas de Contingência]]
- [[redes/machine-learning/conceitos/Analise_Multivariada_Exploratoria|Análise Multivariada Exploratória]]
- [[redes/machine-learning/conceitos/Suavizacao_e_Comparacao_de_Sequencias|Suavização e Comparação de Sequências]]
- [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|Diagnóstico Exploratório de Séries Temporais]]
- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Texto|Análise Exploratória de Texto]]
- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Redes|Análise Exploratória de Redes]]
- [[redes/machine-learning/conceitos/Analise_Exploratoria_Geoespacial|Análise Exploratória Geoespacial]]
- [[redes/machine-learning/conceitos/Metodos_de_Deteccao_de_Outliers|Métodos de Detecção de Outliers]]
- [[redes/machine-learning/conceitos/Perfilamento_e_EDA_Automatizada|Perfilamento e EDA Automatizada]]

## Exemplo mental

Antes de prever atraso de entrega por pedido, confirme se uma linha representa um item ou um pedido, se o alvo está disponível somente depois da entrega, quantos pedidos estão atrasados, como o atraso varia no calendário e se o mesmo cliente aparece em treino e avaliação.

## Perguntas de revisão

1. O que uma linha representa e qual população ela cobre?
2. Como nulos, duplicatas ou junções podem alterar as observações?
3. Quais achados são evidências e quais ainda são hipóteses?
4. Que validação reproduz a forma como o modelo será usado?

## Evidência nas fontes

- Garg (2018), capítulos 1–4: leitura de diferentes formatos, seleção, transformação/reshape e visualização.
- Laboratório do projeto: perfil, estatísticas descritivas, completude, frequências, quantis/decis, IQR/outliers, correlação, séries temporais, grupos e qualidade.
- Veja o registro detalhado em `redes/machine-learning/fontes/EDA_Aulas_Livro_e_Laboratorio.md`.

