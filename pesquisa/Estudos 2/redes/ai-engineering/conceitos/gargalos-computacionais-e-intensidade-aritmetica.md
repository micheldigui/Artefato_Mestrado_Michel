# 🧠 Gargalos Computacionais e Intensidade Aritmética

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 407–410

## 📝 Definição

### Definição formal

Os **Gargalos Computacionais** em processamento de IA representam os limites físicos de silício que restringem a taxa de execução de uma carga de trabalho em um acelerador de hardware, determinados primariamente pelo equilíbrio da **Intensidade Aritmética** ($AI$) — a razão entre a quantidade total de operações de ponto flutuante (FLOPs) executadas e a quantidade total de bytes transferidos da memória física principal para os núcleos de computação do processador:
1. **Limitado por Computação (*Compute-Bound*):** Regime operacional no qual a intensidade aritmética da tarefa é superior à razão de capacidade de processamento sobre largura de banda da máquina, fazendo com que o tempo de execução seja governado pela velocidade máxima de cálculo em FLOP/s dos núcleos;
2. **Limitado por Largura de Banda de Memória (*Memory-Bandwidth Bound*):** Regime operacional no qual a intensidade aritmética é baixa, fazendo com que os núcleos de computação fiquem ociosos aguardando a transferência de tensores e parâmetros da memória física (HBM/DRAM), sendo o tempo de execução governado estritamente pela taxa de transferência de dados em GB/s.

O **Modelo Roofline** (Williams et al., 2009) é a representação analítica e geométrica bidimensional em escala logarítmica que mapeia o limite de desempenho atingível em função da intensidade aritmética do algoritmo e das especificações do hardware.

### Em linguagem simples

É a conta que explica por que a placa de vídeo fica lenta. Ela pode travar por dois motivos: ou porque tem contas demais para fazer e o cérebro dela está fritando no limite (**Compute-Bound**), ou porque as contas são simples, mas os números demoram para sair da memória e chegar ao processador (**Memory-Bandwidth Bound**). Na fase em que a IA lê sua pergunta (Prefill), ela sofre de limite de conta; na fase em que ela escreve a resposta letra por letra (Decode), ela sofre de limite de transferência de memória.

### Escopo e distinções

Não se confunde com "falta de espaço de memória" (*Out of Memory* / capacidade de VRAM). O limite de largura de banda refere-se à **velocidade do cano** que conecta o reservatório de memória aos núcleos matemáticos, e não ao volume total do reservatório.

## 🧩 Problema que resolve

Evita investimentos equivocados de infraestrutura e otimizações ineficazes. Se uma carga de trabalho é limitada por largura de banda de memória (como a decodificação de LLMs), comprar placas com o dobro de núcleos matemáticos (TFLOPs) não trará nenhum ganho de velocidade; a única solução eficaz é aumentar a velocidade da memória (HBM mais rápida), reduzir a quantidade de bytes transferidos via [[redes/ai-engineering/conceitos/quantizacao.md|quantização]] ou agrupar mais requisições via batching.

## 💡 Intuição

Pense em uma fábrica com operários montando caixas de brinquedos:
- **Compute-Bound:** A esteira de transporte joga milhares de peças plásticas rapidamente na bancada. Os operários têm todas as peças à mão, mas a montagem exige aparafusar 50 parafusos minúsculos. O gargalo é a velocidade das mãos dos operários aparafusando (**poder de cálculo da GPU**).
- **Memory-Bandwidth Bound:** A montagem é apenas encaixar uma única tampa plástica (operação trivial e instantânea). Contudo, a esteira mecânica que traz as caixas do depósito é estreita e lenta. Os operários passam $90\%$ do tempo de braços cruzados olhando para a esteira esperando a próxima caixa chegar (**largura de banda da memória**).

## ⚙️ Como funciona

O diagnóstico do gargalo é obtido confrontando a carga algorítmica contra o hardware:

### Etapas

1. **Cálculo da Intensidade Aritmética ($AI$):** O perfilador (como NVIDIA Nsight) calcula quantos FLOPs a camada executa para cada byte de parâmetros e ativações lidos da memória: $AI = \frac{\text{FLOPs}}{\text{Bytes}}$.
2. **Determinação do Ponto de Inflexão (*Ridge Point*):** Calcula-se a razão crítica da máquina:
   $$\text{Ponto de Inflexão} = \frac{\text{FLOP/s de Pico do Processador}}{\text{Largura de Banda de Memória de Pico (Bytes/s)}}$$
3. **Classificação no Modelo Roofline:**
   - *Se $AI < \text{Ponto de Inflexão}$:* A operação situa-se na rampa inclinada do gráfico $\implies$ **Memory-Bandwidth Bound**.
   - *Se $AI \ge \text{Ponto de Inflexão}$:* A operação atinge o teto horizontal do gráfico $\implies$ **Compute-Bound**.
4. **Mapeamento das Fases de LLM:**
   - **Prefill (Leitura):** Processa $P$ tokens em paralelo. Como os mesmos pesos do modelo são reutilizados para todos os $P$ tokens simultaneamente, a intensidade aritmética é alta $\implies$ **Compute-Bound**.
   - **Decode (Geração):** Gera 1 único token por vez. A GPU precisa carregar todos os gigabytes de pesos do modelo da memória para os núcleos para processar um único token $\implies$ **Memory-Bandwidth Bound**.

### Entradas e saídas

- **Entradas:** Código do kernel neural, dimensões de matrizes, batch size e especificações físicas de silício da GPU.
- **Saídas:** Classificação do regime de estrangulamento e gráfico Roofline calibrado.

## 📐 Formulação matemática

O desempenho teórico máximo alcançável $\mathcal{P}$ (em FLOP/s) sob o modelo Roofline é formalizado como o mínimo entre dois tetos:

$$\mathcal{P} = \min\Big(\mathcal{P}_{\text{pico}}, \; AI \times B_{\text{memória}}\Big)$$

Onde:
- $\mathcal{P}_{\text{pico}}$ é a capacidade matemática máxima de pico do chip (em FLOP/s);
- $B_{\text{memória}}$ é a largura de banda máxima da memória (em Bytes/s);
- $AI$ é a intensidade aritmética em FLOPs/Byte.

Para uma GPU NVIDIA H100 SXM (em precisão FP16/BF16 com Tensor Cores):
- $\mathcal{P}_{\text{pico}} \approx 1.979 \text{ TFLOP/s} = 1{,}979 \times 10^{15} \text{ FLOP/s}$;
- $B_{\text{memória}} \approx 3{,}35 \text{ TB/s} = 3{,}35 \times 10^{12} \text{ Bytes/s}$;
- O ponto de inflexão crítico é:
  $$\text{Ponto de Inflexão} = \frac{1{,}979 \times 10^{15}}{3{,}35 \times 10^{12}} \approx 590 \text{ FLOPs/Byte}$$
Qualquer operação que execute menos de 590 cálculos para cada byte transferido da HBM opera estritamente como **memory-bandwidth bound** na H100.

## 🧱 Hipóteses e condições de validade

- Assume que as transferências de dados ocorrem a partir da memória principal mais próxima (HBM na GPU); se houver transferências secundárias pelo barramento PCIe da CPU, a largura de banda efetiva despenca em até uma ordem de grandeza.

## ✅ Quando usar

- Diagnóstico preliminar obrigatório antes de qualquer projeto de otimização de sistemas de atendimento de IA.
- Justificativa para adoção de técnicas como batching contínuo, fusão de operadores em kernels e quantização de pesos.

## 🚫 Quando não usar

- Em softwares analíticos tradicionais puramente limitados por entrada e saída de disco mecânico (*I/O-bound*) ou requisições de rede externa.

## ⚠️ Limitações e armadilhas

- **Confundir falta de memória com gargalo de memória:** Ter VRAM suficiente para carregar um modelo não significa que a operação será rápida; se a largura de banda for lenta, a decodificação sofrerá severamente.
- **Ignorar a transição com o tamanho do lote:** Conforme o batch size de inferência cresce, a intensidade aritmética do decode se eleva, podendo transitar a carga de *memory-bound* para *compute-bound*.

## 🔍 Comparações

| Regime Computacional | O que limita a velocidade? | Como acelerar? | Exemplo Típico em LLMs |
|---|---|---|---|
| **Compute-Bound** | Velocidade de clock e núcleos da GPU | Usar chips com mais FLOP/s e formatos menores (FP8) | **Fase de Prefill (Prompt longo)** |
| **Memory-Bandwidth Bound** | Largura de banda de transferência (GB/s) | Aumentar batch size, quantizar pesos (INT4), HBM3 | **Fase de Decode (Geração sequencial)** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma equipe tenta rodar um modelo Llama 2 de 70B parâmetros para um único usuário ($B=1$) em uma GPU com 2 TB/s de largura de banda de memória.
- Cada parâmetro em FP16 consome 2 bytes: o modelo totaliza 140 GB de dados.
- Para gerar **apenas 1 token de resposta**, a GPU precisa transferir todos os 140 GB da memória HBM para seus núcleos.
- Tempo mínimo físico para transferir 140 GB a 2.000 GB/s:
  $$\text{Tempo} = \frac{140 \text{ GB}}{2.000 \text{ GB/s}} = 0{,}07 \text{ segundos} = 70 \text{ milissegundos por token}$$
Mesmo que a GPU tivesse 10 vezes mais núcleos matemáticos, ela **nunca** conseguiria gerar esse token em menos de 70 ms. A operação é puramente limitada por largura de banda de memória (*memory-bandwidth bound*).

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Complementos

- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]
- [[redes/ai-engineering/conceitos/aceleradores-de-ia-e-hierarquia-de-memoria.md|Aceleradores de IA e Hierarquia de Memória]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (representa os regimes físicos fundamentais da computação).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/quantizacao.md|Quantização]]
- [[redes/ai-engineering/conceitos/batching-continuo-e-dinamico.md|Batching Contínuo e Dinâmico]]
- [[redes/ai-engineering/conceitos/desacoplamento-de-prefill-e-decode.md|Desacoplamento de Prefill e Decode]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 407–410
- **Evidência:** Chip Huyen introduz o conceito de intensidade aritmética e o modelo Roofline originado por Williams et al. (2009), formaliza a dicotomia entre compute-bound e memory-bandwidth bound e demonstra por que a decodificação de LLMs é tipicamente memory-bandwidth bound enquanto o prefill é compute-bound.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é intensidade aritmética e como ela é calculada matematicamente para uma operação neural?
2. Como o modelo Roofline descreve graficamente os dois regimes fundamentais de limitação de hardware?
3. Por que a fase de Prefill de um LLM é caracterizada como compute-bound, enquanto o Decode é memory-bandwidth bound?
4. Qual é o papel do ponto de inflexão (*ridge point*) no gráfico Roofline de um acelerador como a NVIDIA H100?
5. Por que dobrar a capacidade de cálculo (TFLOP/s) de uma GPU não acelera a geração de tokens de um único usuário na fase de decode?
6. De que maneira o aumento do tamanho do lote (*batch size*) altera a intensidade aritmética na decodificação de modelos autorregressivos?
7. Como a técnica de quantização de pesos atua diretamente no alívio de gargalos de largura de banda de memória?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Métricas de Desempenho de Inferência

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 412–419

## 📝 Definição

### Definição formal

As **Métricas de Desempenho de Inferência** (*Inference Performance Metrics*) constituem a taxonomia quantitativa multidimensional empregada para mensurar a latência, a vazão, o cumprimento de acordos de nível de serviço e a eficiência de utilização de silício em servidores de atendimento de [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]], compreendendo quatro eixos avaliativos centrais:
1. **Decomposição da Latência:**
   - **TTFT (*Time to First Token*):** O intervalo temporal entre a submissão da consulta pelo cliente e a emissão do primeiro token da resposta (governado pelo prefill);
   - **TPOT (*Time per Output Token*):** O tempo médio gasto para decodificar cada token subsequente após o primeiro;
   - **ITL (*Inter-Token Latency*) / TBT (*Time Between Tokens*):** A variância e o tempo decorrido entre tokens consecutivos exibidos em modo de transmissão contínua (*streaming*).
2. **Métricas de Capacidade e Volume:**
   - **Throughput (Vazão):** A taxa agregada de tokens processados ou gerados por segundo através de todos os usuários concorrentes (TPS ou RPM);
   - **Goodput:** A fração de requisições ou tokens entregues com sucesso que satisfazem estritamente os acordos de nível de objetivo de serviço (**SLO**).
3. **Métricas de Utilização Física Real:**
   - **MFU (*Model FLOP/s Utilization*):** A razão percentual entre a vazão de cálculo observada e o teto teórico máximo de FLOP/s suportado pelo hardware;
   - **MBU (*Model Bandwidth Utilization*):** A razão percentual entre o tráfego de dados efetivamente transferido da memória e o teto teórico de largura de banda do chip.

### Em linguagem simples

É o painel de instrumentos do carro de corrida da IA. Não basta saber se o carro é "rápido": você precisa saber quantos segundos ele leva para dar a partida (**TTFT**), qual é a velocidade contínua de cruzeiro na estrada (**TPOT**), quantas pessoas ele consegue transportar de uma vez (**Throughput**) e quantas viagens chegaram no horário prometido sem atrasos irritantes (**Goodput**). Além disso, mostra se o motor está realmente sendo aproveitado no seu potencial máximo ou se você está queimando combustível à toa (**MFU e MBU**).

### Escopo e distinções

