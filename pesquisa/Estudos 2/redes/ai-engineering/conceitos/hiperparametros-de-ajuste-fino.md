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
