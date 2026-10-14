# 🧠 Desafios de Avaliação de Modelos de Fundação

**Rede:** `ai-engineering`   **Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 114–117

## 📝 Definição

### Definição formal

Os **Desafios de Avaliação de Modelos de Fundação** constituem o conjunto de barreiras epistemológicas, estatísticas e computacionais que impedem a aplicação direta de métricas clássicas de teste de software e de aprendizado de máquina supervisionado para validar sistemas baseados em [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]], originadas primordialmente por quatro eixos estruturais:

1. **Espaço de saída aberto e gerativo:** Impossibilidade de enumerar um conjunto exaustivo de respostas corretas (*ground truths*);
2. **Escala de inteligência e capacidade cognitiva:** A necessidade de conhecimento altamente especializado (doutorado, medicina, direito complexo) para validar saídas avançadas, quebrando a premissa de anotação barata e não qualificada;
3. **Opacidade arquitetural e de treinamento:** Modelos consumidos como caixas-pretas proprietárias com dados de treino não divulgados;
4. **Saturação acelerada de benchmarks públicos:** Índices de avaliação consolidados perdem utilidade em meses ao serem superados ou contaminados por novas gerações de modelos.

### Em linguagem simples

É a constatação de que avaliar se uma IA moderna é boa virou uma tarefa tão ou mais difícil do que construir o próprio modelo. Antigamente, checar se um modelo acertou era fácil: o resultado era "sim" ou "não", "gato" ou "cachorro". Agora, o modelo escreve ensaios, diagnósticos médicos ou códigos complexos. Para saber se ele está certo, você precisa de especialistas caros lendo página por página ou precisa inventar formas automatizadas inteligentes de teste que não sejam enganadas por textos bonitos, mas falsos.

### Escopo e distinções

Não se confunde com testes unitários determinísticos tradicionais de software (onde entradas fixas produzem saídas estritamente previsíveis). A avaliação em [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]] lida com sistemas estocásticos probabilísticos cujos limites de falha mudam conforme o contexto e os dados fornecidos.

## 🧩 Problema que resolve

Identificar esses desafios impede que equipes adotem abordagens simplistas e perigosas de validação baseadas em "vibe checks" (olhômetro informal) ou no uso cego de tabelas de liderança públicas que não representam os riscos específicos do caso de uso da empresa.

## 💡 Intuição

Pense em corrigir uma prova escolar:

- Corrigir uma prova de matemática básica do ensino fundamental com 10 questões de múltipla escolha é trivial: qualquer pessoa com o gabarito oficial corrige 100 provas em 15 minutos (**ML clássico com tarefas fechadas**).
- Agora imagine avaliar uma tese de doutorado inédita de física quântica teórica com 300 páginas de deduções matemáticas complexas (**LLMs de alta capacidade**). O gabarito não existe; pouquíssimos seres humanos na Terra têm qualificação para entender se as equações fazem sentido, e ler cada linha consome dias de esforço mental exaustivo.

## ⚙️ Como funciona

A crise de avaliação desdobra-se em um ciclo vicioso de saturação e complexidade metodológica:

### Etapas

1. **Lançamento de benchmark:** A comunidade acadêmica introduz um benchmark difícil composto por milhares de tarefas para testar limites conceituais (ex.: GLUE em 2018, MMLU em 2020).
2. **Saturação acelerada:** Modelos maiores escalam parâmetros e dados, superando o teto humano do benchmark em prazos inferiores a um ou dois anos (ex.: o GLUE saturou em 1 ano, exigindo o SuperGLUE; o MMLU exigiu a criação do MMLU-Pro).
3. **Vulnerabilidade a contaminações:** Como os benchmarks são públicos, seus textos vazam para os corpora de pré-treino raspados da internet, inflando pontuações artificiais sem ganho real de utilidade.
4. **Necessidade de avaliação sob medida:** Equipes de engenharia de produto são forçadas a abandonar os benchmarks acadêmicos gerais e projetar baterias de testes privadas centradas em seus próprios fluxos de trabalho.

### Entradas e saídas

- **Entradas:** Saídas abertas textuais e multimodais geradas sob prompts dinâmicos.
- **Saídas:** Diagnóstico de confiabilidade, matrizes de risco factual e taxas de rejeição operacional.

## 📐 Formulação matemática

Em tarefas fechadas clássicas, a perda ou acurácia sobre um conjunto de teste $\mathcal{D}_{\text{teste}} = \{(x_i, y_i)\}_{i=1}^N$ é computada deterministamente comparando com o rótulo único $y_i$:

$$\text{Acurácia} = \frac{1}{N} \sum_{i=1}^N \mathbb{I}\Big(f_\theta(x_i) = y_i\Big)$$

Em saídas gerativas abertas, o conjunto de respostas válidas $\mathcal{Y}^*(x_i)$ possui cardinalidade infinita ($|\mathcal{Y}^*(x_i)| = \infty$). A função de julgamento $J$ torna-se uma integral probabilística intratável analiticamente:

$$\text{Qualidade} = \mathbb{E}_{x \sim \mathcal{D}, y \sim P_\theta(\cdot \mid x)} \Big[ J(y \mid x, \mathcal{C}) \Big]$$

Onde $J$ depende de contexto tácito $\mathcal{C}$, factualidade do mundo e preferências humanas não formalizáveis em equações fechadas simples.

## 🧱 Hipóteses e condições de validade

- Para que qualquer avaliação automatizada seja válida, o sistema de teste deve ter custo e latência substancialmente inferiores aos da anotação humana manual correspondente.
- Os dados do conjunto de teste privado devem ser estritamente segregados para evitar vazamento em pipelines de ajuste fino ou pré-treinamento contínuo.

## ✅ Quando usar

- Diagnóstico estrutural obrigatório no início de qualquer projeto de produto de IA para definir orçamento e arquitetura de testes.
- Na definição dos critérios de corte que impedem a liberação prematura de modelos não homologados para clientes finais.

## 🚫 Quando não usar

- Em sistemas que operam estritamente sobre classificações binárias clássicas ou regressões tabulares, onde o ferramental convencional de validação cruzada do Scikit-Learn resolve o problema com perfeição.

## ⚠️ Limitações e armadilhas

- **A ilusão da pontuação acadêmica:** Assumir que um modelo com $90\%$ no benchmark MMLU atenderá com $90\%$ de sucesso as dúvidas dos clientes de um banco sobre extratos de conta corrente.
- **Subestimação de recursos:** Alocar 95% do tempo da equipe para projetar prompts e apenas 5% para construir pipelines de avaliação sistemática.

## 🔍 Comparações

| Dimensão | Avaliação em ML Tradicional | Avaliação de Modelos de Fundação |
|---|---|---|
| **Espaço de Saída** | Finito e fechado (classes, números) | Aberto, extenso e estocástico (texto livre) |
| **Gabarito (*Ground Truth*)** | Rótulo fixo e inequívoco por amostra | Inexistência de um único gabarito perfeito |
| **Custo de Julgamento** | Milissegundos via código matemático simples | Alto (exige especialistas ou chamadas a outros LLMs) |
| **Durabilidade dos Testes** | Alta (conjuntos de teste duram anos) | Baixa (benchmarks saturam em poucos meses) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma equipe de engenharia constrói um assistente para responder dúvidas de médicos oncologistas sobre laudos de biópsias.

- Se fosse um projeto antigo, o modelo diria apenas: `"Maligno"` ou `"Benigno"`. Conferir o acerto exigiria apenas comparar com o laudo do patologista em uma planilha de Excel.
- Com um LLM moderno, a resposta é um parecer de quatro parágrafos correlacionando mutações genéticas com protocolos quimioterápicos. O estagiário da equipe de TI não consegue ler o texto e dizer se a recomendação está correta ou se o modelo cometeu uma sutileza fatal de dosagem. Avaliar o sistema passa a exigir que oncologistas com 20 anos de experiência passem horas revisando cada resposta do modelo, evidenciando a barreira monumental de avaliação.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]