Supera o índice enganoso de "GPU Utilization" emitido por utilitários de sistema operacional (como `nvidia-smi`), que reporta $100\%$ de ocupação mesmo quando a GPU passa a maior parte do tempo ociosa esperando dados da memória. MFU e MBU quantificam a eficiência matemática real.

## 🧩 Problema que resolve

Resolve a miopia gerencial na contratação e calibração de infraestrutura de IA. Impede que equipes invistam em chips caros achando que a aplicação ficou rápida porque a "utilização da GPU" está em 100%, quando na verdade a experiência do usuário continua degradada com TTFT excessivo ou Goodput insatisfatório.

## 💡 Intuição

Pense em um garçom atendendo mesas em um restaurante:
- **TTFT:** É o tempo que o garçom leva para trazer a cesta de pães de cortesia na mesa assim que você senta. Se demorar 20 minutos, você fica furioso.
- **TPOT:** É a velocidade com que ele serve os pratos seguintes. Desde que chegue mais rápido do que você consegue mastigar (velocidade de leitura humana $\approx 6\text{--}8 \text{ tokens/s}$), o ritmo é confortável.
- **Throughput:** É o número total de pratos que a cozinha consegue entregar por hora para o salão inteiro.
- **Goodput:** É quantas mesas receberam a refeição completa antes de os clientes perderem a paciência e irem embora.
- **MFU:** Mostra se os cozinheiros estão realmente cozinhando em ritmo de alta gastronomia ou se estão de braços cruzados esperando a louça ser lavada.

## ⚙️ Como funciona

O monitoramento de métricas atua sobre o ciclo completo da requisição:

### Etapas

1. **Timestamp de Recepção ($T_0$):** O servidor de inferência registra o milissegundo exato em que a consulta do usuário chega ao gateway.
2. **Medição do Prefill ($T_{\text{primeiro}}$):** Registra o momento em que o modelo emite o primeiro token:
   $$\text{TTFT} = T_{\text{primeiro}} - T_0$$
3. **Monitoramento do Streaming de Decode:** A cada novo token gerado, registra-se o delta temporal em relação ao token anterior ($\text{ITL}$).
4. **Finalização da Sequência ($T_{\text{fim}}$):** Ao emitir o token $\text{<EOS>}$ com $N_{\text{saída}}$ tokens:
   $$\text{TPOT} = \frac{T_{\text{fim}} - T_{\text{primeiro}}}{N_{\text{saída}} - 1}$$
5. **Auditoria Estatística por Percentis:** Consolida-se a distribuição de latências observando não a média aritmética simples (que mascara outliers causados por instabilidades de rede), mas os percentis **p50 (mediana)**, **p90**, **p95** e **p99**.
6. **Cálculo do Goodput:** Filtram-se apenas as requisições em que $\text{TTFT} \le \text{Limite}_{\text{SLO}}$ e $\text{TPOT} \le \text{Limite}_{\text{SLO}}$.

### Entradas e saídas

- **Entradas:** Logs de telemetria de timestamps por token e contadores de hardware da GPU.
- **Saídas:** Painéis de observabilidade de latência, vazão e índices MFU/MBU consolidados.

## 📐 Formulação matemática

A formulação do **Model Bandwidth Utilization (MBU)** para um modelo de $N$ parâmetros com $b$ bytes por parâmetro gerando uma vazão de $S_{\text{tokens}}$ tokens por segundo em uma GPU com largura de banda teórica $B_{\text{teórica}}$ é:

$$\text{MBU} = \frac{N \times b \times S_{\text{tokens}}}{B_{\text{teórica}}}$$

O **Model FLOP/s Utilization (MFU)** compara a vazão real observada contra o teto teórico do chip $\mathcal{F}_{\text{pico}}$ (onde cada token de prefill consome $2N$ FLOPs e cada token de decode consome $2N$ FLOPs em modelos densos):

$$\text{MFU} = \frac{2 \times N \times \text{Throughput}_{\text{tokens/s}}}{\mathcal{F}_{\text{pico}}}$$

O cálculo do capítulo demonstra que na decodificação do Llama 2-70B em FP16 ($b=2$ bytes) gerando $100 \text{ tokens/s}$ em uma GPU com $2 \text{ TB/s}$ ($2.000 \text{ GB/s}$) de largura de banda:

$$\text{Tráfego Real} = 70 \times 10^9 \times 2 \times 100 = 700 \text{ GB/s} \implies \text{MBU} = \frac{700}{2.000} = 35\%$$

## 🧱 Hipóteses e condições de validade

- Para que o TPOT seja perceptivelmente confortável em interfaces com usuário humano em modo streaming, a taxa de emissão deve ser superior à velocidade média de leitura humana (cerca de 120 ms por token ou $\ge 8 \text{ tokens/segundo}$).
- As métricas de latência devem ser calculadas no nível do cliente final (*client-perceived latency*), englobando atrasos de rede e serialização de proxies.

## ✅ Quando usar

- Definição formal de acordos de nível de serviço (SLAs/SLOs) entre equipes de infraestrutura de IA e produtos de negócio.
- Dimensionamento de custos de inferência em pipelines de integração contínua e testes de carga.
- Benchmark de provedores de API concorrentes para identificar qual serviço entrega menor TTFT sob tráfego pesado.

## 🚫 Quando não usar

- Em pipelines de pré-processamento estático em lote (*offline batch processing*), onde o usuário não está esperando na tela e a única métrica que importa é o custo total por milhão de tokens.

## ⚠️ Limitações e armadilhas

- **A falha da média simples em latência:** Uma média de TTFT de 390 ms pode esconder que $10\%$ dos usuários enfrentaram tempos de espera de mais de 3 segundos devido a prompts longos ou enfileiramento na GPU. Avalie sempre o **p99**.
- **O paradoxo do "tempo até publicar":** Em agentes ou tarefas com Cadeia de Pensamento (CoT), o modelo emite o primeiro token internamente de forma rápida, mas o usuário só vê o primeiro caractere da resposta final minutos depois. Meça o tempo até a exibição real para o usuário (*time to publish*).

## 🔍 Comparações

| Métrica | O que mede? | Alvo de Otimização | Impacto Principal |
|---|---|---|---|
| **TTFT** | Tempo até a 1ª palavra surgir | Fase de Prefill da GPU | Percepção imediata de agilidade do app |
| **TPOT** | Tempo entre cada palavra seguinte | Fase de Decode da GPU | Fluidez de leitura do texto em streaming |
| **Throughput** | Volume total de tokens/s do servidor | Aproveitamento global da infra | Redução direta do custo por requisição |
| **Goodput** | Requisições entregues dentro do prazo | Qualidade real de serviço | Satisfação contratual e retenção de usuários |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma empresa de telemedicina define um SLO estrito para seu copiloto de atendimento:
- Limite de TTFT: no máximo **500 ms**;
- Limite de TPOT: no máximo **50 ms/token**.
O servidor recebe 1.000 chamadas simultâneas. 
O relatório mostra que a máquina gerou $2.500 \text{ tokens/segundo}$ (**alto Throughput**). 
Contudo, devido ao enfileiramento pesado, 400 médicos esperaram mais de 2 segundos pelo primeiro token. 
O engenheiro analisa o painel: embora o Throughput pareça espetacular para a equipe de custos, o **Goodput foi de apenas 600 requisições** ($60\%$). Quatrocentos médicos tiveram uma experiência inaceitável, indicando que a empresa precisa provisionar mais réplicas para honrar o SLO de negócio.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Complementos

- [[redes/ai-engineering/conceitos/aceleradores-de-ia-e-hierarquia-de-memoria.md|Aceleradores de IA e Hierarquia de Memória]]
- [[redes/ai-engineering/conceitos/desacoplamento-de-prefill-e-decode.md|Desacoplamento de Prefill e Decode]]

### Alternativas

