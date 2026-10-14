# 🧠 Algoritmos de Recuperação: Lexical versus Vetorial

**Rede:** `ai-engineering` 
**Área:** `recuperacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 257–266

## 📝 Definição

### Definição formal

Os **Algoritmos de Recuperação: Lexical versus Vetorial** representam os dois paradigmas matemáticos fundamentais utilizados pelo componente recuperador (*retriever*) em sistemas de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]] para ordenar e selecionar documentos relevantes frente a uma consulta:

1. **Recuperação Baseada em Termos (Lexical / Esparsa):** Modela documentos e consultas como vetores esparsos de alta dimensionalidade sobre o vocabulário, calculando a relevância através de frequências exatas de palavras e termos estatisticamente raros por meio de estruturas de **índice invertido** e formulações probabilísticas como o **BM25**;
2. **Recuperação Baseada em Embeddings (Vetorial / Densa):** Projeta documentos e consultas em vetores contínuos de dimensionalidade reduzida através de modelos neurais de [[redes/ai-engineering/conceitos/embeddings.md|embeddings]], mensurando a relevância conceitual através da proximidade geométrica (**Similaridade de Cosseno** ou produto interno) acelerada por algoritmos de busca de vizinhos aproximados (*Approximate Nearest Neighbors* — ANN).

### Em linguagem simples

É a escolha entre pesquisar por "palavras exatas" ou pesquisar por "significado". A busca lexical funciona como o Ctrl+F avançado: se você procurar o código de erro "EADDRNOTAVAIL", ela acha exatamente os documentos onde essa palavra estranha está escrita. A busca vetorial funciona como um leitor inteligente: se você procurar "como consertar meu carro que não liga", ela encontra textos sobre "problemas na bateria" ou "troca de motor de arranque", mesmo que as palavras do seu comando não estejam escritas no documento.

### Escopo e distinções

Não se limita à dicotomia simples de texto versus números. O BM25 é rápido, roda em CPU comum e é imbatível para termos raros; a busca vetorial exige GPUs para gerar embeddings, consome bancos de dados vetoriais dedicados e entende sinônimos e conceitos abstratos.

## 🧩 Problema que resolve

Resolve a miopia da recuperação da informação em sistemas cognitivos. Usar apenas busca léxica faz a aplicação falhar quando o usuário pesquisa usando termos diferentes dos usados pelo autor do documento; usar apenas busca vetorial faz a aplicação falhar ao pesquisar por nomes de pessoas, identificadores alfanuméricos e termos técnicos estritos que perdem especificidade quando convertidos em vetores densos.

## 💡 Intuição

Pense em procurar um livro em uma biblioteca pública imensa:

- A **Busca Lexical (BM25)** é o catálogo alfabético do bibliotecário: você procura exatamente pelo título "Memórias Póstumas de Brás Cubas". Se houver uma ficha com esse nome exato, você acha a estante em 5 segundos. Mas se você esquecer o nome e pedir "aquele livro do autor carioca onde o narrador já começa morto", o catálogo alfabético falha completamente.
- A **Busca Vetorial (Semântica)** é um bibliotecário culto que leu todos os livros: você explica o conceito com suas próprias palavras vagas e ele vai diretamente à estante de literatura brasileira do século XIX e puxa o livro correto para você.

## ⚙️ Como funciona

Os dois mecanismos possuem ciclos de indexação e consulta completamente divergentes:

### Etapas

1. **Pipeline Lexical (BM25):**
   - *Indexação:* O texto é tokenizado, pontuações são removidas e alimenta-se uma tabela hash que mapeia cada palavra às IDs dos documentos que a contêm (**índice invertido**).
   - *Consulta:* A query do usuário é decomposta em termos. O algoritmo calcula a frequência do termo no documento ponderada pelo inverso da frequência do termo em toda a base (TF-IDF), aplicando normalização pelo tamanho do documento.
2. **Pipeline Vetorial (Embeddings + ANN):**
   - *Indexação:* O documento é fatiado em pedaços (*chunks*), processado por um modelo de embedding e os vetores resultantes são salvos em estruturas de grafo ou agrupamento em um banco vetorial.
   - *Consulta:* A pergunta do usuário passa pelo mesmo modelo de embedding, virando um vetor de busca.
   - *Algoritmos de ANN (Approximate Nearest Neighbors):* Como o cálculo de distância contra milhões de vetores (*k-NN exato*) é lento demais, bancos vetoriais usam técnicas de aproximação:
     - **HNSW (Hierarchical Navigable Small World):** Constrói um grafo em múltiplas camadas onde vetores similares são conectados por arestas navegáveis em tempo logarítmico;
     - **IVF (Inverted File Index):** Agrupa vetores em clusters via K-means e busca apenas nos clusters mais próximos do centroide da query;
     - **Product Quantization (PQ):** Decompõe vetores em subvetores compactados, acelerando cálculos de distância na memória RAM.

### Entradas e saídas

- **Entradas:** Consulta do usuário em linguagem natural e corpus documental indexado.
- **Saídas:** Lista ordenada dos $k$ documentos com as maiores pontuações de relevância.

## 📐 Formulação matemática

O algoritmo **BM25** calcula a pontuação do documento $D$ para a query $Q$ composta pelos termos $q_1, \dots, q_m$:

$$\text{Score}_{\text{BM25}}(D, Q) = \sum_{i=1}^m \text{IDF}(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}$$

Onde:

- $f(q_i, D)$ é a frequência do termo $q_i$ no documento $D$;
- $|D|$ e $\text{avgdl}$ são o comprimento do documento e o comprimento médio de todos os documentos;
- $k_1$ e $b$ são hiperparâmetros de calibração (tipicamente $k_1 \in [1{,}2; 2{,}0]$ e $b \approx 0{,}75$).

Na **Busca Vetorial**, a pontuação é regida pelo produto escalar normalizado no espaço latente de dimensão $d$:

$$\text{Score}_{\text{vetorial}}(D, Q) = \cos(\mathbf{e}_Q, \mathbf{e}_D) = \frac{\mathbf{e}_Q \cdot \mathbf{e}_D}{\|\mathbf{e}_Q\|_2 \|\mathbf{e}_D\|_2}$$

## 🧱 Hipóteses e condições de validade

- No BM25, assume-se que palavras mais raras no acervo geral carregam maior peso informativo para desempate.
- Na busca vetorial, assume-se que o modelo de embedding utilizado foi treinado com pares semânticos compatíveis com a língua e com o domínio da consulta.

## ✅ Quando usar

- **BM25 / Lexical:** Pesquisa em bases de suporte técnico com códigos alfanuméricos de erro, consultas de artigos de leis com números de artigos expressos, bases de peças industriais e logs de servidores.
- **Vetorial / Embeddings:** Consultas em linguagem natural informal com sinônimos, suporte ao cliente receptivo, perguntas conceituais e sistemas de perguntas e respostas abertas.

## 🚫 Quando não usar

- Não use busca puramente vetorial se a sua aplicação depende criticamente de acertar números exatos de identificação de processos ou IDs de produtos de catálogo.
- Não use BM25 isolado se o vocabulário dos usuários for substancialmente leigo em relação à linguagem técnica usada pelos redatores dos manuais corporativos.

## ⚠️ Limitações e armadilhas

- **O custo oculto dos bancos vetoriais:** Indexar centenas de milhões de vetores densos de alta dimensão em estruturas HNSW exige gigabytes de memória RAM física permanente, tornando a infraestrutura vetorial ordens de magnitude mais cara que índices invertidos baseados em disco.
- **Sobrecarga de latência na geração de embedding:** A busca vetorial exige uma chamada de inferência à rede neural do embedding para a query antes de iniciar a busca, adicionando dezenas de milissegundos à latência da aplicação.

## 🔍 Comparações

| Dimensão | Recuperação Lexical (BM25) | Recuperação Vetorial (Embeddings) |
|---|---|---|
| **Estrutura de dados** | Índice invertido esparso | Grafos navegáveis (HNSW) ou agrupamentos (IVF) |
| **Infraestrutura primária** | CPU comum e disco rápido | RAM de alta velocidade e GPUs para embeddings |
| **Ponto forte** | Palavras raras, termos exatos, números, siglas | Sinônimos, conceitos abstratos, intenção ampla |
| **Ponto cego** | Incapaz de conectar sinônimos ("carro" vs "veículo") | Perde especificidade de termos técnicos raros |
| **Custo operacional** | Extremamente baixo | Moderado a Alto |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um engenheiro pesquisa em um sistema de RAG de telecomunicações o termo: `"Erro BGP 4-byte ASN incompatível"`.

- O motor de **Busca Vetorial** converte a frase em um vetor. O modelo de embedding dilui a sigla "BGP" e traz manuais gerais sobre roteamento e configurações comuns de redes empresariais.
- O motor **Lexical (BM25)** busca imediatamente no índice invertido os termos raros `"BGP"`, `"4-byte"` e `"ASN"`. Ele traz no topo do ranking a nota técnica exata do fabricante que documenta a falha de interoperabilidade no protocolo de roteamento exterior.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/embeddings.md|Embeddings]]

### Complementos

- [[redes/ai-engineering/conceitos/busca-hibrida-e-reciprocal-rank-fusion.md|Busca Híbrida e Reciprocal Rank Fusion (RRF)]]
- [[redes/ai-engineering/conceitos/estrategias-de-chunking-e-otimizacao-de-rag.md|Estratégias de Chunking e Otimização de RAG]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (representam os dois pilares básicos que compõem os motores modernos).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/similaridade-semantica.md|Similaridade Semântica]]
- [[redes/ai-engineering/conceitos/rag-multimodal-e-dados-tabulares.md|RAG Multimodal e Dados Tabulares (Text-to-SQL)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 257–266
- **Evidência:** Chip Huyen destrincha a matemática do TF-IDF e do BM25, compara o funcionamento de buscas esparsas e densas (citando o SPLADE), detalha os principais algoritmos de vizinhos aproximados (FAISS, HNSW, Annoy, IVF e Product Quantization) e formaliza as métricas de precisão de contexto e revocação de contexto em RAG.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a diferença metodológica e computacional entre recuperação baseada em termos e recuperação baseada em embeddings?
2. Como funciona a estrutura de dados de índice invertido utilizada por motores de busca clássicos como o Elasticsearch?
3. Como o algoritmo BM25 calcula e normaliza a pontuação de relevância em função do comprimento dos documentos?
4. Por que a busca vetorial densa exata via k-NN torna-se computacionalmente inviável em bases de dados massivas de milhões de documentos?
5. Quais são os princípios de funcionamento dos algoritmos de busca de vizinhos aproximados HNSW e IVF?
6. Por que consultas que envolvem códigos técnicos ou números de processo frequentemente falham quando executadas puramente sobre embeddings densos?
7. Quais são as métricas padrão da literatura para mensurar a qualidade técnica de um componente de recuperação em RAG?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

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

# 🧠 RAG Multimodal e Dados Tabulares (Text-to-SQL)

**Rede:** `ai-engineering`   **Área:** `recuperacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 273–275