### Complementos

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]
- [[redes/ai-engineering/conceitos/avaliacao-comparativa.md|Avaliação Comparativa (Pairwise)]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (trata-se do mapeamento dos problemas fundamentais da área).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/perplexidade-e-entropia-cruzada.md|Perplexidade e Entropia Cruzada]]
- [[redes/ai-engineering/conceitos/correcao-funcional.md|Correção Funcional (pass@k)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 114–117
- **Evidência:** Chip Huyen discute as razões pelas quais avaliar modelos de fundação é mais árduo do que no ML clássico, citando a observação do matemático Terrence Tao sobre o GPT-o1, a saturação relâmpago de benchmarks como GLUE e MMLU e a disparidade entre o crescimento explosivo de artigos sobre avaliação versus a ausência de infraestrutura madura nas empresas.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são os quatro eixos estruturais que tornam a avaliação de modelos de fundação mais complexa do que a de sistemas de ML clássico?
2. Por que a natureza aberta e gerativa da linguagem impede o uso simplista de matrizes de confusão e acurácia direta?
3. Como o fenômeno da saturação rápida de benchmarks afeta a longevidade dos índices públicos de avaliação como MMLU e GLUE?
4. Qual é a reflexão trazida pelo matemático Terrence Tao em relação à qualificação intelectual necessária para avaliar novos modelos avançados de IA?
5. Por que modelos de fundação comerciais consumidos via API aumentam a opacidade do processo de avaliação?
6. Qual é o perigo de equipes de engenharia utilizarem "vibe checks" como principal critério de validação de produtos?
7. Por que benchmarks públicos frequentemente sofrem de contaminação de dados (*data contamination*)?

## Conexoes com Machine Learning

Estes fundamentos pertencem a outra rede e foram ligados como prerequisitos ou conceitos vizinhos. O MOC nao e usado como no conceitual.
- [[redes/machine-learning/conceitos/Cross-Validation.md|Cross-Validation]]
- [[redes/machine-learning/conceitos/Bias-Variance_Tradeoff.md|Bias-Variance Tradeoff]]
- [[redes/machine-learning/conceitos/Matriz_de_Confusão.md|Matriz de Confusão]]
- [[redes/machine-learning/conceitos/ROC-AUC.md|ROC-AUC]]
- [[redes/machine-learning/conceitos/Precision_e_Recall.md|Precision e Recall]]
- [[redes/machine-learning/conceitos/F1-Score.md|F1-Score]]
- [[redes/machine-learning/conceitos/RMSE_e_MAE.md|RMSE e MAE]]

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Perplexidade e Entropia Cruzada

**Rede:** `ai-engineering`   **Área:** `metricas`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 118–125

## 📝 Definição

### Definição formal

A **Entropia Cruzada** ($H(P, Q)$) e a **Perplexidade** ($\text{PPL}$) são métricas fundamentadas na teoria da informação de Claude Shannon (1951) utilizadas para mensurar a eficácia de um [[redes/ai-engineering/conceitos/modelo-de-linguagem.md|modelo de linguagem]] $Q$ em prever a distribuição estatística verdadeira dos tokens de um corpus textual $P$:

- A **Entropia Cruzada** quantifica o número médio de bits (ou nats) necessários para codificar e prever um token do texto sob o modelo;
- A **Perplexidade** é o exponencial da entropia cruzada ($\text{PPL} = 2^H$ ou $e^H$) e representa a média geométrica ponderada do número efetivo de escolhas de tokens equiprováveis entre as quais o modelo se encontra hesitante a cada passo de geração.

### Em linguagem simples

A perplexidade mede o quão "confuso" ou "surpreso" o modelo fica ao ler um texto. Se a perplexidade do modelo em um parágrafo for 10, significa que, a cada palavra que lê, ele fica tão em dúvida quanto se tivesse que sortear uma palavra dentro de um saco com 10 opções igualmente prováveis. Quanto **menor** a perplexidade, mais o modelo domina aquele texto e menos incerteza ele tem.

### Escopo e distinções

Trata-se de uma métrica de nível intrínseco de modelagem (avalia a precisão na predição do próximo token). Não avalia se uma resposta gerada por um chatbot é educada, prestativa ou segura. A literatura destaca que a perplexidade tipicamente **aumenta** após etapas de alinhamento e pós-treinamento (SFT/RLHF) devido ao colapso de entropia, tornando a métrica inadequada para comparar assistentes de diálogo instruídos.

## 🧩 Problema que resolve

Resolve a necessidade de guiar o treinamento de modelos de linguagem com uma métrica analítica matemática estrita, contínua e diferenciável durante o pré-treinamento. Em aplicações a jusante, a perplexidade resolve o desafio de detectar se um texto foi memorizado durante o treino (detecção de contaminação de dados) ou se um texto de entrada é sem sentido ou corrompido (detecção de anomalias).

## 💡 Intuição

Pense em um leitor experiente de jornais diários:

- Ao ler a frase: `"O presidente assinou uma medida provisória para conter a inflação..."`, ele tem baixíssima perplexidade ($\text{PPL} \approx 2$); o vocabulário e a sintaxe são tão familiares que ele quase adivinha as próximas palavras antes de virar a página.
- Agora imagine que ele abre uma página com palavras aleatórias ou com um texto em finlandês sem tradução: `"kissa istuu pöydällä talossa"`. A incerteza do leitor explode; ele não tem ideia de qual caractere virá em seguida. Sua perplexidade é altíssima ($\text{PPL} > 1000$).

## ⚙️ Como funciona

O cálculo da perplexidade baseia-se na extração das probabilidades condicionais que o modelo atribuiu a cada palavra do próprio texto avaliado:

### Etapas

1. **Ingestão sequencial:** O texto de avaliação é tokenizado em $x_1, x_2, \dots, x_n$.
2. **Extração de Logprobs:** A cada passo $i$, o modelo calcula a probabilidade atribuída ao token verdadeiro que de fato ocorreu na sequência dado o contexto passado: $P(x_i \mid x_1, \dots, x_{i-1})$.
3. **Conversão logarítmica:** Para evitar problemas de subfluxo numérico (*underflow* computacional com números infinitesimais), trabalha-se com o logaritmo da probabilidade ($\log P$).
4. **Média da perda:** Soma-se os valores de log-probabilidade e divide-se pelo número total de tokens $n$, obtendo a entropia cruzada média.
5. **Exponenciação:** Aplica-se a função exponencial ($e^{\text{perda}}$ ou $2^{\text{perda}}$) para obter o valor escalar final de perplexidade.

### Entradas e saídas

- **Entradas:** Texto arbitrário e o modelo de linguagem equipado com API de acesso a *logprobs*.
- **Saídas:** Número escalar positivo ($\text{PPL} \ge 1$), onde 1 representa a perfeição absoluta de predição determinística.

## 📐 Formulação matemática

A entropia cruzada entre a distribuição empírica real $P$ e a distribuição predita pelo modelo $Q$ decompõe-se pela divergência de Kullback-Leibler:

$$H(P, Q) = H(P) + D_{\text{KL}}(P \parallel Q)$$

Como $H(P, Q)$ não é simétrica, $H(P, Q) \neq H(Q, P)$.
Para uma sequência concreta de $n$ tokens $X = (x_1, x_2, \dots, x_n)$, a perplexidade empírica é a média geométrica do inverso das probabilidades condicionais:

$$\text{PPL}(X) = \exp\left( -\frac{1}{n} \sum_{i=1}^n \ln P(x_i \mid x_{<i}) \right) = \left( \prod_{i=1}^n \frac{1}{P(x_i \mid x_{<i})} \right)^{\frac{1}{n}}$$

Variações métricas de escala utilizam bases diferentes de codificação:

- **Bits per character (BPC):** $\text{BPC} = \frac{H_2(X)}{\text{número de caracteres}}$
- **Bits per byte (BPB):** $\text{BPB} = \frac{H_2(X)}{\text{número de bytes}}$

## 🧱 Hipóteses e condições de validade

- Exige acesso obrigatório aos *logits* ou *logprobs* das probabilidades de cada token, inviabilizando seu cálculo em APIs comerciais fechadas que não expõem esses dados (como certas rotas do Anthropic Claude).
- A perplexidade só pode ser comparada diretamente entre modelos que utilizem **exatamente o mesmo tokenizador e vocabulário**; modelos com vocabulários de tamanhos diferentes possuem espaços de amostragem incomparáveis.

## ✅ Quando usar

- Monitoramento e comparação de modelos durante a fase de pré-treinamento (modelos mais poderosos apresentam menor PPL em textos gerais, como demonstrado na família GPT-2).
- **Detecção de contaminação de dados:** Se a perplexidade de um modelo sobre um conjunto de teste público for anipicamente baixa (ex.: $\text{PPL} < 1{,}2$), o modelo certamente memorizou o teste no pré-treino.
- **Detecção de anomalias e textos corrompidos:** Filtro para barrar entradas de usuários compostas por sequências sem sentido ou ataques de injeção baseados em cadeias de caracteres aleatórios.

## 🚫 Quando não usar

- Para avaliar a qualidade de chatbots alinhados para diálogo (modelos pós-SFT/RLHF).
- Para comparar modelos concorrentes que utilizem tokenizadores distintos.

## ⚠️ Limitações e armadilhas

- **O paradoxo do alinhamento:** Um modelo pré-treinado cru geralmente possui menor perplexidade do que sua versão alinhada por RLHF, embora a versão alinhada seja ordens de magnitude mais útil para humanos em tarefas reais.
- **Sensibilidade a formatos:** Textos altamente estruturados (como páginas HTML cheias de tags repetidas) geram perplexidades artificialmente baixas sem que isso signifique alta inteligência do modelo.

## 🔍 Comparações

| Propriedade dos Dados | Impacto na Perplexidade Esperada | Justificativa Teórica |
|---|---|---|
| **Maior estruturação (ex.: código HTML)** | **Diminui** a perplexidade | Sintaxe previsível com tags que se fecham |
| **Maior vocabulário do modelo** | **Aumenta** a perplexidade | Maior espaço amostral de escolhas concorrentes |
| **Maior janela de contexto** | **Diminui** a perplexidade | Mais pistas semânticas disponíveis para desempate |
| **Textos anômalos ou gírias raras** | **Aumenta** drasticamente a perplexidade | Baixa frequência estatística na base de treino |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um engenheiro quer testar se o novo modelo de linguagem de código aberto que ele baixou sofreu vazamento do exame de certificação profissional de contabilidade de 2024.
Ele pega uma questão longa e complexa da prova de 2024 e calcula a perplexidade do modelo sobre o texto da questão acompanhado da resposta oficial. 

- O modelo atinge $\text{PPL} = 1{,}08$. 

Isso significa que o modelo quase não teve incerteza alguma ao longo de 500 palavras consecutivas difíceis. A certeza estatística é tão anômala que comprova que o modelo leu e memorizou aquele exame durante o pré-treinamento, invalidando qualquer teste futuro com aquela prova.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-linguagem.md|Modelo de Linguagem]]
- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]

### Complementos

- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Alternativas

- [[redes/ai-engineering/conceitos/correcao-funcional.md|Correção Funcional (pass@k)]] (para código)
- [[redes/ai-engineering/conceitos/similaridade-semantica.md|Similaridade Semântica]] (para tarefas com gabarito de referência)

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]
- [[redes/ai-engineering/conceitos/pos-treinamento-e-alinhamento.md|Pós-Treinamento e Alinhamento]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 118–125
- **Evidência:** Chip Huyen revisita Shannon (1951) para formalizar entropia e perplexidade, detalha a tabela empírica do GPT-2 comprovando a queda de PPL conforme a escala do modelo aumenta, e explica o fenômeno do colapso de entropia pós-alinhamento e o uso prático de PPL para auditar contaminação de dados.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a definição matemática e a intuição estatística da métrica de Perplexidade (PPL)?
2. Como a entropia cruzada se relaciona conceitualmente com a capacidade de compressão de texto de um modelo?
3. Por que não é possível comparar diretamente a perplexidade de dois modelos que utilizam tokenizadores com vocabulários diferentes?
4. Qual é o motivo técnico pelo qual a perplexidade costuma aumentar após o processo de ajuste fino supervisionado (SFT) e RLHF?
5. Como a perplexidade pode ser utilizada por engenheiros de IA como ferramenta de auditoria para detectar contaminação de dados de treino?
6. De que forma o comprimento do contexto de entrada afeta matematicamente o valor de perplexidade observado em uma sequência?
7. Qual é a diferença operacional entre expressar a entropia em unidades de "bits" versus unidades de "nats"?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Correção Funcional (pass@k)

**Rede:** `ai-engineering`   **Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 126–127

## 📝 Definição

### Definição formal

A **Correção Funcional** (*Functional Correctness* ou *Execution Accuracy*) é um método objetivo de avaliação exata no qual as saídas geradas por um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] são validadas não pela sua similaridade superficial com um texto de referência, mas pela sua capacidade de executar com sucesso em um interpretador ou ambiente operacional e passar em uma bateria rigorosa de testes unitários ou verificações formais de estado. 

A métrica padrão é o **pass@k**, definida como a probabilidade não enviesada de que pelo menos uma dentre $k$ amostras de código geradas de forma independente pelo modelo resolva integralmente o problema proposto, passando em todos os casos de teste pré-estabelecidos.

