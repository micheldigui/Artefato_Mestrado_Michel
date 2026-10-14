# 🧠 Diretrizes e Rubricas de Avaliação

**Rede:** `ai-engineering`  
**Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 4 — Evaluate AI Systems
- Localização: Páginas 202–204

## 📝 Definição

### Definição formal

As **Diretrizes e Rubricas de Avaliação** (*Evaluation Guidelines and Scoring Rubrics*) constituem o arcabouço normativo, formal e operacional que padroniza o julgamento qualitativo de saídas gerativas em um pipeline de Engenharia de IA. Uma rubrica define explicitamente:
1. Os critérios semânticos a serem observados (ex.: relevância, fidelidade, tom de voz);
2. A escala de classificação utilizada (booleana, categórica ou discreta ordinal de 1 a 5);
3. As condições determinantes exatas que justificam a atribuição de cada nota, acompanhadas de exemplos concretos (*few-shot*) representativos de cada faixa da escala;
4. O mapeamento formal entre os índices técnicos obtidos e o **Limiar de Utilidade** (*Usefulness Threshold*), que expressa o patamar mínimo de qualidade que o sistema precisa atingir para gerar valor real às métricas de negócio.

### Em linguagem simples

É o livro de regras detalhado que explica o que é uma resposta boa e o que é uma resposta ruim. Em vez de dizer para um avaliador (humano ou IA) "dê uma nota de 1 a 5 para a resposta", a rubrica descreve exatamente: "Dê nota 1 se a IA inventou dados; dê nota 3 se ela acertou os fatos, mas foi prolixa; dê nota 5 se ela foi concisa, precisa e citou a fonte". Ela estabelece também que, se a IA não tirar média 4, o projeto é cancelado porque não serve para a empresa.

### Escopo e distinções

Não se restringe a instruções para humanos. A mesma diretriz e rubrica elaborada nesta fase do pipeline é posteriormente reaproveitada no prompt de [[redes/ai-engineering/conceitos/ia-como-juiz.md|juízes de IA]] e como especificação de anotação de dados para futuro [[redes/ai-engineering/conceitos/ajuste-fino.md|ajuste fino (finetuning)]].

## 🧩 Problema que resolve

Resolve a ambiguidade e a variância caótica de avaliação. Uma resposta correta nem sempre é uma resposta boa (como o caso citado no livro de um assistente de carreira do LinkedIn que responde para um candidato: `"Você é um candidato horrível para essa vaga"` — a resposta pode ser factualmente verdadeira pelos requisitos, mas é inaceitável como produto). Rubricas definem o que é utilidade real para o usuário final.

## 💡 Intuição

Pense nos critérios de correção da redação do ENEM:
- Os milhares de corretores humanos espalhados pelo país não dão notas com base no que "sentem no coração" ao ler o texto.
- Eles seguem uma folha de critérios estrita dividida em 5 competências (domínio da norma padrão, compreensão da proposta, organização de argumentos, coesão e proposta de intervenção). Cada competência tem descrições exatas do que vale 40, 80, 120, 160 ou 200 pontos. Essa rubrica padronizada é o que permite calibrar a nota entre milhões de alunos.

## ⚙️ Como funciona

O desenvolvimento da diretriz estrutura-se em quatro ações interdependentes:

### Etapas

1. **Definição de Critérios:** Selecionam-se poucos critérios essenciais para o caso (o relatório da LangChain citado no livro revela que empresas utilizam em média 2,3 critérios por produto, como *relevância* e *fidelidade*).
2. **Definição do Sistema de Pontuação:** Escolhe-se a escala matemática:
   - Booleana ($0$ ou $1$);
   - Ternária ($-1$ contradição, $0$ neutro, $+1$ implicação);
   - Discreta de 1 a 5 (evitando escalas contínuas excessivamente amplas como 1 a 100, onde LLMs perdem consistência de julgamento).
3. **Redação da Rubrica com Exemplos:** Escreve-se o comportamento de cada nota com exemplos contrabalançados. A rubrica deve estipular tanto o que o modelo **deve** fazer quanto o que ele **não deve** fazer (como responder perguntas fora de escopo).
4. **Vinculação a Métricas de Negócio:** Constrói-se a tabela de conversão operacional:
   - Exemplo: Factualidade de $80\% \implies$ automação de apenas $30\%$ dos chamados;
   - Factualidade de $98\% \implies$ automação de $90\%$ dos chamados.
5. **Fixação do Limiar de Utilidade (*Usefulness Threshold*):** Determina-se a linha de corte mínima de viabilidade (ex.: consistência factual $< 85\%$ impede o lançamento em produção).

### Entradas e saídas

- **Entradas:** Requisitos de produto, metas de redução de custo ou eficiência operacional e exemplos de falhas históricas.
- **Saídas:** Documento canônico de diretriz de avaliação, prompts de juiz parametrizados e metas contratuais de homologação.

## 📐 Formulação matemática

