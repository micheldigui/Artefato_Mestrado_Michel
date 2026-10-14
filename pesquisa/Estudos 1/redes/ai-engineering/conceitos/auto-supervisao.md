# 🧠 Auto-supervisão

**Rede:** `ai-engineering`   **Área:** `treinamento`

**Rede:** `ai-engineering`  
areas: `aprendizado-de-maquina`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 6–8

## 📝 Definição

### Definição formal

A **Auto-supervisão** (*Self-Supervised Learning*) é um paradigma de aprendizado de máquina no qual os objetivos de treino e seus respectivos rótulos de supervisão (*labels*) são derivados de forma autônoma a partir da estrutura intrínseca dos próprios dados brutos de entrada, eliminando a dependência de anotação manual externa fornecida por humanos.

Um paradigma de aprendizado de máquina onde o modelo aprende a representar e extrair padrões de dados não rotulados através da formulação automática de tarefas preditivas supervisionadas geradas a partir dos próprios dados de entrada.

### Em linguagem simples

É a técnica que permite ao computador aprender sozinho lendo textos comuns da internet. Em vez de um humano dizer "este texto fala de esportes", o computador pega uma frase qualquer, esconde a última palavra e tenta adivinhar qual era. O próprio texto fornece a pergunta e o gabarito.

É um método em que o computador aprende sozinho a partir de textos crus tirados da internet, usando as próprias palavras seguintes de uma frase como gabarito de teste, sem precisar que humanos rotulem os dados manualmente.

### Escopo e distinções

Não se confunde com o aprendizado supervisionado tradicional (que exige rótulos manuais caros criados por pessoas) nem com o aprendizado não supervisionado puro (que apenas agrupa dados sem calcular erros de predição em relação a um alvo). A auto-supervisão formula uma tarefa supervisionada artificial utilizando dados não anotados.

Diferencia-se do aprendizado supervisionado tradicional (que exige rótulos manuais custosos) e do aprendizado não supervisionado puro (que apenas agrupa dados sem objetivo preditivo explícito).

## 🧩 Problema que resolve

Resolve o **gargalo de rotulagem de dados** (*labeling bottleneck*). No aprendizado supervisionado da década de 2010 (como o ImageNet ou classificadores clássicos), rotular milhões de exemplos custava milhões de dólares e meses de trabalho humano. Esse custo impedia os modelos de escalarem para trilhões de exemplos. A auto-supervisão permite consumir toda a massa textual pública existente na internet com custo zero de anotação manual primária.

Resolve o "gargalo de rotulação de dados", superando a barreira financeira e temporal imposta pela necessidade de seres humanos criarem gabaritos manuais para treinar redes neurais em larga escala.

## 💡 Intuição

Pense em uma criança que aprende a falar ouvindo conversas à sua volta. Ninguém fica entregando cartões com definições formais para ela o tempo todo. Seu cérebro prevê constantemente qual será o próximo som ou palavra que os pais vão pronunciar. Se a previsão falhar, o cérebro se ajusta. A auto-supervisão replica essa mecânica cognitiva em escala de supercomputadores.

Imagine um livro em que todas as palavras finais de cada frase foram apagadas com corretivo. O estudante treina sua mente tentando adivinhar qual era a palavra apagada olhando o contexto anterior, aprendendo a gramática e os fatos do mundo sem precisar de um professor corrigindo exercício por exercício.

## ⚙️ Como funciona

O algoritmo extrai automaticamente pares de entrada e resposta a partir de qualquer fluxo de dados:

### Etapas

1. **Ingestão de dados brutos:** Coleta textos não estruturados (livros, páginas web, códigos-fonte).
2. **Criação de amostras de previsão:** Em uma sequência como `"Eu amo comida de rua"`, o sistema gera pares cumulativos de treino:
   - Entrada: `"<BOS>"` $\to$ Saída-alvo: `"Eu"`
   - Entrada: `"<BOS> Eu"` $\to$ Saída-alvo: `"amo"`
   - Entrada: `"<BOS> Eu amo"` $\to$ Saída-alvo: `"comida"`
   - Entrada: `"<BOS> Eu amo comida de rua"` $\to$ Saída-alvo: `"<EOS>"`
