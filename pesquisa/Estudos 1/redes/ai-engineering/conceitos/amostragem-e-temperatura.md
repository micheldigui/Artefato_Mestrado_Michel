# 🧠 Amostragem e Temperatura

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 88–93

## 📝 Definição

### Definição formal

A **Amostragem** (*Sampling*) é o procedimento de inferência estocástica pelo qual um [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|modelo de linguagem autorregressivo]] seleciona o próximo token a ser gerado a partir da distribuição de probabilidade calculada sobre todo o vocabulário. 

A **Temperatura** ($T \in [0, \infty)$) é um hiperparâmetro escalar de suavização que divide os valores numéricos brutos dos *logits* antes da aplicação da função *softmax*, modulando o nível de entropia da distribuição resultante:
- $T \to 0$: colapsa a amostragem na escolha determinística do token de maior probabilidade (**amostragem gananciosa** ou *greedy sampling*);
- $T > 1$: nivela as probabilidades, aumentando a chance de seleção de tokens raros e elevando a aleatoriedade da resposta.

### Em linguagem simples

É o botão que controla a previsibilidade versus a criatividade da IA. Quando você define a temperatura como zero, o modelo é estritamente metódico e escolhe sempre a palavra mais óbvia do dicionário. Conforme você aumenta a temperatura, o modelo começa a arriscar palavras menos comuns, tornando o texto mais solto e criativo, mas com maior risco de ficar sem nexo se o valor for alto demais.

### Escopo e distinções

Não se confunde com alterações nos pesos da rede neural. A temperatura é um cálculo matemático de ajuste pós-processamento aplicado em tempo real na saída da última camada do modelo antes do sorteio do token.

## 🧩 Problema que resolve

Resolve o dilema entre monotonia mecânica e variedade expressiva. Se um modelo utilizar sempre a escolha gananciosa (*greedy*), suas respostas para tarefas criativas ou redação soam repetitivas, artificiais e previsíveis. A amostragem estocástica com temperatura permite que a mesma IA atue tanto como um compilador rigoroso de dados (com $T=0$) quanto como um parceiro de brainstorm literário (com $T=0{,}7$ a $1{,}0$).

## 💡 Intuição

Pense em um músico solista improvisando no palco.
- Se o maestro pedir para ele tocar com **temperatura zero**, o músico tocará estritamente as notas mais clássicas e previsíveis da partitura sem errar nenhuma batida, mas soando mecânico.
- Se o maestro pedir **temperatura 0.7**, o músico manterá a harmonia da canção, mas adicionará notas de jazz inesperadas e variações bonitas.
- Se o maestro definir **temperatura 2.0**, o músico começará a apertar teclas aleatórias de olhos fechados, gerando dissonância e barulho caótico.

## ⚙️ Como funciona

O ajuste matemático dos logits ocorre no momento exato de emissão de cada token:

### Etapas

1. **Geração de Logits:** A rede neural processa o contexto e emite um vetor de pontuações brutas não normalizadas $z = [z_1, z_2, \dots, z_{|V|}]$, uma para cada token do vocabulário.
2. **Divisão pela Temperatura:** Cada pontuação $z_i$ é dividida pelo valor escalar escolhido de $T$: $z_i' = \frac{z_i}{T}$.
   - *Se $T$ for baixo ($0{,}2$):* As diferenças entre as pontuações aumentam exponencialmente; o maior número destaca-se absurdamente dos outros.
   - *Se $T$ for alto ($1{,}5$):* As diferenças diminuem; os valores aproximam-se entre si.
   - *Se $T = 0$:* O sistema pula o cálculo e executa um $\arg\max(z)$, selecionando o maior logit diretamente.
3. **Conversão via Softmax:** O vetor ajustado passa pela função *softmax*, gerando as probabilidades reais de escolha $p_i$.
4. **Sorteio Estocástico:** O algoritmo realiza o sorteio do próximo token ponderado por essas probabilidades.

### Entradas e saídas

- **Entradas:** Vetor de logits brutos da camada final do modelo e o parâmetro escalar $T$.
- **Saídas:** O token específico selecionado para entrar no texto de saída.

## 📐 Formulação matemática

A probabilidade $p_i$ do $i$-ésimo token do vocabulário é expressa por:

$$p_i = \text{softmax}\left(\frac{z}{T}\right)_i = \frac{\exp\left(\frac{z_i}{T}\right)}{\sum_{j=1}^{|V|} \exp\left(\frac{z_j}{T}\right)}$$

No limite em que a temperatura se aproxima de zero, a distribuição estocástica converge para a distribuição delta de Dirac no índice de maior pontuação:

$$\lim_{T \to 0^+} p_i = \begin{cases} 1, & \text{se } i = \arg\max_k(z_k) \\ 0, & \text{caso contrário} \end{cases}$$

