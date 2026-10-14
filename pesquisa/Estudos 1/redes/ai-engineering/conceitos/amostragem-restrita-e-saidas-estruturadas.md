# 🧠 Amostragem Restrita e Saídas Estruturadas

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 99–104

## 📝 Definição

### Definição formal

A **Amostragem Restrita** (*Constrained Sampling*) é uma técnica de decodificação guiada por gramática em que a distribuição de probabilidades sobre os [[redes/ai-engineering/conceitos/tokenizacao.md|tokens]] de um modelo de linguagem é filtrada em tempo de execução na GPU, aplicando-se uma máscara booleana rígida sobre o vetor de logits brutos para forçar a probabilidade de seleção a ser zero para qualquer token que viole regras sintáticas pré-definidas (como esquemas JSON, linguagens livres de contexto ou expressões regulares), garantindo a conformidade determinística de **Saídas Estruturadas** (*Structured Outputs*).

### Em linguagem simples

É colocar "trilhos físicos" na geração de texto da IA. Em vez de torcer para o modelo fechar as aspas ou vírgulas de um arquivo JSON corretamente, o software analisa a gramática a cada caractere. Se na próxima posição a única coisa válida for uma chave fechando `}` ou dois pontos `:`, o sistema simplesmente desativa todas as outras palavras do dicionário da IA, tornando matematicamente impossível o modelo errar o formato do arquivo.

### Escopo e distinções

Não se confunde com o simples pedido no prompt ("Responda em formato JSON"), que é frágil e sujeito a erros. A amostragem restrita opera no nível de inferência de baixo nível do motor de inferência (usando frameworks como *guidance*, *outlines* e *llama.cpp*).

## 🧩 Problema que resolve

Resolve a incompatibilidade entre a natureza textual aberta e probabilística dos LLMs e a exigência de dados estritos de sistemas tradicionais de software. APIs corporativas, bancos de dados relacionais e agentes exigem formatos rígidos (JSON, YAML, SQL). Se uma IA colocar um ponto e vírgula no lugar errado ou emitir texto conversacional antes de um código, sistemas downstream quebram (*crash*).

## 💡 Intuição

Pense em preencher um formulário na internet.
- O **Prompting comum** é como um campo de texto livre onde está escrito "digite sua data de nascimento". O usuário pode digitar "25 de maio de 1990", "25/05/90" ou "ontem", quebrando o banco de dados.
- A **Amostragem Restrita** é uma máscara de formulário no teclado do celular que desativa todas as letras do teclado e deixa apenas os números ativos com barras automáticas `__ / __ / ____`. O usuário é fisicamente impedido pelo sistema de digitar qualquer coisa fora da máscara.

## ⚙️ Como funciona

A verificação sintática ocorre passo a passo durante o loop de decode:

### Etapas

1. **Definição da Gramática:** O desenvolvedor define o esquema desejado (um modelo Pydantic, schema JSON ou regex).
2. **Geração dos Logits da rodada:** O LLM processa o contexto e emite os logits para os 100.000 tokens do vocabulário.
3. **Mascaração Gramatical (Filtro):** O analisador sintático lê o texto gerado até o momento e consulta a gramática. Ele identifica quais tokens do vocabulário manteriam a sintaxe válida:
   - Tokens válidos mantêm seus logits inalterados;
   - Tokens inválidos têm seus logits convertidos para $-\infty$.
4. **Aplicação do Softmax:** Como os tokens inválidos possuem logit $-\infty$, sua probabilidade torna-se estritamente zero: $e^{-\infty} = 0$.
5. **Emissão garantida:** O modelo escolhe o próximo token exclusivamente entre os formatos permitidos pela gramática.

### Entradas e saídas

- **Entradas:** Prompt do usuário e uma especificação formal de formato (JSON Schema/Regex).
- **Saídas:** Resposta que atende com garantia matemática estrita à estrutura definida.

## 📐 Formulação matemática

Seja $z \in \mathbb{R}^{|V|}$ o vetor de logits brutos emitido pelo modelo na posição $t$, e seja $\mathcal{V}_{\text{válido}}(y_{<t}) \subseteq \mathcal{V}$ o subconjunto de tokens que mantêm a sequência compatível com a gramática $\mathcal{G}$. 
Aplica-se uma máscara aditiva $M \in \{0, -\infty\}^{|V|}$:

$$M_i = \begin{cases} 0, & \text{se } i \in \mathcal{V}_{\text{válido}}(y_{<t}) \\ -\infty, & \text{caso contrário} \end{cases}$$

O novo vetor de logits modificados $z^* = z + M$ é normalizado:

$$P(y_t = i \mid y_{<t}) = \frac{\exp(z^*_i)}{\sum_{j=1}^{|V|} \exp(z^*_j)}$$

Se $i \notin \mathcal{V}_{\text{válido}}$, então $P(y_t = i \mid y_{<t}) = 0$.

## 🧱 Hipóteses e condições de validade

- A gramática desejada deve ser passível de representação como um autômato finito determinístico (DFA) ou gramática livre de contexto (CFG) analisável em tempo real.
- Acesso de baixo nível aos logits brutos do modelo (recurso por vezes restrito ou simplificado em certas APIs fechadas comerciais).

## ✅ Quando usar

- Extração de dados de documentos não estruturados para inserção direta em bancos relacionais.
- Chamadas de ferramentas (*function calling*) e execução de comandos em agentes autônomos.
- Tarefas de análise semântica (*semantic parsing*), como Text-to-SQL e Text-to-Regex.

## 🚫 Quando não usar

- Geração de texto livre, artigos reflexivos ou tarefas de escrita criativa onde a imposição de esquemas rígidos anula a utilidade do modelo.

## ⚠️ Limitações e armadilhas

- **Sobrecarga computacional na inferência:** Avaliar gramáticas complexas a cada token pode introduzir latência perceptível no tempo por token gerado (*TPOT*).
- **Truncação prematura:** Se o comprimento máximo de tokens da requisição for atingido antes de o modelo fechar o esquema (ex.: faltando fechar a última chave do JSON), o arquivo final ficará corrompido, a despeito do uso da amostragem restrita.

## 🔍 Comparações

| Nível de Intervenção | Estratégia | Confiabilidade de Formato | Custo / Latência |
|---|---|---|---|
| **Prompting** | Instruir "Retorne apenas JSON" | Média a Baixa ($70\% - 90\%$) | Sem custo extra |
| **Pós-processamento** | Scripts que tentam fechar chaves | Média (corrige erros simples) | Muito baixo |
| **Amostragem Restrita** | Máscara de logits via gramática | **Absoluta ($100\%$)** | Sobrecarga de análise |
| **Finetuning** | Treinar em milhares de exemplos de saída | Alta ($95\% - 99\%$) | Alto custo inicial |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O desenvolvedor precisa extrair a idade e o nome de um cliente em JSON: `{"nome": string, "idade": integer}`.
O modelo gera `{"nome": "Carlos", "idade": `.
Na posição seguinte, o motor de amostragem restrita consulta a gramática:
- Tokens de texto (aspas `"`, letras `A-Z`, palavras como `"trinta"`) recebem logit $-\infty$.
- Tokens numéricos (`0-9`) mantêm seus logits normais.
O modelo é fisicamente obrigado a emitir um número (`30`). Imediatamente após, o motor fecha a chave `}` automaticamente, impedindo preâmbulos ou texto conversacional adicional.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]
- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]

### Complementos

- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Alternativas

- Pós-processamento determinístico com expressões regulares e parsers tolerantes a falhas.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]
- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 99–104
- **Evidência:** Chip Huyen aborda a geração de saídas estruturadas, detalha a filtragem de vetores de logits por gramática através de bibliotecas como guidance e outlines, e discute os trade-offs entre prompting, pós-processamento, amostragem restrita e finetuning com cabeças de classificação.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Amostragem Restrita e como ela assegura a integridade de saídas estruturadas na GPU?
2. Por que confiar apenas em instruções de prompt para gerar JSONs válidos é uma prática arriscada em produção?
3. Como a máscara matemática com valores $-\infty$ atua sobre o vetor de logits antes da aplicação da Softmax?
4. Quais são os principais cenários corporativos que demandam garantias determinísticas de saída estruturada?
5. Qual é o impacto do uso de motores de gramática sobre a latência da fase de decodificação sequencial (*TPOT*)?
6. Como o problema da parada prematura (*early stopping*) pode comprometer um JSON gerado mesmo sob amostragem restrita?
7. Como a equipe de engenharia do LinkedIn utilizou parsers defensivos para resolver discrepâncias de YAML em seus pipelines?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
