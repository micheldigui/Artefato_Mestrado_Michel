# AI Engineering: Building Applications with Foundation Models — Capítulo 6

## Objetivo do capítulo

Examinar os dois padrões de arquitetura dominantes para construção e enriquecimento contextual de aplicações com modelos de fundação: Geração Aumentada de Recuperação (*Retrieval-Augmented Generation* — RAG) e Agentes Autônomos (*Agents*). O capítulo detalha o funcionamento interno de sistemas de recuperação de informação (léxica, semântica e híbrida com fusão de rankings), estratégias de otimização de contexto (chunking, reranking, reescrita de consultas e contextual retrieval), expansão para além de texto (dados multimodais e tabulares via Text-to-SQL), o arcabouço cognitivo e operacional de agentes (planejamento, uso de ferramentas, reflexão com ReAct e Reflexion), seus modos de falha e protocolos de avaliação, concluindo com o design da hierarquia de memória para sistemas de inteligência artificial.

## Resumo do argumento central

Assim como os seres humanos dependem de informações precisas para não cometer erros conceituais, os modelos de fundação demandam contexto pertinente e atualizado para mitigar alucinações e executar tarefas complexas. O RAG resolve a restrição de capacidade e a desatualização factual conectando o modelo a bases de dados externas através de um pipeline desacoplado de indexação e consulta. Embora a janela de contexto dos modelos esteja crescendo para milhões de tokens, o RAG permanece indispensável por razões de custo, latência e eficiência atencional: fornecer apenas o contexto relevante reduz a dispersão do modelo (*lost-in-the-middle*) e barateia a inferência. A recuperação híbrida, combinando a precisão de palavras-chave do BM25 com a densidade semântica de embeddings via *Reciprocal Rank Fusion* (RRF), estabelece o padrão-ouro de busca. 

Por sua vez, os agentes expandem o padrão RAG ao transformar o modelo de fundação no "cérebro" de um sistema cibernético capaz de perceber seu ambiente, traçar planos e executar ações no mundo exterior por meio de chamadas de ferramentas (*function calling*). Contudo, a autonomia dos agentes introduz o problema dos erros compostos — onde a probabilidade de sucesso colapsa exponencialmente ao longo de fluxos com múltiplos passos —, exigindo o desacoplamento formal entre planejamento e execução, técnicas de reflexão iterativa (como ReAct e Reflexion) e sistemas estruturados de memória de curto e longo prazo.

## Conceitos identificados

- Geração Aumentada de Recuperação (RAG)
- Modelo de Fundação
- Embeddings
- Algoritmos de Recuperação: Lexical versus Vetorial
- Busca Híbrida e Reciprocal Rank Fusion (RRF)
- Estratégias de Chunking e Otimização de RAG
- RAG Multimodal e Dados Tabulares (Text-to-SQL)
- Agentes de IA e Inventário de Ferramentas
- Planejamento e Chamada de Funções (Function Calling)
- Reflexão e Correção de Erros em Agentes (ReAct e Reflexion)
- Avaliação e Modos de Falha de Agentes
- Sistemas de Memória para IA

## Sequência lógica do capítulo

1. **Geração Aumentada de Recuperação — RAG (pp. 253–275):** Origens do padrão recuperar-depois-gerar (Chen et al., 2017; Lewis et al., 2020); por que RAG não morrerá com contextos longos (Lei de Parkinson do contexto, custos e foco de atenção); arquitetura retriever-generator; algoritmos de busca (baseados em termos via BM25/TF-IDF versus baseados em embeddings via vetores densos e ANN: LSH, HNSW, Product Quantization, IVF, Annoy); busca híbrida e combinação de rankings com Reciprocal Rank Fusion (RRF); métricas de recuperação (context precision, context recall, NDCG, MAP, MRR); otimizações de recuperação (estratégias de chunking por caracteres/frases/recursivo/tokens, reranking temporal e cruzado, reescrita de queries por LLMs e recuperação contextualizada da Anthropic); RAG multimodal com CLIP e RAG tabular via Text-to-SQL.
2. **Agentes de IA (pp. 275–300):** Definição formal de agente (percepção, planejamento e ação sobre o ambiente); inventário de ferramentas (aumento de conhecimento, extensão de capacidade com interpretadores de código e ações de escrita destrutivas); o gargalo dos erros compostos ($0{,}95^{10} \approx 60\%$, $0{,}95^{100} \approx 0{,}6\%$); planejamento e raciocínio (desacoplamento de plano e execução, classificação de intenção, modelos de fundação como planejadores versus críticas de LeCun e Kambhampati); geração de planos (function calling, granularidade de comandos em nomes exatos versus linguagem natural); fluxos de controle complexos (sequencial, paralelo, ramificação condicional e loops); reflexão e autocorreção (framework ReAct com Thought-Act-Observation e framework Reflexion); seleção dinâmica de ferramentas e evolução de habilidades (Chameleon, Voyager); taxonomia de falhas de agentes (falhas de planejamento, falhas de ferramentas e ineficiência operacional).
3. **Sistemas de Memória (pp. 300–304):** A tríade de memória (conhecimento interno nos pesos, memória de curto prazo no contexto do prompt e memória de longo prazo em bancos vetoriais/RAG); funções de gerenciamento de memória (estouro de contexto dentro da sessão, persistência entre sessões, calibração de consistência e integridade estrutural); estratégias de descarte e condensação (FIFO, sumarização periódica, rastreamento de entidades e reflexão sobre contradições).

