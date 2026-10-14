# AI Engineering: Building Applications with Foundation Models — Capítulo 4

## Objetivo do capítulo

Apresentar uma metodologia prática e estruturada para avaliar sistemas completos de IA baseados em modelos de fundação, cobrindo a definição de critérios multidimensionais (específicos de domínio, gerativos, seguimento de instruções, custo e latência), o processo de seleção de modelos (contrapondo APIs comerciais proprietárias e modelos de código aberto ao longo de sete eixos de decisão), a navegação crítica por benchmarks públicos e seus riscos de contaminação de dados, bem como o projeto de pipelines privados de avaliação ponta a ponta orientados por diretrizes de negócio.

## Resumo do argumento central

Colocar em produção uma aplicação de IA sem saber se ela funciona adequadamente é pior do que nunca tê-la implantado, pois gera custos de manutenção contínuos e riscos operacionais invisíveis. Para mitigar esse problema, o desenvolvimento deve ser orientado pela avaliação (*Evaluation-Driven Development*), definindo critérios de sucesso e rubricas antes mesmo da implementação de código ou prompts. A avaliação sistêmica requer analisar tanto capacidades de domínio (conhecimento técnico e raciocínio em questões de múltipla escolha e tarefas exatas) quanto capacidades de geração (com ênfase na consistência factual local e global e moderação de segurança) e de seguimento de instruções sintáticas e de estilo. Na seleção de modelos, equipes devem filtrar alternativas por atributos rígidos (*hard attributes*) antes de otimizar atributos flexíveis (*soft attributes*). Os benchmarks públicos sofrem de contaminação generalizada, tornando mandatório o uso de suítes de teste privadas. Por fim, um pipeline de avaliação confiável deve inspecionar componentes isoladamente e de ponta a ponta, aplicar fatiamento de dados (*slicing*) para prevenir o Paradoxo de Simpson e dimensionar o volume de amostras de teste para garantir significância estatística.

## Conceitos identificados

- Desenvolvimento Orientado por Avaliação
- Consistência Factual
- Capacidade de Seguir Instruções
- Seleção de Modelos: Atributos Rígidos e Flexíveis
- Modelos Abertos versus APIs Proprietárias
- Contaminação de Dados em Benchmarks
- Diretrizes e Rubricas de Avaliação
- Fatiamento de Dados e Paradoxo de Simpson
- Dimensionamento Amostral de Avaliação
- Modelo de Fundação
- Desafios de Avaliação de Modelos de Fundação
- Correção Funcional (pass@k)
- IA como Juiz (AI-as-a-Judge)

## Sequência lógica do capítulo

1. **Critérios de Avaliação (pp. 160–179):** Proposição do *Evaluation-Driven Development*; avaliação de capacidades específicas de domínio (código funcional e questões de múltipla escolha/MCQs); capacidades de geração (consistência factual local versus global, inferência em linguagem natural/NLI, métodos automatizados como SelfCheckGPT e SAFE, e benchmarks como TruthfulQA); segurança e toxicidade (RealToxicityPrompts, BOLD, vieses políticos); capacidade de seguimento de instruções (restrições verificáveis no IFEval, critérios semânticos no INFOBench e capacidade de *roleplaying* com RoleLLM e CharacterEval); otimização multiobjetivo de Pareto balanceando qualidade, custo e latência (TTFT, TPOT, tokens por minuto).
2. **Seleção de Modelos (pp. 179–191):** Workflow iterativo em quatro etapas; separação entre atributos rígidos (*hard attributes*) e flexíveis (*soft attributes*); dilema clássico *Build vs. Buy*; análise das licenças de código aberto (permissivas, restritas, pesos abertos sem dados); comparação sistemática entre hospedar modelos abertos versus consumir APIs comerciais ao longo de sete eixos: privacidade de dados, linhagem/direitos autorais, desempenho, funcionalidades (suporte a *function calling* e *logprobs*), custos de API versus custos de engenharia, controle/acesso/transparência e operação local na borda (*edge*).
3. **Navegação em Benchmarks Públicos (pp. 191–200):** Criação de tabelas de liderança privadas com benchmarks públicos; análise da correlação entre benchmarks no Open LLM Leaderboard (ARC-C, MMLU, HellaSwag, TruthfulQA, WinoGrande, GSM-8K) para evitar redundâncias; investigação sobre percepções de degradação em modelos comerciais da OpenAI; anatomia da contaminação de dados (vazamento acidental de web scraping, sobreposição indireta e treino intencional pré-lançamento); métodos de detecção de contaminação via sobreposição de $n$-grams e perplexidade; estratégias de mitigação e descarte de dados contaminados.
4. **Design do Pipeline de Avaliação (pp. 200–208):** Passo 1: Avaliação de todos os componentes isoladamente (tarefa ponta a ponta versus turnos conversacionais individuais versus etapas intermediárias de parsing); Passo 2: Criação da diretriz de avaliação (definição de critérios, rubricas de pontuação com exemplos, mapeamento de métricas de IA para métricas de negócio e determinação do limiar de utilidade / *usefulness threshold*); Passo 3: Definição de métodos e dados de teste (uso de *logprobs*, avaliação humana na produção, anotação de dados, técnicas de fatiamento de dados / *data slicing* para diagnosticar o Paradoxo de Simpson, cálculo de tamanho amostral com intervalo de confiança estatística de 95% e a regra do 3x/10x, meta-avaliação do pipeline e iteração contínua com versionamento).

