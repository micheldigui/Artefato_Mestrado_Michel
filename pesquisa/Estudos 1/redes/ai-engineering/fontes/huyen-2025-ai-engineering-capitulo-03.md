# AI Engineering: Building Applications with Foundation Models — Capítulo 3

## Objetivo do capítulo

Apresentar um panorama abrangente e rigoroso sobre as metodologias de avaliação de modelos de fundação. O capítulo disseca a complexidade decorrente da natureza aberta e probabilística das saídas desses modelos, aborda as métricas estatísticas clássicas de modelagem de linguagem (entropia, entropia cruzada e perplexidade), detalha métodos de avaliação exata (correção funcional de código e similaridade com dados de referência via métricas lexicais e semânticas com embeddings) e examina os paradigmas emergentes de avaliação subjetiva automatizada: o uso de IA como juiz (*AI-as-a-judge*), seus vieses intrínsecos e os rankings comparativos par a par (*pairwise*) fundamentados em algoritmos como Elo e Bradley–Terry.

## Resumo do argumento central

A avaliação é o maior gargalo técnico e operacional para colocar aplicações baseadas em modelos de fundação em produção. Enquanto o aprendizado de máquina tradicional operava sobre tarefas fechadas com gabaritos exatos (como classificação e regressão tabular), os modelos de fundação produzem saídas abertas para as quais existe uma infinidade de respostas válidas, tornando obsoleta a simples comparação com um único gabarito pré-definido. Avaliadores humanos são caros, lentos e sujeitos a variabilidade. As métricas estatísticas intrínsecas (como a perplexidade) servem como excelente termômetro de compressão e capacidade básica do modelo de linguagem, mas não refletem a totalidade da utilidade prática para tarefas finais após o pós-treinamento. Consequentemente, a engenharia de IA moderna exige uma composição de abordagens: avaliação exata e determinística onde aplicável (como correção funcional em código via testes unitários e similaridade de embeddings), combinada com avaliação subjetiva automatizada via IA como juiz e modelagem comparativa par a par. No entanto, o uso de juízes neurais introduz novos riscos sistêmicos — como vieses de verbosidade, auto-preferência e posição —, demandando protocolos estritos de calibração, rubricas claras e pipelines de auditoria contínua.

## Conceitos identificados

- Desafios de Avaliação de Modelos de Fundação
- Perplexidade e Entropia Cruzada
- Correção Funcional (pass@k)
- Similaridade Lexical
- Similaridade Semântica
- Embeddings
- IA como Juiz (AI-as-a-Judge)
- Vieses de Avaliação por IA
- Modelos de Preferência e Juízes Especializados
- Avaliação Comparativa (Pairwise)

## Sequência lógica do capítulo

1. **Desafios da Avaliação de Modelos de Fundação (pp. 114–117):** A assimetria de avaliar modelos mais capazes que os próprios avaliadores humanos; ausência de gabaritos fechados em saídas abertas; opacidade de modelos caixa-preta; saturação rápida de benchmarks públicos (GLUE, MMLU) e escassez de infraestrutura de avaliação sistemática em comparação com algoritmos de treino.
2. **Métricas de Modelagem de Linguagem (pp. 118–125):** Definição da teoria da informação de Shannon (1951); formulação de entropia e entropia cruzada; métricas de bits por caractere (BPC) e bits por byte (BPB); definição matemática de perplexidade (PPL); interpretação de PPL (estrutura dos dados, vocabulário, tamanho do contexto); colapso de entropia pós-alinhamento (SFT/RLHF); casos de uso de PPL para detecção de contaminação de dados, anomalias e deduplicação.
3. **Avaliação Exata (pp. 125–136):** Dicotomia entre avaliação exata (sem ambiguidade) e avaliação subjetiva; Correção Funcional em código e SQL via execução e testes unitários (*pass@k* no HumanEval e MBPP); Similaridade contra dados de referência (correspondência exata, similaridade lexical via n-grams e distância de edição: BLEU, ROUGE, METEOR++; similaridade semântica via embeddings e similaridade de cosseno: BERTScore, MoverScore); Introdução a Embeddings e representações multimodais conjuntas (CLIP).
4. **IA como Juiz (pp. 136–148):** Motivações de velocidade, custo e correlação com humanos (MT-Bench, AlpacaEval); formas de uso (pontuação isolada 1–5, comparação com referência, preferência par a par); engenharia de prompts para juízes (rubricas e calibração); limitações críticas (inconsistência estocástica, ambiguidade de critérios entre ferramentas, sobretaxa de custo/latência); vieses sistemáticos (auto-preferência, viés de primeira posição, viés de verbosidade); taxonomia de modelos juízes (modelos mais fortes, auto-avaliação/crítica e modelos especializados: modelos de recompensa como Cappy, juízes com referência como Prometheus/BLEURT e modelos de preferência como PandaLM/JudgeLM).
5. **Rankings com Avaliação Comparativa (pp. 148–156):** Dicotomia entre avaliação pontual (*pointwise*) e comparativa (*pairwise*); facilidade humana em comparar A vs. B; coleta de comparações em produção (Chatbot Arena da LMSYS, ChatGPT); modelagem matemática via algoritmos de ranking (Elo e Bradley–Terry); desafios de escalabilidade quadrática $\mathcal{O}(N^2)$, violações da premissa de transitividade, falta de controle de qualidade em dados públicos e o desafio de mapear taxas de vitória comparativas em métricas absolutas de negócio; perenidade e futuro da avaliação comparativa.

## Principais afirmações

