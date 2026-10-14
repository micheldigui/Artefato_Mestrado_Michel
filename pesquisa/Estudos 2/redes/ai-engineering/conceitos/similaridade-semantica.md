# 🧠 Similaridade Semântica (Semantic Similarity)

**Rede:** `ai-engineering`  
areas: `recuperacao-de-informacao`

**Rede:** `ai-engineering`   **Área:** `metricas`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Metodologia de Avaliação
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 132–134

## 📝 Definição

### Definição formal

Uma métrica de avaliação exata baseada em representações vetoriais (*embeddings*) que calcula a proximidade de significado conceitual entre dois textos num espaço latente de alta dimensão.

A **Similaridade Semântica** (*Semantic Similarity* ou *Semantic Textual Similarity* — STS) é a metodologia de avaliação contínua que quantifica o grau de equivalência conceitual, lógica e de significado entre dois textos ou expressões, independentemente de divergências em suas superfícies ortográficas ou escolhas lexicais, computada mediante a transformação prévia de ambas as passagens em vetores densos através de modelos de [[redes/ai-engineering/conceitos/embeddings.md|embeddings]] e posterior mensuração geométrica da proximidade angular desses vetores no espaço latente via **Similaridade de Cosseno**.

### Em linguagem simples

É a técnica de comparar se duas frases significam a mesma coisa, mesmo que utilizem palavras totalmente diferentes, medindo a distância matemática entre os conceitos em um mapa vetorial.

É a métrica que avalia se duas frases dizem a mesma coisa, mesmo usando palavras completamente diferentes. Em vez de ficar contando letras ou palavras repetidas, o sistema traduz cada frase para uma coordenada matemática no espaço dos significados e mede a distância entre essas ideias.

### Escopo e distinções

Diferencia-se da similaridade lexical (como BLEU ou ROUGE), que conta apenas a sobreposição exata de caracteres e palavras individuais independentemente do contexto semântico.

Supera o gargalo estrito da [[redes/ai-engineering/conceitos/similaridade-lexical.md|similaridade lexical]]. Enquanto o BLEU e o ROUGE exigem que as palavras sejam idênticas, métricas semânticas como o **BERTScore** e o **MoverScore** utilizam representações contextuais para identificar que "Como vai você?" e "E aí, tudo bem?" possuem quase 100% de similaridade de significado.

## 🧩 Problema que resolve

Resolve a rigidez das métricas sintáticas que penalizam sinônimos e paráfrases válidas ao comparar respostas geradas por IA contra textos de referência humana (*gabaritos*).

Resolve a miopia das métricas de sobreposição de texto em aplicações de linguagem natural aberta. Permite avaliar tarefas de resposta a perguntas, atendimento ao cliente e sumarização onde o usuário ou modelo expressa fatos legítimos usando sinônimos, alterações de ordem de palavras ou formulações mais concisas que não coincidem com o gabarito original do anotador humano.

## 💡 Intuição

Se você disser "O carro é vermelho" e o modelo gerar "O automóvel tem cor escarlate", uma contagem de palavras exatas dirá que são textos totalmente diferentes, mas a similaridade semântica perceberá que os conceitos apontam para o mesmo significado exato.

Pense em dois navegadores descrevendo uma ilha:

- Um navegador diz: `"A terra em frente é cercada por águas marinhas por todos os lados"`.
- O segundo navegador diz: `"Avistamos uma ilha no horizonte"`.

Um fiscal puramente lexical diria que os marinheiros falaram de coisas distintas porque quase nenhuma palavra coincide. Um geógrafo (**a similaridade semântica**) sabe a definição de "ilha" e percebe que as duas afirmações apontam exatamente para a mesma coordenada geográfica e factual.

## ⚙️ How it works / Como funciona

### Etapas

1. O texto gerado e o texto de referência são convertidos em vetores densos por um modelo de embedding dedicado.
2. Aplica-se a métrica de Similaridade de Cosseno entre os dois vetores resultantes.
3. O valor escalar obtido (entre -1 e 1) indica o grau de proximidade semântica.

### Entradas e saídas

- Entradas: Dois fragmentos de texto (ex: resposta gerada e referência).
- Saídas: Um valor numérico contínuo indicando a proximidade de significado.

## 📐 Formulação matemática

