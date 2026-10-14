# 🧠 Paradoxo de Simpson

**Rede:** `ai-engineering`  
**Área:** `estatistica-e-avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 4 — Avaliando Sistemas de IA
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

Um fenômeno estatístico no qual uma tendência aparente presente em diversos grupos de dados combinado desaparece ou se inverte quando esses grupos são analisados de forma desagregada (*slicing*).

### Em linguagem simples

É a ilusão matemática em que um modelo parece ser o melhor na média geral de uma tabela, mas quando você divide os dados por categorias específicas, o concorrente é melhor em *todas* as categorias individuais.

### Escopo e distinções

Trata-se de um viés analítico de agregação de métricas, aplicável a qualquer pipeline de teste estatístico ou avaliação de aprendizado de máquina.

## 🧩 Problema que resolve

Evita que engenheiros tomem decisões comerciais ou técnicas equivocadas ao escolherem um modelo de IA inferior com base em escores globais agregados mal interpretados.

## 💡 Intuição

Imagine dois hospitais: o Hospital A parece ter uma taxa de mortalidade pior na média geral. Contudo, ao separar os dados entre "pacientes graves" e "pacientes leves", descobre-se que o Hospital A atende muito mais casos graves e é o melhor em ambas as categorias. A média geral agregada escondia a realidade.

## ⚙️ Como funciona

### Etapas

1. O avaliador calcula a acurácia global agregada de dois modelos de IA (ex: Modelo A = 78%, Modelo B = 83%).
2. Aplica-se a técnica de *Slicing* (recorte de dados), separando o conjunto de testes por subcategorias (ex: perguntas curtas vs. longas, ou usuários de diferentes países).
3. Observa-se que o Modelo A tem escore superior em *todas* as fatias individuais isoladas, revelando a inversão estatística do Paradoxo de Simpson.

### Entradas e saídas

- Entradas: Métricas agregadas de teste e subconjuntos segmentados por fatias (*slices*).
- Saídas: Diagnóstico de inversão de tendência estatística.

## 📐 Formulação matemática

Seja $P(Y \mid X)$ a probabilidade agregada de sucesso e $P(Y \mid X, Z_k)$ a probabilidade condicionada a uma subcategoria $Z_k$. O paradoxo formaliza-se quando:

$$P(Y \mid X_1) > P(Y \mid X_2) \quad \text{mas} \quad P(Y \mid X_1, Z_k) < P(Y \mid X_2, Z_k) \quad \forall k$$

Onde:
- $X_1, X_2$: Modelos ou abordagens comparadas.
- $Z_k$: Subcategorias de fatiamento de dados (*slicing*).

## 🧱 Hipóteses e condições de validade

- Requer que o conjunto de teste seja segmentável em subgrupos representativos independentes para destilação analítica correta.

## ✅ Quando usar

- Na auditoria de resultados de desempenho de modelos antes de aprovar atualizações críticas em produção.

## 🚫 Quando não usar

- Em análises exploratórias de nível macro onde o detalhamento de subgrupos seja irrelevante para o escopo do problema.

## ⚠️ Limitações e armadilhas

- Ignorar o fatiamento de dados (*slicing*) pode levar a implantações de modelos enviesados que prejudicam subgrupos específicos de usuários sem que a média geral perceba.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[paradoxo-de-simpson|Paradoxo de Simpson]] | Explicar a inversão de tendências estatísticas ao desagregar dados. | Métricas agregadas vs. Segmentadas. | Alerta de viés de agregação. | Revela falhas ocultas em médias globais através de fatiamento (*slicing*). |
| [[slicing-de-dados|Fatiamento de Dados (Slicing)]] | Recortar o dataset em subgrupos para análise granular. | Dataset completo + Critérios de corte. | Subconjuntos de teste isolados. | Ferramenta prática para inspecionar e evitar distorções estatísticas. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O Modelo A tem 78% de acurácia geral e o Modelo B tem 83%. Parece que o B é melhor. Mas ao fatiar por idioma, o Modelo A tem 93% em inglês e 73% em espanhol, enquanto o B tem 87% em inglês e 69% em espanhol. O Modelo A vence em ambos os idiomas individualmente, mas perde na média por causa do volume de dados em espanhol.

## 🔗 Relações no grafo

### Pré-requisitos

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Complementos

- [[desenvolvimento-orientado-por-avaliacao|Desenvolvimento Orientado por Avaliação]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- [[contaminacao-de-dados|Contaminação de Dados]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 4 — Avaliando Sistemas de IA
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação do Paradoxo de Simpson e da importância crítica do fatiamento de dados (*slicing*) na avaliação de modelos.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que é o Paradoxo de Simpson?
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
*Nota gerada a partir do capítulo Capítulo 4 — Avaliando Sistemas de IA. A interpretação final deve ser revisada pelo estudante.*