### Em linguagem simples

É testar se o programa gerado pela IA realmente funciona na prática. Em vez de olhar se o código parece bonito ou se usa as mesmas variáveis de uma resposta humana, o sistema executa o código em um interpretador real (como Python ou banco SQL). Se o código compilar, rodar e devolver a resposta certa para todos os testes matemáticos exigidos, a IA ganha nota 10; se der erro ou falhar em um único teste, a nota é zero.

### Escopo e distinções

Diferencia-se radicalmente de métricas baseadas em sobreposição de texto como BLEU ou ROUGE. O capítulo pontua que no benchmark HumanEval, as pontuações de BLEU entre códigos corretos e incorretos eram quase indistinguíveis, comprovando que avaliar código por contagem de palavras não tem valor de engenharia.

## 🧩 Problema que resolve

Resolve a incapacidade de avaliar saídas técnicas e de programação através de similaridade de texto. Em computação, duas funções escritas de maneiras completamente diferentes (uma recursiva e outra iterativa, com nomes de variáveis distintos) podem ser ambas 100% corretas, enquanto uma função idêntica a um gabarito humano com a exceção de um sinal trocado de `+` para `-` está 100% quebrada. A correção funcional avalia a semântica operacional do resultado.

## 💡 Intuição

Pense em contratar um chaveiro para fabricar uma chave para sua porta.

- A **avaliação por similaridade de texto** seria como tirar uma foto da chave original e olhar se a chave nova é feita do mesmo metal prateado e tem o mesmo formato geral.
- A **correção funcional** é colocar a chave na fechadura, girar o trinco e ver se a porta realmente abre sem travar. Não importa se a chave nova é quadrada ou redonda; se ela abre a fechadura com perfeição em todas as tentativas, ela funciona.

## ⚙️ Como funciona

O pipeline de avaliação opera através de geração em lote e execução em ambiente isolado (*sandbox*):

### Etapas

1. **Definição do problema:** O modelo recebe a assinatura de uma função acompanhada de sua docstring explicativa e exemplos de comportamento (ex.: benchmark HumanEval ou MBPP).
2. **Geração de amostras ($n$):** O modelo gera $n$ soluções de código candidatas e independentes ($n \ge k$) com temperatura moderada para permitir diversidade estocástica.
3. **Execução em ambiente seguro (*Sandbox*):** Cada uma das $n$ soluções é executada sequencialmente ou em paralelo contra uma suíte de asserções determinísticas (`assert`).
4. **Contabilização dos sucessos ($c$):** Conta-se quantas amostras ($c$) passaram em $100\%$ dos testes unitários sem levantar nenhuma exceção de runtime.
5. **Cálculo estatístico:** Aplica-se a fórmula combinatória não enviesada do pass@k para derivar a taxa de sucesso.

### Entradas e saídas

- **Entradas:** Problema de programação e suíte de testes unitários com entradas e saídas esperadas.
- **Saídas:** Pontuação percentual pass@k (ex.: pass@1 de $75\%$, pass@10 de $92\%$).

## 📐 Formulação matemática

Para estimar o pass@k sem o viés estatístico de simplesmente gerar apenas $k$ amostras (o que teria alta variância), gera-se um número maior de amostras $n \ge k$ (por exemplo, $n = 200$) e conta-se o número de amostras corretas $c$. A formulação não enviesada introduzida por Chen et al. (OpenAI, 2021) é expressa como:

$$\text{pass@}k = \mathbb{E}_{\text{problemas}} \left[ 1 - \frac{\binom{n - c}{k}}{\binom{n}{k}} \right]$$

Onde:

- $\binom{n}{k}$ é a combinação de $n$ elementos tomados $k$ a $k$;
- $\binom{n - c}{k}$ representa a quantidade de combinações compostas estritamente por amostras incorretas;
- Como consequência probabilística direta: $\text{pass@1} \le \text{pass@3} \le \text{pass@10} \le \dots \le \text{pass@100}$, uma vez que dar mais chances ($k$) ao modelo eleva a probabilidade de pelo menos uma solução estar correta.

## 🧱 Hipóteses e condições de validade

- A suíte de testes unitários deve ter alta cobertura de casos de borda (*edge cases*); testes fracos podem aprovar códigos errôneos que falhariam em cenários reais.
- A execução deve ocorrer em containers isolados sem acesso à rede externa para evitar execução acidental ou intencional de código destrutivo pelo modelo.

## ✅ Quando usar

- Avaliação de modelos e copilotos de programação de software (benchmarks como HumanEval, MBPP).
- Sistemas de geração de consultas a bancos de dados relacionais (Text-to-SQL em benchmarks como Spider, BIRD-SQL e WikiSQL).
- Avaliação de agentes em jogos (onde a pontuação final do jogo dita a correção funcional da IA).

## 🚫 Quando não usar

- Em geração de texto livre, redação de contratos, resumos literários ou conversação geral, onde não existem interpretadores determinísticos nem testes unitários de sintaxe.

## ⚠️ Limitações e armadilhas

- **Foco estrito em acerto funcional:** A métrica pass@k tradicional aprova códigos que funcionam, mas que podem ser terrivelmente ineficientes (consumo absurdo de memória, algoritmos $\mathcal{O}(N^3)$) ou completamente ilegíveis para engenheiros humanos.
- **Risco de segurança na avaliação:** Rodar código arbitrário gerado por IA na máquina do desenvolvedor sem sandbox pode disparar comandos perigosos de deleção de arquivos ou conexões maliciosas de rede.

## 🔍 Comparações

| Métrica | O que avalia? | Método de Cálculo | Sensibilidade a Sinônimos |
|---|---|---|---|
| **BLEU / ROUGE** | Sobreposição visual de texto | Contagem de n-grams | Péssima (penaliza sinônimos) |
| **pass@1** | Correção prática da 1ª tentativa | Execução contra asserções | Imune (foca no comportamento) |
| **pass@10** | Capacidade de resolver em 10 tentativas | Probabilidade combinatória | Imune (mede potencial do modelo) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O modelo recebe a tarefa de criar a função `tem_elementos_proximos(numeros, limite)` que retorna verdadeiro se dois números em uma lista estiverem a uma distância menor que o limite.
O modelo gera três rascunhos de código:

1. O rascunho A usa dois loops aninhados `for` e passa em 6 dos 7 testes, falhando quando a lista contém números negativos.
2. O rascunho B gera um erro de sintaxe `SyntaxError` e nem compila.
3. O rascunho C ordena a lista primeiro e compara elementos adjacentes, passando com sucesso por todas as 7 asserções de teste unitário.

Ao avaliar sob $k=3$ tentativas, como a amostra C obteve êxito pleno, a tarefa é computada como resolvida para o cálculo do pass@3.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]

### Alternativas

- [[redes/ai-engineering/conceitos/similaridade-lexical.md|Similaridade Lexical]]
- [[redes/ai-engineering/conceitos/similaridade-semantica.md|Similaridade Semântica]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]
- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 126–127
- **Evidência:** Chip Huyen aborda a avaliação por correção funcional e execução em interpretadores, detalha o uso de asserções no benchmark HumanEval e MBPP, e demonstra por que a métrica pass@k da OpenAI é o padrão de validação empírica em geração de código e Text-to-SQL.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a definição de Correção Funcional e em que ela se distingue das métricas tradicionais de processamento de texto?
2. Como funciona a formulação matemática da métrica pass@k proposta por Chen et al. no artigo do HumanEval?
3. Por que a pontuação pass@1 é estatisticamente menor ou igual à pontuação pass@10 para um mesmo modelo?
4. Qual foi a constatação empírica da OpenAI sobre a correlação entre pontuações BLEU e a correção funcional real de soluções de código?
5. Como benchmarks de Text-to-SQL modernos (como BIRD-SQL) expandiram a correção funcional para avaliar também a eficiência de execução da consulta?
6. Quais são os riscos de segurança ao avaliar correção funcional e como a infraestrutura de sandbox mitiga esses perigos?
7. Por que um código gerado por IA pode atingir pontuação perfeita no pass@k e ainda assim ser considerado de baixa qualidade por um engenheiro sênior?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

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

# 🧠 Similaridade Semântica

**Rede:** `ai-engineering`   **Área:** `metricas`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 132–134

## 📝 Definição

### Definição formal

A **Similaridade Semântica** (*Semantic Similarity* ou *Semantic Textual Similarity* — STS) é a metodologia de avaliação contínua que quantifica o grau de equivalência conceitual, lógica e de significado entre dois textos ou expressões, independentemente de divergências em suas superfícies ortográficas ou escolhas lexicais, computada mediante a transformação prévia de ambas as passagens em vetores densos através de modelos de [[redes/ai-engineering/conceitos/embeddings.md|embeddings]] e posterior mensuração geométrica da proximidade angular desses vetores no espaço latente via **Similaridade de Cosseno**.

### Em linguagem simples

É a métrica que avalia se duas frases dizem a mesma coisa, mesmo usando palavras completamente diferentes. Em vez de ficar contando letras ou palavras repetidas, o sistema traduz cada frase para uma coordenada matemática no espaço dos significados e mede a distância entre essas ideias.

### Escopo e distinções

Supera o gargalo estrito da [[redes/ai-engineering/conceitos/similaridade-lexical.md|similaridade lexical]]. Enquanto o BLEU e o ROUGE exigem que as palavras sejam idênticas, métricas semânticas como o **BERTScore** e o **MoverScore** utilizam representações contextuais para identificar que "Como vai você?" e "E aí, tudo bem?" possuem quase 100% de similaridade de significado.

## 🧩 Problema que resolve

Resolve a miopia das métricas de sobreposição de texto em aplicações de linguagem natural aberta. Permite avaliar tarefas de resposta a perguntas, atendimento ao cliente e sumarização onde o usuário ou modelo expressa fatos legítimos usando sinônimos, alterações de ordem de palavras ou formulações mais concisas que não coincidem com o gabarito original do anotador humano.

## 💡 Intuição

Pense em dois navegadores descrevendo uma ilha:

- Um navegador diz: `"A terra em frente é cercada por águas marinhas por todos os lados"`.
- O segundo navegador diz: `"Avistamos uma ilha no horizonte"`.

Um fiscal puramente lexical diria que os marinheiros falaram de coisas distintas porque quase nenhuma palavra coincide. Um geógrafo (**a similaridade semântica**) sabe a definição de "ilha" e percebe que as duas afirmações apontam exatamente para a mesma coordenada geográfica e factual.

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

## 📐 Formulação matemática