Dada a representação vetorial em embeddings de dois textos como $A$ e $B$, a similaridade de cosseno é calculada por:

$$\text{Similarity}(A, B) = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}}$$

Onde:
- $A \cdot B$: Produto escalar dos vetores.
- $\|A\|$ e $\|B\|$: Normas Euclidianas (comprimentos) dos vetores.

Sejam $A$ e $B$ os vetores de embedding de dimensão $d$ que representam os dois textos. A Similaridade de Cosseno é definida pelo produto escalar dividido pelo produto de suas normas euclidianas ($L_2$):

$$\text{CosineSimilarity}(A, B) = \frac{A \cdot B}{\|A\|_2 \|B\|_2} = \frac{\sum_{i=1}^d A_i B_i}{\sqrt{\sum_{i=1}^d A_i^2} \sqrt{\sum_{i=1}^d B_i^2}}$$

Onde:

- Valor igual a $1$: vetores com orientação angular perfeitamente idêntica (significados idênticos sob o espaço do modelo);
- Valor igual a $0$: vetores ortogonais (conceitos não correlacionados);
- Valor igual a $-1$: vetores diametralmente opostos.

## 🧱 Hipóteses e condições de validade

- Supõe que o modelo de *embedding* utilizado foi treinado adequadamente para capturar o domínio semântico específico dos textos comparados.

- A qualidade e a dimensionalidade do modelo de embedding subjacente determinam o teto de precisão da métrica; se o modelo de embedding for fraco ou descalibrado, textos com significados distintos podem receber vetores próximos.
- Assume que pequenas alterações sintáticas com grande impacto lógico são capturadas pelo embedding (o que nem sempre é verdade para negações sutis).

## ✅ Quando usar

- Na avaliação automatizada de respostas RAG, sumarização e verificação de paráfrases contra textos de referência.

- Avaliação automática contínua de pipelines de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]], medindo a aderência da resposta aos documentos recuperados.
- Agrupamento (*clustering*) e deduplicação de perguntas repetidas de usuários.
- Sistemas de busca, ranqueamento e recuperação semântica de informação.

## 🚫 Quando não usar

- Em tarefas que exigem validação estrita de sintaxe exata de código de programação ou termos legais específicos onde sinônimos alteram totalmente o significado jurídico.

- Tarefas de programação e código-fonte, onde a semântica depende da execução lógica rígida ([[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional]]).
- Casos em que a presença ou ausência de uma palavra de negação minúscula (ex.: "não aprovado" vs. "aprovado") altera 100% o valor do negócio, pois modelos de embedding médios podem atribuir alta similaridade de cosseno a frases opostas que compartilham quase todas as outras palavras.

## ⚠️ Limitações e armadilhas

- Dependência da qualidade do modelo de *embedding* subjacente; se o vetor falhar em capturar a nuance, a similaridade semântica será imprecisa.

- **Custo computacional adicional:** Gerar embeddings densos em tempo real para milhares de textos exige chamadas de GPU adicionais ou faturas de APIs de embedding.
- **A armadilha da negação:** Frases semanticamente antagônicas como `"Vamos comer, vovó"` e `"Vamos comer a vovó"` podem gerar embeddings com alta similaridade de cosseno em certos modelos por compartilharem as mesmas palavras-chave, apesar do sentido totalmente divergente.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[similaridade-semantica|Similaridade Semântica]] | Avaliar proximidade de significado conceitual via vetores. | Dois textos (Gerado + Referência). | Valor contínuo (-1 a 1). | Foca no significado e aceita sinônimos e paráfrases. |
| [[similaridade-lexical|Similaridade Lexical (BLEU)]] | Avaliar sobreposição exata de palavras baseada em n-gramas. | Dois textos (Gerado + Referência). | Pontuação discreta (0 a 1). | Foca na sintaxe estrita e penaliza variação de vocabulário. |

| Dimensão | Similaridade Lexical | Similaridade Semântica |
|---|---|---|
| **Representação dos dados** | Caracteres discretos e n-grams | Vetores contínuos em espaço latente denso |
| **Tolerância a paráfrases** | Nula | Altíssima |
| **Velocidade de cálculo** | Quase instantânea (CPU simples) | Mais lenta (exige inferência de modelo de embedding) |
| **Dependência de modelo** | Nenhuma (função matemática pura) | Totalmente dependente do modelo de embedding escolhido |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Comparar a frase do aluno "A capital da Itália é Roma" com a frase gabarito "Roma é a capital italiana": a similaridade lexical falharia em dar nota máxima, mas a similaridade semântica atribuirá um valor próximo de 1.0 por reconhecer a identidade conceitual.

