# 🧠 Contaminação de Dados em Benchmarks

**Rede:** `ai-engineering`  
**Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 4 — Evaluate AI Systems
- Localização: Páginas 197–200

## 📝 Definição

### Definição formal

A **Contaminação de Dados** (*Data Contamination*, frequentemente denominada vazamento de dados de teste ou *data leakage*) é o fenômeno metodológico no qual exemplos, questões ou gabaritos pertencentes a um conjunto de dados de avaliação ou benchmark público foram inadvertida ou intencionalmente incorporados aos corpora massivos utilizados durante as etapas de pré-treinamento ou ajuste fino de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]], fazendo com que o modelo decore respostas por capacidade de memorização estatística em vez de demonstrar capacidade real de generalização cognitiva sobre dados não vistos.

### Em linguagem simples

É quando a prova vaza antes do exame e o aluno decora o gabarito. Se uma pergunta de um teste público famoso (como a prova da OAB ou o ENEM) estava jogada em um site da internet que o modelo leu durante o seu treinamento, ele acertará a questão no teste simplesmente repetindo o texto que guardou na memória, e não porque ele realmente "aprendeu" a pensar sobre aquele assunto.

### Escopo e distinções

Não se confunde com trapaça premeditada deliberada (embora ela ocorra no ecossistema competitivo). Na maioria esmagadora dos casos de modelos de fundação, a contaminação é um subproduto acidental inevitável do processo de raspagem web (*web scraping*) cega em larga escala, onde robôs de coleta puxam repositórios do GitHub, PDFs acadêmicos e páginas de teste que continham os próprios benchmarks.

## 🧩 Problema que resolve

Identificar e tratar a contaminação de dados resolve a vulnerabilidade crítica de se tomar decisões de adoção de modelos baseando-se em números de performance falsamente inflados em tabelas de liderança públicas.

## 💡 Intuição

Pense em avaliar um novo candidato a uma vaga de emprego sênior.
- Você aplica um teste técnico famoso que está publicado abertamente no Google há 5 anos. O candidato tira nota 10 com velocidade relâmpago.
- Você assume que ele é o melhor profissional do país. Contudo, no primeiro dia de trabalho real, ao se deparar com o código proprietário da sua empresa, ele não sabe resolver problemas elementares. Ele não era um gênio; ele apenas havia decorado as respostas do teste público na véspera da entrevista.

## ⚙️ Como funciona

A contaminação opera infiltrando-se nos conjuntos de dados e pode ser diagnosticada através de heurísticas matemáticas:

### Etapas

1. **Infiltração silenciosa:** Arquivos de testes (ex.: perguntas do MMLU ou HumanEval) são raspados de fóruns da web e indexados no dataset de pré-treino de trilhões de tokens.
2. **Treinamento e memorização:** A rede neural aplica gradiente descendente sobre esses textos, minimizando a perda e "gravando" a sequência exata de tokens em seus parâmetros.
3. **Diagnóstico por Sobreposição de N-grams:**
   - O engenheiro compara o texto do benchmark com o corpus de treino do modelo;
   - Se uma sequência idêntica contínua de $N$ tokens (ex.: $N \ge 13$ tokens) for localizada em ambos, a amostra de teste é sinalizada como "contaminada" ou "suja".
4. **Diagnóstico por [[redes/ai-engineering/conceitos/perplexidade-e-entropia-cruzada.md|Perplexidade]]:**
   - Calcula-se a incerteza do modelo sobre o texto do teste.
   - Se a perplexidade for anormalmente próxima de 1 (indicando certeza matemática absoluta e ausência de surpresa), conclui-se que o modelo já conhecia aquele texto previamente.
5. **Descontaminação e relato transparente:** Criadores de modelos responsáveis segregam as amostras limpas das contaminadas e reportam métricas em separado.

### Entradas e saídas

- **Entradas:** Arquivos do benchmark de avaliação e checkpoint do modelo ou dataset de treinamento.
- **Saídas:** Percentual de contaminação estimado e pontuações de performance purificadas (*clean scores*).

## 📐 Formulação matemática

O artigo satírico seminal de Rylan Schaeffer (Stanford, 2023), *"Pretraining on the Test Set Is All You Need"*, formalizou empiricamente o impacto da contaminação: ao treinar intencionalmente uma rede minúscula de apenas $10^6$ parâmetros ($1\text{M}$) diretamente sobre os dados de benchmarks consolidados, o minimodelo superou modelos gigantescos de 70B e 175B parâmetros:

$$\text{Acurácia}(M_{1\text{M}} \mid \mathcal{D}_{\text{treino}} = \mathcal{D}_{\text{teste}}) > \text{Acurácia}(M_{175\text{B}} \mid \mathcal{D}_{\text{treino}} \cap \mathcal{D}_{\text{teste}} = \emptyset)$$

