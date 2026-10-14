# 🧠 Similaridade Lexical

**Rede:** `ai-engineering`   **Área:** `metricas`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 130–132

## 📝 Definição

### Definição formal

A **Similaridade Lexical** (*Lexical Similarity*) é a classe de métricas determinísticas e exatas de avaliação de texto que quantifica o grau de sobreposição superficial, coincidência de caracteres e correspondência de subsequências de palavras (**n-grams**) ou distância de edição entre a resposta gerada por um modelo e um ou mais textos canônicos de referência (*ground truths*) fornecidos por humanos. 

As métricas canônicas incluem **BLEU** (baseada em precisão de n-grams modificada, clássica em tradução automática), **ROUGE** (baseada em revocação/recall da maior subsequência comum, clássica em sumarização) e métricas de distância de edição (*Fuzzy Matching*).

### Em linguagem simples

É a conferência mecânica de palavras iguais. O algoritmo pega a resposta que a IA escreveu e compara com a resposta de um humano, contando quantas palavras e pares de palavras são exatamente idênticos. Se o humano escreveu "O carro é veloz" e a IA escreveu "O carro é rápido", a métrica lexical penaliza a IA porque as letras das palavras "veloz" e "rápido" não combinam no papel, ignorando que o sentido é o mesmo.

### Escopo e distinções

Diferencia-se da [[redes/ai-engineering/conceitos/similaridade-semantica.md|similaridade semântica]], que analisa o significado conceitual das frases por meio de vetores densos. A similaridade lexical analisa estritamente a forma ortográfica e posicional dos caracteres e palavras.

## 🧩 Problema que resolve

Resolveu historicamente a necessidade de ter métricas automáticas, baratas, determinísticas e instantâneas para acompanhar o progresso de modelos de tradução automática e sumarização nas décadas de 2000 e 2010, dispensando a contratação contínua de tradutores humanos para cada época de treino.

## 💡 Intuição

Pense em um corretor de provas antiquado que usa um gabarito de papel perfurado sobre uma redação. Ele só dá nota se a palavra escrita pelo aluno coincidir exatamente com os orifícios do gabarito. Se o aluno expressar a mesma ideia genial usando um vocabulário mais rico ou uma estrutura de orações ligeiramente invertida, o gabarito perfurado não encaixa e o aluno recebe nota zero.

## ⚙️ Como funciona

O cálculo opera sobre conjuntos ou sequências de tokens decompostos:

### Etapas

1. **Tokenização e normalização:** Tanto a resposta gerada quanto a referência são fatiadas em palavras, pontuações são tratadas e caracteres convertidos para minúsculas.
2. **Extração de N-grams:** Decompõe-se o texto em blocos de $n$ palavras adjacentes (unigramas: 1 palavra; bigramas: pares de palavras; trigramas: trios).
3. **Contagem de sobreposição:**
   - No **BLEU (Precisão):** Conta-se quantos n-grams gerados pelo modelo aparecem na referência humana, aplicando um teto para evitar repetições enganosas (*clipped precision*) e uma penalidade de brevidade caso a resposta seja curta demais.
   - No **ROUGE (Revocação):** Conta-se quantos n-grams da referência humana foram capturados com sucesso pela resposta do modelo (ex.: ROUGE-L mede a Maior Subsequência Comum).
4. **Cálculo da pontuação:** Produz um escore numérico entre 0 e 1 (ou 0 a 100).

### Entradas e saídas

- **Entradas:** Texto de saída gerado pelo modelo e uma lista de textos de referência humana.
- **Saídas:** Escore numérico determinístico contínuo refletindo a taxa de sobreposição lexical.

## 📐 Formulação matemática

No cálculo da precisão de $n$-gramas modificada $p_n$ do BLEU:

$$p_n = \frac{\sum_{C \in \{\text{Candidatos}\}} \sum_{n\text{-gram} \in C} \text{Count}_{\text{clip}}(n\text{-gram})}{\sum_{C' \in \{\text{Candidatos}\}} \sum_{n\text{-gram}' \in C'} \text{Count}(n\text{-gram}')}$$

A pontuação final do **BLEU** combina a média geométrica das precisões de 1-grama até 4-gramas com uma penalidade de brevidade ($\text{BP}$):

$$\text{BLEU} = \text{BP} \cdot \exp\left( \sum_{n=1}^4 w_n \ln p_n \right), \quad \text{onde } \text{BP} = \begin{cases} 1, & \text{se } c > r \\ \exp(1 - r/c), & \text{se } c \le r \end{cases}$$

