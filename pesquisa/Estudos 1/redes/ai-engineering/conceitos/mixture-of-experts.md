# 🧠 Mixture of Experts (MoE)

**Rede:** `ai-engineering`  
**Área:** `arquitetura`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 68, 354–355

## 📝 Definição

### Definição formal

A **Mixture of Experts** (*MoE* ou Mistura de Especialistas) é uma classe de arquitetura neural esparsa na qual certas camadas densas (geralmente as camadas feedforward/MLP dos blocos Transformer) são substituídas por um conjunto de redes paralelas independentes denominadas **especialistas** (*experts*), coordenadas por uma rede de roteamento (*router* ou *gating network*) que seleciona e ativa dinamicamente apenas um subconjunto restrito desses especialistas para processar cada token de entrada.

### Em linguagem simples

É uma arquitetura onde o modelo possui vários cérebros menores especializados em seu interior, mas consulta apenas um ou dois deles a cada palavra gerada. Isso permite criar um modelo gigante com uma capacidade imensa de conhecimento, mas que gasta a eletricidade e o tempo de um modelo muito menor durante o uso.

### Escopo e distinções

Diferencia-se dos **modelos densos**, onde todos os parâmetros da rede neural são obrigatoriamente acionados e multiplicados para cada token processado. O exemplo emblemático citado no capítulo é o Mixtral 8x7B.

## 🧩 Problema que resolve

Resolve o compromisso rígido entre capacidade de aprendizado e custo de computação. Em modelos densos, para dobrar o conhecimento do modelo é necessário dobrar a quantidade de FLOPs e o custo de inferência por token. O MoE desacopla a capacidade de armazenamento de parâmetros do custo computacional de execução por token.

## 💡 Intuição

Pense em um grande hospital de consultas:
- Em um **modelo denso**, cada paciente que entra com uma dor de cabeça precisa ser consultado ao mesmo tempo por todos os 50 médicos do corpo clínico do hospital em uma sala de conferência lotada. O custo e o tempo gasto são astronômicos.
- Em um **modelo MoE**, existe uma recepcionista de triagem (**o roteador**). O paciente relata o sintoma, a recepcionista analisa a queixa e o encaminha apenas para o neurologista e o clínico geral (**os especialistas ativos**). O hospital possui 50 médicos contratados em seu corpo clínico, mas cada consulta consome apenas a energia de 2 profissionais.

## ⚙️ Como funciona

O processamento do MoE substitui o bloco MLP por uma seleção seletiva:

### Etapas

1. **Recepção do vetor do token:** O token passa pela camada padrão de atenção compartilhada.
2. **Avaliação pelo Roteador (*Gating Network*):** O vetor do token é multiplicado pela matriz de roteamento para calcular pontuações de compatibilidade para todos os $E$ especialistas disponíveis.
3. **Seleção Top-$k$:** O roteador seleciona apenas os $k$ especialistas com as pontuações mais altas (tipicamente $k = 2$, entre 8 especialistas).
4. **Processamento distribuído:** Apenas os $k$ especialistas selecionados executam a passagem de suas camadas neurais para aquele token.
5. **Combinação ponderada:** A saída final do bloco é a soma ponderada das saídas dos especialistas ativos multiplicadas pelas probabilidades calculadas pelo roteador.

### Entradas e saídas

- **Entradas:** Vetor intermediário de ativação de um token.
- **Saídas:** Vetor processado resultante da combinação das redes especialistas selecionadas.

## 📐 Formulação matemática

Dada uma entrada $x$ e $E$ redes especialistas $\{f_1, f_2, \dots, f_E\}$, a saída da camada MoE é dada por:

$$y = \sum_{i=1}^E G(x)_i f_i(x)$$

Onde $G(x)$ é a saída esparsa da rede de roteamento parametrizada por pesos $W_g$. Utilizando seleção Top-$k$:

$$G(x) = \text{softmax}\Big(\text{TopK}(x W_g, k)\Big)$$

Onde $\text{TopK}$ mantém as $k$ maiores pontuações e atribui $-\infty$ a todas as demais, garantindo que $\text{softmax}$ resulte em peso exatamente zero para os especialistas inativos, dispensando a sua execução computacional.
No caso do **Mixtral 8x7B**:
- Parâmetros totais: $46{,}7 \text{ bilhões}$;
- Parâmetros ativos por token ($k=2$): $12{,}9 \text{ bilhões}$.