O usuário pergunta a um bot de atendimento: `"Qual é o valor da assinatura?"`. O banco de suporte contém a resposta canônica de referência: `"A mensalidade custa vinte reais"`.
O modelo gera como resposta: `"O plano sai por R$ 20,00 por mês"`.

- O cálculo de sobreposição lexical (ROUGE) falha porque "plano", "sai", "R$" e "mês" não aparecem na referência.
- O pipeline de **Similaridade Semântica** converte ambas as frases em vetores de 1536 dimensões via modelo de embedding. O cálculo de cosseno entre os dois vetores atinge $0{,}94$, permitindo ao pipeline aprovar automaticamente a resposta da IA como correta.

## 🔗 Relações no grafo

### Pré-requisitos

- [[modelo-de-fundacao|Modelo de Fundação]]

- [[redes/ai-engineering/conceitos/embeddings.md|Embeddings]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[rag|RAG]]

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

- [[redes/ai-engineering/conceitos/similaridade-lexical.md|Similaridade Lexical]]
- [[redes/ai-engineering/conceitos/correcao-funcional.md|Correção Funcional (pass@k)]]

### Conceitos relacionados

- [[ai-as-a-judge|IA como Juiz]]

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Metodologia de Avaliação
- **Localização:** localização não informada no material recebido
- **Evidência:** Descrição da similaridade semântica baseada em embeddings e similaridade de cosseno como alternativa robusta às métricas lexicais.
- **Confiança:** alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 132–134
- **Evidência:** Chip Huyen formaliza a similaridade semântica através de embeddings e similaridade de cosseno, citando ferramentas como BERTScore e MoverScore e contrapondo-a aos limites das métricas lexicais com o exemplo de frases como "Let's eat, grandma" e "Let's eat grandma".
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Similaridade Semântica?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

1. O que é Similaridade Semântica e como ela supera as deficiências fundamentais das métricas lexicais como BLEU?
2. Como a Similaridade de Cosseno utiliza a geometria vetorial para mensurar a proximidade conceitual entre dois textos?
3. O que é o BERTScore e como ele combina alinhamento de tokens com representações densas contextuais?
4. Por que duas frases com significados diametralmente opostos baseadas em negações simples podem receber pontuações de similaridade semântica enganosamente altas?
5. Qual é o papel da dimensionalidade do vetor de embedding na capacidade de resolução da similaridade semântica?
6. De que maneira o cálculo de similaridade semântica é utilizado como bloco funcional no padrão arquitetural de RAG?
7. Quais são as desvantagens operacionais em termos de custo e latência ao adotar similaridade semântica em relação ao casamento exato de strings?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 3 — Metodologia de Avaliação. A interpretação final deve ser revisada pelo estudante.*

## ⚙️ Como funciona

O procedimento opera combinando codificadores neurais densos com funções de distância vetorial:

### Etapas

1. **Ingestão dos pares de texto:** Recebe a resposta gerada pelo modelo candidato ($A$) e o texto de referência ou consulta ($B$).
2. **Geração de Embeddings:** Passa ambos os textos pelo mesmo modelo especializado de embedding (ex.: BERT, Sentence-Transformers, OpenAI text-embedding-3), gerando dois vetores densos $v_A, v_B \in \mathbb{R}^d$.
3. **Cálculo Angular de Proximidade:** Computa-se o produto escalar normalizado entre os dois vetores (**Similaridade de Cosseno**).
4. **Alinhamento contextual de tokens (BERTScore):** Em variantes avançadas como o BERTScore, em vez de um único vetor médio por frase, calcula-se a similaridade de cosseno máxima entre cada token do texto candidato e os tokens do texto de referência, combinando precisão e revocação semântica ponderada.
5. **Emissão do Escore:** Retorna um valor no intervalo de $[-1, 1]$ (frequentemente normalizado para $[0, 1]$).

### Entradas e saídas

- **Entradas:** Texto de saída do modelo e texto de referência (ou par de textos para comparação).
- **Saídas:** Escore escalar contínuo representando a proximidade conceitual.