## 📝 Definição

### Definição formal

O **RAG Multimodal e Dados Tabulares (Text-to-SQL)** compreende a extensão metodológica do padrão de geração aumentada de recuperação para suportar fontes heterogêneas não limitadas a documentos de texto contínuo:

1. **RAG Multimodal:** Arquitetura na qual imagens, gráficos ou áudios são recuperados a partir de metadados ou por meio de espaços latentes compartilhados ([[redes/ai-engineering/conceitos/embeddings.md|embeddings multimodais como o CLIP]]) e injetados no contexto de um modelo de fundação multimodal ([[redes/ai-engineering/conceitos/modelo-multimodal.md|LMM]]);
2. **RAG para Dados Tabulares (Text-to-SQL):** Arquitetura na qual perguntas analíticas em linguagem natural são traduzidas deterministicamente por um componente de análise semântica em consultas SQL estruturadas executadas sobre bancos relacionais, retornando dados tabulares exatos que são injetados no contexto da IA geradora.

### Em linguagem simples

É fazer o RAG funcionar com fotos, gráficos e tabelas de bancos de dados. Em vez de apenas ler textos em PDF, o sistema pode buscar imagens que ajudam a responder à pergunta do cliente (RAG Multimodal) ou pode olhar para o banco de dados da empresa, escrever uma consulta SQL sozinho, pegar os números reais de vendas daquela tabela e explicar o resultado em português claro (Text-to-SQL).

### Escopo e distinções

Distingue-se do RAG de texto tradicional pelo fluxo de processamento intermediário. No Text-to-SQL, o sistema não faz busca vetorial aproximada sobre o conteúdo dos registros; ele consulta esquemas (*schemas*) de tabelas, sintetiza código SQL executável e processa o retorno tabular determinístico.

## 🧩 Problema que resolve

Resolve a incapacidade de LLMs realizarem operações quantitativas exatas e atualizadas sobre grandes bancos de dados corporativos. Se uma empresa tentar colocar 1 milhão de linhas de uma tabela de faturamento em texto puro dentro de um prompt ou banco vetorial, a IA errará contas básicas de soma e média. O Text-to-SQL transfere o cálculo aritmético pesado para o motor do banco de dados (Postgres, Snowflake) e usa a IA apenas para entender a pergunta e explicar a resposta.

## 💡 Intuição

Pense em um diretor executivo pedindo um relatório ao seu analista de inteligência de negócios:

- O diretor pergunta em voz alta: `"Quantas unidades do chapéu fedora vendemos na última semana e qual foi a receita total?"`.
- O analista humano (**o motor Text-to-SQL**) não abre os olhos e fica chutando números de cabeça. Ele abre o computador, escreve um comando formal em SQL `SELECT SUM(unidades), SUM(total) FROM Vendas...`, aperta Enter no terminal e olha o resultado exato na tela.
- Em seguida, ele se vira para o diretor e responde em linguagem natural elegante (**a geração final**): `"Vendemos 1.450 unidades, gerando R$ 85.000,00 de faturamento"`.

## ⚙️ Como funciona

O fluxo tabular exige uma esteira de três etapas estritas:

### Etapas

1. **Tradução Semântica (*Text-to-SQL*):**
   - O sistema recebe a pergunta do usuário e os esquemas das tabelas relevantes (nomes de colunas, chaves primárias e tipos de dados).
   - O modelo traduz a pergunta em uma consulta SQL sintaticamente válida para o dialeto do banco de dados alvo (PostgreSQL, MySQL, BigQuery).
2. **Execução Determinística do SQL:**
   - A consulta gerada é despachada para o motor de banco de dados corporativo através de um executor de ferramentas.
   - O banco de dados processa os filtros, somas e agrupamentos, retornando um conjunto tabular enxuto de resultados estruturados.
3. **Geração Fundamentada:**
   - Os números e registros exatos devolvidos pela consulta SQL são inseridos no prompt do LLM juntamente com a pergunta original.
   - O modelo sintetiza uma resposta explicativa em linguagem natural respaldada pelos dados reais computados.

### Entradas e saídas

- **Entradas:** Pergunta analítica em linguagem natural e conexão de leitura ao banco relacional.
- **Saídas:** Consulta SQL gerada, tabela de dados intermediária e resposta textual final interpretada para o usuário.

## 📐 Formulação matemática

O pipeline decompõe a probabilidade da resposta final $Y$ em duas etapas condicionais sequenciais governadas pela consulta gerada $Q_{\text{SQL}}$ e pelo conjunto de dados resultante $\mathcal{T} = \text{Executa}(Q_{\text{SQL}})$:

$$P(Y \mid X) = P(Q_{\text{SQL}} \mid X, \mathcal{S}_{\text{banco}}) \cdot P(Y \mid X, \mathcal{T})$$

Onde:

- $\mathcal{S}_{\text{banco}}$ representa as definições formais de DDL (*Data Definition Language*) das tabelas do banco de dados;
- $P(Q_{\text{SQL}} \mid X, \mathcal{S}_{\text{banco}})$ é a probabilidade do modelo gerar a consulta formal correta;
- Se houver milhares de tabelas na empresa, utiliza-se um pré-recuperador vetorial para selecionar apenas as $m$ tabelas cujos esquemas sejam semanticamente correlacionados à consulta $X$ antes de acionar a etapa de Text-to-SQL.

## 🧱 Hipóteses e condições de validade

- O banco de dados relacional deve possuir integridade referencial, nomes de colunas semânticos ou dicionários de dados descritivos (*metadados*) que permitam ao modelo inferir o significado de cada coluna.
- Acesso restrito a permissões estritas de leitura (`SELECT`) para impedir acidentalmente ou maliciosamente a execução de comandos destrutivos (`DELETE`, `DROP`).

## ✅ Quando usar

- Dashboards corporativos de BI (Business Intelligence) orientados por conversação natural.
- Consultas financeiras, auditorias de estoque e rastreamento de pedidos em sistemas de e-commerce e ERPs.
- RAG Multimodal: suporte técnico onde o usuário envia fotos de manuais com esquemas elétricos ou diagramas mecânicos.

## 🚫 Quando não usar

- Em dados puramente desestruturados (como cartas abertas ou ensaios literários) onde não existem colunas nem bancos de dados relacionais para consultar.

## ⚠️ Limitações e armadilhas

- **Ambiguidade de esquemas:** Nomes de colunas enigmáticos herdados de sistemas legados (ex.: colunas nomeadas como `VLR_TOT_01_A`) confundem o modelo e induzem a geração de SQLs com cálculos errados.
- **Riscos de segurança e SQL Injection via IA:** Injeções de prompt indiretas contidas em campos de texto do banco de dados podem tentar manipular o gerador de SQL para expor tabelas confidenciais de credenciais.

## 🔍 Comparações

