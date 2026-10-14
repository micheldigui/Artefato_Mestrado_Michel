# 🧠 QLoRA (Quantized Low-Rank Adaptation)

**Rede:** `ai-engineering`  
**Área:** `otimizacao-de-modelos`

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 7 — Finetuning
- Localização: Páginas 345–347

## 📝 Definição

### Definição formal

Uma técnica de ajuste fino eficiente em parâmetros que combina a quantização extrema dos pesos do modelo base para 4 bits (*NF4*) com adaptadores LoRA treinados em alta precisão, complementada por otimizadores paginados (*paged optimizers*) para prevenção de estouro de memória.

O **QLoRA** (*Quantized Low-Rank Adaptation*, Dettmers et al., 2023) é uma técnica avançada de ajuste fino eficiente em parâmetros que combina quantização de alta densidade com adaptadores de posto baixo ([[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA]]), alicerçada em três inovações algorítmicas de engenharia:
1. **Formato de Dados NormalFloat-4 (NF4):** Uma representação de 4 bits teoricamente ótima em termos de informação para parâmetros neurais que seguem distribuição normal com média zero;
2. **Dupla Quantização (*Double Quantization*):** A quantização das próprias constantes de escala de quantização da primeira etapa, reduzindo a sobrecarga residual de memória de 0,5 bit para 0,127 bit por parâmetro;
3. **Otimizadores Paginados (*Paged Optimizers*):** O gerenciamento automático de paginação de memória que descarrega estados do otimizador da VRAM da GPU para a memória RAM da CPU durante picos de ativação de sequências longas, prevenindo falhas de *Out of Memory*.

### Em linguagem simples

É a técnica definitiva de economia de recursos que espreme um modelo gigante de 65 bilhões de parâmetros para caber em uma única placa de vídeo comum de 48GB, permitindo treiná-lo sem perder a precisão do aprendizado.

É a tecnologia que permitiu treinar um modelo monstruoso de 65 bilhões de parâmetros dentro de uma única placa de vídeo profissional de 48 GB (algo que antes exigia um servidor com 8 placas caríssimas). O QLoRA espreme os pesos congelados do modelo para apenas 4 bits na memória, mas no milissegundo em que precisa fazer as contas de matemática, ele descompacta temporariamente os números para 16 bits para não perder a precisão dos cálculos.

### Escopo e distinções

Diferencia-se do LoRA tradicional porque o LoRA comum mantém o modelo base em 16 bits (*FP16/BF16*), enquanto o QLoRA comprime a base para 4 bits, exigindo desquantização dinâmica sob demanda durante o cálculo de gradientes.

Distingue-se do LoRA tradicional porque no LoRA padrão os pesos congelados do modelo base permanecem em 16 bits (FP16 ou BF16). No QLoRA, os pesos base são armazenados em 4 bits estritos (NF4), enquanto apenas os adaptadores LoRA são mantidos e atualizados em 16 bits.

## 🧩 Problema que resolve

Resolve a barreira de hardware imposta pelo tamanho de modelos modernos, viabilizando o ajuste fino de modelos de ponta em hardwares de consumo ou servidores modestos de baixo custo.

Resolve a barreira física de VRAM que impedia desenvolvedores, laboratórios acadêmicos e startups de realizarem ajuste fino em modelos de grande porte ($\ge 65\text{B}$ parâmetros). Com o LoRA comum, um modelo de 65B exige mais de 130 GB de VRAM apenas para carregar os pesos congelados; com o QLoRA, a exigência despenca para cerca de 41 GB, viabilizando o treino em uma única GPU.

## 💡 Intuição

Imagine carregar um dicionário enciclopédico gigante guardado em formato compactado zipado na memória RAM do computador, abrindo e descompactando apenas as páginas exatas que você vai ler a cada consulta de estudo.

Pense em um arquivo morto de documentos jurídicos de uma grande corporação:
- Se você mantiver todos os 10.000 livros de processos físicos abertos sobre as mesas da biblioteca (**LoRA em 16 bits**), você precisará alugar um galpão imenso apenas para sustentar o peso do papel.
- No **QLoRA**, todos os livros antigos são microfilmados e guardados em cartuchos de filme compactos em uma gaveta de 4 bits (**pesos em NF4**). O pesquisador tem uma pequena mesa de leitura de 16 bits (**os adaptadores LoRA**). Quando ele precisa consultar uma página específica do processo antigo, ele coloca o microfilme no projetor, lê a frase em tamanho real, anota sua conclusão no caderno de 16 bits e guarda o filme de volta na gaveta.

