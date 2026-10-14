# 🧠 Geração Aumentada de Recuperação (RAG)

**Rede:** `ai-engineering`   **Área:** `desenvolvimento`

**Rede:** `ai-engineering`  
areas: `recuperacao-de-informacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

A **Geração Aumentada de Recuperação** (*Retrieval-Augmented Generation* — RAG) é um padrão arquitetural de sistemas de IA no qual a geração de resposta por um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] é dinamicamente condicionada a evidências e passagens factuais pertinentes previamente recuperadas de uma base externa de dados ou documentos, em resposta à consulta do usuário.

Um padrão arquitetural que melhora a qualidade de geração de um modelo de fundação ao buscar dinamicamente documentos ou trechos relevantes em uma fonte externa de dados e injetá-los no contexto de entrada do modelo.

### Em linguagem simples

É a técnica de dar um "livro de consultas aberto" para a IA durante uma prova. Em vez de exigir que o modelo adivinhe ou puxe de sua memória interna um dado confidencial ou recente da sua empresa, o sistema busca primeiro os parágrafos relevantes nos seus arquivos e coloca esses textos dentro da pergunta para o modelo ler antes de responder.

É a técnica de dar acesso a um "livro de consultas" ou base de dados interna para a IA, permitindo que ela pesquise as informações corretas antes de redigir a resposta final para o usuário.

### Escopo e distinções

Não se confunde com um simples buscador web nem com o [[redes/ai-engineering/conceitos/finetuning.md|ajuste fino]]. O RAG não altera os parâmetros internos do modelo. É uma técnica de tempo de execução pertencente aos métodos de [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|adaptação de modelos]] baseados em contexto.

Diferencia-se do ajuste fino (*finetuning*): o RAG fornece fatos atualizados em tempo de execução via contexto, enquanto o finetuning altera o comportamento estrutural e o estilo do modelo.

## 🧩 Problema que resolve

Resolve três das maiores limitações intrínsecas dos modelos de fundação:

1. **Alucinações factuais:** Fornece o documento-fonte como âncora de verdade para que o modelo cite e extraia fatos reais.
2. **Desatualização temporal (*knowledge cutoff*):** Permite responder sobre eventos de ontem sem precisar re-treinar o modelo.
3. **Privacidade de dados corporativos:** Permite acessar bases confidenciais sem necessidade de expor essas informações durante o pré-treinamento público de um modelo.

Resolve o problema da desatualização temporal dos modelos de fundação e o risco crítico de alucinação de dados privados ou corporativos que não estavam presentes no corpus original de pré-treinamento.

## 💡 Intuição

Pense em um juiz em um tribunal. Ele possui formação ampla em direito (o modelo de fundação pré-treinado). Contudo, ele não guarda na cabeça todos os detalhes de um contrato corporativo assinado ontem entre duas empresas litigantes. O oficial de justiça busca os autos do processo no arquivo e entrega a pasta em suas mãos (o componente de recuperação). O juiz lê o contrato anexado e dita o parecer com precisão impecável (a geração aumentada).

Imagine um estudante prestando um exame com consulta: em vez de tentar lembrar de tudo o que estudou no ano passado, ele abre o manual da empresa na página exata para responder corretamente à pergunta do cliente.

## ⚙️ Como funciona

A arquitetura clássica desdobra-se em duas fases fundamentais:

### Etapas

1. **Indexação (offline):** 
   - Documentos corporativos são fatiados em pequenos pedaços (*chunks*).
   - Um modelo de representação (*embedding*) converte cada pedaço em um vetor matemático.
   - Os vetores são indexados em um banco de dados vetorial ou sistema de busca.
2. **Recuperação (*Retrieval* — online):**
   - A pergunta do usuário é convertida em vetor de busca.
   - O algoritmo de busca identifica os $k$ pedaços de documentos matematicamente mais similares à pergunta.
3. **Aumento (*Augmentation*):**
   - Os documentos recuperados são concatenados com a pergunta original dentro de um template de prompt.
4. **Geração (*Generation*):**
   - O modelo de fundação lê a pergunta acompanhada do contexto recuperado e sintetiza a resposta final fundamentada nos dados fornecidos.

1. O usuário submete uma consulta (*query*).
2. O sistema recupera documentos relevantes de um repositório externo (ex: base vetorial).
3. Os documentos recuperados são combinados com a consulta original formando um prompt enriquecido.
4. O modelo de fundação processa o prompt enriquecido e gera uma resposta fundamentada.

### Entradas e saídas

- **Entradas:** Consulta do usuário em linguagem natural e uma base de dados não estruturados ou relacionais.
- **Saídas:** Resposta em linguagem natural contendo referências diretas, dados precisos e citações comprováveis.

- Entradas: Consulta do usuário e corpus externo de documentos.
- Saídas: Resposta gerada pelo modelo fundamentada estritamente nos dados recuperados.

## 📐 Formulação matemática

Em uma formulação probabilística desacoplada, o sistema modela a probabilidade da resposta $Y$ integrando sobre o conjunto de passagens recuperadas $Z = \{z_1, \dots, z_k\}$ dado o prompt $X$:

$$P(Y \mid X) = \sum_{z \in Z} P(z \mid X) \, P(Y \mid X, z)$$

Onde:

- $P(z \mid X)$ representa a probabilidade de relevância do documento $z$ calculada pelo componente de busca (*retriever*);
- $P(Y \mid X, z)$ representa a probabilidade de geração do texto pelo modelo de fundação (*generator*) condicionado ao documento selecionado.

Seja $q$ a consulta do usuário, $D$ uma base de dados de documentos, e $R(q, D)$ a função de recuperação que extrai o subconjunto de documentos mais relevantes $d \subset D$. O modelo gerador $M$ produz a resposta $y$:

$$y \sim M(y \mid q, R(q, D))$$

Onde:
- $q$: Consulta de entrada.
- $R(q, D)$: Documentos recuperados externamente.
- $M$: Modelo de fundação gerador.

## 🧱 Hipóteses e condições de validade

- A informação necessária para responder à dúvida do usuário deve existir na base de dados indexada.
- O componente de recuperação (*retriever*) deve ser capaz de posicionar os documentos verdadeiramente relevantes entre os primeiros resultados retornados.

- Hipótese de que os documentos recuperados externamente contêm as informações factuais corretas necessárias para responder à consulta.

## ✅ Quando usar

- Bases de conhecimento dinâmicas que mudam frequentemente (notícias, preços de produtos, manuais internos).
- Aplicações corporativas com tolerância zero a alucinações factuais e que exigem auditoria e comprovação de fontes.
- Casos de uso do tipo "converse com seus documentos" (*talk-to-your-docs*).

- Em aplicações que exigem consulta a bases de conhecimento internas, documentos corporativos atualizados, relatórios confidenciais e prevenção rigorosa de alucinações.

## 🚫 Quando não usar

- Tarefas centradas puramente em estilo de escrita, formato sintático rígido ou raciocínio sem necessidade de busca factual externa.
- Cenários em que toda a base de conhecimento necessária cabe com folga dentro da janela nativa de contexto do modelo sem ônus excessivo de custo de inferência.

- Em cenários onde o conhecimento exigido é puramente conceitual e universal (já presente no pré-treinamento estático) e não sofre alterações temporais.

## ⚠️ Limitações e armadilhas

- **Falha de recuperação:** Se o buscador retornar trechos irrelevantes, o modelo pode alucinar ou afirmar que não encontrou a resposta mesmo que ela esteja em outro documento da base.
- **Envenenamento de contexto (*indirect prompt injection*):** Documentos externos recuperados podem conter instruções maliciosas ocultas que tentam sequestrar o comportamento do modelo.
- **Latência do pipeline:** A etapa extra de busca adiciona tempo ao processamento antes que o modelo gere o primeiro token (*TTFT*).

- Falhas no recuperador (*retriever*) trazem documentos inúteis, fazendo a IA responder incorretamente ("lixo entra, lixo sai").
- Custos adicionais de indexação, armazenamento vetorial e chamadas de busca.

## 🔍 Comparações

| Critério | Geração Aumentada de Recuperação (RAG) | Ajuste Fino (*Finetuning*) |
|---|---|---|
| **Mecanismo** | Recuperação dinâmica de documentos em tempo real | Internalização de padrões nos pesos da rede |
| **Atualização de fatos** | Instantânea (basta atualizar o banco de dados) | Lenta (exige novo treinamento de ajuste) |
| **Auditoria** | Alta (aponta a página e parágrafo exatos da fonte) | Baixa (o modelo não cita pesos individuais) |
| **Custo de manutenção** | Baixo a moderado (manutenção de índices e buscas) | Elevado (treinamentos frequentes em GPUs) |

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[rag|RAG]] | Fornecer fatos externos em tempo de execução via contexto. | Consulta + Documentos externos recuperados. | Resposta fundamentada baseada em fatos. | Insere dados factuais dinamicamente sem alterar os pesos do modelo. |
| [[finetuning|Finetuning]] | Ajustar o comportamento, estilo e formato do modelo. | Dados de demonstração (*Instruction/Response*). | Modelo com pesos atualizados. | Altera os pesos internos permanentes da rede neural. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um cliente pergunta ao chatbot de um banco: `"Qual é o limite de saque internacional do meu cartão Platinum em finais de semana?"`. 
O modelo não sabe a resposta de cabeça. O sistema faz uma busca no banco vetorial dos contratos do banco, localiza a cláusula 14.2 que estipula o limite em `$R`\$ 2.000,00$, injeta esse parágrafo no prompt e o modelo responde com precisão citando a cláusula do contrato.

Um cliente pergunta ao bot de um banco: "Qual é a taxa de juros do meu cartão de crédito ouro atualizada hoje?". O sistema RAG busca o contrato digital do cliente no servidor do banco, injeta o parágrafo de juros no prompt, e o GPT-4 responde o valor exato.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]

- [[modelo-de-fundacao|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]]
- [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]]

- [[engenharia-de-ia|Engenharia de IA]]

### Alternativas

- [[redes/ai-engineering/conceitos/finetuning.md|Ajuste Fino (Finetuning)]]

- [[finetuning|Finetuning]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]
- [[redes/ai-engineering/conceitos/desafio-da-ultima-milha-em-ia.md|Desafio da Última Milha em IA]]

- Nenhuma relação suficientemente sustentada pelo capítulo.

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 11, 253–257
- **Evidência:** O texto define o padrão RAG como uma das três técnicas essenciais de adaptação de modelos, explicando sua origem no trabalho de Lewis et al. (2020) e destacando seu papel em mitigar alucinações e expandir a memória factual dos modelos com bases externas.
- **Confiança:** Alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da Geração Aumentada de Recuperação (RAG) como técnica fundamental de engenharia de IA para adaptar o modelo a dados externos.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. Qual é a definição formal de RAG e quais são os dois componentes centrais de sua arquitetura?
2. Por que o RAG é preferível ao Finetuning para incorporar informações factuais que se alteram frequentemente?
3. Como a técnica de RAG auxilia diretamente na mitigação do fenômeno de alucinação em LLMs?
4. Quais são as etapas envolvidas no pipeline de RAG, desde a ingestão do documento até a geração da resposta?
5. Qual é o impacto do RAG sobre a latência percebida pelo usuário final (*TTFT*)?
6. O que é uma falha de recuperação (*retrieval failure*) e como ela compromete a geração final do modelo?
7. Como a técnica de RAG permite aplicar governança e auditoria sobre as respostas dadas por um modelo de fundação?

1. O que é Geração Aumentada de Recuperação (RAG)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação. A interpretação final deve ser revisada pelo estudante.*