| Modalidade | Fonte de Informação | Motor de Busca | Tolerância a Erros Aritméticos |
|---|---|---|---|
| **RAG Textual Clássico** | PDFs, artigos, transcrições | Banco Vetorial / BM25 | Baixa (LLMs erram contas no texto) |
| **RAG com Text-to-SQL** | Bancos relacionais (SQL) | Interpretador SQL nativo | **Zero (o banco faz a conta exata)** |
| **RAG Multimodal** | Imagens, fotos e gráficos | Espaço compartilhado CLIP | Média (depende da visão computacional) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O caso do e-commerce fictício de gatos **Kitty Vogue** apresentado no capítulo: O gerente comercial pergunta: `"Quantas unidades do chapéu Fruity Fedora foram vendidas nos últimos 7 dias?"`.

1. O componente de **Text-to-SQL** lê o esquema da tabela `Vendas(order_id, timestamp, product_name, units, total)` e emite a query:

   ```sql
   SELECT SUM(units) AS total_vendido 
   FROM Vendas 
   WHERE product_name = 'Fruity Fedora' 
   AND timestamp >= DATE_SUB(CURDATE(), INTERVAL 7 DAY);
   ```

2. O banco relacional executa a query e devolve o valor exato: `total_vendido = 412`.
3. O modelo de fundação recebe o número 412 e responde em português claro ao gerente: `"Nos últimos 7 dias, foram vendidas 412 unidades do chapéu Fruity Fedora"`.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/modelo-multimodal.md|Modelo Multimodal]]

### Complementos

- [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|Agentes de IA e Inventário de Ferramentas]]
- [[redes/ai-engineering/conceitos/estrategias-de-chunking-e-otimizacao-de-rag.md|Estratégias de Chunking e Otimização de RAG]]

### Alternativas

- Despejo bruto de arquivos CSV ou tabelas em formato Markdown dentro do prompt de texto comum.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/planejamento-e-chamada-de-funcoes.md|Planejamento e Chamada de Funções (Function Calling)]]
- [[redes/ai-engineering/conceitos/embeddings.md|Embeddings]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 273–275
- **Evidência:** Chip Huyen aborda a expansão de RAG além de textos, detalhando a indexação visual multimodal através de representações conjuntas do CLIP e formalizando o pipeline de Text-to-SQL sobre bancos relacionais com o exemplo prático da loja Kitty Vogue e seu chapéu Fruity Fedora.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é RAG Multimodal e como modelos como o CLIP viabilizam a recuperação de imagens sem metadados manuais?
2. Por que o Text-to-SQL é considerado a abordagem correta para implementar RAG sobre bases de dados tabulares relacionais?
3. Quais são as três etapas sequenciais que compõem o pipeline de RAG para dados estruturados?
4. Por que inserir tabelas inteiras de banco de dados diretamente no prompt em formato de texto é uma prática ineficiente de engenharia?
5. Como sistemas corporativos lidam com bancos de dados complexos que possuem milhares de tabelas antes de acionar a etapa de Text-to-SQL?
6. Quais salvaguardas de segurança de infraestrutura devem ser implementadas no executor de banco de dados conectado à IA?
7. Qual é o papel dos metadados e da documentação de dicionário de dados na taxa de acerto de modelos geradores de SQL?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Agentes de IA e Inventário de Ferramentas

**Rede:** `ai-engineering`   **Área:** `agentes`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 275–281

## 📝 Definição

### Definição formal

Um **Agente de IA** (*AI Agent*) é um sistema computacional autônomo fundamentado em um ou mais [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]] atuando como núcleo de raciocínio (*planner*), caracterizado formalmente pela capacidade de perceber o estado de seu **ambiente operacional** através de sensores ou fluxos de dados, deliberar sobre objetivos e executar intervenções sobre esse mesmo ambiente através de um **Inventário de Ferramentas** (*Tool Inventory*). 

As ferramentas organizam-se em três categorias funcionais canônicas:

1. **Aumento de Conhecimento:** Mecanismos de leitura para percepção e recuperação contextual ([[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]], navegação web, APIs de notícias);
2. **Extensão de Capacidades:** Ferramentas que superam limitações intrínsecas da rede neural (calculadoras aritméticas, interpretadores de código Python, conversores de fuso horário, renderizadores gráficos);
3. **Ações de Escrita:** Comandos autorizados que alteram fisicamente o estado do ambiente externo (gravar registros em bancos relacionais, enviar e-mails, acionar transações financeiras).

### Em linguagem simples

Um agente é uma IA que deixou de ser apenas um "gerador de texto" e ganhou "mãos e pés" para executar tarefas no mundo digital. O modelo de linguagem é o cérebro; as ferramentas são os braços (calculadora, navegador de internet, terminal de programação). Em vez de apenas responder à sua pergunta, o agente planeja os passos, usa os programas necessários no computador e entrega a tarefa completamente resolvida para você.

### Escopo e distinções

Diferencia-se do padrão RAG tradicional. O RAG é estático e unidirecional (busca dados e gera resposta). O agente é dinâmico, iterativo e dotado de agência: ele decide ativamente se precisa usar uma ferramenta, se o resultado recebido foi satisfatório e quando a tarefa deve ser encerrada.

## 🧩 Problema que resolve

Supera a paralisia operacional e as fraquezas aritméticas e de atualidade dos LLMs puros. Um modelo isolado não sabe a data de hoje, não consegue fazer contas de divisão longas com garantia de exatidão e não tem poder para alterar nada no mundo real. O acoplamento a ferramentas permite que o modelo terceirize cálculos exatos para compiladores e interaja diretamente com APIs corporativas.

## 💡 Intuição

Pense em um analista de compras de uma empresa:

- Se ele estiver trancado em uma sala sem telefone, sem internet e sem computador (**LLM puro**), tudo o que ele pode fazer é escrever textos com base no que ele lembra de cabeça.
- Se você entregar a ele um computador com acesso ao sistema ERP, uma calculadora financeira e um navegador de internet (**o agente com seu inventário de ferramentas**), ele agora consegue cotar preços de fornecedores online, calcular os impostos sem errar um único centavo e emitir a ordem de compra formal no sistema da empresa.

## ⚙️ Como funciona

O ciclo de vida do agente articula-se em torno de uma esteira recorrente de percepção e ação:

### Etapas

1. **Recepção da Meta:** O usuário especifica o objetivo de alto nível e suas restrições (ex.: `"Agende uma reunião com o cliente X para a próxima terça à tarde"`).
2. **Avaliação do Inventário:** O modelo consulta a lista de ferramentas disponíveis declaradas em sua configuração.
3. **Decisão de Ação:** O modelo determina se a tarefa exige o uso de uma ferramenta externa ou se pode ser respondida diretamente com conhecimento interno.
4. **Disparo da Ferramenta:** O modelo emite uma solicitação estruturada de chamada de função contendo os argumentos calculados.
5. **Execução e Retorno:** O software da aplicação executa a ferramenta de verdade e injeta o resultado de volta no contexto do modelo como uma observação.
6. **Avaliação de Sucesso:** O modelo avalia se a meta foi atingida ou se precisa disparar uma nova ferramenta.

### Entradas e saídas

- **Entradas:** Metas do usuário em linguagem natural e documentação estruturada de APIs e ferramentas.
- **Saídas:** Efeitos colaterais executados no ambiente externo e relatórios finais de conclusão da tarefa.

## 📐 Formulação matemática

O grande desafio matemático e operacional que restringe a autonomia dos agentes é o fenômeno dos **Erros Compostos (*Compound Mistakes*)**. 
Seja um agente executando um plano composto por $T$ etapas consecutivas e interdependentes, onde a probabilidade de o modelo tomar a decisão correta em cada etapa individual é $p \in (0, 1)$. A probabilidade de sucesso global do fluxo decai exponencialmente:

$$\text{Acurácia}_{\text{global}} = p^T$$

Para um modelo de altíssima capacidade com $p = 0{,}95$ ($95\%$ de acerto por passo individual):

- Em um plano curto de 5 passos: $\text{Acurácia} = 0{,}95^5 \approx 0{,}774 \;\; (77{,}4\%)$;
- Em um plano médio de 10 passos: $\text{Acurácia} = 0{,}95^{10} \approx 0{,}599 \;\; (59{,}9\%)$;
- Em um fluxo longo de 100 passos: $\text{Acurácia} = 0{,}95^{100} \approx 0{,}0059 \;\; (0{,}59\%)$.

Isso demonstra que em agentes autônomos de longa duração, mesmo modelos quase perfeitos colapsam para taxas de acerto próximas de zero sem mecanismos estritos de [[redes/ai-engineering/conceitos/reflexao-e-correcao-de-erros-em-agentes.md|reflexão e correção de erros]].

## 🧱 Hipóteses e condições de validade

- Exige modelos de fundação com avançada capacidade de raciocínio e aderência estrita a formatos sintáticos (o capítulo enfatiza que agentes demandam os modelos mais poderosos e caros do mercado devido à gravidade dos erros compostos).
- As ferramentas declaradas devem possuir esquemas de tipos rigorosamente documentados e documentações de parâmetros inequívocas.

