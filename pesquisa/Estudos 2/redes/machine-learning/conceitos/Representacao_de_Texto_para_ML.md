---
title: "Representação de Texto para Machine Learning"
type: "conceito"
network: "machine-learning"
area: "Feature Engineering"
status: "rascunho"
source_ids:
  - "ZHENG-CASARI-2018"
  - "OZDEMIR-2022"
  - "DUBOUE-2020"
  - "BARDOL-2025"
tags:
  - conceito
  - feature-engineering
  - texto
---

# Representação de Texto para Machine Learning

## Definição

Transformação de documentos em atributos que um estimador pode processar, preservando aspectos do texto relevantes à tarefa e à unidade de previsão.

## Estratégias

- Limpeza e tokenização; normalização, stopwords, stemming ou lematização quando adequados à língua e à tarefa.
- Bolsa de palavras e n-gramas com contagens; TF-IDF para ponderar termos por documento e corpus.
- Filtragem por frequência e hashing para controlar vocabulário e cardinalidade.
- Embeddings treinados ou pré-treinados para representar contexto semântico; comparar custo, domínio e disponibilidade.
- Estatísticas de documento, comprimento, densidade e atributos estruturais quando sustentados pelo problema.

## Escolha e avaliação

Comece com uma representação esparsa simples como baseline. Faça divisão por documento, pessoa, grupo ou tempo conforme a origem; duplicatas quase idênticas podem atravessar folds. Ajuste vocabulário, filtros e IDF somente no treino do fold. Verifique idioma, negadores, dados sensíveis e drift do vocabulário.

## Conexões
- [[redes/machine-learning/conceitos/Aumento_de_Dados_Textuais_EDA|Aumento de dados textuais (EDA)]]
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]

- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Texto|Análise Exploratória de Texto]]
- [[redes/machine-learning/conceitos/Naive_Bayes|Naive Bayes]]
- [[redes/machine-learning/conceitos/Regressão_Logística|Regressão Logística]]
- [[redes/machine-learning/conceitos/SVM__Support_Vector_Machines_|SVM]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipelines de Feature Engineering sem Vazamento]]

## Evidências nas fontes

Zheng e Casari (2018), caps. 3–4; Ozdemir (2022), cap. 5; Duboue (2020), cap. 8; Bardol (2025), cap. 11 para texto financeiro e embeddings.