Comprovando que a memorização mecânica mascara completamente a ausência de escala e raciocínio. No relatório do GPT-3 (OpenAI, 2020), a equipe identificou que 13 benchmarks apresentavam pelo menos $40\%$ de contaminação em seus dados de treinamento.

## 🧱 Hipóteses e condições de validade

- A detecção exata por sobreposição de $n$-grams pressupõe acesso irrestrito ao conjunto de dados de treino original (recurso que empresas de modelos fechados mantêm sob sigilo).
- A detecção por perplexidade pressupõe acesso aos valores de *logprobs* dos tokens gerados.

## ✅ Quando usar

- Auditoria de benchmarks acadêmicos antes de selecioná-los para guiar decisões de arquitetura corporativa.
- Validação interna obrigatória para certificar que os dados de teste da própria empresa não vazaram acidentalmente para conjuntos de dados de [[redes/ai-engineering/conceitos/ajuste-fino.md|ajuste fino]].

## 🚫 Quando não usar

- Em suítes privadas de avaliação cujas perguntas foram criadas do zero dentro da empresa na semana passada e nunca foram salvas em nenhum servidor acessível pela internet pública.

## ⚠️ Limitações e armadilhas

- **Contaminação indireta:** A contaminação pode ocorrer mesmo que a pergunta não seja idêntica palavra por palavra. Se o modelo foi treinado em livros didáticos de física que usavam exatamente os mesmos números e problemas da prova, ele herdará a resposta sem que a busca exata por $n$-grams detecte o vazamento.
- **Obsolescência imediata:** Como a frase técnica dita no capítulo pontua: *"Um benchmark deixa de ser útil assim que se torna público"*.

## 🔍 Comparações

| Método de Detecção | Precisão Técnica | Exigência de Infraestrutura | Funciona em APIs Fechadas? |
|---|---|---|---|
| **Sobreposição de N-grams** | Altíssima (conferência exata) | Custo computacional pesado (varre trilhões de tokens) | **Não** (exige os dados brutos de treino) |
| **Análise de Perplexidade** | Média a Alta (detecção de anomalia) | Baixa (apenas inferência com logprobs) | **Sim** (se a API expuser logprobs) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma startup quer construir um consultor de vestibulares. Eles avaliam um novo modelo chinês de código aberto que promete ser o melhor do mundo em biologia.
No teste com a prova do ENEM de 2022, o modelo atinge impressionantes $98\%$ de acerto. 
O engenheiro de IA desconfia do resultado, pega a prova do ENEM de 2024 (que foi aplicada no mês passado e ainda não circulou em bases de dados abertas) e submete ao mesmo modelo. 
A acurácia do modelo despenca para medíocres $42\%$. O modelo não entendia de biologia; ele havia apenas raspado uma página da web que continha a prova e o gabarito oficial do exame de 2022.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/perplexidade-e-entropia-cruzada.md|Perplexidade e Entropia Cruzada]]

### Complementos

- [[redes/ai-engineering/conceitos/desenvolvimento-orientado-por-avaliacao.md|Desenvolvimento Orientado por Avaliação]]
- [[redes/ai-engineering/conceitos/selecao-de-modelos-atributos-rigidos-e-flexiveis.md|Seleção de Modelos: Atributos Rígidos e Flexíveis]]

### Alternativas

- Uso de bancos de testes privados com geração dinâmica e rotatividade contínua de questões sintéticas.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]
- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 4 — Evaluate AI Systems
- **Localização:** Páginas 197–200
- **Evidência:** Chip Huyen aborda a prevalência da contaminação em benchmarks públicos, cita a sátira científica de Rylan Schaeffer (2023), detalha os experimentos de detecção no relatório do GPT-3 (onde 13 benchmarks continham pelo menos 40% de vazamento) e formaliza as técnicas de detecção por n-grams e perplexidade.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é contaminação de dados em benchmarks de inteligência artificial e quais são suas principais causas?
2. Como o artigo experimental de Rylan Schaeffer (2023) demonstrou que a contaminação anula o valor comparativo de escalas de modelos?
3. Qual é o procedimento técnico utilizado para detectar contaminação através da medição de Perplexidade?
4. Por que a detecção de contaminação por sobreposição de $n$-grams é inviável para desenvolvedores que utilizam modelos proprietários fechados?
5. O que é a contaminação indireta de dados e por que ela passa despercebida por detectores de strings exatas?
6. Quais foram as constatações empíricas relatadas pela OpenAI sobre a contaminação de dados no relatório técnico do GPT-3?
7. Qual medida prática de engenharia é recomendada para que empresas protejam seus pipelines de avaliação contra a contaminação?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
