# AI Engineering: Building Applications with Foundation Models — Capítulo 7

## Objetivo do capítulo

Apresentar um panorama técnico e metodológico completo sobre o ajuste fino (*finetuning*) de modelos de fundação. O capítulo examina as justificativas estratégicas para aplicar ou evitar o finetuning, formaliza a dicotomia entre finetuning (para forma/estilo) e RAG (para fatos), disseca as restrições físicas de memória de treinamento impostas pela retropropagação e estados de otimizadores, detalha técnicas de precisão numérica e quantização, explora métodos de ajuste eficiente em parâmetros (PEFT) com ênfase aprofundada em LoRA e QLoRA, introduz a fusão de modelos (*model merging*) como alternativa e complemento ao aprendizado multitarefa, e consolida táticas empíricas de seleção de hiperparâmetros.

## Resumo do argumento central

O ajuste fino é uma extensão do aprendizado por transferência que adapta os pesos de um modelo pré-treinado para domínios ou formatos específicos com maior eficiência de amostra do que o treinamento do zero. Contudo, devido à escala dos modelos modernos, o finetuning integral (*Full Finetuning*) exige infraestruturas de hardware e volumes de memória VRAM proibitivos para a maioria dos engenheiros, decorrentes da necessidade de manter em memória não apenas os pesos, mas ativações intermediárias, gradientes e os estados estatísticos do otimizador Adam. Consequentemente, a engenharia de IA moderna apoia-se em duas grandes frentes de otimização: a redução de precisão numérica (quantização e formatos como FP16, BF16 e INT4) e o ajuste fino eficiente em parâmetros (PEFT). 

Dentre as abordagens de PEFT, o LoRA (*Low-Rank Adaptation*) consolidou-se como o padrão dominante ao decompor matrizes densas em produtos de matrizes de baixo posto, viabilizando o ajuste fino com uma fração diminuta de parâmetros treináveis sem introduzir latência adicional na inferência. A combinação de LoRA com quantização de 4 bits (QLoRA) democratizou o ajuste de modelos de dezenas de bilhões de parâmetros em GPUs individuais. Adicionalmente, técnicas emergentes de fusão de modelos (*model merging*) possibilitam unificar habilidades especializadas de múltiplos modelos ajustados em uma única rede sem custos de novo treinamento e sem o risco de esquecimento catastrófico. O sucesso prático do finetuning reside em esgotar previamente as possibilidades de prompting e RAG, e em calibrar criteriosamente hiperparâmetros como taxa de aprendizado, tamanho de lote, acúmulo de gradientes e ponderação da perda do prompt.

## Conceitos identificados

- Ajuste Fino (Finetuning)
- Geração Aumentada de Recuperação (RAG)
- Modelo de Fundação
- Matemática da Memória de Treinamento
- Representações Numéricas e Precisão
- Quantização
- Ajuste Fino Eficiente em Parâmetros (PEFT)
- LoRA (Low-Rank Adaptation)
- Quantized LoRA (QLoRA)
- Fusão de Modelos (Model Merging)
- Hiperparâmetros de Ajuste Fino

## Sequência lógica do capítulo

1. **Visão Geral do Finetuning (pp. 308–311):** Origens no aprendizado por transferência (Bozinovski e Fulgosi, 1976); ganho em eficiência de amostra (*sample efficiency*); modalidades de ajuste (auto-supervisionado/pré-treino continuado, infilling, supervisionado e alinhamento de preferência); distinção entre papéis de desenvolvedores de modelos e engenheiros de aplicação.
2. **Quando Fazer Finetuning (pp. 311–319):** Razões para ajustar (estilo, consistência de saída estruturada, sintaxes raras, mitigação de vieses demográficos, destilação para modelos menores); razões para não ajustar (esquecimento catastrófico, perda de generalidade, custos de infraestrutura e governança de dados); o dilema Finetuning vs. RAG (Finetuning é para forma, RAG é para fatos); fluxo de maturidade arquitetural (Prompting $\to$ Few-Shot $\to$ RAG $\to$ Finetuning).
3. **Gargalos de Memória (pp. 319–332):** Mecânica da retropropagação (*backpropagation*) e parâmetros treináveis; decomposição matemática da pegada de memória (pesos, ativações, gradientes e estados do otimizador Adam); técnica de *gradient checkpointing*; representações numéricas de ponto flutuante (FP32, FP16, BF16, TF32) e inteiros (INT8, INT4); limites de alcance (*range*) versus precisão; quantização na inferência (PTQ) e no treinamento (QAT, precisão mista automática com AMP).
4. **Técnicas de Finetuning (pp. 332–357):** Ajuste fino parcial e a ineficiência de congelar camadas iniciais; emergência do PEFT (Houlsby et al., 2019); taxonomia de métodos PEFT (aditivos/adaptadores versus prompts suaves/soft prompts); fundamentos do LoRA (fatoração de posto baixo, hipótese da baixa dimensão intrínseca de LLMs, hiperparâmetros $r$ e $\alpha$); estratégias de atendimento de múltiplos adaptadores (*multi-LoRA serving*); Quantized LoRA (QLoRA) com o formato NormalFloat-4 (NF4) e otimizadores paginados; Fusão de Modelos (*Model Merging*) como técnica para multitarefa sem esquecimento catastrófico (soma linear, SLERP, poda de interferência com TIES e DARE, e empilhamento de camadas / *frankenmerging*).
5. **Táticas de Finetuning (pp. 357–361):** Seleção de modelos base (estratégia de progressão versus destilação); frameworks de mercado (PEFT, Axolotl, unsloth, LitGPT); calibração de hiperparâmetros (taxa de aprendizado e schedules, tamanho de lote e acúmulo de gradientes, número de épocas e sobreajuste, e ponderação da perda nos tokens do prompt).