Sejam $A$ e $B$ os vetores de embedding de dimensão $d$ que representam os dois textos. A Similaridade de Cosseno é definida pelo produto escalar dividido pelo produto de suas normas euclidianas ($L_2$):

$$\text{CosineSimilarity}(A, B) = \frac{A \cdot B}{\|A\|_2 \|B\|_2} = \frac{\sum_{i=1}^d A_i B_i}{\sqrt{\sum_{i=1}^d A_i^2} \sqrt{\sum_{i=1}^d B_i^2}}$$

Onde:

- Valor igual a $1$: vetores com orientação angular perfeitamente idêntica (significados idênticos sob o espaço do modelo);
- Valor igual a $0$: vetores ortogonais (conceitos não correlacionados);
- Valor igual a $-1$: vetores diametralmente opostos.

## 🧱 Hipóteses e condições de validade

- A qualidade e a dimensionalidade do modelo de embedding subjacente determinam o teto de precisão da métrica; se o modelo de embedding for fraco ou descalibrado, textos com significados distintos podem receber vetores próximos.
- Assume que pequenas alterações sintáticas com grande impacto lógico são capturadas pelo embedding (o que nem sempre é verdade para negações sutis).

## ✅ Quando usar

- Avaliação automática contínua de pipelines de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]], medindo a aderência da resposta aos documentos recuperados.
- Agrupamento (*clustering*) e deduplicação de perguntas repetidas de usuários.
- Sistemas de busca, ranqueamento e recuperação semântica de informação.

## 🚫 Quando não usar

- Tarefas de programação e código-fonte, onde a semântica depende da execução lógica rígida ([[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional]]).
- Casos em que a presença ou ausência de uma palavra de negação minúscula (ex.: "não aprovado" vs. "aprovado") altera 100% o valor do negócio, pois modelos de embedding médios podem atribuir alta similaridade de cosseno a frases opostas que compartilham quase todas as outras palavras.

## ⚠️ Limitações e armadilhas

- **Custo computacional adicional:** Gerar embeddings densos em tempo real para milhares de textos exige chamadas de GPU adicionais ou faturas de APIs de embedding.
- **A armadilha da negação:** Frases semanticamente antagônicas como `"Vamos comer, vovó"` e `"Vamos comer a vovó"` podem gerar embeddings com alta similaridade de cosseno em certos modelos por compartilharem as mesmas palavras-chave, apesar do sentido totalmente divergente.

## 🔍 Comparações

| Dimensão | Similaridade Lexical | Similaridade Semântica |
|---|---|---|
| **Representação dos dados** | Caracteres discretos e n-grams | Vetores contínuos em espaço latente denso |
| **Tolerância a paráfrases** | Nula | Altíssima |
| **Velocidade de cálculo** | Quase instantânea (CPU simples) | Mais lenta (exige inferência de modelo de embedding) |
| **Dependência de modelo** | Nenhuma (função matemática pura) | Totalmente dependente do modelo de embedding escolhido |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O usuário pergunta a um bot de atendimento: `"Qual é o valor da assinatura?"`. O banco de suporte contém a resposta canônica de referência: `"A mensalidade custa vinte reais"`.
O modelo gera como resposta: `"O plano sai por R$ 20,00 por mês"`.

- O cálculo de sobreposição lexical (ROUGE) falha porque "plano", "sai", "R$" e "mês" não aparecem na referência.
- O pipeline de **Similaridade Semântica** converte ambas as frases em vetores de 1536 dimensões via modelo de embedding. O cálculo de cosseno entre os dois vetores atinge $0{,}94$, permitindo ao pipeline aprovar automaticamente a resposta da IA como correta.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/embeddings.md|Embeddings]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]

### Alternativas

- [[redes/ai-engineering/conceitos/similaridade-lexical.md|Similaridade Lexical]]
- [[redes/ai-engineering/conceitos/correcao-funcional.md|Correção Funcional (pass@k)]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 132–134
- **Evidência:** Chip Huyen formaliza a similaridade semântica através de embeddings e similaridade de cosseno, citando ferramentas como BERTScore e MoverScore e contrapondo-a aos limites das métricas lexicais com o exemplo de frases como "Let's eat, grandma" e "Let's eat grandma".
- **Confiança:** Alta

## ❓ Perguntas de revisão

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

# 🧠 Embeddings

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 134–136

## 📝 Definição

### Definição formal

Um **Embedding** é uma representação numérica contínua em formato de vetor de ponto flutuante de dimensão fixa $d$ ($d \in \mathbb{R}^D$, tipicamente entre 100 e 10.000 dimensões) que mapeia entidades discretas complexas e não estruturadas (como palavras, frases inteiras, documentos, imagens ou áudios) para um espaço latente contínuo de menor dimensionalidade, estruturado de modo que a proximidade geométrica entre dois vetores reflita a similaridade semântica ou conceitual entre as entidades correspondentes no mundo real.

### Em linguagem simples

É a "impressão digital matemática" de uma ideia. O computador não sabe o que é um gato ou uma receita de bolo, mas ele sabe transformar essas coisas em uma lista de centenas de números decimais. Se duas coisas têm significados parecidos (como "médico" e "hospital"), as suas listas de números serão muito parecidas e ficarão pertinho uma da outra dentro desse mapa matemático.

### Escopo e distinções

Não se restringe a palavras isoladas (como os históricos Word2Vec e GloVe). Na era dos modelos de fundação, compreende embeddings de documentos inteiros e **espaços de embedding multimodais conjuntos** (como o modelo CLIP da OpenAI), onde um texto descritivo e uma fotografia de uma cena são projetados exatamente no mesmo espaço vetorial.

## 🧩 Problema que resolve

Resolve o problema da representação de dados não estruturados para máquinas. Palavras em linguagem natural e pixels em imagens são dados brutos discretos e de dimensionalidade espacial gigantesca que não permitem operações matemáticas diretas de comparação de significado. Embeddings comprimem esses dados em vetores compactos que viabilizam cálculos instantâneos de similaridade, agrupamento, busca e classificação.

## 💡 Intuição

Pense em um mapa cartográfico tridimensional:

- A cidade de São Paulo e a cidade de Campinas estão em coordenadas geográficas muito próximas no mapa ($X_1, Y_1, Z_1 \approx X_2, Y_2, Z_2$) porque compartilham o mesmo relevo e proximidade física. Tóquio fica do outro lado do globo com coordenadas completamente diferentes.

O espaço de embedding é um mapa similar, só que em vez de ter 3 dimensões, tem 1.536 dimensões, e em vez de mapear cidades geográficas, mapeia conceitos do conhecimento humano.

## ⚙️ Como funciona

Modelos especializados de embedding convertem fluxos de dados brutos em vetores normalizados:

### Etapas

1. **Passagem pelo codificador:** O texto ou imagem passa por uma rede neural dedicada (como um bloco encoder do Transformer ou Vision Transformer).
2. **Compressão contextual:** Camadas de atenção cruzada capturam a relação entre todos os elementos internos da entrada.
3. **Agrupamento (*Pooling*):** As representações de todos os tokens são condensadas em um único vetor consolidado (frequentemente através da extração do token inicial `[CLS]` ou por média ponderada de ativações).
4. **Normalização $L_2$:** O vetor final é normalizado para ter norma euclidiana igual a 1, simplificando o cálculo de similaridade de cosseno a um simples produto escalar rápido.
5. **Projeção Multimodal Conjunta (caso do CLIP):** Textos passam por um codificador de texto e fotos por um codificador visual; uma camada linear projeta ambos no mesmo espaço unificado, alinhando a foto de um cachorro com o texto `"um cachorro correndo no parque"`.

### Entradas e saídas

- **Entradas:** String textual de comprimento variável ou arquivo binário de imagem.
- **Saídas:** Vetor numérico estático de dimensão fixa (ex.: array de 1536 floats de 32 ou 16 bits).

## 📐 Formulação matemática

Seja $\mathcal{X}$ o espaço de entrada e $\mathbb{R}^d$ o espaço latente de embedding. O modelo de embedding atua como a função de mapeamento paramétrica:

$$e = \phi(x; \theta) \in \mathbb{R}^d$$

No modelo multimodal **CLIP** (Radford et al., 2021), utilizam-se dois codificadores simultâneos ($f_{\text{texto}}$ e $f_{\text{imagem}}$) com matrizes de projeção $W_t$ e $W_i$:

$$e_{\text{texto}} = f_{\text{texto}}(T) W_t, \quad e_{\text{imagem}} = f_{\text{imagem}}(I) W_i$$

A função de perda contrastiva de InfoNCE maximiza a similaridade dos pares verdadeiros $(I_k, T_k)$ em um lote de tamanho $B$:

$$\mathcal{L} = -\sum_{k=1}^B \log \frac{\exp\Big(\text{sim}(e_{\text{imagem}}^{(k)}, e_{\text{texto}}^{(k)}) / \tau\Big)}{\sum_{j=1}^B \exp\Big(\text{sim}(e_{\text{imagem}}^{(k)}, e_{\text{texto}}^{(j)}) / \tau\Big)}$$

## 🧱 Hipóteses e condições de validade

- A densidade informativa da entrada deve caber na capacidade dimensional do vetor; tentar comprimir um livro inteiro de 500 páginas em um único vetor de 512 floats causa perda maciça de detalhes específicos.

## ✅ Quando usar

- Alimentação de bancos de dados vetoriais para o componente de recuperação de sistemas de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]].
- Busca de imagens por texto (*text-to-image search*) e catalogação automatizada.
- Agrupamento (*clustering*) de documentos não rotulados e detecção de anomalias semânticas.
- Cálculo de [[redes/ai-engineering/conceitos/similaridade-semantica.md|similaridade semântica]] para avaliação de saídas de IA.

## 🚫 Quando não usar

- Busca estrita por termos alfanuméricos exatos (números de CPF, códigos de rastreamento de carga, nomes raros de medicamentos), onde a busca lexical tradicional por palavras exatas (BM25) é superior aos vetores densos.

## ⚠️ Limitações e armadilhas

- **Opacidade visual:** Olhar para uma lista de 1.536 números não dá ao desenvolvedor nenhuma intuição direta sobre o que o modelo aprendeu; entender falhas exige testes funcionais.
- **Custo de armazenamento em massa:** Indexar centenas de milhões de vetores de alta dimensão consome dezenas de gigabytes de RAM em bancos vetoriais, exigindo técnicas de quantização vetorial.

## 🔍 Comparações

