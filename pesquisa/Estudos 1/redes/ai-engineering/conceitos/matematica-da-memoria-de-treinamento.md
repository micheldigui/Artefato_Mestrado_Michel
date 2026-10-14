# 🧠 Matemática da Memória de Treinamento

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 319–325

## 📝 Definição

### Definição formal

A **Matemática da Memória de Treinamento** (*Training Memory Math*) é o conjunto de formulações analíticas e restrições de engenharia que quantifica o consumo total de memória física (VRAM em GPUs ou TPUs) exigido durante a execução do algoritmo de retropropagação (*backpropagation*) para ajustar os parâmetros de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]]. 

A pegada de memória divide-se em quatro componentes computacionais:
1. **Pesos do Modelo (*Model Weights*):** Os parâmetros que definem a arquitetura da rede neural;
2. **Ativações (*Activations*):** Os tensores intermediários calculados durante a passagem direta (*forward pass*), mantidos em memória para o cálculo da regra da cadeia no gradiente descendente;
3. **Gradientes (*Gradients*):** As derivadas parciais da função de perda calculadas para cada parâmetro treinável durante a passagem reversa (*backward pass*);
4. **Estados do Otimizador (*Optimizer States*):** Variáveis estatísticas mantidas por algoritmos adaptativos (como os momentos de primeira e segunda ordem no **Adam**) para guiar a taxa de atualização de cada peso.

### Em linguagem simples

É a conta de padaria que o engenheiro precisa fazer para saber se o modelo vai caber na placa de vídeo durante o treinamento sem dar o erro fatal de falta de memória (*Out of Memory* — OOM). Enquanto rodar um modelo para responder perguntas (inferência) só precisa guardar os pesos da IA, treiná-la exige guardar também o rascunho de todas as contas intermediárias, os erros cometidos e o histórico do otimizador, fazendo o consumo de memória explodir em até 4 a 6 vezes.

### Escopo e distinções

Diferencia-se da memória de inferência. Na inferência, não existem gradientes nem estados de otimizador, e as ativações são descartadas logo após a geração de cada camada (restando apenas o KV Cache). No treinamento supervisionado ou ajuste fino, a necessidade de atualizar pesos introduz uma sobrecarga massiva proporcional ao número de **parâmetros treináveis**.

## 🧩 Problema que resolve

Resolve a imprevisibilidade de dimensionamento de hardware em projetos de ajuste fino. Permite que equipes calculem com antecedência exata se um modelo de 7B ou 70B parâmetros caberá em uma GPU de 24 GB, 48 GB ou 80 GB, e orienta a adoção de técnicas de mitigação como *gradient checkpointing* ou [[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|PEFT]].

## 💡 Intuição

Pense em um arquiteto revisando uma maquete complexa:
- Na **Inferência**, ele apenas olha a maquete pronta e aponta onde fica a porta principal (**apenas pesos estáticos**).
- No **Treinamento**, ele precisa desmontar e remontar partes da maquete. Para cada peça que ele mexe, ele precisa manter na bancada o manual de montagem (**pesos**), as anotações das medidas temporárias de cada coluna (**ativações**), o cálculo de quantos milímetros a viga ficou torta (**gradientes**) e o histórico de quantas vezes ele já tentou ajustar aquela madeira nos últimos dez minutos (**estados do otimizador**). A bancada de trabalho precisa ser imensamente maior.

## ⚙️ Como funciona

A alocação de memória varia conforme as etapas de cada passo de treino (*step*):

### Etapas

1. **Carregamento dos Pesos:** Os parâmetros da rede são alocados na VRAM (ex.: um modelo de 7B em 16 bits ocupa 14 GB fixos).
2. **Passagem Direta (*Forward Pass*):** O modelo processa o lote de dados (*batch*). As ativações geradas por cada camada de atenção e MLP são salvas na memória para reutilização.
3. **Passagem Reversa (*Backward Pass*):** A função de perda calcula o erro. O algoritmo propaga o gradiente de trás para frente usando as ativações salvas, alocando tensores de gradiente para cada parâmetro treinável.
4. **Passo do Otimizador (*Optimizer Step*):** O otimizador Adam lê os gradientes e atualiza os pesos utilizando o momento acumulado e o segundo momento não centrado mantidos em seus tensores de estado.
5. **Mitigação via Gradient Checkpointing:** Em vez de guardar todas as ativações intermediárias na VRAM durante o forward pass, o sistema descarta a maioria delas e as **recalcula sob demanda** durante o backward pass, trocando um aumento de cerca de 20% a 30% no tempo de processamento por uma redução drástica de até 70% na memória de ativação.

### Entradas e saídas

- **Entradas:** Arquitetura do modelo, tamanho do vocabulário, tamanho de lote (*batch size*), comprimento de contexto e tipo de otimizador.
- **Saídas:** Estimativa exata em gigabytes do requisito de VRAM por dispositivo acelerador.

## 📐 Formulação matemática

Para um modelo denso com $N$ parâmetros totais e $N_{\text{trein}}$ parâmetros treináveis, armazenados em formato de $b$ bytes por valor (onde $b=2$ para FP16/BF16 e $b=4$ para FP32):

$$\text{Memória}_{\text{pesos}} = N \cdot b \text{ bytes}$$

$$\text{Memória}_{\text{gradientes}} = N_{\text{trein}} \cdot b \text{ bytes}$$

Para o otimizador **Adam** tradicional (que mantém uma cópia mestre dos pesos em FP32, o primeiro momento $m_t$ e o segundo momento $v_t$):

$$\text{Memória}_{\text{Adam}} = N_{\text{trein}} \cdot (4_{\text{cópia FP32}} + 4_{\text{momento}} + 4_{\text{variância}}) = 12 \cdot N_{\text{trein}} \text{ bytes}$$

Se o otimizador mantiver os estados em 16 bits: $\text{Memória}_{\text{Adam}} \ge 2 \times N_{\text{trein}} \times b = 4 \cdot N_{\text{trein}}$ bytes.
Somando os componentes estáticos para **Ajuste Fino Completo (*Full Finetuning*)** com $N = N_{\text{trein}}$ em 16 bits ($b=2$):

$$\text{Memória}_{\text{estática}} = \text{Pesos}(2N) + \text{Gradientes}(2N) + \text{Adam}(12N) = 16N \text{ bytes}$$

Para um modelo de **7 bilhões de parâmetros** ($N = 7 \times 10^9$):
$$\text{Memória}_{\text{estática}} = 16 \times 7 \times 10^9 \text{ bytes} \approx 112 \text{ GB}$$
Valor que excede a capacidade de uma GPU de topo de linha A100/H100 de 80 GB, antes mesmo de somar a memória de ativações.

## 🧱 Hipóteses e condições de validade

- A formulação assume o uso do otimizador Adam. Se for utilizado SGD puro sem momento, a memória de estados de otimizador cai para zero.
- A memória de ativações escala linearmente com o tamanho do lote (*batch size*) e com o comprimento da sequência de tokens.

## ✅ Quando usar

- Dimensionamento prévio de infraestrutura antes de iniciar qualquer pipeline de treinamento ou ajuste fino corporativo.
- Diagnóstico de falhas de estouro de memória (*CUDA Out of Memory*).

## 🚫 Quando não usar

- Em cálculos de inferência pura, onde gradientes e estados de otimizador inexistem e a memória é governada pelo tamanho dos pesos e do KV Cache.

## ⚠️ Limitações e armadilhas

- **Subestimar a memória de ativações:** Em contextos longos (ex.: 8K ou 32K tokens) e lotes grandes, o volume de ativações pode superar o tamanho dos próprios pesos do modelo se o *gradient checkpointing* estiver desativado.
- **Ignorar a precisão do otimizador:** Supor que treinar em FP16 significa que o otimizador também usará 16 bits. A maioria dos frameworks mantém os estados do Adam em FP32 para evitar instabilidade numérica, elevando a sobrecarga.

## 🔍 Comparações

| Componente de Memória | Depende de quê? | Proporção Típica (Full FT em 16 bits) |
|---|---|---|
| **Pesos do Modelo** | Tamanho total do modelo ($N$) | $2 \text{ bytes} \times N$ |
| **Gradientes** | Parâmetros treináveis ($N_{\text{trein}}$) | $2 \text{ bytes} \times N_{\text{trein}}$ |
| **Estados do Adam** | Parâmetros treináveis ($N_{\text{trein}}$) | $8 \text{ a } 12 \text{ bytes} \times N_{\text{trein}}$ |
| **Ativações** | Contexto, Batch size, Camadas | Variável (reduzível com checkpointing) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um engenheiro possui uma GPU RTX 4090 de 24 GB e deseja fazer o ajuste fino de um modelo Llama de 7B parâmetros.
- Se tentar fazer **Full Finetuning**: Pesos (14 GB) + Gradientes (14 GB) + Otimizador Adam ($\ge 28$ GB) = Mais de 56 GB de memória estática. A GPU sofre pane de *CUDA OOM* antes de processar o primeiro dado.
- Se aplicar **LoRA (PEFT)** com apenas 70 milhões de parâmetros treináveis ($1\%$ do modelo): Pesos congelados (14 GB) + Gradientes do LoRA (0,14 GB) + Adam do LoRA (0,56 GB) = Apenas $\approx 14{,}7$ GB de memória estática. O modelo roda tranquilamente com folga dentro dos 24 GB da placa.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Complementos

- [[redes/ai-engineering/conceitos/representacoes-numericas-e-precisao.md|Representações Numéricas e Precisão]]
- [[redes/ai-engineering/conceitos/quantizacao.md|Quantização]]
- [[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|Ajuste Fino Eficiente em Parâmetros (PEFT)]]

### Alternativas

