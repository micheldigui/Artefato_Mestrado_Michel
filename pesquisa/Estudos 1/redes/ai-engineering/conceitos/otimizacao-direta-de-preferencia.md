# 🧠 Otimização Direta de Preferência (DPO)

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 84, 88

## 📝 Definição

### Definição formal

A **Otimização Direta de Preferência** (*Direct Preference Optimization* — DPO) é um método matemático de alinhamento de preferências humanas para modelos de linguagem (Rafailov et al., 2023) que deriva uma formulação em forma fechada que mapeia a probabilidade implícita de recompensa diretamente sobre a política do modelo, permitindo otimizar o LLM sobre dados de comparação par a par através de gradiente descendente supervisionado simples, eliminando formalmente a necessidade de treinar um modelo de recompensa intermediário e de aplicar algoritmos complexos de aprendizado por reforço baseados em amostragem em tempo de execução (como o PPO).

### Em linguagem simples

É uma maneira genial e muito mais simples de ensinar a IA a preferir as respostas que os humanos gostam. Em vez de criar um "juiz robô" intermediário e usar técnicas difíceis de aprendizado por reforço para adestrar a IA, o DPO usa uma fórmula matemática que ajusta os pesos da IA diretamente olhando para a lista de respostas certas e erradas, funcionando com a mesma facilidade de um treino comum de computador.

### Escopo e distinções

Distingue-se do [[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|RLHF]] pela ausência do modelo de recompensa explicitamente treinado. Tornou-se a técnica de escolha de equipes industriais de ponta (adotada expressamente pela Meta no Llama 3 para substituir o pipeline de RLHF do Llama 2).

## 🧩 Problema que resolve

Resolve a extrema complexidade operacional, a fragilidade de convergência e a pesada sobrecarga de memória do RLHF tradicional com PPO. O RLHF exige gerenciar múltiplos modelos simultâneos em clusters de GPUs e calibrar dezenas de hiperparâmetros instáveis de aprendizado por reforço. O DPO reduz todo esse esforço a uma perda analítica supervisionada direta, tornando o alinhamento de preferência acessível a qualquer equipe de engenharia.

## 💡 Intuição

Pense em ensinar um motorista a escolher a melhor rota:
- No **RLHF**, você cria primeiro um passageiro virtual artificial exigente que dá notas de 0 a 10 para cada manobra (**o modelo de recompensa**) e faz o motorista dirigir aleatoriamente pela cidade tentando descobrir como ganhar notas altas desse passageiro virtual (**o PPO**).
- No **DPO**, você simplesmente entrega ao motorista uma lista com 1.000 trajetos gravados mostrando: "Nesta esquina, vire pela rua A e não pela rua B". O motorista olha diretamente para a comparação e ajusta suas escolhas de trânsito em uma única aula teórica, sem precisar do passageiro virtual intermediário.

## ⚙️ Como funciona

O algoritmo reescreve a perda de recompensa em termos da probabilidade das palavras do próprio modelo de linguagem:

### Etapas

1. **Conjunto de comparações:** Coleta pares de dados com base na preferência humana: $(x, y_w, y_l)$.
2. **Carregamento dos modelos:** Mantém em memória o modelo sendo treinado ($\pi_\theta$) e uma cópia congelada do modelo SFT de referência ($\pi_{\text{ref}}$).
3. **Cálculo da probabilidade implícita:** O algoritmo avalia qual é a probabilidade que os dois modelos atribuem a cada palavra da resposta vencedora $y_w$ e da resposta perdedora $y_l$.
4. **Aplicação do gradiente DPO:** A função de perda aumenta a probabilidade dos tokens de $y_w$ e diminui a probabilidade dos tokens de $y_l$, escalonada de acordo com o quão surpreso o modelo de referência estaria com essa escolha.
5. **Ajuste direto:** Os pesos do LLM são atualizados em um passo único de treinamento supervisionado estável.

### Entradas e saídas

- **Entradas:** Checkpoint do modelo ajustado via SFT e conjunto de dados comparativos `(instrução, vencedora, perdedora)`.
- **Saídas:** Modelo de fundação com preferências alinhadas, treinado de forma estável.

## 📐 Formulação matemática

A perda do DPO deriva analiticamente da formulação da recompensa ótima do RLHF sob regularização KL, eliminando o parâmetro de recompensa $r_\psi$:

$$\mathcal{L}_{\text{DPO}}(\theta) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) \right]$$

