# 🧠 Leis de Escala e Chinchilla

**Rede:** `ai-engineering`  
**Área:** `modelagem`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 72–74

## 📝 Definição

### Definição formal

As **Leis de Escala** (*Scaling Laws*) em modelos de linguagem são relações empíricas de lei de potência que descrevem com precisão matemática a redução previsível da perda de entropia cruzada (*training loss*) em função da escala de três variáveis interdependentes: número de parâmetros da rede neural ($N$), tamanho do conjunto de dados em tokens de treinamento ($D$) e orçamento total de computação em FLOPs ($C$). 

A **Lei de Escala de Chinchilla** (Hoffmann et al., DeepMind, 2022) provou formalmente que, para atingir o desempenho computacionalmente ótimo sob um orçamento fixo de FLOPs, o número de parâmetros e o número de tokens de treinamento devem ser escalados em proporções iguais (1:1), estabelecendo que a quantidade ideal de tokens de treino é de aproximadamente 20 vezes o número de parâmetros do modelo.

### Em linguagem simples

É a fórmula matemática que ensina como não jogar dinheiro fora ao treinar uma inteligência artificial. Antes dessa lei, as empresas gastavam fortunas construindo modelos gigantescos que liam poucos textos e ficavam "sub-treinados". A lei de Chinchilla provou que para cada parâmetro que você adiciona no modelo, você deve dar a ele cerca de 20 palavras a mais para ler durante o treino.

### Escopo e distinções

A lei de Chinchilla foca no **ótimo computacional de treinamento** (como obter a menor perda com o menor custo financeiro de treino). Diferencia-se do **ótimo de inferência** (adotado por modelos como o Llama), onde desenvolvedores treinam intencionalmente modelos menores com muito mais dados do que Chinchilla recomenda (ex.: Llama 3 treinou um modelo de 8B com 15 trilhões de tokens) para que o modelo fique pequeno, barato e rápido de rodar no dia a dia dos usuários finais.

## 🧩 Problema que resolve

Supera a era de "alquimia" e empirismo cego no treinamento de LLMs. Antes do artigo de Chinchilla, modelos como GPT-3 (175B parâmetros treinados em 300 bilhões de tokens) e Gopher (280B parâmetros em 300 bilhões de tokens) eram massivamente sub-treinados. O modelo Chinchilla provou que um modelo de 70B parâmetros treinado com 1,4 trilhão de tokens supera o Gopher de 280B consumindo o mesmo orçamento computacional exato.

## 💡 Intuição

Pense em preparar um estudante para uma olimpíada acadêmica.
- O **número de parâmetros** é a capacidade biológica do cérebro do estudante.
- O **número de tokens** é a quantidade de livros didáticos que ele tem tempo de ler.
Não adianta contratar um gênio com capacidade cerebral monumental se você der a ele apenas dois livros de resumo para estudar; ele perderá a prova para um aluno comum com boa capacidade que passou o ano inteiro lendo cem livros aprofundados. O cérebro e a quantidade de material de estudo devem crescer juntos.

## ⚙️ Como funciona

O cálculo de dimensionamento parte do orçamento financeiro/físico de infraestrutura:

### Etapas

1. **Definição do orçamento de computação ($C$):** Fixa-se o total de operações de ponto flutuante disponíveis com base nas GPUs contratadas (ex.: $10^{24}$ FLOPs).
2. **Aplicação dos coeficientes de Chinchilla:** Calcula-se a distribuição ótima entre capacidade da rede e material de dados.
3. **Determinação do tamanho do modelo ($N$):** Define-se o número de bilhões de parâmetros que a arquitetura deve ter.
4. **Determinação do volume de tokens ($D$):** Coleta-se e limpa-se uma base de dados contendo aproximadamente $20 \times N$ tokens.
5. **Previsão antecipada da perda:** Antes de ligar as máquinas, a fórmula da lei de potência calcula com alta precisão qual será a perda final de treino obtida, evitando desperdício de recursos.

### Entradas e saídas

- **Entradas:** Orçamento computacional em FLOPs ou restrições de custo de GPU.
- **Saídas:** Parâmetros ótimos de arquitetura ($N$), tamanho exigido do dataset ($D$) e projeção matemática da perda esperada.

## 📐 Formulação matemática

O orçamento total de computação para o pré-treinamento de um Transformer denso autoregressivo padrão aproxima-se por:

$$C \approx 6 N D \text{ FLOPs}$$

Onde $N$ é o número de parâmetros e $D$ é o número de tokens. Hoffmann et al. modelaram a perda $\mathcal{L}$ como:

$$\mathcal{L}(N, D) = E + \frac{A}{N^\alpha} + \frac{B}{D^\beta}$$

