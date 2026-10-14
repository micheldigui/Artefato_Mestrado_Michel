# AI Engineering: Building Applications with Foundation Models — Capítulo 9

## Objetivo do capítulo

Examinar os fundamentos, métricas, gargalos físicos e técnicas multidisciplinares de otimização de inferência para modelos de fundação. O capítulo detalha como acelerar a velocidade de processamento e reduzir os custos operacionais atuando em três níveis complementares: no nível de modelo (compressão, superação do gargalo autoregressivo com decodificação especulativa e otimizações na atenção/KV Cache), no nível de hardware (arquitetura de aceleradores, tipos de memória e unidades de computação) e no nível de serviço de inferência (batching contínuo, desacoplamento de prefill e decode, prompt caching e paralelismo distribuído).

## Resumo do argumento central

Embora o treinamento de grandes modelos atraia grande parte da atenção pública, a inferência responde por até 90% dos custos totais de sistemas de aprendizado de máquina ao longo de seu ciclo de vida. Uma aplicação com excelente precisão é inviável se for lenta demais para a paciência do usuário ou excessivamente cara para a sustentabilidade do modelo de negócio. A inferência de grandes modelos de linguagem (LLMs) é dividida em duas etapas com gargalos físicos distintos: o prefill (paralelo e limitado por capacidade de cálculo — *compute-bound*) e o decode (sequencial e limitado pela taxa de transferência de memória — *memory-bandwidth bound*).

A otimização eficaz exige balancear compensações (*trade-offs*) entre latência (TTFT e TPOT) e vazão/custo (*throughput* e *goodput*), além de monitorar métricas de eficiência real de hardware como MFU e MBU, superando as ilusões de métricas superficiais de GPU. No nível do modelo, o KV Cache é o principal limitador de escalabilidade de contexto, demandando inovações como PagedAttention, atenção agrupada (GQA) e kernels fundidos como FlashAttention, enquanto a decodificação especulativa rompe o gargalo autoregressivo permitindo a verificação paralela de múltiplos tokens. No nível de serviço, a transição do batching estático para o batching contínuo (*in-flight*), o desacoplamento de instâncias dedicadas de prefill e decode, a reutilização de prefixos via prompt caching e estratégias híbridas de paralelismo (tensor, pipeline e réplicas) completam a pilha de aceleração necessária para operar IA generativa em escala industrial.

## Conceitos identificados

- Gargalos Computacionais e Intensidade Aritmética
- Métricas de Desempenho de Inferência
- Aceleradores de IA e Hierarquia de Memória
- Otimização do KV Cache e PagedAttention
- Decodificação Especulativa e Paralela
- Batching Contínuo e Dinâmico
- Prompt Caching e Reutilização de Contexto
- Desacoplamento de Prefill e Decode
- Estratégias de Paralelismo em Inferência
- Kernels e Compiladores de IA
- Fases de Inferência: Prefill e Decode
- Mecanismo de Atenção
- Quantização
- Modelo de Fundação
- Representações Numéricas e Precisão

## Sequência lógica do capítulo

1. **Entendendo a Otimização de Inferência (pp. 406–425):**
   - *Visão Geral de Inferência:* Servidor versus serviço de inferência; gargalos fundamentais (*compute-bound* vs. *memory-bandwidth bound*); modelo Roofline e intensidade aritmética; assimetria entre prefill e decode; APIs online (latência/streaming) versus APIs em lote (*batch*).
   - *Métricas de Performance:* Decomposição da latência (TTFT, TPOT, tempo entre tokens / ITL, percentis p50/p90/p99); vazão (*throughput* em TPS e RPM) e *goodput* (atendimento a SLOs); métricas de utilização real: falhas do `nvidia-smi`, MFU (*Model FLOP/s Utilization*) e MBU (*Model Bandwidth Utilization*).
   - *Aceleradores de IA:* Comparação entre CPUs e GPUs/TPUs; unidades computacionais (escalares, vetores, matrizes/tensores); capacidade de cálculo (FLOP/s em FP32, TF32, FP16, BF16 e FP8); hierarquia de memória (DRAM do host, HBM da GPU, SRAM/caches L1/L2/L3); consumo de energia, dissipação térmica (TDP) e limites de eletricidade em data centers; critérios para seleção de aceleradores.
