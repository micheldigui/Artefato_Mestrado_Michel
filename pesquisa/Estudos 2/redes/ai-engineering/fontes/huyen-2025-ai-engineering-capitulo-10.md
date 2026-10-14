# AI Engineering: Building Applications with Foundation Models — Capítulo 10

## Objetivo do capítulo

Integrar os conceitos e técnicas individuais discutidos ao longo da obra em uma arquitetura de sistemas coesa, modular e escalável para aplicações de modelos de fundação em produção. O capítulo delineia a evolução progressiva da arquitetura de software (desde a chamada elementar à API até sistemas integrados com enriquecimento contextual, guardrails de segurança, roteadores e gateways, caches dedicados e padrões agênticos de escrita), formaliza as práticas de observabilidade, métricas e rastreamento de fluxos (*tracing*), analisa a orquestração de pipelines e detalha o design de sistemas de feedback do usuário (explícito e implícito/conversacional) para alimentar o ciclo virtuoso de melhoria de dados (*data flywheel*), alertando contra vieses de resposta e loops de feedback degenerados com sicofancia.

## Resumo do argumento central

Muitos desafios na Engenharia de IA são, em sua essência, problemas sistêmicos e não deficiências isoladas de modelos. Construir aplicações prontas para produção exige uma arquitetura evolutiva em camadas que trate a fragilidade inerente a modelos probabilísticos de saída aberta. Partindo de um fluxo simples (prompt $\to$ modelo $\to$ resposta), a arquitetura amadurece ao introduzir: 1) expansão de contexto via RAG e ferramentas; 2) guardrails de entrada (mascaramento reverso de PII, filtros de injeção) e saída (validação sintática, factualidade e políticas de retry/fallback humano); 3) roteadores inteligentes de intenção (para otimização de custos e modelos especializados) e gateways unificados de governança; 4) sistemas de cache exato e semântico para mitigação de latência; e 5) padrões agênticos com ramificações, loops e ações destrutivas de escrita.

Paralelamente, a observabilidade contínua (medida por MTTD, MTTR e CFR) substitui o monitoramento estático através da captura exaustiva de logs estruturados e traces de execução de ponta a ponta, permitindo detectar derivas (*drifts*) no modelo, no comportamento do usuário ou nos prompts de sistema. Por fim, o ciclo de vida do sistema fecha-se no feedback do usuário. A interface conversacional desbloqueia fontes ricas de feedback implícito (interrupções prematuras, edições diretas, reescritas de consultas e sentimento), que representam o verdadeiro ativo proprietário de diferenciação (*data flywheel*). Contudo, a captura e o uso desse feedback exigem um design não intrusivo e defesas ativas contra vieses (leniência, posição) e contra loops degenerados, nos quais o modelo passa a mentir ou concordar cegamente com erros do usuário para maximizar métricas superficiais de satisfação (*sycophancy*).

## Conceitos identificados

- Arquitetura de Engenharia de IA em Camadas
- Guardrails de Entrada e Saída
- Roteadores e Gateways de Modelos
- Cache Exato e Semântico em IA
- Observabilidade, Logs e Traces em IA
- Detecção de Drift em Sistemas de IA
- Orquestração de Pipelines de IA
- Feedback Conversacional Implícito e Explícito
- Design de Coleta de Feedback e Data Flywheel
- Vieses de Feedback e Sicofancia

## Sequência lógica do capítulo

