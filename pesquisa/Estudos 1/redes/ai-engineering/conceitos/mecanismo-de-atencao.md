# 🧠 Mecanismo de Atenção

**Rede:** `ai-engineering`  
**Área:** `arquitetura-de-redes-neurais`

**Rede:** `ai-engineering`  
**Área:** `arquitetura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Entendendo Modelos de Fundação
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 58–64

## 📝 Definição

### Definição formal

Um componente de rede neural baseado na arquitetura Transformer que calcula dinamicamente pesos de relevância entre elementos de uma sequência de entrada através de operações matriciais envolvendo vetores de Consulta (*Query*), Chave (*Key*) e Valor (*Value*).

O **Mecanismo de Atenção** (*Attention Mechanism*), especificamente a atenção autorreferencial escalada por produto escalar (*scaled dot-product self-attention*), é um operador matemático diferencial que mapeia uma consulta (*Query*) e um conjunto de pares chave-valor (*Key-Value*) em uma saída vetorial, calculando a média ponderada dos vetores de valor $V$, onde o peso atribuído a cada valor reflete o grau de compatibilidade ou relevância computado entre a consulta $Q$ e a respectiva chave $K$.

### Em linguagem simples

É o mecanismo matemático que permite a um modelo olhar para diferentes partes de um texto e decidir quais palavras são mais importantes para entender o sentido da palavra que está sendo processada no momento.

É o componente que permite ao modelo decidir quais palavras anteriores são importantes para entender a palavra atual. Em vez de ler uma frase longa e resumir tudo em uma única memória comprimida, o modelo mantém todas as palavras visíveis e "olha" diretamente para os termos relevantes, não importando a que distância eles estejam no texto.

### Escopo e distinções

Diferencia-se de redes recorrentes (*RNNs*) porque não processa o texto estritamente palavra por palavra de forma linear, permitindo paralelização massiva e modelagem de dependências de longo alcance.

Introduzido inicialmente para arquiteturas seq2seq com RNNs (Bahdanau et al., 2014), foi consagrado como núcleo exclusivo de processamento na arquitetura Transformer (Vaswani et al., 2017). Não se confunde com as camadas lineares simples (*MLP/Feedforward*); enquanto o MLP transforma representações de cada token de forma isolada, a atenção calcula relações cruzadas entre múltiplos tokens.

## 🧩 Problema que resolve

Resolve a incapacidade de arquiteturas antigas de reter conexões contextuais de longo alcance em textos longos e elimina o gargalo de processamento estritamente sequencial.

Supera dois gargalos críticos das Redes Neurais Recorrentes (RNNs/LSTMs):
1. **Gargalo do vetor de contexto fixo:** RNNs comprimiam uma sentença inteira em um único vetor oculto final. Para textos longos, detalhes do início da frase eram esquecidos (*vanishing gradients*).
2. **Gargalo do processamento sequencial estrito:** RNNs exigiam processar a palavra $t$ antes de iniciar a palavra $t+1$. O mecanismo de atenção no Transformer permite processar todos os tokens de entrada simultaneamente em paralelo durante a fase de ingestão.

## 💡 Intuição

Pense em um sistema de busca em uma biblioteca: a sua pergunta atual é a Consulta (*Query*), os títulos nas lombadas dos livros são as Chaves (*Key*) que indicam o assunto, e o conteúdo escrito dentro do livro escolhido é o Valor (*Value*) real utilizado para responder à sua dúvida.

Imagine um pesquisador elaborando uma monografia.
- A **Query** ($Q$) é a pergunta de pesquisa que ele precisa responder no parágrafo atual.
- As **Keys** ($K$) são as etiquetas ou cabeçalhos nos fichários de sua estante que indicam o tema de cada livro.
- Os **Values** ($V$) são o conteúdo textual detalhado contido nas páginas de cada livro.
O pesquisador compara sua pergunta ($Q$) com todas as etiquetas ($K$). Os livros cujas etiquetas combinam com a pergunta recebem atenção prioritária, e o pesquisador extrai o conteúdo ($V$) desses livros para redigir sua resposta.

## ⚙️ Como funciona

O cálculo opera sobre representações matriciais densas projetadas linearmente a partir dos tokens:

### Etapas

1. O vetor de entrada é multiplicado por matrizes de pesos para gerar os vetores de Consulta ($Q$), Chave ($K$) e Valor ($V$).
2. Calcula-se a pontuação de compatibilidade entre a consulta e todas as chaves através do produto escalar (*dot product*).
3. Aplica-se a função Softmax sobre as pontuações para obter os pesos de atenção normalizados.
4. Multiplica-se os pesos normalizados pelos vetores de Valor para obter a representação contextualizada final.

1. **Projeção linear:** O vetor do token de entrada $x$ é multiplicado por três matrizes de parâmetros treináveis ($W_Q, W_K, W_V$) para produzir os vetores $Q = xW_Q$, $K = xW_K$ e $V = xW_V$.
2. **Cálculo de similaridade:** Executa-se o produto escalar entre $Q$ e a transposta de todas as chaves $K^T$, gerando pontuações brutas de relevância mútua.
3. **Escalonamento:** Divide-se as pontuações por $\sqrt{d_k}$ (raiz quadrada da dimensão da chave) para estabilizar os gradientes e evitar que valores excessivamente altos saturem a função softmax.
4. **Normalização por Softmax:** Aplica-se a função *softmax* linha a linha para converter as pontuações em pesos percentuais de atenção que somam 1.
5. **Ponderação dos valores:** Multiplica-se a matriz de pesos resultantes pela matriz de valores $V$.
6. **Múltiplas cabeças (*Multi-Head Attention*):** Esse processo é executado em paralelo através de $h$ "cabeças" independentes que capturam relações semânticas e sintáticas distintas, cujos resultados são concatenados e projetados pela matriz de saída $W_O$.

### Entradas e saídas

- Entradas: Matrizes de representação sequencial de tokens.
- Saídas: Nova matriz de representação vetorial enriquecida com o contexto ponderado da atenção.

- **Entradas:** Matrizes de ativações de tokens de dimensão $N \times d_{\text{modelo}}$.
- **Saídas:** Nova matriz contextualizada de dimensão $N \times d_{\text{modelo}}$, onde cada posição agora incorpora informações de todos os outros tokens correlacionados.

## 📐 Formulação matemática

A formulação padrão da atenção dimensionada por produto escalar (*Scaled Dot-Product Attention*) é expressa por:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Onde:
- $Q$: Matriz de consultas (*Queries*).
- $K$: Matriz de chaves (*Keys*).
- $V$: Matriz de valores (*Values*).
- $d_k$: Dimensão vetorial das chaves (utilizada como fator de escala para estabilização gradiente).

A equação fundamental da atenção escalada é expressa como:

Onde:
- $Q \in \mathbb{R}^{N \times d_k}$ é a matriz de consultas;
- $K \in \mathbb{R}^{M \times d_k}$ é a matriz de chaves;
- $V \in \mathbb{R}^{M \times d_v}$ é a matriz de valores;
- $\sqrt{d_k}$ é o fator de escala de estabilização numérica;
- A complexidade temporal e espacial da matriz de atenção é $\mathcal{O}(N^2)$ em relação ao comprimento da sequência $N$.

## 🧱 Hipóteses e condições de validade

- Requer espaço de memória computacional proporcional ao quadrado do comprimento da sequência ($O(N^2)$), o que impõe restrições de escala para contextos massivos sem otimizações específicas.

- Os tokens recebem vetores de posição (*positional embeddings*) adicionados às suas entradas, uma vez que o produto escalar de atenção é uma operação equivariante à permutação (sem noção intrínseca de ordem temporal sem os embeddings posicionais).

## ✅ Quando usar

- Em qualquer arquitetura baseada em Transformers para modelagem de sequências em processamento de linguagem natural e visão computacional.

- Componente padrão de modelos de fundação baseados em Transformer para linguagem, código e visão multimodal.
- Aplicações que exigem resolução precisa de referências cruzadas em documentos e código estruturado.

## 🚫 Quando não usar

- Em ambientes com restrições extremas de hardware de memória em tempo real onde alternativas lineares (como SSMs) sejam mandatórias.

- Em contextos de hardware ultra-restrito que exigem processamento linear em tempo real sobre fluxos infinitos de dados, onde alternativas como [[redes/ai-engineering/conceitos/modelos-de-espaco-de-estados.md|Modelos de Espaço de Estados (SSMs)]] são superiores pela complexidade $\mathcal{O}(N)$.

## ⚠️ Limitações e armadilhas

- Complexidade computacional quadrática em relação ao comprimento do contexto, tornando janelas ultra-longas proibitivas sem engenharia avançada de kernels.

- **Custo quadrático:** Conforme o contexto se expande (ex.: de 4K para 128K tokens), o número de cálculos da matriz de atenção cresce com o quadrado do comprimento da sequência ($\mathcal{O}(N^2)$), demandando técnicas de otimização de memória (como FlashAttention e agrupamento de consultas).
- **Sobrecarga de KV Cache:** Na decodificação autoregressiva sequencial, as matrizes $K$ e $V$ de todos os tokens anteriores precisam ser mantidas em VRAM na placa de vídeo, tornando-se o principal limitador de throughput em contextos longos.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[mecanismo-de-atencao|Mecanismo de Atenção]] | Ponderar relações contextuais entre elementos de uma sequência. | Matrizes $Q$, $K$ e $V$. | Vetor de contexto ponderado. | Permite acesso direto e paralelo a qualquer parte do histórico de tokens. |
| [[rnn|Rede Recorrente (RNN)]] | Processar dados sequenciais passo a passo no tempo. | Vetor atual + Estado oculto anterior. | Nova saída + Estado oculto atual. | Processamento estritamente sequencial e propenso a esquecimento de longo prazo. |

| Arquitetura | Dependência Temporal | Complexidade de Sequência | Paralelismo no Treino |
|---|---|---|---|
| **RNN / LSTM** | Passo a passo recorrente | $\mathcal{O}(N)$ | Impossível (sequencial estrito) |
| **Atenção Transformer** | Acesso direto a qualquer token | $\mathcal{O}(N^2)$ | Totalmente paralelo no prefill |
| **SSM / Mamba** | Recorrência linear invariante | $\mathcal{O}(N)$ | Paralelo no treino, linear no decode |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Na frase "O banco de areia afundou porque ele era movediço", o mecanismo de atenção ajuda o modelo a associar fortemente o pronome "ele" ao substantivo "banco de areia" e não à instituição financeira "banco".

Considere a frase: `"O cachorro atravessou a rua correndo porque ele viu um gato"`. 
Quando o modelo está calculando o significado da palavra `"ele"`, a **Query** dessa palavra se alinha perfeitamente com a **Key** de `"cachorro"`, atribuindo um peso de atenção alto ($0{,}85$) a essa posição e um peso irrelevante ($0{,}02$) à palavra `"rua"`. Isso permite que a camada seguinte assimile que `"ele"` é o cachorro, resolvendo a ambiguidade do pronome sem regras fixas.

## 🔗 Relações no grafo

### Pré-requisitos

- [[tokenizacao|Tokenizacao]]
- [[modelo-de-linguagem|Modelo de Linguagem]]

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]

### Complementos

- [[prefill-e-decode|Prefill e Decode]]

- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Alternativas

- [[modelos-de-espaco-de-estado|Modelos de Espaço de Estado (SSMs)]]

- [[redes/ai-engineering/conceitos/modelos-de-espaco-de-estados.md|Modelos de Espaço de Estados (SSMs)]]

### Conceitos relacionados

- [[modelo-de-fundacao|Modelo de Fundação]]

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Entendendo Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Explicação técnica detalhada da formulação matricial de atenção com vetores Q, K e V introduzida pelo Transformer.
- **Confiança:** alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 58–64
- **Evidência:** Chip Huyen destrincha a matemática do mecanismo de atenção do Transformer, detalhando os papéis vetoriais de Q, K e V, as dimensões matriciais (ex.: Llama 2-7B com 32 cabeças e dimensão 4096) e demonstrando por que a atenção suplantou os RNNs ao quebrar a barreira sequencial de entrada.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Mecanismo de Atenção?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

1. O que representam conceitual e matematicamente os vetores Query ($Q$), Key ($K$) e Value ($V$) no mecanismo de atenção?
2. Por que a introdução do mecanismo de atenção sem componentes recorrentes (RNNs) viabilizou o treinamento massivo em paralelo do Transformer?
3. Qual é a finalidade matemática de se dividir o produto escalar de $QK^T$ por $\sqrt{d_k}$ antes da função softmax?
4. Como a complexidade computacional $\mathcal{O}(N^2)$ da atenção afeta o custo e o processamento de contextos longos?
5. De que forma o mecanismo de atenção de múltiplas cabeças (*multi-head attention*) enriquece a capacidade de representação do modelo?
6. O que é o KV Cache na fase de inferência e qual é a sua conexão direta com a mecânica da atenção?
7. Por que a atenção pura é equivariante à permutação e como os embeddings posicionais resolvem essa limitação?

## Conexoes com Machine Learning

Estes fundamentos pertencem a outra rede e foram ligados como prerequisitos ou conceitos vizinhos. O MOC nao e usado como no conceitual.
- [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais.md|Deep Learning & Redes Neurais]]
- [[redes/machine-learning/conceitos/Redes_Neurais_Artificiais.md|Redes Neurais Artificiais]]
- [[redes/machine-learning/conceitos/Funções_de_Ativação.md|Funções de Ativação]]

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 2 — Entendendo Modelos de Fundação. A interpretação final deve ser revisada pelo estudante.*
