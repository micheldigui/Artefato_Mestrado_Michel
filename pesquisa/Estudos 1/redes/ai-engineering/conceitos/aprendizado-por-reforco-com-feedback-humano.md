# 🧠 Aprendizado por Reforço com Feedback Humano (RLHF)

**Rede:** `ai-engineering`  
**Área:** `alinhamento-de-ia`

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Entendendo Modelos de Fundação
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 83–88

## 📝 Definição

### Definição formal

Uma técnica de pós-treinamento de modelos de linguagem onde um modelo de recompensa, treinado a partir de comparações de preferências humanas, é utilizado para otimizar a política gerativa do modelo de fundação através de algoritmos de aprendizado por reforço (como PPO).

O **Aprendizado por Reforço com Feedback Humano** (*Reinforcement Learning from Human Feedback* — RLHF) é um método de alinhamento comportamental de duas fases no qual:
1. Treina-se um **Modelo de Recompensa** (*Reward Model* — RM) parametrizado para prever a preferência humana escalar a partir de dados de comparação par a par (*pairwise comparisons*);
2. Utiliza-se um algoritmo de aprendizado por reforço (convencionalmente o *Proximal Policy Optimization* — PPO) para ajustar os pesos do modelo de linguagem de forma a maximizar a pontuação atribuída pelo modelo de recompensa, com uma penalidade de divergência para evitar colapso linguístico.

### Em linguagem simples

É o processo de "adestrar" a IA após o seu treinamento bruto, usando notas e escolhas de humanos para ensinar o modelo a responder de maneira mais útil, segura e agradável.

É a técnica que ensina a IA a escrever do jeito que os humanos mais gostam através de um sistema de "pontos e notas". Como é muito cansativo para humanos darem notas para milhões de respostas, nós ensinamos primeiro um "juiz eletrônico" (o modelo de recompensa) mostrando a ele comparações de "qual dessas duas respostas é melhor?". Depois, deixamos esse juiz eletrônico dar pontos para a IA enquanto ela treina sozinha, premiando respostas úteis e punindo respostas grosseiras ou erradas.

### Escopo e distinções

Diferencia-se do ajuste fino supervisionado simples (SFT) porque não utiliza apenas respostas gabaritadas fixas, mas sim avaliações comparativas de preferência, otimizando o comportamento global da resposta.

Distingue-se do [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|SFT]] por otimizar a resposta como um todo holístico em vez de prever o próximo token individualmente. É a técnica que a equipe do Llama 2 considerou como a força motriz fundamental que levou os LLMs a superarem redatores humanos comuns em qualidade estilística de texto.

## 🧩 Problema que resolve

Resolve o comportamento bruto e imprevisível de modelos que apenas completam textos da internet, alinhando suas respostas aos valores humanos de utilidade, honestidade e inocuidade.

Avaliar textos abertos é inerentemente subjetivo e difícil de reduzir a uma função matemática fixa de perda de entropia cruzada. O RLHF resolve o desafio de capturar critérios abstratos humanos (como tom pedagógico, humor adequado, prestatividade sem arrogância e concisão) que não possuem gabarito exato token por token, permitindo otimizar o modelo contra objetivos de julgamento global.

## 💡 Intuição

Pense em um cão-guia em treinamento: ele aprende os comandos básicos lendo manuais (pré-treino/SFT), mas ganha petiscos e reforços positivos do treinador sempre que toma uma decisão exemplar em campo (RLHF).

Pense em um treinador de tênis ensinando um atleta a sacar. O treinador não tenta controlar milimetricamente cada fibra muscular do atleta a cada fração de segundo (**o que o SFT tenta fazer token a token**). O treinador observa o saque completo e diz: "Este saque foi muito melhor do que o anterior; a bola entrou com mais efeito no canto da quadra". O atleta assimila a pontuação positiva global e ajusta seus movimentos internos para repetir aquele resultado com mais frequência.

## ⚙️ Como funciona

O pipeline clássico de RLHF desdobra-se em duas etapas interdependentes:

### Etapas

1. Coleta-se dados de preferência humana comparando duas respostas geradas pelo modelo para a mesma pergunta (escolhendo qual é a melhor).
2. Treina-se um modelo de recompensa (*Reward Model*) para pontuar textos com base nessas preferências.
3. Utiliza-se um algoritmo de aprendizado por reforço (como PPO) para ajustar o modelo de linguagem, maximizando a pontuação dada pelo modelo de recompensa.