## 🧱 Hipóteses e condições de validade

- Matematicamente, a temperatura não pode ser estritamente igual a zero (pois causaria divisão por zero $\frac{z_i}{0}$). As bibliotecas e APIs de engenharia tratam $T=0$ implementando uma rota lógica alternativa de $\arg\max$ analítico puro.

## ✅ Quando usar

- **$T = 0$ (Gananciosa):** Classificação de texto, extração de entidades, geração de código-fonte, tradução formal e saídas estruturadas em JSON.
- **$T \in [0{,}6; 0{,}8]$:** Conversação comum, assistentes de suporte ao cliente, redação de e-mails e sumarização equilibrada.
- **$T \ge 1{,}0$:** Brainstorming de ideias, poesia, criação de personagens e tarefas onde desvios da norma são desejados.

## 🚫 Quando não usar

- Nunca use $T > 0$ quando a aplicação exigir reprodutibilidade determinística estrita para testes unitários automatizados de conformidade.
- Nunca use $T > 1{,}5$ em produtos corporativos sérios, pois a taxa de geração de caracteres corrompidos e palavras desconexas eleva-se rapidamente.

## ⚠️ Limitações e armadilhas

- **A ilusão do determinismo absoluto com $T=0$:** Mesmo com $T=0$, modelos comerciais acessados via nuvem podem apresentar pequenas variações de resposta ao longo do tempo devido a operações não associativas de ponto flutuante em GPUs paralelas e mudanças de balanceamento de carga no provedor.
- **Causa direta de inconsistência:** Esquecer a temperatura no padrão de fábrica ($T=1{,}0$) em tarefas de extração de dados é a causa número um de reclamações de engenheiros sobre a IA "mudar de ideia a cada execução".

## 🔍 Comparações

| Temperatura ($T$) | Comportamento do Texto | Entropia | Casos de Uso Recomendados |
|---|---|---|---|
| **$T = 0$** | Determinístico, focado, repetitivo | Mínima | Código, JSON, Fatos, Classificação |
| **$T = 0{,}7$** | Fluido, balanceado, natural | Média | Chatbots, Redação, Resumos gerais |
| **$T \ge 1{,}5$** | Imprevisível, caótico, errático | Máxima | Exploração criativa extrema, geração de ruído |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Considere um modelo que precisa completar a frase `"O céu estava..."`. Os dois maiores logits calculados são `["azul": 4.0, "ensolarado": 2.0]`.
- Se aplicarmos **$T = 1{,}0$**: $e^4 \approx 54{,}6$ e $e^2 \approx 7{,}4$. A palavra `"azul"` tem cerca de $88\%$ de chance e `"ensolarado"` tem $12\%$. O modelo escolherá `"ensolarado"` em 1 de cada 8 vezes.
- Se aplicarmos **$T = 0{,}5$**: Os logits viram `[8.0, 4.0]`. $e^8 \approx 2980$ e $e^4 \approx 54{,}6$. A chance de `"azul"` sobe para $98{,}2\%$. A resposta fica muito mais previsível.
- Se aplicarmos **$T = 2{,}0$**: Os logits viram `[2.0, 1.0]`. $e^2 \approx 7{,}4$ e $e^1 \approx 2{,}7$. A chance de `"azul"` cai para $73\%$ e `"ensolarado"` sobe para $27\%$. O texto ganha variedade estilística.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]

### Complementos

- [[redes/ai-engineering/conceitos/amostragem-top-k-e-top-p.md|Amostragem Top-k e Top-p]]
- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]

### Alternativas

- [[redes/ai-engineering/conceitos/amostragem-restrita-e-saidas-estruturadas.md|Amostragem Restrita e Saídas Estruturadas]] (que remove a liberdade estocástica com base em gramáticas).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 88–93
- **Evidência:** O texto detalha a mecânica de amostragem dos logits através da função softmax, ilustrando com gráficos a redistribuição das probabilidades em diferentes temperaturas e desmistificando o funcionamento prático de $T=0$ como um atalho analítico de $\arg\max$.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que são logits brutos e qual é a função da camada Softmax na amostragem de tokens?
2. Como o hiperparâmetro de temperatura atua matematicamente sobre os logits antes da normalização?
3. O que acontece com a distribuição de probabilidades de um modelo quando a temperatura se aproxima de zero?
4. Por que a amostragem gananciosa (*greedy sampling*) pode tornar textos longos excessivamente repetitivos ou artificiais?
5. Em quais tarefas de engenharia de software o uso de temperatura igual a zero é mandatório?
6. Por que fixar a temperatura em zero não garante $100\%$ de determinismo matemático em APIs comerciais na nuvem?
7. Qual é o perigo de se utilizar valores de temperatura superiores a $1{,}5$ em aplicações corporativas?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