3. **Cálculo do erro:** O modelo prevê a saída e compara com o dado real ocultado.
4. **Retropropagação (*backpropagation*):** O gradiente do erro é propagado para ajustar os bilhões de parâmetros.

1. Coleta-se um corpus massivo de dados brutos não estruturados (ex: páginas da internet, livros).
2. O algoritmo mascara ou oculta partes estruturais dos dados (ex: o próximo token).
3. O modelo faz uma predição para preencher a lacuna oculta.
4. O resultado predito é comparado com o dado real original para calcular o erro e atualizar os pesos via gradiente descendente.

### Entradas e saídas

- **Entradas:** Texto puro contínuo não rotulado.
- **Saídas:** Milhares de exemplos de treinamento estruturados em pares de contexto e token-alvo.

- Entradas: Textos crus e não rotulados em grande volume.
- Saídas: Um modelo com pesos ajustados capaz de prever partes ocultas de dados subsequentes.

## 📐 Formulação matemática

Dado um corpus de texto sequencial $S = (w_1, w_2, \dots, w_N)$, a tarefa de auto-supervisão por predição do próximo token maximiza a verossimilhança logarítmica:

$$\mathcal{L}(\Theta) = \sum_{i=1}^{N} \log P(w_i \mid w_1, w_2, \dots, w_{i-1}; \Theta)$$

Onde:
- $\Theta$: Parâmetros (pesos) do modelo.
- $w_i$: Token atual na sequência.
- $\mathcal{L}(\Theta)$: Função de perda a ser maximizada ou minimizada.

Dada uma sequência arbitrária $X = (x_1, x_2, \dots, x_T)$, a função de perda auto-supervisionada minimiza a divergência entre a predição e o dado original sem vetor de anotação externo $Y$:

$$\min_\theta \mathbb{E}_{X \sim \mathcal{D}} \left[ \sum_{t=1}^T \mathcal{L}\Big(f_\theta(x_{<t}), x_t\Big) \right]$$

Onde a própria amostra $x_t$ atua simultaneamente como dado e gabarito formal de supervisão.

## 🧱 Hipóteses e condições de validade

- O volume de dados brutos deve ser massivo (na ordem de trilhões de tokens) para compensar a menor densidade de informação de cada exemplo comparado a rótulos manuais refinados.
- A distribuição dos dados brutos deve refletir os domínios de conhecimento e padrões que se deseja que o modelo assimile.

- Hipótese de que os dados brutos disponíveis na internet contêm regularidades estatísticas suficientes para o aprendizado de representações complexas de mundo e linguagem.

## ✅ Quando usar

- Fase primária de pré-treinamento de modelos de linguagem, modelos de visão e modelos multimodais de fundação.
- Adaptação de modelos de fundação para novos domínios por meio de pré-treino continuado (*continued pre-training*) com dados textuais brutos da empresa.

- No pré-treinamento de grandes modelos de fundação onde há abundância de dados não rotulados e escassez de dados rotulados por humanos.

## 🚫 Quando não usar

- Ajuste final de comportamento conversacional e alinhamento de segurança, onde exemplos pedagógicos de conduta ética e respeito a instruções exigem anotação e julgamento humano obrigatório ([[redes/ai-engineering/conceitos/finetuning.md|ajuste fino]]).

- Ajuste final de comportamento conversacional e alinhamento de segurança, onde exemplos pedagógicos de conduta ética e respeito a instruções exigem anotação e julgamento humano obrigatório ([[redes/ai-engineering/conceitos/ajuste-fino.md|ajuste fino]]).

- Em cenários com dados extremamente restritos, confidenciais ou de baixíssimo volume onde abordagens supervisionadas diretas ou heurísticas baseadas em regras sejam suficientes.

## ⚠️ Limitações e armadilhas