| Modelo de Embedding | Modalidade | Dimensionalidade Típica | Caso de Uso Dominante |
|---|---|---|---|
| **BERT (base/large)** | Texto puro | 768 / 1024 dimensões | Classificação e NER |
| **OpenAI text-embedding-3** | Texto puro | 1536 / 3072 dimensões | Recuperação geral em RAG |
| **CLIP (OpenAI)** | Texto e Imagem | 512 dimensões compartilhadas | Busca visual e ancoragem de LMMs |
| **ImageBind (Meta)** | 6 modalidades conjuntas | Espaço unificado multi-sensorial | Pesquisa multimodal avançada |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um aplicativo de fotos possui um milhão de imagens sem nenhuma legenda ou tag manual.
O sistema processa cada foto pelo codificador visual do **CLIP**, gerando um vetor de 512 números para cada imagem e armazenando esses vetores em um banco de dados.
Quando o usuário digita na barra de pesquisa: `"Pescador no pôr do sol"`, o sistema passa esse texto pelo codificador de texto do CLIP, que devolve um vetor com números extremamente parecidos com os das fotos onde há barcos e luz alaranjada no mar. O sistema calcula a similaridade em milissegundos e exibe as fotos perfeitas sem que ninguém tenha precisado escrever a palavra "pescador" em nenhuma delas.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/similaridade-semantica.md|Similaridade Semântica]]
- [[redes/ai-engineering/conceitos/modelo-multimodal.md|Modelo Multimodal]]

### Alternativas

- Representações esparsas tradicionais (*One-Hot Encoding*, TF-IDF).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 134–136
- **Evidência:** Chip Huyen introduz formalmente o conceito de embeddings como vetores de dimensão reduzida para representar significado, lista tamanhos comuns de modelos (BERT, OpenAI, Cohere) e detalha a arquitetura do CLIP e do ImageBind para espaços de representação conjunta inter-modalidades.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é um embedding no contexto do aprendizado de máquina e como ele mapeia a semântica de dados não estruturados?
2. O que significa afirmar que um espaço de embedding multimodal conjunto (como o do CLIP) alinha texto e imagens?
3. Quais são as dimensões vetoriais típicas encontradas em modelos de embedding contemporâneos?
4. Como o treinamento contrastivo com a perda de InfoNCE permite alinhar pares de texto e imagem sem anotação humana manual direta?
5. Por que a busca por palavras-chave exatas (como números de série) costuma falhar quando implementada puramente sobre embeddings densos?
6. Como os embeddings viabilizam o funcionamento da busca vetorial dentro do padrão arquitetural de RAG?
7. Qual é o benchmark padrão da indústria mencionado no capítulo para avaliar e comparar a qualidade de modelos de embedding de texto (MTEB)?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 IA como Juiz (AI-as-a-Judge)

**Rede:** `ai-engineering`   **Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 136–148

## 📝 Definição

### Definição formal

A metodologia de **IA como Juiz** (*AI-as-a-Judge* ou *LLM-as-a-Judge*) consiste no uso de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] configurado via engenharia de prompt especializada ou ajuste fino para atuar como avaliador automatizado de saídas geradas por outros modelos ou sistemas cognitivos, emitindo pontuações escalares, classificações qualitativas ou julgamentos de preferência acompanhados de justificativas analíticas em linguagem natural.

### Em linguagem simples

É usar uma IA inteligente (como o GPT-4) para corrigir as tarefas de outras IAs menores ou mais baratas. Em vez de contratar uma equipe de humanos para ler milhares de respostas e dar notas, você cria uma instrução com regras bem claras de avaliação e manda a IA juiz dizer quem acertou, quem errou e explicar o porquê de cada nota.

### Escopo e distinções

Um juiz de IA não é apenas um modelo bruto; **é um sistema composto por um modelo, uma temperatura calibrada e um prompt de julgamento contendo uma rubrica estrita**. Alterar qualquer um desses elementos resulta em um juiz diferente. Pode operar com ou sem textos de referência humana (*reference-free* vs. *reference-based*).

## 🧩 Problema que resolve

Resolve o gargalo de escala e custo da avaliação humana para saídas abertas. Humanos custam dezenas de dólares por hora, cansam-se com rapidez e levam semanas para avaliar um conjunto robusto de dados. A IA como juiz executa milhares de avaliações por minuto a uma fração mínima do custo, permitindo que times de engenharia auditem aplicações a cada novo commit de código.

## 💡 Intuição

Pense em uma banca examinadora de vestibular:

- Contratar 50 professores universitários para ler todas as redações de simulados semanais de uma escola é financeiramente inviável (**avaliação puramente humana**).
- Um programa comum de computador que conta palavras não serve para avaliar redação (**métricas lexicais como BLEU**).
- A **IA como Juiz** atua como um professor-assistente digital incansável: ele lê a redação do aluno, consulta a folha de critérios oficiais do exame (**a rubrica no prompt**), confere se o tema foi respeitado, aponta onde houve fuga de contexto e atribui uma nota de 1 a 5 explicando o motivo de cada desconto de ponto.

## ⚙️ Como funciona

O processo desdobra-se em três modalidades paradigmáticas de execução:

### Etapas

1. **Seleção do modo de julgamento:**
   - **Pontual (*Pointwise*):** Avalia uma resposta isolada atribuindo uma nota (ex.: escala Likert de 1 a 5);
   - **Com referência:** Compara a resposta gerada com um gabarito ideal e avalia a consistência factual;
   - **Comparativa (*Pairwise*):** Compara as respostas A e B de dois modelos para o mesmo comando e declara qual é a vencedora.
2. **Construção da Rubrica no Prompt:** O prompt do juiz estabelece a definição inequívoca do critério avaliado (ex.: *relevância*, *alucinação*, *tom de voz*), fixa a escala de notas e fornece exemplos claros do que justifica uma nota mínima ou máxima (*few-shot*).
3. **Execução de inferência calibrada:** Despacha-se a solicitação para o modelo juiz fixando a temperatura estritamente em $T = 0$ para maximizar a consistência.
4. **Extração de notas e justificativas:** O juiz emite a nota em formato estruturado (JSON) acompanhado da cadeia de raciocínio explicativa (*rationale*).
5. **Auditoria por amostragem:** Engenheiros humanos revisam periodicamente uma fatia das notas da IA juiz para detectar desvios.

### Entradas e saídas

- **Entradas:** Pergunta original, resposta gerada pelo sistema alvo, contexto (se houver) e rubrica de julgamento.
- **Saídas:** Escore escalar/categórico e justificativa em linguagem natural.

## 📐 Formulação matemática

Em uma avaliação pontual sob o critério $C$ e uma escala de notas $\mathcal{S} = \{1, 2, 3, 4, 5\}$, o juiz modela a probabilidade condicional da pontuação $s$ e de sua explicação $E$:

$$P(s, E \mid x, y, \mathcal{R}_C; \theta_{\text{juiz}})$$

Onde:

- $x$ é a pergunta do usuário;
- $y$ é a resposta sendo julgada;
- $\mathcal{R}_C$ é a rubrica detalhada do critério $C$.

Estudos empíricos (Zheng et al., 2023, no benchmark MT-Bench) comprovaram que a taxa de concordância entre o GPT-4 atuando como juiz e especialistas humanos atinge até $85\%$, superando a concordância observada entre humanos não especialistas ($81\%$).

## 🧱 Hipóteses e condições de validade

- O modelo que atua como juiz deve possuir capacidade analítica e de raciocínio igual ou superior à do modelo que está sendo avaliado (salvo no caso de [[redes/ai-engineering/conceitos/modelos-de-preferencia-e-juizes-especializados.md|juízes especializados de escopo estreito]]).
- A rubrica de pontuação deve ser estritamente explícita; critérios vagos como "avalie se o texto é bom" geram notas com variância incontrolável.

## ✅ Quando usar

- Avaliação contínua de regressão em pipelines de integração contínua (CI/CD) de engenharia de IA.
- Avaliação de consistência factual em sistemas de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]] corporativos onde não existem gabaritos estáticos humanos.
- Geração automatizada de dados de preferência para etapas de pós-treinamento (*RLAIF*).

## 🚫 Quando não usar

- Em decisões judiciais, concessão automática de crédito ou diagnósticos médicos diretos de missão crítica sem qualquer revisão humana de conformidade legal.
- Em tarefas onde uma métrica determinística e exata existe e pode ser computada a custo zero ([[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional de código]]).

## ⚠️ Limitações e armadilhas

- **Inconsistência estocástica:** Juízes de IA podem atribuir notas diferentes para o mesmo texto se o prompt sofrer alterações minúsculas ou se a temperatura não estiver travada em zero.
- **Sobretaxa de latência e custos:** Usar o GPT-4 para avaliar cada resposta gerada pelo GPT-4 dobra a fatura mensal de API da aplicação.
- **Vieses cognitivos estruturais:** Juízes de IA sofrem de distorções previsíveis detalhadas no conceito de [[redes/ai-engineering/conceitos/vieses-de-avaliacao-por-ia.md|Vieses de Avaliação por IA]].

## 🔍 Comparações

| Dimensão | Avaliadores Humanos Especialistas | IA como Juiz (ex.: GPT-4) |
|---|---|---|
| **Custo por amostra** | Elevado ($3,50 a centenas de dólares) | Centavos ou frações de centavo |
| **Tempo para 10.000 testes** | Semanas a meses | Minutos a poucas horas |
| **Consistência** | Sujeita a humor, fadiga e turnos | Alta (com $T=0$ e rubrica sólida) |
| **Capacidade de Auditoria** | Difícil padronizar explicações | Explicações detalhadas para toda nota |
| **Vieses** | Subjetividade humana e viés de recência | Auto-preferência, verbosidade e posição |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um engenheiro altera o prompt de um assistente de viagens e quer saber se o novo prompt gera respostas mais úteis.
Ele dispara um conjunto de 500 perguntas para o modelo novo. Em seguida, um script envia a pergunta e a resposta para o **GPT-4 atuando como juiz**, com o seguinte comando de sistema: `"Você é um avaliador de suporte ao cliente. Avalie a utilidade da resposta em uma escala de 1 a 5. Uma resposta nota 5 deve sugerir horários de voos reais e bairros específicos para hospedagem. Retorne sua resposta em formato JSON: {"nota": int, "motivo": string}"`.
Em 3 minutos, o juiz processa as 500 respostas, entrega as notas consolidadas e aponta que a utilidade média subiu de $3{,}8$ para $4{,}6$, comprovando com dados que a alteração de engenharia foi bem-sucedida.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/vieses-de-avaliacao-por-ia.md|Vieses de Avaliação por IA]]
- [[redes/ai-engineering/conceitos/modelos-de-preferencia-e-juizes-especializados.md|Modelos de Preferência e Juízes Especializados]]
- [[redes/ai-engineering/conceitos/avaliacao-comparativa.md|Avaliação Comparativa (Pairwise)]]

