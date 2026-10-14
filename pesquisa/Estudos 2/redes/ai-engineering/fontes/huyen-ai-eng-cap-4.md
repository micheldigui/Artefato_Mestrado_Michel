---
title: "AI Engineering: Building Applications with Foundation Models — Capítulo 4"
type: "fonte"
network: "ai-engineering"
source_kind: "livro"
author: "Chip Huyen"
source_id: "huyen-ai-eng"
chapter: "Capítulo 4 — Avaliando Sistemas de IA"
location: "localização não informada no material recebido"
evidence: "fonte_analisada"
confidence: "revisar"
tags:
  - fonte
  - rede/ai-engineering
  - tipo/livro
status: "indexado"
---

# Capítulo 4 — Avaliando Sistemas de IA

## 1. Objetivo do capítulo
Apresentar a metodologia prática para projetar e implementar um pipeline de avaliação de sistemas de IA, abordando a definição de critérios sistêmicos, o fluxo de seleção de modelos, a escolha entre construir (*build*) ou comprar (*buy*), o problema da contaminação em benchmarks públicos e o passo a passo para criar diretrizes e conjuntos de dados de teste robustos.

## 2. Resumo do argumento central
Desenvolver aplicações de IA sem um pipeline de avaliação sistemática — adotando a prática de Desenvolvimento Orientado por Avaliação (*Evaluation-Driven Development*) — expõe o projeto a falhas catastróficas e custos invisíveis. A seleção de modelos e o design de testes devem equilibrar critérios de domínio, geração, seguimento de instruções, custos e latência, superando os vieses e as contaminações dos benchmarks públicos através de datasets privados e estruturados.

## 3. Conceitos identificados
- Desenvolvimento Orientado por Avaliação (*Evaluation-Driven Development*)
- Pilares de Critérios de Avaliação (Domínio, Geração, Instrução, Custo e Latência)
- Consistência Factual Local vs. Global
- Avaliação de Capacidade de *Roleplaying*
- Fluxo de Seleção de Modelos
- Decisão de Construir vs. Comprar (*Build vs. Buy*)
- Contaminação de Dados em Benchmarks Públicos (*Data Contamination*)
- Métodos de Detecção de Contaminação (Sobreposição de N-grams e Perplexidade)
- Pipeline de Avaliação Sistêmica (Abordagem de Três Passos)
- Slicing de Dados e o Paradoxo de Simpson
- Amostragem Estatística e Estimativa de Tamanho de Amostra

## 4. Sequência lógica do capítulo
1. Justificativa da avaliação prévia: por que a ausência de métricas torna a implantação em produção mais arriscada do que nunca.
2. Definição dos critérios de avaliação sistêmica: domínio, geração (focalizando alucinações locais e globais, e segurança/toxicidade) e seguimento de instruções (*IFEval* e *INFOBench*).
3. O fluxo de seleção de modelos: filtragem de atributos rígidos (*hard*) e flexíveis (*soft*), e a decisão comercial de construir (*self-host*) versus comprar (*model APIs*).
4. O problema dos benchmarks públicos e da contaminação de dados por memorização prévia de treino.
5. O guia prático de três passos para projetar o pipeline de avaliação interna da aplicação.
6. Considerações avançadas sobre amostragem, recortes de dados (*slicing*) e controle de vieses estatísticos como o Paradoxo de Simpson.

## 5. Principais afirmações
- O sucesso na engenharia de IA depende criticamente da definição de critérios de avaliação antes da escrita do código de produto (*Evaluation-Driven Development*).
- Os benchmarks públicos tradicionais sofrem de contaminação generalizada de dados de treinamento, o que distorce a capacidade preditiva real de um modelo para tarefas corporativas específicas.
- A decomposição de testes em fatias de dados (*slicing*) evita distorções estatísticas perigosas decorrentes do Paradoxo de Simpson.

## 6. Fórmulas ou procedimentos apresentados
- Regra prática de proporção de tamanho de amostra estatística (regra da raiz quadrada / proporção de 10x para reduções de 3x na diferença de acurácia).
- Procedimento algorítmico de 3 passos para criação de um pipeline customizado de avaliação.

## 7. Exemplos relevantes
- Estudo de caso sobre a variação de pontuação do MMLU no Gemini e GPT-4 decorrente unicamente da variação na técnica de *prompt engineering* utilizada nos testes.
- Exemplos de instruções estruturadas e automaticamente verificáveis do *IFEval* (ex: contagem de palavras, restrição de listas em JSON).

## 8. Limitações e ressalvas
- A avaliação de sistemas complexos de IA é inerentemente incompleta se baseada em um único escore unidimensional; exige-se uma matriz multifacetada de critérios.
- O custo computacional de rodar benchmarks amplos e pipelines de avaliação interna pode ser proibitivo se não planejado com amostragem eficiente.

## 9. Dúvidas em aberto
Não informado ou não suficientemente esclarecido no trecho analisado.

## 10. Localização da fonte
localização não informada no material recebido
