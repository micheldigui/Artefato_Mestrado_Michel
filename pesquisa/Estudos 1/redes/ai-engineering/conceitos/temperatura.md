# 🧠 Temperatura

**Rede:** `ai-engineering`  
**Área:** `amostragem-estocastica`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Entendendo Modelos de Fundação
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

Um hiperparâmetro de amostragem que dimensiona os valores de logits gerados por um modelo de linguagem antes da aplicação da função Softmax, controlando a nitidez ou a suavidade da distribuição de probabilidade resultante.

### Em linguagem simples

É o botão de controle de criatividade da IA: valores próximos de zero tornam a IA previsível e literal, enquanto valores altos a tornam criativa e imprevisível.

### Escopo e distinções

Atua diretamente sobre a distribuição estatística de escolha do próximo token, diferenciando-se de filtros de corte absoluto como Top-k e Top-p.

## 🧩 Problema que resolve

Resolve a rigidez excessiva de modelos estritamente determinísticos (*greedy decoding*), permitindo calibrar o nível de variedade e criatividade nas respostas geradas.

## 💡 Intuição

Pense na temperatura de um sistema físico: partículas frias ficam paradas e previsíveis em um único lugar, enquanto partículas aquecidas ganham energia térmica e espalham-se de maneira caótica por todo o ambiente.

## ⚙️ Como funciona

### Etapas

1. O modelo calcula os logits brutos para cada token do vocabulário.
2. Cada logit é dividido pelo valor do hiperparâmetro de temperatura $T$.
3. Aplica-se a função Softmax sobre os logits escalados para obter as probabilidades ajustadas.
4. O próximo token é amostrado com base nessa nova distribuição.

### Entradas e saídas

- Entradas: Vetor de logits brutos e valor numérico de temperatura $T$.
- Saídas: Nova distribuição de probabilidade ajustada para amostragem.

## 📐 Formulação matemática

Dado um logit $x_i$ e uma temperatura $T > 0$, o logit ajustado $z_i$ e a probabilidade resultante $p_i$ são calculados por:

$$z_i = \frac{x_i}{T}, \quad p_i = \frac{e^{z_i}}{\sum_{j} e^{z_j}}$$

Onde:
- $x_i$: Logit original do token $i$.
- $T$: Parâmetro de temperatura.
- Conforme $T \to 0$, a distribuição aproxima-se de uma escolha determinística (*argmax*).
- Conforme $T \to \infty$, a distribuição aproxima-se de uma escolha totalmente uniforme.

## 🧱 Hipóteses e condições de validade

- Requer acesso direto aos logits brutos da camada final do modelo.

## ✅ Quando usar

- Em tarefas criativas, geração de histórias e *brainstorming* (temperatura alta, ex: 0.7); ou em tarefas estritas de código, extração de dados e matemática (temperatura próxima de 0).

## 🚫 Quando não usar

- Em tarefas que exigem determinismo lógico e exatidão absoluta (como consultas SQL ou cálculos financeiros) com temperatura alta.

## ⚠️ Limitações e armadilhas

- Temperaturas excessivamente altas geram textos incoerentes, com repetições e quebras gramaticais severas ("alucinações estocásticas").

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[temperatura|Temperatura]] | Dimensionar logits para modular criatividade e estocasticidade. | Logits brutos + Valor de $T$. | Probabilidades ajustadas. | Altera a escala de toda a distribuição de logits. |
| [[top-k-e-top-p|Top-k / Top-p]] | Filtrar o conjunto de candidatos viáveis cortando caudas improváveis. | Probabilidades / Logits. | Subconjunto restrito de tokens elegíveis. | Realiza corte estrutural de candidatos com base em quantidade ou cumulatividade. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Se você perguntar "Qual a capital da França?", com temperatura 0 a IA responde sempre "Paris". Com temperatura 1.5, ela pode começar a inventar nomes exóticos ou divagar sobre a culinária francesa de forma imprevisível.

## 🔗 Relações no grafo

### Pré-requisitos

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Complementos

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Alternativas

- [[top-k-e-top-p|Top-k e Top-p]]

### Conceitos relacionados

- [[modelo-de-fundacao|Modelo de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Entendendo Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da matemática da temperatura e seu impacto de remapeamento sobre os logits antes da Softmax.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que é Temperatura?
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