## ✅ Quando usar

- Automação de fluxos de trabalho corporativos de múltiplos passos (onboarding de funcionários, extração e conciliação de faturas, geração e depuração contínua de código).
- Assistentes de pesquisa analítica profunda que exigem múltiplos acessos à web combinados com análise de dados tabulares.

## 🚫 Quando não usar

- Em tarefas simples que exigem respostas de texto imediatas com latência mínima de menos de 1 segundo (onde o overhead de planejamento e execução de ferramentas torna o sistema lento demais).
- Processos de missão crítica financeira que não tolerem supervisão humana mandatória ([[redes/ai-engineering/conceitos/humano-no-loop.md|Humano no Loop]]).

## ⚠️ Limitações e armadilhas

- **Risco de Ações Destrutivas Irreversíveis:** Dar permissão irrestrita para uma ferramenta de escrita executar ordens como `DELETE` em bancos de produção ou enviar e-mails públicos para clientes sem confirmação prévia humana.
- **Loops Infinitos de Ferramentas:** O agente entrar em um ciclo vicioso disparando a mesma ferramenta repetidamente ao receber uma mensagem de erro inesperada, esgotando o orçamento de API em poucos minutos.

## 🔍 Comparações

| Dimensão | Chatbot Tradicional / RAG Puro | Agente de IA com Ferramentas |
|---|---|---|
| **Fluxo de execução** | Linear e estático (Entrada $\to$ Saída) | Cíclico e iterativo (Pensa $\to$ Age $\to$ Avalia) |
| **Poder de ação** | Passivo (apenas gera texto) | Ativo (executa código, altera bancos de dados) |
| **Sensibilidade a erros** | Baixa (um erro afeta apenas uma frase) | Crítica (erros compostos inviabilizam o plano) |
| **Exigência de modelo** | Modelos médios funcionam bem | Exige modelos de elite na fronteira de raciocínio |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um agente de suporte de TI recebe o comando: `"O usuário Marcos esqueceu a senha da VPN. Redefina a senha e avise-o por SMS"`.

1. **Passo 1 (Conhecimento):** O agente usa a ferramenta `busca_usuario(nome="Marcos")` para descobrir o ID e o telefone do usuário.
2. **Passo 2 (Ação de Escrita Crítica):** O agente gera a chamada `redefinir_senha_vpn(user_id=8492)`. O sistema de segurança intercepta a chamada e exige confirmação de token de segurança.
3. **Passo 3 (Extensão de Capacidade):** O agente aciona a ferramenta de envio de mensagens `enviar_sms(telefone="+5511999999999", texto="Sua nova senha temporária é X")`.
4. **Conclusão:** O agente reporta ao administrador que o fluxo foi concluído com sucesso em 3 passos coordenados.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]

### Complementos

- [[redes/ai-engineering/conceitos/planejamento-e-chamada-de-funcoes.md|Planejamento e Chamada de Funções (Function Calling)]]
- [[redes/ai-engineering/conceitos/reflexao-e-correcao-de-erros-em-agentes.md|Reflexão e Correção de Erros em Agentes (ReAct e Reflexion)]]
- [[redes/ai-engineering/conceitos/avaliacao-e-modos-de-falha-de-agentes.md|Avaliação e Modos de Falha de Agentes]]

### Alternativas

- Scripts estáticos determinísticos com chamadas de API fixas em código tradicional sem raciocínio estocástico de IA.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/sistemas-de-memoria-para-ia.md|Sistemas de Memória para IA]]
- [[redes/ai-engineering/conceitos/humano-no-loop.md|Humano no Loop (Crawl-Walk-Run)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 275–281
- **Evidência:** Chip Huyen formaliza a definição clássica de agente a partir de Russell & Norvig (1995), estabelece a taxonomia das três categorias de ferramentas, apresenta os ganhos empíricos do agente Chameleon (Lu et al., 2023) e analisa o desafio matemático dos erros compostos sobre trajetórias de execução longa.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a definição canônica de um Agente de IA e quais componentes estruturam sua relação com o ambiente?
2. Quais são as três classes funcionais de ferramentas disponíveis no inventário de um agente inteligente?
3. O que é o fenômeno dos erros compostos (*compound mistakes*) e por que ele impõe limites severos a fluxos de muitos passos?
4. Por que a construção de agentes autônomos exige modelos de fundação na fronteira máxima de capacidade de raciocínio?
5. Qual é o perigo de segurança associado à concessão de ações de escrita a agentes e como o conceito de Humano no Loop atua como barreira?
6. Como o estudo experimental do Chameleon demonstrou que o acoplamento a ferramentas supera o uso de modelos isolados?
7. Qual é a distinção fundamental de dinamismo e controle entre o padrão RAG puro e um Agente autônomo?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Planejamento e Chamada de Funções (Function Calling)

**Rede:** `ai-engineering`   **Área:** `agentes`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 281–292

## 📝 Definição

### Definição formal

O **Planejamento e Chamada de Funções** (*Planning and Function Calling*) compreende a mecânica algorítmica e a interface estruturada pelas quais um [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|agente de IA]] decompõe um objetivo abstrato em uma trajetória viável de passos de computação e invoca programas de software externos:

- **Planejamento (*Planning*):** A capacidade do modelo de formular roteiros operacionais (*trajectories*) que delimitam a sequência de estados, decisões e ações exigidas para atingir a meta sob restrições de tempo e recursos;
- **Chamada de Funções (*Function Calling*):** A habilidade nativa da rede neural de emitir saídas estritamente estruturadas (em JSON) contendo o identificador canônico de uma função e os argumentos nominais extraídos ou deduzidos do contexto, permitindo que a aplicação hospedeira execute o código determinístico correspondente.

### Em linguagem simples

Planejar é quando a IA monta um plano de ação na cabeça antes de sair fazendo besteira. A Chamada de Funções (*Function Calling*) é a maneira padronizada que a IA tem de "apertar os botões" dos outros sistemas: em vez de apenas falar frases bonitas, ela cospe um bloquinho de código formatado dizendo com precisão: *"Chame a função `consultar_clima` para a cidade de `São Paulo`"*.

### Escopo e distinções

O modelo de linguagem **não executa a função diretamente em seu silício**. O modelo apenas gera o texto estruturado que expressa a intenção de execução; é o código da aplicação de software em volta que intercepta esse texto, executa a função no mundo real e devolve a resposta para o modelo continuar pensando.

## 🧩 Problema que resolve

Resolve a barreira de comunicação entre a linguagem natural ambígua e os sistemas de software determinísticos. Sem *function calling*, desenvolvedores precisavam usar expressões regulares frágeis para tentar descobrir se a IA estava pedindo para rodar um comando; com o suporte nativo calibrado no pós-treinamento, o modelo emite chamadas perfeitas garantidas por gramáticas de decodificação.

## 💡 Intuição

Pense em um executivo estrangeiro que não fala português contratando uma secretária executiva no Brasil:

- O executivo (**o modelo de fundação**) dita em inglês uma ordem de alto nível: `"Quero me hospedar perto da praia no Rio amanhã"`.
- A secretária entende a intenção e redige uma ordem de serviço técnica no sistema corporativo (**Function Calling**): `reserva_hotel(cidade="Rio de Janeiro", regiao="Copacabana", data="2026-09-18")`.
- O sistema de reservas do hotel processa a ordem de serviço e devolve o voucher confirmado.

## ⚙️ Como funciona

O planejamento moderno exige desacoplar formalmente o plano da sua execução real:

### Etapas

1. **Declaração do Inventário de Funções:** A aplicação envia para a API do modelo uma lista contendo as assinaturas em JSON Schema de todas as ferramentas disponíveis (nome, descrição e tipos de parâmetros).
2. **Geração do Plano de Ação:** O modelo avalia o comando do usuário e gera uma decomposição de ações, que pode seguir diferentes **fluxos de controle**:
   - *Sequencial:* Passo B depende estritamente do término do Passo A;
   - *Paralelo:* Múltiplas ferramentas independentes são acionadas ao mesmo tempo;
   - *Ramificação Condicional (IF/ELSE):* Ação seguinte depende do resultado retornado pela anterior;
   - *Loop (WHILE/FOR):* Repetição de varredura até que uma condição de parada seja satisfeita.
3. **Validação do Plano:** O software valida o plano gerado contra heurísticas e diretrizes de segurança antes de disparar ferramentas perigosas.
4. **Emissão da Chamada (*Tool Call*):** O modelo produz a saída estruturada com `name: "nome_funcao"` e `arguments: "{...}"`.
5. **Execução no Host:** A aplicação executa a função localmente (ex.: consulta um banco SQL ou chama uma API externa).
6. **Injeção da Observação:** O retorno da ferramenta é encapsulado sob a tag de papel de ferramenta (`role: "tool"`) e realimentado no contexto do modelo para orientar o próximo passo.

### Entradas e saídas

- **Entradas:** Descrições de esquemas de ferramentas e solicitação contextual do usuário.
- **Saídas:** Objetos de chamada de função (`tool_calls`) prontos para execução no runtime da aplicação.

## 📐 Formulação matemática

O processo de planejamento atua como um problema de busca em árvore sobre um grafo de estados $\mathcal{S}$ e ações $\mathcal{A}$. 
Dado o estado atual $s_t$, a política do modelo de fundação parametriza a distribuição sobre a próxima ação estruturada $a_t \in \mathcal{A}$ e seus argumentos $\theta_{\text{args}}$:

$$P(a_t, \theta_{\text{args}} \mid s_t; \Theta_{\text{modelo}}) = P(a_t \mid s_t) \cdot P(\theta_{\text{args}} \mid s_t, a_t)$$

Nas APIs de ponta, o desenvolvedor pode configurar o hiperparâmetro de controle de ferramentas $\text{tool\_choice}$:

- $\text{tool\_choice} = \text{"none"}$: Força $P(a_t = \text{texto}) = 1$;
- $\text{tool\_choice} = \text{"required"}$: Força $P(a_t \in \mathcal{A}_{\text{ferramentas}}) = 1$;
- $\text{tool\_choice} = \text{"auto"}$: O modelo calibra dinamicamente a necessidade da ferramenta.

## 🧱 Hipóteses e condições de validade

- A inferência pressupõe modelos que passaram por pós-treinamento específico com amostras sintéticas de function calling para evitar alucinações de argumentos ou chamadas de funções inexistentes.

## ✅ Quando usar

- Integração de modelos com bancos de dados relacionais e APIs de serviços web corporativos.
- Automação de pipelines onde a resposta da IA deve alimentar diretamente variáveis em outros programas de software sem necessidade de parsing manual por regex.

## 🚫 Quando não usar

- Consultas onde toda a informação exigida já consta com clareza dentro do contexto do prompt original, onde disparar chamadas de função vazias gera latência e custos inúteis.

## ⚠️ Limitações e armadilhas

- **Alucinação de parâmetros:** O modelo pode acertar o nome da função perfeitamente, mas inventar um valor fictício para um parâmetro obrigatório caso o dado não tenha sido fornecido pelo usuário.
- **Sobrecarga de contexto por esquemas:** Declarar dezenas ou centenas de ferramentas na API consome milhares de tokens de entrada antes mesmo de o usuário digitar sua pergunta, encarecendo a fatura e aproximando o modelo do efeito *lost-in-the-middle*.

## 🔍 Comparações

| Abordagem de Controle | Como opera? | Robustez a Falhas | Flexibilidade |
|---|---|---|---|
| **Plano em Texto Livre** | O modelo escreve o que vai fazer em parágrafos | Baixa (difícil de automatizar por código) | Alta |
| **Function Calling Nativo** | Emissão de objetos JSON validados por gramática | **Altíssima (garante conformidade sintática)** | Estruturada |
| **Plano em Linguagem Natural com Tradutor** | Modelo planeja em texto; um submodelo traduz para código | Alta (robusto a mudanças de nomes de APIs) | Máxima |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um usuário pergunta: `"Quantos quilos pesam 40 libras?"`.
A aplicação declarou previamente a ferramenta `lbs_to_kg(lbs: float)`.
O modelo de fundação analisa a pergunta e, em vez de responder com texto, devolve a chamada estruturada:

```json
{
  "tool_calls": [
    {
      "name": "lbs_to_kg",
      "arguments": "{\"lbs\": 40.0}"
    }
  ]
}
```

A aplicação intercepta a mensagem, roda a função matemática simples em Python `40.0 * 0.453592 = 18.1437`, e envia de volta para o modelo: `{"role": "tool", "content": "18.14 kg"}`. O modelo lê o dado e finaliza para o usuário: `"40 libras equivalem a aproximadamente 18,14 quilos"`.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|Agentes de IA e Inventário de Ferramentas]]
- [[redes/ai-engineering/conceitos/amostragem-restrita-e-saidas-estruturadas.md|Amostragem Restrita e Saídas Estruturadas]]

