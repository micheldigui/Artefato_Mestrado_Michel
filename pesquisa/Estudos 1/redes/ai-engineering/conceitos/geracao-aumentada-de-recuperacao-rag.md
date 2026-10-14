# 🧠 Geração Aumentada de Recuperação (RAG)

**Rede:** `ai-engineering`  
**Área:** `recuperacao-de-informacao`

**Rede:** `ai-engineering`   **Área:** `desenvolvimento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG e Agentes
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 11, 253–257

## 📝 Definição

### Definição formal

Um padrão arquitetural composto por um subsistema de recuperação (*Retriever*) e um subsistema gerador (*Generator*), projetado para buscar dinamicamente informações contextuais em fontes de dados externas com base em uma consulta e incorporá-las no prompt de entrada do modelo de linguagem.

A **Geração Aumentada de Recuperação** (*Retrieval-Augmented Generation* — RAG) é um padrão arquitetural de sistemas de IA no qual a geração de resposta por um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] é dinamicamente condicionada a evidências e passagens factuais pertinentes previamente recuperadas de uma base externa de dados ou documentos, em resposta à consulta do usuário.

### Em linguagem simples

É a técnica fundamental que conecta a IA a uma biblioteca ou base de dados privada para que ela pesquise os fatos corretos antes de redigir uma resposta baseada em documentos reais.

É a técnica de dar um "livro de consultas aberto" para a IA durante uma prova. Em vez de exigir que o modelo adivinhe ou puxe de sua memória interna um dado confidencial ou recente da sua empresa, o sistema busca primeiro os parágrafos relevantes nos seus arquivos e coloca esses textos dentro da pergunta para o modelo ler antes de responder.

### Escopo e distinções

Diferencia-se da memória interna do modelo (pré-treino) e do ajuste fino (*finetuning*). O RAG injeta dados factuais dinamicamente no nível do prompt sem alterar os parâmetros internos de peso da rede neural.

Não se confunde com um simples buscador web nem com o [[redes/ai-engineering/conceitos/ajuste-fino.md|ajuste fino]]. O RAG não altera os parâmetros internos do modelo. É uma técnica de tempo de execução pertencente aos métodos de [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|adaptação de modelos]] baseados em contexto.

## 🧩 Problema que resolve

Resolve o problema da desatualização de dados dos modelos de fundação e o risco crítico de alucinação de fatos corporativos ou privados que não estavam disponíveis no momento do treinamento original.

Resolve três das maiores limitações intrínsecas dos modelos de fundação:

1. **Alucinações factuais:** Fornece o documento-fonte como âncora de verdade para que o modelo cite e extraia fatos reais.
2. **Desatualização temporal (*knowledge cutoff*):** Permite responder sobre eventos de ontem sem precisar re-treinar o modelo.
3. **Privacidade de dados corporativos:** Permite acessar bases confidenciais sem necessidade de expor essas informações durante o pré-treinamento público de um modelo.

## 💡 Intuição

Pense em um profissional experiente que, ao receber uma pergunta complexa sobre o relatório fiscal de ontem da empresa, não tenta adivinhar de cabeça, mas abre o arquivo contábil no computador para conferir os números exatos antes de falar.

Pense em um juiz em um tribunal. Ele possui formação ampla em direito (o modelo de fundação pré-treinado). Contudo, ele não guarda na cabeça todos os detalhes de um contrato corporativo assinado ontem entre duas empresas litigantes. O oficial de justiça busca os autos do processo no arquivo e entrega a pasta em suas mãos (o componente de recuperação). O juiz lê o contrato anexado e dita o parecer com precisão impecável (a geração aumentada).

## ⚙️ Como funciona

A arquitetura clássica desdobra-se em duas fases fundamentais:

### Etapas

1. **Indexação:** Documentos externos são divididos em pedaços menores (*chunks*), convertidos em vetores (*embeddings*) e armazenados em um banco de dados vetorial ou indexados via índices invertidos textuais.
2. **Consulta (Query):** O usuário submete uma pergunta.
3. **Recuperação:** O *retriever* busca os trechos mais relevantes da base de dados usando busca semântica, lexical ou híbrida.
4. **Geração:** O modelo de fundação recebe a pergunta do usuário somada aos trechos recuperados (*contexto*) e redige a resposta final.

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

### Entradas e saídas

- Entradas: Consulta do usuário e base de dados externa de documentos.
- Saídas: Resposta gerada fundamentada estritamente nos dados recuperados.

- **Entradas:** Consulta do usuário em linguagem natural e uma base de dados não estruturados ou relacionais.
- **Saídas:** Resposta em linguagem natural contendo referências diretas, dados precisos e citações comprováveis.

## 📐 Formulação matemática

Dado um modelo gerador $M$, uma consulta $q$ e uma função de recuperação $R$ sobre um corpus $D$:

$$\text{Resposta} = M(q, R(q, D))$$

Onde o recuperador $R$ retorna os $k$ trechos textuais $d_1, d_2, \dots, d_k \subset D$ que maximizam a pontuação de relevância em relação a $q$.

Em uma formulação probabilística desacoplada, o sistema modela a probabilidade da resposta $Y$ integrando sobre o conjunto de passagens recuperadas $Z = \{z_1, \dots, z_k\}$ dado o prompt $X$:

$$P(Y \mid X) = \sum_{z \in Z} P(z \mid X) \, P(Y \mid X, z)$$

Onde:

- $P(z \mid X)$ representa a probabilidade de relevância do documento $z$ calculada pelo componente de busca (*retriever*);
- $P(Y \mid X, z)$ representa a probabilidade de geração do texto pelo modelo de fundação (*generator*) condicionado ao documento selecionado.

## 🧱 Hipóteses e condições de validade

- Supõe que o mecanismo de recuperação é capaz de trazer os documentos corretos e que a janela de contexto do modelo gerador é capaz de processar os trechos injetados sem perda de foco (*lost-in-the-middle*).

- A informação necessária para responder à dúvida do usuário deve existir na base de dados indexada.
- O componente de recuperação (*retriever*) deve ser capaz de posicionar os documentos verdadeiramente relevantes entre os primeiros resultados retornados.

## ✅ Quando usar

- Em assistentes corporativos, busca em bases de conhecimento, análise de contratos, suporte técnico e qualquer sistema que exija respostas baseadas em documentos privados ou atualizados.

- Bases de conhecimento dinâmicas que mudam frequentemente (notícias, preços de produtos, manuais internos).
- Aplicações corporativas com tolerância zero a alucinações factuais e que exigem auditoria e comprovação de fontes.
- Casos de uso do tipo "converse com seus documentos" (*talk-to-your-docs*).

## 🚫 Quando não usar

- Em tarefas que dependem exclusivamente de raciocínio abstrato, criatividade literária pura ou lógica matemática interna que não exija consulta a fatos externos.

- Tarefas centradas puramente em estilo de escrita, formato sintático rígido ou raciocínio sem necessidade de busca factual externa.
- Cenários em que toda a base de conhecimento necessária cabe com folga dentro da janela nativa de contexto do modelo sem ônus excessivo de custo de inferência.

## ⚠️ Limitações e armadilhas

- **Falhas de Recuperação:** Se o recuperador trouxer documentos errados, a IA gerará uma resposta errada ou alucinada com base em premissas falsas ("lixo entra, lixo sai").
- Latência e custos adicionais associados à infraestrutura de busca vetorial.

- **Falha de recuperação:** Se o buscador retornar trechos irrelevantes, o modelo pode alucinar ou afirmar que não encontrou a resposta mesmo que ela esteja em outro documento da base.
- **Envenenamento de contexto (*indirect prompt injection*):** Documentos externos recuperados podem conter instruções maliciosas ocultas que tentam sequestrar o comportamento do modelo.
- **Latência do pipeline:** A etapa extra de busca adiciona tempo ao processamento antes que o modelo gere o primeiro token (*TTFT*).

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[geracao-aumentada-de-recuperacao-rag|RAG]] | Fornecer fatos externos em tempo de execução via prompt. | Consulta + Documentos externos recuperados. | Resposta fundamentada baseada em fatos. | Insere dados factuais dinamicamente sem alterar os pesos do modelo. |
| [[finetuning|Finetuning]] | Ajustar o comportamento, estilo e formato do modelo. | Dataset de demonstração (*Instruction/Response*). | Modelo com pesos atualizados. | Altera os pesos internos permanentes da rede neural. |

| Critério | Geração Aumentada de Recuperação (RAG) | Ajuste Fino (*Finetuning*) |
|---|---|---|
| **Mecanismo** | Recuperação dinâmica de documentos em tempo real | Internalização de padrões nos pesos da rede |
| **Atualização de fatos** | Instantânea (basta atualizar o banco de dados) | Lenta (exige novo treinamento de ajuste) |
| **Auditoria** | Alta (aponta a página e parágrafo exatos da fonte) | Baixa (o modelo não cita pesos individuais) |
| **Custo de manutenção** | Baixo a moderado (manutenção de índices e buscas) | Elevado (treinamentos frequentes em GPUs) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um usuário pergunta ao bot de RH: "Quantos dias de férias posso tirar após completar um ano?". O sistema RAG busca o artigo exato da CLT salvo no banco vetorial da empresa, injeta o parágrafo no prompt, e a IA responde informando exatamente 30 dias.

Um cliente pergunta ao chatbot de um banco: `"Qual é o limite de saque internacional do meu cartão Platinum em finais de semana?"`. 
O modelo não sabe a resposta de cabeça. O sistema faz uma busca no banco vetorial dos contratos do banco, localiza a cláusula 14.2 que estipula o limite em `$R`\$ 2.000,00$, injeta esse parágrafo no prompt e o modelo responde com precisão citando a cláusula do contrato.

## 🔗 Relações no grafo

### Pré-requisitos

- [[modelo-de-fundacao|Modelo de Fundação]]

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]]
- [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]]

### Alternativas

- [[finetuning|Finetuning]]

- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]
- [[redes/ai-engineering/conceitos/desafio-da-ultima-milha-em-ia.md|Desafio da Última Milha em IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG e Agentes
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da arquitetura RAG, separando componentes de recuperação (*retriever*) e geração (*generator*).
- **Confiança:** alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 11, 253–257
- **Evidência:** O texto define o padrão RAG como uma das três técnicas essenciais de adaptação de modelos, explicando sua origem no trabalho de Lewis et al. (2020) e destacando seu papel em mitigar alucinações e expandir a memória factual dos modelos com bases externas.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Geração Aumentada de Recuperação (RAG)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

1. Qual é a definição formal de RAG e quais são os dois componentes centrais de sua arquitetura?
2. Por que o RAG é preferível ao Finetuning para incorporar informações factuais que se alteram frequentemente?
3. Como a técnica de RAG auxilia diretamente na mitigação do fenômeno de alucinação em LLMs?
4. Quais são as etapas envolvidas no pipeline de RAG, desde a ingestão do documento até a geração da resposta?
5. Qual é o impacto do RAG sobre a latência percebida pelo usuário final (*TTFT*)?
6. O que é uma falha de recuperação (*retrieval failure*) e como ela compromete a geração final do modelo?
7. Como a técnica de RAG permite aplicar governança e auditoria sobre as respostas dadas por um modelo de fundação?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 6 — RAG e Agentes. A interpretação final deve ser revisada pelo estudante.*
