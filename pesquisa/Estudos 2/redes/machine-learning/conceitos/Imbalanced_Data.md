---
title: "Imbalanced Data"
type: "conceito"
network: "machine-learning"
area: "Feature Engineering"
source_ids:
  - "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
  - "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
source_evidence:
  - id: "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
    matches: 3
    sections:
      - "Data 1"
      - "3. Text Data: Flattening, Filtering, and Chunking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41"
  - id: "Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua"
    matches: 95
    sections:
      - "1.9 Common Datasets"
      - "2.1.1 Regression versus Classification"
      - "2.1.2 Deterministic versus Probabilistic Classification"
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - feature-engineering
status: "canônico"
---

# 🧠 Imbalanced Data

**Rede:** `machine-learning`

## 📚 Origem do conteúdo
As fontes abaixo são metadados de rastreabilidade. Elas não são nós da rede de conhecimento.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — Feature Engineering for Machine Learning Principles and Techniques for Data Scientists
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — Machine Learning Foundations v1 Supervised

## 📝 Definição
Situação em que uma ou mais classes têm muito mais exemplos que as demais.

## 💡 Intuição
A classe rara pode ser a mais importante, mas um modelo que sempre prevê a classe majoritária parece bom em accuracy.

## ⚙️ Como funciona
Use pesos de classe, amostragem, limiar, métricas por classe e validação adequada; oversampling e [[redes/machine-learning/conceitos/SMOTE|SMOTE]] devem ocorrer apenas dentro do treino. SMOTE interpola vizinhos e pode gerar pontos sem significado para variáveis categóricas, temporais ou domínios com restrições.

## 🧩 Problema que resolve
Fraude, defeitos, eventos médicos e qualquer detecção de eventos raros.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Fraude, defeitos, eventos médicos e qualquer detecção de eventos raros.

## ⚠️ Limitações e armadilhas
Duplicar exemplos antes da validação, avaliar só accuracy e tratar distribuição como detalhe quando ela representa o processo.

## 🔗 Relações
- [[redes/machine-learning/conceitos/ADASYN|ADASYN]]
- [[redes/machine-learning/conceitos/Precision_e_Recall|Precision e Recall]]
- [[redes/machine-learning/conceitos/Matriz_de_Confusão|Matriz de Confusão]]
- [[redes/machine-learning/conceitos/F1-Score|F1-Score]]
- [[redes/machine-learning/conceitos/Detecção_de_Anomalias|Detecção de Anomalias]]
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados (Data Augmentation)]]
- [[redes/machine-learning/conceitos/Oversampling_e_Bootstrap|Oversampling e bootstrap]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — 3 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Data 1; 3. Text Data: Flattening, Filtering, and Chunking. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 95 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: 1.9 Common Datasets; 2.1.1 Regression versus Classification; 2.1.2 Deterministic versus Probabilistic Classification

## 🧪 Exemplo mental
Treinar detecção de fraude priorizando recall da classe rara e monitorar quantos alertas falsos a equipe consegue investigar.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Imbalanced Data** sem repetir a definição?
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