- Técnicas de descarregamento para CPU (*CPU Offloading*) e particionamento de estados (ZeRO/DeepSpeed).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]
- [[redes/ai-engineering/conceitos/hiperparametros-de-ajuste-fino.md|Hiperparâmetros de Ajuste Fino]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 319–325
- **Evidência:** Chip Huyen formaliza a equação de memória de treinamento com backpropagation, analisa a pesquisa de Korthikanti et al. (2022) demonstrando que a memória de ativações pode superar o tamanho dos pesos em modelos Megatron e detalha a aritmética do otimizador Adam com gradientes.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são os quatro componentes fundamentais que compõem a pegada de memória VRAM durante o treinamento de um LLM?
2. Por que a memória exigida para o treinamento é ordens de magnitude superior à memória de inferência para o mesmo modelo?
3. Como o otimizador Adam atua sobre a memória e por que ele consome mais VRAM do que os próprios pesos do modelo no ajuste fino completo?
4. O que é a técnica de *Gradient Checkpointing* e qual compromisso de engenharia ela estabelece entre tempo de computação e memória?
5. Como a redução do número de parâmetros treináveis através de PEFT/LoRA afeta diretamente a fórmula da memória do otimizador?
6. Por que manter ativações intermediárias na VRAM é um requisito obrigatório para a execução do algoritmo de retropropagação clássico?
7. Qual é a pegada aproximada de memória estática em gigabytes necessária para executar o Full Finetuning de um modelo de 13 bilhões de parâmetros em 16 bits?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Representações Numéricas e Precisão

**Rede:** `ai-engineering`  
**Área:** `infraestrutura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 325–328

## 📝 Definição

### Definição formal

As **Representações Numéricas e Precisão** (*Numerical Representations and Precision*) definem os formatos e padrões de codificação em nível de bits (seguindo ou adaptando a norma IEEE 754) utilizados para armazenar e computar pesos matemáticos, ativações e gradientes em hardware de aceleração de IA. 

Cada formato de ponto flutuante distribui seus bits entre três componentes fundamentais:
1. **Bit de Sinal:** Determina se o número é positivo ou negativo ($1 \text{ bit}$);
2. **Bits de Alcance (*Exponent*):** Determinam a magnitude máxima e mínima representável sem causar estouro numérico (*overflow* ou *underflow*);
3. **Bits de Precisão (*Mantissa / Significand*):** Determinam a granularidade e resolução das casas decimais do valor.

### Em linguagem simples

É a maneira como o computador anota os números da rede neural na memória usando zeros e uns. Você pode usar um formato pesado como o FP32 (que usa 32 bits para anotar cada número com dezenas de casas decimais perfeitas) ou formatos modernos mais leves como o FP16 e o BF16 (que usam metade da memória, apenas 16 bits). A grande sacada é que o BF16 prefere ter espaço para números gigantes e minúsculos sem quebrar as contas, enquanto o FP16 prefere ter mais casas decimais exatas.

### Escopo e distinções

Não se confunde com o conceito de precisão em métricas de avaliação (como precisão e revocação). Trata-se da resolução computacional dos dados no silício. Formatos principais incluem **FP32** (precisão simples), **FP16** (meia precisão), **BF16** (Brain Floating Point, criado pelo Google), **TF32** (formato híbrido interno de 19 bits da NVIDIA) e formatos inteiros de quantização como **INT8** e **INT4**.

## 🧩 Problema que resolve

Resolve a saturação de memória e a lentidão de processamento em aceleradores de IA. Armazenar trilhões de operações em FP32 consome memória VRAM em excesso e satura barramentos físicos de transferência. A transição para formatos de 16 ou 8 bits reduz o consumo de memória pela metade ou por quatro vezes, acelerando multiplicações de matrizes nos núcleos especializados das GPUs.

## 💡 Intuição

Pense em medir ingredientes para fazer um bolo:
- O formato **FP32** é uma balança de laboratório químico de alta precisão que mede até o milionésimo de grama. É perfeita, mas o display demora para estabilizar e o aparelho é enorme e caro.
- O formato **BF16** é uma balança de cozinha comum que aguenta sacos pesados de farinha sem quebrar e mede os gramas com precisão suficiente para a receita do bolo dar certo. Para redes neurais, a "balança de cozinha" funciona tão bem quanto a balança de laboratório químico e permite produzir dez vezes mais bolos no mesmo tempo.

## ⚙️ Como funciona

A arquitetura dos formatos distribui os bits conforme suas prioridades operacionais:

### Etapas

1. **FP32 (Padrão IEEE 754):** Aloca 1 bit de sinal, 8 bits de expoente (alcance) e 23 bits de mantissa (precisão). Ocupa 4 bytes por parâmetro.
2. **FP16 (Meia Precisão):** Aloca 1 bit de sinal, 5 bits de expoente e 10 bits de mantissa. Ocupa 2 bytes. O alcance é limitado: números maiores que $65.504$ sofrem estouro para infinito ($\text{INF}$), causando instabilidade no treino.
3. **BF16 (BFloat16):** Aloca 1 bit de sinal, **8 bits de expoente** (o mesmo alcance que o FP32) e 7 bits de mantissa. Ocupa 2 bytes. O modelo ganha imunidade contra estouros de gradientes, sacrificando apenas pequenas casas decimais irrelevantes para redes profundas.
4. **TF32 (TensorFloat-32):** Formato proprietário da NVIDIA para núcleos tensores que usa 19 bits (1 sinal, 8 expoente, 10 mantissa), executando com a velocidade de 16 bits sem exigir alterações de código do usuário em FP32.

### Entradas e saídas

- **Entradas:** Matrizes numéricas contínuas de tensores neurais.
- **Saídas:** Representações compactadas com trade-offs conhecidos de truncamento decimal.

## 📐 Formulação matemática

A distribuição de bits nos formatos mais relevantes de IA estrutura-se como:

$$\text{FP32:} \quad [S_1 \mid E_8 \mid M_{23}] \implies \text{Alcance: } \approx 10^{\pm 38}, \quad \text{Precisão: } \approx 7 \text{ dígitos decimais}$$

$$\text{FP16:} \quad [S_1 \mid E_5 \mid M_{10}] \implies \text{Alcance: } \approx 10^{\pm 5}, \quad \text{Precisão: } \approx 3\text{--}4 \text{ dígitos decimais}$$

$$\text{BF16:} \quad [S_1 \mid E_8 \mid M_7] \implies \text{Alcance: } \approx 10^{\pm 38}, \quad \text{Precisão: } \approx 2 \text{ dígitos decimais}$$

O exemplo numérico do capítulo ilustra a perda de precisão com o número $1234{,}56789$:
- Em FP32: $1234{,}56789$;
- Em FP16: $1235{,}0$ (desvio relativo de $0{,}035\%$);
- Em BF16: $1232{,}0$ (desvio relativo de $0{,}208\%$).
Contudo, se o número for $123.456{,}789$, o FP16 sofre estouro para $\text{INF}$ (falha catastrófica), enquanto o BF16 o representa como $123.392{,}0$ com sucesso operacional.

## 🧱 Hipóteses e condições de validade

- O uso nativo de BF16 exige hardware compatível (GPUs NVIDIA da arquitetura Ampere A100/RTX 3000 em diante ou TPUs do Google); hardware mais antigo (como V100 ou T4) não suporta aceleração nativa de BF16.

## ✅ Quando usar

- **BF16:** Formato padrão recomendado para pré-treinamento e ajuste fino de grandes modelos de fundação em GPUs modernas.
- **FP16:** Padrão para inferência e treinamento em aceleradores que não dispõem de suporte físico a BF16.
- **FP32:** Reservado para o acúmulo de estados de otimizadores (Adam) e cálculo crítico de funções de perda onde a precisão de gradientes minúsculos é indispensável.

## 🚫 Quando não usar

- Não carregue modelos nativamente calibrados em BF16 dentro de instâncias forçadas para FP16 sem verificar a ocorrência de *overflows* (como o erro histórico que degradou o Llama 2).

## ⚠️ Limitações e armadilhas

- **O erro do carregamento cruzado:** Modelos modernos (Llama 2 e Llama 3) são treinados e disponibilizados em BF16. Se o engenheiro carregar o modelo em FP16 por engano em seu script, ativações que excedem $65.504$ viram $\text{INF}$, degradando drasticamente o desempenho do modelo em produção.
- **Underflow numérico:** Em gradientes minúsculos, formatos com poucos bits de expoente arredondam o valor para zero, paralisando o aprendizado da rede.

## 🔍 Comparações

| Formato | Bits Totais | Bits de Expoente (Alcance) | Bits de Mantissa (Precisão) | Risco de Overflow | Uso Primário |
|---|---|---|---|---|---|
| **FP32** | 32 bits (4 bytes) | 8 bits | 23 bits | Desprezível | Mestre de pesos e estados do Adam |
| **FP16** | 16 bits (2 bytes) | 5 bits | 10 bits | **Alto (teto em 65.504)** | Inferência em GPUs antigas |
| **BF16** | 16 bits (2 bytes) | **8 bits** | 7 bits | **Mínimo (mesmo do FP32)** | **Padrão ouro de treino moderno** |
| **TF32** | 19 bits (~2,4 bytes)| 8 bits | 10 bits | Mínimo | Aceleração interna em núcleos Tensor |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Durante o ajuste fino de um modelo de linguagem, uma camada profunda calcula um gradiente de magnitude $70.000{,}0$.
- Se o pipeline estiver configurado em **FP16**, o maior número que o formato consegue representar é $65.504$. O valor $70.000$ vira $\text{INF}$ (infinito). Na multiplicação seguinte, qualquer número multiplicado por infinito vira $\text{NaN}$ (*Not a Number*). Em três iterações, todos os parâmetros da rede viram $\text{NaN}$ e o treinamento é irremediavelmente destruído.
- Se o pipeline estiver em **BF16**, os 8 bits de expoente absorvem $70.000$ com facilidade (o teto é $\approx 10^{38}$). O treino prossegue estável até a convergência.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/matematica-da-memoria-de-treinamento.md|Matemática da Memória de Treinamento]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/quantizacao.md|Quantização]]
- [[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|Ajuste Fino Eficiente em Parâmetros (PEFT)]]

### Alternativas

- Formatos de precisão dupla (FP64 / 8 bytes), impraticáveis para redes neurais profundas devido à sobrecarga de memória.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/quantized-lora-qlora.md|Quantized LoRA (QLoRA)]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 325–328
- **Evidência:** Chip Huyen destrincha as representações numéricas do padrão IEEE 754, apresenta o diagrama comparativo de bits entre FP32, FP16, BF16 e TF32 (Figura 7-6), detalha a Tabela 7-3 com conversões concretas e analisa a armadilha empírica de carregar modelos Llama 2/Llama 3 em FP16 em vez de BF16.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a função dos bits de expoente e dos bits de mantissa na estrutura de um número de ponto flutuante?
2. Por que o formato BF16 tornou-se a representação padrão para o treinamento de grandes modelos de linguagem em vez do FP16?
3. O que acontece matematicamente quando uma operação em FP16 ultrapassa o valor escalar de 65.504?
4. Qual foi o erro de engenharia comum cometido por equipes ao carregar o modelo Llama 2 no formato FP16?
5. Como o formato proprietário TF32 da NVIDIA opera para acelerar cálculos matemáticos sem exigir mudanças de código do usuário?
6. Por que os estados do otimizador Adam continuam sendo frequentemente armazenados em FP32 mesmo quando o modelo é treinado em BF16?
7. Qual é a diferença fundamental entre formatos de ponto flutuante e formatos de números inteiros como INT8 e INT4?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Quantização

**Rede:** `ai-engineering`  
**Área:** `infraestrutura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 328–332

## 📝 Definição

### Definição formal

A **Quantização** (*Quantization*) é a técnica de compressão e aceleração de modelos neurais que consiste no mapeamento não linear ou afim de parâmetros contínuos de alta precisão (tipicamente representados em formatos de ponto flutuante de 32 ou 16 bits como FP32/FP16/BF16) para representações discretas de menor número de bits (como inteiros **INT8**, **INT4** ou formatos especializados como **NF4** e modelos de 1,58 bits), reduzindo o consumo de memória VRAM e a largura de banda exigida na inferência e no treinamento. 

Desdobra-se em duas abordagens primárias:
1. **Quantização Pós-Treinamento (*Post-Training Quantization* — PTQ):** O modelo é treinado normalmente em alta precisão e seus pesos são convertidos para baixa precisão após o término do treino;
2. **Treinamento Ciente de Quantização (*Quantization-Aware Training* — QAT):** O modelo simula os efeitos de arredondamento de baixa precisão durante a passagem direta do treinamento, permitindo que a rede aprenda a compensar os erros de truncamento antes da conversão final.

### Em linguagem simples

É a arte de "arredondar os números" da IA para que o modelo fique muito menor, mais leve e mais rápido. Em vez de salvar cada peso do cérebro da IA como um número decimal com 16 dígitos, você o converte para um número inteiro pequeno de 8 ou 4 bits. Isso reduz o tamanho do modelo de 40 GB para 10 GB, permitindo que você rode um modelo potente dentro de um computador comum ou até mesmo de um celular sem perder quase nada de inteligência.

### Escopo e distinções

Estritamente falando, na teoria matemática clássica de processamento de sinais, quantização aplica-se à conversão para números inteiros discretos (*fixed point*). No jargão consolidado da Engenharia de IA, o termo é utilizado de forma ampla para abranger qualquer redução de precisão de bits, incluindo formatos fracionários como FP8 e FP4.

## 🧩 Problema que resolve

Resolve o gargalo físico de memória e largura de banda que impede a implantação de LLMs em produção e em dispositivos de borda (*edge*). Modelos de 70B parâmetros em FP16 exigem 140 GB de VRAM apenas para carregar os pesos, inviabilizando servidores comuns. A quantização para INT4 comprime o mesmo modelo para cerca de 35 GB, viabilizando sua execução em hardware comercial com redução brutal de custos de nuvem.

## 💡 Intuição

Pense em salvar uma fotografia colorida de alta resolução em um computador antigo:
- A imagem original é salva no formato RAW sem compressão de 32 bits (**FP32**), onde cada pixel tem milhões de gradações de cores imperceptíveis para o olho humano. O arquivo ocupa 100 megabytes.
- A **Quantização** converte a imagem para o formato GIF ou JPEG comprimido de 8 bits (**INT8**). O algoritmo reduz a paleta para as 256 cores mais importantes. Se você olhar a foto na tela do celular, ela parece visualmente idêntica à original, mas o arquivo agora ocupa apenas 2 megabytes e abre dez vezes mais rápido.

## ⚙️ Como funciona

O processo de quantização linear afim mapeia valores contínuos reais para inteiros discretos através de uma escala e um ponto zero:

### Etapas

1. **Determinação dos Limites:** Varre-se o tensor de pesos para identificar o valor mínimo ($\alpha$) e o valor máximo ($\beta$) daquela matriz.
2. **Cálculo da Escala ($S$) e Ponto Zero ($Z$):**
   - $S = \frac{\beta - \alpha}{2^b - 1}$ (onde $b$ é o número de bits de destino, ex.: $b=8 \implies 255$ níveis);
   - $Z$ é o inteiro que mapeia o zero real para o espaço quantizado.
3. **Mapeamento e Arredondamento:** Cada peso contínuo $W$ é dividido pela escala, somado a $Z$ e arredondado para o inteiro mais próximo: $W_{\text{quant}} = \text{clip}\left(\text{round}\left(\frac{W}{S}\right) + Z\right)$.
4. **Desquantização na Execução:** Durante a multiplicação matricial, os inteiros podem ser convertidos de volta para ponto flutuante em tempo real para preservar a estabilidade da adição.

### Entradas e saídas

- **Entradas:** Matriz de pesos em alta precisão (FP32/BF16) e hiperparâmetros de grade de quantização.
- **Saídas:** Matriz comprimida de inteiros acompanhada de pequenos vetores escalares de escala e ponto zero.

## 📐 Formulação matemática

A quantização uniforme simétrica de um vetor de pesos contínuos $x \in [\alpha, \beta]$ com $\beta = \max(|x|)$ para um intervalo de inteiros com sinal $b$-bits $[-2^{b-1}, 2^{b-1}-1]$ é definida por:

$$q = \text{clip}\left( \left\lfloor \frac{x}{S} \right\rceil, \; -2^{b-1}, \; 2^{b-1}-1 \right), \quad \text{onde } S = \frac{\max(|x|)}{2^{b-1}-1}$$

A reconstrução aproximada (desquantização) é expressa como:

$$\tilde{x} = q \cdot S$$

O erro de quantização $\|\tilde{x} - x\|$ introduz ruído numérico. No modelo **BitNet b1.58** (Microsoft, 2024), a quantização extrema adota parâmetros ternários restritos $\{-1, 0, 1\}$, operando com apenas $1{,}58$ bits teóricos por peso:

$$W_{i,j} \in \{-1, 0, 1\} \implies \text{Multiplicações são substituídas por adições puras}$$

Eliminando as multiplicações de ponto flutuante nos núcleos de cálculo do silício.

## 🧱 Hipóteses e condições de validade

- A distribuição dos pesos deve ser estatisticamente bem comportada (frequentemente normal com média zero); a presença de valores anômalos extremos (*outliers*) em canais específicos pode distorcer a escala $S$ e destruir a precisão da matriz inteira, exigindo quantização por bloco ou por canal.

## ✅ Quando usar

- **PTQ (Pós-Treino):** Prática padrão e quase universal na disponibilização de modelos abertos para inferência em produção (INT8 e INT4).
- **QAT / Precisão Mista:** Durante o treinamento para reduzir o tempo de execução e a pegada de VRAM em clusters acelerados.
- **Edge Computing:** Implantação de LLMs em dispositivos móveis, navegadores web e hardware com suporte estrito a inteiros.

## 🚫 Quando não usar

- Em tensores ultrassensíveis como os embeddings de entrada, matrizes de posições e camadas finais de cabeça de modelo, que devem ser mantidos em 16 bits para evitar colapso de vocabulário.

## ⚠️ Limitações e armadilhas

- **Degradação de Acurácia em 4 bits puros:** Quantizar modelos pequenos (como 1B ou 3B parâmetros) para 4 bits causa perdas perceptíveis de raciocínio lógico; modelos grandes ($\ge 70\text{B}$) são muito mais tolerantes e resilientes à perda de bits.
- **Sobrecarga de conversão se mal implementada:** Se o hardware não tiver suporte nativo para operações na precisão quantizada, o sistema perderá tempo convertendo inteiros para floats a cada camada, aumentando a latência em vez de reduzi-la.

## 🔍 Comparações

| Modalidade | Quando ocorre? | Custo de Implementação | Impacto na Acurácia |
|---|---|---|---|
| **PTQ (Post-Training)** | Após o término do treinamento | **Mínimo (poucas linhas de código)** | Pequena perda em 8/4 bits |
| **QAT (Quantization-Aware)**| Durante o treinamento | Alto (exige treinar simulando inteiros) | **Preserva a acurácia quase original** |
| **Quantização Extrema (1-bit)**| No design da arquitetura base | Altíssimo (re-treino completo do zero) | Competitivo até certos limites de escala |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma equipe precisa colocar o modelo Llama 3-70B para rodar no servidor local de um hospital.
- O arquivo original em **BF16** consome **140 GB** de espaço em disco e exige duas placas NVIDIA A100 de 80 GB (custo inviável para o setor).
- O engenheiro aplica **PTQ para INT4** através de uma biblioteca de quantização moderna.
- O tamanho do modelo cai para **38 GB**. O modelo passa a rodar confortavelmente em uma única placa comercial mais acessível, respondendo prontuários com perda métrica de acurácia inferior a $1\%$ nos testes clínicos.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/representacoes-numericas-e-precisao.md|Representações Numéricas e Precisão]]
- [[redes/ai-engineering/conceitos/matematica-da-memoria-de-treinamento.md|Matemática da Memória de Treinamento]]