## Principais afirmações

- O aprendizado por transferência através de modelos de fundação eleva drasticamente a eficiência amostral: comportamentos que exigiriam milhões de exemplos do zero podem ser aprendidos com centenas ou milhares de demonstrações.
- Modelos de fundação possuem dimensões intrínsecas surpreendentemente baixas após o pré-treinamento, o que viabiliza matematicamente adaptar redes de bilhões de parâmetros atualizando apenas uma fração minúscula de pesos de baixo posto.
- O gargalo primário do treinamento e ajuste fino de LLMs é a memória VRAM da GPU, impulsionada exponencialmente pelo otimizador Adam, que armazena dois estados adicionais (momento e variância) para cada parâmetro treinável.
- A regra canônica de arquitetura dita que Finetuning serve prioritariamente para modelar a **forma** (estilo, sintaxe, formato JSON/código e concisão), enquanto RAG serve para injetar os **fatos** (dados recentes, privados e auditáveis).
- A quantização converte valores numéricos para formatos com menor número de bits, reduzindo a pegada de memória e acelerando operações matriciais, mas introduz riscos de instabilidade caso limites de representação sejam ultrapassados.
- O método LoRA preserva os pesos originais congelados e injeta matrizes fatoradas adicionais, permitindo fusão direta dos pesos antes da inferência ou atendimento dinâmico de centenas de adaptadores especializados compartilhando o mesmo modelo base.
- A fusão de modelos (*model merging*) viabiliza criar modelos multitarefa sem custo computacional de treinamento e contorna o esquecimento catastrófico através de operações algébricas e geométricas sobre vetores de tarefa.

## Fórmulas ou procedimentos apresentados

- Decomposição fundamental da memória de treinamento:
  $$\text{Memória}_{\text{treino}} = \text{Pesos} + \text{Ativações} + \text{Gradientes} + \text{Estados do Otimizador}$$
- Memória dos estados do otimizador Adam para $N_{\text{treináveis}}$ parâmetros em formato de 16 bits (2 bytes):
  $$\text{Memória}_{\text{Adam}} = 2 \times N_{\text{treináveis}} \times 2 \text{ bytes} = 4 \times N_{\text{treináveis}} \text{ bytes}$$
- Formulação da adaptação de baixo posto no LoRA para matriz $W_0 \in \mathbb{R}^{d \times k}$:
  $$W' = W_0 + \Delta W = W_0 + \frac{\alpha}{r} (B \cdot A)$$
  *(onde $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times k}$ e o posto $r \ll \min(d, k)$).*
- Combinação linear ponderada na fusão de modelos:
  $$\text{Merge}(M_A, M_B) = \frac{w_A M_A + w_B M_B}{w_A + w_B}$$
- Interpolação Linear Esférica (SLERP) entre vetores normalizados $v_0$ e $v_1$ com ângulo $\theta$:
  $$\text{SLERP}(v_0, v_1; t) = \frac{\sin((1 - t)\theta)}{\sin(\theta)} v_0 + \frac{\sin(t\theta)}{\sin(\theta)} v_1, \quad \text{onde } \theta = \arccos\left(\frac{v_0 \cdot v_1}{\|v_0\| \|v_1\|}\right)$$

## Exemplos relevantes

- Caso Grammarly: substituição de modelos massivos por modelos Flan-T5 60 vezes menores ajustados especificamente para tarefas de edição textual com apenas 82.000 exemplos, superando os modelos maiores.
- Caso BloombergGPT: modelo de 50 bilhões de parâmetros treinado do zero com custo estimado entre US$ 1,3 e 2,6 milhões de computação, que foi posteriormente superado em benchmarks financeiros por modelos generalistas como o GPT-4 em modo zero-shot.
- Confusão operacional entre FP16 e BF16 no Llama 2: equipes que carregaram o modelo em FP16 sofreram degradação severa de acurácia porque os pesos foram calibrados para a faixa dinâmica do BF16.
- Caso Guanaco (Dettmers et al., 2023): modelo de 65 bilhões de parâmetros ajustado em uma única GPU de 48 GB através de QLoRA em formato NF4, atingindo desempenho comparativo competitivo contra o ChatGPT.

## Limitações e ressalvas

- O capítulo concentra-se no ajuste supervisionado e eficiente em parâmetros para adaptação de modelos; procedimentos aprofundados de alinhamento com RLHF e DPO foram examinados no Capítulo 2.
- Métodos empíricos de fusão de modelos (como frankenmerging e SLERP) possuem fundamentação teórica ainda em consolidação, exigindo validação empírica estrita a cada aplicação.

## Dúvidas em aberto

- Até que ponto matrizes de posto ultrabaixo ($r=1$ ou $r=2$) conseguem generalizar para tarefas que exigem reestruturação conceitual profunda sem sofrer saturação rápida?
- Quais são os limites de convergência assintótica de modelos treinados inteiramente em regimes de 1 bit ou 1,58 bits por parâmetro em comparação com modelos densos quantizados?

## Localização da fonte

Capítulo 7, páginas 307 a 362 do livro impresso / arquivo de texto consolidado.