- Uso ingênuo da métrica de GPU Utilization do comando `nvidia-smi`.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/batching-continuo-e-dinamico.md|Batching Contínuo e Dinâmico]]
- [[redes/ai-engineering/conceitos/decodificacao-especulativa-e-paralela.md|Decodificação Especulativa e Paralela]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 412–419
- **Evidência:** Chip Huyen formaliza o vocabulário de métricas de inferência, desconstrói as falhas do comando nvidia-smi para medição de GPU, formaliza as equações de MFU (introduzido no artigo do PaLM, Chowdhery et al., 2022) e MBU, e detalha a Tabela 9-1 com a utilização empírica de aceleradores no GPT-3, Gopher e PaLM.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as métricas fundamentais que compõem a decomposição da latência em modelos de linguagem autorregressivos?
2. Por que a métrica de "GPU Utilization" emitida pelo utilitário `nvidia-smi` é considerada enganosa por engenheiros de sistemas de IA?
3. O que representam conceitualmente as métricas MFU (*Model FLOP/s Utilization*) e MBU (*Model Bandwidth Utilization*)?
4. Qual é a distinção técnica entre Throughput bruto de tokens e Goodput sob um acordo de nível de objetivo de serviço (SLO)?
5. Por que avaliar a latência de uma aplicação apenas pela média aritmética simples é uma prática metodológica inadequada?
6. Como o conceito de "Time to Publish" se aplica a sistemas que utilizam raciocínio encadeado (Chain-of-Thought) ou agentes?
7. Qual é a velocidade aproximada de geração de tokens por segundo (TPOT) recomendada para que a decodificação acompanhe a velocidade de leitura humana?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Aceleradores de IA e Hierarquia de Memória

**Rede:** `ai-engineering`  
**Área:** `infraestrutura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 419–425

## 📝 Definição

### Definição formal

Os **Aceleradores de IA e sua Hierarquia de Memória** (*AI Accelerators and Memory Hierarchy*) compreendem o conjunto de circuitos integrados de aplicação específica (ASICs) ou processadores paralelos massivos (GPUs, TPUs, IPUs, LPUs) projetados para acelerar primitivas matemáticas de multiplicação e adição matricial (GEMM), organizados em torno de uma arquitetura física de memória em camadas estratificadas por velocidade e capacidade:
1. **Memória do Sistema / Host (DRAM da CPU):** Alta capacidade de armazenamento (centenas de GB a TB), mas com menor largura de banda de transferência ($25\text{--}50 \text{ GB/s}$);
2. **Memória de Alta Largura de Banda da GPU (HBM / VRAM):** Memória dedicada empilhada em três dimensões integrada fisicamente ao substrato do acelerador, fornecendo largura de banda intermediária massiva ($1\text{--}3{,}5 \text{ TB/s}$) e capacidade média ($24\text{--}80 \text{ GB}$ por chip);
3. **Memória Estática Integrada no Silício (*On-Chip SRAM*):** Registradores internos e caches $L_1, L_2, L_3$ embutidos diretamente ao lado das unidades lógicas e aritméticas (ALUs), operando com larguras de banda colossais ($> 10 \text{ TB/s}$), porém com capacidade física diminuta (tipicamente $< 50 \text{ MB}$).

### Em linguagem simples

É a estrutura física dos computadores construídos para IA. Uma CPU comum de notebook é como um professor solitário genial que resolve contas difíceis sozinho. Uma GPU é como um exército de 10.000 operários fazendo continhas de multiplicar ao mesmo tempo. Para alimentar esse exército, o chip tem três níveis de despensa: um armazém distante e gigante (a memória da CPU), uma geladeira rápida ao lado da mesa (a memória HBM da placa de vídeo) e o bolso do avental do operário (a memória SRAM dentro do chip), onde tudo é instantâneo mas cabe pouquíssima coisa.

### Escopo e distinções

Não abrange apenas placas gráficas para jogos. Na era dos modelos de fundação, engloba chips especializados exclusivamente na fase de inferência (como Apple Neural Engine, AWS Inferentia, Meta MTIA e Groq LPU), otimizados para menor consumo térmico e operações em precisão reduzida (INT8, FP4).

## 🧩 Problema que resolve

Resolve a lentidão física das CPUs tradicionais em operações de multiplicação de tensores e matrizes, que compõem mais de 90% dos cálculos de redes neurais profundas. Permite paralelizar trilhões de operações matemáticas por segundo respeitando as restrições térmicas e de largura de banda do silício.

## 💡 Intuição

Pense em abastecer uma equipe de pedreiros construindo um muro de tijolos:
- A **DRAM da CPU** é o depósito de materiais de construção no outro bairro. Tem milhões de tijolos guardados, mas o caminhão leva meia hora para trazer cada carga até o canteiro de obras.
- A **HBM da GPU** é a pilha de tijolos descarregada no quintal da obra. Os tijolos chegam à mão dos operários em carrinhos de mão rápidos em poucos segundos.
- A **SRAM On-Chip** é a mão do pedreiro segurando os dois tijolos que ele vai assentar com cimento exatamente agora. A ação é instantânea, mas ele só consegue segurar dois tijolos por vez.

## ⚙️ Como funciona

O tráfego de instruções e dados nos aceleradores navega verticalmente pela hierarquia:

### Etapas

1. **Despacho pelo Host:** A CPU prepara as matrizes de entrada e despacha comandos de execução para o acelerador através do barramento PCIe.
2. **Carga na HBM:** Os parâmetros e dados da requisição residem na memória física HBM da GPU.
3. **Puxada para a SRAM (Tiling):** Para evitar que os núcleos de processamento esperem os ciclos lentos da HBM, blocos de tensores (*tiles*) são transferidos em alta velocidade para a memória SRAM interna compartilhada.
4. **Execução nos Núcleos Tensores (*Tensor Cores*):** As unidades matemáticas realizam multiplicações e acumulações matriciais em passos únicos de clock.
5. **Dissipação Térmica e Energia:** O consumo elétrico escala com a atividade dos transistores; o limite de dissipação térmica do chip (**TDP** — *Thermal Design Power*) determina o teto de frequência de operação contínua sem que o hardware sofra estrangulamento térmico (*thermal throttling*).

### Entradas e saídas

- **Entradas:** Tensores armazenados em memória DRAM/HBM e comandos de controle de kernel.
- **Saídas:** Tensores resultantes de ativações gravados de volta na memória e calor físico dissipado pelos radiadores de resfriamento.

## 📐 Formulação matemática

O desempenho computacional de um acelerador quantifica-se em FLOP/s por precisão de ponto flutuante. 
Em uma GPU como a NVIDIA H100 SXM, a relação entre precisão e capacidade computacional atinge:
- TF32 Tensor Core: $989 \text{ TFLOP/s}$;
- FP16 / BF16 Tensor Core: $1.979 \text{ TFLOP/s}$;
- FP8 Tensor Core: $3.958 \text{ TFLOP/s}$.

A cada redução de precisão pela metade (de 16 bits para 8 bits), a taxa de processamento de operações **dobra** no silício devido ao empacotamento vetorial nos núcleos.
A potência térmica do acelerador é delimitada pelo TDP (ex.: $700 \text{ Watts}$ para uma única GPU H100). Um cluster industrial operando a pico consome anualmente cerca de:

$$\text{Energia}_{\text{anual}} \approx 700 \text{ W} \times 24 \text{ h} \times 365 \text{ dias} \approx 6.132 \text{ kWh}$$

Equivalente a quase dois terços do consumo elétrico anual total de uma residência média nos Estados Unidos.

## 🧱 Hipóteses e condições de validade

- Para aproveitar a largura de banda teórica da HBM, as requisições de memória devem ser alinhadas e contíguas (*memory coalescing*); acessos desordenados ou fragmentados degradam a taxa de transferência para valores comparáveis à memória comum.

## ✅ Quando usar

- GPUs com HBM de grande porte (A100, H100, H200): mandatórias para pré-treinamento, ajuste fino de grande porte e inferência com modelos densos massivos.
- Chips especializados em inferência (AWS Inferentia, Groq LPU): recomendados para otimização de custo por token em inferência corporativa com tráfego previsível.
- NPUs e aceleradores de borda (Apple Neural Engine): indispensáveis para execução local de modelos de até 3B ou 7B em smartphones e computadores pessoais.

## 🚫 Quando não usar

- Não tente rodar inferência de LLMs em larga escala utilizando servidores baseados exclusivamente em CPUs comuns sem aceleradores, sob pena de latências centenas de vezes piores.

## ⚠️ Limitações e armadilhas

- **O gargalo do barramento PCIe:** Se o modelo for maior que a memória da GPU e exigir que partes dos pesos fiquem na CPU memory, a velocidade de transferência entre a CPU e a GPU pelo barramento PCIe torna-se o estrangulamento dominante da aplicação.
- **O desafio do resfriamento em data centers:** Montar clusters de centenas de GPUs sem projetos avançados de refrigeração líquida ou climatização industrial causa desligamentos automáticos por segurança térmica.

## 🔍 Comparações

| Nível de Memória | Localização Física | Largura de Banda Típica | Capacidade Típica | Custo por Gigabyte |
|---|---|---|---|---|
| **CPU DRAM** | Placa-mãe do servidor | $25\text{--}50 \text{ GB/s}$ | $128 \text{ GB a } 2 \text{ TB}$ | Muito Baixo |
| **GPU HBM3** | Empilhada no substrato da GPU | **$1\text{--}3{,}5 \text{ TB/s}$** | $24 \text{ a } 141 \text{ GB}$ | Alto |
| **SRAM On-Chip** | Dentro do silício de cálculo | **$> 10 \text{ TB/s}$** | $20 \text{ a } 50 \text{ MB}$ | **Extremamente Alto** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um engenheiro tenta otimizar o kernel de atenção de um modelo de linguagem:
- No código ingênuo, a GPU calcula o produto de matrizes da atenção, grava o resultado intermediário na **HBM** lenta (gastando milissegundos preciosos no cano de 2 TB/s) e depois lê esse dado de volta para aplicar a função Softmax.
- Com um kernel avançado como o **FlashAttention**, o código é reescrito para fatiar as matrizes em bloquinhos que cabem inteiramente dentro da **SRAM on-chip** (a memória ultrarrápida de 10 TB/s dentro do processador). O cálculo do produto e a Softmax ocorrem diretamente na SRAM sem nenhuma leitura ou gravação intermediária na HBM. O processamento da camada atinge aceleração de até 3 a 4 vezes apenas respeitando a hierarquia física de memória.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]
- [[redes/ai-engineering/conceitos/representacoes-numericas-e-precisao.md|Representações Numéricas e Precisão]]

### Complementos

- [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|Otimização do KV Cache e PagedAttention]]
- [[redes/ai-engineering/conceitos/kernels-e-compiladores-de-ia.md|Kernels e Compiladores de IA]]

### Alternativas

- Uso exclusivo de CPUs de múltiplos núcleos para tarefas estritamente lineares.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]
- [[redes/ai-engineering/conceitos/gargalos-de-escala.md|Gargalos de Escala: Dados e Energia]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 419–425
- **Evidência:** Chip Huyen formaliza a arquitetura dos aceleradores de IA, apresenta a Tabela 9-2 com especificações de TFLOP/s da NVIDIA H100 SXM para diferentes formatos de precisão, ilustra o diagrama da hierarquia de três níveis de memória (Figura 9-7) e discute a crise de potência elétrica e limites de TDP de data centers.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a diferença arquitetural de propósito geral entre CPUs e GPUs no processamento de dados?
2. Quais são os três níveis que compõem a hierarquia de memória acessível a um acelerador de inteligência artificial?
3. Por que a memória de alta largura de banda (HBM) é crucial para mitigar o gargalo de decodificação sequencial de LLMs?
4. Como a capacidade de processamento em FLOP/s de uma GPU como a NVIDIA H100 escala ao reduzir a precisão de FP16 para FP8?
5. O que representa o TDP (*Thermal Design Power*) de um chip acelerador e qual o seu impacto na infraestrutura física de data centers?
6. Qual é a função da memória estática on-chip (SRAM) e por que ela viabiliza a criação de kernels otimizados como o FlashAttention?
7. Por que a transferência de tensores através do barramento PCIe entre a CPU e a GPU atua frequentemente como estrangulamento em modelos particionados?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Otimização do KV Cache e PagedAttention

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 433–436

## 📝 Definição

### Definição formal

A **Otimização do KV Cache e PagedAttention** compreende o conjunto de intervenções matemáticas, arquiteturais e de gerenciamento de memória voltadas a mitigar a saturação de VRAM provocada pela retenção contínua dos tensores de chaves (*Keys*) e valores (*Values*) durante a decodificação autorregressiva de modelos Transformer:
1. **KV Cache:** O buffer de memória física que armazena os vetores $K$ e $V$ de todos os tokens anteriores de uma sequência para evitar o recálculo redundante da atenção a cada novo passo de decodificação;
2. **Redesign da Atenção:** Modificações estruturais na arquitetura do modelo que reduzem a quantidade física de pares chave-valor mantidos no cache, destacando-se a **Atenção de Consulta Agrupada (*Grouped-Query Attention* — GQA)** e a **Atenção Multi-Consulta (*Multi-Query Attention* — MQA)**;
3. **PagedAttention (Kwon et al., 2023 / vLLM):** Algoritmo de gerenciamento de memória inspirado na paginação de memória virtual de sistemas operacionais, que particiona o KV Cache em blocos físicos não contíguos na memória da GPU, eliminando a fragmentação interna e externa e viabilizando o compartilhamento flexível de memória entre requisições paralelas;
4. **FlashAttention (Dao et al., 2022):** Kernel de aceleração de computação exata de atenção que divide matrizes em blocos para realizar o cálculo inteiro dentro da SRAM rápida on-chip sem gravar matrizes intermediárias completas na HBM lenta.

### Em linguagem simples

É a solução de engenharia para o maior devorador de memória da IA durante a conversa. Toda vez que a IA gera uma palavra nova, ela precisa lembrar das palavras antigas; para não ter que reler tudo do zero a cada letra, ela guarda uma "cola matemática" na memória (o KV Cache). Só que essa cola cresce tanto em conversas longas que enche toda a memória da placa de vídeo. O PagedAttention organiza essa cola em "páginas soltas" como se fosse a memória do Windows, acabando com o desperdício de espaço, e o GQA faz as cabeças de atenção compartilharem a mesma cola para economizar até $80\%$ de memória.

### Escopo e distinções

O KV Cache é utilizado **exclusivamente durante a inferência**, nunca no treinamento. No treinamento, como a sequência inteira de tokens futuros já é conhecida em avanço, todos os cálculos de atenção são executados simultaneamente em paralelo, tornando o armazenamento de estados passados desnecessário.

## 🧩 Problema que resolve

Resolve a barreira de contexto longo e o desperdício de memória em servidores de atendimento de LLMs. Na alocação tradicional de tensores, o sistema precisava pré-alocar um bloco contíguo de VRAM gigante na GPU para cada usuário, reservando espaço para a janela máxima possível (ex.: 4.000 tokens), mesmo que o usuário só usasse 50 tokens. Essa fragmentação desperdiçava de $60\%$ a $80\%$ da memória da GPU, impedindo o servidor de atender múltiplos clientes em paralelo.

## 💡 Intuição

Pense em um hotel com quartos gigantes:
- Na **alocação tradicional de KV Cache**, se uma família de 2 pessoas chega ao hotel, a gerência reserva um andar inteiro de 100 quartos contíguos trancados exclusivamente para eles, caso decidam convidar parentes mais tarde. Os quartos ficam vazios, ninguém mais pode usar e o hotel lota com apenas 5 hóspedes (**fragmentação de memória**).
- Com o **PagedAttention**, a gerência distribui chaves de quartos individuais conforme as pessoas chegam. Se a família tem 2 pessoas, eles ganham 2 quartos no 1º andar; se chegar um parente amanhã, o parente ganha um quarto no 4º andar. A memória é preenchida bloco a bloco sem desperdício de espaço vago.

## ⚙️ Como funciona

O gerenciamento articula transformações arquiteturais e estruturas de dados de paginação:

### Etapas

1. **Atenção Agrupada (GQA):** Em vez de cada cabeça de atenção ter seu próprio par exclusivo de $K$ e $V$, o modelo agrupa as cabeças de consulta ($Q$) para compartilhar um único par de $K$ e $V$. No Llama 3, 32 cabeças de consulta compartilham 8 cabeças de $K, V$ (redução de $4\times$ no tamanho físico do cache).
2. **Alocação por Blocos no PagedAttention:** O servidor (vLLM) divide a VRAM livre em blocos lógicos de tamanho fixo (ex.: blocos que comportam 16 tokens).
3. **Mapeamento via Tabela de Blocos (*Block Table*):** A aplicação mantém uma tabela de tradução análoga à tabela de páginas do sistema operacional, mapeando blocos lógicos de tokens para blocos físicos dispersos na HBM.
4. **Alocação Dinâmica Sob Demanda:** Conforme novos tokens são emitidos na decodificação sequencial, novos blocos físicos são alocados apenas quando o bloco atual é totalmente preenchido.
5. **Compartilhamento de Memória por Cópia em Gravação (*Copy-on-Write*):** Se 10 usuários fazem perguntas sobre o mesmo prompt de sistema, todos compartilham os mesmos blocos físicos do prompt na VRAM; blocos separados só são alocados quando suas respostas individuais começam a divergir.

### Entradas e saídas

- **Entradas:** Vetores de atenção emitidos durante a decodificação sequencial.
- **Saídas:** Acesso instantâneo e contíguo a representações históricas com zero desperdício de fragmentação física.

## 📐 Formulação matemática

O tamanho bruto da memória necessária para armazenar o KV Cache completo de um lote de requisições em um modelo Transformer autorregressivo sem otimização de agrupamento é calculado por:

$$\text{Memória}_{\text{KV\_Cache}} = 2 \times B \times S \times L \times H \times M \text{ bytes}$$

Onde:
- $2$ representa os dois vetores armazenados ($K$ e $V$);
- $B$ é o tamanho do lote (*batch size*);
- $S$ é o comprimento da sequência em tokens;
- $L$ é o número de camadas Transformer (*layers*);
- $H$ é a dimensão oculta do modelo (*hidden dimension*);
- $M$ é o número de bytes por valor na representação numérica (ex.: $M=2$ para FP16/BF16).

No caso do **Llama 2-13B** ($L = 40$, $H = 5.120$, em 16 bits $M=2$):
Para um lote moderado de $B = 32$ usuários e contexto longo de $S = 2.048$ tokens:
$$\text{Memória}_{\text{KV}} = 2 \times 32 \times 2.048 \times 40 \times 5.120 \times 2 \approx 53{,}68 \text{ GB}$$
O KV Cache sozinho consome mais de 53 GB de VRAM, superando com folga os 26 GB exigidos pelos pesos do próprio modelo. 

Com a adoção de **Grouped-Query Attention (GQA)** com razão de agrupamento $G = \frac{H_Q}{H_{KV}}$:

$$\text{Memória}_{\text{GQA}} = \frac{\text{Memória}_{\text{KV}}}{G}$$

Se $G = 4$, a pegada cai de 53,68 GB para apenas **13,42 GB**.

## 🧱 Hipóteses e condições de validade

- O uso de GQA exige que o modelo tenha sido pré-treinado ou explicitamente ajustado nessa arquitetura de cabeças agrupadas.
- O PagedAttention pressupõe o suporte a kernels customizados de leitura que consigam ler vetores em blocos físicos dispersos de memória sem penalidade excessiva de latência.

## ✅ Quando usar

- Mandatório em servidores de inferência corporativos (vLLM, TensorRT-LLM, TGI) para suportar múltiplos usuários concorrentes.
- Aplicações com diálogos longos (como o caso da Character.AI com 180 mensagens) e sistemas de RAG com documentos extensos.

## 🚫 Quando não usar

- Em modelos de processamento único de tarefas curtíssimas (ex.: classificação de sentimento de 10 palavras em lote unitário), onde a sobrecarga do cache é insignificante.

## ⚠️ Limitações e armadilhas

- **Sobrecarga de Ejeção (*Eviction*):** Se a memória física da GPU for totalmente preenchida pelos blocos de PagedAttention durante um pico de tráfego, o servidor precisa pausar e ejetar blocos para a memória da CPU ou descartá-los para recalcular mais tarde, gerando picos súbitos de latência.

## 🔍 Comparações

| Técnica | Alvo de Otimização | Mecanismo | Impacto Principal |
|---|---|---|---|
| **Multi-Query Attention (MQA)**| Arquitetura do Modelo | 1 único par $K, V$ para todas as cabeças | Redução máxima de VRAM, leve perda de acurácia |
| **Grouped-Query Attention (GQA)**| Arquitetura do Modelo | Grupos de cabeças compartilham $K, V$ | **Equilíbrio perfeito entre qualidade e memória** |
| **PagedAttention** | Sistema Operacional do Servidor| Paginação em blocos não contíguos | **Elimina desperdício e dobra a capacidade de lote** |
| **FlashAttention** | Silício / Kernel de Execução | Computação em blocos dentro da SRAM | **Acelera o tempo de cálculo em até 3x** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um servidor rodando um modelo de 70B parâmetros atende a 10 alunos universitários que abriram o mesmo livro de biologia de 8.000 tokens para fazer perguntas diferentes:
- *Sem PagedAttention:* O servidor precisa alocar 10 blocos contíguos de 8.000 tokens na VRAM. O livro de biologia é duplicado 10 vezes na memória da GPU, ocupando centenas de gigabytes e derrubando o servidor com *Out of Memory*.
- *Com PagedAttention:* Os 8.000 tokens do livro de biologia são gravados **uma única vez** em blocos de memória física compartilhada. Todos os 10 alunos leem os mesmos blocos físicos. O servidor só cria blocos novos e pequenos para as perguntas e respostas específicas de cada aluno, permitindo atender os 10 estudantes na mesma máquina que antes não aguentava dois.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/mecanismo-de-atencao.md|Mecanismo de Atenção]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Complementos

- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]
- [[redes/ai-engineering/conceitos/batching-continuo-e-dinamico.md|Batching Contínuo e Dinâmico]]

### Alternativas

- Arquiteturas de tempo linear que dispensam o KV Cache por completo ([[redes/ai-engineering/conceitos/modelos-de-espaco-de-estados.md|Modelos de Espaço de Estados (SSMs)]]).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/aceleradores-de-ia-e-hierarquia-de-memoria.md|Aceleradores de IA e Hierarquia de Memória]]
- [[redes/ai-engineering/conceitos/prompt-caching-e-reutilizacao-de-contexto.md|Prompt Caching e Reutilização de Contexto]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 433–436
- **Evidência:** Chip Huyen formaliza a equação aritmética do KV Cache no Llama 2-13B (resultando em 54 GB de memória), detalha as inovações de redesenho de atenção (GQA de Ainslie et al., 2023; MQA de Shazeer, 2019), cita o caso real da Character.AI que reduziu o cache em mais de 20 vezes, explica a paginação de memória do PagedAttention (Kwon et al., 2023 no vLLM) e a aceleração de kernels com FlashAttention (Dao et al., 2022).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é o KV Cache e por que ele é utilizado exclusivamente durante a inferência e nunca no treinamento de LLMs?
2. Como funciona a fórmula de cálculo da memória exigida pelo KV Cache e quais variáveis a fazem crescer de forma crítica?
3. Qual é a diferença arquitetural entre Multi-Head Attention (MHA), Multi-Query Attention (MQA) e Grouped-Query Attention (GQA)?
4. Como o algoritmo PagedAttention do framework vLLM soluciona o problema da fragmentação interna e externa de memória da GPU?
5. De que maneira a técnica de cópia em gravação (*copy-on-write*) do PagedAttention viabiliza o compartilhamento de prompts idênticos entre múltiplos usuários?
6. Como o kernel FlashAttention utiliza a hierarquia de memória da GPU (SRAM versus HBM) para acelerar a atenção sem perdas matemáticas?
7. Como a empresa Character.AI estruturou sua arquitetura de atenção para conseguir atender conversas com históricos médios de 180 mensagens sem estouro de memória?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Decodificação Especulativa e Paralela

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 428–433

## 📝 Definição

### Definição formal

A **Decodificação Especulativa e Paralela** (*Speculative and Parallel Decoding*) compreende o conjunto de técnicas algorítmicas projetadas para romper o gargalo estritamente sequencial da decodificação autorregressiva em modelos de linguagem, viabilizando a emissão de múltiplos tokens de saída por passo de relógio sem degradar a distribuição matemática do modelo alvo:
1. **Decodificação Especulativa (*Speculative Decoding* / *Speculative Sampling*):** Um modelo rascunho (*draft model*) menor, mais leve e mais rápido gera estocasticamente uma sequência de $K$ tokens candidatos; o modelo alvo (*target model*) maior avalia todos os $K$ tokens em paralelo em um único passo de prefill, aceitando a maior subsequência coerente com sua própria distribuição e corrigindo o primeiro token divergente;
2. **Inferência com Referência (*Inference with Reference*):** Variante sem modelo auxiliar que copia trechos de tokens diretamente do contexto de entrada (como código existente ou documentos em RAG) como rascunhos para validação paralela;
3. **Decodificação Paralela Não-Autoregressiva (Medusa / Jacobi):** Técnicas que utilizam cabeças de predição adicionais treinadas sobre o mesmo modelo base para prever múltiplos tokens futuros concorrentes ($x_{t+1}, x_{t+2}, \dots$) em paralelo, estruturados em árvores de atenção avaliadas simultaneamente.

### Em linguagem simples

É o truque para fazer a IA parar de digitar devagarzinho uma palavra por vez. Em vez de colocar o modelo gigante para pensar em cada vírgula, você coloca um modelo menor e ultrarrápido para "chutar" as próximas 5 palavras de uma vez (o rascunho). Em seguida, o modelo grande apenas passa os olhos por todas as 5 palavras de uma só vez para carimbar as que estão certas. Se o modelo pequeno acertou 4 palavras, o sistema cospe 4 palavras na tela no mesmo tempo que antes levava para escrever uma única palavra, sem mudar em nada o texto final.

### Escopo e distinções

A decodificação especulativa clássica é uma técnica **sem perdas (*lossless*)**. O texto final produzido é matematicamente indistinguível daquele que seria gerado se o modelo alvo grande tivesse rodado sozinho passo a passo.

## 🧩 Problema que resolve

Resolve o estrangulamento de largura de banda de memória (*memory-bandwidth bound*) da fase de decode. Como a decodificação tradicional gera apenas 1 token por passagem dos pesos na memória física da GPU, os núcleos matemáticos passam a maior parte do tempo ociosos. A decodificação especulativa aproveita esses FLOPs computacionais ociosos para verificar múltiplos tokens simultaneamente a custo zero de transferência adicional.

## 💡 Intuição

Pense em um escritor famoso e premiado que tem um prazo apertadíssimo para entregar um livro:
- No **modo tradicional**, o escritor senta e digita cada letra no teclado sozinho, pensando em cada palavra. O processo é lento e desgastante.
- Na **decodificação especulativa**, o escritor contrata um estagiário rápido de digitação (**o modelo draft**). O estagiário redige rascunhos rápidos das próximas duas frases. O escritor experiente bate o olho no parágrafo em meio segundo: ele aprova as primeiras 8 palavras, risca a 9ª palavra que estava feia e escreve a palavra correta por cima. Ele avançou quase uma frase inteira com um único olhar crítico.

## ⚙️ Como funciona

O ciclo de especulação e conferência opera em um loop contínuo:

### Etapas

1. **Geração do Rascunho:** O modelo rascunho (ex.: um modelo de 1B parâmetros) gera $K$ tokens sequenciais rápidos: $[x_{t+1}, x_{t+2}, \dots, x_{t+K}]$.
2. **Verificação Paralela:** O modelo alvo (ex.: um modelo de 70B parâmetros) processa os $K$ tokens de uma só vez em modo paralelo (exatamente como se fosse uma fase de prefill).
3. **Critério de Aceitação:** O modelo alvo compara a probabilidade de cada token rascunhado contra sua própria distribuição:
   - Os tokens são aceitos da esquerda para a direita até o ponto da primeira divergência estatística;
   - Se o modelo alvo aceitar $j$ tokens ($j \le K$), o próprio modelo alvo gera deterministicamente o token subsequente $x_{t+j+1}$.
4. **Ciclo de Reinício:** A sequência aceita é anexada ao histórico acumulado e o modelo rascunho inicia a especulação dos próximos $K$ tokens a partir dessa nova posição.
5. **Ganho Líquido:** Se $j = K$, o sistema emitiu $K + 1$ tokens em uma única chamada do modelo alvo grande. Se $j = 0$ (o modelo rascunho errou logo o primeiro token), o modelo alvo ainda assim emitiu 1 token correto garantido, garantindo que o sistema nunca regrida.

### Entradas e saídas

- **Entradas:** Contexto atual, modelo alvo e modelo rascunho (ou cabeças de decodificação Medusa).
- **Saídas:** Emissão em bloco de múltiplos tokens validados sem desvios probabilísticos.

## 📐 Formulação matemática

Seja $M_{\text{alvo}}$ o modelo alvo que define a distribuição $P(x)$ e seja $M_{\text{draft}}$ o modelo rascunho que define $Q(x)$. 
Para manter a distribuição final perfeitamente preservada (*lossless*), o critério de aceitação de um token rascunhado $x$ adota amostragem de rejeição modificada (Leviathan et al., 2022):

$$P(\text{aceitar } x) = \min\left(1, \; \frac{P(x)}{Q(x)}\right)$$

Se o token for rejeitado, ele é reamostrado a partir da distribuição residual normalizada:

$$P_{\text{residual}}(x) = \frac{\max\Big(0, \; P(x) - Q(x)\Big)}{\sum_{x'} \max\Big(0, \; P(x') - Q(x')\Big)}$$

Garantindo que a distribuição marginal final observada seja identicamente igual a $P(x)$.
A aceleração esperada $\mathbb{E}[\text{Speedup}]$ depende da taxa média de aceitação $\alpha \in [0, 1]$ e da razão de custo temporal $c$ entre o modelo rascunho e o modelo alvo:

$$\mathbb{E}[\text{Speedup}] = \frac{1 - \alpha^{K+1}}{(1 - \alpha)(\alpha K c + 1)}$$

No experimento da DeepMind (Chen et al., 2023) com o modelo Chinchilla-70B e um rascunho de 4B ($8\times$ mais rápido no decode individual), a decodificação especulativa reduziu a latência global da resposta pela metade ($2\times$ de speedup real).

## 🧱 Hipóteses e condições de validade

- O modelo rascunho e o modelo alvo devem idealmente compartilhar **o mesmo vocabulário e o mesmo tokenizador** para que a correspondência de tokens seja direta e sem erros de tradução.
- A GPU deve possuir memória física suficiente para acomodar o modelo alvo e o modelo rascunho simultaneamente, ou os dois modelos devem ser distribuídos em instâncias de hardware coordenadas.

## ✅ Quando usar

- Tarefas estruturadas com alta previsibilidade local, como geração e depuração de código-fonte, redação técnica de contratos padronizados e formulários.
- Sistemas corporativos de chat interativo onde a redução do tempo por token (*TPOT*) é a prioridade máxima de experiência do usuário.

## 🚫 Quando não usar

- Em geração literária altamente caótica e aleatória com alta temperatura ($T \ge 1{,}5$), onde a taxa de aceitação $\alpha$ despenca para quase zero, fazendo o sistema gastar tempo gerando rascunhos que serão $100\%$ descartados.

## ⚠️ Limitações e armadilhas

- **O custo de memória do modelo rascunho:** Alocar uma GPU inteira para carregar o modelo de rascunho pode ser economicamente ineficiente se o ganho de velocidade não for compensado por maior densidade de requisições.
- **Calibração do número de passos ($K$):** Escolher $K$ muito alto (ex.: $K=10$) em domínios difíceis gera desperdício de cálculo, pois a maioria dos tokens rascunhados além do segundo será rejeitada. Valores típicos de $K$ situam-se entre 3 e 5.

## 🔍 Comparações

| Técnica | Requer Modelo Extra? | Modifica a Rede Base? | Garantia Matemática | Ganho de Velocidade Típico |
|---|---|---|---|---|
| **Speculative Decoding** | **Sim (modelo draft)** | Não (zero mudanças) | **Lossless (Exato)** | $1{,}8\times$ a $2{,}5\times$ |
| **Inference with Reference** | Não (copia do prompt) | Não (zero mudanças) | **Lossless (Exato)** | $1{,}5\times$ a $2{,}0\times$ (em RAG/código) |
| **Medusa** | Não (apenas cabeças extras)| Sim (treina camadas leves) | Lossless com árvore | $1{,}5\times$ a $1{,}9\times$ |
| **Decode Padrão** | Não | Não | Linha de base | $1{,}0\times$ (lento) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um assistente de IA está gerando uma resposta em código Python. O contexto atual termina em `for i in range(`.
- O modelo rascunho leve prevê rapidamente os próximos 4 tokens: `10): \n print(i)`.
- O modelo alvo de 70B processa esses 4 tokens em paralelo em uma fração de milissegundo. Ele analisa as probabilidades:
  - `10)` $\implies$ aprovado ($100\%$ de acordo);
  - `:` $\implies$ aprovado;
  - `\n` $\implies$ aprovado;
  - `print` $\implies$ aprovado.
O modelo alvo aceitou todos os 4 tokens de rascunho de uma vez e ainda emitiu o 5º token `(`. O usuário viu 5 tokens surgirem na tela no tempo exato que levaria para gerar apenas um único token pelo método convencional.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Complementos

- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]
- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]

### Alternativas

- Modelos de tempo linear que não sofrem do mesmo gargalo de decodificação ([[redes/ai-engineering/conceitos/modelos-de-espaco-de-estados.md|Modelos de Espaço de Estados (SSMs)]]).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|Otimização do KV Cache e PagedAttention]]
- [[redes/ai-engineering/conceitos/batching-continuo-e-dinamico.md|Batching Contínuo e Dinâmico]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 428–433
- **Evidência:** Chip Huyen formaliza a decodificação especulativa a partir de Stern et al. (2018) e Leviathan et al. (2022), cita os ganhos práticos no Chinchilla-70B e T5-XXL da DeepMind, detalha o método Inference with Reference (Yang et al., 2023) para tarefas com sobreposição de contexto, e analisa abordagens de decodificação paralela como Lookahead (decodificação de Jacobi) e Medusa (Cai et al., 2024).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Decodificação Especulativa e como ela transforma parte da decodificação sequencial em processamento paralelo?
2. Por que a decodificação especulativa é classificada na literatura técnica como uma abordagem *lossless* (sem perdas)?
3. Como a amostragem de rejeição modificada opera para garantir que a distribuição do modelo alvo seja estritamente preservada?
4. O que é a técnica de Inferência com Referência (*Inference with Reference*) e em quais casos de uso práticos ela é mais vantajosa?
5. Como o framework Medusa utiliza cabeças adicionais de decodificação e árvores de atenção para acelerar a geração sem um modelo draft separado?
6. Por que domínios altamente estruturados (como código de programação) exibem taxas de aceleração muito superiores a tarefas de escrita criativa?
7. Qual é o risco de degradação de desempenho se o modelo de rascunho apresentar uma taxa de aceitação de tokens excessivamente baixa?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Batching Contínuo e Dinâmico

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 440–442

## 📝 Definição

### Definição formal

O **Batching Contínuo e Dinâmico** (*Continuous and Dynamic Batching*) compreende o conjunto de políticas e algoritmos de gerenciamento de filas e execução concorrente em servidores de inferência de [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]], projetados para agrupar requisições independentes e elevar a vazão (*throughput*) da GPU sem penalizar desproporcionalmente a latência individual:
1. **Batching Estático (*Static Batching*):** Agrupa um número fixo de entradas e retém o processamento até que todo o lote seja preenchido e todas as respostas concluídas;
2. **Batching Dinâmico (*Dynamic Batching*):** Fecha o lote com base em uma janela temporal limite ou capacidade máxima, despachando o processamento do grupo de requisições de uma só vez;
3. **Batching Contínuo (*Continuous Batching* / *In-Flight Batching*, Yu et al., Orca, 2022):** Mecanismo de agendamento iterativo em nível de token individual que remove requisições finalizadas do lote imediatamente no momento em que emitem o token de parada ($\text{<EOS>}$) e insere novas requisições recém-chegadas em seus lugares a cada ciclo de decodificação.

### Em linguagem simples

É a diferença entre um ônibus tradicional e um elevador inteligente. O batching tradicional funciona como um ônibus de excursão que só dá a partida quando todos os 50 assentos estiverem cheios e não deixa ninguém descer até a viagem inteira terminar para todos. O **Batching Contínuo** funciona como um elevador de fluxo contínuo: ele abre a porta a cada andar; se alguém chegou ao seu destino, essa pessoa sai imediatamente (a resposta é entregue ao usuário), e se tem alguém esperando no corredor, essa nova pessoa entra na vaga que acabou de abrir, aproveitando a capacidade máxima do elevador a cada segundo.

### Escopo e distinções

Em tarefas tradicionais de ML (como classificação tabular), todas as predições de um lote demoram exatamente o mesmo tempo. Em modelos de linguagem generativos, uma pergunta pode exigir uma resposta de 10 tokens enquanto outra exige 1.000 tokens. O batching contínuo resolve a disparidade heterogênea do comprimento das saídas.

## 🧩 Problema que resolve

Resolve o desperdício massivo de computação e o atraso artificial de requisições curtas causados pelo loteamento rígido. No batching ingênuo, um usuário que pediu uma resposta de uma única palavra fica preso esperando a GPU processar por 30 segundos porque outro usuário no mesmo lote pediu uma dissertação acadêmica de 1.000 palavras.

## 💡 Intuição

Pense em uma fila de caixas de atendimento bancário:
- No **Batching Estático**, o banco atende 4 clientes ao mesmo tempo, mas os caixas são proibidos de atender qualquer nova pessoa até que o cliente mais enrolado e lento termine de contar suas moedas.
- No **Batching Contínuo**, assim que o primeiro cliente finaliza um pagamento rápido de 30 segundos, ele é liberado imediatamente (**resposta entregue**) e o próximo cliente da fila ocupa aquela posição de atendimento sem esperar os outros três caixas terminarem.

## ⚙️ Como funciona

O agendador do servidor de inferência atua a cada ciclo do loop de decode:

### Etapas

1. **Recepção de Requisições:** Consultas com prompts de comprimentos heterogêneos entram na fila do servidor.
2. **Ciclo de Decodificação Iterativa:** A GPU processa um passo de decode para todas as requisições ativas atualmente no lote.
3. **Detecção de Conclusão no Nível do Token:** O agendador inspeciona a saída emitida por cada slot de atendimento:
   - Se uma requisição gerou o token especial de término $\text{<EOS>}$ ou estourou seu limite máximo, seu resultado é empacotado e enviado de volta ao cliente;
   - Seu slot de processamento na GPU e seus blocos de memória no [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|KV Cache]] são imediatamente liberados.
4. **Inserção In-Flight:** Uma nova requisição em espera na fila passa por sua fase inicial de prefill e seus tensores são alocados no slot recém-desocupado.
5. **Continuidade Operacional:** O próximo ciclo de decodificação executa simultaneamente passos de decode para requisições antigas e o início de geração da requisição recém-inserida.

### Entradas e saídas

- **Entradas:** Fila contínua e assíncrona de solicitações com comprimentos variáveis.
- **Saídas:** Respostas retornadas no menor tempo individual possível com vazão máxima de tokens por segundo na GPU.

## 📐 Formulação matemática

Seja um lote estático $\mathcal{B}$ de tamanho $B$ com comprimentos de saída $L = \{l_1, l_2, \dots, l_B\}$. 
No **Batching Estático**, o tempo total de ocupação dos recursos do lote é governado pelo elemento de cauda máxima:

$$T_{\text{estático}} \propto \max(l_1, l_2, \dots, l_B)$$

O desperdício de computação (número de slots ociosos multiplicados por passos ociosos) é:

$$\text{Desperdício} = \sum_{i=1}^B \Big(\max(L) - l_i\Big)$$

No **Batching Contínuo (Orca)**, o desperdício computacional por preenchimento de lacunas converge para zero:

$$\text{Desperdício}_{\text{contínuo}} \approx 0 \implies \text{Throughput} \propto \frac{\sum_{i=1}^N l_i}{\text{Tempo Total}}$$

A taxa de ocupação dos núcleos da GPU atinge patamares contínuos de saturação ótima, dobrando ou triplicando a vazão de tokens por segundo em comparação ao loteamento estático.

## 🧱 Hipóteses e condições de validade

- Exige que o motor de inferência gerencie o KV Cache através de alocadores dinâmicos de memória (como o [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|PagedAttention]]) para evitar que a inserção de novos usuários exija realocações físicas contíguas na VRAM.

## ✅ Quando usar

- Padrão arquitetural mandatório para qualquer servidor de inferência corporativo em produção (implementado nativamente em vLLM, TensorRT-LLM e TGI).
- APIs públicas ou privadas com centenas de usuários concorrentes enviando prompts com comprimentos de resposta imprevisíveis.

## 🚫 Quando não usar

- Em sistemas de usuário único isolado rodando em computadores pessoais desconectados da rede, onde o lote físico é estritamente $B = 1$.

## ⚠️ Limitações e armadilhas

- **Degradação sutil de latência individual:** Embora a vazão global do servidor aumente drasticamente, o tempo por token (*TPOT*) de cada usuário individual pode sofrer pequenos aumentos em comparação à execução isolada sem loteamento, exigindo calibração contra o SLO da aplicação.

## 🔍 Comparações

| Modalidade de Batching | Quando o Lote Parte? | Quando a Resposta Sai? | Desperdício de GPU |
|---|---|---|---|
| **Estático** | Quando atinge $N$ requisições | Quando **todos** terminam | **Altíssimo (espera o mais longo)** |
| **Dinâmico** | Atinge $N$ requisições ou timeout | Quando **todos** terminam | Alto (espera o mais longo do grupo) |
| **Contínuo (*In-Flight*)**| Imediatamente para slots livres | **Assim que o token $\text{<EOS>}$ surge** | **Mínimo (slots sempre cheios)** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Dois usuários mandam perguntas no mesmo segundo para um servidor:
- O Usuário A pergunta: `"Qual é a capital da França?"` (exige 2 tokens de resposta: `"É Paris"`).
- O Usuário B pede: `"Escreva uma redação de 800 palavras sobre a Revolução Francesa"`.
- *Com Batching Estático:* O Usuário A espera 25 segundos na frente da tela olhando para um ícone de carregamento girando porque o sistema não pode entregar seus 2 tokens até que a redação do Usuário B seja totalmente digitada.
- *Com Batching Contínuo:* Em 50 milissegundos, o Usuário A recebe `"É Paris"`, sua vaga é liberada na placa de vídeo e uma nova pergunta de outro cliente entra no lugar, enquanto o Usuário B continua recebendo sua redação longa sem nenhuma interrupção.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]
- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]

### Complementos

- [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|Otimização do KV Cache e PagedAttention]]
- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]

### Alternativas

- Atendimento puramente sequencial de requisições isoladas sem loteamento (*single-stream processing*).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/desacoplamento-de-prefill-e-decode.md|Desacoplamento de Prefill e Decode]]
- [[redes/ai-engineering/conceitos/estrategias-de-paralelismo-em-inferencia.md|Estratégias de Paralelismo em Inferência]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 440–442
- **Evidência:** Chip Huyen compara batching estático e dinâmico com a metáfora do ônibus (Figura 9-15) e detalha a inovação do continuous batching originada no paper Orca (Yu et al., 2022), demonstrando a eliminação de ociosidade por diferenças no comprimento das respostas.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a deficiência estrutural do batching estático tradicional quando aplicado a modelos de linguagem autorregressivos?
2. Como o batching contínuo (*in-flight batching*) opera no nível de iteração de tokens individuais?
3. O que é o framework Orca e qual foi sua contribuição para os motores de inferência modernos?
4. Como a sobreposição de requisições com comprimentos heterogêneos de saída afeta a taxa de ocupação dos núcleos da GPU?
5. Qual é o compromisso (*trade-off*) clássico entre latência individual (TPOT) e vazão agregada (*throughput*) ao aumentar o tamanho do lote?
6. Por que o batching contínuo depende intrinsecamente de alocadores dinâmicos de memória como o PagedAttention?
7. De que maneira o tempo limite (*timeout*) do batching dinâmico tenta mitigar a latência na ausência de fluxo contínuo de usuários?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Prompt Caching e Reutilização de Contexto

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 443–444

## 📝 Definição

### Definição formal

O **Prompt Caching** (*Prefix Caching* ou *Context Caching*, Gim et al., 2023) é a técnica de otimização no nível de serviço de inferência na qual os estados intermediários computados durante a fase de prefill (especificamente as representações em tensores do [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|KV Cache]]) correspondentes a prefixos ou segmentos textuais estáticos e idênticos compartilhados por múltiplas requisições (como instruções de sistema longas, poucos exemplos demonstrativos ou documentos de referência em RAG) são persistidos na memória da GPU ou em armazenamento rápido, permitindo que requisições subsequentes reutilizem diretamente esses tensores pré-calculados, eliminando a computação redundante de atenção e barateando custos operacionais.

### Em linguagem simples

É salvar a "leitura prévia" de textos que nunca mudam. Se a sua empresa coloca um manual de 50 páginas ou uma instrução de sistema gigantesca em todas as perguntas que os clientes fazem, a IA tradicionalmente gastava tempo e cobrava dinheiro para reler essas mesmas 50 páginas a cada clique. O Prompt Caching faz a IA ler o manual uma única vez e guardar a memória dessa leitura pronta; nas perguntas seguintes, ela pula a leitura e vai direto para a resposta, reduzindo o tempo de espera e dando descontos de até 90% na fatura de tokens.

### Escopo e distinções

Diferencia-se do cache semântico tradicional. O cache semântico devolve uma resposta inteira pronta para perguntas similares. O Prompt Caching atua **dentro do fluxo de inferência da rede neural**: ele não devolve a resposta final pronta; ele acelera o processamento do **começo do texto**, permitindo que o modelo gere respostas completamente inéditas para perguntas novas.

## 🧩 Problema que resolve

Resolve a penalidade financeira e de latência imposta por prompts com contextos estáticos volumosos. Em fluxos de trabalho corporativos com copilotos de código que anexam repositórios inteiros ou assistentes jurídicos que operam sobre contratos extensos, pagar repetidamente para a GPU processar os mesmos 50.000 tokens de entrada a cada mensagem de diálogo tornava as aplicações financeiramente insustentáveis.

## 💡 Intuição

Pense em um consultor de investimentos que atende clientes durante o dia:
- **Sem Prompt Caching:** Antes de cada cliente novo sentar na cadeira, o consultor é obrigado a ler novamente do zero o relatório econômico de 200 páginas do Banco Central. Ele passa 40 minutos lendo o relatório antes de dar o primeiro "bom dia" ao cliente (**latência TTFT gigante**).
- **Com Prompt Caching:** O consultor lê o relatório uma única vez no início da manhã e coloca post-its coloridos nas páginas principais (**o cache na memória**). Quando os clientes chegam ao longo do dia, ele atende instantaneamente porque o relatório já está fresco e assimilado em sua mente.

## ⚙️ Como funciona

O mecanismo baseia-se na detecção de casamento de prefixos (*prefix matching*):

### Etapas

1. **Recepção da Requisição:** A aplicação envia o prompt contendo um segmento de cabeçalho compartilhado (ex.: System Prompt de 2.000 tokens) seguido pela pergunta dinâmica do usuário.
2. **Identificação do Prefixo em Cache:** O motor de inferência verifica se o hash ou a sequência inicial de tokens coincide com blocos de KV Cache já armazenados na memória rápida.
3. **Pulo do Prefill Redundante (*Cache Hit*):**
   - O modelo não executa cálculos matriciais para os primeiros 2.000 tokens;
   - Os tensores de $K$ e $V$ correspondentes são carregados instantaneamente da tabela de cache.
4. **Execução Restrita:** A GPU processa em modo prefill apenas os tokens novos e dinâmicos específicos daquela pergunta (ex.: 20 tokens).
5. **Decodificação Imediata:** O modelo emite o primeiro token da resposta com latência mínima (**redução dramática do TTFT**).

### Entradas e saídas

- **Entradas:** Prompts com sobreposições estruturais de texto em suas posições iniciais.
- **Saídas:** Resposta gerada de forma autônoma com redução de até 90% no custo faturado de tokens de entrada e queda drástica no tempo de resposta.

## 📐 Formulação matemática

A latência da fase de prefill para uma sequência de entrada dividida entre um prefixo estático de comprimento $P_{\text{cache}}$ e uma consulta dinâmica $P_{\text{novo}}$ transforma-se de:

$$T_{\text{prefill\_sem\_cache}} \propto (P_{\text{cache}} + P_{\text{novo}})^2$$

Para:

$$T_{\text{prefill\_com\_cache}} \propto P_{\text{novo}}^2 + \text{Overhead}_{\text{leitura\_cache}}$$

Como tipicamente $P_{\text{cache}} \gg P_{\text{novo}}$ (ex.: $100.000$ tokens de cache contra $50$ tokens de pergunta nova), a economia temporal atinge ordens de grandeza.
A tabela empírica documentada no capítulo com base nos dados da Anthropic (2024) formaliza os ganhos práticos:

| Cenário de Uso | Tamanho do Cache | Latência TTFT sem Cache | Latência TTFT com Cache | Redução de Custo |
|---|---|---|---|---|
| **Chat com Livro Completo** | 100.000 tokens | $11{,}5 \text{ s}$ | **$2{,}4 \text{ s}$ (queda de $79\%$)** | **$-90\%$** |
| **Many-Shot Prompting** | 10.000 tokens | $1{,}6 \text{ s}$ | **$1{,}1 \text{ s}$ (queda de $31\%$)** | **$-86\%$** |
| **Diálogo Multi-Turno** | Contexto longo | $\approx 10{,}0 \text{ s}$ | **$\approx 2{,}5 \text{ s}$ (queda de $75\%$)** | **$-53\%$** |

## 🧱 Hipóteses e condições de validade

- A sobreposição de texto deve ocorrer **obrigatoriamente a partir do primeiro token da sequência (o prefixo)**; se o texto dinâmico for inserido no início e o texto estático no final, o mecanismo de atenção causal quebra a compatibilidade do cache e invalida o reaproveitamento.
- A aplicação deve manter um volume de consultas com intervalo temporal menor que a política de expiração (*TTL*) do cache do provedor para evitar que o cache seja ejetado por inatividade.

## ✅ Quando usar

- Sistemas de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]] que utilizam documentos de base compartilhados por centenas de consultas consecutivas.
- Assistentes corporativos que utilizam prompts de sistema densos com dezenas de exemplos demonstrativos (*many-shot prompting*).
- Interfaces de conversação de múltiplos turnos longos, reaproveitando as mensagens anteriores a cada nova resposta.

## 🚫 Quando não usar

- Em requisições avulsas e esparsas onde cada entrada é completamente aleatória, sem nenhum texto de cabeçalho ou documento comum compartilhado.

## ⚠️ Limitações e armadilhas

- **Custo de Armazenamento do Cache:** Provedores de nuvem (como o Google Gemini) concedem descontos pesados no custo de processamento do token em cache, mas cobram uma taxa de manutenção horária pelo espaço de memória alocado para reter o cache; se a taxa de consultas for baixa, o custo de armazenamento pode superar a economia de inferência.
- **Quebras Inadvertidas de Hash de Prefixo:** Inserir timestamps dinâmicos (como a data de hoje ou a hora atual) no topo do System Prompt invalida o cache para todas as requisições subsequentes. Variáveis dinâmicas devem ser sempre posicionadas após o bloco estático em cache.

## 🔍 Comparações

| Dimensão | Cache Semântico Tradicional | Prompt Caching (Prefix Caching) |
|---|---|---|
| **O que é salvo?** | A resposta final inteira em texto | Os tensores de atenção ($K, V$) do início do prompt |
| **Flexibilidade da pergunta**| Nula (só funciona se a pergunta for similar) | **Total (a pergunta do usuário pode ser inédita)** |
| **Nível de Atuação** | No software externo antes da IA | **Dentro do motor de inferência da GPU** |
| **Capacidade Gerativa** | Não gera nada novo (devolve texto estático) | **Gera raciocínios e respostas 100% inéditas** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma plataforma de análise de contratos carrega a convenção coletiva de trabalho de um sindicato (um documento longo de 80 páginas e 30.000 tokens).
- Cem advogados diferentes acessam a plataforma para fazer perguntas distintas sobre o mesmo documento: *"Qual é o adicional de periculosidade?"*, *"Qual é o prazo de licença-maternidade?"*, etc.
- **Sem Prompt Caching:** O provedor processa os 30.000 tokens cem vezes ($3.000.000$ de tokens de entrada faturados) e cada advogado espera 5 segundos para a resposta começar a ser digitada.
- **Com Prompt Caching:** O documento é processado uma única vez na primeira chamada. Para as 99 perguntas seguintes, os 30.000 tokens são lidos do cache instantaneamente: o TTFT despenca para 0,3 segundo e a fatura do dia cai em quase 90%.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]
- [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|Otimização do KV Cache e PagedAttention]]

### Complementos

- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]
- [[redes/ai-engineering/conceitos/templates-de-chat-e-prompts-de-sistema.md|Templates de Chat e Prompts de Sistema]]

### Alternativas

- Cache de respostas semântico tradicional via similaridade vetorial.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 443–444
- **Evidência:** Chip Huyen conceitua o prompt caching a partir de Gim et al. (2023), ilustra o mecanismo de prefixo reutilizado (Figura 9-17) e analisa a Tabela 9-3 detalhando os ganhos empíricos oficiais divulgados pela Anthropic e Google Gemini com reduções de até 90% em custos e 79% em tempo de primeiro token.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Prompt Caching (*Prefix Caching*) e qual componente da inferência de LLMs ele reutiliza?
2. Em que o Prompt Caching difere estruturalmente de um cache semântico tradicional de respostas?
3. Por que a inserção de variáveis dinâmicas (como horários ou dados do usuário) no início do prompt pode anular o benefício do Prompt Caching?
4. Quais foram os ganhos percentuais de latência (TTFT) e custo financeiro documentados pela Anthropic no processamento de livros com 100.000 tokens?
5. Qual é o trade-off econômico introduzido pela cobrança horária de retenção de cache em provedores como o Google Gemini?
6. Como o Prompt Caching atua para acelerar conversas interativas de múltiplos turnos ao longo de um diálogo extenso?
7. Por que a técnica é considerada especialmente revolucionária para sistemas corporativos baseados em RAG?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Desacoplamento de Prefill e Decode

**Rede:** `ai-engineering`  
**Área:** `infraestrutura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 442–443

## 📝 Definição

### Definição formal

O **Desacoplamento de Prefill e Decode** (*Disaggregated Prefill and Decode Serving*, formalizado em sistemas como *DistServe* de Zhong et al., 2024 e *Inference Without Interference* / Splitwise de Hu et al., 2024) é um padrão arquitetural de infraestrutura distribuída para atendimento de [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]] no qual a fase de processamento do prompt de entrada (**Prefill**) e a fase de geração sequencial de tokens de saída (**Decode**) são executadas em conjuntos separados e dedicados de instâncias físicas de aceleradores (GPUs/TPUs), transferindo o estado intermediário do [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|KV Cache]] entre os nós através de interconexões de alta largura de banda (como NVLink ou InfiniBand).

