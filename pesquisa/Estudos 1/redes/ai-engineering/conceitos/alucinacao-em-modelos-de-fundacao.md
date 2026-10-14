# 🧠 Alucinação em Modelos de Fundação

**Rede:** `ai-engineering`  
**Área:** `modelagem`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 105, 107–111

## 📝 Definição

### Definição formal

A **Alucinação** (*Hallucination*) em modelos de fundação é a geração de conteúdo em linguagem natural ou multimodal que se apresenta de forma fluida, gramaticalmente impecável e persuasiva, mas que é factualmente incorreta, sem sustentação na realidade empírica ou desprovida de embasamento no contexto ou fontes explicitamente fornecidas na entrada.

As duas hipóteses teóricas fundamentais que explicam o fenômeno são:
1. **Hipótese da Auto-ilusão (*Self-delusion* / *Snowballing*):** Decorre da auto-supervisão autoregressiva, onde o modelo é incapaz de diferenciar premissas reais fornecidas no prompt de tokens inventados por ele mesmo; ao gerar uma primeira afirmação errônea, o modelo condiciona os passos futuros a esse erro, "auto-iludindo-se" para justificar a premissa falsa inicial.
2. **Hipótese da Divergência de Conhecimento Interno:** Decorre da fase de supervisão ([[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|SFT]]), onde o modelo é treinado para imitar respostas escritas por anotadores humanos que continham conhecimentos externos que os pesos internos do modelo pré-treinado não possuíam, ensinando a rede a "adivinhar e fingir convicção".

### Em linguagem simples

É quando a IA mente com convicção e elegância. O texto soa perfeito, mas ela inventou nomes, leis ou fatos que não existem no mundo real. Isso acontece porque o modelo é apenas um autocompletar estatístico sofisticado: se ele começar a inventar uma mentira, ele passa a acreditar na própria mentira nos parágrafos seguintes.

### Escopo e distinções

Não se confunde com "erro de lógica pura" ou bug de software convencional. A alucinação é um subproduto intrínseco da natureza probabilística e da amostragem estocástica que torna esses modelos criativos e úteis. Em tarefas artísticas, a alucinação é chamada de "criatividade"; em tarefas jurídicas, médicas ou financeiras, é uma falha crítica de integridade.

## 🧩 Problema que resolve

Compreender as causas da alucinação resolve o problema de diagnóstico de falhas em sistemas de produção. Em vez de tentar "eliminar a alucinação" com comandos ingênuos no prompt ("Por favor, não minta"), o engenheiro de IA adota medidas arquiteturais sistêmicas de contenção: ancoragem factual ([[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]]), amostragem com verificadores externos ([[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|test time compute]]) e supervisão por [[redes/ai-engineering/conceitos/humano-no-loop.md|humano no loop]].

## 💡 Intuição

Pense em um contador de histórias que começa a mentir em uma roda de amigos. Ele inventa sem querer que esteve na França semana passada. Em vez de parar, quando alguém pergunta como era o hotel, ele é obrigado a inventar o nome do hotel, a cor do quarto e o que comeu no café da manhã para não se contradizer. Cada detalhe novo inventado ancora-se na mentira anterior (**efeito bola de neve da auto-ilusão**).

## ⚙️ Como funciona

O mecanismo autorregressivo favorece a amplificação de pequenos desvios:

### Etapas

1. **Geração do Desvio Inicial:** Por amostragem probabilística ou ausência de dados de contexto, o modelo emite um primeiro token factualmente desconectado (ex.: `"Chip Huyen é uma arquiteta"`).
2. **Incorporação ao Histórico:** Esse token é anexado à sequência de entrada para a etapa de decode seguinte: `["Quem", "é", "Chip", "Huyen?", "Chip", "Huyen", "é", "uma", "arquiteta"]`.
3. **Condicionamento Autoregressivo Cego:** A atenção processa o histórico consolidado. O modelo não tem uma etiqueta interna que diga "fui eu que acabei de inventar a palavra arquiteta". Ele a trata com a mesma autoridade de um fato histórico consumido da Wikipedia.
4. **Efeito Bola de Neve (*Snowballing*):** Os próximos tokens buscam maximizar a probabilidade condicional dado que ela é arquiteta, gerando: `"renomada que desenhou pontes famosas no Vietnã"`.
5. **Apresentação Confiante:** O resultado final é entregue sem qualquer marcador de incerteza nativa.

### Entradas e saídas

- **Entradas:** Prompt do usuário sem evidência explícita suficiente ou que exige conhecimento que o modelo não assimilou.
- **Saídas:** Resposta longa, gramaticalmente fluida e estruturada, porém completamente inventada.

## 📐 Formulação matemática

Em um modelo autoregressivo, a probabilidade conjunta da sequência é:

$$P(y_1, y_2, \dots, y_T \mid x) = \prod_{t=1}^T P(y_t \mid x, y_{<t})$$

Se em $t=1$ o modelo amostra um evento de erro $y_1 = e_1$, toda a distribuição subsequente é condicionada ao erro:

$$P(y_t \mid x, e_1, y_2, \dots, y_{t-1})$$

Como $P(y_t \mid x, e_1) \neq P(y_t \mid x, y_{\text{fato}})$, a probabilidade de ocorrência de novos erros cresce monotonicamente:

$$P(\text{erro em } t \mid \text{erro em } t-1) \gg P(\text{erro em } t \mid \text{acerto em } t-1)$$

## 🧱 Hipóteses e condições de validade

- Como os modelos de fundação operam através de compressão de perda (*lossy compression*) de dados da internet, a alucinação é um fenômeno estrutural inevitável sob abordagens puramente probabilísticas não ancoradas externamente.

## ✅ Quando usar

- O estudo do mecanismo de alucinação deve ser utilizado na concepção de matrizes de risco, limites de tolerância de erro e testes de segurança de produtos de IA.

## 🚫 Quando não usar

- Nunca assumir que um modelo alinhado por RLHF ou DPO está livre de alucinações; o estudo do InstructGPT demonstrou que o RLHF chegou a piorar a alucinação factual em certos casos, pois priorizou a simpatia e a extensão da resposta sobre a exatidão crua.

## ⚠️ Limitações e armadilhas

- **Prompts ingênuos de desencorajamento:** Incluir frases como `"Seja $100\%$ verdadeiro e nunca invente nada"` reduz marginalmente alucinações superficiais, mas falha totalmente quando o modelo sofre o efeito de auto-ilusão em textos longos.
- **Confiabilidade no tom de voz:** Usuários humanos tendem a confiar em respostas bem pontuadas e prolixas, tornando as alucinações de LLMs ordens de magnitude mais perigosas do que erros óbvios de sistemas tradicionais.

## 🔍 Comparações

| Hipótese de Alucinação | Causa Raiz | Momento de Origem | Estratégia de Mitigação |
|---|---|---|---|
| **Auto-ilusão (*Snowballing*)** | Condicionamento autorregressivo sobre erros próprios | Tempo de inferência (Decode) | Prompts concisos, RAG, Verificadores |
| **Divergência de Conhecimento** | Treinar com respostas que o modelo base desconhece | Pós-treinamento (SFT) | Curadoria que respeita os dados de pré-treino |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O caso clássico dos advogados de Nova York multados pela corte em 2023:
Os advogados usaram o ChatGPT para redigir uma petição jurídica sobre um acidente em uma companhia aérea. O modelo começou citando um processo imaginário: `"Varghese v. China Southern Airlines"`. 
A partir desse primeiro erro, o efeito de bola de neve fez o modelo inventar o número do processo, o nome do juiz fictício, citações textuais de jurisprudência inexistente e a data da audiência. O texto tinha jargão jurídico perfeito e convenceu os advogados, que apresentaram a peça ao tribunal sem checar se o processo existia de verdade nos arquivos da Justiça.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]

### Complementos

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]] (estratégia primária de mitigação)
- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (trata-se de uma propriedade emergente do sistema).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/pos-treinamento-e-alinhamento.md|Pós-Treinamento e Alinhamento]]
- [[redes/ai-engineering/conceitos/humano-no-loop.md|Humano no Loop (Crawl-Walk-Run)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 105, 107–111
- **Evidência:** Chip Huyen aborda a natureza probabilística da IA e disseca as duas hipóteses científicas da alucinação: a hipótese de auto-ilusão da DeepMind (Ortega et al., 2021) e de Zhang et al. (2023), e a hipótese do descompasso de conhecimento interno do modelo versus anotadores (Leo Gao e John Schulman da OpenAI).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é alucinação em modelos de fundação e por que ela não se confunde com erros tradicionais de lógica de software?
2. Como funciona a hipótese da auto-ilusão (*self-delusion*) e o efeito de bola de neve (*snowballing*) em modelos autorregressivos?
3. De que forma a prática de anotação humana na etapa de SFT pode forçar o modelo a aprender a alucinar?
4. Por que exigir que a IA gere respostas concisas tende empiricamente a diminuir a taxa de alucinação?
5. Qual foi o resultado inesperado apresentado no artigo do InstructGPT sobre a relação entre RLHF e alucinações factuais?
6. Como a implementação do padrão arquitetural de RAG atua diretamente no bloqueio do mecanismo de alucinação?
7. Por que o tom de voz confiante e a gramática fluida de um modelo de fundação tornam a alucinação especialmente perigosa em contextos corporativos regulados?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.


*Nota gerada a partir do capítulo Capítulo 2 — Understanding Foundation Models. A interpretação final deve ser revisada pelo estudante.*
