# AI Engineering: Building Applications with Foundation Models — Capítulo 2

## Objetivo do capítulo

Desmistificar a arquitetura interna, o processo de criação e o comportamento operacional dos modelos de fundação. O capítulo examina as decisões críticas de projeto que determinam as capacidades e restrições das aplicações a jusante: a curadoria e assimetria de dados de treinamento, a mecânica da arquitetura Transformer frente a alternativas lineares, o dimensionamento e as leis de escala computacional, o pós-treinamento para alinhamento com a preferência humana, as estratégias de amostragem probabilística e as causas fundamentais da inconsistência e das alucinações.

## Resumo do argumento central

A eficácia de uma aplicação de IA depende de compreender que os modelos de fundação não são oráculos determinísticos, mas distribuidores probabilísticos moldados por seus dados de pré-treino, sua arquitetura física e suas etapas de pós-treinamento. O pré-treino com auto-supervisão em corpora massivos gera competências latentes, mas reflete assimetrias severas de dados (como o domínio do inglês em relação a línguas de baixos recursos) e saturação iminente de dados públicos e energia. A arquitetura Transformer domina o cenário através do mecanismo de atenção multi-cabeça, dividindo a inferência em duas fases computacionalmente distintas: prefill (paralelo e limitado por cálculo) e decode (sequencial e limitado por largura de banda de memória). Modelos esparsos como Mixture-of-Experts (MoE) reduzem o custo ativo por token. Para torná-los utilizáveis e seguros, o pós-treinamento combina ajuste fino supervisionado (SFT) com alinhamento de preferências (RLHF ou DPO). Por fim, o comportamento final em produção é fortemente controlado em tempo de inferência por amostragem (temperatura, top-k, top-p, saídas estruturadas) e computação em tempo de teste (*test time compute*). As alucinações decorrem tanto da auto-ilusão cumulativa do processo autoregressivo quanto do descompasso entre o conhecimento interno do modelo e as exigências das anotações humanas.

## Conceitos identificados

- Mecanismo de Atenção
- Fases de Inferência: Prefill e Decode
- Modelos de Espaço de Estados (SSMs)
- Mixture of Experts (MoE)
- Leis de Escala e Chinchilla
- Gargalos de Escala: Dados e Energia
- Pós-Treinamento e Alinhamento
- Ajuste Fino Supervisionado (SFT)
- Aprendizado por Reforço com Feedback Humano (RLHF)
- Otimização Direta de Preferência (DPO)
- Amostragem e Temperatura
- Amostragem Top-k e Top-p
- Computação em Tempo de Teste (Test Time Compute)
- Amostragem Restrita e Saídas Estruturadas
- Alucinação em Modelos de Fundação
- Modelo de Fundação
- Tokenização e Vocabulário

## Sequência lógica do capítulo

1. **Dados de Treinamento (pp. 50–57):** Qualidade e procedência do Common Crawl/C4; disparidades de eficiência e custo em modelos multilíngues e línguas de baixos recursos; modelos focados em domínios específicos (AlphaFold, Med-PaLM 2).
2. **Modelagem e Arquitetura (pp. 58–66):** Limitações do seq2seq com RNNs; formulação matemática da atenção ($Q, K, V$); blocos Transformer e matrizes lineares; separação operacional de prefill e decode; alternativas emergentes (RWKV e Modelos de Espaço de Estados como S4, H3, Mamba e Jamba).
3. **Tamanho do Modelo e Leis de Escala (pp. 67–77):** Parâmetros e esparsidade; arquiteturas Mixture-of-Experts (MoE, Mixtral 8x7B); métricas de computação (FLOPs, FLOP/s, MFU); Lei de Escala de Chinchilla para alocação ótima de parâmetros e dados de treino; extrapolação e $\mu\text{P}$; gargalos físicos (exaustão de dados públicos, colapso de modelo por dados sintéticos e escassez de eletricidade).
4. **Pós-Treinamento (pp. 78–88):** Transição de completação de texto para diálogo; Ajuste Fino Supervisionado (SFT) via clonagem comportamental com dados de demonstração; Alinhamento de Preferência via RLHF (modelagem de recompensa pairwise, função de perda sigmoid, otimização PPO) e DPO.
5. **Amostragem e Geração (pp. 88–105):** Logits, softmax e logprobs; amostragem gulosa vs. estocástica; Temperatura; Top-k e Top-p (amostragem de núcleo); condições de parada; Computação em Tempo de Teste (Best-of-N, verificadores e equivalência com aumento de escala); Saídas Estruturadas (parsing semântico, amostragem restrita guiada por gramática e decodificadores especializados).
6. **A Natureza Probabilística da IA (pp. 105–111):** Inconsistência (mesma entrada com saídas diferentes; sementes e desvios de hardware); Alucinação: definição, hipótese da auto-ilusão (*snowballing*) e hipótese da divergência de conhecimento interno/anotador; mitigações pragmáticas.

