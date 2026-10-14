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
