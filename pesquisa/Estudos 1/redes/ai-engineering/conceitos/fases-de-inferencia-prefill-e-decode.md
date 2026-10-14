# 🧠 Fases de Inferência: Prefill e Decode

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 60, 407–414, 442–443

## 📝 Definição

### Definição formal

As **Fases de Inferência: Prefill e Decode** constituem a bipartição operacional do ciclo de execução de modelos de fundação autorregressivos baseados na arquitetura Transformer:
1. **Prefill (Pré-preenchimento):** Fase inicial em que todos os tokens do prompt fornecido pelo usuário são ingeridos e processados simultaneamente em paralelo, gerando o primeiro token de saída e inicializando a memória temporária de chaves e valores (*KV Cache*).
2. **Decode (Decodificação):** Fase subsequente em que novos tokens são gerados de maneira estritamente sequencial, token a token, consumindo e atualizando o KV Cache a cada iteração.

### Em linguagem simples

É a diferença entre o tempo que a IA leva para ler a sua pergunta e o tempo que ela leva para digitar a resposta. Ela lê todas as palavras da sua pergunta de uma só vez (Prefill). Mas, na hora de responder, ela é obrigada a escrever palavra por palavra, uma de cada vez (Decode).

### Escopo e distinções

Essa divisão existe devido à natureza do [[redes/ai-engineering/conceitos/mecanismo-de-atencao.md|mecanismo de atenção]] em modelos autorregressivos. Enquanto o treinamento e o prefill se beneficiam de paralelismo maciço, o decode é impedido de paralelizar a geração de saídas pela dependência causal estrita (cada token gerado serve de entrada para o próximo).

## 🧩 Problema que resolve

Identificar as duas fases resolve o problema de diagnóstico de latência e alocação de hardware para atendimento de IA (*serving*). Sem essa separação conceitual, engenheiros não conseguem entender por que uma aplicação com prompts longos demora para começar a responder, enquanto aplicações que geram respostas longas sofrem com vazão baixa na placa de vídeo.

## 💡 Intuição

Pense em um estudante fazendo uma prova discursiva:
- **Prefill:** É o momento em que ele abre a prova e lê o enunciado de uma página inteira. Ele passa os olhos pelo texto rapidamente, assimilando todas as frases de uma vez (**paralelo**).
- **Decode:** É o momento em que ele pega a caneta e começa a redigir a resposta na folha oficial. Ele não consegue escrever dez palavras ao mesmo tempo; sua mão precisa escrever uma palavra por vez de forma contínua (**sequencial**).

## ⚙️ Como funciona

As duas fases impõem perfis de estresse computacional completamente diferentes aos processadores de IA (GPUs):

### Etapas

1. **Ingestão do Prompt (Início do Prefill):** O vetor de tokens de entrada $[x_1, \dots, x_P]$ é despachado para a GPU.
2. **Computação paralela da atenção:** Todos os $P$ tokens são multiplicados pelas matrizes de peso em paralelo.
3. **Povoamento do KV Cache:** Os vetores de Key e Value calculados para todos os tokens de entrada são armazenados na VRAM da GPU.
4. **Emissão do primeiro token:** O modelo produz os logits do primeiro token gerado $y_1$ (**Fim do Prefill** — determina o *TTFT*).
5. **Início do Loop de Decode:** O token recém-gerado $y_t$ é alimentado de volta ao modelo.
6. **Leitura e atualização de memória:** O modelo lê os parâmetros inteiros da rede da VRAM, consulta o KV Cache anterior, calcula apenas o novo vetor $K, V$ para $y_t$ e anexa-o ao cache.
7. **Emissão do token e iteração:** O modelo escolhe $y_{t+1}$ (**determina o *TPOT***) e repete os passos 5 a 7 até encontrar o marcador $\text{<EOS>}$.

### Entradas e saídas

- **No Prefill:** Entrada de $P$ tokens; saída de 1 token e preenchimento do KV Cache.
- **No Decode:** Entrada de 1 token (mais o cache acumulado); saída de 1 token subsequente por passo.

## 📐 Formulação matemática

O perfil computacional das duas fases é caracterizado pela métrica de intensidade aritmética (*Arithmetic Intensity* — $AI$), expressa em FLOPs por byte transferido da memória:

$$\text{Fase de Prefill:} \quad AI_{\text{prefill}} \approx \frac{2 \cdot P \cdot |\Theta|}{2 \cdot |\Theta| + \dots} \gg 1 \implies \text{Compute-Bound}$$