## 🧱 Hipóteses e condições de validade

- O hardware de inferência deve possuir memória física VRAM suficiente para armazenar a totalidade dos parâmetros do modelo (pesos de todos os especialistas), mesmo que apenas uma fração esteja ativa por token.
- O algoritmo de treinamento deve aplicar perdas de equilíbrio de carga (*load balancing loss*) para impedir que o roteador vicie e envie todos os tokens para os mesmos um ou dois especialistas.

## ✅ Quando usar

- Sistemas de alta escala que demandam conhecimento amplo e enciclopédico com orçamentos restritos de latência e custo de processamento de inferência.
- Cenários onde a infraestrutura dispõe de bastante memória RAM/VRAM para carregar pesos, mas necessita de alta taxa de tokens gerados por segundo.

## 🚫 Quando não usar

- Em dispositivos locais com severa escassez de memória de armazenamento (como smartphones básicos), onde o tamanho em gigabytes do arquivo de pesos do modelo é o limitador primário, inviabilizando carregar os especialistas inativos.

## ⚠️ Limitações e armadilhas

- **Confusão de nomenclatura:** Chamar um modelo MoE de "8x7B" sugere erroneamente que ele tem $8 \times 7 = 56$ bilhões de parâmetros isolados. Devido ao compartilhamento de matrizes de atenção e embeddings, o modelo possui menos parâmetros totais (46,7B no Mixtral) e opera com velocidade de 12,9B.
- **Complexidade de treinamento:** MoEs são mais difíceis de estabilizar durante o pré-treinamento e apresentam desafios acentuados de paralelismo de comunicação entre GPUs.

## 🔍 Comparações

| Dimensão | Modelo Denso (ex.: Llama 2-70B) | Modelo MoE (ex.: Mixtral 8x7B) |
|---|---|---|
| **Ativação de parâmetros** | 100% dos parâmetros a cada token | Fração seletiva (ex.: ~27% dos parâmetros) |
| **Consumo de memória VRAM** | Proporcional aos parâmetros totais | Proporcional aos parâmetros totais |
| **Custo de inferência (FLOPs)** | Proporcional aos parâmetros totais | Proporcional apenas aos parâmetros ativos |
| **Velocidade por token** | Mais lenta | Significativamente mais rápida |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um usuário envia o prompt: `"Escreva uma função em Python para calcular a variância e explique a teoria estatística"`.
- Quando o modelo processa as palavras de código Python (`def`, `import numpy`), o roteador ativa os especialistas número 3 e 7 (redes que aprenderam padrões de sintaxe de programação).
- Quando a frase avança para a explicação formal dos conceitos (`distribuição amostral`), o roteador comuta e ativa os especialistas 1 e 5 (redes alinhadas com raciocínio matemático e prosa conceitual). 
O sistema transita entre expertises sem precisar processar o peso bruto da rede inteira a cada caractere.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/mecanismo-de-atencao.md|Mecanismo de Atenção]]

### Complementos

- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]
- [[redes/ai-engineering/conceitos/leis-de-escala-e-chinchilla.md|Leis de Escala e Chinchilla]]

### Alternativas

- Modelos Densos convencionais (Transformer Denso).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/gargalos-de-escala.md|Gargalos de Escala: Dados e Energia]]
- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 68, 354–355
- **Evidência:** O texto descreve a arquitetura Mixture-of-Experts originada por Shazeer et al. (2017) e popularizada pelo Mixtral 8x7B, demonstrando como a esparsidade permite que um modelo de 46,7B de parâmetros totais opere com o custo e velocidade de computação de um modelo de apenas 12,9B de parâmetros ativos.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é a arquitetura Mixture of Experts (MoE) e como ela se diferencia estruturalmente de um modelo denso?
2. O que representam os conceitos de "parâmetros totais" e "parâmetros ativos por token" em um MoE?
3. Como funciona a rede de roteamento (*gating network*) na seleção dos especialistas para cada token?
4. Por que o modelo Mixtral 8x7B possui 46,7 bilhões de parâmetros totais e não 56 bilhões, como o nome sugere à primeira vista?
5. Quais são as vantagens de custo e latência proporcionadas pelo MoE durante a inferência em produção?
6. Por que um modelo MoE ainda exige uma quantidade de memória VRAM equivalente à totalidade de seus parâmetros para ser hospedado?
7. Qual desafio de engenharia decorre da necessidade de balanceamento de carga entre os especialistas durante o treinamento?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
