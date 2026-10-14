# 🧠 Ajuste Fino Supervisionado (SFT)

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 80–83

## 📝 Definição

### Definição formal

O **Ajuste Fino Supervisionado** (*Supervised Finetuning* — SFT) no ciclo de vida de modelos de fundação é o procedimento de aprendizado supervisionado em que os parâmetros de um modelo pré-treinado são ajustados sobre um conjunto selecionado de **dados de demonstração** compostos por pares rotulados de entrada e saída `(instrução, resposta_ideal)`, com o objetivo de executar **clonagem comportamental** (*behavior cloning*) do estilo dialógico, resolutivo e cooperativo demonstrado pelos anotadores.

### Em linguagem simples

É a fase do treinamento onde a IA aprende por imitação. Entregamos a ela milhares de exemplos de conversas perfeitas escritas por especialistas (com a pergunta do usuário e a resposta ideal do assistente) para que o modelo aprenda a responder como um assistente prestativo em vez de apenas continuar completando textos aleatórios da internet.

### Escopo e distinções

Distingue-se do pré-treino por utilizar supervisão explícita com pares de conversa e instruções com curadoria rigorosa de qualidade. Também se distingue do alinhamento de preferência ([[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|RLHF]]), pois o SFT treina com base em uma única resposta gabaritada por exemplo, enquanto o RLHF treina a partir da comparação entre múltiplas respostas (`melhor` vs. `pior`).

## 🧩 Problema que resolve

Supera o desalinhamento de formato do modelo pré-treinado. Um modelo cru não sabe que uma pergunta exige uma resposta resolutiva; ele pode responder a uma pergunta com outra pergunta ou simplesmente anexar links web quebrados. O SFT condiciona o modelo a reconhecer padrões de comandos (`"Resuma"`, `"Traduza"`, `"Explique"`) e adotar a postura formal de execução direta da tarefa.

## 💡 Intuição

Pense em um ator talentoso que decorou todos os clássicos da literatura mundial (o modelo pré-treinado). Ele tem domínio vocabular absoluto, mas não sabe qual personagem deve interpretar no palco hoje. O diretor de teatro senta com ele, entrega o roteiro e demonstra a postura física, o tom de voz e o ritmo das falas daquele personagem (**dados de demonstração do SFT**). O ator imita e internaliza o papel de assistente.

## ⚙️ Como funciona

O processo depende essencialmente do rigor pedagógico da equipe de curadoria:

### Etapas

1. **Taxonomia de tarefas:** Mapeia-se os tipos de solicitações que o modelo deve dominar (perguntas abertas, sumarização, tradução, extração, geração de código, brainstorm).
2. **Criação de dados de demonstração:** Redatores ou especialistas qualificados (frequentemente com graduação e pós-graduação) redigem as respostas ideais para cada comando.
3. **Treinamento supervisionado:** O modelo ingere os pares e atualiza seus pesos matemáticos minimizando a perda de entropia cruzada sobre os tokens da resposta ideal.
4. **Mascaramento da perda do prompt:** O algoritmo calcula erros e atualiza gradientes quase exclusivamente sobre os tokens da resposta gerada, ignorando os tokens do comando de entrada para não desperdiçar capacidade memorizando as perguntas.

### Entradas e saídas

- **Entradas:** Checkpoint pré-treinado e milhares de pares curados `(prompt, resposta)`.
- **Saídas:** Checkpoint "SFT", capaz de manter conversação e seguir ordens diretas.

## 📐 Formulação matemática

O treinamento supervisionado opera pela maximização da log-verossimilhança condicional restrita aos tokens da resposta $Y = (y_1, y_2, \dots, y_M)$ dado o prompt $X = (x_1, x_2, \dots, x_N)$:

$$\mathcal{L}_{\text{SFT}}(\theta) = -\sum_{j=1}^M \log P(y_j \mid x_1, \dots, x_N, y_1, \dots, y_{j-1}; \theta)$$

A computação da função de perda penaliza desvios probabilísticos apenas nas posições dos tokens da resposta gerada, ignorando o cálculo de gradientes sobre as posições dos tokens do prompt de entrada $X$.