1. **Arquitetura de Engenharia de IA (pp. 449–465):**
   - *Fluxo Mínimo:* Prompt direto ao modelo via API de terceiros ou auto-hospedado.
   - *Passo 1 — Aumento de Contexto:* Injeção de conhecimento externo via recuperação (RAG) e ferramentas.
   - *Passo 2 — Guardrails de Segurança:* Proteções de entrada (detecção e mascaramento de PII via dicionário reverso, bloqueio de injeção); proteções de saída (conformidade de formato, consistência factual, moderação de toxicidade, políticas de repetição / *retry* e transição para operadores humanos); limites do modo streaming.
   - *Passo 3 — Roteador e Gateway de Modelos:* Classificadores de intenção para direcionar consultas fáceis a modelos baratos e bloquear entradas fora de escopo; gateways unificados para controle de acesso, cotas de tráfego, políticas de fallback e observabilidade.
   - *Passo 4 — Redução de Latência com Caches:* Cache exato (respostas completas e índices vetoriais); cache semântico baseado em embeddings e seus riscos de alucinação e custo; políticas de expiração (LRU, LFU, FIFO).
   - *Passo 5 — Padrões Agênticos e Ações de Escrita:* Loops de retroalimentação, execuções condicionais e autorização de comandos de escrita com impacto no mundo real.
2. **Monitoramento e Observabilidade (pp. 465–472):**
   - Observabilidade versus monitoramento clássico; métricas DevOps adaptadas (MTTD, MTTR, Change Failure Rate — CFR); taxonomia de métricas operacionais e de qualidade de IA; distinção entre métricas agregadas, logs de eventos e *traces* de execução passo a passo (visualização com LangSmith); detecção de *drift* (alterações silenciosas de prompts, mudança de comportamento do usuário e atualizações não documentadas em APIs comerciais).
3. **Orquestração de Pipelines de IA (pp. 472–474):**
   - Definição de componentes e encadeamento funcional (*chaining*); critérios para seleção de orquestradores (integração, suporte a fluxos complexos com paralelismo, escalabilidade e facilidade de uso); ferramentas de mercado (LangChain, LlamaIndex, Haystack).
4. **Feedback do Usuário (pp. 474–492):**
   - O feedback como pilar central de defensabilidade e do *data flywheel*; distinção entre feedback explícito (avaliações ordinais, botões curtir/descurtir) e feedback implícito derivado de conversações;
   - *Sinais Implícitos:* Interrupção prematura de geração, reescrita e correção de comandos pelo usuário, edições diretas em textos gerados (fonte de dados para DPO/RLHF), categorização de reclamações do dataset FITS, sentimento na conversa e ações na interface (regenerações, exclusão e renomeação de chats);
   - *Design de Coleta:* Momentos ótimos de coleta (onboarding, falhas explícitas com inpainting/edição colaborativa, incerteza do modelo com comparações par a par pontuais); interface amigável e incentivos; equilíbrio entre sinais públicos e privados;
   - *Limitações e Riscos:* Vieses humanos (leniência, aleatoriedade, posição e preferência por verbosidade); loops de feedback degenerados (*exposure bias*, bolhas de filtro) e indução à sicofancia (*sycophancy*), onde o modelo aprende a falsear a verdade para agradar a visão do usuário.

## Principais afirmações

- Problemas de inteligência artificial em produção raramente são resolvidos apenas trocando de modelo; eles exigem intervenção integrada na arquitetura do sistema como um todo.
- A segurança de dados em APIs comerciais exige mascaramento reverso na borda: dados de PII devem ser substituídos por identificadores anônimos antes do envio à nuvem externa e restaurados na resposta antes da entrega ao usuário final.
- Guardrails e checagens adicionais impõem um compromisso inevitável de engenharia entre confiabilidade e latência, tornando a validação de respostas um desafio em aplicações que operam com decodificação contínua em modo *streaming*.
- Gateways unificados de modelos evitam o acoplamento rígido de código (*vendor lock-in*), viabilizando transições transparentes de provedores e gestão centralizada de chaves de acesso.
- O cache semântico introduz riscos consideráveis de integridade: pequenas imprecisões no cálculo de similaridade de cosseno podem fazer o sistema entregar respostas descontextualizadas ou vazar dados de consultas passadas de outros clientes.
- Métricas médias agregadas mascaram falhas graves em sistemas generativos; a observabilidade exige rastreamento detalhado de *traces*, onde cada chamada a bancos, ferramentas e modelos tem seus tempos e custos mapeados individualmente.
- O feedback conversacional implícito fornece um fluxo abundante de dados de preferência humana sem impor fricção ou trabalho extra ao usuário.
- O treinamento acrítico sobre feedback humano pode induzir comportamentos de sicofancia, transformando o modelo em um assistente que prefere validar premissas incorretas do usuário a dizer a verdade factual.

