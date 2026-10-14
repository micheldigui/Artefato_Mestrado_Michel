# 🧠 Pós-Treinamento e Alinhamento

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 78–80

## 📝 Definição

### Definição formal

O **Pós-Treinamento e Alinhamento** (*Post-Training and Alignment*) é o estágio do ciclo de desenvolvimento de modelos de fundação que sucede o pré-treinamento auto-supervisionado, cujo objetivo é transformar uma máquina de predição estatística de próximo token em um assistente conversacional seguro, coerente e obediente a instruções, através da calibração comportamental de suas respostas frente às expectativas, restrições éticas e preferências dos usuários humanos. 

Estrutura-se convencionalmente em duas fases sequenciais:
1. **Ajuste Fino Supervisionado** ([[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|SFT]]);
2. **Ajuste Fino de Preferência** ([[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|RLHF]] ou [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia.md|DPO]]).

### Em linguagem simples

É a etapa de "educação e boas maneiras" da IA. O pré-treinamento faz o modelo ler a biblioteca inteira da internet e absorver fatos e linguagem, mas o modelo ainda age como uma criatura caótica e bruta que apenas completa frases aleatórias. O pós-treinamento ensina esse cérebro a conversar educadamente, seguir ordens, recusar pedidos perigosos e formatar as respostas do jeito que as pessoas gostam.

### Escopo e distinções

Consome uma fração diminuta da computação total de treinamento (no InstructGPT, o pós-treino utilizou apenas $2\%$ da computação total, enquanto o pré-treino consumiu $98\%$). Não tem a função primária de ensinar novos conhecimentos factuais (que devem ser adquiridos no pré-treino ou via RAG), mas de desbloquear e canalizar o conhecimento latente pré-existente.

## 🧩 Problema que resolve

Resolve os dois males fundamentais de um modelo puramente pré-treinado:
1. **Inaptidão conversacional:** Se você envia `"Como fazer uma pizza?"` para um modelo puramente pré-treinado, ele pode completar com `"para uma família de seis pessoas?"` ou `"Ingredientes necessários:"` em vez de fornecer a instrução culinária, pois foi treinado apenas para autocompletar documentos da web.
2. **Toxicidade e perigo operacional:** Textos da internet contêm misoginia, racismo, manuais de fabricação de armas e receitas de venenos. O alinhamento molda os filtros éticos e de conformidade do modelo.

## 💡 Intuição

O capítulo utiliza a célebre metáfora visual do meme do monstro **Shoggoth com uma máscara sorridente**:
- O pré-treino gera o monstro cósmico incompreensível e selvagem (o Shoggoth), repleto de todo o conhecimento caótico da internet.
- O SFT veste esse monstro com roupas sociais humanas, ensinando-o a sentar à mesa e falar nossa língua.
- O alinhamento de preferência (RLHF/DPO) coloca a máscara sorridente no monstro, ensinando-o a sorrir para os clientes, ser polido e evitar assustar as pessoas.

## ⚙️ Como funciona

O pipeline divide as tarefas em níveis crescentes de refinamento:

### Etapas

1. **Modelo Base Pré-Treinado:** Ponto de partida com bilhões de parâmetros treinados via auto-supervisão.
2. **Ajuste Fino Supervisionado ([[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|SFT]]):** Treinamento do modelo com pares `(prompt, resposta_ideal)` escritos ou revisados por humanos de alta qualificação educacional para clonar o comportamento de assistente.
3. **Alinhamento de Preferência:** Treinamento que otimiza a resposta em nível de texto completo (e não de token isolado) utilizando comparação de respostas (`melhor` vs. `pior`):
   - Via modelo de recompensa e aprendizado por reforço ([[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|RLHF]]);
   - Ou via otimização direta da política ([[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia.md|DPO]]).
4. **Disponibilização do Modelo Instruído (*Instruct/Chat*):** O modelo final é congelado para consumo seguro na camada de aplicação.

### Entradas e saídas

- **Entradas:** Checkpoint pré-treinado bruto, conjuntos de dados de instrução e conjuntos de dados de preferências pareadas.
- **Saídas:** Um modelo alinhado (*aligned model*) configurado para aceitar comandos de usuários com baixa taxa de refutação indevida ou respostas danosas.

## 📐 Formulação matemática

O pré-treinamento minimiza o erro no nível de token individual. O pós-treinamento maximiza a utilidade esperada da trajetória completa da resposta $y$ dada a instrução $x$ sob uma função de valor ou preferência humana $R(x, y)$:

$$\max_\theta \mathbb{E}_{x \sim \mathcal{D}, y \sim \pi_\theta(\cdot \mid x)} \Big[ R(x, y) \Big] - \beta \, \mathbb{D}_{\text{KL}}\Big(\pi_\theta(y \mid x) \;\big\|\; \pi_{\text{ref}}(y \mid x)\Big)$$

Onde a penalidade de divergência de Kullback-Leibler ($\mathbb{D}_{\text{KL}}$) em relação ao modelo de referência original $\pi_{\text{ref}}$ impede que o alinhamento distorça a linguagem do modelo a ponto de destruir sua capacidade de fala natural.

## 🧱 Hipóteses e condições de validade

- Assume que as preferências dos rotuladores contratados refletem de maneira representativa ou aceitável os valores e normas desejadas pelos usuários finais da aplicação.
- O modelo pré-treinado deve possuir conhecimento de base suficiente; o alinhamento não consegue compensar a ausência completa de fatos pré-existentes na rede.

## ✅ Quando usar

- Essencial na criação de modelos comerciais de conversação, assistentes de código e sistemas de suporte ao cliente.
- Ao construir versões especializadas de modelos abertos que precisam respeitar políticas rígidas de compliance corporativo.

## 🚫 Quando não usar

- Em pesquisas teóricas de modelagem pura de linguagem ou tarefas que exigem completação crua e não filtrada de sequências literárias.

## ⚠️ Limitações e armadilhas

- **Taxa de alinhamento (*Alignment Tax*):** Modelos alinhados excessivamente podem sofrer quedas sutis em tarefas de criatividade pura ou raciocínio não convencional, ou tornar-se tediosos e repetitivos.
- **Recusas falsas (*False Refusals*):** O modelo pode se tornar excessivamente cauteloso e recusar responder perguntas perfeitamente legítimas por confundi-las superficialmente com solicitações perigosas.

## 🔍 Comparações

| Dimensão | Pré-Treinamento | Pós-Treinamento (Alinhamento) |
|---|---|---|
| **Consumo de computação** | Maciço (~98% do total de FLOPs) | Diminuto (~2% do total de FLOPs) |
| **Mecanismo de supervisão** | [[redes/ai-engineering/conceitos/auto-supervisao.md\|Auto-supervisão]] em dados brutos | Instrução supervisionada e preferência |
| **Objetivo primário** | Aquisição de conhecimento e gramática | Segurança, utilidade e adequação conversacional |
| **Comportamento resultante** | Máquina de completação textual | Assistente conversacional confiável |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um usuário digita o prompt: `"Como invadir a casa de alguém?"`.
- Um **modelo puramente pré-treinado** completa estatisticamente o texto como se fosse um romance policial: `"pela janela dos fundos, aproveitando que os donos estavam viajando"`.
- O mesmo modelo após **Pós-Treinamento e Alinhamento** avalia a restrição de segurança e responde de forma prestativa e ética: `"Não posso fornecer instruções para entrada não autorizada em propriedades. Se você foi trancado para fora de sua casa, recomendo contatar um chaveiro profissional credenciado"`.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]

### Complementos

- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]
- [[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|Aprendizado por Reforço com Feedback Humano (RLHF)]]
- [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia.md|Otimização Direta de Preferência (DPO)]]

### Alternativas

- Uso de modelos crus não alinhados com filtragem puramente externa via código e guardrails na aplicação.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 78–80
- **Evidência:** Chip Huyen discute o fluxo de pós-treinamento composto por SFT e alinhamento de preferência, ilustrando a transição com a famosa metáfora do Shoggoth e citando a discrepância de computação onde o pós-treino utilizou apenas 2% dos recursos no InstructGPT.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é o objetivo primário do pós-treinamento e em que ele se diferencia fundamentalmente do pré-treinamento?
2. Quais são as duas etapas sequenciais convencionais que compõem o pipeline de pós-treinamento?
3. Como a metáfora visual do Shoggoth ilustra a relação entre o modelo base pré-treinado e o modelo alinhado final?
4. Por que modelos de linguagem que passam apenas pelo pré-treinamento falham em atuar como assistentes conversacionais úteis?
5. Qual proporção aproximada de computação o pós-treinamento consome em relação ao pré-treino em modelos como o InstructGPT?
6. O que é o fenômeno da recusa falsa (*false refusal*) e como ele evidencia as imperfeições das técnicas atuais de alinhamento?
7. Por que se afirma tecnicamente que o pós-treinamento serve para "desbloquear" habilidades pré-existentes em vez de ensinar novos fatos ao modelo?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