### Complementos

- [[redes/ai-engineering/conceitos/reflexao-e-correcao-de-erros-em-agentes.md|Reflexão e Correção de Erros em Agentes (ReAct e Reflexion)]]
- [[redes/ai-engineering/conceitos/avaliacao-e-modos-de-falha-de-agentes.md|Avaliação e Modos de Falha de Agentes]]

### Alternativas

- Parsing manual de texto livre através de expressões regulares complexas.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/rag-multimodal-e-dados-tabulares.md|RAG Multimodal e Dados Tabulares (Text-to-SQL)]]
- [[redes/ai-engineering/conceitos/sistemas-de-memoria-para-ia.md|Sistemas de Memória para IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 281–292
- **Evidência:** Chip Huyen discute o debate sobre se LLMs autorregressivos conseguem planejar (citando as críticas de Yann LeCun e Kambhampati), detalha a implementação de pseudocódigo de Function Calling nas APIs modernas, analisa a granularidade de planos e formaliza os quatro fluxos de controle complexos (sequencial, paralelo, branching e loops).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Function Calling e por que ele não significa que a rede neural executa o código internamente?
2. Por que o desacoplamento formal entre a geração do plano e sua execução física é indispensável para a segurança de agentes?
3. Quais são os quatro fluxos de controle fundamentais que podem estruturar a trajetória de execução de um agente?
4. Como o debate entre Yann LeCun e pesquisadores de LLMs caracteriza as limitações de planejamento de modelos autorregressivos puros?
5. Qual é o perigo de declarar centenas de ferramentas simultâneas no esquema de uma API de modelo de fundação?
6. Como funciona a abordagem de planejamento em dois níveis (plano em linguagem natural seguido por um modelo tradutor de chamadas)?
7. O que acontece quando o modelo de fundação emite uma chamada de função com parâmetros obrigatórios alucinados?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Reflexão e Correção de Erros em Agentes (ReAct e Reflexion)

**Rede:** `ai-engineering`   **Área:** `agentes`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 292–294

## 📝 Definição

### Definição formal

A **Reflexão e Correção de Erros em Agentes** (*Reflection and Error Correction*) é o paradigma arquitetural no qual um [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|agente de IA]] intercala a execução de ações com etapas introspectivas de avaliação crítica e auto-exame, diagnosticando desvios e atualizando autonomamente seu plano de ação a partir do feedback do ambiente. 

Estrutura-se em dois frameworks canônicos fundamentais:

1. **ReAct (Reason + Act, Yao et al., 2022):** Intercala passos explícitos de raciocínio verbalizado (**Pensamento / *Thought***), execução de ferramentas (**Ação / *Act***) e recepção de resultados do ambiente (**Observação / *Observation***) em uma única trajetória contínua;
2. **Reflexion (Shinn et al., 2023):** Arquitetura multi-modular que adiciona um módulo avaliador e um módulo de auto-reflexão verbal; após o fracasso de uma trajetória completa, o agente formula um diagnóstico textual sobre o motivo do erro e utiliza essa reflexão como contexto adicional para tentar novamente com uma nova estratégia.

### Em linguagem simples

É a capacidade da IA de "parar, respirar, pensar no que acabou de acontecer e corrigir o próprio erro". Em vez de agir no piloto automático disparando ferramentas sem parar, o modelo que usa ReAct escreve o que está pensando antes de tomar uma ação e lê o resultado antes de dar o próximo passo. Se o plano der errado, o Reflexion faz a IA se perguntar: *"Por que eu errei essa conta?"*, anotando a lição aprendida em sua memória para não cometer a mesma falha na tentativa seguinte.

### Escopo e distinções

Não se confunde com o simples [[redes/ai-engineering/conceitos/cadeia-de-pensamento.md|Chain-of-Thought (CoT)]]. O CoT é estático e fechado no raciocínio textual puro. O ReAct e o Reflexion são dinâmicos e abertos ao mundo exterior: as reflexões são condicionadas a observações empíricas concretas devolvidas por ferramentas e interpretadores externos.

## 🧩 Problema que resolve

Resolve a rigidez e a fragilidade catastrófica de agentes autônomos. Sem reflexão, se uma ferramenta retornar um erro de rede ou parâmetros incorretos, o agente tradicional quebra ou continua insistindo na mesma chamada falha indefinidamente. A reflexão confere resiliência e adaptação dinâmica perante a incerteza do ambiente.

## 💡 Intuição

Pense em um programador depurando um erro em um software:

- Um robô sem reflexão tenta compilar o código. Dá erro. Ele tenta compilar o mesmo código de novo. Dá o mesmo erro. Ele repete até travar.
- O programador que usa **ReAct e Reflexion** lê a mensagem de erro do terminal (**Observação**), pensa: *"O erro diz 'módulo não encontrado', o que significa que esqueci de rodar o pip install"* (**Pensamento/Reflexão**), digita o comando de instalação no terminal (**Ação**) e resolve o problema na segunda tentativa.

## ⚙️ Como funciona

O ciclo operacional dos dois frameworks estrutura-se de maneira coordenada:

### Etapas

1. **Ciclo ReAct (Dentro do Turno):**
   - **Thought (Pensamento):** O modelo analisa o estado atual e escreve seu raciocínio: `"Preciso encontrar o ano de nascimento do autor X antes de calcular sua idade atual."`
   - **Act (Ação):** O modelo emite o comando da ferramenta: `busca_web(query="ano de nascimento autor X")`.
   - **Observation (Observação):** O sistema executa a busca e injeta o retorno no contexto: `"O autor X nasceu em 1942."`
   - O loop repete-se ciclicamente até que o pensamento determine que o objetivo foi atingido, emitindo `Finish [Resposta]`.
2. **Ciclo Reflexion (Entre Trajetórias):**
   - O agente executa um plano completo (por exemplo, escreve uma função de software).
   - Um **Avaliador** roda os testes unitários e constata que 2 de 10 testes falharam.
   - O módulo de **Auto-Reflexão** analisa o código e os testes reprovados e gera um diagnóstico: `"Meu código falhou porque assumiu que a lista de entrada nunca continha valores nulos."`
   - Essa reflexão é inserida no histórico de memória do agente como um aviso prévio; o agente inicia uma nova tentativa do zero, desta vez tratando explicitamente os valores nulos e passando em todos os testes.

### Entradas e saídas

- **Entradas:** Meta do usuário, histórico da conversa e tracebacks de ferramentas ou testes unitários.
- **Saídas:** Trajetória auto-corrigida e entrega do resultado final validado.

## 📐 Formulação matemática

No framework **Reflexion**, a geração da trajetória $\tau_t$ na tentativa $t$ é condicionada não apenas ao objetivo $x$, mas ao histórico acumulado de reflexões verbais pregressas $\text{mem}_{\text{refl}} = \{r_1, r_2, \dots, r_{t-1}\}$:

$$\tau_t \sim \pi_\theta\Big(\cdot \;\Big|\; x, \; \text{mem}_{\text{refl}}\Big)$$

Onde a reflexão $r_{t-1}$ é produzida por um modelo reflexivo $\pi_{\text{refl}}$ avaliando a trajetória fracassada anterior e seu escore de feedback escalar $\mathcal{S}(\tau_{t-1})$:

$$r_{t-1} \sim \pi_{\text{refl}}\Big(\cdot \;\Big|\; \tau_{t-1}, \; \mathcal{S}(\tau_{t-1}), \; x\Big)$$

Essa retroalimentação transforma uma tarefa de aprendizado por reforço por tentativa e erro em um processo heurístico guiado por memória semântica em linguagem natural.

## 🧱 Hipóteses e condições de validade

- O modelo subjacente deve ter discernimento analítico suficiente para identificar o que causou o erro; modelos fracos tendem a alucinar explicações desconexas durante a fase de auto-reflexão, piorando o desempenho na segunda tentativa.

## ✅ Quando usar

- Agentes de geração e depuração automatizada de software (como SWE-agent).
- Resolução de problemas de perguntas e respostas em múltiplos saltos (*multi-hop QA* como o benchmark HotpotQA).
- Tarefas onde o ambiente fornece sinais claros e automáticos de sucesso ou falha (testes unitários, mensagens de erro de compilação, status HTTP).

## 🚫 Quando não usar

- Aplicações estritamente informativas de leitura única onde a resposta deve ser gerada em menos de 500 milissegundos.

## ⚠️ Limitações e armadilhas

- **Multiplicação de tokens e latência extrema:** Externalizar pensamentos, observações e reflexões a cada passo consome centenas de tokens adicionais por chamada de API, multiplicando a fatura financeira e o tempo de espera do cliente.
- **Auto-ilusão na reflexão:** O modelo convencer-se falsamente de que completou uma tarefa quando na verdade omitiu passos cruciais, encerrando a execução prematuramente.

## 🔍 Comparações

| Característica | Chain-of-Thought (CoT) | ReAct | Reflexion |
|---|---|---|---|
| **Interação externa** | Nula (apenas texto interno) | **Sim (chama ferramentas reais)** | **Sim (avalia testes e códigos)** |
| **Momento de correção** | Apenas no fluxo da decodificação | A cada passo de ferramenta | **Entre tentativas inteiras fracassadas** |
| **Memória utilizada** | Linear dentro do prompt | Histórico local de ações | **Buffer de reflexões persistidas** |
| **Resiliência a falhas de API** | Inexistente | Alta | **Máxima** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um agente é programado para criar uma função em Python que inverte as palavras de uma frase sem inverter as pontuações finais.

- *Tentativa 1:* O agente escreve o código. O interpretador roda os testes unitários e devolve: `AssertionError: Esperado 'Olá, mundo!' mas obteve '!mundo ,Olá'`.
- *Fase de Reflexion:* O modelo lê o erro e gera a reflexão: `"Reflexão: Meu código tratou a pontuação como parte da última palavra; preciso usar uma expressão regular para separar as palavras das pontuações antes de aplicar a inversão."`
- *Tentativa 2:* O agente reinicia o script, incorpora sua própria anotação de alerta, escreve o código com regex e passa com sucesso em 100% dos testes.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|Agentes de IA e Inventário de Ferramentas]]
- [[redes/ai-engineering/conceitos/planejamento-e-chamada-de-funcoes.md|Planejamento e Chamada de Funções (Function Calling)]]