### Complementos

- [[redes/ai-engineering/conceitos/quantized-lora-qlora.md|Quantized LoRA (QLoRA)]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Alternativas

- Manutenção de modelos em precisão original sem compressão (*Full Precision FP32/BF16*).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|Ajuste Fino Eficiente em Parâmetros (PEFT)]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 328–332
- **Evidência:** Chip Huyen formaliza as técnicas de quantização na inferência e no treino, analisa o esquema de quantização mista da Apple com média de 3,5 bits por peso para dispositivos locais, detalha os resultados empíricos do BitNet b1.58 (Tabela 7-4) e explica a distinção prática entre PTQ e QAT.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é quantização no contexto da Engenharia de IA e qual o seu benefício operacional primário?
2. Qual é a diferença fundamental entre Quantização Pós-Treinamento (PTQ) e Treinamento Ciente de Quantização (QAT)?
3. Como a escala ($S$) e o ponto zero ($Z$) operam matematicamente no mapeamento de números contínuos para inteiros discretos?
4. Por que modelos de grande escala (como 70B parâmetros) são mais tolerantes à quantização agressiva de 4 bits do que modelos compactos (como 1B ou 3B)?
5. O que é a arquitetura BitNet b1.58 da Microsoft e como ela elimina a necessidade de multiplicações matriciais tradicionais?
6. Quais componentes de uma rede neural profunda geralmente são preservados em 16 bits para evitar o colapso de precisão durante a quantização mista?
7. Em quais circunstâncias uma quantização mal projetada pode resultar em aumento de latência em vez de aceleração de resposta?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Ajuste Fino Eficiente em Parâmetros (PEFT)

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 332–338

## 📝 Definição

### Definição formal

O **Ajuste Fino Eficiente em Parâmetros** (*Parameter-Efficient Finetuning* — PEFT) é o paradigma de aprendizado por transferência em que um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] pré-treinado tem a vasta maioria de seus parâmetros originais congelados (*frozen*), enquanto o processo de otimização por gradiente descendente é restrito à atualização de um número residual e minúsculo de parâmetros treináveis (tipicamente entre $0{,}01\%$ e $3\%$ do total de pesos), alcançando desempenho empírico comparável ao do ajuste fino completo (*Full Finetuning*) com uma fração mínima dos requisitos de memória VRAM e computação. 

