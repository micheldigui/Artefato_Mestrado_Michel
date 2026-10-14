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
