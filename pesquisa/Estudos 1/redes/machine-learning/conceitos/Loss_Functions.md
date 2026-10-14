---
title: "Loss Functions"
type: "conceito"
network: "machine-learning"
area: "Otimização e Treinamento"
source_ids:
  - "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
  - "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
  - "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
    matches: 5
    sections: []
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 63
    sections: []
  - id: "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
    matches: 17
    sections: []
  - id: "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
    matches: 8
    sections: []
  - id: "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
    matches: 5
    sections: []
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 234
    sections:
      - "2.2.3 Loss Functions"
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - otimiza--o-e-treinamento
status: "canônico"
---

# 🧠 Loss Functions

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
Funções que quantificam o custo de previsões incorretas e orientam o treinamento do modelo.

## 💡 Intuição
O que o modelo aprende depende do que a função de perda considera caro ou aceitável.

## ⚙️ Como funciona
MSE e MAE são comuns em regressão; log loss em classificação probabilística; perdas robustas podem reduzir efeito de outliers.

## 🧩 Problema que resolve
Definir o objetivo de otimização e alinhar treinamento com o tipo de erro relevante no domínio.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Definir o objetivo de otimização e alinhar treinamento com o tipo de erro relevante no domínio.

## ⚠️ Limitações e armadilhas
Otimizar uma perda que não representa a métrica de negócio, ignorar escala e usar função incompatível com a saída do modelo.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Gradient_Descent|Gradient Descent]]
- [[redes/machine-learning/conceitos/RMSE_e_MAE|RMSE e MAE]]
- [[redes/machine-learning/conceitos/Regressão_Logística|Regressão Logística]]
- [[redes/machine-learning/conceitos/Overfitting_e_Underfitting|Overfitting e Underfitting]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — 5 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 63 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — 17 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — 8 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — 5 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 234 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 2.2.3 Loss Functions

## 🧪 Exemplo mental
Treinar uma classificação com log loss e escolher o limiar de decisão separadamente conforme precision e recall.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Loss Functions** sem repetir a definição?
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