As técnicas de PEFT dividem-se em duas macro-categorias estruturais:
1. **Métodos Aditivos / Baseados em Adaptadores (*Adapter-based*):** Injetam novos módulos ou camadas parametrizadas compactas dentro ou ao lado dos blocos do modelo (como Houlsby Adapters, [[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA]] e $(IA)^3$);
2. **Métodos de Prompts Suaves (*Soft Prompt-based*):** Introduzem vetores contínuos treináveis adicionais prepensados ao fluxo de ativação dos tokens sem alterar matrizes de peso internas (como *Prompt Tuning*, *Prefix-Tuning* e *P-Tuning*).

### Em linguagem simples

É o método que tornou viável para pessoas comuns e pequenas empresas ajustarem IAs gigantescas. Em vez de tentar recalibrar todos os 70 bilhões de parâmetros de uma rede (o que exige supercomputadores caríssimos), você "trava" o cérebro original da IA e mexe em menos de 1% de parâmetros extras colocados estrategicamente. A IA aprende a nova tarefa perfeitamente, mas você gasta centenas de vezes menos memória e consegue treinar tudo em uma única placa de vídeo.

### Escopo e distinções

Diferencia-se do **ajuste fino parcial ingênuo** (congelar as 9 primeiras camadas e treinar apenas a última), que a literatura comprovou ser ineficiente (exigiria treinar cerca de 25% dos pesos para atingir resultados aceitáveis). O PEFT insere flexibilidade estrutural coordenada ao longo de toda a profundidade da rede neural.

## 🧩 Problema que resolve

Resolve a inacessibilidade financeira e física do *Full Finetuning*. Atualizar todos os pesos de modelos modernos exige manter na memória gigabytes massivos de gradientes e estados do otimizador Adam, exigindo clusters com múltiplas placas de vídeo de 80 GB. O PEFT reduz os parâmetros treináveis de bilhões para poucos milhões, colapsando a demanda de VRAM de otimizadores para valores desprezíveis.

## 💡 Intuição

Pense em um livro de receitas de 1.000 páginas escrito por um chef consagrado:
- No **Full Finetuning**, para adaptar o livro para a culinária brasileira, você reescreveria as 1.000 páginas do livro palavra por palavra em uma nova gráfica. O custo de impressão é absurdo.
- No **PEFT**, você mantém o livro original intacto e fechado na estante (**pesos congelados**). Você simplesmente anexa ao final de cada capítulo uma tira adesiva de post-it com notas de 3 linhas dizendo: *"Substitua a manteiga por azeite de dendê"* (**adaptadores**). O livro continua o mesmo, a adaptação foi perfeita e você gastou apenas alguns centavos de papel.

## ⚙️ Como funciona

O ecossistema de PEFT atua modificando a rota de ativação das camadas neurais:

### Etapas

1. **Congelamento Estrutural:** O algoritmo percorre todos os parâmetros originais $\theta_{\text{base}}$ do modelo de fundação e desativa o cálculo de gradientes (`requires_grad = False`).
2. **Injeção de Parâmetros Treináveis:**
   - *Se método de adaptador:* Insere pequenas matrizes auxiliares compactas em posições selecionadas (ex.: camadas de atenção ou MLPs);
   - *Se método de soft prompt:* Adiciona uma sequência de vetores contínuos virtuais no início dos tokens de entrada ou em cada camada.
3. **Passagem Direta (*Forward Pass*):** A entrada passa pelas camadas originais congeladas e pelos novos parâmetros injetados.
4. **Retropropagação Restrita:** O cálculo do gradiente descendente calcula erros e atualiza os estados do otimizador **apenas e exclusivamente para os parâmetros adicionados**.
5. **Geração de Artefato Modular:** Ao final do treino, o sistema salva em disco apenas o arquivo minúsculo contendo os parâmetros treinados (frequentemente entre 10 MB e 100 MB), que pode ser acoplado dinamicamente ao modelo base em tempo de inferência.

### Entradas e saídas

- **Entradas:** Modelo de fundação base congelado e dataset de instrução supervisionado.
- **Saídas:** Arquivo leve de adaptador/prompt suave que parametriza a nova especialidade.

## 📐 Formulação matemática

No ajuste fino supervisionado tradicional, otimizam-se todos os parâmetros $\Theta$:

$$\min_\Theta \sum_{(x, y) \in \mathcal{D}} \mathcal{L}\big(f_\Theta(x), y\big)$$

No **PEFT**, particiona-se o espaço de parâmetros em $\Theta = \{\theta_{\text{congelado}}, \; \phi_{\text{treinável}}\}$, onde $|\phi_{\text{treinável}}| \ll |\theta_{\text{congelado}}|$:

$$\min_{\phi} \sum_{(x, y) \in \mathcal{D}} \mathcal{L}\Big(f_{\theta_{\text{congelado}}, \, \phi}(x), y\Big)$$

O artigo pioneiro de Houlsby et al. (2019) no benchmark GLUE demonstrou que treinando apenas **$3{,}6\%$ de parâmetros adicionais** via adaptadores, o modelo atingiu desempenho a apenas **$0{,}4\%$** de distância do ajuste completo de 100% dos parâmetros.

## 🧱 Hipóteses e condições de validade

- Fundamenta-se na descoberta empírica e teórica de que grandes modelos de fundação pré-treinados possuem **baixa dimensão intrínseca** (*low intrinsic dimension*): as soluções ótimas para tarefas a jusante residem em um subespaço linear de dimensão ordens de magnitude menor do que o número nominal de parâmetros da rede.

## ✅ Quando usar

- Quase sempre: é a abordagem padrão de largada recomendada para qualquer projeto corporativo de ajuste fino.
- Cenários onde uma única empresa precisa oferecer modelos customizados para dezenas ou centenas de clientes diferentes a partir de um mesmo modelo base compartilhado.
- Ambientes com restrições severas de hardware (treinamento em GPUs individuais de 16 GB ou 24 GB).

## 🚫 Quando não usar

- Em pré-treinamento contínuo massivo (*continued pre-training*) com trilhões de tokens para ensinar uma nova língua inteira do zero a um modelo que nunca a viu.

## ⚠️ Limitações e armadilhas

- **Sobrecarga de latência dos adaptadores originais:** A proposta inicial de Houlsby inseria novas camadas sequenciais que aumentavam o tempo de inferência em até 20%. Essa limitação foi superada pelo design do [[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA]].
- **Soft Prompts difíceis de interpretar:** Métodos baseados em *prompt tuning* puro (vetores contínuos virtuais) são caixas-pretas numéricas que não podem ser lidas nem editadas por humanos como prompts de texto tradicionais.

## 🔍 Comparações

| Família PEFT | Onde atua? | Mecanismo | Impacto na Latência de Inferência |
|---|---|---|---|
| **Adaptadores Clássicos (Houlsby)** | Entre camadas do Transformer | Novas camadas lineares pequenas | Adiciona latência (passos extras no forward) |
| **LoRA / Aditivos Modernos** | Em paralelo às matrizes de peso | Decomposição de baixo posto ($A \times B$) | **Zero latência extra (pesos podem ser fundidos)** |
| **Soft Prompts (Prefix-Tuning)** | No fluxo de ativação dos tokens | Vetores virtuais contínuos treináveis | Reduz discretamente a janela útil de contexto |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma empresa de software de RH quer treinar um assistente para responder dúvidas sobre a CLT brasileira.
- Se utilizasse **Full Finetuning** sobre o Llama 3-70B, ela precisaria alugar um cluster com 8 placas H100 custando dezenas de milhares de dólares por semana.
- A equipe opta por **PEFT (LoRA)**. Eles congelam os 70 bilhões de parâmetros e treinam apenas 50 milhões de parâmetros adicionais ($0{,}07\%$). O treinamento roda confortavelmente em uma única máquina com duas placas menores e termina em uma tarde, atingindo pontuação idêntica em testes práticos de legislação trabalhista.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/matematica-da-memoria-de-treinamento.md|Matemática da Memória de Treinamento]]

### Complementos

- [[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA (Low-Rank Adaptation)]]
- [[redes/ai-engineering/conceitos/quantized-lora-qlora.md|Quantized LoRA (QLoRA)]]
- [[redes/ai-engineering/conceitos/fusao-de-modelos-model-merging.md|Fusão de Modelos (Model Merging)]]

### Alternativas