### Em linguagem simples

É a estratégia de separar quem lê de quem escreve na infraestrutura da empresa. Como a tarefa de ler a pergunta do usuário exige força bruta de cálculo matemático e a tarefa de escrever a resposta exige velocidade de memória, colocar as duas para rodar na mesma placa de vídeo faz uma atrapalhar a outra. Separando o trabalho em duas equipes de computadores — uma sala de máquinas só para ler as perguntas e outra sala só para digitar as respostas —, o sistema elimina travamentos e responde muito mais rápido.

### Escopo e distinções

Diferencia-se da arquitetura tradicional colocalizada (*colocated serving*), onde a mesma GPU executa alternadamente o prefill e o decode para todas as requisições que chegam ao servidor, gerando interferência temporal.

## 🧩 Problema que resolve

Resolve o fenômeno da **interferência mútua de recursos (*Inter-phase Interference*)**. Quando uma GPU está no meio da decodificação contínua de respostas para dez usuários (onde a fluidez do texto exige que cada palavra saia em menos de 50 milissegundos) e chega uma nova requisição com um documento longo de 8.000 tokens, a GPU precisa pausar a digitação para calcular o prefill pesado do novo usuário. Isso causa soluços e congelamentos súbitos na tela dos outros dez usuários (*spikes* no p99 de TPOT/ITL).

