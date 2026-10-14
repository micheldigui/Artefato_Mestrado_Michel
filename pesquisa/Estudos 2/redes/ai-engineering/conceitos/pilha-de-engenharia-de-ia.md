# 🧠 Pilha de Engenharia de IA

**Rede:** `ai-engineering`   **Área:** `arquitetura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 35–39

## 📝 Definição

### Definição formal

A **Pilha de Engenharia de IA** (*AI Engineering Stack*) é o modelo arquitetural de referência estruturado em três camadas hierárquicas interdependentes que englobam a totalidade dos componentes de software, modelos, dados e hardware necessários para construir, adaptar, implantar e monitorar aplicações baseadas em modelos de fundação:

1. **Camada de Aplicação** (*Application Layer*);
2. **Camada de Desenvolvimento de Modelos** (*Model Development Layer*);
3. **Camada de Infraestrutura** (*Infrastructure Layer*).

### Em linguagem simples

É o mapa de engenharia que mostra onde cada pedaço da tecnologia de IA se encaixa. Ele explica a diferença entre quem está desenhando a tela e o prompt para o usuário (topo da pilha), quem está ajustando o modelo e preparando dados (meio) e quem está gerenciando os servidores e as placas de vídeo nos data centers (base).

### Escopo e distinções

Não se confunde com pilhas puras de desenvolvimento web (como MERN ou LAMP) nem com pipelines monolíticos de MLOps clássico. A pilha de IA acomoda novas abstrações, como bancos vetoriais, frameworks de orquestração de prompts, guardrails e serviços gerenciados de modelos (*MaaS*).

## 🧩 Problema que resolve

Resolve a desorganização de responsabilidades e ferramentas no ciclo de vida de produtos de inteligência artificial. Sem a delimitação clara das camadas da pilha, equipes confundem otimizações de servidor com problemas de qualidade de prompt, ou tentam resolver gargalos de interface alterando matrizes de peso na infraestrutura.

## 💡 Intuição

Pense em um restaurante de alta gastronomia:

- **Camada de Aplicação:** É o salão de atendimento, o garçom, o cardápio e a apresentação visual do prato que o cliente experimenta.
- **Camada de Desenvolvimento de Modelos:** É a cozinha principal, onde os chefs combinam receitas, ajustam temperos e refinam as preparações básicas.
- **Camada de Infraestrutura:** É a despensa refrigerada, os fornos industriais de alta potência, o fornecimento contínuo de gás e energia e a gestão logística de insumos básicos.

## ⚙️ Como funciona

A interação técnica entre as três camadas opera verticalmente:

### Etapas

1. **Camada de Aplicação:** 
   - Recebe as entradas dos usuários por interfaces web, móveis ou extensões.
   - Aplica técnicas de [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]] e orquestra a injeção de contexto via [[redes/ai-engineering/conceitos/rag.md|RAG]].
   - Executa rotinas de avaliação de saída e aplica guardrails de segurança.
2. **Camada de Desenvolvimento de Modelos:**
   - Realiza a curadoria e processamento de dados ([[redes/ai-engineering/conceitos/auto-supervisao.md|auto-supervisão]], limpeza, deduplicação).
   - Executa procedimentos de [[redes/ai-engineering/conceitos/finetuning.md|ajuste fino (finetuning)]] e destilação.
   - Aplica otimizações de inferência de baixo nível (quantização e paralelismo de tensores).
3. **Camada de Infraestrutura:**
   - Gerencia clusters físicos de processamento (GPUs, TPUs).
   - Garante a orquestração de servidores de atendimento (*model serving*) e controle de tráfego.
   - Executa o monitoramento operacional de latência, vazão e integridade de hardware.

1. **Camada de Aplicação:** 
   - Recebe as entradas dos usuários por interfaces web, móveis ou extensões.
   - Aplica técnicas de [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]] e orquestra a injeção de contexto via [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]].
   - Executa rotinas de avaliação de saída e aplica guardrails de segurança.
2. **Camada de Desenvolvimento de Modelos:**
   - Realiza a curadoria e processamento de dados ([[redes/ai-engineering/conceitos/auto-supervisao.md|auto-supervisão]], limpeza, deduplicação).
   - Executa procedimentos de [[redes/ai-engineering/conceitos/ajuste-fino.md|ajuste fino (finetuning)]] e destilação.
   - Aplica otimizações de inferência de baixo nível (quantização e paralelismo de tensores).
3. **Camada de Infraestrutura:**
   - Gerencia clusters físicos de processamento (GPUs, TPUs).
   - Garante a orquestração de servidores de atendimento (*model serving*) e controle de tráfego.
   - Executa o monitoramento operacional de latência, vazão e integridade de hardware.

### Entradas e saídas

- **Entradas:** Carga de trabalho de usuários no topo; capacidade computacional de silício na base.
- **Saídas:** Respostas cognitivas confiáveis entregues aos clientes com observabilidade e custos controlados.

## 📐 Formulação matemática

Não aplicável diretamente como fórmula matemática contínua. Representa-se arquiteturalmente como uma relação de dependência hierárquica e latência cumulativa:

$$T_{\text{total}} = T_{\text{aplicação}} + T_{\text{recuperação}} + T_{\text{inferência(modelo)}} + T_{\text{rede(infra)}}$$

Onde cada camada é responsável por minimizar sua parcela de sobrecarga temporal e financeira no custo total de propriedade (*TCO*).

## 🧱 Hipóteses e condições de validade

- Desacoplamento técnico: a camada de aplicação deve ser projetada para ser agnóstica ao modelo de fundação base sempre que possível, viabilizando a substituição de provedores sem reconstrução da interface.

## ✅ Quando usar

- Estruturação de equipes técnicas multidisciplinares de IA.
- Auditoria de arquitetura corporativa para identificar lacunas de segurança, monitoramento ou desempenho.
- Planejamento de contratação de ferramentas e infraestrutura em nuvem.

## 🚫 Quando não usar

- Aplicações triviais de uso pessoal de prompts sem qualquer integração de produto ou tráfego recorrente.

## ⚠️ Limitações e armadilhas

- **Superdimensionamento precoce:** Construir pipelines complexos de desenvolvimento de modelos e clusters próprios de infraestrutura antes de validar o produto na camada de aplicação via APIs comerciais simples.
- **Ignorar a camada de infraestrutura:** Subestimar o custo de rede, throughput de tokens e a volatilidade de disponibilidade de GPUs de alta performance no mercado global.

## 🔍 Comparações

| Camada | Foco Principal | Ferramental Paradigmático | Perfil Profissional |
|---|---|---|---|
| **Aplicação** | Contexto, prompt, interface, UX e avaliação | LangChain, LlamaIndex, vLLM Client, eval harnesses | Engenheiro de IA, Desenvolvedor Full-Stack |
| **Desenvolvimento de Modelos** | Ajuste fino, quantização e curadoria | PyTorch, Hugging Face, Axolotl, DeepSpeed | Engenheiro de ML, Cientista de Dados |
| **Infraestrutura** | Hospedagem, clusters de GPU e monitoramento | Kubernetes, Triton Inference Server, CUDA, Slurm | Engenheiro de MLOps, Engenheiro de Plataforma |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma startup de tecnologia educacional cria um tutor de matemática personalizado.

- Na **Camada de Infraestrutura**, a equipe aluga uma instância de nuvem com 8 GPUs conectadas por rede de alta largura de banda.
- Na **Camada de Desenvolvimento de Modelos**, o time pega o modelo aberto Llama 3 e aplica técnicas de quantização e ajuste fino sobre provas históricas de vestibulares.
- Na **Camada de Aplicação**, os engenheiros criam uma interface web em React, integram ferramentas de rendering de fórmulas matemáticas (LaTeX) e desenham prompts defensivos para impedir que os alunos usem o tutor para colar em tarefas não permitidas.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]]
- [[redes/ai-engineering/conceitos/desafio-da-ultima-milha-em-ia.md|Desafio da Última Milha em IA]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (representa a taxonomia padrão da indústria para arquitetura de sistemas).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]
- [[redes/ai-engineering/conceitos/rag.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/finetuning.md|Ajuste Fino (Finetuning)]]

- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]
- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 35–39
- **Evidência:** Chip Huyen estabelece a estrutura de três camadas da pilha de IA através do diagrama da Figura 1-14 e analisa a evolução temporal de repositórios do GitHub pertencentes a cada categoria.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as três camadas fundamentais que compõem a Pilha de Engenharia de IA?
2. Quais responsabilidades técnicas pertencem exclusivamente à camada de aplicação?
3. Como a camada de infraestrutura de IA se diferencia da infraestrutura de software web tradicional?
4. Por que repositórios voltados à camada de aplicação cresceram com velocidade muito superior aos de infraestrutura após 2023?
5. Qual é o papel da camada de desenvolvimento de modelos dentro de uma empresa que não treina LLMs do zero?
6. De que forma o desacoplamento entre as camadas da pilha reduz o risco de dependência de fornecedor (*vendor lock-in*)?
7. Por que iniciar o desenvolvimento de um produto de IA pela camada de infraestrutura costuma ser um erro de engenharia?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