- Ajuste Fino Completo (*Full Finetuning*).
- Ajuste Fino Parcial Ingênuo de Camadas Finais.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]
- [[redes/ai-engineering/conceitos/representacoes-numericas-e-precisao.md|Representações Numéricas e Precisão]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 332–338
- **Evidência:** Chip Huyen introduz o conceito de PEFT citando o artigo seminal de Houlsby et al. (2019) no benchmark GLUE, apresenta o gráfico de desempenho (Figura 7-7) contra o ajuste parcial de camadas, detalha a taxonomia de adaptadores e soft prompts (P-tuning, Prefix-tuning) e analisa dados do repositório huggingface/peft comprovando a dominância absoluta de LoRA no mercado.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é o paradigma de Ajuste Fino Eficiente em Parâmetros (PEFT) e qual problema de infraestrutura ele resolve?
2. Por que o ajuste parcial ingênuo de congelar as primeiras camadas e treinar apenas as últimas é considerado ineficiente?
3. Quais são as duas macro-categorias estruturais nas quais os métodos de PEFT se dividem?
4. O que é a hipótese da baixa dimensão intrínseca (*low intrinsic dimension*) e como ela fundamenta teoricamente a eficácia do PEFT?
5. Qual era a principal limitação dos adaptadores pioneiros de Houlsby et al. (2019) em relação à velocidade de inferência?
6. O que são *Soft Prompts* (como no Prefix-Tuning) e em que eles se diferenciam dos prompts em linguagem natural tradicional?
7. Como a natureza modular dos artefatos de PEFT viabiliza o atendimento simultâneo de múltiplos clientes especializados sobre um mesmo modelo base?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 LoRA (Low-Rank Adaptation)

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 338–345

## 📝 Definição

### Definição formal

O **LoRA** (*Low-Rank Adaptation*, Hu et al., 2021) é um método de ajuste fino eficiente em parâmetros ([[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|PEFT]]) no qual a matriz de pesos congelada pré-existente $W_0 \in \mathbb{R}^{d \times k}$ de uma camada neural é mantida inalterada, enquanto sua atualização de peso cumulativa $\Delta W$ é parametrizada através de uma decomposição de posto baixo (*low-rank factorization*) composta pelo produto de duas matrizes treináveis compactas $B \in \mathbb{R}^{d \times r}$ e $A \in \mathbb{R}^{r \times k}$, onde o posto $r \ll \min(d, k)$, viabilizando um treinamento com consumo diminuto de memória de otimizador e **sem introduzir nenhuma latência adicional na inferência**, uma vez que os pesos fatorados podem ser fundidos analiticamente de volta à matriz original.

### Em linguagem simples

É a técnica mais popular e inteligente de ajustar modelos de IA no mundo hoje. Em vez de mexer em uma tabela gigante de números com milhões de casas, o LoRA fatia a correção dessa tabela em duas tabelinhas finas e compridas. Multiplicar essas duas tabelinhas finas dá o mesmo resultado prático da tabela gigante, mas você gasta mil vezes menos memória para treinar. E quando o treino acaba, você simplesmente soma essas tabelinhas na tabela principal, garantindo que o modelo rode na velocidade normal sem ficar lento.

### Escopo e distinções

Distingue-se dos adaptadores anteriores de Houlsby porque o LoRA opera em **paralelo** à camada original e não em série sequencial. Na inferência, as matrizes $A$ e $B$ podem ser somadas fisicamente em $W_0$, eliminando a sobrecarga de tempo de execução.

## 🧩 Problema que resolve

Resolve o dilema entre eficiência de treinamento e velocidade de atendimento em produção. Permite ajustar modelos gigantescos (como GPT-3 ou Llama) reduzindo em até 3 vezes os requisitos de VRAM de otimizador e gerando arquivos leves de adaptadores (dezenas de megabytes) que tornam o armazenamento e a troca de modelos em servidores algo trivial.

## 💡 Intuição

Pense em retocar uma pintura a óleo famosa em um museu:
- O **Full Finetuning** rasparia a tela inteira e pintaria uma nova tela do zero.
- O **LoRA** coloca uma lâmina de vidro transparente perfeitamente alinhada sobre a pintura original (**matriz $W_0$ congelada**). O artista faz pequenos traços finos com pincel apenas sobre o vidro (**matrizes de baixo posto $A$ e $B$**). A luz que passa pelo vidro e atinge a tela soma os dois efeitos visualmente. Se você quiser expor o quadro em definitivo, basta colar o vidro na tela (**fusão de pesos**), sem alterar a espessura da moldura.

## ⚙️ Como funciona

A mecânica baseia-se em álgebra linear e projeção dimensional intermediária:

### Etapas

1. **Fixação da Matriz Base:** Seleciona-se uma matriz de pesos da atenção (tipicamente $W_q, W_v$ ou todas as matrizes incluindo MLPs) e congela-se seus valores.
2. **Criação das Matrizes Fatoradas:** Cria-se a matriz $A$ com dimensão $r \times k$ (inicializada com distribuição gaussiana aleatória) e a matriz $B$ com dimensão $d \times r$ (inicializada estritamente com zeros, garantindo que $\Delta W = B \cdot A = 0$ no início exato do treino).
3. **Definição do Posto ($r$):** Escolhe-se a dimensão intermediária $r$ (valores típicos entre 4 e 64).
4. **Passagem Direta:** A ativação de entrada $x$ é multiplicada em paralelo por $W_0$ e pelo ramo LoRA escalonado por $\frac{\alpha}{r}$:
   $$h = W_0 x + \frac{\alpha}{r} B A x$$
5. **Atualização por Retropropagação:** Apenas os parâmetros de $A$ e $B$ recebem gradientes e têm seus estados atualizados pelo otimizador Adam.
6. **Modos de Implantação (Serving):**
   - *Modo Fundido (Merged):* Soma-se $W_{\text{novo}} = W_0 + \frac{\alpha}{r}BA$ antes de ligar o servidor $\to$ latência idêntica à do modelo base original;
   - *Modo Multi-LoRA (Separado):* Mantém-se $W_0$ compartilhado na VRAM e comuta-se dinamicamente entre múltiplos pares $(A, B)$ conforme o cliente que dispara a requisição.

### Entradas e saídas

- **Entradas:** Matriz original congelada de dimensão $d \times k$, posto $r$ e fator de escala $\alpha$.
- **Saídas:** Pares treinados de matrizes compactas $A$ e $B$ contendo o delta de aprendizado especializado.

## 📐 Formulação matemática

Para uma camada linear que computa $h = W_0 x$, com $W_0 \in \mathbb{R}^{d \times k}$ e $x \in \mathbb{R}^k$, o LoRA introduz:

$$h = W_0 x + \Delta W x = W_0 x + \frac{\alpha}{r} B A x$$

Onde:
- $A \in \mathbb{R}^{r \times k}$, $B \in \mathbb{R}^{d \times r}$ com posto $r \ll \min(d, k)$;
- $\alpha$ é uma constante hiperparamétrica de escala que estabiliza o aprendizado ao alterar o valor de $r$.
No exemplo do GPT-3 de 175B ($d = 12.288$):
- A matriz de atenção $W_0$ possui $12.288 \times 12.288 \approx 151 \text{ milhões}$ de parâmetros;
- O adaptador LoRA com $r=2$ possui $(12.288 \times 2) + (2 \times 12.288) = 49.152$ parâmetros por matriz, uma redução de mais de **$3.000$ vezes** no número de parâmetros treináveis por camada.

## 🧱 Hipóteses e condições de validade

- A tarefa adaptada deve ser compatível com a baixa dimensão intrínseca do modelo pré-treinado; pesquisas empíricas revelam que aumentar o posto $r$ além de certos valores (ex.: $r > 64$) raramente traz ganhos adicionais de qualidade e pode induzir sobreajuste (*overfitting*).

## ✅ Quando usar

- Ajuste de modelos de linguagem para tarefas de domínio, estilo de marca, seguimento de instruções sintáticas e copilotos de programação.
- Plataformas SaaS multi-inquilino (*multi-tenant*) que precisam servir modelos personalizados para milhares de empresas compartilhando a mesma GPU base via *Multi-LoRA serving*.

## 🚫 Quando não usar

- Em casos onde o modelo precisa passar por alterações conceituais tão radicais e colossais que o subespaço de posto baixo torna-se insuficiente para absorver os novos conhecimentos (onde o *Full Finetuning* volta a ser necessário).

## ⚠️ Limitações e armadilhas

- **Complexidade de seleção de matrizes alvo:** Aplicar LoRA apenas em $W_q$ e $W_v$ consome menos memória, mas pesquisas recentes (Databricks, 2023) comprovam que aplicar LoRA em todas as matrizes lineares (incluindo camadas feedforward/MLP) entrega qualidade substancialmente superior.
- **Calibração de $\alpha$ e $r$:** Desbalancear a razão $\frac{\alpha}{r}$ pode desestabilizar a magnitude das atualizações nos primeiros passos de treinamento.

## 🔍 Comparações

| Dimensão | Full Finetuning | LoRA Fundido (*Merged*) | Multi-LoRA (Separado) |
|---|---|---|---|
| **Latência de Inferência** | Linha de base original | **Linha de base original (0% overhead)** | Ligeiramente maior (overhead de fusão dinâmica) |
| **Armazenamento de 100 modelos**| $100 \times 14 \text{ GB} = 1{,}4 \text{ TB}$ | $100 \times 14 \text{ GB} = 1{,}4 \text{ TB}$ | **$14 \text{ GB} + (100 \times 30 \text{ MB}) \approx 17 \text{ GB}$** |
| **Memória VRAM no Treino** | Altíssima ($> 56$ GB para 7B) | Baixa ($< 18$ GB para 7B) | Baixa ($< 18$ GB para 7B) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

A Apple precisa implantar assistentes de IA personalizados nos iPhones para 5 funções diferentes: resumir e-mails, transcrever mensagens de voz, sugerir respostas no chat, formatar notas e criar emojis.
- Se usasse **Full Finetuning**, o iPhone precisaria guardar 5 modelos completos de 3 bilhões de parâmetros, estourando toda a memória do aparelho ($5 \times 6 \text{ GB} = 30 \text{ GB}$).
- A Apple mantém **apenas 1 modelo base compacto de 3B congelado** na memória e carrega 5 adaptadores LoRA minúsculos de 20 MB cada. Quando o usuário abre o e-mail, o sistema aciona o adaptador LoRA de e-mails em milissegundos; quando abre o chat, comuta para o adaptador de mensagens, viabilizando inteligência multifacetada on-device.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|Ajuste Fino Eficiente em Parâmetros (PEFT)]]
- [[redes/ai-engineering/conceitos/matematica-da-memoria-de-treinamento.md|Matemática da Memória de Treinamento]]

### Complementos

- [[redes/ai-engineering/conceitos/quantized-lora-qlora.md|Quantized LoRA (QLoRA)]]
- [[redes/ai-engineering/conceitos/fusao-de-modelos-model-merging.md|Fusão de Modelos (Model Merging)]]

### Alternativas

- Métodos baseados em prompts suaves (*Prefix-Tuning*, *P-Tuning*).
- Ajuste Fino Completo (*Full Finetuning*).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/mecanismo-de-atencao.md|Mecanismo de Atenção]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 338–345
- **Evidência:** Chip Huyen detalha a formulação matricial de Hu et al. (2021), analisa os experimentos com GPT-3 demonstrando acurácia competitiva com apenas 0,0027% de parâmetros treináveis, detalha a Tabela 7-5 com testes nos benchmarks WikiSQL e MultiNLI, e explica a arquitetura de Multi-LoRA serving demonstrando a redução de armazenamento de 1,68B para 23,3M parâmetros.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é o método LoRA e como a fatoração de posto baixo ($B \cdot A$) atua sobre a matriz de pesos de uma camada?
2. Por que a matriz $B$ é inicializada estritamente com zeros e a matriz $A$ com distribuição gaussiana aleatória no início do treino?
3. O que representam os hiperparâmetros de posto ($r$) e escala ($\alpha$) na formulação matemática do LoRA?
4. Por que o LoRA não introduz nenhuma sobretaxa de latência de inferência quando implantado no modo fundido (*merged*)?
5. Como a técnica de *Multi-LoRA serving* viabiliza servir dezenas de modelos especializados compartilhando uma única GPU?
6. Qual foi o resultado empírico obtido pelos autores do LoRA ao comparar a adaptação de apenas matrizes de atenção ($W_q, W_v$) contra todas as matrizes lineares?
7. Por que aumentar indefinidamente o posto $r$ (ex.: $r=256$) geralmente não se traduz em ganhos de performance na aplicação final?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Quantized LoRA (QLoRA)

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 345–347

## 📝 Definição

### Definição formal

O **QLoRA** (*Quantized Low-Rank Adaptation*, Dettmers et al., 2023) é uma técnica avançada de ajuste fino eficiente em parâmetros que combina quantização de alta densidade com adaptadores de posto baixo ([[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA]]), alicerçada em três inovações algorítmicas de engenharia:
1. **Formato de Dados NormalFloat-4 (NF4):** Uma representação de 4 bits teoricamente ótima em termos de informação para parâmetros neurais que seguem distribuição normal com média zero;
2. **Dupla Quantização (*Double Quantization*):** A quantização das próprias constantes de escala de quantização da primeira etapa, reduzindo a sobrecarga residual de memória de 0,5 bit para 0,127 bit por parâmetro;
3. **Otimizadores Paginados (*Paged Optimizers*):** O gerenciamento automático de paginação de memória que descarrega estados do otimizador da VRAM da GPU para a memória RAM da CPU durante picos de ativação de sequências longas, prevenindo falhas de *Out of Memory*.