2. **Otimização de Modelos (pp. 426–440):**
   - *Compressão de Modelo:* Revisão de quantização e destilação; poda (*pruning*) estruturada e não estruturada; esparsidade.
   - *Superando o Gargalo Autoregressivo:* Decodificação especulativa (*speculative decoding* com modelo rascunho/proposta); inferência com referência (cópia de trechos do contexto); decodificação paralela (decodificação de Jacobi / Lookahead e cabeças múltiplas Medusa).
   - *Otimização da Atenção e KV Cache:* Cálculo da pegada de memória do KV Cache ($2 \times B \times S \times L \times H \times M$); redesign de atenção (atenção em janela local, atenção entre camadas / cross-layer, Multi-Query Attention e Grouped-Query Attention — GQA); gestão de memória com PagedAttention (vLLM); quantização de KV Cache; kernels especializados (FlashAttention e FlashAttention-3).
   - *Kernels e Compiladores:* Programação em baixo nível (CUDA, Triton, ROCm); técnicas de aceleração (vetorização, paralelização, loop tiling, fusão de operadores); compilers e ferramentas de lowering (*torch.compile*, OpenXLA, TensorRT, TVM, MLIR); estudo de caso de throughput no PyTorch.
3. **Otimização do Serviço de Inferência (pp. 440–447):**
   - *Batching:* Batching estático versus dinâmico; batching contínuo (*in-flight batching*, framework Orca).
   - *Desacoplamento de Prefill e Decode:* Disagregação física de instâncias (*DistServe*, *Inference Without Interference* / Splitwise) e otimização das razões de instâncias de prefill e decode.
   - *Prompt Caching:* Armazenamento e reuso de representações de prefixos estáticos (system prompts, documentos de RAG) e economias de custo/TTFT documentadas (Google Gemini, Anthropic Claude).
   - *Paralelismo:* Paralelismo de réplicas (*data parallelism* na inferência); paralelismo de modelo: paralelismo de tensores (intra-operador / colunar e linear) e paralelismo de pipeline (estágios com micro-lotes); paralelismo de contexto e de sequência.

## Principais afirmações

- A inferência é a fase economicamente determinante da inteligência artificial aplicada, correspondendo historicamente a até 90% dos gastos com machine learning em produção.
- Uma operação é classificada como *compute-bound* ou *memory-bandwidth bound* com base em sua intensidade aritmética (FLOPs por byte de acesso à memória), mapeada graficamente através do modelo Roofline.
- A fase de prefill de um LLM é *compute-bound* e paralela, ditando o TTFT; a fase de decode é *memory-bandwidth bound* e sequencial, ditando o TPOT.
- O percentual de "GPU Utilization" reportado pelo comando `nvidia-smi` é enganoso, pois indica apenas o tempo em que os circuitos da GPU estiveram ativos, e não a eficiência real de uso do silício; métricas de engenharia corretas são o MFU (utilização de FLOP/s teóricos) e o MBU (utilização da largura de banda teórica da memória).
- A memória dedicada de alta largura de banda (HBM) das GPUs é uma ordem de magnitude mais rápida que a memória DRAM de CPUs, mas seu limite de capacidade física é o principal gargalo para contextos longos devido ao crescimento do KV Cache.
- O tamanho do KV Cache em modelos Transformer densos cresce linearmente com o comprimento do contexto e tamanho do lote, podendo superar em até três vezes a pegada dos próprios pesos do modelo em cenários de contexto extenso.
- A decodificação especulativa é uma técnica sem perdas (*lossless*) que acelera a inferência aproveitando FLOPs ociosos durante o decode para verificar sequências de tokens sugeridas por um modelo menor.
- O batching contínuo (*in-flight batching*) elimina a ineficiência do batching tradicional ao permitir que novas requisições entrem no processamento assim que requisições finalizadas liberam seus recursos.
- O desacoplamento físico das fases de prefill e decode em nós de computação separados neutraliza a interferência mútua, otimizando simultaneamente o TTFT e o TPOT.
- O prompt caching reduz drasticamente custos de tokens de entrada (em até 90%) e o tempo de pré-preenchimento ao reaproveitar estados de atenção de trechos textuais repetitivos entre requisições.

