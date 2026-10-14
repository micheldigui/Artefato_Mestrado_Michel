# 🧠 Busca Híbrida (*Hybrid Search*)

**Rede:** `ai-engineering`  
**Área:** `recuperacao-de-informacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG e Agentes
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

Uma estratégia de recuperação de informação que combina a busca baseada em termos lexicais (*keyword/BM25*) com a busca baseada em vetores semânticos (*embedding-based/vector search*), unificando os resultados através de algoritmos de fusão de ranqueamento.

### Em linguagem simples

É a união de dois mundos na busca: o "Ctrl+F" tradicional (que acha códigos exatos, siglas e números de série) com a busca por inteligência semântica (que acha ideias e sinônimos).

### Escopo e distinções

Diferencia-se da busca estritamente vetorial ou estritamente lexical ao explorar simultaneamente a exatidão de termos exatos e a flexibilidade conceitual de significados.

## 🧩 Problema que resolve

Resolve a falha onde buscas estritamente semânticas perdem códigos específicos (como números de peças ou erros de sistema) e buscas lexicais falham ao não entender sinônimos ou intenções conceituais do usuário.

## 💡 Intuição

Imagine procurar um livro em uma livraria: a busca lexical age como procurar o título exato na etiqueta impressa, enquanto a busca semântica age como descrever a história do livro para o atendente encontrar algo com o mesmo tema. Juntas, as chances de acerto são máximas.

## ⚙️ Como funciona

### Etapas

1. A consulta do usuário é enviada em paralelo para o recuperador lexical (ex: BM25) e para o recuperador vetorial semântico.
2. Cada recuperador retorna sua própria lista ordenada de documentos mais relevantes.
3. Utiliza-se um algoritmo de fusão (como o *Reciprocal Rank Fusion - RRF*) para combinar as pontuações e posições das duas listas.
4. Uma única lista unificada e otimizada de documentos é entregue ao pipeline de geração (*RAG*).

### Entradas e saídas

- Entradas: Consulta de texto do usuário e base de dados indexada lexical e vetorialmente.
- Saídas: Lista unificada de documentos recuperados por relevância combinada.

## 📐 Formulação matemática

O algoritmo de fusão *Reciprocal Rank Fusion* (RRF) calcula a pontuação unificada de um documento $d$ somando as inversas de suas posições ($r_i$) nas diferentes listas de recuperação:

$$\text{RRF\_Score}(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$

Onde:
- $M$: Conjunto de sistemas de recuperação utilizados (ex: léxico e vetorial).
- $r_m(d)$: Posição (*rank*) do documento $d$ no sistema $m$.
- $k$: Constante de suavização (tipicamente fixada em 60).

## 🧱 Hipóteses e condições de validade

- Supõe que a base de dados possui suporte simultâneo a índices textuais invertidos e armazenamento vetorial.

## ✅ Quando usar

- Em sistemas de RAG corporativos de alta exigência onde os usuários buscam tanto termos técnicos exatos quanto conceitos conceituais vagos.

## 🚫 Quando não usar

- Em ambientes com recursos de infraestrutura extremamente limitados que suportem apenas um tipo de índice de busca simples.

## ⚠️ Limitações e armadilhas

- Aumenta a complexidade operacional da arquitetura de dados e exige ajuste fino (*tuning*) dos pesos de combinação entre as buscas.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[busca-hibrida|Busca Híbrida]] | Unificar busca lexical exata e busca vetorial semântica. | Consulta do usuário. | Lista unificada de documentos ranqueados. | Combina o melhor dos dois mundos (precisão de termos + contexto conceitual). |
| [[busca-vetorial|Busca Vetorial Pura]] | Encontrar documentos por proximidade de significado vetorial. | Vetor de embedding da consulta. | Lista de documentos por similaridade de cosseno. | Cega a termos exatos, siglas e códigos literais isolados. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um engenheiro busca no manual: "Erro EADDRNOTAVAIL (99)". A busca lexical acha o código exato do erro no manual técnico, enquanto a busca semântica acha parágrafos que falam sobre problemas de conexão de rede. A busca híbrida une ambos e traz o guia perfeito.

## 🔗 Relações no grafo

### Pré-requisitos

- [[geracao-aumentada-de-recuperacao-rag|Geração Aumentada de Recuperação (RAG)]]

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG e Agentes
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da busca híbrida e do algoritmo Reciprocal Rank Fusion (RRF) para otimização de recuperação em RAG.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que é Busca Híbrida (Hybrid Search)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Когда usar / Quando usar?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 6 — RAG e Agentes. A interpretação final deve ser revisada pelo estudante.*