$$\text{Fase de Decode:} \quad AI_{\text{decode}} \approx \frac{2 \cdot 1 \cdot |\Theta|}{2 \cdot |\Theta| + \text{KV\_Cache}} \approx 1 \implies \text{Memory-Bandwidth Bound}$$

Onde $P$ é o comprimento do prompt e $|\Theta|$ é a quantidade total de parâmetros do modelo. Como no decode processa-se apenas $1$ token a cada passagem dos gigabytes de pesos pela GPU, a taxa de operações por byte lido é mínima.

## 🧱 Hipóteses e condições de validade

- Aplica-se exclusivamente a arquiteturas autorregressivas baseadas em Transformer que utilizam representações em KV Cache para decodificação.

## ✅ Quando usar

- Métricas de dimensionamento de infraestrutura de inferência: separação de métricas entre **TTFT** (*Time to First Token*, dominado pelo prefill) e **TPOT** (*Time per Output Token*, dominado pelo decode).
- Arquiteturas avançadas de atendimento que desacoplam nós de prefill e decode em instâncias físicas separadas de hardware.

## 🚫 Quando não usar

- Em modelos puramente mascarados (como o BERT), que realizam apenas uma passagem de prefill estática sem fase de decode iterativo.

## ⚠️ Limitações e armadilhas

- **Disputa por recursos (*Interference*):** Executar prefill e decode na mesma GPU faz com que requisições longas de prefill drenem todo o poder de cálculo dos núcleos, pausando a geração contínua dos tokens de decode de outros usuários conectados e causando picos súbitos de latência.
- **Escalabilidade de memória do KV Cache:** Prompts maciços geram fases de prefill computacionalmente eficientes, mas deixam caches volumosos que limitam a quantidade de usuários que a GPU consegue manter no decode em paralelo.

## 🔍 Comparações

| Dimensão | Prefill (Pré-preenchimento) | Decode (Decodificação) |
|---|---|---|
| **Natureza matemática** | Paralela | Sequencial autoregressiva |
| **Gargalo no silício** | **Compute-Bound** (Cálculo puro) | **Memory-Bandwidth Bound** (Velocidade da memória) |
| **Aproveitamento da GPU** | Alto MFU (núcleos ocupados) | Baixo MFU (núcleos ociosos esperando dados) |
| **Métrica de usuário** | TTFT (*Time to First Token*) | TPOT (*Time per Output Token*) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um usuário cola um documento de 4.000 tokens e pede: `"Resuma em uma palavra"`.
- A GPU executa o **Prefill**: todos os 4.000 tokens são processados simultaneamente. A GPU opera em capacidade matemática máxima por 150 milissegundos e produz a palavra `"Aprovado"`.
- Um segundo usuário envia uma pergunta de 5 tokens: `"Conte uma história de 500 palavras"`.
- O Prefill dura apenas 5 milissegundos. Mas o **Decode** exige 500 passos sequenciais individuais; a cada uma das 500 palavras geradas, a GPU precisa carregar todos os 14 GB de pesos de um modelo de 7B da memória de alta velocidade para os processadores, levando 15 segundos no total para concluir a digitação.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/mecanismo-de-atencao.md|Mecanismo de Atenção]]
- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]

### Complementos

- [[redes/ai-engineering/conceitos/leis-de-escala-e-chinchilla.md|Leis de Escala e Chinchilla]]

### Alternativas

- Modelos de decodificação paralela especulativa ou arquiteturas de tempo linear como [[redes/ai-engineering/conceitos/modelos-de-espaco-de-estados.md|Modelos de Espaço de Estados (SSMs)]].

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]
- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 60, 407–414, 442–443
- **Evidência:** O texto define formalmente a dicotomia prefill/decode na página 60 e expande no Capítulo 9 demonstrando que o prefill é compute-bound e o decode é bandwidth-bound, justificando o surgimento de arquiteturas modernas que desacoplam essas duas etapas em instâncias dedicadas.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as distinções operacionais e computacionais entre as fases de Prefill e Decode na inferência de LLMs?
2. Por que a fase de Prefill é caracterizada como compute-bound, enquanto a fase de Decode é memory-bandwidth bound?
3. Qual é a correlação direta entre a fase de Prefill e a métrica de experiência do usuário TTFT (*Time to First Token*)?
4. Como a dependência autoregressiva impede a execução em lote paralelo da fase de Decode?
5. O que acontece com a intensidade aritmética da GPU quando o modelo gera respostas longas a partir de prompts curtos?
6. Por que o compartilhamento da mesma GPU para prefill e decode pode prejudicar o acordo de nível de serviço (SLO) de latência de uma aplicação?
7. Qual é o papel do KV Cache na transição entre o término do prefill e a continuidade das etapas de decode?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
