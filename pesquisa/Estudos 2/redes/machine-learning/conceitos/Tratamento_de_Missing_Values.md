---
title: "Tratamento de Missing Values"
type: "conceito"
network: "machine-learning"
area: "Feature Engineering"
source_ids:
  - "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
  - "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
    matches: 7
    sections:
      - "Data 1"
      - "3. Text Data: Flattening, Filtering, and Chunking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41"
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 20
    sections:
      - "Insufficient Quantity of Training Data 23"
      - "Nonrepresentative Training Data 25"
      - "Poor-Quality Data 26"
      - "Overfitting the Training Data 27"
      - "Underfitting the Training Data 29"
      - "Data Mismatch 32"
      - "Working with Real Data 35"
  - id: "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
    matches: 11
    sections:
      - "1.4.2 Data Privacy and Security"
      - "1.4.4 Data Science"
  - id: "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
    matches: 5
    sections:
      - "1.1 IF DATA HAD MASS, THE EARTH WOULD BE A BLACK HOLE 1"
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 144
    sections:
      - "1.9 Common Datasets"
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - feature-engineering
status: "canônico"
---

# 🧠 Tratamento de Missing Values

**Rede:** `machine-learning`

## 📚 Origem do conteúdo
As fontes abaixo são metadados de rastreabilidade. Elas não são nós da rede de conhecimento.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — Feature Engineering for Machine Learning Principles and Techniques for Data Scientists
- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — Hands-On Machine Learning with Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — Introduction into Machine Learning 4th Edition
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — Machine Learning An Algorithmic Perspective (2nd ed)
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — Machine Learning Foundations v1 Supervised

## 📝 Definição
Conjunto de estratégias para entender, representar, imputar ou remover valores ausentes sem introduzir viés ou vazamento.

## 💡 Intuição
Ausência pode ser ruído, falha de medição ou informação sobre o processo; tratá-la exige entender a causa.

## ⚙️ Como funciona
Opções incluem remoção, imputação por estatística, modelos, indicadores de ausência e métodos específicos para séries temporais.

## 🧩 Problema que resolve
Quase todo pipeline real com dados incompletos, especialmente antes de algoritmos que não aceitam nulos.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Quase todo pipeline real com dados incompletos, especialmente antes de algoritmos que não aceitam nulos.

## ⚠️ Limitações e armadilhas
Imputar usando validação ou teste, apagar casos importantes, ignorar mecanismo de ausência e misturar categorias com números.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Overfitting_e_Underfitting|Overfitting e Underfitting]]
- [[redes/machine-learning/conceitos/Outliers|Outliers]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — 7 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Data 1; 3. Text Data: Flattening, Filtering, and Chunking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 20 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Insufficient Quantity of Training Data 23; Nonrepresentative Training Data 25; Poor-Quality Data 26; Overfitting the Training Data 27; Underfitting the Training Data 29; Data Mismatch 32; Working with Real Data 35
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — 11 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 1.4.2 Data Privacy and Security; 1.4.4 Data Science
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — 5 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 1.1 IF DATA HAD MASS, THE EARTH WOULD BE A BLACK HOLE 1
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 144 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 1.9 Common Datasets

## 🧪 Exemplo mental
Imputar mediana calculada no treino e criar um indicador para informar ao modelo que o valor original estava ausente.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Tratamento de Missing Values** sem repetir a definição?
2. Qual problema concreto este conceito resolve e qual é a variável de saída?
3. Quais hipóteses precisam ser verdadeiras para a aplicação ser confiável?
4. Que alternativa eu compararia e qual critério justificaria a escolha?
5. Como eu verificaria o comportamento em dados novos ou em um caso-limite?

## 📌 Notas pessoais
- [ ] Escrever uma explicação com minhas próprias palavras.
- [ ] Implementar ou revisar um exemplo pequeno.
- [ ] Registrar uma decisão, dúvida ou conexão nova.

---
*Nota canônica gerada pelo pipeline; preserve as seções pessoais ao regenerar.*


## Diagnóstico específico

- [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|Diagnóstico Exploratório de Séries Temporais]] trata lacunas temporais e interpolação no contexto da sequência.