### Complementos

- [[redes/ai-engineering/conceitos/cadeia-de-pensamento.md|Cadeia de Pensamento (Chain-of-Thought - CoT)]]
- [[redes/ai-engineering/conceitos/sistemas-de-memoria-para-ia.md|Sistemas de Memória para IA]]

### Alternativas

- Execução cega em lote sem paradas introspectivas intermediárias (*blind execution*).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/avaliacao-e-modos-de-falha-de-agentes.md|Avaliação e Modos de Falha de Agentes]]
- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 292–294
- **Evidência:** Chip Huyen destrincha a intercalação de raciocínio e ação originada pelo framework ReAct (Yao et al., 2022) no benchmark HotpotQA, e formaliza a arquitetura Reflexion (Shinn et al., 2023) composta por módulos de avaliação e memória verbal de trajetórias passadas.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é o framework ReAct e quais são as três etapas sequenciais que compõem o seu ciclo contínuo de execução?
2. Como o ReAct supera as limitações estáticas da Cadeia de Pensamento (Chain-of-Thought) tradicional?
3. Como funciona a arquitetura do framework Reflexion na correção de falhas entre trajetórias completas?
4. Qual é a função do módulo de "Auto-Reflexão Verbal" dentro da memória de trabalho do Reflexion?
5. Quais são os impactos financeiros e operacionais de latência decorrentes do uso extensivo de passos de reflexão?
6. O que é o fenômeno da "auto-ilusão na reflexão" e como ele pode induzir o encerramento prematuro de tarefas não concluídas?
7. Por que ambientes dotados de testes determinísticos de software são ideais para a aplicação prática do Reflexion?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Avaliação e Modos de Falha de Agentes

**Rede:** `ai-engineering`   **Área:** `agentes`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 298–300

## 📝 Definição

### Definição formal

A **Avaliação e Modos de Falha de Agentes** (*Agent Failure Modes and Evaluation*) compreende o conjunto de metodologias, métricas de observabilidade e taxonomias de erro voltadas a diagnosticar, mensurar e prevenir as avarias operacionais exclusivas que emergem em fluxos de trabalho autônomos impulsionados por [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|agentes de IA]], estruturando-se em três classes canônicas de falha:

1. **Falhas de Planejamento (*Planning Failures*):** Erros cognitivos do modelo gerador de planos (chamada de ferramentas inexistentes no inventário, fornecimento de argumentos inválidos, violação de restrições de negócio ou erros de reflexão em que o modelo acredita falsamente ter concluído a tarefa);
2. **Falhas de Ferramenta (*Tool Failures*):** Avarias decorrentes de ferramentas quebradas no mundo real (falhas de conexão, erros de tradução de sintaxe ou ausência de ferramentas adequadas para a tarefa solicitada);
3. **Falhas de Eficiência (*Efficiency Failures*):** Trajetórias que concluem a tarefa com sucesso, mas consomem quantidades desproporcionais de passos, tempo de execução e custos financeiros de tokens.

### Em linguagem simples

É a perícia técnica que investiga por que um agente autônomo falhou. Como um agente pensa, chama programas e toma decisões sozinho, ele pode falhar de muitas formas diferentes: ele pode inventar uma ferramenta que não existe, pode passar uma data errada como parâmetro, pode chamar a ferramenta certa mas a ferramenta estar fora do ar, ou pode levar 50 passos para fazer algo que um humano faria em dois cliques. Avaliar o agente é medir com que frequência cada uma dessas falhas acontece para poder consertá-las.

### Escopo e distinções

Diferencia-se da avaliação tradicional de modelos de linguagem (que mede apenas se o texto é fluente ou factualmente correto). A avaliação de agentes mede o **comportamento no ambiente**: a validade de chamadas de API, a preservação de restrições de tempo/orçamento e o sucesso de ponta a ponta na resolução do problema real.

