# 🧠 Modelo de Linguagem Mascarado

**Rede:** `ai-engineering`   **Área:** `modelagem`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 4–5

## 📝 Definição

### Definição formal

Um **Modelo de Linguagem Mascarado** (*Masked Language Model* — MLM) é uma classe de modelo de linguagem treinado para prever a identidade de um ou mais [[redes/ai-engineering/conceitos/tokenizacao.md|tokens]] arbitrariamente omitidos (*mascarados*) no interior de uma sequência, condicionando sua predição simultaneamente ao contexto precedente (à esquerda) e sucedente (à direita) da posição mascarada.

### Em linguagem simples

É um modelo de IA treinado como um jogo de "preencher as lacunas". O algoritmo pega uma frase, esconde algumas palavras no meio com uma etiqueta especial (como `[MASK]`) e obriga o modelo a adivinhar qual palavra foi escondida, usando como pista tanto o que vem antes quanto o que vem depois.

### Escopo e distinções

Distingue-se do [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|modelo de linguagem autoregressivo]], pois não gera texto sequencialmente da esquerda para a direita de forma fluida. É otimizado para gerar representações densas (*embeddings*) ricas de significado bidirecional para o texto de entrada. O exemplo clássico citado no texto é o BERT (Devlin et al., 2018).

## 🧩 Problema que resolve

Resolve a limitação dos modelos causais estritos em tarefas onde a compreensão do significado global de uma sentença depende criticamente do que vem adiante. Por exemplo, na frase "O banco onde sentei estava quebrado", entender o sentido da palavra "banco" depende do verbo "sentei", que ocorre depois. O MLM captura essa relação de forma direta.

## 💡 Intuição

Imagine fazer uma prova com questões de múltipla escolha com lacunas: "O animal que late e guarda a casa é o [____]". Você não precisa ler a frase apenas até o espaço em branco; você lê a oração inteira, analisa a palavra "casa" que vem no final e deduz com firmeza que a resposta é "cachorro".

## ⚙️ Como funciona

O ciclo de processamento do MLM envolve corrupção proposital e reconstrução:

### Etapas

1. **Amostragem de mascaramento:** Em um texto de treino, uma fração dos tokens (tipicamente 15%) é selecionada e substituída pelo token especial `[MASK]`.
2. **Passagem bidirecional:** A sequência completa (incluindo o `[MASK]`) passa pelas camadas do modelo (como blocos *encoder* do Transformer), onde a atenção bidirecional calcula a influência mútua entre todas as palavras.
3. **Predição no ponto da lacuna:** O vetor latente gerado na posição exata do token `[MASK]` é projetado sobre o vocabulário para produzir probabilidades.
4. **Cálculo de perda:** A função de perda penaliza o modelo caso ele não prediga o token original que foi omitido.

### Entradas e saídas

- **Entradas:** Sequência de texto corrompida contendo um ou mais marcadores de lacuna (ex.: `"O meu [MASK] é azul"`).
- **Saídas:** Distribuição de probabilidade sobre o vocabulário para preencher especificamente as posições mascaradas (ex.: probabilidade de `"carro"` ser a palavra ausente).

## 📐 Formulação matemática

O objetivo de otimização minimiza a perda de entropia cruzada apenas nas posições mascaradas $\mathcal{M}$:

$$\mathcal{L}_{\text{MLM}} = -\sum_{i \in \mathcal{M}} \log P(x_i \mid \tilde{X}; \theta)$$

Onde:

- $\tilde{X}$ é a sequência com tokens mascarados;
- $x_i$ é o token original verdadeiro na posição $i$;
- $\mathcal{M}$ é o subconjunto de índices dos tokens mascarados.

## 🧱 Hipóteses e condições de validade

- O acesso irrestrito ao contexto futuro e passado não constitui trapaça metodológica para a tarefa pretendida (portanto, válido para classificação, representação e depuração, mas não para geração causal de texto).

## ✅ Quando usar

- Tarefas não generativas de Processamento de Linguagem Natural: análise de sentimentos, classificação de texto, reconhecimento de entidades nomeadas (NER).
- Tarefas que exigem compreensão de código global, como detecção de bugs em um script, onde os erros dependem tanto do que foi importado no início quanto do que foi chamado no final.
- Criação de modelos de representação densa (*embeddings*) para alimentar sistemas de busca vetorial em [[redes/ai-engineering/conceitos/rag.md|RAG]].

- Tarefas não generativas de Processamento de Linguagem Natural: análise de sentimentos, classificação de texto, reconhecimento de entidades nomeadas (NER).
- Tarefas que exigem compreensão de código global, como detecção de bugs em um script, onde os erros dependem tanto do que foi importado no início quanto do que foi chamado no final.
- Criação de modelos de representação densa (*embeddings*) para alimentar sistemas de busca vetorial em [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]].

## 🚫 Quando não usar

- Aplicações de geração de texto aberto (chatbots, assistentes de redação, copilotos generativos de código), pois o MLM não foi estruturado para inferência sequencial expansiva.

## ⚠️ Limitações e armadilhas

- **Incompatibilidade gerativa:** Tentar usar um modelo puramente mascarado para gerar textos longos exige esquemas de decodificação complexos e ineficientes.
- **Discrepância pré-treino/inferência:** Durante a inferência do mundo real, o modelo não recebe textos com o token `[MASK]`, o que exige artifícios de treinamento para mitigar a lacuna de distribuição.

## 🔍 Comparações

| Aspecto | Modelo Mascarado (MLM) | Modelo Autoregressivo (ALM) |
|---|---|---|
| **Mecanismo de atenção** | Bidirecional completa | Causal (unidirecional) |
| **Ponto forte** | Compreensão semântica profunda | Geração fluida e aberta de texto |
| **Uso em IA moderna** | Classificadores leves e modelos de *embedding* | LLMs conversacionais e generativos |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um modelo de auditoria de software recebe o trecho:  `def calcular_desconto(preco): return preco * [MASK]` O modelo analisa o contexto anterior (`calcular_desconto`, `preco`) e o operador matemático `*` e estima com precisão que o token na lacuna deve ser uma variável ou constante numérica (como `fator` ou `0.1`), identificando rapidamente a estrutura de código esperada.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-linguagem.md|Modelo de Linguagem]]
- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]

### Complementos

- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]

### Alternativas

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/rag.md|Geração Aumentada de Recuperação (RAG)]]

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 4–5
- **Evidência:** O texto descreve o funcionamento do Masked Language Model, citando o BERT, e pontua seu uso contemporâneo em tarefas não-generativas, como análise de sentimento e depuração de código contextual.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é o mecanismo de predição característico de um modelo de linguagem mascarado?
2. Por que o modelo mascarado é classificado como tendo atenção bidirecional?
3. Em quais cenários práticos de engenharia de software um modelo MLM é mais vantajoso do que um modelo autorregressivo?
4. Como o BERT exemplifica a aplicação de auto-supervisão em modelos mascarados?
5. Qual é o motivo estrutural que impede o MLM de ser a arquitetura de escolha padrão para chatbots conversacionais?
6. De que forma o mascaramento bidirecional contribui para a geração de embeddings de alta qualidade semântica?
7. Qual é a perda estatística otimizada durante o treinamento de um MLM?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
