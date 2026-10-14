---
title: "IA centrada no modelo (Model-Centric AI)"
type: "conceito"
status: "rascunho"
tags:
  - machine-learning
  - engenharia-de-dados
source: "AI Engineering: Building Applications with Foundation Models, cap. 3 — Data Engineering"
created: "2026-09-23"
---

# IA centrada no modelo (Model-Centric AI)

## Resumo

Abordagem de desenvolvimento que busca melhorar o desempenho de um sistema de IA principalmente por mudanças no modelo: arquitetura, escala ou técnicas de treinamento. Ela contrasta com a abordagem centrada em dados, que mantém o modelo fixo e investe em curadoria e qualidade dos dados. Na prática, as duas frentes se complementam.

## Ideias principais

- **Centrada no modelo:** tenta elevar o desempenho projetando novas arquiteturas, aumentando modelos ou desenvolvendo métodos de treinamento.
- **Centrada em dados:** tenta elevar o desempenho aprimorando processamento, rotulagem, cobertura e qualidade dos conjuntos de dados, inclusive com menos recursos de treinamento.
- **Como comparar:** em uma avaliação centrada no modelo, o conjunto de dados costuma ser mantido constante enquanto se comparam modelos. Em uma avaliação centrada em dados, o modelo e o procedimento de avaliação são padronizados enquanto se comparam conjuntos de dados.
- Exemplos de trabalho centrado em dados incluem corrigir rótulos incorretos, acrescentar exemplos de casos-limite e ampliar os dados. O resultado deve ser medido em tarefas de avaliação relevantes, não apenas pela aparência do conjunto.
- A divisão é útil para orientar experimentos e pesquisa, mas progresso real frequentemente exige melhorias conjuntas no modelo e nos dados.

## Aplicação

Ao diagnosticar desempenho baixo, registre uma linha de base reproduzível e altere uma frente por vez: arquitetura/treinamento ou dados. Avalie as mudanças no mesmo conjunto de tarefas e verifique efeitos colaterais como viés, alucinações e robustez em casos-limite.

## Limitações

Nem todo problema do modelo pode ser resolvido com dados, e melhorar a arquitetura não corrige automaticamente dados enviesados ou mal rotulados. Comparações também dependem de avaliações representativas e de controles consistentes de treinamento.

## Conexões

- [[redes/ai-engineering/conceitos/qlora|QLoRA]]
- [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia-dpo|Otimização Direta de Preferência (DPO)]]

## Fonte

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*, seção “A Data-Centric View of AI”, cap. 3. Texto local: `fontes/referencias-ia-ml/txt/AI_Engineering_Building_Applications_-_Chip_Huyen.txt`.
- Síntese baseada na definição e nos exemplos da fonte; sem citações literais.