## 🧩 Problema que resolve

Resolve a extrema opacidade de sistemas autônomos em produção. Se um agente falha ao tentar reservar um hotel para um cliente, sem uma taxonomia estrita de modos de falha a equipe não sabe se o erro ocorreu porque o LLM planejou mal, porque a API do hotel caiu ou porque a ferramenta demorou tanto que a sessão expirou.

## 💡 Intuição

Pense em um voo de avião não tripulado que caiu:

- **Falha de Planejamento:** O piloto automático calculou uma rota que passava exatamente por dentro de uma montanha.
- **Falha de Ferramenta:** O piloto automático traçou a rota perfeita, mas o motor direito sofreu uma pane física de combustível e parou de funcionar.
- **Falha de Eficiência:** O avião desviou da montanha e pousou no aeroporto correto, mas deu tantas voltas em círculos desnecessárias pelo caminho que gastou 5 vezes mais combustível e chegou com quatro horas de atraso.

## ⚙️ Como funciona

A suíte de testes avalia o agente através de métricas isoladas e integradas:

### Etapas

1. **Curadoria do Banco de Testes de Agentes:** Cria-se um conjunto representativo de tarefas complexas onde cada exemplo é uma tupla: `(tarefa, inventário_de_ferramentas, restrições, estado_esperado)`.
2. **Execução Instrumentada:** O agente executa a tarefa em ambiente controlado, enquanto a infraestrutura de telemetria registra cada log de pensamento, chamada de ferramenta e retorno de ambiente.
3. **Auditoria de Chamadas de Ferramenta:** Um script verifica:
   - Quantas ferramentas chamadas eram válidas?
   - Os argumentos passados respeitaram os tipos do JSON Schema?
   - Os valores dos argumentos eram logicamente corretos para o contexto?
4. **Auditoria de Conclusão da Meta (*Goal Completion*):** Valida-se o estado final do ambiente (ex.: o banco de dados foi atualizado corretamente? O e-mail foi disparado?).
5. **Cálculo de Métricas de Eficiência:** Registra-se o número médio de passos necessários por tarefa concluída e o custo total consolidado de inferência.

### Entradas e saídas

- **Entradas:** Metas de teste e telemetria de execução das trajetórias dos agentes.
- **Saídas:** Relatório analítico com taxas de falhas de planejamento, quebras de ferramentas e tempo médio de conclusão.

## 📐 Formulação matemática

A taxa de integridade de planejamento $R_{\text{plano}}$ sobre um conjunto de $T$ chamadas de ferramentas é avaliada pela proporção de invocações conformes:

$$R_{\text{plano}} = \frac{1}{T} \sum_{t=1}^T \mathbb{I}\Big(\text{Ferramenta}(t) \in \mathcal{F}_{\text{inventário}}\Big) \cdot \mathbb{I}\Big(\text{Args}(t) \text{ válidos}\Big)$$

A **Eficiência Relativa de Passos** ($\text{EFS}$) compara o número de passos tomados pelo agente $S_{\text{agente}}$ contra uma linha de base ótima humana ou algorítmica $S_{\text{ótimo}}$:

$$\text{EFS} = \frac{S_{\text{ótimo}}}{\mathbb{E}[S_{\text{agente}}]}$$

Onde valores próximos a 1 indicam trajetórias diretas e enxutas, e valores $\ll 1$ sinalizam agentes prolixos que disparam ferramentas desnecessárias.

## 🧱 Hipóteses e condições de validade

- Exige ambientes de teste reproduzíveis e idempotentes (*sandboxes* que possam ser resetadas para o estado inicial após cada execução para não acumular efeitos colaterais de testes anteriores).

## ✅ Quando usar

- Homologação de sistemas autônomos de agentes antes do lançamento em ambientes de clientes.
- Benchmarks de agentes da indústria como Berkeley Function Calling Leaderboard, TravelPlanner e AgentOps.

## 🚫 Quando não usar

- Em aplicações de geração puramente passivas sem ferramentas externas (onde métricas clássicas de RAG ou correção funcional são suficientes).

## ⚠️ Limitações e armadilhas

- **Falsa equivalência de eficiência humana:** O que é ineficiente para um humano pode ser trivial para a IA. Um humano levaria 2 horas para visitar 50 sites um por um; um agente com chamadas assíncronas paralelas pode visitar 50 sites em 3 segundos sem esforço cognitivo. A eficiência deve ser calibrada pelo custo e tempo real de máquina.
- **Testar apenas casos de caminho feliz (*Happy Path*):** Avaliar o agente apenas com comandos perfeitos onde nenhuma API externa falha, mascarando a incapacidade do agente de lidar com timeouts e erros de rede.

## 🔍 Comparações

| Categoria de Falha | Onde reside a causa? | Exemplo Real | Estratégia de Mitigação |
|---|---|---|---|
| **Planejamento** | No modelo de fundação | Chama função inexistente ou passa string onde devia ser int | Prompt com tipagem estrita e DPO |
| **Ferramenta** | No software externo | A API de clima retornou erro HTTP 500 | Retry com backoff e rotas de fallback |
| **Eficiência** | Na política de busca | Dá 20 passos em círculo antes de achar a resposta | Ajuste fino com trajetórias de especialistas |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um agente recebe a ordem de reservar quartos de hotel para 50 participantes de um evento.

- **Falha de Planejamento por Reflexão Errada:** O agente faz chamadas para reservar 40 quartos. Em seguida, ele emite a mensagem: `"Pronto! Todos os 50 participantes foram acomodados com sucesso."`. O modelo sofreu uma falha de auto-exame: ele parou o trabalho antes da meta real e insistiu com convicção de que havia terminado tudo.
- **Auditoria de Avaliação:** O pipeline de teste intercepta a finalização, conta os quartos reservados no banco (apenas 40), sinaliza uma falha estrita de conclusão de meta e impede o agente de enviar o e-mail falso de confirmação ao cliente.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|Agentes de IA e Inventário de Ferramentas]]
- [[redes/ai-engineering/conceitos/planejamento-e-chamada-de-funcoes.md|Planejamento e Chamada de Funções (Function Calling)]]

### Complementos

