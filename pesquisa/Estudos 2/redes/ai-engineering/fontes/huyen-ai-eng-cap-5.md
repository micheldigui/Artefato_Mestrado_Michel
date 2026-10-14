---
title: "AI Engineering: Building Applications with Foundation Models — Capítulo 5"
type: "fonte"
network: "ai-engineering"
source_kind: "livro"
author: "Chip Huyen"
source_id: "huyen-ai-eng"
chapter: "Capítulo 5 — Engenharia de Prompt"
location: "localização não informada no material recebido"
evidence: "fonte_analisada"
confidence: "revisar"
tags:
  - fonte
  - rede/ai-engineering
  - tipo/livro
status: "indexado"
---

# Capítulo 5 — Engenharia de Prompt

## 1. Objetivo do capítulo
Apresentar as diretrizes teóricas e práticas da engenharia de prompt como técnica primária de adaptação de modelos, cobrindo anatomia estrutural, aprendizado em contexto (*in-context learning*), melhores práticas de escrita, ferramentas de otimização, versionamento e a vertente de segurança voltada para a engenharia de prompt defensiva contra ataques de extração, *jailbreaking* e injeções de prompt.

## 2. Resumo do argumento central
A engenharia de prompt vai muito além de "tentar e errar palavras"; constitui uma interface de comunicação estruturada com modelos estocásticos. Embora o aprendizado em contexto permita que modelos pré-treinados executem tarefas para as quais não foram explicitamente ajustados, a vulnerabilidade inerente dos modelos a seguir instruções maliciosas exige que o desenvolvimento de prompts seja acompanhado de defesas sistêmicas rigorosas, como a hierarquia de instruções e o isolamento de ferramentas.

## 3. Conceitos identificados
- Engenharia de Prompt (*Prompt Engineering*)
- Anatomia do Prompt (Instrução, Exemplos, Contexto e Tarefa)
- Aprendizado em Contexto (*In-Context Learning*)
- Zero-Shot vs. Few-Shot
- Prompts de Sistema (*System Prompts*) vs. Prompts de Usuário (*User Prompts*)
- Comprimento de Contexto e Eficiência de Contexto
- Teste de Agulha no Palheiro (*Needle in a Haystack*)
- Melhores Práticas de Escrita de Prompts (Clareza, Personas, Decomposição)
- Cadeia de Pensamento (*Chain-of-Thought* / CoT)
- Ferramentas de Otimização Automatizada de Prompts (DSPy, Promptbreeder, TextGrad)
- Organização e Versionamento de Prompts (Catálogos e arquivos `.prompt`)
- Engenharia de Prompt Defensiva
- Engenharia de Prompt Inversa (*Reverse Prompt Engineering*)
- *Jailbreaking* e Injeção de Prompt (*Prompt Injection*)
- Injeção de Prompt Indireta (*Indirect Prompt Injection*)
- Extração de Dados de Treinamento (*Data Extraction*)
- Defesa por Hierarquia de Instruções (*Instruction Hierarchy*)

## 4. Sequência lógica do capítulo
1. Introdução à anatomia fundamental e ao aprendizado em contexto (zero-shot e few-shot).
2. Explicação da separação de canais entre prompts de sistema e de usuário, e o impacto da eficiência do contexto (*Needle in a Haystack*).
3. Melhores práticas metodológicas: escrita explícita, uso de personas, exemplos direcionados, decomposição de subtarefas e indução de raciocínio via *Chain-of-Thought*.
4. Avaliação de ferramentas voltadas para a automação e otimização de prompts.
5. Organização de código e versionamento de prompts em catálogos estruturados.
6. A vertente de segurança e engenharia defensiva: como mitigar ataques de extração de prompts, *jailbreaking*, injeções diretas e indiretas.

## 5. Principais afirmações
- A capacidade de aprendizado em contexto (*in-context learning*) permite que modelos utilizem dados e exemplos de teste sem alterar seus parâmetros estruturais internos.
- Modelos de linguagem possuem sensibilidade posicional, prestando muito mais atenção em instruções colocadas no início ou no fim do contexto do que no meio (*Lost-in-the-Middle*).
- A vulnerabilidade crítica dos modelos reside na incapacidade nativa de distinguir comandos privilegiados de sistema de instruções maliciosas inseridas por usuários ou dados externos recuperados (*Indirect Prompt Injection*).

## 6. Fórmulas ou procedimentos apresentados
- Estruturação em camadas de templates de chat (ex: Llama 2 e Llama 3 com delimitadores especiais como `[INST]`, `<<SYS>>`, `<|start_header_id|>`).
- Procedimento algorítmico da hierarquia de instruções para priorização de segurança.

## 7. Exemplos relevantes
- Casos de variação de desempenho baseados na posição do conteúdo no teste de Agulha no Palheiro.
- Demonstrações de prompts de *jailbreaking* clássicos (ex: modo DAN - *Do Anything Now*, ataques de avó / *grandma exploit*).

## 8. Limitações e ressalvas
- Prompts longos aumentam drasticamente os custos de tokens de entrada e a latência de processamento (*Prefill*).
- Nenhuma barreira baseada exclusivamente em texto consegue blindar um modelo a 100% contra engenharia reversa ou injeções sofisticadas de prompt sem defesas estruturais de sistema.

## 9. Dúvidas em aberto
Não informado ou não suficientemente esclarecido no trecho analisado.

## 10. Localização da fonte
localização não informada no material recebido