## ⚙️ How it works / Como funciona

### Etapas

1. O modelo base é carregado na memória comprimido em formato de 4 bits utilizando um tipo especial de quantização gaussiana otimizada (*NormalFloat4 - NF4*).
2. Adiciona-se os adaptadores LoRA em 16 bits ao redor das camadas congeladas.
3. Durante o cálculo da passagem de avanço (*forward pass*), os pesos de 4 bits são desquantizados dinamicamente para *BF16* para o cálculo matricial.
4. Otimizadores paginados gerenciados via CPU/GPU impedem falhas de estouro de memória (*OOM*) caso o lote de dados estoure a capacidade do hardware.

### Entradas e saídas

- Entradas: Modelo base em 4 bits, adaptadores LoRA e dataset de adaptação.
- Saídas: Adaptador LoRA treinado e otimizado pronto para fusão ou inferência.

## 📐 Formulação matemática

Utiliza a quantização *NormalFloat4 (NF4)* baseada na premissa informada de que os pesos de redes neurais pré-treinadas seguem uma distribuição normal zero-centrada. A desquantização dinâmica reconstrói o tensor original $W^{BF16}$ a partir do tensor quantizado $W^{NF4}$:

$$W^{BF16} = \text{dequantize}(W^{NF4})$$

Onde o gradiente e os adaptadores LoRA operam em precisão superior para preservar a convergência do aprendizado sem perda catastrófica de desempenho.

O tipo de dados **NormalFloat (NF4)** baseia-se na quantização de quantis de informação teórica ótima para distribuições gaussianas padronizadas $X \sim \mathcal{N}(0, 1)$. 
Os $2^k = 16$ pontos discretos de quantização $q_i$ ($i \in \{0, \dots, 15\}$) são distribuídos de modo que a integral da densidade de probabilidade entre quantis adjacentes seja constante:

$$q_i = \frac{1}{2} \left( Q_X\left(\frac{i}{2^k}\right) + Q_X\left(\frac{i+1}{2^k}\right) \right)$$

Onde $Q_X(\cdot)$ é a função de quantil (inversa da função de distribuição cumulativa) da distribuição normal padrão.
Durante a passagem direta, a operação computada pelo kernel em tempo de execução é:

$$Y^{\text{BF16}} = X^{\text{BF16}} \cdot \text{dequant}\Big(c_1^{\text{FP32}}, \; c_2^{\text{FP8}}, \; W^{\text{NF4}}\Big) + \frac{\alpha}{r} X^{\text{BF16}} A^{\text{BF16}} B^{\text{BF16}}$$

Onde $c_1$ e $c_2$ são as constantes derivadas da dupla quantização.

## 🧱 Hipóteses e condições de validade

- Supõe que a desquantização dinâmica em tempo de execução compensa a perda de precisão estática de 4 bits sem destruir a convergência do gradiente.

- Exige compiladores e kernels especializados em CUDA (como a biblioteca *bitsandbytes*) configurados para executar a desquantização rápida sob demanda na GPU.

## ✅ Quando usar

- Quando se deseja realizar o ajuste fino de modelos massivos (ex: 33B a 70B parâmetros) dispondo de recursos limitados de hardware de GPU.

- Ajuste fino de modelos maciços (33B, 65B, 70B parâmetros) quando a infraestrutura disponível é limitada a uma única GPU profissional de 48 GB ou GPUs de 80 GB individuais.
- Democratização de pesquisa e testes rápidos de modelos de ponta com restrições severas de orçamento em nuvem.

## 🚫 Когда não usar / Quando não usar

- Em ambientes corporativos que possuem clusters ilimitados de múltiplos nós de GPUs com alta performance, onde o overhead computacional de desquantização do QLoRA possa ser evitado.

## ⚠️ Limitações e armadilhas

- O processo de desquantização e quantização em tempo de execução adiciona uma sobrecarga computacional que pode tornar o treinamento mais lento do que o LoRA convencional em 16 bits.