Sob a restrição de que $\alpha \approx \beta \approx 0{,}5$, a otimização com multiplicadores de Lagrange dita que para minimizar a perda sob um custo fixo $C$:

$$N \propto C^a, \quad D \propto C^b \quad \text{com } a \approx b \approx 0{,}5 \implies \frac{D}{N} \approx 20$$

## 🧱 Hipóteses e condições de validade

- Assume que o custo de coleta e armazenamento de dados de treino é negligenciável quando comparado ao custo do poder de computação das GPUs.
- Desenvolvida empiricamente para modelos densos alimentados com texto de qualidade padrão; ajustes são necessários para arquiteturas esparsas (MoE) e síntese maciça de dados.

## ✅ Quando usar

- Dimensionamento e planejamento orçamentário de pré-treinamento de modelos a partir do zero.
- Avaliação crítica de relatórios técnicos de novos modelos lançados no mercado para identificar se o modelo foi sub-treinado ou sobre-treinado.

## 🚫 Quando não usar

- Em aplicações típicas de engenharia de software na camada de aplicação, onde os modelos são consumidos já prontos via API de terceiros.

## ⚠️ Limitações e armadilhas

- **Foco estrito no treinamento:** O ótimo de Chinchilla minimiza o custo de treino, mas ignora o custo operacional de inferência a longo prazo. Se um modelo menor (sobre-treinado além de Chinchilla) puder atingir o mesmo desempenho de um modelo grande, o modelo menor deve ser preferido em produção porque sua inferência será muito mais barata.

## 🔍 Comparações

| Modelo | Parâmetros ($N$) | Tokens de Treino ($D$) | Relação $D/N$ | Status de Chinchilla |
|---|---|---|---|---|
| **GPT-3 (2020)** | 175 bilhões | 300 bilhões | $\approx 1{,}7$ | Severamente sub-treinado |
| **Gopher (2021)** | 280 bilhões | 300 bilhões | $\approx 1{,}1$ | Severamente sub-treinado |
| **Chinchilla (2022)** | 70 bilhões | 1,4 trilhão | $\approx 20$ | **Computacionalmente ótimo** |
| **Llama 3 (2024)** | 8 bilhões | 15 trilhões | $\approx 1.875$ | Sobre-treinado (ótimo de inferência) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma startup de tecnologia dispõe de um orçamento de computação capaz de realizar $3{,}6 \times 10^{23}$ FLOPs de treino.
- Se a equipe seguisse a abordagem pré-Chinchilla, ela construiria um modelo gigante de **100 bilhões de parâmetros**, mas só conseguiria alimentá-lo com **60 bilhões de tokens** antes do dinheiro acabar ($D/N = 0{,}6$). O modelo ficaria medíocre e esqueceria conceitos básicos.
- Aplicando a **Lei de Chinchilla**, a equipe divide o orçamento igualmente: constrói um modelo enxuto de **17 bilhões de parâmetros** e o treina com **350 bilhões de tokens** ($D/N \approx 20$). O modelo atinge pontuações muito superiores nos testes gastando a mesma quantia financeira.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]

### Complementos

- [[redes/ai-engineering/conceitos/gargalos-de-escala.md|Gargalos de Escala: Dados e Energia]]
- [[redes/ai-engineering/conceitos/mixture-of-experts.md|Mixture of Experts (MoE)]]

### Alternativas

- Dimensionamento voltado para otimalidade de inferência (*Inference-optimal scaling* adotado pela Meta no Llama).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 72–74
- **Evidência:** O texto detalha a publicação clássica da DeepMind (2022) "Training Compute-Optimal Large Language Models", demonstrando que o número de tokens de treinamento deve ser aproximadamente 20 vezes o tamanho do modelo para garantir a otimalidade computacional frente ao custo de FLOPs.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que são as Leis de Escala em modelos de linguagem e qual a sua relevância prática para o orçamento de IA?
2. Qual foi a descoberta empírica central estabelecida pelo artigo do modelo Chinchilla da DeepMind em 2022?
3. Qual é a proporção recomendada entre o número de tokens de treino e o número de parâmetros de um modelo denso segundo Chinchilla?
4. Por que modelos pioneiros como o GPT-3 de 175B e o Gopher de 280B são classificados tecnicamente como sub-treinados?
5. Qual é a diferença estratégica fundamental entre um modelo "computacionalmente ótimo para treinamento" e um modelo "ótimo para inferência"?
6. Como o Llama 3 exemplifica a decisão de violar a proporção estrita de Chinchilla em favor da eficiência de atendimento em produção?
7. Qual é a fórmula básica de aproximação que relaciona o orçamento de FLOPs ($C$), os parâmetros ($N$) e os tokens ($D$)?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
