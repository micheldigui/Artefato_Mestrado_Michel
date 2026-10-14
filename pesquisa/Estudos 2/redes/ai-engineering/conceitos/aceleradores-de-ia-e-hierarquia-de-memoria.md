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