## Principais afirmações

- A avaliação é o maior gargalo para a adoção industrial de IA; aplicações cuja precisão não pode ser mensurada operam como passivos de alto risco corporativo.
- Capacidades de domínio fechadas são frequentemente avaliadas via MCQs porque são fáceis de pontuar e comparar com uma linha de base aleatória, mas MCQs medem a capacidade de classificar/reconhecer respostas, e não a habilidade de sintetizá-las em formato aberto.
- A consistência factual é substancialmente mais tratável de verificar localmente (aderência a um contexto fornecido, como em RAG) do que globalmente (aderência a todo o conhecimento aberto do mundo).
- Na seleção de modelos, os atributos rígidos (políticas de compliance, restrições legais de privacidade e hardware disponível) devem atuar como filtros eliminatórios antes de qualquer esforço de otimização de atributos flexíveis (acurácia ou toxicidade).
- A tecnologia base do modelo tornou-se uma commodity; a diferenciação competitiva deslocou-se para a camada de aplicação e a integridade do pipeline de avaliação.
- Benchmarks públicos tornam-se virtualmente inúteis ou descalibrados assim que se tornam públicos devido à contaminação endêmica dos conjuntos de pré-treino raspados da internet.
- Analisar apenas a média geral agregada de acerto de uma aplicação de IA mascara falhas graves em subgrupos vulneráveis ou classes raras, incorrendo frequentemente no Paradoxo de Simpson.
- Para cada redução de 3 vezes na diferença métrica de desempenho que se deseja detectar entre dois sistemas com 95% de confiança estatística, o tamanho da amostra de teste precisa crescer aproximadamente 10 vezes.

## Fórmulas ou procedimentos apresentados

- Relação de proporção amostral para significância estatística com 95% de confiança (OpenAI):
  $$\Delta_{\text{score}} = 30\% \implies N \approx 10$$
  $$\Delta_{\text{score}} = 10\% \implies N \approx 100$$
  $$\Delta_{\text{score}} = 3\% \implies N \approx 1.000$$
  $$\Delta_{\text{score}} = 1\% \implies N \approx 10.000$$
  *(Para uma redução de $\approx 3{,}16\times$ no delta observável, a amostra escala em $\approx 10\times$, decorrente da raiz quadrada $\sqrt{10} \approx 3{,}16$).*
- Cálculo de Factualidade e Premissa via NLI (Entailment / Contradição / Neutro):
  $$P(\text{Factual}) \propto P(\text{Entailment} \mid \text{Contexto}, \text{Afirmação})$$
- Formulação tabular do Paradoxo de Simpson em subgrupos de teste:
  $$\text{Score}(A \mid G_1) > \text{Score}(B \mid G_1) \quad \land \quad \text{Score}(A \mid G_2) > \text{Score}(B \mid G_2) \quad \centernot\implies \quad \text{Score}(A_{\text{total}}) > \text{Score}(B_{\text{total}})$$

## Exemplos relevantes

- Caso da concessionária de veículos usados cujo modelo de precificação operava em produção há um ano sem que a equipe técnica soubesse se suas predições eram acuradas.
- Experimento de Rylan Schaeffer ("Pretraining on the Test Set Is All You Need"): um modelo minúsculo de apenas 1 milhão de parâmetros treinado diretamente sobre os dados dos benchmarks bateu os maiores modelos do mundo, expondo a fragilidade de benchmarks públicos contaminados.
- Parser defensivo de YAML do LinkedIn: elevou a taxa de conformidade sintática de 90% para 99,99% em produção através de scripts simples de pós-processamento, comprovando que pequenas intervenções heurísticas superam ajustes complexos de modelos.
- Auditoria contínua do LinkedIn avaliando manualmente até 500 conversas diárias com sistemas de IA para garantir supervisão contra desvios de produção.

## Limitações e ressalvas

- As diretrizes de tamanho amostral e custo computacional dependem das características de distribuição estatística e variância das saídas específicas de cada domínio de negócio.
- O capítulo aborda a seleção entre hospedar modelos e usar APIs comerciais com base no cenário econômico de GPUs e preços de nuvem consolidados até 2024.

## Dúvidas em aberto

- Como estabelecer metodologias universalmente aceitas para certificar que um modelo de fundação não sofreu contaminação indireta durante o pré-treinamento quando seus desenvolvedores não divulgam seus dados?
- Até que ponto a verificação automatizada de factualidade por motores de busca (como o SAFE da DeepMind) permanece financeiramente sustentável para aplicações de altíssimo volume de requisições?

## Localização da fonte

Capítulo 4, páginas 159 a 209 do livro impresso / arquivo de texto consolidado.