## 🧱 Hipóteses e condições de validade

- A qualidade intrínseca das respostas dos anotadores é o teto de inteligência comportamental que o SFT consegue transmitir; demonstrações com erros factuais ou inconsistências de estilo ensinam vícios que o modelo assimilará com facilidade.

## ✅ Quando usar

- Fase obrigatória após o pré-treinamento para transformar qualquer LLM em um modelo funcional de instruções (*Instruct model*).
- Adaptação corporativa profunda de modelos abertos para adotar linguagem técnica de nichos específicos (ex.: atendimento bancário ou pareceres jurídicos).

## 🚫 Quando não usar

- Para tentar ensinar conhecimentos factuais novos e massivos que não existiam no modelo de fundação base (o que costuma desencadear o vício de [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|alucinação]]).

## ⚠️ Limitações e armadilhas

- **Custo e lentidão humana:** Criar respostas perfeitas para tarefas complexas de raciocínio pode levar até 30 minutos por amostra para um especialista humano, tornando a base de dados cara de produzir.
- **Indução à alucinação por descompasso:** Se o anotador humano utilizar um conhecimento externo sofisticado que o modelo base nunca aprendeu no pré-treino para escrever uma resposta brilhante, o SFT ensinará o modelo a forçar respostas semelhantes sem ter os fatos para sustentá-las.

## 🔍 Comparações

| Aspecto | SFT (Ajuste Supervisionado) | Alinhamento de Preferência (RLHF) |
|---|---|---|
| **Formato do dado** | Par unitário `(prompt, resposta)` | Par comparativo `(prompt, venceu, perdeu)` |
| **Custo de anotação** | Muito alto (redigir do zero) | Menor (apenas escolher a melhor opção) |
| **Nível de otimização** | Token a token (predição local) | Resposta completa (julgamento holístico) |
| **Função primária** | Ensinar a seguir o formato de diálogo | Ensinar nuances de estilo e segurança |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O time do InstructGPT contrata anotadores para criar dados de demonstração.
- Prompt: `"Explique por que o céu é azul como se eu tivesse 5 anos"`.
- Resposta do anotador: `"A luz do Sol parece branca, mas ela tem todas as cores do arco-íris misturadas. Quando ela chega na Terra, o ar espalha a cor azul para todos os lados mais do que as outras cores, por isso quando você olha para cima vê tudo azul!"`.
O modelo é treinado sobre 13.000 pares como esse. A partir daí, ele aprende o padrão comportamental de simplificar explicações científicas com analogias quando o usuário pede explicações no formato `"ELI5"`.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/pos-treinamento-e-alinhamento.md|Pós-Treinamento e Alinhamento]]

### Complementos

- [[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|Aprendizado por Reforço com Feedback Humano (RLHF)]]
- [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia.md|Otimização Direta de Preferência (DPO)]]

### Alternativas

- Treinamento direto do zero apenas com dados de conversação (economicamente inviável frente ao paradigma pré-treino + SFT).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 80–83
- **Evidência:** Chip Huyen explica o processo de SFT no InstructGPT, destacando o perfil demográfico de anotadores altamente educados para gerar dados de demonstração e analisando como o SFT ensina o formato conversacional através da clonagem de comportamento.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a definição de Ajuste Fino Supervisionado (SFT) no contexto do pós-treinamento de LLMs?
2. Como funciona o conceito de "clonagem comportamental" aplicado ao aprendizado por instruções?
3. Por que a função de perda durante o SFT é calculada sobre os tokens da resposta e não sobre os tokens do prompt?
4. Quais são as principais limitações e gargalos econômicos decorrentes da produção de dados manuais de demonstração?
5. De que forma o SFT pode induzir involuntariamente o modelo a alucinar se os dados de treino exigirem conhecimentos ausentes do pré-treino?
6. Qual foi o volume aproximado de dados de demonstração utilizado pela OpenAI para criar o modelo InstructGPT?
7. Por que o SFT por si só geralmente não é suficiente para produzir um modelo com alto refinamento de estilo e segurança corporativa?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