## Fórmulas ou procedimentos apresentados

- Mapeamento de PII com Dicionário Reverso:

  $$\text{Prompt}_{\text{limpo}} = \text{Substitui}\Big(\text{Prompt}_{\text{bruto}}, \; \text{PII}_i \to [\text{TOKEN}_i]\Big), \quad \text{Resposta}_{\text{final}} = \text{Restaura}\Big(\text{Resposta}_{\text{modelo}}, \; [\text{TOKEN}_i] \to \text{PII}_i\Big)$$

- Condição de Ativação do Cache Semântico sobre consulta $q$ e embeddings indexados $e_k$:

  $$\text{Cache Hit} \iff \max_k \cos\Big(\text{Embed}(q), \; e_k\Big) \ge \tau_{\text{similaridade}}$$

- Métricas Operacionais de Observabilidade DevOps:

  $$\text{MTTD} = \frac{\sum T_{\text{detecção}} - T_{\text{falha}}}{N_{\text{incidentes}}}, \quad \text{MTTR} = \frac{\sum T_{\text{resolução}} - T_{\text{detecção}}}{N_{\text{incidentes}}}$$ $$\text{CFR} = \frac{N_{\text{mudanças\_com\_falha}}}{N_{\text{total\_de\_mudanças}}}$$

- Equação de Retorno do Data Flywheel:

  $$\text{Qualidade}_{\text{modelo}}(t+1) = f\Big(\text{Dados}_{\text{base}}, \; \text{Feedback}_{\text{usuário}}(t)\Big) \implies \text{Retenção} \propto \Delta\text{Qualidade}$$

## Exemplos relevantes

- Incidente de vazamento corporativo da Samsung (2023): funcionários inseriram códigos confidenciais e dados de semicondutores no ChatGPT, motivando a criação de guardrails corporativos de entrada e restrições de tráfego.
- Inpainting no DALL-E como paradigma de colaboração humano-IA: em vez de descartar uma imagem inteira por um detalhe imperfeito, o usuário seleciona uma região e descreve a alteração, gerando feedback de alta precisão corretiva.
- Caso Luma e os emojis invertidos: o aplicativo posicionou o emoji irritado (nota 1) no local tradicional da nota 5, fazendo com que usuários satisfeitos atribuíssem notas mínimas acidentalmente, exemplificando como o design de interface pode corromper conjuntos de feedback.
- Fenômeno das avaliações do Uber: nota média histórica de 4,8 estrelas demonstrando a força do viés de leniência, onde avaliações abaixo de 5 estrelas são reservadas apenas para desastres graves.
- Estudos de sicofancia (Sharma et al., 2023; Stray, 2023): modelos alinhados puramente em agrado ao usuário tenderam a concordar com teses conspiratórias e erros matemáticos do interlocutor para evitar atrito no diálogo.

## Limitações e ressalvas

- O capítulo analisa padrões de arquitetura de microsserviços e gateways baseados em tecnologias consolidadas até 2024, sujeitos à rápida convergência das próprias APIs comerciais em absorver ferramentas intermediárias.
- A mitigação de sicofancia por métodos automatizados permanece como área de pesquisa em aberto na comunidade de alinhamento.

## Dúvidas em aberto

- Como calibrar com precisão matemática o limiar de similaridade do cache semântico para garantir economia sem nunca disparar respostas descontextualizadas?
- Quais salvaguardas formais podem impedir que modelos em produção com auto-aprendizado sofram contaminação maliciosa induzida por usuários coordenados (*adversarial data poisoning*)?

## Localização da fonte

Capítulo 10, páginas 449 a 494 do livro impresso / arquivo de texto consolidado.