- [[redes/ai-engineering/conceitos/reflexao-e-correcao-de-erros-em-agentes.md|Reflexão e Correção de Erros em Agentes (ReAct e Reflexion)]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (representa o framework de diagnóstico de falhas).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/sistemas-de-memoria-para-ia.md|Sistemas de Memória para IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 298–300
- **Evidência:** Chip Huyen estabelece a taxonomia de modos de falha de agentes (planejamento, ferramentas e eficiência), cita benchmarks contemporâneos como Berkeley Function Calling Leaderboard, AgentOps e TravelPlanner, e analisa a armadilha de erros de reflexão onde o agente insiste falsamente que concluiu a tarefa.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as três categorias primárias de modos de falha em agentes de IA descritas no capítulo?
2. Como se manifestam as falhas de planejamento no acionamento de ferramentas externas?
3. O que é um erro de reflexão na avaliação de metas de um agente?
4. Por que a medição de eficiência de passos de um agente não deve ser comparada de forma ingênua com os padrões de tempo de um operador humano?
5. Quais métricas objetivas de telemetria devem ser extraídas a cada chamada de função durante a auditoria de um agente?
6. Como os benchmarks modernos de agentes (como o TravelPlanner) estruturam restrições de tempo e orçamento para avaliar planejamento complexo?
7. Por que ambientes de teste para agentes exigem infraestruturas isoladas do tipo sandbox com capacidade de reset de estado?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Sistemas de Memória para IA

**Rede:** `ai-engineering`   **Área:** `arquitetura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 300–304

## 📝 Definição

### Definição formal

Os **Sistemas de Memória para IA** (*Memory Systems for AI*) compreendem o conjunto integrado de mecanismos e estruturas de dados projetadas para permitir que um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] retenha, organize, atualize e recupere informações ao longo do tempo, estruturando-se em uma hierarquia funcional de três níveis interdependentes:

1. **Conhecimento Interno (*Parametric Memory*):** Conhecimento assimilado e codificado nos pesos matemáticos da rede neural durante o pré-treinamento e ajuste fino; é imutável em tempo de execução e acessível de forma onipresente em todas as inferências;
2. **Memória de Curto Prazo (*Working / Short-Term Memory*):** O contexto temporário contido na janela de tokens da requisição atual (*prompt context*); é rápida, flexível, mas volátil e estritamente limitada pelo comprimento máximo de contexto do modelo;
3. **Memória de Longo Prazo (*Non-Parametric / Long-Term Memory*):** Bases de dados e índices externos ([[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]], bancos vetoriais, logs de sessões passadas) acessados sob demanda via recuperação; é persistente entre sessões, editável sem re-treinar o modelo e com capacidade de armazenamento virtualmente infinita.

### Em linguagem simples

É a organização de como a IA guarda o que sabe. O conhecimento interno é como o seu cérebro biológico: você sabe falar português sem precisar consultar um livro. A memória de curto prazo é a sua memória de trabalho: você lembra o que acabou de ler nesta frase, mas vai esquecer quando mudar de assunto. A memória de longo prazo é o seu caderno de anotações ou o Google: coisas que você guarda fora do seu cérebro e consulta sempre que precisa se lembrar de algo antigo ou de conversas do mês passado.

### Escopo e distinções

Não se confunde puramente com o gerenciamento de memória física de hardware (RAM/VRAM de GPUs). Refere-se à arquitetura informacional que governa o que a IA deve lembrar, esquecer ou atualizar sobre seus usuários e tarefas ao longo de múltiplas conversas.

## 🧩 Problema que resolve

Resolve a amnésia congênita e o estouro de contexto de agentes e assistentes. Se uma conversa com um coach ou assistente tiver 200 mensagens, ela estoura o limite da janela de contexto ou torna a fatura de tokens impagável. Um sistema de memória filtra o que é importante, resume o passado e guarda as preferências do cliente de forma persistente.

## 💡 Intuição

Pense em um médico consultando um paciente crônico:

- **Conhecimento Interno:** Ele sabe fisiologia, anatomia e farmacologia porque estudou medicina na faculdade (pesos do modelo).
- **Memória de Curto Prazo:** Ele ouve a queixa atual do paciente nos últimos 5 minutos de consulta e retém o sintoma na cabeça (janela de contexto).
- **Memória de Longo Prazo:** Ele puxa a pasta do prontuário físico do paciente no arquivo do consultório para checar qual remédio receitou na consulta do ano passado e se o paciente tem alergia a penicilina (banco de dados externo de memória).

## ⚙️ Como funciona

O ciclo de gerenciamento de memória opera através de rotinas de admissão, condensação e descarte:

### Etapas

1. **Monitoramento da Janela:** Conforme a conversa avança, o sistema monitora o consumo de tokens na memória de curto prazo.
2. **Alocação de Quota:** Define-se uma reserva de espaço (ex.: reservar 30% da janela de contexto para recuperação de memória de longo prazo e deixar até 70% para o diálogo imediato).
3. **Transbordo e Estratégia de Descarte:** Quando o limite de curto prazo é atingido, o sistema aciona uma das seguintes políticas:
   - **FIFO (First-In, First-Out):** Apaga as mensagens mais antigas (arriscado, pois a primeira mensagem costuma conter o objetivo da conversa);
   - **Sumarização Periódica:** Um LLM resume as primeiras 20 mensagens em um parágrafo denso e descarta o texto bruto;
   - **Rastreamento de Entidades:** Um classificador extrai fatos atômicos estruturados (ex.: `gosta de livros de ficção científica`, `mora em Curitiba`) e salva em uma tabela de perfil;
   - **Reflexão sobre Contradições:** Se o usuário disser `"Mudei para São Paulo semana passada"`, o agente atualiza o dado de residência antigo, sobrescrevendo a informação defasada.
4. **Recuperação Contextual:** Na próxima sessão do usuário, o sistema recupera as entidades de perfil e os resumos passados relevantes e injeta no prompt inicial.

### Entradas e saídas

- **Entradas:** Histórico bruto de conversas de múltiplos turnos e atualizações contextuais do usuário.
- **Saídas:** Perfil persistente do usuário e prompts de contexto limpos sem redundâncias nem estouro de tokens.

## 📐 Formulação matemática

A capacidade total de informação disponível para o agente no passo $t$ é a união da memória paramétrica $\Theta$ e dos estados recuperados do histórico $H_{<t}$:

$$\mathcal{M}_{\text{total}}(t) = \Theta \cup \mathcal{C}_{\text{curto\_prazo}}(t) \cup \text{Recupera}\Big(\mathcal{D}_{\text{longo\_prazo}}, \; x_t\Big)$$

Sob a restrição estrita de comprimento máximo da janela de contexto $L_{\text{max}}$:

$$|\mathcal{C}_{\text{curto\_prazo}}(t)| + |\mathcal{C}_{\text{recuperado}}(t)| \le L_{\text{max}}$$

Onde qualquer excedente de informação informacional $\Delta > 0$ exige compressão semântica via operador de sumarização $\mathcal{S}$:

$$\mathcal{S}: H_{\text{antigo}} \mapsto H_{\text{comprimido}}, \quad \text{onde } |H_{\text{comprimido}}| \ll |H_{\text{antigo}}|$$

## 🧱 Hipóteses e condições de validade

- A persistência de dados pessoais de usuários na memória de longo prazo exige estrita conformidade regulatória (LGPD/GDPR), garantindo que o usuário possa auditar e solicitar a exclusão de suas memórias a qualquer momento.

## ✅ Quando usar

- Assistentes pessoais virtuais, tutores educacionais de longo prazo e copilotos corporativos que atendem o mesmo funcionário repetidamente ao longo de semanas ou meses.
- Agentes de fluxo longo que acumulam milhares de observações intermediárias de ferramentas.

## 🚫 Quando não usar

- Em APIs de classificação sem estado (*stateless*), como um analisador de spam de e-mails onde cada requisição é 100% independente da anterior.

## ⚠️ Limitações e armadilhas

- **Falha crítica do FIFO:** Usar o descarte ingênuo das mensagens mais velhas faz o modelo esquecer quem ele é e o que o usuário pediu para ele fazer no início do diálogo.
- **Alucinação na sumarização da memória:** O modelo de resumo condensar a conversa com um erro sutil de fato, e esse erro virar uma "falsa memória" permanente salva no banco de dados para todas as futuras sessões.

## 🔍 Comparações

| Nível de Memória | Onde reside? | Custo de Atualização | Persistência |
|---|---|---|---|
| **Conhecimento Interno** | Pesos da rede neural ($\theta$) | Altíssimo (exige [[redes/ai-engineering/conceitos/ajuste-fino.md\|Finetuning]]) | Permanente |
| **Curto Prazo (Contexto)** | Tokens na janela de atenção | Gratuito e instantâneo | Volátil (some ao fechar a sessão) |
| **Longo Prazo (Externo)** | Bancos vetoriais / Relacionais | Baixo (operações normais de banco) | **Permanente entre sessões** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um usuário utiliza um assistente de leitura há seis meses:

- Na sessão de março, ele comentou casualmente: `"Eu li O Problema dos Três Corpos e achei a melhor ficção científica da minha vida"`.
- O sistema de memória extrai o fato e salva no banco de dados de longo prazo do usuário: `{"preferencia_literaria": "Ficção científica", "livro_favorito": "O Problema dos Três Corpos"}`.
- Em setembro, o usuário abre o aplicativo e diz apenas: `"Me recomende um livro novo para este final de semana"`.

O agente consulta a **memória de longo prazo**, recupera o perfil silenciosamente e responde: `"Recomendo 'A Dança da Floresta' ou 'Fundação' de Isaac Asimov, que exploram dilemas sociológicos e espaciais parecidos com a complexidade que você adorou em O Problema dos Três Corpos"`.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]

### Complementos

- [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|Agentes de IA e Inventário de Ferramentas]]
- [[redes/ai-engineering/conceitos/eficiencia-de-contexto-e-lost-in-the-middle.md|Eficiência de Contexto e Efeito Lost-in-the-Middle]]

### Alternativas

- Arquiteturas sem estado (*stateless*) onde cada requisição começa do zero absoluto.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/planejamento-e-chamada-de-funcoes.md|Planejamento e Chamada de Funções (Function Calling)]]
- [[redes/ai-engineering/conceitos/reflexao-e-correcao-de-erros-em-agentes.md|Reflexão e Correção de Erros em Agentes (ReAct e Reflexion)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 300–304
- **Evidência:** Chip Huyen formaliza a hierarquia de memória (conhecimento interno, curto prazo e longo prazo), analisa o uso de buffers de contexto e detalha estratégias avançadas de gestão de memória com base em sumarização e reflexão contra contradições (citando trabalhos de Bae et al., 2022 e Liu et al., 2023).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são os três níveis que compõem a hierarquia de memória em sistemas de inteligência artificial?
2. Como a memória não-paramétrica de longo prazo permite atualizar o comportamento do modelo sem necessidade de alterar seus pesos matemáticos?
3. Por que a estratégia simples de descarte por FIFO (First-In, First-Out) pode comprometer tarefas longas de agentes?
4. Quais são as principais abordagens para comprimir o histórico de conversas e evitar o estouro da janela de contexto?
5. De que maneira a persistência de memória entre diferentes sessões viabiliza a personalização de produtos cognitivos?
6. Como o sistema lida com contradições factuais introduzidas pelo usuário ao longo do tempo (como mudança de endereço ou gostos)?
7. Quais são as implicações legais e regulatórias de governança ao armazenar perfis persistentes de memória de usuários?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

*Nota gerada a partir do capítulo Capítulo 6 — RAG and Agents. A interpretação final deve ser revisada pelo estudante.*