- A avaliação é o elo mais vulnerável da engenharia de IA: à medida que os modelos ganham capacidade, o custo de julgamento humano cresce exponencialmente, tornando a avaliação manual inviável em escala.
- A perplexidade quantifica a incerteza do modelo na previsão do próximo token; um modelo com PPL igual a 4 possui, em média, a mesma incerteza de escolher aleatoriamente entre 4 opções equiprováveis.
- A perplexidade tende a aumentar após o pós-treinamento (SFT/RLHF) devido ao colapso de entropia, tornando a métrica inadequada para avaliar a qualidade final de conversação de assistentes instruídos.
- Testes unitários com validação de execução (*pass@k*) são o padrão-ouro de avaliação objetiva em programação e consultas estruturadas (Text-to-SQL).
- Métricas lexicais baseadas em contagem de palavras (como BLEU e ROUGE) falham estruturalmente em avaliar respostas abertas e criativas, pois penalizam o uso de sinônimos válidos e explicações divergentes do texto de referência.
- A abordagem de IA como juiz apresenta correlação de até 85% a 98% com avaliadores humanos em benchmarks gerais, superando a concordância entre humanos não especialistas em tarefas abertas.
- Juízes de IA sofrem de vieses persistentes previsíveis, especialmente o viés de verbosidade (preferência por respostas longas e prolixas em detrimento de respostas curtas e factualmente corretas).
- Avaliações comparativas par a par (*pairwise*) nunca se tornam saturadas como os benchmarks tradicionais, pois a régua de qualidade sobe automaticamente com o lançamento de novos modelos competidores.

## Fórmulas ou procedimentos apresentados

- Entropia de Shannon:

  $$H(P) = -\sum_{x} P(x) \log_2 P(x)$$

- Entropia Cruzada entre a distribuição real $P$ e a distribuição aprendida $Q$:

  $$H(P, Q) = H(P) + D_{\text{KL}}(P \parallel Q) = -\sum_{x} P(x) \log Q(x)$$

- Perplexidade baseada em base 2 ou natural ($e$):

  $$\text{PPL}(P, Q) = 2^{H(P, Q)} \quad \text{ou} \quad \text{PPL}(P, Q) = e^{H(P, Q)}$$

- Perplexidade computada diretamente por produto de probabilidades condicionais sobre uma sequência de tokens $X = (x_1, \dots, x_n)$:

  $$\text{PPL}(X) = \left( \prod_{i=1}^n \frac{1}{P(x_i \mid x_1, \dots, x_{i-1})} \right)^{\frac{1}{n}}$$

- Métrica pass@k para validação funcional de código:

  $$\text{pass@}k = \mathbb{E}_{\text{problemas}} \left[ 1 - \frac{\binom{n - c}{k}}{\binom{n}{k}} \right]$$ *(onde $n$ é o total de amostras geradas, $c$ é o número de amostras corretas que passaram nos testes unitários e $k$ é o número de tentativas permitidas).*

- Similaridade de Cosseno entre embeddings $A$ e $B$:

  $$\text{CosineSimilarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{\sum_{i=1}^d A_i B_i}{\sqrt{\sum_{i=1}^d A_i^2} \sqrt{\sum_{i=1}^d B_i^2}}$$

- Função de perda sigmoide para treino de modelos de recompensa a partir de pares:

  $$\mathcal{L} = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma\Big(r_\theta(x, y_w) - r_\theta(x, y_l)\Big) \right]$$

## Exemplos relevantes

- Citação de Terrence Tao comparando a avaliação do GPT-o1 à de um "estudante de pós-graduação medíocre, mas competente", ilustrando o problema de escassez de avaliadores qualificados no topo da distribuição intelectual.
- Falha de similaridade lexical no modelo visual Fuyu (Adept): o modelo gerou uma legenda perfeitamente correta para uma imagem, mas recebeu nota zero porque a resposta exata não constava na lista restrita de referências humanas do benchmark.
- Discrepância na definição de critérios entre frameworks: para o critério "faithfulness" (fidelidade), o MLflow utiliza notas de 1 a 5, o Ragas utiliza valores booleanos 0 e 1, e o LlamaIndex exige respostas textuais "YES" ou "NO", evidenciando a ausência de padronização nas métricas de IA juiz.
- Contaminação da Chatbot Arena por comandos triviais: de 33.000 prompts analisados em 2023, mais de 180 eram apenas "hello" ou "hi", demonstrando que dados abertos de crowdsourcing contêm ruído massivo que dilui a capacidade de diferenciar modelos de elite.

## Limitações e ressalvas

- As métricas de modelagem de linguagem baseadas em perplexidade exigem acesso aos *logprobs* dos tokens da saída, recurso que provedores de modelos comerciais proprietários frequentemente restringem ou omitem por motivos de segurança e propriedade intelectual.
- Os modelos de recompensa e avaliações comparativas assumem transitividade matemática das preferências, hipótese contestada na prática pela subjetividade e dependência contextual das escolhas humanas.

## Dúvidas em aberto

- Como criar sistemas de avaliação de confiança absoluta para tarefas onde a capacidade da IA ultrapassa a fronteira do conhecimento dos maiores especialistas humanos em tempo real?
- Qual é o mecanismo de calibração ideal para neutralizar simultaneamente o viés de verbosidade e a auto-preferência em juízes neurais sem degradar a sensibilidade analítica do avaliador?

## Localização da fonte

Capítulo 3, páginas 113 a 157 do livro impresso / arquivo de texto consolidado.
