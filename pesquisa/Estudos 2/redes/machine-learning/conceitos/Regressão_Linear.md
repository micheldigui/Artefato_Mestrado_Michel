---
title: "Regressão Linear"
type: "conceito"
network: "machine-learning"
area: "Supervised Learning"
source_ids:
  - "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
  - "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
  - "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
    matches: 19
    sections: []
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 65
    sections: []
  - id: "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
    matches: 33
    sections:
      - "1.2.3 Regression"
  - id: "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
    matches: 98
    sections:
      - "1.1 Linear EquationSystems 6"
  - id: "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
    matches: 7
    sections:
      - "1.4.1 Regression 6"
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 246
    sections:
      - "2.1.1 Regression versus Classification"
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - supervised-learning
status: "canônico"
---

# 🧠 Regressão Linear

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
Modelo supervisionado que estima uma variável contínua como combinação linear das variáveis de entrada.

## 💡 Intuição
O modelo procura um plano que minimize, em média, a distância entre os valores observados e as previsões.

## ⚙️ Como funciona
Na forma simples, y_hat = b0 + b1x. Os coeficientes são normalmente ajustados minimizando o erro quadrático médio ou a soma dos quadrados dos resíduos.

## 🧩 Problema que resolve
Previsão de valores numéricos, modelagem de relações aproximadamente lineares e construção de um baseline interpretável.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Previsão de valores numéricos, modelagem de relações aproximadamente lineares e construção de um baseline interpretável.

## ⚠️ Limitações e armadilhas
Relação não linear não modelada, multicolinearidade, outliers influentes, heterocedasticidade e confusão entre correlação e causalidade.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Gradient_Descent|Gradient Descent]]
- [[redes/machine-learning/conceitos/Regularização_L2__Ridge_|Regularização L2 (Ridge)]]
- [[redes/machine-learning/conceitos/Overfitting_e_Underfitting|Overfitting e Underfitting]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — 19 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 65 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — 33 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 1.2.3 Regression
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — 98 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 1.1 Linear EquationSystems 6
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — 7 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 1.4.1 Regression 6
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 246 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 2.1.1 Regression versus Classification

## 🧪 Exemplo mental
Estimar o tempo de entrega a partir de distância, volume de pedidos e condições de tráfego.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Regressão Linear** sem repetir a definição?
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
