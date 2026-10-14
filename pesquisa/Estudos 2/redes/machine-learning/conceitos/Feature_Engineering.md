---
title: "Feature Engineering"
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
  - "ZHENG-CASARI-2018"
  - "OZDEMIR-2022"
  - "DUBOUE-2020"
  - "CAMPESATO-2024"
  - "SAFDAR-2023"
  - "BARDOL-2025"
  - "SOHAIL-2025"
  - "CUANTUM-2024"
source_evidence:
  - id: "Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng"
    matches: 64
    sections:
      - "Features 3"
      - "Feature Scaling or Normalization 29"
      - "Interaction Features 35"
      - "Feature Selection 38"
  - id: "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
    matches: 13
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
    matches: 60
    sections: []
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - feature-engineering
status: "canônico"
---

# 🧠 Feature Engineering

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
Processo de transformar dados brutos em atributos úteis, confiáveis e disponíveis para um modelo.

## 💡 Intuição
A qualidade da representação dos dados frequentemente limita mais o resultado que a escolha do algoritmo.

## ⚙️ Como funciona
Inclui entender o domínio, limpar dados, criar variáveis, codificar categorias, tratar ausências, selecionar atributos e encapsular tudo em um pipeline reproduzível.


## Tipos de operação

Uma forma prática de classificar o trabalho é distinguir melhoria de atributos existentes, construção de novos atributos, seleção de um subconjunto, extração de uma representação e aprendizado de atributos pelo próprio modelo. Essas operações podem coexistir, mas têm riscos e saídas diferentes.

- Transformações numéricas e interações: [[redes/machine-learning/conceitos/Construcao_de_Atributos_Numericos|construção e transformação de atributos numéricos]].
- Datas, histórico e agregações temporais: [[redes/machine-learning/conceitos/Engenharia_de_Atributos_Temporais|engenharia de atributos temporais]].
- Texto: [[redes/machine-learning/conceitos/Representacao_de_Texto_para_ML|representação de texto para ML]].
- Imagens: [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|extração de atributos de imagens]].
- Ampliação de variantes plausíveis para treino: [[redes/machine-learning/conceitos/Aumento_de_Dados|aumento de dados (Data Augmentation)]].
- Pipeline reproduzível: [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|pipeline sem vazamento]].

## Ciclo guiado pelo EDA

Use [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|EDA]] para identificar forma, escala, ausência, cardinalidade, dependência e estrutura dos dados. Formule uma hipótese de atributo, implemente-a no pipeline, compare com baseline em validação que respeite tempo/grupos e registre desempenho, estabilidade, interpretabilidade, equidade e custo. O EDA orienta o experimento; não prova que a transformação melhora o modelo.

## 🧩 Problema que resolve
Sempre que dados brutos não estiverem na forma adequada para a tarefa, o modelo ou o processo de produção.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Sempre que dados brutos não estiverem na forma adequada para a tarefa, o modelo ou o processo de produção.

## ⚠️ Limitações e armadilhas
Vazamento entre treino e teste, transformações não reproduzíveis, proxies problemáticos e criação de atributos sem hipótese verificável.

## 🔗 Relações
- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Construcao_de_Atributos_Numericos|Construção e Transformação de Atributos Numéricos]]
- [[redes/machine-learning/conceitos/Engenharia_de_Atributos_Temporais|Engenharia de Atributos Temporais]]
- [[redes/machine-learning/conceitos/Representacao_de_Texto_para_ML|Representação de Texto para ML]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de Atributos de Imagens]]
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipelines de Feature Engineering sem Vazamento]]
- [[redes/machine-learning/conceitos/Normalização_e_Padronização|Normalização e Padronização]]
- [[redes/machine-learning/conceitos/One-Hot_Encoding|One-Hot Encoding]]
- [[redes/machine-learning/conceitos/Tratamento_de_Missing_Values|Tratamento de Missing Values]]
- [[redes/machine-learning/conceitos/Outliers|Outliers]]
- [[redes/machine-learning/conceitos/Seleção_de_Atributos__Feature_Selection_|Seleção de Atributos]]
- [[redes/machine-learning/conceitos/Redução_de_Dimensionalidade|Redução de Dimensionalidade]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-Validation]]
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de Modelos Orientada pelo EDA]]
## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- `ML_Livros/Feature_Engineering_for_Machine_Learning_Principles_and_Techniques_for_Data_Scientists_-_Alice_Zheng.txt` — 64 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Features 3; Feature Scaling or Normalization 29; Interaction Features 35; Feature Selection 38
- `ML_Livros/Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron.txt` — 13 ocorrência(s) do termo/padrão
  - Seções indicadas no sumário: Irrelevant Features 27; Hyperparameter Tuning and Model Selection 31
- `ML_Livros/Introduction_into_Machine_Learning_4th_Edition_-_Ethem_Alpaydin.txt` — 19 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Introduction_to_Machine_Learning_From_Math_to_Code_-_Ruye_Wang.txt` — 9 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_An_Algorithmic_Perspective_(2nd_ed).txt` — 3 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.
- `ML_Livros/Machine_Learning_Foundations_v1_Supervised_-_Roi_Yehoshua.txt` — 60 ocorrência(s) do termo/padrão
  - A ocorrência foi localizada no texto, mas não houve correspondência segura no sumário extraído.

Fontes novas e capítulos usados nesta ampliação: `redes/machine-learning/fontes/Feature_Engineering_Livros_e_Laboratorio.md`.

## 🧪 Exemplo mental
Criar recência, frequência e valor de compra a partir do histórico transacional antes de treinar churn.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Feature Engineering** sem repetir a definição?
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


