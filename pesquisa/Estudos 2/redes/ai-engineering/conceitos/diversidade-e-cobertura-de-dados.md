# 🧠 Diversidade e Cobertura de Dados

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 369–372

## 📝 Definição

### Definição formal

A **Diversidade e Cobertura de Dados** (*Data Coverage and Diversity*) é a propriedade estatística e representacional de um conjunto de treinamento que quantifica a dispersão e o equilíbrio heterogêneo de seus exemplos ao longo de múltiplos eixos ortogonais: domínios do conhecimento humano, tipologias de tarefas cognitivas (resumo, tradução, extração), distribuições de extensão de contexto, dialetos e formatos sintáticos de saída, garantindo que a parametrização do [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] não colapse em modos estreitos e preserve sua capacidade de generalização e raciocínio formal.

### Em linguagem simples

É a garantia de que a IA veja exemplos variados de verdade. Se você alimentar o modelo apenas com e-mails curtos e formais, ele se tornará incapaz de entender gírias, documentos longos ou código. Uma boa cobertura garante que o dataset misture assuntos técnicos, conversas casuais, textos em múltiplos idiomas e problemas de matemática para que a inteligência da IA seja ampla e resiliente.

### Escopo e distinções

A mistura ideal de dados varia conforme a fase do modelo. No pré-treinamento, o objetivo é absorver a estrutura estatística do mundo; no pós-treinamento supervisionado (SFT), o objetivo é cobrir a diversidade de pedidos dos usuários; e no alinhamento de preferência (RLHF/DPO), a diversidade equilibra as preferências subjetivas humanas.

## 🧩 Problema que resolve

Resolve a miopia operacional e o sobreajuste restrito (*narrow overfitting*). Modelos treinados com dados homogêneos perdem plasticidade, falham quando o usuário formula uma pergunta fora do padrão rígido de treino e podem sofrer quedas drásticas de raciocínio. A diversidade de tarefas e domínios força a rede neural a desenvolver representações latentes profundas e generalizáveis.

## 💡 Intuição

Pense na formação de um médico clínico geral:

- Se durante toda a faculdade e residência o médico atender apenas pacientes idosos com dor no joelho (**baixa cobertura e homogeneidade**), ele será incapaz de diagnosticar uma doença tropical em uma criança ou interpretar um eletrocardiograma de emergência.
- O currículo de medicina exige que o estudante passe por pediatria, cirurgia geral, psiquiatria, ginecologia e pronto-socorro (**alta diversidade e cobertura balanceada**), formando um profissional apto a lidar com a imprevisibilidade de qualquer paciente que entrar no consultório.

## ⚙️ Como funciona

A orquestração da diversidade opera através de matrizes de balanceamento de dados:

### Etapas

1. **Mapeamento de Eixos de Heterogeneidade:** Define-se os domínios necessários:
   - Domínio de Conhecimento: Ciências, Humanidades, Finanças, Notícias;
   - Domínio Estruturado: Código-fonte em múltiplas linguagens (Python, JS, SQL, Rust);
   - Domínio Racional: Problemas de matemática, dedução e quebra-cabeças lógicos;
   - Diversidade de Extensão: Amostras variando de 10 tokens a 32.000 tokens.
2. **Determinação da Mistura de Dados (*Data Mix*):** Modela-se a proporção exata de cada categoria em cada fase do treinamento.
3. **Injeção Estratégica de Código e Matemática:** Estudos empíricos provam que dados de código e matemática não servem apenas para ensinar a programar ou calcular; eles funcionam como catalisadores de raciocínio abstrato para o modelo inteiro.
4. **Recozimento de Dados (*Data Annealing*):** Na fase final do pré-treino, eleva-se progressivamente a proporção de dados de alta densidade informativa (código limpo e artigos matemáticos) acompanhada de uma redução na taxa de aprendizado, provocando saltos expressivos nos benchmarks de inteligência.

### Entradas e saídas

- **Entradas:** Corpora diversificados categorizados e rotulados tematicamente.
- **Saídas:** Um dataset combinado que maximiza o escore médio de avaliação multidimensional.

## 📐 Formulação matemática

O estudo empírico do **Llama 3** (Dubey et al., 2024) documenta como a distribuição proporcional ótima da mistura de dados se transforma drasticamente entre as etapas do ciclo de vida:

| Categoria Temática | Pré-Treinamento | Ajuste Fino Supervisionado (SFT) | Alinhamento de Preferência |
|---|---|---|---|
| **Conhecimento Geral (Inglês)** | $50{,}0\%$ | $52{,}66\%$ | $81{,}99\%$ |
| **Matemática e Raciocínio** | $25{,}0\%$ | $21{,}19\%$ | $5{,}89\%$ |
| **Programação e Código** | $17{,}0\%$ | $14{,}89\%$ | $6{,}93\%$ |
| **Multilíngue** | $8{,}0\%$ | $3{,}01\%$ | $5{,}19\%$ |
| **Tarefas Tipo Exame** | — | $8{,}14\%$ | — |
| **Contexto Longo** | — | $0{,}11\%$ | — |