O mapeamento entre a métrica técnica média da rubrica $\bar{S}_{\text{rubrica}} \in [1, 5]$ e a métrica de negócio $B$ (ex.: taxa de retenção ou tickets resolvidos) é modelado por uma função monotônica não linear:

$$B = g(\bar{S}_{\text{rubrica}}), \quad \text{onde } \frac{dB}{d\bar{S}} > 0$$

O **Limiar de Utilidade** $\tau_{\text{utilidade}}$ é o valor crítico no qual o retorno de negócio supera os custos operacionais da infraestrutura:

$$\tau_{\text{utilidade}} = \inf \Big\{ s \in [1, 5] \;\Big|\; g(s) \cdot V_{\text{ticket}} - C_{\text{inferência}} > 0 \Big\}$$

## 🧱 Hipóteses e condições de validade

- A rubrica deve ser testada e validada primeiro com humanos: se dois engenheiros da equipe não conseguirem concordar na nota atribuída a um exemplo com base na rubrica, ela deve ser reescrita até eliminar a ambiguidade antes de ser automatizada.

## ✅ Quando usar

- Componente fundamental do Passo 2 de qualquer pipeline de [[redes/ai-engineering/conceitos/desenvolvimento-orientado-por-avaliacao.md|Desenvolvimento Orientado por Avaliação (EDD)]].
- Na concepção de diretrizes para rotuladores terceirizados e calibração de modelos juízes.

## 🚫 Quando não usar

- Em métricas puramente exatas que dependem de compiladores determinísticos ([[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional de código]]), onde a saída é regida por testes de asserção binária direta.

## ⚠️ Limitações e armadilhas

- **Rubricas excessivamente vagas:** Instruir o avaliador a dar nota baixa se o texto "não for bom".
- **Desconexão com o negócio:** Focar em atingir nota 5 em criatividade literária quando o objetivo da empresa é reduzir o tempo de leitura do cliente através de concisão extrema.

## 🔍 Comparações

| Tipo de Escala | Facilidade de Uso por IA | Consistência de Calibração | Cenário Indicado |
|---|---|---|---|
| **Booleana (0 / 1)** | Máxima | Altíssima | Conformidade de formato, ausência de PII |
| **Ordinal (1 a 5)** | Alta | Moderada a Alta (com rubrica sólida) | Relevância, tom de voz, completude |
| **Contínua (0 a 100)** | Baixíssima | Pobre (LLMs hesitam entre 78 e 82) | Evitar em juízes de IA |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma empresa de seguros cria uma rubrica para o critério "Clareza de Exclusão de Cobertura":
- **Nota 1:** A IA não menciona as regras de exclusão ou diz que tudo está coberto.
- **Nota 2:** A IA menciona que há exclusões, mas não explica quais são.
- **Nota 3:** A IA lista as exclusões em linguagem jurídica cifrada sem explicar o impacto ao cliente.
- **Nota 4:** A IA lista as exclusões em linguagem simples, mas deixa dúvidas sobre prazos.
- **Nota 5:** A IA lista as exclusões em tópicos, traduz o jargão para português simples e aponta o artigo exato da apólice.
Com essa rubrica no prompt da IA juiz, todas as 5.000 respostas de teste são classificadas sem ambiguidade.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/desenvolvimento-orientado-por-avaliacao.md|Desenvolvimento Orientado por Avaliação]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]
- [[redes/ai-engineering/conceitos/fatiamento-de-dados-e-paradoxo-de-simpson.md|Fatiamento de Dados e Paradoxo de Simpson]]

### Alternativas

- Julgamento subjetivo por intuição de operadores sem critérios documentados.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/consistencia-factual.md|Consistência Factual]]
- [[redes/ai-engineering/conceitos/dimensionamento-amostral-de-avaliacao.md|Dimensionamento Amostral de Avaliação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 4 — Evaluate AI Systems
- **Localização:** Páginas 202–204
- **Evidência:** Chip Huyen destaca que a definição de diretrizes de avaliação é o passo mais desafiador na experiência do LinkedIn, relata a preferência por escalas discretas de 1 a 5 com exemplos calibrados e aborda o conceito de limiar de utilidade (usefulness threshold) mapeado para metas de negócio.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que são Diretrizes e Rubricas de Avaliação no contexto da Engenharia de IA?
2. Por que escalas discretas de 1 a 5 são empiricamente superiores a escalas de 1 a 100 para calibrar juízes de IA?
3. O que é o "Limiar de Utilidade" (*Usefulness Threshold*) e qual a sua função no ciclo de vida de um produto?
4. Como o exemplo do assistente de carreira do LinkedIn ilustra que uma resposta factualmente correta pode ser inaceitável como produto?
5. De que forma as rubricas devem abordar instruções sobre o que o modelo **não deve** fazer (conteúdo fora de escopo)?
6. Como o trabalho de validação de rubricas entre humanos protege o pipeline automatizado subsequente?
7. Por que a elaboração de uma rubrica de avaliação economiza tempo futuro na fase de anotação de dados para ajuste fino?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
