# 🧠 Busca Híbrida e Reciprocal Rank Fusion (RRF)

**Rede:** `ai-engineering`   **Área:** `recuperacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 266–267

## 📝 Definição

### Definição formal

A **Busca Híbrida** (*Hybrid Search*) é o padrão arquitetural de recuperação em sistemas de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]] que integra simultaneamente múltiplos algoritmos de busca complementares — convencionalmente um recuperador léxico esparso ([[redes/ai-engineering/conceitos/algoritmos-de-recuperacao-lexical-e-vetorial.md|BM25]]) e um recuperador semântico denso (vetores de embeddings) —, consolidando os candidatos recuperados através de um procedimento de reranqueamento sequencial ou por fusão paralela de listas ordenadas.

O **Reciprocal Rank Fusion** (*RRF*, Cormack et al., 2009) é um algoritmo de agregação de classificações independente de calibração métrica que combina múltiplos rankings de busca atribuindo uma pontuação inversamente proporcional à posição ordinal (*rank*) que cada documento ocupa em cada lista individual, somando essas frações amortecidas por uma constante de suavização para gerar um ordenamento final unificado.

### Em linguagem simples

É a técnica de consultar ao mesmo tempo o especialista em palavras exatas (BM25) e o especialista em ideias parecidas (busca vetorial), juntando as duas respostas em uma lista única perfeita. O algoritmo RRF resolve o problema de juntar os resultados sem se importar se uma nota era de 0 a 1 e a outra era de 1 a 100: ele olha apenas para a posição que o documento tirou em cada lista (1º lugar, 2º lugar, 5º lugar) e premia os documentos que ficaram bem colocados nas duas buscas.

### Escopo e distinções

Diferencia-se da busca vetorial pura e do BM25 isolado por atuar como um método de *ensemble*. O RRF distingue-se de métodos ingênuos de média ponderada porque não exige a normalização matemática de escalas de pontuação totalmente incompatíveis entre motores de busca distintos.

## 🧩 Problema que resolve

Resolve a incompatibilidade de escalas de pontuação na junção de sistemas de busca. Um motor BM25 devolve notas arbitrárias positivas desbalanceadas (ex.: pontuações entre 2.5 e 28.3), enquanto a similaridade de cosseno vetorial devolve pontuações entre -1 e 1. Tentar somar essas notas diretamente gera distorções matemáticas incontroláveis. O RRF descarta as notas brutas e utiliza estritamente as ordens de colocação relativas.

## 💡 Intuição

Pense em eleger o melhor restaurante da cidade combinando a votação de dois jurados muito diferentes:

- O **Jurado A** é rigoroso e dá notas de 1 a 5 com casas decimais.
- O **Jurado B** é exagerado e dá notas de 10 a 1.000 pontos.

Se você tentar somar as notas brutas dos dois, as notas gigantescas do Jurado B vão engolir as opiniões do Jurado A. Mas se você simplesmente olhar a lista de cada um e ver: *"Qual restaurante ficou em primeiro lugar na lista do Jurado A e também ficou entre os primeiros na lista do Jurado B?"*, você descobre o verdadeiro campeão com justiça absoluta (**mecanismo do RRF**).

## ⚙️ Como funciona

A busca híbrida com RRF opera em duas etapas concorrentes coordenadas por um agregador:

### Etapas

1. **Disparo Paralelo:** A consulta do usuário é disparada simultaneamente para dois motores de busca:
   - Motor 1 (BM25): busca por correspondência de palavras-chave exatas e termos raros;
   - Motor 2 (Vetorial): converte a query em embedding e faz a busca por similaridade angular no banco vetorial.
2. **Obtenção das Listas Individuais:** Cada motor retorna seus $K$ melhores documentos ordenados de $1$ a $K$.
3. **Cálculo da Pontuação RRF:** Para cada documento único presente em qualquer uma das duas listas, calcula-se sua fração recíproca com base na sua colocação ordinal em cada lista. Documentos que não aparecem em uma lista recebem pontuação zero correspondente àquela fonte.
4. **Soma e Reordenação Global:** As pontuações recíprocas são somadas; os documentos são reordenados em ordem decrescente desse escore consolidado.
5. **Corte e Injeção:** Os $k$ melhores documentos da lista unificada são passados para a montagem do contexto do modelo de fundação.

### Entradas e saídas

- **Entradas:** Consulta do usuário e acesso paralelo aos índices léxico e vetorial.
- **Saídas:** Lista única, balanceada e altamente resiliente de passagens documentais.

## 📐 Formulação matemática

Dada uma coleção de documentos $D$ e um conjunto de $n$ listas ranqueadas por sistemas de recuperação distintos, a pontuação RRF de um documento $D$ é calculada por:

$$\text{Score}_{\text{RRF}}(D) = \sum_{i=1}^n \frac{1}{k + r_i(D)}$$

Onde:

- $n$ é a quantidade de sistemas de busca integrados (tipicamente $n=2$: BM25 e Vetorial);
- $r_i(D)$ é a posição ordinal (1º, 2º, 3º...) que o documento $D$ alcançou no ranking do sistema $i$;
- $k$ é uma constante de suavização e amortecimento (convencionada na literatura e no artigo de Cormack et al. como $k = 60$).

Se o documento $D$ não estiver presente no ranking do sistema $i$, o termo correspondente é omitido da soma. O fator $k=60$ garante que a diferença entre o 1º e o 2º lugar não seja desproporcionalmente esmagadora em relação a documentos que aparecem com consistência em posições médias em ambos os buscadores.

## 🧱 Hipóteses e condições de validade

- Assume que ambos os motores de busca possuem qualidade individual mínima aceitável; somar um motor de busca altamente ruidoso ou quebrado apenas dilui os resultados do motor competente.
- Os identificadores de documentos devem ser consistentes e idênticos entre os dois índices para viabilizar a correspondência de IDs.

## ✅ Quando usar

- Padrão recomendado para quase todos os pipelines de RAG corporativos que operam sobre bases de dados heterogêneas de texto.
- Aplicações com vocabulário misto (onde usuários pesquisam tanto por conceitos amplos quanto por códigos de peças, nomes próprios ou termos de jargão técnico).

## 🚫 Quando não usar

- Em sistemas onde a latência de recuperação precisa ser estritamente inferior a 10 milissegundos e o custo de computação impede a manutenção de dois índices e duas buscas simultâneas.

## ⚠️ Limitações e armadilhas

- **Custo duplo de indexação e busca:** Manter um índice invertido (Elasticsearch) e um banco vetorial (HNSW) dobra o trabalho de sincronização contínua e a infraestrutura de dados da aplicação.
- **Ajuste estático de $k$:** Usar cegamente $k=60$ sem testar variações pode não ser ideal para conjuntos onde o número total de candidatos recuperados é muito pequeno (ex.: recuperar apenas top-3 de cada motor).

## 🔍 Comparações

| Estratégia de Busca | Resiliência a Sinônimos | Resiliência a Termos Raros | Sensibilidade a Calibração de Escores |
|---|---|---|---|
| **BM25 Puro** | Baixa | **Máxima** | Não se aplica |
| **Vetorial Puro** | **Máxima** | Moderada a Baixa | Não se aplica |
| **Média Ponderada Simples** | Alta | Alta | **Crítica (quebra se as escalas forem diferentes)** |
| **Busca Híbrida com RRF** | **Máxima** | **Máxima** | **Imune (usa apenas ordem de chegada)** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um documento sobre a política salarial da empresa está sendo buscado:

- O **BM25** analisa a consulta e coloca o documento na **1ª posição** ($r_1 = 1$).
- A **Busca Vetorial** coloca o mesmo documento na **3ª posição** ($r_2 = 3$).

Aplicando o RRF com a constante canônica $k=60$: $$\text{Score}_{\text{RRF}} = \frac{1}{60 + 1} + \frac{1}{60 + 3} = \frac{1}{61} + \frac{1}{63} \approx 0{,}01639 + 0{,}01587 = 0{,}03226$$ Outro documento apareceu em 1º lugar apenas no BM25, mas nem foi listado pelo motor vetorial: sua pontuação é de apenas $\frac{1}{61} \approx 0{,}01639$.
O documento que teve consenso entre os dois sistemas salta para o topo do ranking unificado com o dobro da pontuação.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/algoritmos-de-recuperacao-lexical-e-vetorial.md|Algoritmos de Recuperação: Lexical versus Vetorial]]

### Complementos

- [[redes/ai-engineering/conceitos/estrategias-de-chunking-e-otimizacao-de-rag.md|Estratégias de Chunking e Otimização de RAG]]

### Alternativas

- Fusão por Reranqueamento Sequencial com Cross-Encoders (onde o BM25 filtra os 100 melhores e um modelo neural pesado reordena o top-10).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/embeddings.md|Embeddings]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 266–267
- **Evidência:** Chip Huyen aborda a combinação de algoritmos de recuperação na busca híbrida e formaliza a equação do Reciprocal Rank Fusion (RRF) baseado em Cormack et al. (2009), explicando o papel da constante de amortecimento k=60 para estabilizar rankings de fontes heterogêneas.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Busca Híbrida e qual deficiência estrutural de sistemas de busca únicos ela foi desenhada para resolver?
2. Como funciona a formulação matemática do algoritmo Reciprocal Rank Fusion (RRF)?
3. Por que o RRF é considerado superior à média ponderada simples de notas na agregação de motores de busca distintos?
4. Qual é a função da constante de amortecimento $k=60$ na fórmula do RRF?
5. Como a combinação de rankings paralelos difere metodologicamente do reranqueamento sequencial com modelos de cross-encoder?
6. Quais são os custos adicionais de infraestrutura e engenharia ao se implantar uma arquitetura de busca híbrida?
7. Por que a busca híbrida é especialmente indicada para ambientes corporativos com vocabulário técnico e consultas de usuários leigos?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
