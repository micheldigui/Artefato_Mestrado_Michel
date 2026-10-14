---
title: "AI Engineering: Building Applications with Foundation Models — Capítulo 2"
type: "fonte"
network: "ai-engineering"
source_kind: "livro"
author: "Chip Huyen"
source_id: "huyen-ai-eng"
chapter: "Capítulo 2 — Entendendo Modelos de Fundação"
location: "localização não informada no material recebido"
evidence: "fonte_analisada"
confidence: "revisar"
tags:
  - fonte
  - rede/ai-engineering
  - tipo/livro
status: "indexado"
---

# Capítulo 2 — Entendendo Modelos de Fundação

## 1. Objetivo do capítulo
Analisar as decisões de design subjacentes à criação de modelos de fundação — cobrindo a curadoria de dados de treinamento, escolhas de arquitetura de rede neural, dimensionamento computacional, estratégias de pós-treinamento, amostragem e a natureza probabilística inerente à geração de texto.

## 2. Resumo do argumento central
O comportamento, as limitações e as capacidades de um modelo de fundação em aplicações downstream derivam diretamente de suas escolhas de construção. Como o treinamento do zero é custoso e restrito, o engenheiro de IA deve compreender o impacto de fatores como a qualidade dos dados, a arquitetura de atenção do Transformer, os limites de escala e os parâmetros de amostragem para controlar problemas como alucinações, inconsistências e restrições de formato de saída.

## 3. Conceitos identificados
- Dados de Treinamento
- Arquitetura de Modelo
- Arquitetura Transformer
- Mecanismo de Atenção
- Módulos Prefill e Decode
- Modelos de Espaço de Estado (SSMs)
- Parâmetros e Escala
- Mixture of Experts (MoE)
- Lei de Escala de Chinchilla (Chinchilla Scaling Law)
- Pós-Training (Pós-Treinamento)
- Ajuste Fino Supervisionado (SFT)
- Aprendizado por Reforço com Feedback Humano (RLHF)
- Otimização Direta de Preferência (DPO)
- Amostragem (Sampling)
- Logits e Logprobs
- Temperatura
- Top-k e Top-p (Nucleus Sampling)
- Test Time Compute
- Amostragem Restrita (Constrained Sampling)
- Alucinação

## 4. Sequência lógica do capítulo
1. Análise dos dados de treinamento: o domínio e o impacto da escassez em modelos multilíngues e específicos de domínio.
2. Análise da arquitetura dos modelos: do Transformer clássico (atenção, Q/K/V) a alternativas modernas como Mamba e Jamba.
3. Dimensionamento (Scale): o significado de parâmetros, tokens, FLOPs e a Lei de Escala de Chinchilla.
4. Pós-treinamento e alinhamento humano: transformando modelos de completação em assistentes via SFT, RLHF e DPO.
5. O processo de amostragem: como o modelo escolhe tokens utilizando logits, temperatura, Top-k e Top-p.
6. Garantias estruturais de saída e a natureza probabilística: como lidar com inconsistências e o fenômeno das alucinações.

## 5. Principais afirmações
- A qualidade e a distribuição dos dados de treinamento determinam diretamente as falhas e os vieses do modelo em idiomas minoritários ou domínios restritos.
- O dimensionamento ideal de um modelo de fundação obedece a leis matemáticas de escala que vinculam o número de parâmetros ao volume ideal de tokens de treinamento.
- A amostragem estocástica baseada em temperatura introduz criatividade, mas é a causa raiz da inconsistência e de alucinações em tarefas determinísticas.

## 6. Fórmulas ou procedimentos apresentados
- Cálculo da atenção baseada em matrizes de consulta, chave e valor ($Q, K, V$).
- Aplicação da função Softmax com fator de temperatura para remapeamento de logits.
- Regra de proporção de tokens de Chinchilla (tokens $\approx 20 \times$ parâmetros).

## 7. Exemplos relevantes
- Análise de representação de idiomas no dataset Common Crawl e o impacto em benchmarks de raciocínio (ex: MMLU em línguas de baixo recurso).
- Demonstração do impacto do ajuste de temperatura nas probabilidades de escolha de tokens de vocabulário.

## 8. Limitações e ressalvas
- A opacidade de dados de treino em modelos comerciais dificulta prever falhas de domínio específico sem testes empíricos rigorosos.
- O pós-treinamento de alinhamento reduz comportamentos tóxicos, mas não elimina a raiz estocástica das alucinações.

## 9. Dúvidas em aberto
Não informado ou não suficientemente esclarecido no trecho analisado.

## 10. Localização da fonte
localização não informada no material recebido