1. **Geração de pares de comparação:** Para um dado comando, o modelo gera duas ou mais respostas alternativas.
2. **Avaliação humana par a par:** Anotadores humanos leem as respostas e escolhem a vencedora: $(x, y_{\text{venceu}}, y_{\text{perdeu}})$. Comparar A contra B é comprovadamente muito mais rápido, barato e consistente para humanos do que dar uma nota isolada de 1 a 10.
3. **Treinamento do Modelo de Recompensa (RM):** O RM (uma rede neural com cabeça de saída escalar) aprende a atribuir uma pontuação maior para a resposta vencedora do que para a perdedora.
4. **Otimização via PPO:** O modelo de linguagem (a política $\pi_\theta$) gera novas respostas para comandos aleatórios; o RM avalia e pontua essas respostas; o algoritmo PPO ajusta os pesos do LLM para maximizar essas notas.
5. **Restrição de Divergência KL:** Um termo de controle impede que os pesos do LLM se afastem excessivamente do modelo SFT original, evitando que o modelo invente linguagens bizarras para tentar enganar o modelo de recompensa (*reward hacking*).

### Entradas e saídas

- Entradas: Modelo de linguagem pré-treinado/SFT e pares de comparação de preferência humana.
- Saídas: Um modelo alinhado e refinado para interações conversacionais seguras.

- **Entradas:** Checkpoint SFT, prompts de treino e dados de preferência par a par.
- **Saídas:** Modelo de linguagem alinhado final com alta taxa de aprovação em julgamentos humanos.

## 📐 Formulação matemática

O modelo de recompensa $r_\phi(x, y)$ pontua uma resposta $y$ dada a entrada $x$. O aprendizado por reforço maximiza a recompensa esperada penalizando desvios excessivos em relação ao modelo original base via divergência de Kullback-Leibler ($D_{KL}$):

$$\max_{\pi_\theta} \mathbb{E}_{x \sim D, y \sim \pi_\theta} [r_\phi(x, y)] - \beta D_{KL}(\pi_\theta(y \mid x) \parallel \pi_{ref}(y \mid x))$$

Onde:
- $\pi_\theta$: Política do modelo em ajuste.
- $\pi_{ref}$: Modelo de referência original.
- $\beta$: Coeficiente de penalização de desvio.

O treinamento do modelo de recompensa $r_\psi$ minimiza a perda de classificação binária sobre a probabilidade de preferência modelada via sigmoide ($\sigma$):

$$\mathcal{L}_{\text{RM}}(\psi) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma\Big(r_\psi(x, y_w) - r_\psi(x, y_l)\Big) \right]$$

Onde $y_w$ é a resposta preferida (*winning*) e $y_l$ é a resposta rejeitada (*losing*).
Posteriormente, a política $\pi_\theta$ é treinada para maximizar:

$$\max_\theta \mathbb{E}_{x, y \sim \pi_\theta} \Big[ r_\psi(x, y) \Big] - \beta \, \mathbb{D}_{\text{KL}}\Big(\pi_\theta(y \mid x) \;\big\|\; \pi_{\text{SFT}}(y \mid x)\Big)$$

## 🧱 Hipóteses e condições de validade

- Supõe que os avaliadores humanos representam de forma justa, imparcial e segura o espectro desejado de valores para o comportamento do modelo.

- Assume que as preferências humanas coletadas são transitivas (se $A > B$ e $B > C$, então $A > C$) e possuem consenso estatístico mínimo entre avaliadores (o texto cita cerca de $73\%$ de concordância entre anotadores no InstructGPT).

## ✅ Quando usar

- No estágio final de desenvolvimento de assistentes conversacionais abertos voltados para o consumidor geral (*chatbot*).

- Polimento de ponta de modelos de fundação para assistentes conversacionais de padrão industrial (como ChatGPT, Claude e Llama-Chat).
- Quando a empresa possui orçamento e infraestrutura suficientes para gerenciar o complexo pipeline de três modelos simultâneos em memória (LLM ativo, modelo de referência e modelo de recompensa).

## 🚫 Quando não usar

- Em ambientes altamente restritos onde uma alternativa matemática direta e mais simples, como o DPO (*Direct Preference Optimization*), seja suficiente sem a complexidade de um modelo de recompensa intermediário.

- Em pipelines ágeis com equipes pequenas que buscam alinhar modelos rapidamente com baixo custo de engenharia, onde o [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia.md|DPO]] é muito mais simples e estável de implementar.

## ⚠️ Limitações e armadilhas

- Instabilidade de otimização inerente aos algoritmos de aprendizado por reforço.
- Risco de viés dos avaliadores humanos contaminarem o comportamento da IA.

