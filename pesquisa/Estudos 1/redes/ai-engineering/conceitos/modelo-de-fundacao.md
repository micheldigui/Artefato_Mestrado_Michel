# 🧠 Modelo de Fundação

**Rede:** `ai-engineering`   **Área:** `modelagem`

**Rede:** `ai-engineering`  
areas: `inteligencia-artificial`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 8–12

## 📝 Definição

### Definição formal

Um **Modelo de Fundação** (*Foundation Model*) é uma arquitetura de aprendizado profundo caracterizada por escala massiva de parâmetros e pré-treinamento sobre conjuntos volumosos e heterogêneos de dados não rotulados por meio de [[redes/ai-engineering/conceitos/auto-supervisao.md|auto-supervisão]], projetada para servir de substrato geral capaz de ser adaptado para uma multiplicidade de tarefas a jusante (*downstream tasks*).

Um modelo de inteligência artificial de grande escala, geralmente treinado em dados massivos e heterogêneos por meio de auto-supervisão, projetado para servir como base generalista que pode ser adaptada a uma ampla gama de tarefas subsequentes.

### Em linguagem simples

É um modelo "coringa" gigante que aprendeu noções gerais sobre linguagem, código, imagens ou outros dados ao ler e analisar uma quantidade colossal de informações. Ele recebe o nome de "fundação" porque não foi treinado para fazer apenas uma coisa específica (como traduzir ou classificar e-mails), mas sim para servir de alicerce sobre o qual você constrói diversas ferramentas diferentes.

É um modelo de IA gigantesco, extremamente versátil e inteligente, que já vem pré-treinado com um vasto conhecimento do mundo e serve de base para você construir aplicações específicas sem precisar criar tudo do zero.

### Escopo e distinções

Distingue-se dos modelos estreitos (*task-specific models*) da era anterior do aprendizado profundo, que aprendiam apenas uma distribuição restrita de entrada para saída (como um classificador de sentimento de resenhas de cinema que nada sabia sobre código ou medicina). O modelo de fundação transcende domínios isolados e, com frequência crescente, opera como [[redes/ai-engineering/conceitos/modelo-multimodal.md|modelo multimodal]].

Diferencia-se dos antigos modelos de IA focados em uma única tarefa estreita (*task-specific models*). Abrange tanto modelos puramente textuais (*LLMs*) quanto modelos multimodais (*LMMs*).

## 🧩 Problema que resolve

Supera a redundância e a ineficiência econômica de se treinar um modelo novo para cada problema de computação cognitiva. Antes dos modelos de fundação, equipes precisavam coletar conjuntos de dados dedicados e desenhar pipelines isolados para centenas de tarefas diferentes. O modelo de fundação unifica o conhecimento base em uma única estrutura que já possui entendimento de mundo pré-adquirido.

Resolve a ineficiência de ter que treinar um modelo de inteligência artificial separado e custoso para cada problema específico de negócio (como análise de sentimento, tradução ou classificação de e-mails).

## 💡 Intuição

Pense em um estudante de ensino superior com excelente formação analítica e domínio avançado de vários idiomas. Ele ainda não é um advogado sênior nem um engenheiro civil especialista em barragens. Contudo, devido à sua base sólida de raciocínio e linguagem, você pode fornecer instruções específicas, entregar manuais de referência e ele executará tarefas em ambas as áreas muito mais rápido do que alguém que precisasse aprender o alfabeto e o raciocínio formal do início.

Pense em um profissional recém-formado em uma universidade de elite: ele possui uma base cultural, de idiomas e de raciocínio geral ampla o suficiente para ser contratado e treinado rapidamente para qualquer cargo específico de uma empresa.

## ⚙️ Como funciona

O ciclo de um modelo de fundação apoia-se em duas etapas essenciais:

### Etapas

1. **Pré-treinamento massivo:** Treinado em supercomputadores sobre trilhões de tokens textuais ou multimodais através de objetivos de [[redes/ai-engineering/conceitos/auto-supervisao.md|auto-supervisão]], assimilando relações semânticas, gramaticais e contextuais.
2. **Pós-treinamento e alinhamento:** Passa por ajustes supervisionados e técnicas de preferência para responder adequadamente a solicitações humanas.
3. **Disponibilização:** O modelo é congelado e exposto para consumo via APIs de serviço (*MaaS*) ou empacotado para download como pesos abertos (*open weights*).
4. **Adaptação operacional:** Desenvolvedores utilizam [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|técnicas de adaptação]] (prompts, RAG ou finetuning) para direcionar o modelo para casos específicos.