No pré-treino e SFT, a soma de matemática e código compõe **mais de $36\%$ a $42\%$** de todo o treinamento, valor ordens de magnitude superior à presença natural dessas categorias na internet pública, comprovando que a cobertura deve ser artificialmente balanceada para privilégio de raciocínio formal.
O experimento de Zhou et al. (2023) com 2.000 amostras provou que modelos treinados em dados **diversos e de alta qualidade** superam em quase duas vezes a acurácia de modelos treinados apenas com qualidade sem diversidade.

## 🧱 Hipóteses e condições de validade

- A diversidade deve ser genuína e estrutural; adicionar centenas de variações cosméticas da mesma pergunta altera apenas o vocabulário superficial sem conferir ganho real de cobertura conceitual.

## ✅ Quando usar

- Concepção e calibração de pipelines de pré-treinamento e ajuste fino de modelos de fundação generalistas ou corporativos.
- Planejamento curricular de dados de modelos que atuarão como agentes autônomos em ambientes variados.

## 🚫 Quando não usar

- Em adaptadores LoRA hiper-especializados cujo único propósito contratual estrito seja executar uma única rotina determinística de formatação (onde a especialização extrema é o objetivo desejado).

## ⚠️ Limitações e armadilhas

- **O Dilema da Adição de Dados (*Data Addition Dilemma*, Shen et al., 2024):** Injetar dados heterogêneos desbalanceados ou de baixa compatibilidade distribucional pode, em certos cenários, degradar a performance do modelo em tarefas primárias em vez de aprimorá-la.
- **Sub-representação linguística:** Reservar menos de 5% a 8% para dados multilíngues perpetua a ineficiência de tokenização e eleva a taxa de erros em idiomas secundários.

## 🔍 Comparações

| Abordagem de Cobertura | Vantagem Primária | Ponto Cego Crítico |
|---|---|---|
| **Dataset Focado em Domínio Único** | Maestria rápida na tarefa específica | Perda catastrófica de capacidade de raciocínio geral |
| **Dataset Balanceado Multidomínio** | **Alta capacidade de transferência e generalização** | Exige esforço complexo de balanceamento de dados |
| **Raspagem Bruta sem Balanceamento** | Volume abundante e barato de dados | Reflete as assimetrias e vícios da internet aberta |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma equipe quer criar um assistente virtual para advogados tributaristas.

- Se o dataset contiver **apenas petições tributárias**, o modelo decora termos como "ICMS" e "imunidade tributária", mas falha miseravelmente quando o advogado pede para ele calcular a alíquota composta ou estruturar os dados em uma tabela JSON.
- A equipe aplica **alta cobertura**: insere 60% de petições jurídicas, 20% de exercícios de matemática financeira com passos de resolução e 20% de códigos Python e esquemas JSON. O modelo resultante passa a interpretar as leis, calcular os impostos com precisão e entregar a resposta estruturada diretamente na planilha do advogado.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/qualidade-e-conformidade-de-dados.md|Qualidade e Conformidade de Dados]]
- [[redes/ai-engineering/conceitos/sintese-de-instrucoes-e-self-instruct.md|Síntese de Instruções e Self-Instruct]]

### Alternativas

- Treinamento em dados mono-temáticos puros.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]
- [[redes/ai-engineering/conceitos/fatiamento-de-dados-e-paradoxo-de-simpson.md|Fatiamento de Dados e Paradoxo de Simpson]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 369–372
- **Evidência:** Chip Huyen apresenta a Tabela 8-1 detalhando as proporções de dados em todas as fases do Llama 3 (Meta), discute a importância de código e matemática para o raciocínio global e analisa o experimento de Zhou et al. (2023) comparando modelos treinados sob diferentes regimes de qualidade versus diversidade (Figura 8-1).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Cobertura e Diversidade de Dados e por que ela é indispensável para evitar o sobreajuste de modelos de fundação?
2. Por que conjuntos de dados de treinamento de LLMs contêm proporções artificialmente altas de código e matemática (frequentemente superiores a 35%)?
3. Como as proporções da mistura de dados se transformam entre o pré-treinamento, o SFT e o alinhamento de preferência no Llama 3?
4. O que é a técnica de "recozimento de dados" (*data annealing*) e qual o seu impacto na fase final de pré-treinamento?
5. Qual foi o resultado demonstrado pelo experimento de Zhou et al. (2023) ao comparar datasets que combinavam qualidade versus diversidade?
6. O que é o "Dilema da Adição de Dados" documentado por Shen et al. (2024)?
7. De que maneira a inclusão de diferentes extensões de contexto fortalece a resiliência do modelo contra o efeito *lost-in-the-middle*?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