### Alternativas

- Avaliação por painéis manuais de rotuladores humanos.
- [[redes/ai-engineering/conceitos/similaridade-semantica.md|Similaridade Semântica]] direta via cosseno.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 136–148
- **Evidência:** Chip Huyen destaca o crescimento meteórico da IA como juiz (presente em 58% das avaliações na plataforma LangChain em 2023), citando o artigo clássico do MT-Bench (Zheng et al., 2023) e do AlpacaEval (Dubois et al., 2023) e alertando que nunca se deve confiar em um juiz sem ter visibilidade plena do seu modelo e prompt subjacentes.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a definição de IA como Juiz (*AI-as-a-Judge*) e quais são suas três principais modalidades operacionais?
2. Por que o conceito de juiz de IA abrange não apenas o modelo, mas também o prompt da rubrica e a temperatura de inferência?
3. Quais são as vantagens de custo e velocidade proporcionadas por juízes neurais em comparação com anotadores humanos de crowdsourcing?
4. Como a pesquisa científica valida a confiabilidade de juízes de IA ao correlacioná-los com preferências de especialistas humanos?
5. Qual é o papel da elaboração de rubricas detalhadas e exemplos *few-shot* no prompt de um juiz de IA?
6. Por que é recomendável travar a temperatura em $T=0$ ao executar chamadas de avaliação automatizada?
7. Quais são as principais desvantagens financeiras e de latência geradas pela inserção de juízes de IA dentro de pipelines de produção em tempo real?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Vieses de Avaliação por IA

**Rede:** `ai-engineering`   **Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 144–145

## 📝 Definição

### Definição formal

Os **Vieses de Avaliação por IA** (*Biases of AI as a Judge*) são distorções estatísticas, estruturais e comportamentais sistemáticas e reprodutíveis manifestadas por modelos de fundação quando empregados na função de julgamento avaliativo, levando à atribuição de pontuações que não refletem a qualidade factual ou intrínseca das saídas avaliadas. 

Os três vieses canônicos documentados na literatura técnica são:

1. **Viés de Auto-preferência (*Self-bias*):** A tendência estatística de um modelo favorecer sistematicamente saídas geradas por ele mesmo ou por modelos da mesma família de arquitetura e alinhamento;
2. **Viés de Posição (*Position bias*):** A assimetria de julgamento induzida pela ordem em que os candidatos são apresentados no prompt, com forte favorecimento para a primeira opção apresentada (*first-position bias*);
3. **Viés de Verbosidade (*Verbosity bias*):** A forte propensão de juízes neurais atribuírem notas superiores a respostas extensas, detalhadas e prolixas, mesmo quando contêm erros factuais ou quando uma resposta concisa seria superior.

### Em linguagem simples

São os "pontos cegos" e preconceitos matemáticos que uma IA examinadora tem na hora de dar notas. Uma IA julgando tende a achar que os próprios textos dela são os melhores do mundo, tende a votar no primeiro candidato que aparece na folha de teste e quase sempre dá nota mais alta para quem escreveu uma redação enorme e enrolada, mesmo que uma resposta curta de duas linhas estivesse muito mais certa.

### Escopo e distinções

Não se confundem com preconceitos sociais ou discriminação de gênero e raça nos dados de treinamento (embora também possam ocorrer). Trata-se de vieses algorítmicos ligados à mecânica da atenção e à distribuição estatística de preferências aprendidas no pós-treinamento.

## 🧩 Problema que resolve

Mapear esses vieses resolve a armadilha de aceitar pontuações de juízes de IA como verdades incontestáveis. Saber que esses vieses existem permite aplicar contramedidas de engenharia (como inverter a ordem dos candidatos, penalizar a extensão do texto ou calibrar notas cruzadas) para purificar os dados de avaliação.

## 💡 Intuição

Pense em um concurso de oratória com um jurado humano cansado:

- Se um orador fala por 20 minutos usando palavras difíceis e postura imponente, o jurado assume que ele é muito inteligente, mesmo que o discurso não tenha chegado a conclusão nenhuma (**viés de verbosidade**).
- Se o jurado assiste a 10 apresentações seguidas, ele presta atenção no primeiro concorrente da manhã e já está exausto no último (**viés de posição**).
- E se um dos concorrentes for aluno formado na mesma faculdade que o jurado estudou, o jurado sentirá uma simpatia inconsciente pelo seu estilo de fala (**viés de auto-preferência**).

## ⚙️ Como funciona

Cada viés possui um mecanismo subjacente específico:

### Etapas

1. **Operação do Viés de Auto-preferência:** A rede neural do juiz foi treinada com a mesma distribuição probabilística de seus próprios pesos. Quando ele lê um texto gerado por ele mesmo, as palavras seguintes são aquelas com as maiores probabilidades em sua própria matriz de atenção, gerando alta familiaridade intrínseca e resultando em notas infladas (estudos mostram que o GPT-4 se favorece com $+10\%$ de vitórias e o Claude-v1 com $+25\%$).
2. **Operação do Viés de Posição:** A atenção do Transformer tende a dedicar mais peso aos primeiros tokens estruturados que aparecem no contexto. Em disputas par a par (A vs. B), a opção apresentada como "Opção A" ganha estatisticamente mais disputas do que quando colocada como "Opção B".
3. **Operação do Viés de Verbosidade:** O juiz confunde extensão com completeza de raciocínio. Estudos (Wu e Aji, 2023) comprovaram que juízes de ponta preferem respostas de 100 palavras com erros factuais graves a respostas perfeitas de 50 palavras sem erros.
4. **Contramedidas de Engenharia:**
   - Para anular o viés de posição: executa-se cada avaliação duas vezes, invertendo as ordens (A vs B e depois B vs A), aceitando o resultado apenas em caso de coerência mútua;
   - Para o viés de verbosidade: impõe-se limites estritos de caracteres ou instruções que penalizam prolixidade.

### Entradas e saídas

- **Entradas:** Par de respostas avaliadas por um juiz neural.
- **Saídas:** Escore potencialmente distorcido que exige algoritmos de desenviesamento (*debiasing*).

## 📐 Formulação matemática

O viés de posição entre os modelos $M_1$ e $M_2$ é formalizado pela assimetria na taxa empírica de vitória $P(\text{vitória})$ em função da posição de apresentação $\pi \in \{\text{Posição 1}, \text{Posição 2}\}$:

$$P\Big(M_1 \succ M_2 \mid \pi(M_1) = 1\Big) \neq 1 - P\Big(M_2 \succ M_1 \mid \pi(M_2) = 1\Big)$$

O desenviesamento por permutação calcula a preferência agregada balanceando as duas probabilidades condicionais de ordem:

$$P_{\text{balanceado}}(M_1 \succ M_2) = \frac{1}{2} \left[ P(M_1 \succ M_2 \mid M_1 \text{ em 1}) + P(M_1 \succ M_2 \mid M_1 \text{ em 2}) \right]$$

## 🧱 Hipóteses e condições de validade

- A inversão de posições só funciona como neutralizadora do viés se o juiz não cair em impasses repetidos (*draws* induzidos pela contradição de ordem).

## ✅ Quando usar

- Auditoria obrigatória de qualquer benchmark ou pipeline de CI/CD que utilize [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como juiz]].
- Concepção de diretrizes de alinhamento e curadoria de dados sintéticos de preferência para evitar colapso de extensão em modelos novos.

## 🚫 Quando não usar

- Em avaliações exatas determinísticas ([[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional]]), pois o interpretador de código não sofre de vieses estilísticos nem favorece códigos mais longos.

## ⚠️ Limitações e armadilhas

- **A inflação da prolixidade corporativa:** Modelos treinados com dados de preferência gerados por juízes de IA tornam-se progressivamente mais prolixos e cansativos a cada geração se o viés de verbosidade não for neutralizado na raiz.
- **Custo dobrado:** A técnica padrão de desenviesamento de posição exige rodar a avaliação duas vezes com ordem invertida, duplicando a fatura de tokens da IA juiz.

## 🔍 Comparações

| Viés do Juiz | Como se manifesta? | Contramedida de Engenharia | Custo da Correção |
|---|---|---|---|
| **Auto-preferência** | Dá notas mais altas para si mesmo | Usar juízes de fornecedores concorrentes ou modelos neutros | Baixo |
| **Primeira Posição** | Prefere a primeira opção apresentada no prompt | Avaliação simétrica permutada (executar A/B e B/A) | Dobra o custo de inferência |
| **Verbosidade** | Prefere respostas longas e enroladas a curtas e exatas | Normalização de tamanho e penalidade explícita na rubrica | Mínimo |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma equipe quer comparar se o Modelo X é melhor que o Modelo Y para resumir laudos médicos.
O comando é: `"Qual é o órgão afetado?"`.

- O Modelo X responde em 4 palavras: `"O rim esquerdo (nefrite)"`. (100% correto).
- O Modelo Y responde em 120 palavras: `"Ao analisar detidamente o prontuário sob a ótica da nefrologia moderna, observa-se que o paciente apresenta uma condição inflamatória no fígado, que é um órgão vital..."` (Errou feio o órgão, mas usou termos bonitos e texto longo).