- **Absorção indiscriminada de vícios:** Como o modelo aprende com tudo o que lê via auto-supervisão, ele assimila desinformação, preconceitos, termos tóxicos e erros conceituais presentes na internet aberta.
- **Otimização de completação e não de conversa:** A auto-supervisão ensina o modelo a completar frases como se fosse uma página web, e não a dialogar utilmente como um assistente educado.

- Absorção de vieses, preconceitos, fake news e conteúdos tóxicos presentes nos dados crus da internet.
- Custo computacional massivo para processamento em escala de trilhões de tokens.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[auto-supervisão|Auto-supervisão]] | Aprender padrões preditivos extraindo rótulos dos próprios dados. | Dados brutos não rotulados. | Modelo ajustado preditivamente. | Dispensa rotulação humana explícita. |
| [[aprendizado-supervisionado|Aprendizado Supervisionado]] | Mapear entradas para saídas pré-determinadas. | Pares de (Entrada, Rótulo Humano). | Modelo preditivo classificador/regressor. | Depende estritamente de rótulos manuais criados por humanos. |

| Paradigma | Origem do Rótulo (*Label*) | Custo por Exemplo | Escala Viável |
|---|---|---|---|
| **Supervisionado** | Anotador humano especialista | Alto (centavos a dólares) | Milhares a milhões de dados |
| **Não Supervisionado** | Sem rótulos (agrupamento puro) | Zero | Ilimitada |
| **Auto-supervisionado** | Derivado internamente do dado | Zero | Trilhões de tokens (escala de internet) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma biblioteca digital possui 1 milhão de artigos científicos em formato de texto sem qualquer classificação temática.

- *Abordagem supervisionada:* Exigiria que bibliotecários lessem e catalogassem manualmente cada artigo em áreas e subáreas antes de treinar qualquer modelo.
- *Abordagem auto-supervisionada:* O sistema consome diretamente os artigos; quebra as frases em predição da próxima palavra e, nesse processo de adivinhar termos técnicos subsequentes, a rede neural aprende terminologias de física, química e biologia por pura regularidade estatística.

Pegando a frase "O cão correu atrás do...", o modelo usa a própria continuação real do documento ("...gato") como gabarito automático para ajustar sua rede neural, repetindo esse processo bilhões de vezes com textos da internet.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Complementos

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/modelo-de-linguagem-mascarado.md|Modelo de Linguagem Mascarado]]

- [[modelo-de-linguagem|Modelo de Linguagem]]

### Alternativas

- Aprendizado supervisionado com rótulos manuais clássicos.

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/finetuning.md|Ajuste Fino (Finetuning)]]

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

- [[modelo-de-fundacao|Modelo de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 6–8
- **Evidência:** Chip Huyen explica como a auto-supervisão rompeu o gargalo de rotulagem do aprendizado supervisionado (como no ImageNet), permitindo a expansão dos modelos para conjuntos de dados de trilhões de tokens sem custo de anotação manual.
- **Confiança:** Alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Explicação detalhada de como a auto-supervisão viabilizou a escala de modelos de linguagem ao eliminar a necessidade de rótulos manuais.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. Como a auto-supervisão supera o histórico "gargalo de rotulagem de dados" da inteligência artificial?
2. De que forma uma frase simples de cinco palavras pode gerar múltiplos exemplos de treinamento auto-supervisionado?
3. Qual é a distinção técnica formal entre aprendizado auto-supervisionado e aprendizado não supervisionado?
4. Por que a auto-supervisão é o motor fundamental por trás da escala dos Large Language Models (LLMs)?
5. Quais são as desvantagens de treinar um modelo exclusivamente via auto-supervisão com textos da internet aberta?
6. Como o conceito de auto-supervisão se aplica ao treinamento de modelos multimodais de imagem e texto?
7. Por que um modelo puramente auto-supervisionado precisa passar por etapas posteriores de ajuste fino para atuar como assistente conversacional?

1. O que é Auto-supervisão?
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
