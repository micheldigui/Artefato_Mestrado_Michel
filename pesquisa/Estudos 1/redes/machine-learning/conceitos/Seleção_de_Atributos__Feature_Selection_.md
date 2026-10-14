---
title: "Seleção de Atributos (Feature Selection)"
type: "conceito"
network: "machine-learning"
area: "Feature Engineering"
source_ids:
  - "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
  - "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
  - "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
    matches: 23
    sections:
      - "Features 3"
      - "Feature Scaling or Normalization 29"
      - "Interaction Features 35"
      - "Feature Selection 38"
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 8
    sections:
      - "Irrelevant Features 27"
      - "Hyperparameter Tuning and Model Selection 31"
  - id: "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
    matches: 19
    sections: []
  - id: "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
    matches: 9
    sections: []
  - id: "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
    matches: 3
    sections: []
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 34
    sections: []
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - feature-engineering
status: "canônico"
---

# 🧠 Seleção de Atributos (Feature Selection)

**Rede:** `machine-learning`

## 📚 Origem do conteúdo
As fontes abaixo são metadados de rastreabilidade. Elas não são nós da rede de conhecimento.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — Feature Engineering for Machine Learning Principles and Techniques for Data Scientists
- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — Hands-On Machine Learning with Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — Introduction into Machine Learning 4th Edition
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — Introduction to Machine Learning From Math to Code
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — Machine Learning An Algorithmic Perspective (2nd ed)
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — Machine Learning Foundations v1 Supervised

## 📝 Definição
Processo de escolher um subconjunto de atributos relevantes para reduzir ruído, custo e risco de sobreajuste.

## 💡 Intuição
Mais variáveis não significam necessariamente mais informação; atributos irrelevantes podem dificultar o aprendizado.

## ⚙️ Como funciona
Métodos filter usam estatísticas, wrapper avalia modelos e embedded seleciona durante o treinamento, como Lasso ou importância de árvores.

## 🧩 Problema que resolve
Alta dimensionalidade, necessidade de interpretabilidade e redução de custo de coleta ou inferência.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Alta dimensionalidade, necessidade de interpretabilidade e redução de custo de coleta ou inferência.

## ⚠️ Limitações e armadilhas
Selecionar olhando o teste, confundir correlação com utilidade fora da amostra e remover variáveis úteis em conjunto.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]]
- [[redes/machine-learning/conceitos/Regularização_L2__Ridge_|Regularização L2 (Ridge)]]
- [[redes/machine-learning/conceitos/Redução_de_Dimensionalidade|Redução de Dimensionalidade]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — 23 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Features 3; Feature Scaling or Normalization 29; Interaction Features 35; Feature Selection 38
- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 8 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Irrelevant Features 27; Hyperparameter Tuning and Model Selection 31
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — 19 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — 9 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — 3 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 34 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.

## 🧪 Exemplo mental
Selecionar variáveis de um modelo de churn dentro de cada fold para evitar que a validação influencie a escolha.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Seleção de Atributos (Feature Selection)** sem repetir a definição?
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