Onde:
- $\pi_\theta$ é o modelo que está sendo otimizado;
- $\pi_{\text{ref}}$ é o modelo base original congelado;
- $\beta$ é o coeficiente hiperparamétrico que controla a intensidade da penalidade de desvio em relação ao modelo original;
- $\sigma$ é a função sigmoide clássica.

## 🧱 Hipóteses e condições de validade

- O modelo de referência $\pi_{\text{ref}}$ deve ser exatamente o modelo que gerou as respostas iniciais ou o checkpoint SFT imediato para garantir que as razões de probabilidade mantenham coerência matemática.

## ✅ Quando usar

- Alinhamento de preferência padrão para a vasta maioria das aplicações modernas e adaptações corporativas de modelos de código aberto.
- Quando a equipe não dispõe de tempo nem de infraestrutura para calibrar algoritmos de aprendizado por reforço como o PPO.

## 🚫 Quando não usar

- Em fluxos onde você precisa expressamente de um **Modelo de Recompensa avulso** para atuar como avaliador ou verificador independente (*verifier*) em estratégias de inferência de computação em tempo de teste (*Best-of-N*).

## ⚠️ Limitações e armadilhas

- **Dependência da qualidade dos dados comparativos:** Se as respostas nos pares de dados tiverem diferenças sutis demais ou ruídos de anotação, o modelo pode apresentar sobre-ajuste (*overfitting*) e degradar a coerência do texto.
- **Variações no parâmetro $\beta$:** Valores inadequados de $\beta$ podem fazer o modelo ignorar a preferência humana ($\beta$ muito baixo) ou perder totalmente a fluência natural ($\beta$ muito alto).

## 🔍 Comparações

| Característica | Otimização Direta (DPO) | Aprendizado por Reforço (RLHF) |
|---|---|---|
| **Abordagem metodológica** | Otimização supervisionada em forma fechada | Aprendizado por Reforço em tempo de execução |
| **Modelos em VRAM no treino** | 2 modelos (ativo e referência) | 3 a 4 modelos (ativo, ref, recompensa, valor) |
| **Complexidade de código** | Baixa (poucas linhas sobre perda padrão) | Altíssima (motores de atores e críticos PPO) |
| **Adoção na indústria moderna** | Padrão dominante emergente (Llama 3) | Tradicional (InstructGPT, Llama 2) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma empresa quer treinar seu assistente para responder dúvidas de clientes corporativos de forma objetiva sem preâmbulos enrolados como `"Com certeza! Ficarei muito feliz em ajudar você hoje com isso..."`.
A equipe cria 5.000 pares onde a resposta $y_w$ vai direto aos fatos e a resposta $y_l$ começa com enrolações adocicadas. O **DPO** recebe os pares e calcula a razão entre as probabilidades dos tokens nos dois modelos. Em poucas horas de gradiente descendente convencional em GPU, o modelo aprende a abaixar drasticamente a probabilidade de início com clichês de IA e passa a responder diretamente ao ponto, sem necessidade de nenhum modelo de recompensa intermediário.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/pos-treinamento-e-alinhamento.md|Pós-Treinamento e Alinhamento]]
- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]

### Complementos

- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]

### Alternativas

- [[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|Aprendizado por Reforço com Feedback Humano (RLHF)]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]
- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 84, 88
- **Evidência:** O texto cita a publicação de Rafailov et al. (2023) sobre DPO, destacando sua crescente adesão pela indústria para reduzir a complexidade operacional do RLHF tradicional e pontuando a decisão da Meta de substituir o RLHF do Llama 2 pelo DPO no Llama 3.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é a técnica de Otimização Direta de Preferência (DPO) e qual é a sua principal inovação conceitual em relação ao RLHF?
2. Por que o DPO elimina matematicamente a necessidade de treinar um modelo de recompensa dedicado?
3. Quais são as vantagens de estabilidade e consumo de memória de GPU ao treinar com DPO em comparação ao PPO?
4. Qual é o papel do hiperparâmetro $\beta$ na formulação matemática da função de perda do DPO?
5. Por que a equipe de engenharia da Meta optou por migrar do RLHF no Llama 2 para o DPO no desenvolvimento do Llama 3?
6. Em qual cenário específico de arquitetura a manutenção de um modelo de recompensa clássico ainda é vantajosa sobre o DPO?
7. Como o modelo de referência congelado ($\pi_{\text{ref}}$) atua para preservar a fluência linguística durante a aplicação do DPO?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
