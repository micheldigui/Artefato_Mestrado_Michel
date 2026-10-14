---
title: "F1-Score"
type: "conceito"
network: "machine-learning"
area: "Validação e Métricas"
source_ids:
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 2
    sections: []
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 53
    sections: []
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - valida--o-e-m-tricas
status: "canônico"
---

# 🧠 F1-Score

**Rede:** `machine-learning`

## 📚 Origem do conteúdo
As fontes abaixo são metadados de rastreabilidade. Elas não são nós da rede de conhecimento.

- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — Hands-On Machine Learning with Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — Machine Learning Foundations v1 Supervised

## 📝 Definição
Média harmônica entre precision e recall, usada quando se deseja equilibrar os dois tipos de desempenho.

## 💡 Intuição
Um modelo só obtém F1 alto se não abandonar precision nem recall.

## ⚙️ Como funciona
F1 = 2·precision·recall/(precision+recall). F-beta permite dar mais peso a recall ou precision.

## 🧩 Problema que resolve
Classificação desbalanceada com importância semelhante para falsos positivos e falsos negativos.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Classificação desbalanceada com importância semelhante para falsos positivos e falsos negativos.

## ⚠️ Limitações e armadilhas
Esconde a troca entre precision e recall, depende do limiar e pode ser inadequado quando os custos de erro são assimétricos.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Precision_e_Recall|Precision e Recall]]
- [[redes/machine-learning/conceitos/Matriz_de_Confusão|Matriz de Confusão]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/ROC-AUC|ROC-AUC]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 2 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 53 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.

## 🧪 Exemplo mental
Selecionar um limiar de classificação maximizando F1 somente quando os dois tipos de erro têm peso parecido.

## 🧠 Perguntas de revisão
1. Como eu explicaria **F1-Score** sem repetir a definição?
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

