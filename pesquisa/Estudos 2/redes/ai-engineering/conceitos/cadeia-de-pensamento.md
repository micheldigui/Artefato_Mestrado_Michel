# 🧠 Cadeia de Pensamento (Chain-of-Thought / CoT)

**Rede:** `ai-engineering`  
**Área:** `engenharia-de-prompt`

**Rede:** `ai-engineering`   **Área:** `desenvolvimento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 5 — Engenharia de Prompt
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 5 — Prompt Engineering
- Localização: Páginas 227–229

## 📝 Definição

### Definição formal

Uma técnica de engenharia de prompt que induz um modelo de linguagem a gerar uma série de passos intermediários de raciocínio lógico antes de produzir a resposta final para um problema complexo.

A **Cadeia de Pensamento** (*Chain-of-Thought* — CoT) é uma técnica de engenharia de prompt (Wei et al., 2022) que condiciona o modelo de linguagem autorregressivo a externalizar uma sequência encadeada de passos lógicos intermediários de raciocínio antes de emitir a resposta final para uma consulta, aumentando a precisão em tarefas que demandam múltiplos estágios de inferência (como matemática, lógica formal e raciocínio simbólico).

Apresenta-se sob duas modalidades canônicas:

1. **Zero-Shot CoT:** Estimulado pela adição de frases de ancoragem genéricas no prompt (como `"Pense passo a passo"` ou `"Explique suas razões antes de concluir"`);
2. **Few-Shot / One-Shot CoT:** Guiado por demonstrações explícitas contendo o desenvolvimento do raciocínio analítico intermediário.

### Em linguagem simples

É a instrução dada à IA para que ela "faça as contas no rascunho" ou explique seu raciocínio passo a passo antes de dar o resultado definitivo.

É a técnica de forçar a IA a "fazer a conta no rascunho" antes de dar a resposta definitiva. Se você pedir a uma pessoa para calcular de cabeça uma conta de multiplicação de três dígitos instantaneamente, ela provavelmente vai errar. Mas se você der papel e caneta e pedir para ela calcular passo a passo, ela acertará com facilidade. O CoT dá esse "espaço de rascunho" na tela para o modelo pensar.

### Escopo e distinções

Diferencia-se de prompts de resposta direta (*direct answering*): em vez de forçar o modelo a saltar direto para o resultado final, o CoT aloca espaço na janela de contexto para cálculos intermediários.

Não se confunde com o treinamento ou ajuste de parâmetros. O CoT opera em tempo de inferência puramente textual. Cada token de raciocínio gerado atua como contexto autoregressivo para o cálculo do próximo passo, diminuindo saltos lógicos perigosos. Conecta-se também à técnica de **auto-crítica (*self-critique*)**, onde o modelo revisa seu próprio raciocínio antes da entrega.

## 🧩 Problema que resolve

Resolve a incapacidade de modelos de resolver problemas complexos de matemática, lógica e programação quando solicitados a entregar a resposta final de forma instantânea sem processamento intermediário.

Resolve a alta taxa de erro dos modelos autorregressivos em tarefas que exigem planejamento e múltiplos passos dedutivos. Como os LLMs alocam uma quantidade fixa de processamento para emitir cada token individual, tentar saltar diretamente de uma premissa complexa para a resposta final forçava o modelo a "adivinhar" o resultado em um único passo, causando falhas graves e alucinações de lógica.

## 💡 Intuição

Pedir para um aluno resolver mentalmente uma equação algébrica complexa e dar só o número final costuma gerar erros; pedir para ele anotar cada etapa da fórmula em um papel garante que o resultado final esteja correto.

Pense em um detetive investigando um crime:

- Se ele olhar para a cena do crime e gritar imediatamente: `"O culpado é o mordomo!"` (**tentativa direta sem CoT**), a chance de ele cometer uma injustiça é enorme.
- Mas se ele externalizar o raciocínio: `"A porta estava trancada por dentro; logo, o autor tinha a chave. Apenas três pessoas tinham a chave: o mordomo, o herdeiro e a cozinheira. A cozinheira tem um álibi confirmado; o herdeiro estava fora da cidade... portanto, o culpado é o mordomo"` (**Cadeia de Pensamento**), o encadeamento dedutivo torna a conclusão quase à prova de falhas.

## ⚙️ How it works / Como funciona

### Etapas

1. O desenvolvedor insere uma diretriz explícita no prompt (ex: "Pense passo a passo" ou "Explique seu raciocínio antes de responder").
2. O modelo de linguagem gera o primeiro passo lógico do problema como um token subsequente.
3. Utilizando o primeiro passo gerado como contexto, o modelo gera o segundo passo, e assim sucessivamente.
4. O modelo sintetiza a conclusão final com base em toda a cadeia lógica construída nas etapas anteriores.

### Entradas e saídas

- Entradas: Problema complexo + Instrução de decomposição lógica (*CoT*).
- Saídas: Cadeia textual de raciocínio intermediário seguida pela resposta final.

## 📐 Formulação matemática

Dado um problema $x$, o modelo não gera diretamente $y$, mas sim uma sequência latente de passos intermediários $z = (z_1, z_2, \dots, z_k)$ antes de gerar a resposta $y$:

$$P(y, z \mid x) = \prod_{i=1}^{k} P(z_i \mid x, z_{1}, \dots, z_{i-1}) \cdot P(y \mid x, z)$$

Onde:
- $z$: Passos intermediários de raciocínio (*Chain-of-Thought*).
- $y$: Resposta final sintetizada após o encadeamento.

Seja $x$ a pergunta e $y$ a resposta final. Na amostragem padrão sem CoT, o modelo calcula diretamente $P(y \mid x)$.
Com a Cadeia de Pensamento, introduz-se uma variável latente de passos de raciocínio intermediários $Z = (z_1, z_2, \dots, z_M)$:

$$P(y \mid x) = \sum_{Z} P(y \mid x, Z) P(Z \mid x) \approx P(y \mid x, Z^*) P(Z^* \mid x)$$

Onde $Z^*$ é a trajetória de raciocínio de alta probabilidade gerada sequencialmente:

$$P(Z^* \mid x) = \prod_{m=1}^M P(z_m \mid x, z_{<m})$$

O artigo seminal de Wei et al. (2022) demonstrou aumentos massivos de desempenho no benchmark de matemática escolar GSM-8K para modelos de grande escala (como PaLM e LaMDA), comprovando também que o CoT é uma capacidade emergente que só traz retornos robustos em modelos com dezenas de bilhões de parâmetros.

## 🧱 Hipóteses e condições de validade

- Supõe que o modelo possui conhecimento básico suficiente sobre as regras do domínio para desmembrar o problema em etapas coerentes.

- Efeito concentrado em modelos de alta capacidade (geralmente $\ge 50\text{B}$ parâmetros); em modelos muito pequenos (como $1\text{B}$ ou $3\text{B}$), forçar o CoT pode paradoxalmente degradar a acurácia, pois o modelo inventa desculpas ilógicas no meio do raciocínio.

## ✅ Quando usar

- Em tarefas de raciocínio lógico, resolução de problemas matemáticos, lógica de programação e tomadas de decisão corporativas multifacetadas.

- Problemas de matemática, física, cálculo financeiro e lógica formal.
- Depuração e geração de algoritmos de programação de software.
- Tarefas de decisão complexa onde a auditoria humana exige que o sistema explique a justificativa do parecer emitido.

## 🚫 Quando não usar

- Em perguntas triviais de recuperação de fatos diretos (ex: "Qual a capital do Brasil?"), pois o CoT adiciona latência e custo desnecessários de tokens.

- Em tarefas simples de extração direta de fatos (ex.: `"Qual é a capital da Itália?"`), onde forçar o modelo a pensar passo a passo apenas consome tokens desnecessários e adiciona latência inútil.

## ⚠️ Limitações e armadilhas

- Aumenta o consumo de tokens de saída e eleva a latência geral de resposta (*TPOT*).
- Risco de o modelo gerar passos intermediários com falhas lógicas (*alucinação de raciocínio*), o que corrompe a conclusão final.

- **Aumento exponencial de tokens e latência:** A IA precisa gerar dezenas ou centenas de tokens de "pensamento" antes de entregar a resposta final, elevando os custos de saída (*TPOT*) e o tempo de espera do usuário.
- **Racionalização de erros (*Confabulação pós-hoc*):** Se o modelo adotar uma premissa falsa no primeiro passo do CoT, ele usará todo o restante da cadeia de pensamento para inventar justificativas lógicas sofisticadas para defender a resposta errada.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[cadeia-de-pensamento|Chain-of-Thought (CoT)]] | Induzir passos intermediários de raciocínio lógico. | Pergunta complexa + Instrução de passo a passo. | Rascunho lógico + Resposta final. | Força o modelo a desmembrar a lógica em etapas textuais. |
| [[resposta-direta|Resposta Direta (Zero-Shot)]] | Obter a resposta final de forma instantânea. | Pergunta direta. | Apenas a resposta final. | Sem processamento intermediário explícito exposto. |

| Modalidade de Prompt | Mecânica de Execução | Custo de Tokens | Precisão em Raciocínio |
|---|---|---|---|
| **Padrão Direto** | Emite a resposta imediatamente | Mínimo | Baixa a Média |
| **Zero-Shot CoT** | Adiciona `"Pense passo a passo"` | Moderado | Alta |
| **Few-Shot CoT** | Fornece 3 a 5 exemplos completos com rascunho | Mais Alto | **Máxima** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Perguntar: "Se comprei 3 maçãs por R$ 2 cada e dei uma nota de R$ 10, quanto recebo de troco? Pense passo a passo". A IA escreverá: 1) Custo total = 3 x 2 = 6; 2) Troco = 10 - 6 = 4; Resposta final: R$ 4.

Problema: `"A lanchonete tinha 23 maçãs. Usou 20 no almoço e comprou mais 6. Quantas maçãs restam?"`.

- *Sem CoT:* O modelo tenta chutar o número final direto e pode responder erroneamente: `"9"`.
- *Com CoT:* O modelo gera a cadeia:

`"1. A lanchonete começou com 23 maçãs."` `"2. Usou 20 no almoço: 23 - 20 = 3 maçãs restantes."` `"3. Comprou mais 6: 3 + 6 = 9 maçãs."` `"Resposta final: 9 maçãs."` O encadeamento passo a passo ancora o cálculo aritmético em cada posição, garantindo a correção.

## 🔗 Relações no grafo

### Pré-requisitos

- [[aprendizado-em-contexto|Aprendizado em Contexto]]

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

- [[redes/ai-engineering/conceitos/aprendizado-em-contexto.md|Aprendizado em Contexto (In-Context Learning)]]
- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

- Resposta direta de passagem única (*Direct Zero-Shot*).

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

- [[redes/ai-engineering/conceitos/decomposicao-e-encadeamento-de-prompts.md|Decomposição e Encadeamento de Prompts]]
- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 5 — Engenharia de Prompt
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da técnica Chain-of-Thought (CoT) para elicitação de raciocínio passo a passo em modelos de linguagem.
- **Confiança:** alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 5 — Prompt Engineering
- **Localização:** Páginas 227–229
- **Evidência:** Chip Huyen discute o artigo pioneiro de Wei et al. (2022) sobre Chain-of-Thought, apresenta a Tabela 5-4 com variações de prompts (zero-shot CoT, one-shot CoT), analisa o caso do LinkedIn comprovando que o CoT reduz alucinações e adverte sobre o trade-off crítico de latência e consumo de tokens.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Cadeia de Pensamento (Chain-of-Thought / CoT)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

1. O que é a técnica de Cadeia de Pensamento (*Chain-of-Thought* — CoT) e qual problema fundamental ela resolve?
2. Como a formulação probabilística da decodificação autoregressiva explica o sucesso do CoT em tarefas lógicas?
3. Qual é a diferença operacional entre as abordagens de Zero-Shot CoT e Few-Shot CoT?
4. Por que o CoT é considerado uma capacidade emergente que se manifesta prioritariamente em modelos de grande escala?
5. Quais são as penalidades de latência e de custo de tokens acarretadas pela imposição de respostas passo a passo?
6. De que maneira a técnica de auto-crítica (*self-critique*) complementa o fluxo de raciocínio do CoT?
7. Como a equipe de engenharia do LinkedIn utilizou o CoT para mitigar alucinações em suas aplicações corporativas?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 5 — Engenharia de Prompt. A interpretação final deve ser revisada pelo estudante.*

## ⚙️ Como funciona

O processo atua explorando a mecânica causal de decodificação sequencial:

### Etapas

1. **Injeção do Gatilho Lógico:** O prompt inclui a ordem explícita de desdobramento (ex.: `"Pense passo a passo antes de chegar à resposta"`).
2. **Geração do Rascunho Intermediário:** O modelo emite os primeiros tokens decompondo o problema em premissas simples (passo 1, passo 2, passo 3).
3. **Condicionamento da Atenção:** Conforme cada passo é redigido, ele passa a integrar o histórico acumulado de contexto. A atenção da rede neural agora atende a passos lógicos já validados na tela, e não apenas ao enunciado bruto.
4. **Emissão da Conclusão:** O modelo chega ao resultado final condicionado a um histórico de alta coerência matemática ou dedutiva.

### Entradas e saídas

- **Entradas:** Problema dedutivo e uma diretriz ou demonstração de raciocínio passo a passo.
- **Saídas:** Texto estruturado contendo a justificativa intermediária explícita e a conclusão final correta.