## 💡 Intuição

Pense em um consultório médico de triagem e consulta:
- No **modelo misturado comum**, o mesmo médico faz a triagem pesada (medição de pressão, histórico de saúde, exame físico longo) e atende o retorno rápido de quem só veio pegar uma receita carimbada. Se entrar um paciente em estado grave na triagem, o paciente que só queria a receita carimbada fica preso na sala de espera por duas horas.
- No **desacoplamento**, o consultório coloca enfermeiros dedicados exclusivamente na sala de triagem (**nós de prefill**). Assim que o paciente é examinado e tem sua ficha preenchida, ele é encaminhado para os médicos que ficam em outra sala apenas prescrevendo tratamentos e tirando dúvidas de forma contínua (**nós de decode**). Ninguém fica preso esperando.

## ⚙️ Como funciona

O tráfego de inferência é roteado por etapas especializadas:

### Etapas

1. **Recepção e Roteamento para Nó de Prefill:** A consulta do usuário chega ao balanceador e é despachada para uma GPU configurada com paralelismo otimizado para computação bruta (alto número de TFLOPs).
2. **Execução do Prefill:** A GPU processa todos os tokens de entrada em paralelo e calcula o estado inicial do KV Cache e o primeiro token da resposta.
3. **Transferência do KV Cache via Rede de Alta Velocidade:** O buffer contendo as matrizes de chaves e valores calculadas é transferido do nó de prefill para o nó de decode através de barramentos ultrarrápidos (como NVLink entre nós ou RDMA sobre InfiniBand), minimizando a sobrecarga de comunicação.
4. **Alocação no Nó de Decode:** Uma GPU configurada com alta largura de banda de memória (HBM) e otimizada para batching contínuo recebe o KV Cache e assume a geração sequencial.
5. **Decodificação Contínua Desimpedida:** O nó de decode emite os tokens restantes da resposta em fluxo ininterrupto, imune a interferências de novas perguntas que estejam chegando à plataforma.

