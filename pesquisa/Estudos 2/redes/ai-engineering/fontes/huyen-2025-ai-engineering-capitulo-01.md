# AI Engineering: Building Applications with Foundation Models — Capítulo 1

## Objetivo do capítulo

Introduzir o surgimento da Engenharia de IA (*AI Engineering*) como uma disciplina prática e distinta da Engenharia de Aprendizado de Máquina tradicional (*ML Engineering*), impulsionada pela transição de modelos de linguagem para modelos de fundação acessíveis como serviço (*Model-as-a-Service*). O capítulo estabelece as bases conceituais de modelos autorregressivos, auto-supervisão, multimodalidade, técnicas primárias de adaptação, arquitetura da pilha de tecnologia (*AI stack*), planejamento de casos de uso corporativos e os gargalos críticos de viabilização em produção.

## Resumo do argumento central

A partir de 2020, o crescimento em escala computacional e de dados permitiu que modelos de linguagem treinados por auto-supervisão superassem limitações históricas de rotulagem manual e evoluíssem para modelos de fundação multimodais e generalistas. O custo astronômico de pré-treinamento restringiu a criação de modelos básicos a poucas entidades, estabelecendo o paradigma de modelos fornecidos como serviço via APIs. Consequentemente, o foco da engenharia deslocou-se do treinamento do zero para a adaptação rápida de modelos prontos (via engenharia de prompt, RAG e ajuste fino). Isso democratizou o desenvolvimento de produtos cognitivos, mas introduziu novos desafios críticos: a natureza probabilística e de saída aberta dos modelos dificulta a avaliação; a latência e o custo de inferência tornam-se gargalos primários; e o "desafio da última milha" demonstra que passar de um protótipo funcional (0 a 60%) para um sistema confiável em produção (60 a 100%) exige rigor de engenharia, governança e integração sistêmica.

## Conceitos identificados

- Engenharia de IA
- Modelo de Fundação
- Modelo de Linguagem
- Modelo de Linguagem Autoregressivo
- Modelo de Linguagem Mascarado
- Tokenização e Vocabulário
- Auto-supervisão
- Modelo Multimodal
- Adaptação de Modelos
- Engenharia de Prompt
- Geração Aumentada de Recuperação (RAG)
- Ajuste Fino (Finetuning)
- Pilha de Engenharia de IA
- Desafio da Última Milha em IA
- Humano no Loop (Crawl-Walk-Run)
- Defensabilidade de Produto de IA

## Sequência lógica do capítulo

1. **A ascensão da Engenharia de IA (pp. 2–16):** Análise da evolução histórica dos modelos de linguagem estatísticos clássicos (Shannon, 1951) até os LLMs modernos; explicação do papel da auto-supervisão para romper o gargalo de anotação; transição para modelos multimodais de fundação e impacto do modelo como serviço.
2. **Casos de uso de Modelos de Fundação (pp. 16–28):** Mapeamento empírico de aplicações de consumo e corporativas em oito categorias centrais (programação, mídia visual, redação, educação, agentes conversacionais, agregação de informação, organização de dados e automação de fluxos de trabalho).
3. **Planejamento de Aplicações de IA (pp. 28–35):** Framework de avaliação de casos de uso; critérios de risco e necessidade de IA; taxonomia do papel da IA (crítico vs. complementar, reativo vs. proativo, dinâmico vs. estático); desenho de governança (*human-in-the-loop* e modelo *Crawl-Walk-Run*); análise de defensabilidade de produtos; gerenciamento do desafio da última milha e manutenção contínua.
4. **A Pilha de Engenharia de IA (pp. 35–47):** Estruturação da pilha em três camadas (aplicação, desenvolvimento de modelos e infraestrutura); comparação detalhada entre Engenharia de IA, Engenharia de ML Tradicional e Engenharia *Full-Stack*.

## Principais afirmações

- A escala pós-2020 catalisou uma mudança qualitativa nas capacidades dos modelos, transformando a IA de disciplina especializada de nicho em ferramenta universal de desenvolvimento de software.
- A auto-supervisão é o mecanismo central que possibilitou a expansão dos modelos, pois elimina a dependência de anotação humana manual no pré-treinamento ao derivar rótulos diretamente dos dados brutos.
- Modelos de fundação são máquinas de completação estatística probabilística; seus resultados nunca são garantias determinísticas de correção factual.
- A Engenharia de IA foca na adaptação e avaliação de modelos existentes de saída aberta, enquanto o ML tradicional foca na modelagem matemática e no treinamento de modelos para saídas fechadas a partir de dados tabulares.
- Construir uma demonstração funcional com modelos de fundação leva dias ("0 a 60"), mas estabilizar a aplicação para produção ("60 a 100") consome meses de esforço sistemático de avaliação, mitigação de alucinações e otimização de latência.
- As vantagens competitivas em produtos de IA dependem fundamentalmente de distribuição e dados proprietários em ciclo de melhoria (*data flywheel*), e raramente apenas da tecnologia do modelo em si.

## Fórmulas ou procedimentos apresentados

- Relação aproximada de tokenização em inglês: $100 \text{ tokens} \approx 75 \text{ palavras}$ (fator de escala de aproximadamente $0{,}75$ palavra por token no GPT-4).
- Processamento sequencial autoregressivo: cálculo da probabilidade conjunta da sequência como produto das probabilidades condicionais de cada token subsequente dado o contexto precedente.
- Matriz de decisão *Build vs. Buy* e framework progressivo de automação *Crawl-Walk-Run*.

## Exemplos relevantes

- Análise estatística de Sherlock Holmes no conto "The Adventure of the Dancing Men" para ilustrar propriedades de frequência de linguagem.
- Caso de sucesso do GitHub Copilot superando 100 milhões de dólares em receita recorrente anual (ARR) como marco de IA generativa em produção.
- Estudo de impacto do ChatGPT na produtividade de escrita profissional (Noy e Zhang, MIT, 2023), demonstrando redução de 40% no tempo de execução e aumento de 18% na qualidade avaliada.
- Disparidade de custo de tokenização: texto equivalente exigindo 7 tokens em inglês versus 72 tokens em birmanês no dataset MASSIVE.

## Limitações e ressalvas

- O capítulo aborda conceitos fundamentais e conceituais de alto nível, adiando os detalhes operacionais matemáticos de amostragem, avaliação e atendimento para os capítulos posteriores.
- A literatura técnica citada reflete majoritariamente modelos com base na arquitetura Transformer desenvolvidos até 2024.

## Dúvidas em aberto

- Até que ponto a camada de aplicação permanecerá defensável contra a incorporação de funcionalidades nativas diretamente pelos provedores de modelos de fundação?
- Como a regulação internacional de propriedade intelectual e direitos autorais de dados de treino afetará o ecossistema de modelos de código aberto?

## Localização da fonte

Capítulo 1, páginas 1 a 48 do livro impresso / arquivo de texto consolidado.