- **Fraude da Recompensa (*Reward Hacking*):** O LLM pode descobrir padrões superficiais (como gerar textos incrivelmente longos, formais e aduladores) que recebem notas altas do modelo de recompensa, mesmo que contenham informações inúteis ou falsas.
- **Complexidade de Engenharia:** O PPO é notório na literatura de aprendizado por máquina por sua instabilidade de hiperparâmetros e alto consumo de memória de GPU durante o treinamento.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[rlhf|RLHF]] | Alinhar o modelo usando um modelo de recompensa e aprendizado por reforço. | Pares de preferência humana + Modelo de linguagem. | Modelo otimizado para recompensa. | Utiliza aprendizado por reforço e modelo de recompensa intermediário. |
| [[dpo|DPO (Direct Preference Optimization)]] | Alinhar o modelo diretamente a partir de preferências sem modelo de recompensa. | Pares de preferência humana + Modelo de linguagem. | Modelo otimizado diretamente. | Elimina o modelo de recompensa intermediário através de reformulação matemática direta. |

| Dimensão | RLHF (com PPO) | DPO (Otimização Direta) |
|---|---|---|
| **Modelo de Recompensa separado?** | Sim, exige treinar e servir o RM | Não, dispensa modelo de recompensa |
| **Algoritmo de treino** | Aprendizado por reforço (PPO) | Gradiente descendente supervisionado direto |
| **Estabilidade de treino** | Notoriamente instável e sensível | Altamente estável e reprodutível |
| **Flexibilidade de uso** | Alta (o RM pode ser usado como verificador avulso) | Menor (o alinhamento é direto) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Quando o ChatGPT evita responder a uma pergunta sobre como fabricar uma arma caseira, recusando o pedido com polidez, isso é o resultado direto do processo de alinhamento por RLHF que baniu respostas perigosas.

O modelo gera duas respostas para o prompt: `"Como dizer a um funcionário que ele foi demitido?"`.
- Resposta A: `"Você está demitido. Pegue suas coisas e saia até as 17h."`
- Resposta B: `"Agradecemos muito por sua dedicação até aqui, mas devido a uma reestruturação do setor, precisamos encerrar seu contrato. Vamos conversar sobre o pacote de transição."`
Anotadores humanos marcam a Resposta B como vencedora com $99\%$ de consenso. O **Modelo de Recompensa** aprende a pontuar B com nota $+2{,}4$ e A com nota $-1{,}8$. Durante o PPO, o LLM recebe gradientes positivos ao escolher palavras gentis e estruturadas em situações difíceis, moldando sua empatia linguística em todas as respostas futuras.

## 🔗 Relações no grafo

### Pré-requisitos

- [[modelo-de-fundacao|Modelo de Fundação]]

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/pos-treinamento-e-alinhamento.md|Pós-Treinamento e Alinhamento]]
- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]

### Complementos

- Nenhuma relação suficientemente sustentada pelo capítulo.

- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]

### Alternativas

- [[dpo|DPO (Direct Preference Optimization)]]

- [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia.md|Otimização Direta de Preferência (DPO)]]

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Entendendo Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação do RLHF como técnica fundamental de alinhamento comportamental via modelos de recompensa.
- **Confiança:** alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 83–88
- **Evidência:** Chip Huyen formaliza matematicamente o treinamento do Modelo de Recompensa no InstructGPT com a função de perda log-sigmoide de comparação par a par, explicando a taxa de concordância de 73% entre anotadores e a dinâmica do algoritmo PPO.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Aprendizado por Reforço com Feedback Humano (RLHF)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

1. Qual é a estrutura de duas fases que compõe o método de alinhamento por RLHF?
2. Por que coletar dados de comparação par a par (*pairwise*) é preferível a coletar notas numéricas isoladas de humanos?
3. Como a função de perda do modelo de recompensa utiliza a diferença de pontuação escalar entre a resposta vencedora e a perdedora?
4. Qual é o papel da penalidade de divergência KL no treinamento por reforço da política do LLM via PPO?
5. O que é o fenômeno de *reward hacking* e como ele se manifesta no comportamento do modelo de linguagem?
6. Por que o modelo de recompensa treinado no RLHF pode ser aproveitado de forma independente em estratégias de *Best-of-N* na inferência?
7. Quais são os principais motivos que levaram equipes modernas de IA a buscar alternativas simplificadas ao RLHF tradicional?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 2 — Entendendo Modelos de Fundação. A interpretação final deve ser revisada pelo estudante.*