### Entradas e saídas

- **Entradas:** Carga de trabalho de inferência mista com prompts longos e respostas variáveis.
- **Saídas:** Estabilidade estrita de SLOs com isolamento de TTFT e TPOT.

## 📐 Formulação matemática

O dimensionamento de capacidade em sistemas desacoplados é determinado pela razão ótima de instâncias entre nós de prefill ($N_{\text{prefill}}$) e nós de decode ($N_{\text{decode}}$), modelada com base no perfil de tráfego:

$$R_{\text{instâncias}} = \frac{N_{\text{prefill}}}{N_{\text{decode}}} \approx \frac{\bar{P}_{\text{entrada}} \times \text{Throughput}_{\text{req}}}{\bar{P}_{\text{saída}} \times \text{Throughput}_{\text{req}}} \times \frac{AI_{\text{decode}}}{AI_{\text{prefill}}}$$

Onde $\bar{P}_{\text{entrada}}$ e $\bar{P}_{\text{saída}}$ representam as médias de tokens de prompt e de geração.
Conforme as diretrizes do capítulo:
- Em cargas dominadas por documentos longos com foco em minimizar o TTFT (ex.: RAG e sumarização): a proporção típica é de **$2:1$ a $4:1$** (mais máquinas alocadas para prefill);
- Em cargas dominadas por consultas curtas com respostas extensas (ex.: redação de código ou histórias): a proporção inverte-se para **$1:2$ a $1:1$** (mais máquinas dedicadas a decode).