### Em linguagem simples

É a tecnologia que permitiu treinar um modelo monstruoso de 65 bilhões de parâmetros dentro de uma única placa de vídeo profissional de 48 GB (algo que antes exigia um servidor com 8 placas caríssimas). O QLoRA espreme os pesos congelados do modelo para apenas 4 bits na memória, mas no milissegundo em que precisa fazer as contas de matemática, ele descompacta temporariamente os números para 16 bits para não perder a precisão dos cálculos.

### Escopo e distinções

Distingue-se do LoRA tradicional porque no LoRA padrão os pesos congelados do modelo base permanecem em 16 bits (FP16 ou BF16). No QLoRA, os pesos base são armazenados em 4 bits estritos (NF4), enquanto apenas os adaptadores LoRA são mantidos e atualizados em 16 bits.

## 🧩 Problema que resolve

Resolve a barreira física de VRAM que impedia desenvolvedores, laboratórios acadêmicos e startups de realizarem ajuste fino em modelos de grande porte ($\ge 65\text{B}$ parâmetros). Com o LoRA comum, um modelo de 65B exige mais de 130 GB de VRAM apenas para carregar os pesos congelados; com o QLoRA, a exigência despenca para cerca de 41 GB, viabilizando o treino em uma única GPU.

## 💡 Intuição

Pense em um arquivo morto de documentos jurídicos de uma grande corporação:
- Se você mantiver todos os 10.000 livros de processos físicos abertos sobre as mesas da biblioteca (**LoRA em 16 bits**), você precisará alugar um galpão imenso apenas para sustentar o peso do papel.
- No **QLoRA**, todos os livros antigos são microfilmados e guardados em cartuchos de filme compactos em uma gaveta de 4 bits (**pesos em NF4**). O pesquisador tem uma pequena mesa de leitura de 16 bits (**os adaptadores LoRA**). Quando ele precisa consultar uma página específica do processo antigo, ele coloca o microfilme no projetor, lê a frase em tamanho real, anota sua conclusão no caderno de 16 bits e guarda o filme de volta na gaveta.

## ⚙️ Como funciona

O pipeline intercala compactação estática de memória com descompressão dinâmica em tempo de execução:

### Etapas

1. **Quantização NF4 dos Pesos Base:** Os pesos originais do modelo de fundação são quantizados para o formato NormalFloat de 4 bits e alocados na VRAM da GPU.
2. **Dupla Quantização:** Os fatores de escala derivados do NF4 são novamente quantizados para 8 bits, economizando centenas de megabytes adicionais.
3. **Acoplamento dos Adaptadores LoRA:** Anexam-se as matrizes de baixo posto $A$ e $B$ em formato de alta precisão (BF16 de 16 bits).
4. **Desquantização Just-in-Time no Forward Pass:** Durante a passagem direta, no instante exato em que a camada vai multiplicar o tensor pelo peso em 4 bits, o kernel computacional desquantiza dinamicamente o bloco de NF4 para BF16, executa a multiplicação matricial em 16 bits e descarta o tensor de 16 bits da memória imediatamente após a operação.
5. **Retropropagação e Otimizador Paginado:** Os gradientes são calculados apenas para os adaptadores LoRA em 16 bits; caso a VRAM atinja o limite físico em prompts longos, o driver de paginação transfere blocos do otimizador Adam para a memória RAM da CPU via barramento PCIe sem abortar o treinamento.

### Entradas e saídas

- **Entradas:** Modelo de fundação de grande escala e dados de instrução supervisionados.
- **Saídas:** Adaptadores LoRA treinados a partir de uma base quantizada em 4 bits.

## 📐 Formulação matemática

O tipo de dados **NormalFloat (NF4)** baseia-se na quantização de quantis de informação teórica ótima para distribuições gaussianas padronizadas $X \sim \mathcal{N}(0, 1)$. 
Os $2^k = 16$ pontos discretos de quantização $q_i$ ($i \in \{0, \dots, 15\}$) são distribuídos de modo que a integral da densidade de probabilidade entre quantis adjacentes seja constante:

$$q_i = \frac{1}{2} \left( Q_X\left(\frac{i}{2^k}\right) + Q_X\left(\frac{i+1}{2^k}\right) \right)$$

Onde $Q_X(\cdot)$ é a função de quantil (inversa da função de distribuição cumulativa) da distribuição normal padrão.
Durante a passagem direta, a operação computada pelo kernel em tempo de execução é:

$$Y^{\text{BF16}} = X^{\text{BF16}} \cdot \text{dequant}\Big(c_1^{\text{FP32}}, \; c_2^{\text{FP8}}, \; W^{\text{NF4}}\Big) + \frac{\alpha}{r} X^{\text{BF16}} A^{\text{BF16}} B^{\text{BF16}}$$

Onde $c_1$ e $c_2$ são as constantes derivadas da dupla quantização.

## 🧱 Hipóteses e condições de validade

- Exige compiladores e kernels especializados em CUDA (como a biblioteca *bitsandbytes*) configurados para executar a desquantização rápida sob demanda na GPU.

## ✅ Quando usar

- Ajuste fino de modelos maciços (33B, 65B, 70B parâmetros) quando a infraestrutura disponível é limitada a uma única GPU profissional de 48 GB ou GPUs de 80 GB individuais.
- Democratização de pesquisa e testes rápidos de modelos de ponta com restrições severas de orçamento em nuvem.

## 🚫 Quando não usar

- Em cenários onde o gargalo primário absoluto do projeto é o **tempo de relógio de treinamento** e há abundância de GPUs de alta performance: a etapa contínua de quantização e desquantização em tempo de execução introduz uma penalidade temporal que torna o QLoRA tipicamente entre $20\%$ e $40\%$ mais lento por época do que o LoRA padrão em 16 bits.

## ⚠️ Limitações e armadilhas

- **Sobretaxa de Tempo de Computação:** A economia drástica de memória VRAM é paga com aumento no tempo de treinamento devido ao processamento repetido de conversão de tipos de dados.
- **Fusão de Pesos Complexa:** Para fundir os pesos finais do LoRA de volta ao modelo original, é necessário desquantizar a base inteira para 16 bits antes da soma algébrica, gerando um modelo final de tamanho padrão em disco.

## 🔍 Comparações

| Característica | LoRA Convencional | QLoRA |
|---|---|---|
| **Precisão dos Pesos Base** | 16 bits (FP16 / BF16) | **4 bits (NF4)** |
| **Precisão dos Adaptadores**| 16 bits (FP16 / BF16) | 16 bits (BF16) |
| **VRAM para Modelo de 65B** | $> 130 \text{ GB}$ (exige múltiplas GPUs) | **$\approx 41 \text{ GB}$ (uma única GPU de 48 GB)** |
| **Velocidade por Época** | Mais rápida | Mais lenta (overhead de desquantização) |
| **Desempenho Final** | Linha de base competitiva | Praticamente indistinguível do LoRA de 16 bits |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O laboratório de pesquisa da Universidade de Washington introduziu a família de modelos **Guanaco** através do QLoRA:
Eles pegaram o modelo bruto Llama 1 de 65 bilhões de parâmetros. 
- Com o Full Finetuning ou LoRA convencional, eles precisariam de um cluster com pelo menos 8 a 16 placas A100 interconectadas, consumindo milhares de dólares de orçamento acadêmico.
- Aplicando **QLoRA em 4 bits NF4 com otimizadores paginados**, eles executaram o treinamento do Guanaco de 65B em uma única GPU NVIDIA RTX de 48 GB em apenas 24 horas. O modelo resultante atingiu pontuação de $99{,}3\%$ no benchmark Vicuna e competiu de igual para igual com o ChatGPT comercial na avaliação de juízes de IA.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA (Low-Rank Adaptation)]]
- [[redes/ai-engineering/conceitos/quantizacao.md|Quantização]]
- [[redes/ai-engineering/conceitos/representacoes-numericas-e-precisao.md|Representações Numéricas e Precisão]]

### Complementos

- [[redes/ai-engineering/conceitos/matematica-da-memoria-de-treinamento.md|Matemática da Memória de Treinamento]]

### Alternativas

- LoRA tradicional em meia precisão (16 bits).
- Métodos concorrentes de quantização e ajuste como QA-LoRA e IR-QLoRA.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/hiperparametros-de-ajuste-fino.md|Hiperparâmetros de Ajuste Fino]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 345–347
- **Evidência:** Chip Huyen destrincha a publicação de Dettmers et al. (2023) sobre QLoRA, detalha as inovações de NF4 e paged optimizers, e apresenta a Tabela 7-7 com os escores Elo dos modelos Guanaco de 7B a 65B avaliados pelo GPT-4 em comparação direta com ChatGPT e Bard.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é QLoRA e quais são as três inovações algorítmicas fundamentais introduzidas por Dettmers et al. (2023)?
2. Como funciona o tipo de dados NormalFloat-4 (NF4) e por que ele é teoricamente ótimo para pesos de redes neurais?
3. O que é a técnica de Dupla Quantização (*Double Quantization*) e qual economia marginal de memória ela proporciona?
4. Qual é a função dos Otimizadores Paginados (*Paged Optimizers*) no gerenciamento de picos de memória VRAM?
5. Qual é o compromisso de engenharia (*trade-off*) essencial entre economia de memória e tempo de processamento ao escolher entre LoRA e QLoRA?
6. Como o procedimento de desquantização *Just-in-Time* opera na GPU durante a passagem direta de um modelo QLoRA?
7. Como a família de modelos Guanaco exemplificou empiricamente o poder de democratização do QLoRA em modelos de 65B parâmetros?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Fusão de Modelos (Model Merging)

**Rede:** `ai-engineering`  
**Área:** `modelagem`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 347–357

## 📝 Definição

### Definição formal

A **Fusão de Modelos** (*Model Merging*) é o conjunto de técnicas algébricas, geométricas e estruturais pelas quais dois ou mais [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]] previamente treinados ou ajustados (frequentemente compartilhando o mesmo modelo base inicial) têm seus pesos matemáticos combinados diretamente no espaço de parâmetros, sintetizando um novo modelo consolidado que unifica as competências multidisciplinares de seus constituintes **sem exigir dados de treinamento adicionais e sem despender computação de GPUs para retropropagação**. 

