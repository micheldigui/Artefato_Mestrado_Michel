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