## 🧱 Hipóteses e condições de validade

- A infraestrutura de cluster deve dispor de conexões de interconexão entre GPUs de altíssima velocidade (como redes de barramento com largura de banda $\ge 100 \text{ GB/s}$); se a transferência do KV Cache entre máquinas ocorrer sobre redes Ethernet convencionais lentas, a sobrecarga de rede anula os ganhos do desacoplamento.

## ✅ Quando usar

- Plataformas de inferência corporativas de alta densidade de tráfego que operam sob contratos rígidos de nível de serviço (SLAs).
- Sistemas com alta variância no comprimento dos prompts (onde algumas requisições têm 100 tokens e outras têm 32.000 tokens).

## 🚫 Quando não usar

- Em implantações pequenas operando com apenas 1 ou 2 GPUs no total, onde a sobrecarga de particionar as placas não compensa a flexibilidade de um pool único.

## ⚠️ Limitações e armadilhas

- **Sobrecarga de Tráfego de Rede (*Communication Overhead*):** Em sequências com contexto muito extenso, o tamanho do KV Cache atinge gigabytes de dados; transferir esse buffer entre servidores consome capacidade das placas de rede.
- **Complexidade de Orquestração:** Exige agendadores distribuídos inteligentes capazes de lidar com falhas de nós em ambas as pontas do pipeline de atendimento.

## 🔍 Comparações

| Característica | Servidor Tradicional Colocalizado | Servidor Desacoplado (DistServe / Splitwise) |
|---|---|---|
| **Alocação de GPU** | Mesma GPU faz prefill e decode | **GPUs distintas especializadas por fase** |
| **Interferência mútua** | Alta (prefills longos travam decodes ativos) | **Zero (isolamento físico de fases)** |
| **Estabilidade de TPOT (p99)**| Instável (com picos frequentes de atraso) | **Altamente estável e previsível** |
| **Requisito de Rede** | Padrão interno de máquina | **Exige NVLink ou redes RDMA/InfiniBand** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um data center da Meta atende milhões de requisições do assistente do WhatsApp:
- Um usuário envia um documento PDF de 10 páginas para análise.
- A requisição é direcionada a um **nó de prefill**, equipado com placas calibradas para processamento massivo. O texto de 10 páginas é mastigado em paralelo em 200 milissegundos e o KV Cache é gerado.
- Esse buffer de dados é despachado em alta velocidade via NVLink para um **nó de decode**, onde outras GPUs estão gerando respostas para milhares de usuários em lote contínuo.
- O nó de prefill fica imediatamente liberado para ler o próximo PDF, e os usuários que estavam recebendo respostas no nó de decode não sentiram nenhuma queda de velocidade na digitação de suas mensagens.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]
- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]

### Complementos

- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]
- [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|Otimização do KV Cache e PagedAttention]]

### Alternativas

