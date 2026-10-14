---
title: "Stochastic Gradient Descent (SGD)"
type: "conceito"
network: "machine-learning"
area: "Otimização e Treinamento"
source_ids:
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
  - "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
  - "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 138
    sections:
      - "Batch and Online Learning 14"
  - id: "Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin"
    matches: 22
    sections: []
  - id: "Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang"
    matches: 12
    sections:
      - "2.3 Gradient Descent Method 47"
      - "2.4 Line minimization 50"
      - "2.6 Conjugate gradientmethod 64"
      - "2.7 Issues of Local/GlobalMinimum 77"
  - id: "Machine_Learning_An_Algorithmic_Perspective__2nd_ed_"
    matches: 11
    sections: []
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 77
    sections:
      - "2.1.2 Deterministic versus Probabilistic Classification"
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - otimiza--o-e-treinamento
status: "canônico"
---

# 🧠 Stochastic Gradient Descent (SGD)

**Rede:** `machine-learning`

## 📚 Origem do conteúdo
As fontes abaixo são metadados de rastreabilidade. Elas não são nós da rede de conhecimento.

- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — Hands-On Machine Learning with Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — Introduction into Machine Learning 4th Edition
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — Introduction to Machine Learning From Math to Code
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — Machine Learning An Algorithmic Perspective (2nd ed)
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — Machine Learning Foundations v1 Supervised

## 📝 Definição
Variante do gradiente descendente que atualiza os parâmetros usando um exemplo ou mini-lote por vez.

## 💡 Intuição
Atualizações ruidosas são mais baratas e podem explorar a paisagem da perda, mas tornam a trajetória instável.

## ⚙️ Como funciona
A cada passo calcula um gradiente aproximado; embaralhamento, tamanho de lote, taxa de aprendizado e momentum afetam a convergência.

## 🧩 Problema que resolve
Grandes conjuntos de dados, aprendizado online e modelos em que o custo de um gradiente completo é alto.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Grandes conjuntos de dados, aprendizado online e modelos em que o custo de um gradiente completo é alto.

## ⚠️ Limitações e armadilhas
Oscilação, sensibilidade à escala e necessidade de agendamento da taxa de aprendizado.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Gradient_Descent|Gradient Descent]]
- [[redes/machine-learning/conceitos/Normalização_e_Padronização|Normalização e Padronização]]
- [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais|Deep Learning & Redes Neurais]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 138 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Batch and Online Learning 14
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — 22 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — 12 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 2.3 Gradient Descent Method 47; 2.4 Line minimization 50; 2.6 Conjugate gradientmethod 64; 2.7 Issues of Local/GlobalMinimum 77
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — 11 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 77 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 2.1.2 Deterministic versus Probabilistic Classification

## 🧪 Exemplo mental
Atualizar um classificador conforme novos lotes chegam, sem recalcular o gradiente sobre todo o histórico.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Stochastic Gradient Descent (SGD)** sem repetir a definição?
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