- **Sobretaxa de Tempo de Computação:** A economia drástica de memória VRAM é paga com aumento no tempo de treinamento devido ao processamento repetido de conversão de tipos de dados.
- **Fusão de Pesos Complexa:** Para fundir os pesos finais do LoRA de volta ao modelo original, é necessário desquantizar a base inteira para 16 bits antes da soma algébrica, gerando um modelo final de tamanho padrão em disco.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[qlora|QLoRA]] | Viabilizar treino de modelos gigantes em 4 bits via adaptadores. | Modelo base em 4 bits + LoRA. | Adaptador treinado. | Comprime a base para 4 bits (*NF4*), sacrificando um pouco de velocidade por muita economia de VRAM. |
| [[lora|LoRA padrão]] | Ajustar modelos eficientemente congelando a base em 16 bits. | Modelo base em 16 bits + LoRA. | Adaptador treinado. | Mantém o modelo base na precisão original de 16 bits, exigindo mais VRAM. |

| Característica | LoRA Convencional | QLoRA |
|---|---|---|
| **Precisão dos Pesos Base** | 16 bits (FP16 / BF16) | **4 bits (NF4)** |
| **Precisão dos Adaptadores**| 16 bits (FP16 / BF16) | 16 bits (BF16) |
| **VRAM para Modelo de 65B** | $> 130 \text{ GB}$ (exige múltiplas GPUs) | **$\approx 41 \text{ GB}$ (uma única GPU de 48 GB)** |
| **Velocidade por Época** | Mais rápida | Mais lenta (overhead de desquantização) |
| **Desempenho Final** | Linha de base competitiva | Praticamente indistinguível do LoRA de 16 bits |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Fazer o *finetuning* do Llama 2 de 70 bilhões de parâmetros rodando perfeitamente em uma única placa de vídeo comercial de 48GB (como uma A6000), algo que antes exigiria oito placas de vídeo corporativas em rede.

O laboratório de pesquisa da Universidade de Washington introduziu a família de modelos **Guanaco** através do QLoRA:
Eles pegaram o modelo bruto Llama 1 de 65 bilhões de parâmetros. 
- Com o Full Finetuning ou LoRA convencional, eles precisariam de um cluster com pelo menos 8 a 16 placas A100 interconectadas, consumindo milhares de dólares de orçamento acadêmico.
- Aplicando **QLoRA em 4 bits NF4 com otimizadores paginados**, eles executaram o treinamento do Guanaco de 65B em uma única GPU NVIDIA RTX de 48 GB em apenas 24 horas. O modelo resultante atingiu pontuação de $99{,}3\%$ no benchmark Vicuna e competiu de igual para igual com o ChatGPT comercial na avaliação de juízes de IA.

## 🔗 Relações no grafo

### Pré-requisitos

- [[lora|LoRA (Low-Rank Adaptation)]]
- [[finetuning|Finetuning]]

- [[redes/ai-engineering/conceitos/lora-low-rank-adaptation.md|LoRA (Low-Rank Adaptation)]]
- [[redes/ai-engineering/conceitos/quantizacao.md|Quantização]]
- [[redes/ai-engineering/conceitos/representacoes-numericas-e-precisao.md|Representações Numéricas e Precisão]]

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

- [[redes/ai-engineering/conceitos/matematica-da-memoria-de-treinamento.md|Matemática da Memória de Treinamento]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

- LoRA tradicional em meia precisão (16 bits).
- Métodos concorrentes de quantização e ajuste como QA-LoRA e IR-QLoRA.

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/hiperparametros-de-ajuste-fino.md|Hiperparâmetros de Ajuste Fino]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da técnica QLoRA, quantização NF4 e otimizadores paginados para redução drástica de memória em treinamento.
- **Confiança:** alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 7 — Finetuning
- **Localização:** Páginas 345–347
- **Evidência:** Chip Huyen destrincha a publicação de Dettmers et al. (2023) sobre QLoRA, detalha as inovações de NF4 e paged optimizers, e apresenta a Tabela 7-7 com os escores Elo dos modelos Guanaco de 7B a 65B avaliados pelo GPT-4 em comparação direta com ChatGPT e Bard.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é QLoRA (Quantized Low-Rank Adaptation)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

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

---
*Nota gerada a partir do capítulo Capítulo 7 — Finetuning. A interpretação final deve ser revisada pelo estudante.*

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

## 🚫 Quando não usar

- Em cenários onde o gargalo primário absoluto do projeto é o **tempo de relógio de treinamento** e há abundância de GPUs de alta performance: a etapa contínua de quantização e desquantização em tempo de execução introduz uma penalidade temporal que torna o QLoRA tipicamente entre $20\%$ e $40\%$ mais lento por época do que o LoRA padrão em 16 bits.
