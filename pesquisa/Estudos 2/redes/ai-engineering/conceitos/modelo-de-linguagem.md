# 🧠 Modelo de Linguagem

**Rede:** `ai-engineering`   **Área:** `modelagem`

**Rede:** `ai-engineering`  
**Área:** `processamento-de-linguagem-natural`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 2–6

## 📝 Definição

### Definição formal

Um **Modelo de Linguagem** (*Language Model* — LM) é uma distribuição estatística de probabilidade sobre sequências de palavras ou [[redes/ai-engineering/conceitos/tokenizacao.md|tokens]], cujo propósito formal é calcular a probabilidade $P(W)$ de uma sequência arbitrária $W = (w_1, w_2, \dots, w_n)$ ocorrer em uma dada língua, ou estimar a distribuição condicional $P(w_t \mid w_1, \dots, w_{t-1})$ de uma palavra futura dado o contexto precedente.

Um modelo estatístico ou neural que codifica a distribuição de probabilidade sobre sequências de tokens em uma ou mais linguagens naturais, permitindo estimar a probabilidade de ocorrência de um token dado um contexto prévio.

### Em linguagem simples

É um programa que aprendeu os padrões estatísticos de como as palavras são usadas juntas. Ele serve para responder à pergunta: "Dada esta frase que começou assim, qual é a palavra mais provável de vir agora?".

É um sistema computacional treinado para entender as regras estatísticas de um idioma, permitindo prever qual palavra ou parte de palavra tem mais chances de aparecer em seguida em uma frase.

### Escopo e distinções

Não se confunde com um dicionário ou um conjunto fixo de regras gramaticais simbólicas. O modelo não "sabe" gramática no sentido declarativo de regras lógicas; ele capta regularidades estatísticas a partir da frequência e coocorrência de termos em corpora textuais. Divide-se primariamente em [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|modelos de linguagem autoregressivos]] e [[redes/ai-engineering/conceitos/modelo-de-linguagem-mascarado.md|modelos de linguagem mascarados]].

Abrange desde modelos estatísticos tradicionais baseados em contagem de n-gramas até grandes redes neurais profundas. Não deve ser confundido com um sistema de raciocínio lógico formal; trata-se de um preditor estatístico de padrões textuais.

## 🧩 Problema que resolve

Resolve a necessidade de quantificar e predizer computacionalmente o comportamento da linguagem humana. Permite que sistemas de software realizem traduções automáticas, correções ortográficas, reconhecimento de fala e completação de texto sem exigir a especificação manual de bilhões de regras gramaticais e de contexto.

Resolve a incapacidade de computadores de processar, antecipar e gerar texto de maneira fluida e estatisticamente coerente. Sem modelos de linguagem, sistemas computacionais não conseguiriam realizar tarefas como predição de texto, tradução automática ou sumarização.

## 💡 Intuição

Imagine um jogo de adivinhação: alguém diz "Meu prato predileto de domingo é arroz com...". Pelo seu conhecimento da língua e cultura, seu cérebro sabe que a probabilidade de a próxima palavra ser "feijão" é imensamente superior à probabilidade de ser "computador" ou "automóvel". O modelo de linguagem é o motor matemático que calcula com exatidão essas probabilidades numéricas para cada palavra possível.

Pense no recurso de predição de texto do teclado do seu smartphone: conforme você digita as primeiras palavras, o sistema calcula quais palavras seguintes são estatisticamente mais prováveis com base em tudo o que você já digitou.

## ⚙️ Como funciona

O modelo converte texto em representações numéricas e aplica operações matriciais para derivar probabilidades:

### Etapas

1. **Segmentação da entrada:** O texto bruto é convertido em uma cadeia de tokens pelo vocabulário do modelo ([[redes/ai-engineering/conceitos/tokenizacao.md|tokenização]]).
2. **Representação vetorial:** Cada token é mapeado para um vetor denso (*embedding*).
3. **Processamento contextual:** Camadas de redes neurais avaliam as dependências entre os tokens da sequência.
4. **Cálculo da camada de saída:** O modelo produz pontuações brutas (*logits*) para cada token pertencente ao vocabulário.
5. **Normalização probabilística:** Aplica a função *softmax* sobre os *logits*, convertendo-os em uma distribuição de probabilidades que soma 1.

1. O texto original é processado e quebrado em unidades atômicas chamadas tokens por um tokenizador.
2. O modelo analisa o contexto histórico de tokens anteriores.
3. O sistema calcula a distribuição de probabilidade para o vocabulário completo.
4. Um token é selecionado através de estratégias de amostragem.

### Entradas e saídas

- **Entradas:** Uma sequência de tokens de contexto $x_1, x_2, \dots, x_{t-1}$.
- **Saídas:** Um vetor de probabilidades de tamanho $|V|$ (onde $|V|$ é o tamanho do vocabulário), indicando a chance de cada token candidato ocupar a posição $x_t$.

- Entradas: Uma sequência de texto (contexto ou prompt) dividida em tokens.
- Saídas: Uma distribuição de probabilidade sobre o vocabulário ou o próximo token selecionado.

## 📐 Formulação matemática

A probabilidade conjunta de uma sequência textual de $n$ palavras decompõe-se pela regra da cadeia de probabilidades:

$$P(w_1, w_2, \dots, w_n) = \prod_{i=1}^n P(w_i \mid w_1, w_2, \dots, w_{i-1})$$

A qualidade preditiva do modelo sobre um corpus de teste de $N$ tokens é historicamente medida através da métrica de entropia cruzada ($H$) ou perplexidade ($\text{PPL}$):

$$\text{PPL}(W) = \exp\left( -\frac{1}{N} \sum_{i=1}^N \ln P(w_i \mid w_{<i}) \right)$$