As abordagens canônicas estruturam-se em três modalidades:
1. **Soma e Interpolação:** Média linear ponderada de pesos (*Model Soups*), Interpolação Linear Esférica (**SLERP**) e aritmética de vetores de tarefa (*task vectors*);
2. **Poda e Resolução de Interferência:** Técnicas como **TIES-Merging** e **DARE**, que eliminam parâmetros redundantes ou conflitantes de tarefas antes da soma;
3. **Empilhamento de Camadas (*Layer Stacking / Frankenmerging*):** Concatenação vertical de blocos de camadas de modelos diferentes para expandir a profundidade ou gerar modelos esparsos (*MoE upcycling*), como no caso do SOLAR 10.7B.

### Em linguagem simples

É a técnica de "misturar o cérebro" de dois ou mais modelos em um só usando apenas fórmulas matemáticas simples, sem gastar nem um centavo com novo treinamento de placas de vídeo. Se você tem um modelo excelente em programação e outro modelo excelente em medicina, você pode fundir os arquivos de peso dos dois no seu computador comum para criar um modelo único que entende tanto de código quanto de medicina, sem que um conhecimento apague o outro.

### Escopo e distinções

Diferencia-se do **ensemble clássico de modelos**. No ensemble, todos os modelos originais precisam ser mantidos na memória e rodar em paralelo a cada pergunta do usuário (multiplicando o custo de inferência). Na fusão de modelos, os parâmetros são fundidos em um **único arquivo de modelo**, mantendo a velocidade e a latência de inferência originais.

## 🧩 Problema que resolve

Resolve o dilema do **Esquecimento Catastrófico** no treinamento multitarefa. Treinar um modelo sequencialmente em tarefas diferentes (aprender Tarefa A e depois aprender Tarefa B) faz a rede esquecer a Tarefa A. Treinar todas as tarefas simultaneamente exige um conjunto unificado massivo de dados e computação proibitiva. A fusão de modelos permite treinar especialistas em paralelo e combiná-los algebricamente a custo computacional quase zero.

## 💡 Intuição

Pense na pintura com tintas a óleo:
- O **Ensemble** é contratar dois pintores para pintar dois quadros separados e depois pendurar os dois lado a lado na parede da sala. Ocupa o dobro de espaço e custa o dobro.
- O **Treinamento Sequencial** é pintar uma paisagem linda em uma tela e depois pintar um retrato por cima da mesma tela; as tintas novas cobrem e apagam a paisagem original (**esquecimento catastrófico**).
- O **Model Merging (SLERP/TIES)** é misturar cuidadosamente as gotas exatas de tinta de dois potes coloridos em uma paleta antes de tocar na tela, gerando uma nova cor rica e harmoniosa que carrega a essência dos dois pigmentos originais.

## ⚙️ Como funciona

O procedimento opera manipulando tensores de peso fora do ambiente de treino:

### Etapas

1. **Extração dos Vetores de Tarefa (*Task Vectors*):**
   - Dado um modelo base $\theta_{\text{base}}$ e um modelo ajustado na tarefa A ($\theta_A$), o vetor de tarefa é a diferença aritmética simples: $\tau_A = \theta_A - \theta_{\text{base}}$.
   - Esse vetor isola matematicamente o "conhecimento adquirido" naquela especialidade.
2. **Poda e Eletividade de Sinal (TIES / DARE):**
   - Descarta-se até $80\%$ a $90\%$ das menores alterações do vetor de tarefa (parâmetros redundantes que pouco contribuem para a especialidade);
   - Resolve-se conflitos de sinal onde a Tarefa A puxa um peso para positivo e a Tarefa B puxa para negativo.
3. **Aplicação da Fusão Geométrica:**
   - *Combinação Linear:* Soma ponderada clássica $\theta_{\text{merged}} = \theta_{\text{base}} + \lambda_A \tau_A + \lambda_B \tau_B$;
   - *SLERP:* Trata os tensores como vetores multidimensionais e interpola os pesos ao longo do arco esférico superficial, preservando a magnitude geométrica dos pesos que a média linear simples tende a achatar.
4. **Empilhamento e Expansão (*Layer Stacking*):**
   - Seleciona-se blocos de camadas de modelos precursores (ex.: pegar 72 de 80 camadas de dois modelos Llama-70B distintos) e monta-se uma rede mais profunda (como o modelo comunitário Goliath-120B).
5. **Gravação do Modelo Final:** O novo checkpoint consolidado é gravado em disco pronto para inferência ou para um breve pós-treinamento de alinhamento.

### Entradas e saídas

- **Entradas:** Dois ou mais checkpoints de modelos (pesos completos ou adaptadores LoRA).
- **Saídas:** Um único modelo consolidado com capacidades agregadas.

## 📐 Formulação matemática

O vetor de tarefa para a tarefa $m$ deriva de:

$$\tau_m = \theta_m - \theta_{\text{base}}$$

A fusão **TIES-Merging** (Yadav et al., 2023) atua em três passos operacionais:
1. **Trim (Podar):** Mantém apenas os $k\%$ maiores valores absolutos de $\tau_m$ e zera os demais via máscara booleana $M_m$: $\hat{\tau}_m = \tau_m \odot M_m$;
2. **Elect Sign (Eleger Sinal):** Calcula o vetor de sinal majoritário ponderado $\gamma \in \{-1, 1\}^d$ através da soma das direções de todas as tarefas;
3. **Disjoint Merge (Fundir):** Média apenas dos parâmetros cujos sinais coincidem com o sinal eleito $\gamma$.

Na interpolação esférica **SLERP** com fator $t \in [0, 1]$ entre os vetores de peso $v_0$ e $v_1$ normalizados:

$$\text{SLERP}(v_0, v_1; t) = \frac{\sin((1 - t)\theta)}{\sin(\theta)} v_0 + \frac{\sin(t\theta)}{\sin(\theta)} v_1, \quad \theta = \arccos(\hat{v}_0 \cdot \hat{v}_1)$$

## 🧱 Hipóteses e condições de validade

- A fusão por soma e vetores de tarefa exige obrigatoriamente que os modelos constituintes compartilhem a mesma arquitetura dimensional e tenham partido do mesmo checkpoint de pré-treino (*same basin of attraction*).
- Modelos treinados do zero de forma independente possuem matrizes em permutações desconexas que geram ruído branco se somadas sem alinhamento prévio (*Git Re-Basin*).

## ✅ Quando usar

- Combinar um modelo forte em conversação com outro forte em raciocínio matemático ou código sem gastar computação de treino.
- Compactar múltiplos adaptadores LoRA corporativos em uma única rede para simplificar o pipeline de atendimento.
- Criação de modelos para dispositivos de borda com memória estrita que precisam executar múltiplas funções.

## 🚫 Quando não usar

- Tentar fundir modelos com vocabulários, tokenizadores ou dimensões de camadas incompatíveis (ex.: tentar somar linearmente um modelo Llama 3 com um modelo Mistral).

## ⚠️ Limitações e armadilhas

- **Interferência Destrutiva entre Parâmetros:** A fusão ingênua sem poda (como média direta de múltiplos modelos) faz com que parâmetros especializados se anulem mutuamente, degradando a performance geral em todas as tarefas.
- **Instabilidade de Frankenmerging:** Modelos criados por empilhamento arbitrário de camadas (layer stacking) frequentemente exigem uma etapa subsequente de ajuste fino para reparar descontinuidades nas ativações entre blocos que não foram treinados juntos.

## 🔍 Comparações

| Técnica de Fusão | Preserva Magnitude Vetorial? | Resolve Conflito de Sinais? | Custo Computacional |
|---|---|---|---|
| **Média Linear Simples** | Não (achata a variância) | Não (cancela sinais opostos) | Mínimo (CPU) |
| **SLERP** | **Sim (caminha no arco da esfera)** | Parcialmente (apenas 2 modelos) | Mínimo (CPU) |
| **TIES-Merging / DARE** | Sim | **Sim (poda os menores e elege o sinal)**| Baixo (CPU) |
| **Ensemble Tradicional** | Não aplicável (não funde pesos)| Não aplicável | **Altíssimo (roda $N$ modelos na GPU)** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

A startup Upstage precisava criar um modelo intermediário de cerca de 10 bilhões de parâmetros, mas só existiam bases abertas de 7B e de 70B disponíveis.
Em vez de gastar centenas de milhares de dólares treinando um modelo de 10B do zero:
- A equipe aplicou **Layer Stacking (Depthwise Scaling)** sobre o Llama 2-7B (que possui 32 camadas).
- Eles duplicaram o modelo, fundiram 16 camadas intermediárias e empilharam as restantes, sintetizando uma arquitetura inédita de **48 camadas e 10,7 bilhões de parâmetros** (**o modelo SOLAR 10.7B**).
- Com um breve ajuste fino subsequente, o SOLAR 10.7B superou modelos muito maiores em benchmarks globais com uma fração diminuta do custo histórico de desenvolvimento.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

### Complementos

- [[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA (Low-Rank Adaptation)]]
- [[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|Ajuste Fino Eficiente em Parâmetros (PEFT)]]

### Alternativas

- Treinamento Multitarefa Simultâneo (*Joint Multitask Training*).
- Ensembles de Modelos em Tempo de Execução.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/mixture-of-experts.md|Mixture of Experts (MoE)]] (MoE Upcycling decorre de layer stacking)
- [[redes/ai-engineering/conceitos/matematica-da-memoria-de-treinamento.md|Matemática da Memória de Treinamento]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 347–357
- **Evidência:** Chip Huyen aborda a taxonomia de fusão de modelos (soma, empilhamento e concatenação), detalha o conceito de vetores de tarefa (Ilharco et al., 2022), as técnicas de resolução de interferência TIES (Yadav et al., 2023) e DARE (Yu et al., 2023), o algoritmo SLERP e a arquitetura de upscaling do SOLAR 10.7B (Kim et al., 2023).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é a Fusão de Modelos (*Model Merging*) e qual é a sua principal vantagem econômica frente ao retreinamento multitarefa?
2. Como a abordagem de fusão de modelos contorna o problema do esquecimento catastrófico (*catastrophic forgetting*)?
3. O que são vetores de tarefa (*task vectors*) e como operações de soma e subtração aritmética atuam sobre eles?
4. Por que a Interpolação Linear Esférica (SLERP) é geometricamente superior à média linear simples na fusão de dois modelos?
5. Qual é o mecanismo de ação da técnica TIES-Merging para eliminar interferências e conflitos de sinal entre especialistas?
6. O que é a técnica de *Layer Stacking* (Frankenmerging) e como o modelo SOLAR 10.7B a utilizou para criar um modelo de profundidade expandida?
7. Por que a fusão por soma de parâmetros exige que os modelos compartilhem obrigatoriamente a mesma linhagem e arquitetura base de pré-treino?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Hiperparâmetros de Ajuste Fino

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 359–361

## 📝 Definição

### Definição formal

Os **Hiperparâmetros de Ajuste Fino** (*Finetuning Hyperparameters*) são as variáveis de configuração exógenas e políticas de controle algorítmico que governam a dinâmica de otimização, convergência estatística e estabilidade numérica durante o treinamento supervisionado ou adaptativo de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]], compreendendo quatro eixos operacionais centrais:
1. **Taxa de Aprendizado (*Learning Rate* — $\eta$) e Agendas (*Schedules*):** A magnitude do passo de atualização dos parâmetros ao longo da superfície de perda;
2. **Tamanho de Lote (*Batch Size*) e Acúmulo de Gradientes (*Gradient Accumulation*):** O volume de dados empíricos agregados antes de cada atualização física dos pesos;
3. **Número de Épocas (*Epochs*):** A quantidade de passagens completas sobre o conjunto de dados de ajuste fino;
4. **Ponderação da Perda do Prompt (*Prompt Loss Weight*):** O fator escalar que regula a contribuição relativa dos tokens da instrução de entrada na função de perda em comparação com os tokens da resposta gerada.

