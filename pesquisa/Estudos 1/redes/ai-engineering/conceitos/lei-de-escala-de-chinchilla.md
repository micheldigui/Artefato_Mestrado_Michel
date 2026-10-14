# 🧠 Lei de Escala de Chinchilla

**Rede:** `ai-engineering`  
**Área:** `dimensionamento-computacional`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Entendendo Modelos de Fundação
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

Uma diretriz empírica de dimensionamento estabelecida pela DeepMind que determina a proporção matemática ótima entre o número de parâmetros de um modelo de linguagem e o volume de tokens de treinamento para um orçamento fixo de computação (*FLOPs*).

### Em linguagem simples

É a regra matemática que diz exatamente quantos textos um modelo precisa ler para que o dinheiro gasto treinando seus parâmetros valha a pena, provando que muitos modelos antigos eram "grandes demais para poucos dados".

### Escopo danoso/distinções

Aplica-se estritamente ao treinamento ótimo de modelos densos a partir do zero. Não substitui métricas de ajuste fino posterior (*finetuning*).

## 🧩 Problema que resolve

Resolve o desperdício histórico de recursos em inteligência artificial onde equipes criavam modelos gigantescos com poucos dados de leitura, provando que o volume de dados precisava crescer na mesma proporção que os parâmetros.

## 💡 Intuição

Não adianta construir uma biblioteca gigante se você comprar apenas três livros para colocar nas prateleiras; da mesma forma, um modelo com bilhões de parâmetros precisa ler dezenas de bilhões de palavras para preencher sua capacidade de aprendizado.

## ⚙️ Como funciona

### Etapas

1. Define-se o orçamento computacional total disponível em FLOPs.
2. Utiliza-se a equação de Chinchilla para calcular a alocação ideal dividida estritamente entre o tamanho do modelo ($N$) e o volume de tokens ($D$).
3. Executa-se o pré-treinamento equilibrado.

### Entradas e saídas

- Entradas: Orçamento computacional total disponível.
- Saídas: Número ótimo de parâmetros do modelo e número ótimo de tokens de treinamento.

## 📐 Formulação matemática

A relação empírica proposta no estudo de Chinchilla estabelece que o modelo ótimo para um orçamento de computação $C$ escala em proporção igual:

$$N \propto C^{0.5}, \quad D \propto C^{0.5}$$

Na prática, a proporção recomendada para treinamento computacionalmente ótimo (*compute-optimal*) é de aproximadamente **20 tokens para cada 1 parâmetro**:

$$D \approx 20 \times N$$

Onde:
- $N$: Número de parâmetros do modelo.
- $D$: Número de tokens no corpus de treinamento.
- $C$: Orçamento total de computação em FLOPs.

## 🧱 Hipóteses e condições de validade

- Válido para arquiteturas densas tradicionais baseadas em Transformers treinadas com distribuições padronizadas de dados na internet.

## ✅ Quando usar

- No planejamento do projeto de pré-treinamento de novos modelos de linguagem do zero.

## 🚫 Quando não usar

- Em estratégias de ajuste fino (*finetuning*) ou adaptação baseada em PEFT, onde o modelo base já foi previamente treinado.

## ⚠️ Limitações e armadilhas

- A proporção ótima pode mudar com a inclusão massiva de dados sintéticos ou novas arquiteturas esparsas (*MoE*).

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[lei-de-escala-de-chinchilla|Lei de Chinchilla]] | Definir proporção ótima entre parâmetros e tokens de treino. | Orçamento de computação (*FLOPs*). | Quantidade ótima de parâmetros e tokens. | Foca no dimensionamento equilibrado de pré-treinamento. |
| [[finetuning|Finetuning]] | Adaptar pesos de um modelo já existente a uma tarefa. | Modelo base + Dataset especializado. | Modelo especializado ajustado. | Modifica um modelo pronto e não treina do zero. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Se você planeja treinar um modelo de fundação com 7 bilhões de parâmetros, a Lei de Chinchilla estipula que você precisará alimentá-lo com aproximadamente 140 bilhões de tokens de texto de alta qualidade para extrair o máximo desempenho possível daquele investimento.

## 🔗 Relações no grafo

### Pré-requisitos

- [[modelo-de-fundacao|Modelo de Fundação]]

### Complementos

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Entendendo Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da lei de escala de Chinchilla e sua proporção de 20 tokens por parâmetro para treinamento ótimo.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que é Lei de Escala de Chinchilla?
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
*Nota gerada a partir do capítulo Capítulo 2 — Entendendo Modelos de Fundação. A interpretação final deve ser revisada pelo estudante.*