Quanto menor a perplexidade, maior a precisão do modelo em antecipar a sequência real.

Representado formalmente pela probabilidade conjunta de uma sequência de tokens $X = (x_1, x_2, \dots, x_T)$, decomposta pelo produto de probabilidades condicionais:

$$P(X) = \prod_{t=1}^{T} P(x_t \mid x_1, x_2, \dots, x_{t-1})$$

Onde:
- $X$: Sequência completa de tokens.
- $x_t$: Token na posição temporal $t$.
- $P(x_t \mid x_1, \dots, x_{t-1})$: Probabilidade condicional do token atual dada a história prévia.

## 🧱 Hipóteses e condições de validade

- A linguagem natural exibe consistência estatística interna suficiente para que padrões observados em dados passados sejam generalizáveis para novas construções textuais (princípio formalizado por Claude Shannon em 1951).
- O vocabulário utilizado cobre suficientemente os termos da língua, mitigando o problema de termos fora do vocabulário (*out-of-vocabulary*).

- Hipótese de que a linguagem natural pode ser aproximada por distribuições estatísticas de probabilidade sequencial.
- Dependência de dados de treinamento que representem adequadamente a distribuição do idioma-alvo.

## ✅ Quando usar

- Tarefas de geração, edição, sumarização ou reescrita de conteúdo textual.
- Sistemas de autocompletar, tradução e transcrição fonética para texto.
- Avaliação de plausibilidade ou fluência de frases em pipelines de processamento de linguagem natural.

- Tarefas de predição de texto, autocompletar, correção gramatical, tradução e geração de conteúdo textual geral.

## 🚫 Quando não usar

- Casos em que se exige exatidão determinística imediata sem tolerância a erros probabilísticos.
- Recuperação de dados estruturados relacionais simples, onde uma consulta SQL direta é ordens de grandeza mais rápida, exata e barata.

- Em tarefas que exigem garantia matemática de exatidão lógica formal sem verificação externa, pois o modelo opera puramente sob predição estatística.

## ⚠️ Limitações e armadilhas

- **Confusão entre fluência e veracidade:** O fato de uma frase ser estatisticamente provável não implica que o fato nela narrado seja verdadeiro no mundo real.
- **Dependência do viés de dados:** O modelo reflete os preconceitos, termos desatualizados e frequências assimétricas presentes em seus dados de treinamento.

- Vulnerável a alucinações estatísticas.
- Dependência severa da qualidade e diversidade do corpus de treinamento.
- Incapacidade inerente de validar a veracidade factual do mundo real sem mecanismos externos de busca ou recuperação.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[modelo-de-linguagem|Modelo de Linguagem]] | Estimar probabilidades de sequências textuais. | Sequência de tokens. | Distribuição de probabilidade / Próximo token. | Foco estrutural estatístico amplo sobre o idioma. |
| [[modelo-de-fundacao|Modelo de Fundação]] | Servir de base generalista para múltiplos domínios e modalidades. | Dados multimodais em grande escala. | Representações generalizadas / Respostas complexas. | Escala massiva e capacidade de generalização de zero-shot para diversas tarefas. |

| Abordagem | Modelo de Linguagem Neural | Gramáticas Formais Clássicas |
|---|---|---|
| **Mecanismo** | Distribuições de probabilidade aprendidas | Regras determinísticas "SE-ENTÃO" |
| **Robustez** | Tolera ambiguidades, gírias e erros gramaticais | Quebra perante desvios das regras formais |
| **Escalabilidade** | Aumenta de capacidade com mais dados e parâmetros | Torna-se ingovernável com milhares de regras manuais |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Considere a frase inacabada: "O médico solicitou um exame de...". 
O modelo de linguagem recebe esses 7 tokens de entrada, calcula as pontuações para os 100.000 tokens do seu vocabulário e atribui alta probabilidade para termos como "sangue" ($0{,}35$), "imagem" ($0{,}20$) ou "urina" ($0{,}15$), e probabilidade próxima de zero para tokens como "banana" ($0{,}000001$) ou "ontem" ($0{,}000002$).

Dada a frase incompleta "O gato subiu no...", o modelo de linguagem atribui altas probabilidades estatísticas a tokens como "telhado" ou "muro", e probabilidade próxima de zero para termos gramaticalmente desconexos como "computadorizador".

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Complementos

- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]

- [[tokenizacao|Tokenizacao]]
- [[auto-supervisão|Auto-supervisão]]

### Alternativas

- Gramáticas simbólicas livres de contexto e analisadores sintáticos determinísticos.

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/modelo-de-linguagem-mascarado.md|Modelo de Linguagem Mascarado]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

- [[modelo-de-fundacao|Modelo de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 2–6
- **Evidência:** O texto traça a evolução dos LMs desde Shannon (1951) e o conto de Sherlock Holmes, explicando como os modelos codificam distribuições de probabilidade estatística de idiomas sobre tokens.
- **Confiança:** Alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Descrição da evolução histórica e estatística de modelos que codificam informações sobre um ou mais idiomas.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. Qual é a definição matemática e operacional de um modelo de linguagem?
2. Como a quebra do texto em tokens afeta o funcionamento do modelo de linguagem?
3. O que motivou a transição de gramáticas formais baseadas em regras para modelos de linguagem estatísticos?
4. Qual é a diferença conceitual entre calcular a probabilidade de uma sequência completa e calcular a probabilidade condicional do próximo token?
5. Por que um modelo de linguagem pode gerar um texto gramaticalmente perfeito que expressa uma mentira factual completa?
6. Como o trabalho clássico de Claude Shannon (1951) se relaciona com os LLMs modernos?
7. Quais são os dois ramos arquiteturais principais nos quais os modelos de linguagem se dividem?

1. O que é Modelo de Linguagem?
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
