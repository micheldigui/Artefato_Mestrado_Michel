---
title: "DBSCAN"
type: "conceito"
network: "machine-learning"
area: "Unsupervised Learning"
source_ids:
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
source_evidence:
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 31
    sections: []
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - unsupervised-learning
status: "canônico"
---

# 🧠 DBSCAN

**Rede:** `machine-learning`

## 📚 Origem do conteúdo
As fontes abaixo são metadados de rastreabilidade. Elas não são nós da rede de conhecimento.

- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — Hands-On Machine Learning with Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron

## 📝 Definição
Algoritmo de agrupamento baseado em densidade que identifica regiões densas e marca pontos isolados como ruído.

## 💡 Intuição
Um grupo é uma região em que muitos pontos estão próximos; pontos sem vizinhança suficiente não precisam pertencer a nenhum grupo.

## ⚙️ Como funciona
Com epsilon e min_samples, distingue pontos núcleo, alcançáveis e ruído, expandindo clusters a partir dos pontos núcleo.

## 🧩 Problema que resolve
Grupos de formas arbitrárias, detecção de ruído e cenários em que não se quer informar o número de clusters.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Grupos de formas arbitrárias, detecção de ruído e cenários em que não se quer informar o número de clusters.

## ⚠️ Limitações e armadilhas
Escolha de epsilon, escalas diferentes e densidades variadas podem produzir resultados ruins; alta dimensionalidade prejudica a distância.

## 🔗 Relações
- [[redes/machine-learning/conceitos/K-Means_Clustering|K-Means Clustering]]
- [[redes/machine-learning/conceitos/Outliers|Outliers]]
- [[redes/machine-learning/conceitos/Detecção_de_Anomalias|Detecção de Anomalias]]
- [[redes/machine-learning/conceitos/Normalização_e_Padronização|Normalização e Padronização]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 31 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.

## 🧪 Exemplo mental
Encontrar regiões de concentração de GPS e separar trajetórias esparsas como ruído.

## 🧠 Perguntas de revisão
1. Como eu explicaria **DBSCAN** sem repetir a definição?
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