1. Coleta de dados massivos em larga escala na internet e em bases corporativas.
2. Pré-treinamento computacional intensivo via auto-supervisão (custo elevado restrito a grandes corporações).
3. Pós-treinamento de alinhamento com preferências humanas (*SFT* e *RLHF*).
4. Disponibilização do modelo final para adaptação externa via APIs (*Model as a Service*) ou pesos abertos.

### Entradas e saídas

- **Entradas:** Vetores de tokens derivados de linguagem natural, imagens, sinais de áudio ou dados estruturados combinados.
- **Saídas:** Distribuições de probabilidade para geração do próximo token textual, vetor de representação (*embedding*) ou geração de outras modalidades.

- Entradas: Prompts textuais, imagens, áudios ou dados multimodais combinados.
- Saídas: Respostas gerativas abertas, classificações ou execuções estruturadas.

## 📐 Formulação matemática

O modelo atua como um estimador de densidade de probabilidade parametrizado por uma quantidade massiva de parâmetros $\theta \in \mathbb{R}^{|\Theta|}$, onde tipicamente $|\Theta| \ge 10^9$ (bilhões de parâmetros):

$$P_\theta(x) = \prod_{i=1}^n P_\theta(x_i \mid x_1, \dots, x_{i-1})$$

A capacidade de generalização para novas tarefas sem atualização de pesos funda-se no aprendizado em contexto (*in-context learning*):

$$\arg\max_y P_\theta(y \mid x_{\text{tarefa}}, \text{exemplos})$$

Onde o modelo prevê a saída correta $y$ condicionado a descrições e demonstrações fornecidas no prompt.

Abstratamente, seja $M_\Theta$ um modelo parametrizado por pesos $\Theta$ obtidos após o pré-treinamento em larga escala. A adaptação para uma tarefa nova $T$ ocorre maximizando a probabilidade condicionada ajustada:

$$\Theta^* = \arg\max_{\Theta} \sum_{(x,y) \in T} \log P(y \mid x; \Theta)$$

Onde:
- $\Theta$: Pesos originais do modelo de fundação.
- $\Theta^*$: Pesos ajustados após adaptação.
- $(x,y)$: Pares de dados específicos da tarefa downstream $T$.

## 🧱 Hipóteses e condições de validade

- Hipótese de escala (*Scaling Hypothesis*): o aumento coordenado de parâmetros, volume de dados de treino e computação disponível resulta em ganhos previsíveis e contínuos de capacidade cognitiva.
- Qualidade e diversidade do conjunto original de treinamento: lacunas graves nos dados de treino (como ausência de uma língua ou área científica) limitam a viabilidade do modelo naquele domínio.

- Hipótese de transferência (*transfer learning*): o conhecimento geral adquirido em domínios amplos transfere-se eficazmente para tarefas especializadas restritas.

## ✅ Quando usar

- Base para qualquer aplicação que exija geração textual aberta, interpretação complexa de documentos ou interação com usuários.
- Como componente de raciocínio central em fluxos de trabalho autônomos e agentes.
- Quando o custo e o tempo de coletar dados e treinar uma arquitetura específica do zero forem inviáveis.

- Em praticamente qualquer aplicação moderna de IA que exija compreensão de linguagem, criatividade, síntese ou tomada de decisão baseada em texto e multimodalidade.

## 🚫 Quando não usar

- Em hardware minúsculo e desconectado que não suporte a quantidade mínima de memória necessária para armazenar bilhões de parâmetros em formatos quantizados.
- Problemas matemáticos determinísticos rígidos em que algoritmos analíticos exatos funcionam com garantia absoluta e custo desprezível.

- Em ambientes com restrições extremas de hardware embarcado onde modelos diminutos especializados baseados em regras ou árvores de decisão tradicionais sejam suficientes e mais baratos.

## ⚠️ Limitações e armadilhas