### Em linguagem simples

São os "botões de controle" que o engenheiro precisa ajustar na máquina antes de apertar o botão de iniciar o treinamento. Se você girar o botão da velocidade de aprendizado rápido demais, o modelo enlouquece e desaprende o português; se você girar devagar demais, o treino demora semanas e custa uma fortuna sem sair do lugar. Ajustar esses botões com sabedoria garante que a IA aprenda a tarefa com o menor custo e sem estragar o cérebro que ela já tinha.

### Escopo e distinções

Diferenciam-se dos **parâmetros** (pesos internos que o modelo aprende sozinho). Os hiperparâmetros são fixados pelo engenheiro e controlam as restrições físicas de hardware, prevenindo sobreajuste (*overfitting*) e instabilidade numérica.

## 🧩 Problema que resolve

Resolve a volatilidade e o desperdício computacional em experimentos de ajuste fino. Escolhas equivocadas de hiperparâmetros causam perda de convergência, destruição dos pesos pré-treinados ou sobreajuste severo onde o modelo decora as perguntas do treino mas erra tudo o que recebe de usuários em produção.

## 💡 Intuição

Pense em assar um pão artesanal no forno:
- A **Taxa de Aprendizado** é a temperatura do forno. Se colocar a $500^\circ\text{C}$, a crosta queima nos primeiros dois minutos e o miolo fica cru (**perda de estabilidade e colapso**). Se colocar a $50^\circ\text{C}$, o pão fica lá por dez horas e nunca assa (**sub-aprendizado**).
- As **Épocas** é o tempo de forno: deixar 30 minutos é perfeito; esquecer o pão por 5 horas dentro do forno transforma a massa em carvão seco (**sobreajuste/overfitting**).
- O **Tamanho do Lote** é o tamanho da assadeira: assar um pãozinho isolado a cada vez gasta gás demais de forma instável; assar fornadas cheias garante temperatura estável e cozimento uniforme.

## ⚙️ Como funciona

A calibração dos hiperparâmetros atua diretamente no ciclo de atualização da GPU:

### Etapas

1. **Definição da Taxa de Aprendizado ($\eta$):** 
   - No ajuste fino, utiliza-se taxas ordens de magnitude menores do que no pré-treinamento (faixas típicas entre $10^{-7}$ e $10^{-4}$);
   - Uma heurística consagrada consiste em tomar a taxa final do pré-treino do modelo base e multiplicá-la por um fator entre $0{,}1$ e $1{,}0$;
   - Aplica-se um *learning rate schedule* (como decaimento cosseno com aquecimento / *warmup* inicial).
2. **Dimensionamento do Lote e Acúmulo de Gradientes:**
   - Como a memória VRAM não suporta lotes físicos grandes para LLMs, utiliza-se um lote físico pequeno (ex.: tamanho 2 ou 4);
   - Para evitar a instabilidade estatística de atualizar pesos com apenas 2 exemplos, aplica-se **Acúmulo de Gradientes**: a GPU calcula gradientes para múltiplos mini-lotes consecutivos somando-os na memória, e dispara o passo do otimizador apenas após acumular o equivalente a um lote efetivo saudável (ex.: 32 ou 64 amostras).
3. **Controle de Épocas:**
   - Para bases massivas de centenas de milhares de pares, 1 a 2 épocas são suficientes;
   - Para datasets compactos de poucas centenas de exemplos de alta curadoria, treina-se por 3 a 5 épocas monitorando a perda de validação (*eval loss*).
4. **Mascaramento da Perda do Prompt (*Prompt Loss Weight*):**
   - Configura-se o peso de perda dos tokens do prompt em $0\%$ (ou $10\%$). Os gradientes penalizam apenas os erros nas posições dos tokens da resposta ideal, impedindo que o modelo desperdice capacidade memorizando as palavras do usuário.

### Entradas e saídas

- **Entradas:** Conjuntos de treino e validação e orçamento de hardware disponível.
- **Saídas:** Curvas de perda (*loss curves*) suaves e decrescentes convergindo para um ponto ótimo de validação.

## 📐 Formulação matemática

A regra de atualização de parâmetros sob descida de gradiente estocástica com momento ou Adam é governada pela taxa $\eta_t$:

$$\theta_{t+1} = \theta_t - \eta_t \cdot \hat{m}_t$$

O tamanho efetivo do lote ($B_{\text{efetivo}}$) resultante do acúmulo de gradientes sobre $S_{\text{accum}}$ passos físicos de tamanho $B_{\text{físico}}$ com paralelismo de dados em $G$ GPUs é:

$$B_{\text{efetivo}} = B_{\text{físico}} \times S_{\text{accum}} \times G$$

Na computação da perda mista ponderada, seja $X$ os tokens do prompt e $Y$ os tokens da resposta, com peso $\lambda_{\text{prompt}} \in [0, 1]$:

$$\mathcal{L}_{\text{total}} = \lambda_{\text{prompt}} \sum_{i \in X} \mathcal{L}(x_i) + \sum_{j \in Y} \mathcal{L}(y_j)$$

Fixar $\lambda_{\text{prompt}} = 0$ foca $100\%$ do poder de atualização da rede exclusivamente na qualidade da geração de $Y$.

## 🧱 Hipóteses e condições de validade

- A estabilidade da convergência pressupõe monitoramento contínuo da perda de validação; se a perda de treino continuar caindo enquanto a perda de validação sobe, o modelo entrou em regime estrito de sobreajuste e o treino deve ser interrompido imediatamente (*Early Stopping*).

## ✅ Quando usar

- Configuração obrigatória em qualquer script de treinamento de LoRA, QLoRA ou Full Finetuning com frameworks como Hugging Face TRL, unsloth ou Axolotl.

## 🚫 Quando não usar

- Em inferência pura ou em técnicas de engenharia de prompt em tempo de execução, onde não há treinamento de parâmetros.

## ⚠️ Limitações e armadilhas

- **Lotes físicos minúsculos sem acúmulo de gradientes:** Atualizar pesos a cada 1 ou 2 exemplos gera gradientes ruidosos que fazem a curva de perda oscilar violentamente, impedindo a convergência.
- **Taxa de aprendizado excessivamente alta:** Aplicar taxas de aprendizado de ML tradicional (como $10^{-2}$ ou $10^{-3}$) em LLMs pré-treinados destrói os pesos da atenção, fazendo a perda explodir para $\text{NaN}$ nos primeiros 10 passos.

## 🔍 Comparações

| Hiperparâmetro | Se for muito Baixo... | Se for muito Alto... | Valor Típico no Finetuning |
|---|---|---|---|
| **Learning Rate ($\eta$)** | Aprendizado excessivamente lento | Explosão de perda e colapso de pesos | $1 \times 10^{-5}$ a $2 \times 10^{-4}$ |
| **Batch Size Efetivo** | Gradientes ruidosos e treino instável | Estouro de memória VRAM da GPU | 16 a 64 amostras |
| **Número de Épocas** | Sub-aprendizado (não internaliza o estilo) | Sobreajuste (decora os exemplos exatos) | 1 a 4 épocas |
| **Prompt Loss Weight** | Foco estrito na resposta (Recomendado)| O modelo gasta capacidade decorando perguntas| **$0{,}0$ a $0{,}1$** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um engenheiro configura o ajuste fino de um modelo médico com 2.000 exemplos de prontuários em uma GPU com apenas 16 GB de VRAM.
- Devido ao limite de memória, ele só consegue colocar um **Batch Size físico de 1**. Se ele atualizasse os pesos a cada prontuário isolado, a variação extrema entre casos médicos faria o treinamento oscilar loucamente.
- Ele ativa o **Gradient Accumulation em 32 passos**: a GPU processa 32 prontuários sequencialmente, acumula os gradientes matemáticos na VRAM sem atualizar os pesos e só executa o passo do otimizador Adam na 32ª amostra. O treinamento atinge a estabilidade matemática perfeita de um supercomputador mantendo a pegada física de uma única placa modesta.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/matematica-da-memoria-de-treinamento.md|Matemática da Memória de Treinamento]]
- [[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|Ajuste Fino Eficiente em Parâmetros (PEFT)]]

### Complementos

- [[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA (Low-Rank Adaptation)]]
- [[redes/ai-engineering/conceitos/quantized-lora-qlora.md|Quantized LoRA (QLoRA)]]

### Alternativas

- Busca automatizada de hiperparâmetros por força bruta (inviável economicamente para modelos de grande escala).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]
- [[redes/ai-engineering/conceitos/representacoes-numericas-e-precisao.md|Representações Numéricas e Precisão]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 359–361
- **Evidência:** Chip Huyen destrincha a calibração de hiperparâmetros no finetuning prático, analisa as dinâmicas de curvas de perda para diagnosticar taxas de aprendizado inadequadas, detalha a técnica de acúmulo de gradientes para contornar restrições de VRAM e explica o mascaramento e ponderação de perda nos tokens do prompt.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são os principais hiperparâmetros de controle operados durante o ajuste fino de um modelo de fundação?
2. Por que a taxa de aprendizado adotada no finetuning deve ser ordens de magnitude menor do que a utilizada no pré-treinamento original?
3. O que é a técnica de Acúmulo de Gradientes (*Gradient Accumulation*) e qual problema de memória física ela contorna?
4. Como o comportamento relativo entre a curva de perda de treinamento (*training loss*) e a curva de validação orienta o número ideal de épocas?
5. O que é o *Prompt Loss Weight* e qual é a justificativa de engenharia para fixá-lo em zero ou em valores muito baixos?
6. Quais são os sintomas visíveis na curva de perda quando a taxa de aprendizado foi configurada com valor excessivamente alto?
7. Como a fórmula de tamanho efetivo de lote correlaciona o lote físico por GPU com os passos de acúmulo de gradiente?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.


*Nota gerada a partir do capítulo Capítulo 7 — Finetuning. A interpretação final deve ser revisada pelo estudante.*
