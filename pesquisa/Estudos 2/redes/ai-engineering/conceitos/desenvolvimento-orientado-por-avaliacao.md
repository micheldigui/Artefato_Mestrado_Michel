# 🧠 Desenvolvimento Orientado por Avaliação (Evaluation-Driven Development)

**Rede:** `ai-engineering`  
**Área:** `metodologia-de-engenharia`

**Rede:** `ai-engineering`  
**Área:** `metodologia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 4 — Avaliando Sistemas de IA
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 4 — Evaluate AI Systems
- Localização: Páginas 160–161

## 📝 Definição

### Definição formal

Uma metodologia de engenharia de software aplicada a sistemas de IA na qual o conjunto de testes, as métricas de sucesso e os critérios de aceitação são rigorosamente definidos e implementados *antes* da construção ou ajuste do código da aplicação e dos prompts.

O **Desenvolvimento Orientado por Avaliação** (*Evaluation-Driven Development* — EDD) é um paradigma de engenharia de software aplicado a sistemas baseados em [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]], diretamente inspirado no desenvolvimento orientado a testes (*Test-Driven Development* — TDD), no qual as métricas de sucesso, as rubricas qualitativas de pontuação, as restrições de conformidade e o pipeline sistemático de avaliação são formalmente especificados e implementados **antes** da construção de prompts, cadeias de recuperação ou ajustes finos do modelo.

### Em linguagem simples

É a prática de estabelecer as regras da prova e o gabarito de correção antes de começar a escrever o código do produto ou ajustar a inteligência artificial.

É a prática de criar o gabarito e os critérios da prova antes de começar a ensinar o aluno. Em vez de sair escrevendo prompts e conectando bancos de dados para depois tentar adivinhar se a IA está boa no "olhômetro", o engenheiro estabelece primeiro como vai medir o acerto, quanto o sistema pode custar e o que é considerado uma resposta inaceitável.

### Escopo e distinções

Inspirado no *Test-Driven Development (TDD)* clássico da engenharia de software, adaptado para lidar com a natureza probabilística e estocástica de modelos de fundação.

Não se confunde com o teste de software tradicional baseado em asserções booleanas puras (`assert x == y`). Em sistemas generativos probabilísticos com saídas abertas, o EDD exige a criação de conjuntos de dados de referência representativos, modelos juízes calibrados e faixas de tolerância estatística vinculadas diretamente ao retorno financeiro ou operacional do caso de uso.

## 🧩 Problema que resolve

Resolve o desenvolvimento desorganizado e baseado em achismos (*vibe check*), onde engenheiros ajustam prompts aleatoriamente sem saber se as mudanças realmente melhoram o sistema ou apenas corrigem um caso isolado.

Resolve a armadilha comum na qual equipes constroem e lançam aplicações de IA impressionantes em demonstrações internas, mas que operam em produção sem que ninguém saiba se estão gerando valor real ou acumulando erros silenciosos. Evita o desperdício financeiro em casos de uso cuja precisão exigida pelo negócio é inalcançável com a tecnologia ou orçamento disponíveis.

## 💡 Intuição

Imagine um arquiteto que desenha a planta e as exigências estruturais de teste de carga de uma ponte antes de começar a amontoar tijolos, garantindo que cada peça colocada cumpra uma meta de segurança verificável.

Imagine construir uma ponte sobre um rio. No desenvolvimento tradicional com TDD, você sabe exatamente a largura em metros e a carga em toneladas que a estrutura deve aguentar antes de comprar o primeiro saco de cimento. Construir IA sem EDD é o equivalente a construir uma ponte improvisada de madeira e depois tentar descobrir se ela aguenta caminhões pesados simplesmente mandando um caminhão passar por cima para ver se desaba.

## ⚙️ Como funciona

O ciclo de vida do EDD estrutura-se em um fluxo iterativo e disciplinado:

### Etapas

1. Mapeamento das necessidades de negócio e tradução em métricas de avaliação quantificáveis.
2. Construção do dataset de teste de referência (composto por casos reais de uso e exemplos difíceis).
3. Definição das rubricas de pontuação e ferramentas automáticas (ex: IA como Juiz ou testes funcionais).
4. Desenvolvimento iterativo do código e dos prompts guiado estritamente pela melhoria contínua nas pontuações do dataset de teste.

1. **Definição dos objetivos de negócio:** Mapeia-se o problema real (ex.: automatizar 50% dos chamados de suporte técnico de primeiro nível).
2. **Estabelecimento dos critérios de avaliação:** Desdobra-se a meta de negócio em critérios técnicos mensuráveis (consistência factual, seguimento de instruções, latência e custo).
3. **Construção da suíte de teste e rubricas:** Coletam-se consultas reais e definem-se diretrizes claras do que constitui notas de 1 a 5 ([[redes/ai-engineering/conceitos/diretrizes-e-rubricas-de-avaliacao.md|rubricas de avaliação]]).
4. **Estabelecimento do limiar de utilidade (*Usefulness Threshold*):** Determina-se a nota mínima que o sistema precisa atingir para ser economicamente viável (ex.: consistência factual $\ge 90\%$).
5. **Desenvolvimento e iteração:** Engenheiros experimentam prompts, RAG e finetuning, usando a suíte como farol contínuo.
6. **Decisão de lançamento ou descarte:** Se o sistema ultrapassar o limiar, é homologado; caso contrário, é descartado antes de incorrer em passivos de produção.

### Entradas e saídas

- Entradas: Requisitos do produto e métricas de desempenho desejadas.
- Saídas: Pipeline de testes automatizado e artefatos de código validados por métricas objetivas.

- **Entradas:** Requisitos de produto, restrições operacionais e dados brutos de interações reais.
- **Saídas:** Pipeline automatizado de testes, relatórios de conformidade e decisões claras de homologação.

## 📐 Formulação matemática

Não possui uma equação matemática isolada; modela-se como um processo de otimização de função objetivo onde o objetivo é maximizar o escore de teste $E$:

$$\max_{\text{Prompt, Modelo, RAG}} E(\text{Pipeline}, D_{teste})$$

Onde:
- $E$: Função de avaliação sistêmica.
- $D_{teste}$: Conjunto de dados de teste de referência fixo.

O valor esperado de negócio $V_{\text{negócio}}$ de implantar uma aplicação de IA sob o paradigma EDD é condicionado à função indicadora do limiar de utilidade $\tau$:

$$V_{\text{negócio}} = \begin{cases} \mathbb{E}[\text{Retorno}(M)] - \text{Custo}(M), & \text{se } \mathcal{S}_{\text{eval}}(M) \ge \tau \\ 0 \text{ (não implantar)}, & \text{se } \mathcal{S}_{\text{eval}}(M) < \tau \end{cases}$$

Onde $\mathcal{S}_{\text{eval}}(M)$ é a pontuação multidimensional agregada obtida pelo sistema $M$ na suíte de avaliação preliminar.

## 🧱 Hipóteses e condições de validade

- Supõe que o conjunto de dados de teste reflete fidedignamente a distribuição estatística e os desafios reais enfrentados pelos usuários em produção.

- A tarefa pretendida deve possuir critérios de qualidade passíveis de formalização ou comparação consensual entre humanos especialistas.
- Existência de dados de teste suficientes para garantir significância estatística ([[redes/ai-engineering/conceitos/dimensionamento-amostral-de-avaliacao.md|dimensionamento amostral]]).

## ✅ Quando usar

- No início de qualquer projeto de engenharia de IA voltado para produção empresarial ou comercial.

- Em todos os projetos corporativos de inteligência artificial generativa com impacto em clientes ou processos internos.
- Decisões estratégicas de priorização de casos de uso na esteira de desenvolvimento de produtos.

## 🚫 Quando não usar

- Em protótipos exploratórios ultra-rápidos de final de semana onde a persistência do software não é necessária.

- Em explorações individuais de aprendizado ou hackathons recreativos de poucas horas onde o único objetivo é a experimentação estética.

## ⚠️ Limitações e armadilhas

- Exige esforço inicial de planejamento e rotulação que pode desacelerar o início do código, o que gera resistência em equipes focadas apenas em entregar protótipos visuais rápidos.

- **Foco exclusivo no mensurável fácil:** A tendência perigosa de avaliar apenas o que é trivial de medir (como métricas de classificação simples), deixando de lado aspectos vitais, mas difíceis de quantificar (como tom de voz empático ou clareza pedagógica).

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[desenvolvimento-orientado-por-avaliacao|Desenvolvimento Orientado por Avaliação]] | Definir métricas e testes antes de codificar a IA. | Requisitos e métricas de aceite. | Pipeline de validação + Código guiado por dados. | Foco preventivo e métrico na qualidade sistêmica. |
| [[vibe-check|Avaliação por Olhômetro (Vibe Check)]] | Testar o sistema de forma informal e subjetiva. | Impressões visuais momentâneas. | Opinião informal ("Parece bom"). | Subjetivo, não reproduzível e altamente propenso a vieses. |

| Dimensão | Desenvolvimento Ad-Hoc (Olhômetro) | Desenvolvimento Orientado por Avaliação (EDD) |
|---|---|---|
| **Definição de Métricas** | Após o desenvolvimento (se houver) | Antes da primeira linha de prompt ou código |
| **Feedback de Iteração** | Subjetivo e baseado em poucos exemplos manuais | Sistemático, estatístico e reprodutível |
| **Previsibilidade de ROI** | Baixa (surpresas desagradáveis em produção) | Alta (lançamento condicionado ao limiar de utilidade) |
| **Velocidade de Longo Prazo** | Lenta (regressões invisíveis quebram o sistema) | Rápida (mudanças validadas instantaneamente) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Criar 100 perguntas difíceis de atendimento ao cliente com suas respectivas respostas ideais antes de mexer em qualquer linha de prompt do bot, garantindo que cada alteração seja testada contra essas 100 perguntas de forma automatizada.

Uma equipe recebe a demanda de criar um assistente de IA para explicar benefícios corporativos aos funcionários de uma multinacional.
- *Sem EDD:* A equipe cria um prompt no ChatGPT, testa com 5 perguntas da sua cabeça, acha que funcionou e coloca o bot no ar. No primeiro mês, o bot informa erroneamente a um funcionário que ele tem direito a auxílio-creche internacional, gerando uma crise jurídica.
- *Com EDD:* Antes de tocar no modelo, a equipe reúne 200 dúvidas reais do RH, define que a consistência factual local com o manual interno deve ser de no mínimo $98\%$ e que o bot deve se recusar a responder casos omissos. Eles constroem a suíte de testes e descobrem que nenhum modelo atinge $98\%$ sem um RAG bem desenhado, evitando o lançamento prematuro e direcionando a engenharia para a solução correta.

## 🔗 Relações no grafo

### Pré-requisitos

- [[ai-as-a-judge|IA como Juiz]]

- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

- [[redes/ai-engineering/conceitos/diretrizes-e-rubricas-de-avaliacao.md|Diretrizes e Rubricas de Avaliação]]
- [[redes/ai-engineering/conceitos/fatiamento-de-dados-e-paradoxo-de-simpson.md|Fatiamento de Dados e Paradoxo de Simpson]]
- [[redes/ai-engineering/conceitos/dimensionamento-amostral-de-avaliacao.md|Dimensionamento Amostral de Avaliação]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

- Validação informal baseada em amostragem manual esporádica (*vibe check*).

### Conceitos relacionados

- [[rag|RAG]]

- [[redes/ai-engineering/conceitos/consistencia-factual.md|Consistência Factual]]
- [[redes/ai-engineering/conceitos/selecao-de-modelos-atributos-rigidos-e-flexiveis.md|Seleção de Modelos: Atributos Rígidos e Flexíveis]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 4 — Avaliando Sistemas de IA
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da metodologia de desenvolvimento orientado por avaliação para estruturação de projetos de IA corporativos confiáveis.
- **Confiança:** alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 4 — Evaluate AI Systems
- **Localização:** Páginas 160–161
- **Evidência:** Chip Huyen formaliza o Evaluation-Driven Development como análogo ao TDD do desenvolvimento de software, argumentando que os casos de uso corporativos mais bem-sucedidos em produção são justamente aqueles cujos critérios de avaliação puderam ser rigorosamente estabelecidos de antemão.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Desenvolvimento Orientado por Avaliação (Evaluation-Driven Development)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

1. O que é o Desenvolvimento Orientado por Avaliação (EDD) e como ele se compara ao TDD da engenharia tradicional?
2. Por que manter em produção uma aplicação de IA cuja acurácia é desconhecida é considerado pior do que nunca tê-la implantado?
3. De que forma o estabelecimento de um "limiar de utilidade" (*usefulness threshold*) protege a empresa contra prejuízos operacionais?
4. Quais são os quatro pilares técnicos sobre os quais os critérios de avaliação devem ser desdobrados no EDD?
5. Como o EDD altera o fluxo de iteração de engenheiros ao modificar prompts ou testar novas versões de modelos?
6. O que é a armadilha de "procurar a chave sob o poste de luz" no contexto da definição de casos de uso de IA?
7. Como as métricas operacionais e financeiras de negócio são integradas à formulação das metas técnicas no EDD?

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

---
*Nota gerada a partir do capítulo Capítulo 4 — Avaliando Sistemas de IA. A interpretação final deve ser revisada pelo estudante.*
