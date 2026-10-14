# 🧠 Tokenização

**Rede:** `ai-engineering`  
**Área:** `processamento-de-linguagem-natural`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

O processo computacional de segmentação de um fluxo contínuo de texto em unidades menores discretas chamadas tokens, que servem como entradas fundamentais para modelos de linguagem baseados em redes neurais.

### Em linguagem simples

É o ato de fatiar uma frase em pedacinhos menores (que podem ser letras, palavras inteiras ou sílabas/partes de palavras) para que o computador consiga processar o texto numericamente.

### Escopo e distinções

Envolve algoritmos de divisão baseados em vocabulário fixo ou subpalavras (*subword tokenization*). Não se confunde com separação estrita por espaços em branco, pois gerencia palavras desconhecidas e sufixos eficientemente.

## 🧩 Problema que resolve

Resolve a impossibilidade de redes neurais processarem texto bruto diretamente como strings de caracteres contínuos, convertendo sequências textuais em sequências discretas tratáveis matematicamente.

## 💡 Intuição

Pense em um tradutor que pega uma palavra composta longa e complexa em alemão e a divide em blocos menores conhecidos para conseguir entender o significado combinado de cada parte.

## ⚙️ Como funciona

### Etapas

1. O texto de entrada bruto é recebido pelo tokenizador.
2. O texto é mapeado contra o vocabulário predefinido do modelo.
3. Palavras compostas ou raras são subdivididas em subpalavras conhecidas.
4. Cada token resultante é convertido em seu respectivo índice numérico inteiro.

### Entradas e saídas

- Entradas: String de texto bruta (ex: "I can't wait").
- Saídas: Sequência de identificadores numéricos de tokens.

## 📐 Formulação matemática

Seja $S$ uma string de texto contínua e $T$ o conjunto de regras de segmentação do vocabulário $V$, a tokenização mapeia $S$ em uma sequência ordenada de tokens discretos:

$$\text{Tokenize}(S) = (t_1, t_2, \dots, t_n), \quad t_i \in V$$

Onde cada $t_i$ possui um índice inteiro correspondente no vocabulário do modelo.

## 🧱 Hipóteses e condições de validade

- O vocabulário do tokenizador deve cobrir adequadamente os caracteres e padrões morfológicos do idioma de entrada para evitar proporções excessivas de tokens desconhecidos (`[UNK]`).

## ✅ Quando usar

- Obrigatoriamente em qualquer pipeline que prepare dados textuais para consumo por modelos de linguagem e redes neurais.

## 🚫 Quando não usar

- Não aplicável diretamente em dados puramente tabulares ou numéricos que não passem por representação textual sequencial.

## ⚠️ Limitações e armadilhas

- Eficiência variável entre idiomas: idiomas com menor representação no corpus de treino geram muito mais tokens para expressar a mesma ideia, elevando custos e latência computacional.
- Dificuldade com pontuações especiais, emojis e código compactado se o vocabulário não estiver otimizado.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[tokenizacao|Tokenização]] | Converter strings textuais em sequências de tokens numéricos. | String de texto bruto. | Sequência de tokens discretos. | Foco na fragmentação atômica do texto. |
| [[modelo-de-linguagem|Modelo de Linguagem]] | Estimar probabilidades de sequências de tokens. | Sequência de tokens. | Probabilidade / Próximo token. | Foco na predição estatística e não na fragmentação. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

A frase "I can't wait" é processada pelo tokenizador do GPT-4 e fatiada em pedaços distintos, onde a palavra contraída "can't" é inteligentemente dividida em dois tokens separados ("can" e "'t") para otimizar o vocabulário.

## 🔗 Relações no grafo

### Pré-requisitos

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Complementos

- [[modelo-de-linguagem|Modelo de Linguagem]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- [[modelo-de-fundacao|Modelo de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação conceitual do funcionamento de tokens e vocabulários, exemplificado pelo fracionamento de frases no GPT-4.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que é Tokenização?
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