## Fórmulas ou procedimentos apresentados

- Intensidade Aritmética ($AI$):
  $$AI = \frac{\text{Operações de Ponto Flutuante (FLOPs)}}{\text{Tráfego de Dados de Memória (Bytes)}}$$
- Latência Total de Inferência Autorregressiva:
  $$\text{Latência}_{\text{total}} = \text{TTFT} + \text{TPOT} \times (N_{\text{tokens\_saída}} - 1)$$
- Cálculo de Largura de Banda de Memória Efetiva em LLMs:
  $$\text{Largura de Banda Utilizada} = N_{\text{parâmetros}} \times \text{Bytes/parâmetro} \times \text{Tokens/segundo}$$
- Model Bandwidth Utilization (MBU):
  $$\text{MBU} = \frac{N_{\text{parâmetros}} \times \text{Bytes/parâmetro} \times \text{Tokens/segundo}}{\text{Largura de Banda Teórica de Pico da GPU}}$$
- Tamanho Teórico do KV Cache (sem otimizações):
  $$\text{Memória}_{\text{KV\_Cache}} = 2 \times B \times S \times L \times H \times M \text{ bytes}$$
  *(onde $B$ é o batch size, $S$ é o comprimento da sequência, $L$ é o número de camadas Transformer, $H$ é a dimensão oculta do modelo e $M$ é o número de bytes por valor na representação numérica).*
- Pontuação do Goodput sob Restrições de SLO:
  $$\text{Goodput} = \frac{1}{\Delta t} \sum_{i \in \text{Requisições}} \mathbb{I}\Big(\text{TTFT}_i \le \text{SLO}_{\text{TTFT}} \;\land\; \text{TPOT}_i \le \text{SLO}_{\text{TPOT}}\Big)$$

## Exemplos relevantes

- Cálculo de MBU no Llama 2-70B em FP16 (2 bytes por peso): gerando 100 tokens/s, o modelo consome $70 \times 10^9 \times 2 \times 100 = 700 \text{ GB/s}$ de largura de banda. Em uma GPU A100 de 80 GB com pico teórico de 2.000 GB/s, o MBU atinge $35\%$.
- Experimento da Anyscale: um único token de saída na fase de decode tem impacto sobre a latência equivalente ao processamento de 100 tokens de entrada na fase de prefill.
- Caso Character.AI: com média de 180 mensagens de histórico conversacional por usuário, a empresa utilizou multi-query attention, camadas locais/globais intercaladas e cross-layer attention para reduzir o KV Cache em mais de 20 vezes, tornando o volume de memória insignificante para lotes massivos.
- Tabela de economia do Prompt Caching na Anthropic: redução de 79% no TTFT (de 11,5 s para 2,4 s) e economia financeira de 90% em consultas sobre livros de 100.000 tokens em cache.
- Estudo de caso de compilação no PyTorch: o encadeamento sucessivo de `torch.compile`, quantização INT8, quantização INT4 e decodificação especulativa elevou a vazão de geração do Llama-7B em múltiplas vezes em uma GPU A100.

## Limitações e ressalvas

- O cálculo analítico da intensidade aritmética e limites de hardware varia conforme a implementação exata dos kernels de baixo nível e o suporte a instruções de hardware específicas (como núcleos Tensor).
- O ganho real da decodificação especulativa depende fortemente da taxa de aceitação de tokens do modelo rascunho, que oscila conforme a previsibilidade do domínio (alta em código estruturado, menor em prosa criativa).

## Dúvidas em aberto

- Como conciliar o aumento contínuo de janelas de contexto com os limites térmicos e de densidade de empacotamento das futuras gerações de memórias HBM?
- Em que medida arquiteturas de decodificação puramente paralelas (como Medusa ou difusão discreta) conseguirão substituir integralmente o loop autorregressivo sem perda de coerência semântica?

## Localização da fonte

Capítulo 9, páginas 405 a 448 do livro impresso / arquivo de texto consolidado.