## Principais afirmações

- Modelos de linguagem sofrem disparidades extremas de custo de inferência e latência entre idiomas devido a tokenizadores otimizados desproporcionalmente para o inglês.
- O mecanismo de atenção do Transformer supera os RNNs pelo processamento paralelo de entradas, mas a decodificação de saída permanece estritamente sequencial.
- Na inferência de LLMs, o prefill é *compute-bound* (limitado pelo processamento da GPU), enquanto o decode é *memory-bandwidth bound* (limitado pela taxa de transferência da memória de alta largura de banda para os núcleos).
- A Lei de Escala de Chinchilla dita que, para otimalidade computacional, o volume de tokens de treinamento deve escalar linearmente com o número de parâmetros, mantendo a proporção de aproximadamente 20 tokens por parâmetro em modelos densos.
- O crescimento contínuo da escala de pré-treinamento aproxima-se de dois gargalos físicos intransponíveis no curto prazo: o esgotamento do estoque de dados textuais humanos de alta qualidade na internet pública e os limites de infraestrutura da rede de distribuição de energia elétrica.
- O pós-treinamento com dados de demonstração (SFT) e preferência (RLHF/DPO) não introduz conhecimento factual de forma primária; sua função essencial é alinhar a forma de expressão e a utilidade comunicacional do modelo aos padrões de preferência dos usuários.
- Aumentar a computação em tempo de inferência através de rascunhos paralelos e modelos verificadores especializados (*test time compute*) pode produzir ganhos de acurácia em tarefas complexas comparáveis a aumentar o tamanho físico do modelo em até 30 vezes.
- A alucinação em LLMs decorre prioritariamente do condicionamento autorregressivo cego, onde erros iniciais são incorporados ao contexto como verdades inquestionáveis pelo próprio modelo (*self-delusion*), e de tentativas de forçar o modelo a responder fatos que não constam em sua distribuição de pesos.

## Fórmulas ou procedimentos apresentados

- Atenção escalada por produto escalar:
  $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
- Conversão de logits para probabilidades com temperatura:
  $$p_i = \frac{e^{x_i / T}}{\sum_j e^{x_j / T}}$$
- Probabilidade conjunta de sequência na amostragem:
  $$P(x_1, \dots, x_n) = \prod_{i=1}^n P(x_i \mid x_{<i}) \implies \log P(x_1, \dots, x_n) = \sum_{i=1}^n \log P(x_i \mid x_{<i})$$
- Função de perda de treino do Modelo de Recompensa (RLHF):
  $$\mathcal{L}_{\text{RM}}(\theta) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma\Big(r_\theta(x, y_w) - r_\theta(x, y_l)\Big) \right]$$
- Proporção empírica de Chinchilla para modelos densos:
  $$N_{\text{tokens}} \approx 20 \times N_{\text{parâmetros}}$$

## Exemplos relevantes

- Análise de tokenização no dataset MASSIVE: a mesma sentença expressa consome mediana de 7 tokens em inglês, 32 tokens em hindi e 72 tokens em birmanês, tornando a inferência em birmanês 10 vezes mais cara e lenta.
- Mixtral 8x7B: modelo esparso com 46,7 bilhões de parâmetros totais que ativa apenas 12,9 bilhões de parâmetros por token, executando com a velocidade e custo computacional de um modelo de 13B.
- Experimento da OpenAI com verificadores de soluções matemáticas (Cobbe et al., 2021): o uso de um modelo verificador para selecionar entre múltiplos rascunhos gerou ganho de desempenho equivalente a um salto de 30 vezes na escala de parâmetros do modelo gerador.
- Episódio de auto-ilusão no modelo LLaVA-v1.5-7B: ao confundir uma embalagem de xampu com leite na primeira premissa, o modelo passou a listar leite como ingrediente ativo na composição química do produto.

## Limitações e ressalvas

- As formulações de leis de escala referem-se a modelos densos treinados sobre dados predominantemente humanos; a adaptação precisa dessas curvas para arquiteturas MoE e dados majoritariamente sintéticos permanece como campo ativo de investigação empírica.
- O capítulo descreve os mecanismos fundamentais de alinhamento e amostragem, reservando os procedimentos técnicos aprofundados de quantização de hardware e memória de treinamento para o Capítulo 7.

## Dúvidas em aberto

- Como calibrar com precisão o ponto de transição em que dados gerados por IA passam a deteriorar a estabilidade representacional das gerações subsequentes (*model collapse*) versus refinar o alinhamento?
- Modelos autorregressivos puros poderão eliminar completamente alucinações sem acoplamento obrigatório a motores determinísticos externos de verificação e recuperação?

## Localização da fonte

Capítulo 2, páginas 49 a 112 do livro impresso / arquivo de texto consolidado.