## Principais afirmações

- RAG é o equivalente à engenharia de atributos (*feature engineering*) para a era dos modelos de fundação: trata-se de selecionar e injetar os dados exatos necessários para o modelo tomar uma decisão informada.
- A expansão das janelas de contexto para milhões de tokens não elimina o RAG, pois processar centenas de milhares de tokens desnecessários encarece a inferência, eleva a latência (*TTFT*) e dispersa a atenção do modelo (*lost-in-the-middle*).
- Em tarefas corporativas de busca, superar um sistema BM25 bem ajustado é extremamente difícil; a abordagem mais resiliente em produção é a busca híbrida combinando BM25 e busca vetorial via Reciprocal Rank Fusion (RRF).
- Agentes sofrem dramaticamente do problema de erros compostos: se um modelo tem acurácia de 95% por passo, em uma tarefa de 10 passos a taxa de sucesso cai para 60%, e em 100 passos ela colapsa para menos de 1%, tornando mandatório o uso de modelos de elite e mecanismos de reflexão.
- Planejamento deve ser estritamente desacoplado da execução: planos gerados por LLMs devem ser validados por código determinístico, heurísticas ou modelos juízes antes de dispararem chamadas reais de ferramentas no mundo exterior.
- A concessão de ações de escrita a agentes (enviar e-mails, deletar tabelas, transacionar dinheiro) exige barreiras rígidas de isolamento (*sandboxing*) e aprovação explícita por humano no loop para evitar danos materiais irreversíveis.
- O histórico da conversa mantido na memória de curto prazo (janela de contexto) não deve ser gerenciado puramente por descarte FIFO ingênuo, pois as instruções iniciais da conversa geralmente contêm o objetivo primário da tarefa.

## Fórmulas ou procedimentos apresentados

- Cálculo clássico de pontuação TF-IDF:

  $$\text{Score}_{\text{TF-IDF}}(D, Q) = \sum_{t \in Q} \text{IDF}(t) \cdot f(t, D), \quad \text{onde } \text{IDF}(t) = \log\frac{N}{C(t)}$$

- Fusão de Rankings por Posição Recíproca (*Reciprocal Rank Fusion* — RRF):

  $$\text{Score}_{\text{RRF}}(D) = \sum_{i=1}^n \frac{1}{k + r_i(D)}$$ *(onde $n$ é o número de sistemas de busca, $r_i(D)$ é a posição do documento no ranking do buscador $i$, e $k$ é uma constante de suavização, convencionalmente $k=60$).*

- Degradação de acurácia composta em fluxos agênticos de $T$ etapas com acurácia individual $p$:

  $$\text{Acurácia}_{\text{composta}} = p^T \implies 0{,}95^{10} \approx 0{,}5987 \; (59{,}8\%), \quad 0{,}95^{100} \approx 0{,}0059 \; (0{,}59\%)$$

- Similaridade de cosseno para recuperação vetorial:

  $$\text{Sim}(u, v) = \frac{u \cdot v}{\|u\|_2 \|v\|_2}$$

## Exemplos relevantes

- Caso Kitty Vogue: ecommerce fictício de moda felina utilizado para demonstrar o fluxo de RAG sobre dados tabulares com geração de consultas SQL dinâmicas (Text-to-SQL) e projeção de receita.
- Estudo Chameleon (Lu et al., 2023): agente equipado com 13 ferramentas externas que superou o GPT-4 puro em tarefas científicas (ScienceQA) com ganho de $11{,}37\%$ e em raciocínio matemático tabular (TabMWP) com ganho de $17\%$.
- Framework Reflexion (Shinn et al., 2023): agente de programação que gera código, submete a testes unitários, lê o traceback de erro, formula uma auto-reflexão verbal do porquê falhou e propõe uma nova trajetória corrigida.
- Contextual Retrieval da Anthropic (2024): técnica que utiliza um modelo leve para gerar um texto contextual de 50 a 100 tokens posicionado no cabeçalho de cada chunk antes da indexação, reduzindo drasticamente chunks órfãos e descontextualizados.

## Limitações e ressalvas

- O capítulo aborda agentes baseados em modelos autorregressivos como um campo de fronteira altamente experimental, onde consensos acadêmicos sobre a capacidade pura de planejamento de LLMs ainda estão em disputa aberta.
- A avaliação de agentes em ambientes virtuais (como TravelPlanner ou AgentOps) não garante imunidade contra imprevistos dinâmicos no mundo físico real.

## Dúvidas em aberto

- Até que ponto arquiteturas neuro-simbólicas ou modelos integrados de mundo (*world models*) substituirão o planejamento puramente autoregressivo em agentes de longo prazo?
- Como desenhar mecanismos de memória de longo prazo que resolvam contradições factuais de forma autônoma sem exigir confirmação manual constante do usuário?

## Localização da fonte

Capítulo 6, páginas 253 a 306 do livro impresso / arquivo de texto consolidado.