Onde $c$ é o comprimento da resposta gerada e $r$ é o comprimento da referência humana mais próxima.

## 🧱 Hipóteses e condições de validade

- Assume que a qualidade de uma resposta correlaciona-se com a frequência de palavras idênticas usadas pelo redator humano da referência.
- Exige que o conjunto de referências humanas seja extenso e diversificado; se houver apenas uma referência, qualquer variação estilística legítima é penalizada.

## ✅ Quando usar

- Linhas de base históricas rápidas em tarefas tradicionais de tradução literal de idiomas com sintaxe próxima.
- Tarefas estritamente extrativas onde o texto deve copiar trechos literais de uma lei ou norma regulatória.

## 🚫 Quando não usar

- Avaliação de chatbots conversacionais, agentes autônomos, redação criativa ou respostas abertas de modelos de fundação modernos.
- Avaliação de código-fonte (onde a [[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional]] via testes de execução é obrigatória).

## ⚠️ Limitações e armadilhas

- **Penalização de sinônimos e paráfrases:** Respostas brilhantes que usam palavras mais elegantes ou diretas do que o anotador humano original recebem notas baixas.
- **Vulnerabilidade a referências humanas medíocres:** O capítulo cita o caso da competição WMT 2023, onde muitas traduções de referência humana continham erros graves de gramática, distorcendo os escores das IAs.
- **Caso Fuyu da Adept:** O modelo gerou a legenda correta para uma imagem, mas tirou nota baixa porque o benchmark só tinha 3 frases humanas cadastradas que usavam palavras diferentes.

## 🔍 Comparações

| Característica | BLEU | ROUGE | Similaridade Semântica (Embeddings) |
|---|---|---|---|
| **Foco principal** | Precisão (o que o modelo gerou está na referência?) | Revocação (o modelo capturou o que estava na referência?) | Significado conceitual e semântica latente |
| **Tarefa histórica** | Tradução Automática | Sumarização de Documentos | Recuperação em RAG e avaliação aberta |
| **Tolerância a sinônimos** | Nula (apenas correspondência exata de tokens) | Nula (apenas correspondência exata de tokens) | Altíssima (sinônimos têm vetores próximos) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Considere a referência humana: `"A paciente relatou cefaleia intensa e febre alta"`.
O modelo de fundação gera a resposta: `"A mulher descreveu forte dor de cabeça e temperatura corporal elevada"`.

- Um médico humano avalia a resposta como $100\%$ correta clinicamente.
- O cálculo de **Similaridade Lexical (BLEU)** avalia: a palavra `"mulher"` não está na referência (era `"paciente"`), `"descreveu"` não está (era `"relatou"`), `"forte dor de cabeça"` não combina com `"cefaleia intensa"` e `"temperatura corporal elevada"` não bate com `"febre alta"`. O BLEU desmorona para um valor próximo de zero, penalizando uma resposta clinicamente impecável.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/similaridade-semantica.md|Similaridade Semântica]]

### Alternativas

- [[redes/ai-engineering/conceitos/correcao-funcional.md|Correção Funcional (pass@k)]]
- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 130–132
- **Evidência:** Chip Huyen discute métricas lexicais baseadas em n-grams e distância de edição (BLEU, ROUGE, METEOR++), ilustrando a falha do modelo visual Fuyu que recebeu escore baixo por limitação das referências e citando a decadência dessas métricas na era dos LLMs.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Similaridade Lexical e quais são as métricas estatísticas mais representativas dessa abordagem?
2. Qual é a distinção matemática central entre o foco do BLEU (precisão) e o foco do ROUGE (revocação)?
3. Por que métricas como BLEU e ROUGE entraram em desuso na avaliação de modelos de fundação generativos modernos?
4. Como o exemplo do modelo Fuyu ilustra o risco de se utilizar conjuntos de referências humanas limitados para avaliar descrições abertas?
5. Qual é o motivo pelo qual um modelo pode obter alta similaridade lexical em uma tarefa de código e, ainda assim, gerar uma função completamente quebrada?
6. O que é a penalidade de brevidade (*brevity penalty*) na formulação formal do BLEU e qual problema ela evita?
7. Em quais tarefas residuais específicas da engenharia de software a similaridade lexical ainda pode fornecer linhas de base aceitáveis?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