O **Juiz de IA descalibrado** lê as duas opções. Influenciado pelo **viés de verbosidade**, ele atribui a vitória ao Modelo Y, afirmando que Y foi "mais detalhado, completo e atencioso", ignorando que Y errou a informação clínica básica.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/avaliacao-comparativa.md|Avaliação Comparativa (Pairwise)]]
- [[redes/ai-engineering/conceitos/modelos-de-preferencia-e-juizes-especializados.md|Modelos de Preferência e Juízes Especializados]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (trata-se de limitações intrínsecas a serem mitigadas).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 144–145
- **Evidência:** O texto descreve em detalhe os vieses de self-bias (GPT-4 favorecendo-se em 10% e Claude-v1 em 25% no MT-Bench), first-position bias (oposto ao recency bias dos humanos) e verbosity bias (pesquisas de Wu e Aji comprovando que juízes preferem respostas de 100 palavras erradas a respostas de 50 palavras certas).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são os três vieses canônicos manifestados por modelos de fundação quando atuam como juízes de avaliação?
2. Como funciona o viés de auto-preferência (*self-bias*) e qual é a sua magnitude empírica documentada no GPT-4 e no Claude?
3. Por que o viés de posição dos LLMs (que favorece a primeira opção) é o oposto exato do viés de recência típico dos seres humanos?
4. Como o viés de verbosidade pode induzir uma equipe a lançar um modelo que comete mais erros factuais do que o modelo anterior?
5. Qual técnica matemática e algorítmica de engenharia é recomendada para neutralizar o viés de primeira posição em testes comparativos?
6. Qual é o impacto financeiro da aplicação de rotinas de desenviesamento por permutação sobre a fatura de tokens da aplicação?
7. Por que modelos de fundação mais modernos e maiores tendem empiricamente a sofrer menos do viés de verbosidade do que modelos mais antigos (como o GPT-3.5)?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Modelos de Preferência e Juízes Especializados

**Rede:** `ai-engineering`   **Área:** `modelagem`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 146–148

## 📝 Definição

### Definição formal

Os **Modelos de Preferência e Juízes Especializados** (*Specialized AI Judges and Preference Models*) são arquiteturas neurais de porte compacto (frequentemente de centenas de milhões a poucos bilhões de parâmetros) treinadas e calibradas de forma supervisionada exclusivamente para tarefas de avaliação, pontuação ou predição de preferência humana, operando com rubricas ou esquemas de saída estritos sem o custo, a lentidão ou a instabilidade de modelos de fundação generalistas gigantescos. 

Subdividem-se em três categorias funcionais primárias:

1. **Modelos de Recompensa (*Reward Models*):** Recebem um par `(prompt, resposta)` e emitem uma pontuação escalar contínua de qualidade (ex.: Cappy da Google, com 360M de parâmetros);
2. **Juízes baseados em referência:** Avaliam uma resposta candidata contra um gabarito ideal de referência e uma rubrica explícita (ex.: BLEURT e Prometheus);
3. **Modelos de Preferência (*Preference Models*):** Recebem `(prompt, resposta_1, resposta_2)` e predizem diretamente qual das duas opções os humanos prefeririam, gerando explicações analíticas integradas (ex.: PandaLM e JudgeLM).

### Em linguagem simples

Em vez de gastar uma fortuna contratando o maior modelo de IA do mundo (como o GPT-4) para ficar dando notas nas tarefas da sua empresa, você usa um modelo "pequeno e especialista", treinado apenas para ser juiz. Ele não sabe contar piadas nem programar, mas sabe avaliar perfeitamente se um texto está bem escrito ou se uma resposta é melhor que a outra, rodando em servidores locais com custo e velocidade excelentes.

### Escopo e distinções

Diferenciam-se da [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como juiz generalista]] (que depende de prompts longos em LLMs gigantescos). Modelos de preferência possuem matrizes ajustadas especificamente para discernir qualidade e prever decisões humanas de forma estável.

## 🧩 Problema que resolve

Resolve a barreira econômica e de latência da avaliação por IA. Usar LLMs gigantescos como juízes dobra ou triplica os custos de inferência da aplicação e adiciona segundos de atraso no tempo de resposta. Juízes especializados de 360M a 7B de parâmetros realizam o mesmo trabalho de pontuação consumindo uma fração ínfima de memória e milissegundos de processamento.

## 💡 Intuição

Pense em um campeonato de ginástica olímpica. Você não precisa contratar o atleta campeão mundial que sabe fazer todos os saltos mortais acrobáticos mais complexos para ser o juiz de mesa. Você pode contratar um árbitro dedicado que já tem idade avançada e não consegue mais dar nenhum salto (**o modelo pequeno especializado**), mas que tem os olhos cirurgicamente treinados para bater o olho no movimento e dar a nota exata baseada no livro oficial de regras da competição. Julgar é cognitivamente mais simples do que gerar.

## ⚙️ Como funciona

O pipeline varia conforme a classe funcional do modelo especialista:

### Etapas

1. **Abordagem de Modelo de Recompensa (ex.: Cappy):**
   - Recebe o prompt $x$ e a resposta gerada $y$;
   - Uma rede leve (ex.: baseada em RoBERTa de 360M de parâmetros) processa o texto e passa sua representação por uma cabeça linear de regressão;
   - Emite um valor contínuo no intervalo de $[0, 1]$ refletindo a probabilidade de correção factual.
2. **Abordagem de Juiz com Referência (ex.: Prometheus):**
   - Recebe o prompt, a resposta gerada, uma resposta de referência perfeita e a rubrica textual de 1 a 5;
   - O modelo gera a nota discreta e a justificativa sintética de forma determinística.
3. **Abordagem de Modelo de Preferência (ex.: PandaLM):**
   - Recebe as respostas dos Modelos A e B para a mesma pergunta;
   - A rede processa os dois textos e gera uma saída estruturada identificando o vencedor (`1`, `2` ou `Empate`), acompanhada dos motivos técnicos da decisão.

### Entradas e saídas

- **Entradas:** Pares ou trios de dados de avaliação `(prompt, resposta)` ou `(prompt, resposta_A, resposta_B)`.
- **Saídas:** Escore escalar contínuo, classe vencedora ou parecer estruturado com justificativa.

## 📐 Formulação matemática

Para um modelo de preferência $P_\phi$, o objetivo é maximizar a precisão na predição da escolha humana $y^* \in \{1, 2\}$ entre duas respostas $y_1$ e $y_2$:

$$y^* = \arg\max_{i \in \{1, 2\}} P_\phi\Big(\text{Vencedor} = i \;\Big|\; x, y_1, y_2\Big)$$

Em modelos de recompensa escalares $r_\psi$, o sistema mapeia a qualidade para uma curva calibrada:

$$s = r_\psi(x, y) \in [0, 1]$$

Onde $s$ atua como o estimador não linear que substitui o julgamento humano na triagem de qualidade de inferência ou na filtragem de dados de pós-treinamento.

## 🧱 Hipóteses e condições de validade

- Assume a premissa de que a capacidade de **discernir e avaliar** um resultado é uma tarefa de complexidade computacional inferior à capacidade de **sintetizar e gerar** a resposta a partir do nada (princípio análogo à teoria da complexidade computacional, onde verificar uma solução polinomial é mais simples do que encontrá-la).

## ✅ Quando usar

- Filtros de guardrail de saída e segurança em tempo real onde a latência permitida para a checagem é inferior a 200 milissegundos.
- Geração massiva de dados de preferência para treinamento de novos modelos via DPO/RLAIF sem estourar orçamentos de computação.
- Estratégias de inferência com [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Best-of-N)]], onde o juiz especializado avalia rascunhos em paralelo.

## 🚫 Quando não usar

- Para avaliar raciocínios inéditos de ponta que exigem raciocínio causal de múltiplos passos em áreas onde o modelo especialista pequeno não foi treinado.

## ⚠️ Limitações e armadilhas

- **Falta de generalização de domínio:** Um juiz treinado para avaliar resumos jornalísticos pode cometer falhas grotescas ao tentar avaliar se um trecho de código Rust está correto.
- **Ambiguidade de escalas:** Ferramentas como o BLEURT usam escalas confusas e não padronizadas (com notas que podem variar entre $-2{,}5$ e $+1{,}0$), exigindo normalização matemática adicional pelo engenheiro.

## 🔍 Comparações

| Tipo de Juiz | Tamanho Típico | O que recebe na entrada? | Saída Produzida | Custo / Latência |
|---|---|---|---|---|
| **LLM Gigante (GPT-4)** | Centenas de bilhões | Prompt + Rubrica + Texto | Texto livre com nota e justificativa | Alto / Lento |
| **Modelo de Recompensa (Cappy)** | ~360 milhões | Prompt + Resposta | Escore escalar simples $[0, 1]$ | **Mínimo / Ultrarrápido** |
| **Juiz com Rubrica (Prometheus)** | ~7 a 13 bilhões | Prompt + Resposta + Gabarito | Nota de 1 a 5 com justificativa | Médio / Balanceado |
| **Modelo de Preferência (PandaLM)** | ~7 bilhões | Prompt + Resposta A + Resposta B | Escolha do vencedor (A/B/Empate) | Baixo a Médio |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma plataforma corporativa quer selecionar a melhor resposta entre 5 opções geradas em paralelo para cada pergunta de atendimento financeiro ao cliente.

- Se usasse o **GPT-4 como juiz**, cada pergunta custaria 5 vezes mais e demoraria 8 segundos para ser entregue, inviabilizando o produto.
- A equipe implanta localmente o modelo de recompensa **Cappy** (360M de parâmetros) na mesma máquina da GPU. Os 5 rascunhos são gerados; o Cappy lê os 5 textos em apenas 40 milissegundos, atribui notas: `[0.12, 0.45, 0.91, 0.82, 0.30]`, e despacha imediatamente a terceira resposta (nota $0{,}91$) para o cliente, alcançando alta qualidade sem elevar custos de terceiros.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]
- [[redes/ai-engineering/conceitos/avaliacao-comparativa.md|Avaliação Comparativa (Pairwise)]]

### Alternativas

