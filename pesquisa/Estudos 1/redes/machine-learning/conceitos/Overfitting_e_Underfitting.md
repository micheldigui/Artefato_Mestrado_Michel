---
title: "Overfitting e Underfitting"
type: "conceito"
network: "machine-learning"
area: "Validação e Métricas"
source_ids:
  - "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
  - "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
  - "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
    matches: 4
    sections: []
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 103
    sections:
      - "Overfitting the Training Data 27"
      - "Underfitting the Training Data 29"
  - id: "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
    matches: 21
    sections: []
  - id: "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
    matches: 92
    sections: []
  - id: "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
    matches: 19
    sections:
      - "2.2.1 Overfitting 19"
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 230
    sections: []
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - valida--o-e-m-tricas
status: "canônico"
---

# 🧠 Overfitting e Underfitting

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
Overfitting ocorre quando o modelo aprende ruído do treino; underfitting ocorre quando não captura estrutura suficiente do problema.

## 💡 Intuição
Um modelo útil deve aprender padrões que se repetem em dados novos, não memorizar exemplos nem simplificar demais.

## ⚙️ Como funciona
Compare desempenho em treino, validação e teste. Regularização, early stopping, mais dados, atributos melhores e ajuste de complexidade ajudam no diagnóstico.

## 🧩 Problema que resolve
Todo ciclo de modelagem supervisionada, desde o baseline até a seleção final do modelo.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Todo ciclo de modelagem supervisionada, desde o baseline até a seleção final do modelo.

## ⚠️ Limitações e armadilhas
Usar o conjunto de teste para decidir hiperparâmetros, ignorar vazamento e interpretar uma única divisão como evidência definitiva.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Bias-Variance_Tradeoff|Bias-Variance Tradeoff]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Regularização_L2__Ridge_|Regularização L2 (Ridge)]]
- [[redes/machine-learning/conceitos/Gradient_Boosting|Gradient Boosting]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — 4 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 103 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Overfitting the Training Data 27; Underfitting the Training Data 29
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — 21 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — 92 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — 19 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 2.2.1 Overfitting 19
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 230 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.

## 🧪 Exemplo mental
Uma árvore com profundidade 30 tem quase 100% no treino, mas cai muito na validação: sinal de sobreajuste.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Overfitting e Underfitting** sem repetir a definição?
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
