# 🧠 Estratégias de Chunking e Otimização de RAG

**Rede:** `ai-engineering`   **Área:** `recuperacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 267–273

## 📝 Definição

### Definição formal

As **Estratégias de Chunking e Otimização de RAG** constituem o conjunto de técnicas de engenharia de dados e de fluxo de inferência voltadas a maximizar as métricas de precisão de contexto (*Context Precision*) e revocação de contexto (*Context Recall*) no pipeline de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]], estruturando-se em quatro pilares metodológicos:

1. **Estratégia de Chunking:** O fracionamento algorítmico de documentos contínuos em passagens atômicas (*chunks*) calibradas por unidades de corte (caracteres, parágrafos ou tokens) acompanhadas de **sobreposição posicional (*overlap*)** para preservar fronteiras semânticas;
2. **Reranqueamento (*Reranking*):** A reordenação de candidatos por modelos neurais densos pesados (*cross-encoders*) ou critérios temporais de recência;
3. **Reescrita de Consultas (*Query Rewriting*):** A reformulação, desambiguação e expansão da pergunta do usuário através de um LLM leve para torná-la autossuficiente e compatível com os índices de busca;
4. **Recuperação Contextual (*Contextual Retrieval* — Anthropic, 2024):** A injeção sistemática de metadados e resumos concisos explicativos no cabeçalho de cada chunk antes da indexação, situando o trecho dentro da totalidade do documento original.

### Em linguagem simples

São os truques de engenharia para fazer o sistema de busca da IA acertar o alvo com perfeição. Em vez de picotar um documento de qualquer jeito e cortar frases importantes pela metade, você define o tamanho exato de cada pedaço com uma margem de segurança de repetição entre eles. Além disso, se a pergunta do cliente for confusa, a IA reescreve a pergunta antes de buscar; e antes de salvar cada pedaço de texto no banco de dados, ela cola uma etiqueta explicando a qual documento e assunto aquele parágrafo pertencia.

### Escopo e distinções

Não se limita à simples configuração do tamanho do texto no código. Trata-se de uma intervenção em duas pontas: otimização na preparação e indexação dos dados brutos (chunking e contextual retrieval) e otimização dinâmica no momento da consulta (reescrita de query e reranking).

## 🧩 Problema que resolve

Resolve a síndrome do "chunk órfão" e a perda de contexto em limites de fragmentação. Se um parágrafo diz apenas `"A sua receita caiu 15% no último trimestre"`, o motor de busca vetorial não tem como saber a qual empresa o texto se refere porque o nome da corporação estava citado três páginas antes. As estratégias de otimização enriquecem os fragmentos com o contexto global do documento, eliminando recuperações inúteis.

## 💡 Intuição

Pense em recortar receitas de uma revista de culinária antiga para colar em um fichário:

- Se você recortar com a tesoura exatamente no limite do papel sem cuidado (**chunking ingênuo sem overlap**), você corta a lista de ingredientes na metade e joga fora a temperatura do forno que estava no topo da página seguinte.
- Se você tirar uma fotocópia com bordas largas (**overlap**) e escrever à mão com uma caneta vermelha no topo do recorte: `"[Receita de Torta de Maçã da Edição de Natal de 1995]"` (**Contextual Retrieval da Anthropic**), qualquer pessoa que achar aquele pedaço solto de papel na mesa saberá imediatamente do que se trata a receita.

## ⚙️ Como funciona

O pipeline opera articulando preparações em tempo de indexação e em tempo de execução:

### Etapas

1. **Particionamento com Sobreposição (*Chunking com Overlap*):**
   - O documento é dividido em janelas (ex.: 512 tokens ou 2.048 caracteres).
   - Define-se um overlap de 10% a 20% (ex.: 50 tokens) para garantir que a última frase do chunk 1 seja também a primeira frase do chunk 2, impedindo o corte de orações no meio.
2. **Contextual Retrieval (Prepend de Metadados):**
   - Antes de gerar os vetores, um LLM leve lê o documento inteiro e o chunk específico.
   - O LLM emite um resumo situacional conciso de 50 a 100 tokens explicando a que se refere o trecho.
   - Esse texto situacional é colado no topo do chunk e a versão combinada é enviada ao modelo de embedding e ao índice BM25.
3. **Reescrita de Consulta em Execução (*Query Rewriting*):**
   - Se o usuário perguntar em uma conversa contínua: `"E qual é o preço dele?"`, um LLM reescreve a query para torná-la autônoma: `"Qual é o preço do fone de ouvido Sony WH-1000XM5?"`.
4. **Reranking Cruzado (*Cross-Encoder*):**
   - O buscador recupera 50 candidatos rápidos via [[redes/ai-engineering/conceitos/busca-hibrida-e-reciprocal-rank-fusion.md|Busca Híbrida]].
   - Um modelo classificador pesado avalia o par `(query, candidato)` conjuntamente com atenção cruzada completa e seleciona com precisão cirúrgica apenas os 5 melhores para entrar no prompt do gerador.

### Entradas e saídas

- **Entradas:** Documentos extensos originais e perguntas conversacionais incompletas de usuários.
- **Saídas:** Chunks semanticamente autossuficientes e conjuntos de contexto ultrarrápido com altíssima precisão factual.

## 📐 Formulação matemática

No particionamento sequencial de um documento de comprimento $L$ com tamanho de chunk $C$ e sobreposição de corte $O$ ($O < C$), o índice inicial do $k$-ésimo chunk ($k \ge 0$) e a quantidade total de fragmentos $M$ são dados por:

$$\text{Início}(k) = k \cdot (C - O), \quad M = \left\lceil \frac{L - O}{C - O} \right\rceil$$

Na abordagem do **Contextual Retrieval**, seja $D$ o documento integral e $c_k$ o fragmento bruto. Um modelo paramétrico gera a âncora textual contextual $\alpha_k$:

$$\alpha_k = f_{\text{LLM}}(D, c_k) \implies c_k^* = [\alpha_k \circ c_k]$$

O embedding final indexado no banco vetorial é $\mathbf{e}_k = \text{Embed}(c_k^*)$, cujas dimensões incorporam a densidade semântica do documento pai.

## 🧱 Hipóteses e condições de validade

- A sobreposição de corte ($O$) deve ser calibrada: overlaps muito pequenos não evitam a quebra de frases longas; overlaps muito grandes duplicam desnecessariamente o volume de chunks e os custos de armazenamento vetorial.

## ✅ Quando usar

- Bases corporativas com manuais complexos, relatórios financeiros e contratos com seções interdependentes.
- Chatbots de múltiplos turnos onde usuários utilizam pronomes e perguntas curtas que dependem do histórico imediato para serem entendidas.

## 🚫 Quando não usar

- Bases de dados compostas estritamente por perguntas e respostas atômicas já curadas (onde cada par FAQ já é naturalmente um chunk perfeito e autocontido).

## ⚠️ Limitações e armadilhas

- **Custo computacional no Contextual Retrieval:** Rodar um LLM para gerar um cabeçalho para cada um de 100.000 chunks pode custar centenas de dólares antes da aplicação sequer entrar em produção.
- **Latência do Reranker:** Modelos de cross-encoder são lentos na inferência; usá-los para reordenar 500 candidatos pode adicionar mais de um segundo à resposta final.

## 🔍 Comparações

| Técnica de Otimização | Momento de Aplicação | O que altera? | Principal Impacto |
|---|---|---|---|
| **Chunking com Overlap** | Indexação (Offline) | Estrutura física dos fragmentos | Elimina perda de contexto nas bordas |
| **Contextual Retrieval** | Indexação (Offline) | Enriquece o conteúdo textual do chunk | Elimina chunks órfãos sem assunto definido |
| **Reescrita de Query** | Inferência (Online) | A pergunta enviada aos buscadores | Resolve ambiguidades e pronomes em diálogos |
| **Cross-Encoder Reranking** | Inferência (Online) | A ordenação dos documentos recuperados | Eleva drasticamente a precisão do top-5 |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Considere o diálogo em um chatbot de suporte de software:

- Usuário: `"Como instalo o aplicativo no Windows?"`
- IA: `"Você deve baixar o instalador .exe e executar como administrador."`
- Usuário: `"E se der erro de permissão nele?"`

Se o sistema fizer a busca com o texto bruto `"E se der erro de permissão nele?"`, o motor vetorial não sabe o que é "nele" e traz manuais de permissão de servidores Linux.
O módulo de **Reescrita de Query** analisa a conversa e reescreve a pergunta para: `"Como resolver erro de permissão ao executar o instalador .exe no Windows?"`. 
A busca recupera a página exata da base de suporte, garantindo a resposta correta.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/algoritmos-de-recuperacao-lexical-e-vetorial.md|Algoritmos de Recuperação: Lexical versus Vetorial]]

### Complementos

- [[redes/ai-engineering/conceitos/busca-hibrida-e-reciprocal-rank-fusion.md|Busca Híbrida e Reciprocal Rank Fusion (RRF)]]
- [[redes/ai-engineering/conceitos/eficiencia-de-contexto-e-lost-in-the-middle.md|Eficiência de Contexto e Efeito Lost-in-the-Middle]]

### Alternativas

- Injeção forçada do documento integral na janela de contexto nominal sem fragmentação.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/embeddings.md|Embeddings]]
- [[redes/ai-engineering/conceitos/rag-multimodal-e-dados-tabulares.md|RAG Multimodal e Dados Tabulares (Text-to-SQL)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 267–273
- **Evidência:** Chip Huyen discute o impacto do tamanho de chunks e trade-offs de overlap, formaliza a técnica de query rewriting para diálogos, analisa o reranqueamento temporal e apresenta detalhadamente a técnica de Contextual Retrieval desenvolvida pela Anthropic (2024), incluindo o template oficial de prompt de situacionamento de chunks.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as quatro táticas fundamentais de otimização de sistemas de RAG descritas no capítulo?
2. Por que a introdução de sobreposição (*overlap*) no particionamento de documentos é indispensável para a integridade semântica?
3. O que é a técnica de Contextual Retrieval desenvolvida pela Anthropic e como ela neutraliza o problema dos chunks descontextualizados?
4. Como o processo de Reescrita de Consultas (*Query Rewriting*) atua para resolver pronomes e ambiguidades em conversas de múltiplos turnos?
5. Qual é o papel de um modelo de reranqueamento (*cross-encoder*) e em que ele se diferencia dos modelos tradicionais de embedding duplo (*bi-encoders*)?
6. Quais são as penalidades operacionais de latência e custo associadas ao uso de LLMs para reescrever consultas a cada turno de diálogo?
7. Como a fragmentação por tokens específicos do vocabulário do modelo gerador se compara com a fragmentação tradicional por caracteres ou parágrafos?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