- Atendimento colocalizado padrão com batching contínuo em pool compartilhado de GPUs.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/batching-continuo-e-dinamico.md|Batching Contínuo e Dinâmico]]
- [[redes/ai-engineering/conceitos/estrategias-de-paralelismo-em-inferencia.md|Estratégias de Paralelismo em Inferência]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 442–443
- **Evidência:** Chip Huyen formaliza a dissociação física entre prefill e decode baseando-se nos estudos seminais do DistServe (Zhong et al., 2024) e Splitwise (Hu et al., 2024), detalhando as razões ótimas de alocação de instâncias (de 2:1 a 4:1 para prefill dominante e 1:2 para decode dominante) documentadas também pela engenharia da Meta no Llama.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é o problema operacional de "interferência de recursos" que motivou a criação do desacoplamento de prefill e decode?
2. Por que a fase de prefill e a fase de decode exigem perfis de otimização de silício fundamentalmente distintos?
3. Quais são os sistemas acadêmicos e industriais pioneiros citados no texto que implementaram essa arquitetura desagregada?
4. Como a relação média entre tokens de entrada e tokens de saída determina a proporção ótima de instâncias de prefill versus decode?
5. Qual infraestrutura física de rede é necessária para que a transferência do KV Cache entre máquinas não gere um gargalo de latência?
6. Como o desacoplamento de fases atua na redução do percentil p99 da métrica de tempo por token de saída (TPOT)?
7. Em quais cenários de pequeno porte essa arquitetura desagregada torna-se desaconselhada devido à sobrecarga de complexidade?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Estratégias de Paralelismo em Inferência

**Rede:** `ai-engineering`  
**Área:** `infraestrutura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 444–447

## 📝 Definição

### Definição formal

As **Estratégias de Paralelismo em Inferência** (*Parallelism Strategies for Inference*) representam o conjunto de métodos de computação distribuída e particionamento matricial utilizados para hospedar e executar [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]] cuja escala de parâmetros ou volume de requisições excede a capacidade de memória VRAM ou os requisitos de latência de um único acelerador de hardware, estruturando-se em quatro modalidades primárias:
1. **Paralelismo de Réplicas (*Replica Parallelism*):** Instanciação de múltiplas cópias completas do modelo idêntico em dispositivos separados, particionando o tráfego de usuários através de balanceadores de carga;
2. **Paralelismo de Tensores (*Tensor Parallelism* / Intra-operador):** Fracionamento das matrizes de peso de cada camada individual (atenção e feedforward) ao longo de linhas ou colunas através de múltiplos aceleradores interconectados, computando partes da mesma multiplicação matricial em paralelo;
3. **Paralelismo de Pipeline (*Pipeline Parallelism* / Inter-estágios):** Particionamento sequencial do modelo ao longo de suas camadas (ex.: camadas 1 a 20 na GPU 1, camadas 21 a 40 na GPU 2), processando lotes divididos em micro-lotes que fluem através das máquinas em linha de montagem;
4. **Paralelismo de Contexto e Sequência (*Context / Sequence Parallelism*):** Divisão de sequências ultra-longas de tokens de entrada através de múltiplos dispositivos para viabilizar o cálculo da atenção em contextos de milhões de tokens.

### Em linguagem simples

É como dividir o trabalho pesado entre vários computadores quando a IA é grande demais para caber em uma única placa de vídeo. Se você tem muitos clientes, a forma mais fácil é colocar várias cópias da mesma IA em computadores separados (**Paralelismo de Réplicas**). Se a IA for um monstro de 70 bilhões de parâmetros que não cabe em uma placa só, você fatia as equações matemáticas ao meio para duas placas resolverem juntas (**Paralelismo de Tensores**) ou coloca as primeiras camadas em uma placa e as camadas finais em outra (**Paralelismo de Pipeline**).

### Escopo e distinções

Diferencia-se do paralelismo de treinamento. No treinamento, o paralelismo de pipeline é amplamente utilizado para aumentar a vazão de dados; na inferência com restrições rígidas de latência, o paralelismo de pipeline é evitado porque adiciona atrasos de comunicação sequencial (*bubbles*), sendo preterido em favor do paralelismo de tensores e réplicas.

## 🧩 Problema que resolve

Resolve a impossibilidade física de carregar modelos de dezenas ou centenas de bilhões de parâmetros em uma única GPU. Permite que modelos como o Llama 3-70B (que ocupa 140 GB em FP16) rodem com latência ultra-baixa distribuídos em nós de 4 ou 8 GPUs de 24 GB ou 80 GB interconectadas.

## 💡 Intuição

Pense em carregar um piano de cauda escada acima:
- **Paralelismo de Réplicas:** Você tem 50 pessoas querendo subir de elevador com mochilas leves. Você constrói 4 elevadores idênticos e divide as pessoas entre eles.
- **Paralelismo de Tensores:** O piano de cauda pesa 500 kg e nenhum homem consegue levantá-lo sozinho. Quatro carregadores fortes seguram o mesmo piano ao mesmo tempo, cada um levantando um pé do instrumento e subindo os degraus em perfeita sincronia milimétrica.
- **Paralelismo de Pipeline:** Uma linha de montagem de baldes de água: a pessoa na base do poço enche o balde e passa para quem está no meio da escada, que por sua vez passa para quem está no topo.

## ⚙️ Como funciona

Cada estratégia de particionamento intervém em um nível diferente da pilha de software:

### Etapas

1. **Paralelismo de Tensores (Matmul Paralelo):**
   - Na camada de atenção, as matrizes de projeção de Query, Key e Value ($W_q, W_k, W_v$) são fatiadas verticalmente (por colunas) entre $N$ GPUs.
   - Cada GPU multiplica o tensor de entrada por sua respectiva fatia sem precisar conversar com as outras placas.
   - Na camada de projeção de saída ($W_o$), a matriz é fatiada horizontalmente (por linhas).
   - Ao final da operação, uma primitiva de comunicação coletiva **All-Reduce** sincroniza e soma os resultados parciais de todas as placas via barramento NVLink de altíssima velocidade.
2. **Paralelismo de Pipeline:**
   - O lote de entrada é fragmentado em micro-lotes.
   - Enquanto a GPU 2 processa o micro-lote 1 na camada 21, a GPU 1 já está processando o micro-lote 2 na camada 1, criando sobreposição temporal de execução.
3. **Paralelismo de Réplicas (Bin-Packing):**
   - Um algoritmo de empacotamento distribui modelos de diferentes tamanhos (8B, 70B) na quantidade exata de placas para maximizar a densidade de atendimento por Watt consumido.

### Entradas e saídas

- **Entradas:** Modelo de fundação particionado e fluxo distribuído de requisições de inferência.
- **Saídas:** Inferência executada com menor tempo por token e capacidade de atendimento massiva.

## 📐 Formulação matemática

No **Paralelismo de Tensores Colunar** (Shoeybi et al., Megatron-LM), a matriz de pesos $W \in \mathbb{R}^{d \times k}$ é particionada em $N$ fatias verticais $W = [W_1 \mid W_2 \mid \dots \mid W_N]$, onde cada fatia $W_i \in \mathbb{R}^{d \times (k/N)}$ reside na GPU $i$:

$$Y_i = X \cdot W_i, \quad \text{onde } Y = [Y_1 \mid Y_2 \mid \dots \mid Y_N]$$

No **Paralelismo de Tensores Linear**, a matriz subsequente $V \in \mathbb{R}^{k \times m}$ é particionada horizontalmente:

$$V = \begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_N \end{bmatrix} \implies Z = Y \cdot V = \sum_{i=1}^N Y_i \cdot V_i = \text{All-Reduce}\Big(Y_i \cdot V_i\Big)$$

A operação exige exatamente duas comunicações coletivas All-Reduce por bloco Transformer, tornando a latência diretamente dependente da largura de banda da interconexão entre as placas físicas.

## 🧱 Hipóteses e condições de validade

- O Paralelismo de Tensores exige que as GPUs estejam no **mesmo nó físico** conectadas por barramentos de altíssima velocidade (como NVLink com taxas de centenas de GB/s); tentar rodar paralelismo de tensores entre servidores distantes conectados por cabos de rede comuns destrói a performance devido à latência do All-Reduce.

## ✅ Quando usar

- **Paralelismo de Tensores:** Modelos que excedem a memória de uma única GPU ou aplicações que exigem reduzir a latência de TPOT dividindo o esforço da camada entre múltiplos núcleos simultâneos.
- **Paralelismo de Réplicas:** Aplicações com alto volume de usuários concorrentes onde o modelo cabe com folga dentro de um único chip (ou dentro de um único par).

## 🚫 Quando não usar

- Evite Paralelismo de Pipeline para sistemas interativos de suporte ao cliente com exigência de baixa latência individual de resposta.

## ⚠️ Limitações e armadilhas

- **Sobrecarga de Comunicação (*Communication Overhead*):** Conforme o grau de paralelismo de tensores se expande além de 8 GPUs, o tempo gasto somando gradientes e ativações no All-Reduce começa a superar o tempo ganho na matemática paralela.
- **Bolhas de Pipeline (*Pipeline Bubbles*):** No paralelismo de pipeline, instâncias a jusante passam tempo ociosas esperando as primeiras camadas processarem os dados iniciais.

## 🔍 Comparações

| Estratégia de Paralelismo | Onde particiona? | Impacto na Latência (TPOT) | Requisito de Hardware |
|---|---|---|---|
| **Réplicas (*Data*)** | Não particiona (duplica tudo) | Não altera (mesma da placa única) | GPUs isoladas sem interconexão rápida |
| **Tensores (*Tensor*)** | **Dentro de cada camada (matrizes)** | **Reduz a latência (acelera a matemática)**| **Mandatório NVLink local no mesmo nó** |
| **Pipeline (*Pipeline*)** | Entre camadas sequenciais | **Aumenta a latência individual** | Conexões padrão de rede entre nós |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma empresa precisa servir o modelo Llama 3-70B em precisão FP16:
- O modelo exige 140 GB de VRAM. A empresa tem servidores com 4 placas de 48 GB cada (total de 192 GB por servidor).
- A equipe configura **Paralelismo de Tensores com grau 4 ($TP=4$)**:
  - Cada uma das 4 GPUs carrega exatamente 35 GB de pesos na memória HBM.
  - Quando um token chega, todas as 4 GPUs multiplicam suas fatias da matriz de atenção ao mesmo tempo.
  - O barramento NVLink soma as 4 fatias em milissegundos.
O modelo funciona perfeitamente, cabe com folga na memória e gera tokens quase quatro vezes mais rápido do que geraria se tentasse rodar em uma única máquina sobrecarregada.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/aceleradores-de-ia-e-hierarquia-de-memoria.md|Aceleradores de IA e Hierarquia de Memória]]

### Complementos

- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]
- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]

### Alternativas

- Hospedagem monolítica em GPU única com modelos comprimidos via [[redes/ai-engineering/conceitos/quantizacao.md|quantização]].

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/desacoplamento-de-prefill-e-decode.md|Desacoplamento de Prefill e Decode]]
- [[redes/ai-engineering/conceitos/batching-continuo-e-dinamico.md|Batching Contínuo e Dinâmico]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 444–447
- **Evidência:** Chip Huyen formaliza o problema de bin-packing no paralelismo de réplicas, destrincha o funcionamento do paralelismo de tensores ilustrado com diagrama matricial (Figura 9-18) e o paralelismo de pipeline com micro-lotes (Figura 9-19), analisando também extensões de paralelismo de contexto e sequência para sequências ultra-longas.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as quatro modalidades primárias de paralelismo aplicáveis à inferência de modelos de fundação?
2. Como funciona a partição de matrizes de atenção e feedforward no Paralelismo de Tensores (Megatron-LM)?
3. Por que o Paralelismo de Tensores exige que os aceleradores estejam no mesmo nó físico conectados por barramentos como o NVLink?
4. Qual é a razão pela qual o Paralelismo de Pipeline é amplamente evitado em sistemas de inferência interativos de baixa latência?
5. Como o Paralelismo de Réplicas atua para aumentar a vazão de atendimento em aplicações com alto tráfego concorrente?
6. O que são as primitivas de comunicação coletiva All-Reduce e em qual momento do cálculo matricial elas são acionadas?
7. Como o Paralelismo de Contexto opera para viabilizar o processamento de prompts que contêm centenas de milhares de tokens?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Kernels e Compiladores de IA

**Rede:** `ai-engineering`  
**Área:** `infraestrutura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 437–440

## 📝 Definição

### Definição formal

Os **Kernels e Compiladores de IA** (*AI Kernels and Compilers*) constituem a camada de software de baixo nível e otimização de tempo de compilação que converte representações declarativas de grafos neurais em código de máquina altamente otimizado para o silício dos aceleradores de hardware:
1. **Kernel de IA:** Uma rotina de código especializada escrita em linguagens de controle de hardware (como CUDA, OpenAI Triton ou AMD ROCm) projetada para ser executada massivamente em paralelo por milhares de threads em uma GPU ou TPU, implementando operações matemáticas fundamentais (multiplicação matricial, convolução ou atenção);
2. **Compilador de IA:** Um software de tradução e otimização intermediária (como *torch.compile*, TensorRT, OpenXLA e Apache TVM) que executa a transformação estrutural (*lowering*) do grafo do modelo, aplicando técnicas de **fusão de operadores (*operator fusion*)**, **reordenação de loops (*loop tiling*)**, **vetorização** e eliminação de alocações redundantes de memória.

### Em linguagem simples

É a tradução do código em Python para a linguagem bruta que a placa de vídeo entende de verdade. Programar em Python é fácil e flexível para humanos, mas é lento e desorganizado para a máquina. Os compiladores de IA e os kernels pegam as equações da rede neural e juntam várias contas seguidas em uma única passagem rápida dentro do chip (fusão de operadores), garantindo que a placa de vídeo não perca tempo salvando e lendo resultados intermediários na memória lenta.

### Escopo e distinções

Não se confunde com compiladores de software tradicionais (como GCC ou Clang para C++). Compiladores de IA operam sobre **grafos de tensores multidimensionais**, otimizando fluxos de dados matriciais e alocação estática de memória em aceleradores paralelos.

## 🧩 Problema que resolve

Resolve a ineficiência do modelo interpretado em Python. No código convencional com PyTorch sem compilação, para calcular uma camada com ativação (ex.: Multiplicação $\to$ Bias $\to$ ReLU), a GPU precisa carregar os dados da memória física HBM três vezes separadas para cada operação elementar. Kernels fundidos e compiladores unem essas três etapas em um único circuito computacional, eliminando viagens desnecessárias à memória.

## 💡 Intuição

Pense em um trabalhador limpando uma janela de vidro de três andares:
- No **modo sem compilação (não fundido)**, ele pega o balde com água e passa na janela inteira do prédio. Depois guarda o balde, desce a escada, pega o rodo, sobe a escada e passa o rodo na janela inteira. Depois desce a escada, pega o pano seco, sobe de novo e seca o vidro. Ele subiu e desceu a escada três vezes para fazer três tarefas simples (**leitura e gravação repetida na memória VRAM**).
- No **modo compilado com fusão de operadores**, o trabalhador sobe a escada segurando o balde, o rodo e o pano de uma vez. Em cada pedaço de vidro, ele molha, passa o rodo e seca no mesmo instante antes de dar o próximo passo (**processamento dentro da SRAM rápida**). Ele limpa o prédio em um terço do tempo.

## ⚙️ Como funciona

A otimização atua estruturando o grafo de computação através de quatro transformações canônicas:

### Etapas

1. **Captura do Grafo (*Graph Capture*):** O compilador (ex.: *torch.compile*) rastreia as operações executadas pelo código Python e constrói um grafo estático de dependências.
2. **Fusão de Operadores (*Operator Fusion*):** O compilador identifica operadores sequenciais que atuam sobre os mesmos dados (ex.: multiplicação matricial seguida de adição de bias e ativação GELU) e os funde em um único kernel indivisível.
3. **Loop Tiling (Reordenação de Acesso):** O algoritmo fatia laços de repetição em blocos dimensionados para caber com precisão cirúrgica dentro dos limites de capacidade da memória estática ultra-rápida on-chip (**SRAM**) da GPU.
4. **Vetorização e Paralelização:** O código organiza os dados para que as instruções matemáticas operem sobre múltiplos elementos contíguos de memória simultaneamente através de instruções SIMD/SIMT.
5. **Geração de Código de Máquina (*Lowering*):** O compilador emite código binário nativo para o hardware (ex.: instruções PTX/SASS para NVIDIA ou binários para TPUs).

### Entradas e saídas

- **Entradas:** Código do modelo em framework de alto nível (PyTorch, TensorFlow).
- **Saídas:** Binários compilados e kernels em baixo nível otimizados para a microarquitetura alvo.

## 📐 Formulação matemática

Considere duas operações matriciais elementares consecutivas sobre a entrada $X$: uma adição linear $A = X + W_1$ seguida por uma ativação não-linear $Y = \text{ReLU}(A) = \max(0, A)$.
- **Sem Fusão de Operadores:**
  - Passo 1: Lê $X$ e $W_1$ da HBM $\to$ Computa soma na ALU $\to$ Grava $A$ na HBM ($2 \text{ leituras} + 1 \text{ escrita}$);
  - Passo 2: Lê $A$ da HBM $\to$ Computa $\max(0, A)$ na ALU $\to$ Grava $Y$ na HBM ($1 \text{ leitura} + 1 \text{ escrita}$).
  - Custo total de memória: **3 leituras + 2 escritas na VRAM**.
- **Com Fusão de Operadores:**
  - Kernel fundido carrega $X$ e $W_1$ nos registradores/SRAM $\to$ Computa $Y = \max(0, X + W_1)$ no mesmo ciclo $\to$ Grava apenas $Y$ final na HBM.
  - Custo total de memória: **2 leituras + 1 escrita na VRAM** (redução de $40\%$ no tráfego de barramento físico).

O estudo de caso da equipe do PyTorch (2023) citado no capítulo demonstrou que a aplicação do `torch.compile` combinada com quantização INT8/INT4 e decodificação especulativa multiplicou por várias vezes a vazão de geração do Llama-7B em uma GPU A100.

## 🧱 Hipóteses e condições de validade

- O grafo de execução do modelo deve possuir formas de tensores (*tensor shapes*) preferencialmente estáticas ou com dinamismo controlado; grafos com variações imprevisíveis a cada chamada forçam o compilador a re-compilar o código frequentemente (*re-compilation overhead*), degradando o desempenho.

## ✅ Quando usar

- Homologação de qualquer modelo aberto em ambientes corporativos de alto tráfego antes de colocá-lo para atender requisições de clientes.
- Construção de kernels especializados para novas arquiteturas neurais que não possuem suporte nativo otimizado em bibliotecas padrão de mercado (usando OpenAI Triton).

## 🚫 Quando não usar

- Em sessões rápidas de depuração e experimentação exploratória de código onde o tempo de espera da primeira compilação inicial (*warmup compile time*) atrapalha o ciclo de teste do cientista de dados.

## ⚠️ Limitações e armadilhas

- **Linguagens de baixo nível difíceis de dominar:** Programar kernels em CUDA clássico exige gerenciar manualmente sincronização de threads e perigos de concorrência (*race conditions*); ferramentas como Triton mitigam essa barreira ao permitir escrever kernels em sintaxe similar a Python.
- **Incompatibilidade entre gerações de GPUs:** Um kernel hiper-otimizado para a arquitetura NVIDIA A100 (como o FlashAttention original) pode apresentar desempenho abaixo do esperado em uma H100 se não for reestruturado para aproveitar os novos recursos assíncronos do silício (como o FlashAttention-3).

## 🔍 Comparações

| Abordagem | Facilidade de Escrita | Eficiência de Execução | Controle de Memória |
|---|---|---|---|
| **Python Puro (PyTorch eager)** | **Máxima (rápido e intuitivo)** | Moderada a Baixa | Abstrato (gerenciado pelo framework) |
| **torch.compile / Compiladores**| Alta (basta 1 linha de código) | **Excelente e automatizada** | Otimizado via grafos estáticos |
| **Kernels Manuais em CUDA/Triton**| Baixa (exige engenharia sênior) | **Máxima Absoluta** | **Controle manual milimétrico na SRAM** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um engenheiro nota que seu pipeline de inferência de visão computacional passa $40\%$ do tempo de cada frame convertendo imagens de formato e aplicando filtros de brilho em passos separados no PyTorch.
Ele adiciona a linha de código `modelo_otimizado = torch.compile(modelo)`.
Na primeira execução, o compilador analisa o código por alguns segundos, identifica 12 operações matriciais menores consecutivas, remove as passagens redundantes de memória VRAM e funde todas as operações em um único kernel de baixo nível. A partir da segunda execução, a taxa de quadros por segundo da aplicação salta de 30 FPS para 85 FPS sem nenhuma alteração nos pesos matemáticos da rede.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/aceleradores-de-ia-e-hierarquia-de-memoria.md|Aceleradores de IA e Hierarquia de Memória]]
- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]

### Complementos

- [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|Otimização do KV Cache e PagedAttention]]
- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]

### Alternativas

- Execução puramente interpretada em modo dinâmico convencional (*Eager Mode*).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/quantizacao.md|Quantização]]
- [[redes/ai-engineering/conceitos/decodificacao-especulativa-e-paralela.md|Decodificação Especulativa e Paralela]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 437–440
- **Evidência:** Chip Huyen aborda a escrita de kernels especializados em CUDA, Triton e ROCm, detalha as quatro técnicas centrais de otimização de baixo nível (vetorização, paralelização, loop tiling e fusão de operadores) e analisa compiladores de IA como torch.compile, OpenXLA, TensorRT e TVM, ilustrando os saltos cumulativos de vazão obtidos pela equipe do PyTorch (Figura 9-14).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é um Kernel de IA e em que ele se diferencia de um programa de software convencional em Python?
2. Quais são as quatro técnicas clássicas de otimização de baixo nível aplicadas na programação de kernels em aceleradores?
3. Como a técnica de Fusão de Operadores (*Operator Fusion*) atua fisicamente para reduzir o tráfego de dados na memória VRAM?
4. Qual é o papel da linguagem OpenAI Triton na democratização da escrita de kernels para engenheiros de IA?
5. O que é o processo de *Lowering* executado por compiladores de IA como o *torch.compile* ou o TensorRT?
6. Como o estudo de caso da equipe do PyTorch demonstrou o efeito cumulativo de combinar compilador, quantização e decodificação especulativa?
7. Por que matrizes de tensores com formas altamente dinâmicas podem gerar sobrecarga de compilação repetida em compiladores de grafos estáticos?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.


*Nota gerada a partir do capítulo Capítulo 9 — Inference Optimization. A interpretação final deve ser revisada pelo estudante.*