- **Natureza probabilística e alucinações:** Modelos de fundação não possuem banco de fatos indexado; eles completam sequências estatisticamente prováveis, gerando afirmações incorretas com tom de certeza.
- **Tamanho e custo operacional:** Exigem hardware especializado (GPUs) com alta largura de banda de memória para execução, acarretando custos contínuos de operação.
- **Opacidade:** A maioria dos modelos líderes é fornecida como caixas-pretas proprietárias, ocultando detalhes exatos de dados de treino e hiperparâmetros.

- Alto custo computacional de inferência e dependência de infraestrutura externa (*Model as a Service*).
- Vulnerabilidade a alucinações e comportamento estocástico imprevisível.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[modelo-de-fundacao|Modelo de Fundação]] | Servir de base generalista para múltiplos domínios e modalidades. | Dados multimodais em grande escala. | Representações generalizadas / Respostas complexas. | Escala massiva e capacidade de generalização de zero-shot para diversas tarefas. |
| [[modelo-de-linguagem|Modelo de Linguagem]] | Estimar probabilidades de sequências textuais. | Sequência de tokens. | Distribuição de probabilidade / Próximo token. | Foco estrutural estatístico amplo sobre o idioma. |

| Dimensão | Modelo de Fundação | Modelo Especializado Clássico |
|---|---|---|
| **Escopo** | Generalista, multi-tarefa e adaptável | Focado estritamente em uma única tarefa pré-definida |
| **Custo de criação** | Dezenas a centenas de milhões de dólares | Centenas a milhares de dólares |
| **Treinamento** | Auto-supervisão em escala de internet | Aprendizado supervisionado com anotação manual |
| **Flexibilidade** | Alta via instruções em linguagem natural | Baixa; exige re-treino para mudar de escopo |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Considere um hospital que deseja criar três ferramentas: um extrator de sintomas a partir de relatos livres de pacientes, um sumarizador de prontuários médicos para troca de turnos de enfermagem e um assistente para responder dúvidas operacionais sobre preparo de exames. 
Em vez de construir, rotular dados e treinar três redes neurais completamente distintas, a equipe de engenharia adota um único **modelo de fundação** e implementa três prompts e contextos diferentes para cobrir as três necessidades com a mesma infraestrutura básica.

Em vez de treinar um modelo específico de IA para detectar spam e outro modelo separado para traduzir francês, uma empresa utiliza o GPT-4 (um modelo de fundação) para realizar ambas as tarefas apenas alterando as instruções textuais enviadas via API.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-linguagem.md|Modelo de Linguagem]]
- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]

- [[modelo-de-linguagem|Modelo de Linguagem]]
- [[auto-supervisão|Auto-supervisão]]

### Complementos

- [[redes/ai-engineering/conceitos/modelo-multimodal.md|Modelo Multimodal]]
- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]]
- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Alternativas

- Modelos estatísticos ou supervisionados tradicionais de tarefa única (*task-specific models*).

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]
- [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]]

- [[tokenizacao|Tokenizacao]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 8–12
- **Evidência:** O texto descreve a transição dos modelos de linguagem para modelos de fundação, ressaltando a mudança de modelos de tarefa única para modelos de propósito geral adaptáveis, impulsionados pela inclusão de múltiplas modalidades e dados massivos.
- **Confiança:** Alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Definição analítica da transição de modelos específicos para modelos gerais de fundação e o paradigma de distribuição de modelos como serviço.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. Qual é a definição formal de um modelo de fundação e o que o termo "fundação" simboliza?
2. Em que aspectos um modelo de fundação difere dos modelos tradicionais de aprendizado profundo focados em tarefa única?
3. Qual é o papel da auto-supervisão no surgimento e viabilização técnica dos modelos de fundação?
4. Como a multimodalidade expande o escopo funcional dos modelos de fundação tradicionais de texto?
5. Quais são as principais restrições operacionais e econômicas decorrentes da magnitude de parâmetros de um modelo de fundação?
6. Por que dizemos que um modelo de fundação é uma máquina de completação probabilística e não uma base de dados factual?
7. Quais são as três abordagens principais para adaptar um modelo de fundação às necessidades de um produto específico?

1. O que é Modelo de Fundação?
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
*Nota gerada a partir do capítulo Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação. A interpretação final deve ser revisada pelo estudante.*