- Uso de modelos de fundação generalistas de grande porte como juízes universais.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|Aprendizado por Reforço com Feedback Humano (RLHF)]] (modelos de recompensa originam-se aqui)
- [[redes/ai-engineering/conceitos/vieses-de-avaliacao-por-ia.md|Vieses de Avaliação por IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 146–148
- **Evidência:** Chip Huyen introduz a pesquisa emergente de juízes pequenos e especializados, detalhando o modelo de recompensa Cappy da Google (360M parâmetros), juízes baseados em referência como Prometheus e BLEURT, e modelos dedicados à predição de preferência como PandaLM e JudgeLM.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que são Juízes Especializados e Modelos de Preferência e qual vantagem fundamental eles oferecem frente a LLMs generalistas?
2. Quais são as três categorias funcionais primárias de juízes especializados detalhadas no texto?
3. Como o modelo de recompensa Cappy (Google, 360M) exemplifica a viabilidade de modelos leves para avaliação?
4. Qual é a premissa cognitiva que justifica o fato de um modelo pequeno ser capaz de avaliar a saída de um modelo substancialmente maior?
5. Como os modelos de preferência (como PandaLM) são utilizados para automatizar a coleta de dados de treinamento de alinhamento?
6. Qual é a principal limitação operacional dos modelos de juiz baseados em referência (como Prometheus e BLEURT)?
7. De que maneira juízes especializados viabilizam a implementação em produção da estratégia de *Best-of-N* com baixa latência?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Avaliação Comparativa (Pairwise)

**Rede:** `ai-engineering`   **Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 148–156

## 📝 Definição

### Definição formal

A **Avaliação Comparativa** (*Comparative Evaluation* ou *Pairwise Evaluation*) é a metodologia de validação empírica na qual dois ou mais modelos de fundação recebem o mesmo prompt simultaneamente e suas respostas são apresentadas lado a lado para que um avaliador (humano ou [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como juiz]]) selecione a melhor saída (*vencedor*), alimentando algoritmos estatísticos de estimação de habilidades latentes (**Elo** ou **Bradley–Terry**) para produzir um ordenamento global (*ranking*) da capacidade relativa dos modelos competidores.

### Em linguagem simples

É o método de campeonato esportivo aplicado à IA. Em vez de pedir para alguém ler um texto e dar uma nota de 1 a 10 (o que é muito difícil e varia de pessoa para pessoa), você coloca as respostas de dois modelos lado a lado de forma anônima e pergunta: "Qual destas duas ficou melhor?". A partir de milhares de votos de "A ganhou de B", uma fórmula matemática calcula quem é o campeão do ranking, como se fosse o ranking mundial de xadrez.

### Escopo e distinções

Diferencia-se da **avaliação pontual (*pointwise*)**, que pontua cada resposta de forma isolada. Também não se confunde com testes A/B convencionais de software: no teste A/B, o usuário vê apenas uma opção por vez; na avaliação comparativa, ele vê as duas opções ao mesmo tempo em disputa direta (*match*). O padrão-ouro global dessa abordagem na indústria é a **LMSYS Chatbot Arena**.

## 🧩 Problema que resolve

Resolve a saturação de benchmarks acadêmicos estáticos e a inconsistência de julgamento humano em notas absolutas. Perguntar se um resumo merece nota "3" ou "4" gera divergências profundas entre avaliadores. No entanto, perguntar qual resumo é superior gera altíssimo consenso. Além disso, a avaliação comparativa **nunca satura**: quando um modelo novo e melhor é lançado, ele simplesmente passa a vencer os antigos, empurrando o ranking para cima sem necessidade de reescrever o teste.

## 💡 Intuição

Pense em escolher o melhor sorvete da cidade:

- Se você for a uma sorveteria na segunda-feira e der uma nota 8 para o sorvete de chocolate, e na sexta-feira for a outra sorveteria e der nota 8 para outro sorvete de chocolate, é muito difícil saber qual era realmente o melhor. O seu humor na sexta-feira mudou a sua nota absoluta.
- Mas se você sentar com os dois potes de sorvete lado a lado, provar uma colherada do sorvete A e uma do sorvete B no mesmo instante, o seu cérebro sabe com clareza imediata qual dos dois tem o sabor mais gostoso (**julgamento comparativo direto**).

## ⚙️ Como funciona

O pipeline organiza partidas e recalcula pontuações continuamente:

### Etapas

1. **Apresentação em teste cego:** O usuário envia uma pergunta na interface (ex.: Chatbot Arena). O sistema seleciona dois modelos anonimizados (Modelo 1 e Modelo 2) para responder em colunas paralelas.
2. **Coleta do voto:** O usuário lê as respostas e vota: `Modelo A é melhor`, `Modelo B é melhor` ou `Empate`.
3. **Revelação e registro:** Os nomes reais dos modelos são revelados ao usuário e o resultado do confronto (*match*) é adicionado ao histórico da base.
4. **Cálculo da probabilidade de vitória:** O sistema monitora a taxa empírica de vitória (*win rate*) de cada par de modelos concorrentes.
5. **Atualização do Algoritmo de Ranking:** Utiliza-se a modelagem de **Bradley–Terry** (ou rating Elo) para estimar um valor de habilidade latente contínua para cada modelo a partir da matriz de vitórias e derrotas.
6. **Publicação da tabela de liderança:** Os modelos são ordenados do mais forte para o mais fraco com seus intervalos de confiança estatística.

### Entradas e saídas

- **Entradas:** Milhares de confrontos par a par `(modelo_A, modelo_B, vencedor)`.
- **Saídas:** Tabela ordenada de liderança (*leaderboard*) com pontuações escalares comparativas calibradas.

## 📐 Formulação matemática

O modelo estatístico clássico de **Bradley–Terry** define que a probabilidade de o modelo $A$ vencer o modelo $B$ ($P(A \succ B)$) é governada por suas habilidades latentes subjacentes $s_A$ e $s_B$:

$$P(A \succ B) = \frac{e^{s_A}}{e^{s_A} + e^{s_B}} = \frac{1}{1 + e^{-(s_A - s_B)}} = \sigma(s_A - s_B)$$

Onde $\sigma$ é a função sigmoide logística.
No algoritmo de **Elo** tradicional, a pontuação de um modelo $R_A$ é atualizada a cada partida disputada com base na diferença entre o resultado real $S_A \in \{1, 0{,}5, 0\}$ e o resultado esperado $E_A = P(A \succ B)$:

$$R_A^{\text{novo}} = R_A^{\text{antigo}} + K \cdot (S_A - E_A)$$

Onde $K$ é a constante de sensibilidade de ajuste da taxa de aprendizado do rating. A LMSYS Chatbot Arena utiliza o modelo de Bradley–Terry resolvido por máxima verossimilhança e re-escalonado para a base Elo clássica (com base de 1000 pontos).

## 🧱 Hipóteses e condições de validade

- **Premissa de Transitividade:** Assume que as preferências são transitivas (se $A \succ B$ e $B \succ C$, então $A \succ C$). Na prática, como comprovado por estudos teóricos, preferências humanas em LLMs podem exibir não-transitividade devido a variações nos prompts e critérios de diferentes avaliadores.
- O volume de confrontos deve ser estatisticamente denso para cobrir as combinações entre todos os pares concorrentes.

## ✅ Quando usar

- Escolha do melhor modelo de fundação para adotar na empresa através de rankings públicos confiáveis e difíceis de fraudar (*gaming-resistant*).
- Validação final de um novo modelo proprietário ou ajustado via finetuning antes de colocá-lo no ar, comparando-o diretamente contra o modelo em produção.
- Geração de dados de comparação para alimentar etapas de pós-treinamento com [[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|RLHF]] ou [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia.md|DPO]].

## 🚫 Quando não usar

- Em tarefas onde a resposta correta é uma verdade factual ou matemática exata e o usuário comum não tem conhecimento para julgar (ex.: perguntar cálculos atuariais e pedir para o usuário votar em qual parece mais bonito pode coroar respostas erradas).

## ⚠️ Limitações e armadilhas

- **Gargalo de Escala Quadrático ($\mathcal{O}(N^2)$):** O número de pares necessários para testar todos os modelos cresce com o quadrado do número de competidores. Para 57 modelos, existem $1.596$ pares distintos, exigindo centenas de milhares de votos para preencher a matriz.
- **Falta de aterramento em produção:** As perguntas digitadas por voluntários na web pública tendem a ser saudações curtas ("oi", "olá") ou charadas lógicas, não refletindo a complexidade de sistemas reais corporativos dotados de RAG e documentos longos.
- **Da preferência relativa à viabilidade absoluta:** Saber que o Modelo B vence o Modelo A em $51\%$ das disputas não diz se o Modelo B é "bom o suficiente" para atender um cliente nem se esse ganho de $1\%$ justifica pagar o dobro na fatura da API.

## 🔍 Comparações

| Característica | Avaliação Pontual (*Pointwise*) | Avaliação Comparativa (*Pairwise*) |
|---|---|---|
| **Formato da tarefa** | Atribuir nota isolada a uma resposta | Escolher a melhor entre duas opções |
| **Facilidade humana** | Difícil (exige calibrar escala de notas) | Intuitiva e de alto consenso |
| **Saturação** | Rápida (modelos atingem a nota máxima) | Inexistente (o teto sobe com novos competidores) |
| **Escalabilidade** | Linear com o número de modelos ($\mathcal{O}(N)$) | Quadrática com o número de modelos ($\mathcal{O}(N^2)$) |
| **Vulnerabilidade a trapaça** | Fácil de fraudar treinando no teste | Extremamente difícil de fraudar (*teste cego*) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma empresa quer decidir se troca seu modelo atual em produção (Modelo A) pelo novo modelo lançado no mercado (Modelo B).
Em vez de confiar nas tabelas de marketing da internet, a equipe programa o sistema interno para rotear $10\%$ das perguntas reais de seus funcionários para os dois modelos ao mesmo tempo. 
Na tela dos funcionários, surgem duas respostas anônimas lado a lado. Após 2.000 confrontos coletados na semana de testes, o algoritmo de **Bradley–Terry** revela que o Modelo B venceu em $68\%$ das partidas em tarefas de redação de e-mails, mas perdeu em $75\%$ dos casos que envolviam cálculos de comissões de vendas. Essa análise comparativa permite à empresa tomar uma decisão cirúrgica sobre onde vale a pena pagar pela troca do modelo.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]
- [[redes/ai-engineering/conceitos/vieses-de-avaliacao-por-ia.md|Vieses de Avaliação por IA]]
- [[redes/ai-engineering/conceitos/modelos-de-preferencia-e-juizes-especializados.md|Modelos de Preferência e Juízes Especializados]]

### Alternativas

- Avaliação Pontual (*Pointwise scoring* de 1 a 5).
- Testes A/B tradicionais desemparelhados de produto.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|Aprendizado por Reforço com Feedback Humano (RLHF)]]
- [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia.md|Otimização Direta de Preferência (DPO)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 148–156
- **Evidência:** Chip Huyen destrincha a mecânica da Chatbot Arena da LMSYS, detalha as formulações dos algoritmos Elo e Bradley–Terry, analisa os limites matemáticos da transitividade e aborda os desafios de representatividade de prompts simples e conversão de win-rates em valor de negócio.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Avaliação Comparativa (*Pairwise*) e qual vantagem fundamental ela apresenta sobre a avaliação pontual de notas?
2. Como funciona a modelagem de probabilidades no algoritmo de Bradley–Terry para derivar o ranking de modelos concorrentes?
3. Por que tabelas de liderança baseadas em testes comparativos cegos (como a Chatbot Arena) são muito mais difíceis de serem burladas ou fraudadas por criadores de modelos?
4. Qual é o problema do crescimento quadrático $\mathcal{O}(N^2)$ no número de confrontos e como algoritmos de pareamento eficiente tentam mitigá-lo?
5. O que é a premissa de transitividade e por que ela é frequentemente violada em avaliações de modelos de fundação no mundo real?
6. Por que utilizar votação comparativa com usuários comuns para avaliar respostas que exigem exatidão factual (como medicina ou matemática) pode produzir dados errôneos?
7. Qual é a principal dificuldade de engenharia ao tentar traduzir uma taxa de vitória de 55% de um modelo em decisões práticas de retorno sobre investimento (ROI) corporativo?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

*Nota gerada a partir do capítulo Capítulo 3 — Evaluation Methodology. A interpretação final deve ser revisada pelo estudante.*
