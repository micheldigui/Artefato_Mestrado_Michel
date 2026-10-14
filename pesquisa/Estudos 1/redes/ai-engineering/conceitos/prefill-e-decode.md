# 🧠 Prefill e Decode

**Rede:** `ai-engineering`  
**Área:** `otimizacao-de-inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Entendendo Modelos de Fundação
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

As duas fases computacionais distintas que compõem o ciclo de inferência de um modelo de linguagem autoregressivo: o *Prefill* (processamento paralelo da entrada) e o *Decode* (geração sequencial iterativa de saída).

### Em linguagem simples

O ciclo de inferência da IA divide-se em dois momentos: primeiro ela lê toda a sua pergunta de uma vez só bem rápido (*Prefill*), e depois ela escreve a resposta palavra por palavra de forma mais lenta (*Decode*).

### Escopo e distinções

Diferenciam-se fundamentalmente pelo perfil de carga de hardware: o *Prefill* é limitado por poder de cálculo aritmético (*compute-bound*), enquanto o *Decode* é limitado pela largura de banda de memória (*memory-bandwidth bound*).

## 🧩 Problema que resolve

Explica o comportamento de latência assimétrica em modelos gerativos, permitindo que arquiteturas de servidores de IA otimizem recursos computacionais de forma separada para leitura de prompts e geração de tokens.

## 💡 Intuição

Pense em um estudante lendo uma questão de prova complexa (ele lê o enunciado inteiro de um golpe só de forma rápida) e depois redigindo a redação dissertativa resposta por resposta, palavra por palavra, olhando pausadamente para o manual de consulta.

## ⚙️ Como funciona

### Etapas

1. **Prefill:** Todos os tokens do prompt de entrada são passados simultaneamente pela rede neural para calcular e popular o cache de atenção inicial (*KV Cache*).
2. **Decode:** O modelo prediz o primeiro token subsequente, anexa-o ao contexto, e repete o processo iterativamente, gerando um token por vez de forma autoregressiva até encontrar o marcador de parada (*EOS*).

### Entradas e saídas

- Entradas: Prompt textual inicial do usuário.
- Saídas: Geração sequencial de tokens de resposta preenchendo o fluxo de saída.

## 📐 Formulação matemática

Não possui uma equação isolada própria, sendo caracterizada pelas restrições de complexidade de hardware:
- *Prefill:* Operações matriciais densas em paralelo de custo $O(N^2)$ onde $N$ é o tamanho do prompt.
- *Decode:* Passagens iterativas sequenciais limitadas pela taxa de transferência de memória $M$ dos pesos do modelo:

$$\text{Tempo}_{\text{decode}} \propto \text{Tamanho dos Pesos} / \text{Largura de Banda de Memória}$$

## 🧱 Hipóteses e condições de validade

- Requer suporte a alocação dinâmica de memória em GPU para gerenciar o crescimento sequencial do cache de atenção durante a fase de decodificação.

## ✅ Quando usar

- No projeto e dimensionamento de servidores de inferência de modelos de linguagem para equilibrar métricas de TTFT (*Time to First Token*) e TPOT (*Time per Output Token*).

## 🚫 Quando não usar

- Não aplicável em modelos discriminativos puros que não geram texto de forma autoregressiva sequencial.

## ⚠️ Limitações e armadilhas

- Como o *Decode* é limitado pela largura de banda de memória, adicionar usuários simultâneos sem técnicas avançadas de loteamento (*batching*) degrada severamente a velocidade de escrita por token.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[prefill-e-decode|Prefill]] | Processar o prompt de entrada de forma paralela. | Sequência completa do prompt. | Estados iniciais e *KV Cache* populado. | Operação paralela intensiva em computação (*compute-bound*). |
| [[prefill-e-decode|Decode]] | Gerar tokens de resposta de forma iterativa sequencial. | Contexto acumulado atual. | Um único token gerado por ciclo. | Operação sequencial iterativa limitada por memória (*memory-bandwidth bound*). |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Quando você envia uma pergunta de 500 palavras para o ChatGPT, a resposta inicial demora um segundo para começar (*Prefill*), mas assim que começa, as palavras aparecem em sequência contínua na tela (*Decode*).

## 🔗 Relações no grafo

### Pré-requisitos

- [[mecanismo-de-atencao|Mecanismo de Atenção]]

### Complementos

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- [[modelo-de-fundacao|Modelo de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Entendendo Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Descrição das fases de pré-preenchimento e decodificação autoregressiva e seus respectivos impactos de gargalo computacional.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que são Prefill e Decode?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 2 — Entendendo Modelos de Fundação. A interpretação final deve ser revisada pelo estudante.*
