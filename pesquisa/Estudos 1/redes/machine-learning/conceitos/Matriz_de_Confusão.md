---
title: "Matriz de Confusão"
type: "conceito"
network: "machine-learning"
area: "Validação e Métricas"
source_ids:
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
  - "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
  - "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 17
    sections: []
  - id: "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
    matches: 5
    sections: []
  - id: "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
    matches: 21
    sections: []
  - id: "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
    matches: 10
    sections:
      - "2.2.3 The Confusion Matrix 21"
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 30
    sections: []
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - valida--o-e-m-tricas
status: "canônico"
---

# 🧠 Matriz de Confusão

**Rede:** `machine-learning`

## 📚 Origem do conteúdo
As fontes abaixo são metadados de rastreabilidade. Elas não são nós da rede de conhecimento.

- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — Hands-On Machine Learning with Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — Introduction into Machine Learning 4th Edition
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — Introduction to Machine Learning From Math to Code
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — Machine Learning An Algorithmic Perspective (2nd ed)
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — Machine Learning Foundations v1 Supervised

## 📝 Definição
Tabela que cruza classes reais e previstas, contabilizando verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos.

## 💡 Intuição
Além de dizer quanto o modelo acertou, mostra qual tipo de erro ele comete e em que classe.

## ⚙️ Como funciona
A matriz é a base de métricas como accuracy, precision, recall, especificidade e F1; em multiclasse, pode ser analisada por classe.

## 🧩 Problema que resolve
Diagnóstico de classificadores e escolha de limiar conforme os custos dos erros.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Diagnóstico de classificadores e escolha de limiar conforme os custos dos erros.

## ⚠️ Limitações e armadilhas
Accuracy pode esconder classes raras, a ordem dos eixos pode confundir e comparações precisam usar a mesma convenção.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Precision_e_Recall|Precision e Recall]]
- [[redes/machine-learning/conceitos/F1-Score|F1-Score]]
- [[redes/machine-learning/conceitos/ROC-AUC|ROC-AUC]]
- [[redes/machine-learning/conceitos/Detecção_de_Anomalias|Detecção de Anomalias]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 17 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — 5 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — 21 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — 10 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 2.2.3 The Confusion Matrix 21
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 30 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.

## 🧪 Exemplo mental
Em detecção de fraude, acompanhar falsos negativos pode ser mais importante que maximizar accuracy.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Matriz de Confusão** sem repetir a definição?
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
