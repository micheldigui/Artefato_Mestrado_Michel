# 🧠 Detecção de Drift em Sistemas de IA

**Rede:** `ai-engineering`   **Área:** `governanca`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 10 — AI Engineering Architecture and User Feedback
- Localização: Páginas 471–472

## 📝 Definição

### Definição formal

A **Detecção de Drift em Sistemas de IA** (*Drift Detection*) é a metodologia de monitoramento contínuo voltada a identificar alterações estatísticas, semânticas ou comportamentais na distribuição dos dados de entrada, nas saídas geradas ou no desempenho empírico de uma aplicação baseada em [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]] ao longo do tempo, estruturando-se em três vetores causais primários:

1. **Deriva do Modelo Subjacente (*Underlying Model Drift*):** Modificações silenciosas, atualizações de pesos ou otimizações de infraestrutura aplicadas por provedores comerciais de API sem aviso prévio transparente, alterando a distribuição de saídas da aplicação;
2. **Deriva de Comportamento do Usuário (*User Behavior Drift*):** Mudanças na forma como os usuários interagem com o sistema à medida que se adaptam à tecnologia (ex.: aprendendo a ser mais concisos, explorando brechas ou submetendo tarefas progressivamente mais complexas);
3. **Deriva de Prompt de Sistema (*System Prompt Drift*):** Alterações acidentais, edições de templates compartilhados ou correções pontuais de texto que modificam inadvertidamente o comportamento da aplicação em produção.

### Em linguagem simples

É o alarme que avisa quando "as regras do jogo mudaram sem você perceber". Um aplicativo de IA pode começar a dar respostas piores por três motivos: a OpenAI ou o Google atualizaram a IA deles por baixo do capô sem te avisar; os seus clientes mudaram o jeito de escrever e estão fazendo perguntas mais difíceis; ou um colega de equipe mexeu no texto do prompt de sistema da empresa e esqueceu de avisar aos outros. O monitoramento de drift descobre exatamente qual dessas três coisas aconteceu.

### Escopo e distinções

Em ML tradicional, o drift era puramente estatístico (mudança na média ou variância de colunas numéricas de tabelas). Na Engenharia de IA com LLMs, o drift abrange **mudanças semânticas e estilísticas sutis** em texto aberto, exigindo técnicas de análise de distribuição de tokens, comprimentos de resposta e testes contínuos de regressão.

## 🧩 Problema que resolve

Resolve a degradação silenciosa de sistemas em produção. Aplicações de IA raramente quebram com mensagens formais de erro de software; elas simplesmente passam a responder com pior qualidade, aumentam alucinações ou erram classificações sutis. Monitorar drift permite identificar quedas de acurácia antes que os clientes abandonem o produto.

## 💡 Intuição

Pense em um sensor de água em uma estação de tratamento:

- **Deriva do Usuário:** A população da cidade começou a cozinhar com um novo tipo de óleo vegetal que deixa a água do esgoto mais gordurosa. A água que chega mudou na origem.
- **Deriva do Modelo (Fornecedor):** A fábrica que vende os filtros de cloro para a estação alterou a fórmula química do produto sem avisar a prefeitura. O filtro que antes limpava em 5 minutos agora demora 10 minutos.
- **Deriva do Sistema:** O operador da estação girou uma válvula manual achando que era uma torneira comum.

## ⚙️ Como funciona

A detecção de drift opera através de rotinas estatísticas de comparação temporal:

### Etapas

1. **Linha de Base Histórica (*Baseline*):** Registra-se a distribuição de referência da aplicação em seu estado ótimo homologado (extensão média de tokens de entrada e saída, distribuição de vocabulário, taxa de chamadas de ferramentas e escores em suítes de teste).
2. **Janelamento Temporal de Produção:** O sistema coleta amostras contínuas de dados de telemetria das últimas 24 horas ou última semana.
3. **Detecção de Mudança de Prompt de Sistema:** Um script determinístico calcula o hash criptográfico do prompt de sistema consolidado a cada deploy; se o hash divergir, um evento de auditoria é registrado.
4. **Auditoria de Distribuição de Usuários:** Analisa-se métricas de texto: se o número médio de tokens por mensagem de usuário estiver caindo gradualmente, isso indica que os usuários aprenderam a ser mais concisos ou estão insatisfeitos com respostas longas.
5. **Testes Sintéticos Canários (*Canary Evaluations*):** Dispara-se periodicamente (ex.: a cada 6 horas) uma bateria fixa de 50 perguntas canônicas idênticas contra a API do modelo; se as respostas divergirem das respostas homologadas ou a taxa de acerto cair, conclui-se que o **provedor da API alterou o modelo subjacente**.

### Entradas e saídas

- **Entradas:** Telemetria contínua de produção e resultados de testes canários periódicos.
- **Saídas:** Alertas de desvio distribucional e relatórios de causa raiz (modelo, usuário ou prompt).

## 📐 Formulação matemática

A divergência distribucional entre as saídas na janela de referência $P_{\text{base}}(Y)$ e na janela de monitoramento atual $P_{\text{atual}}(Y)$ pode ser quantificada pela divergência de Jensen-Shannon ($\text{JSD}$) sobre a frequência de tokens ou categorias de intenção:

$$\text{JSD}\Big(P_{\text{base}} \;\parallel\; P_{\text{atual}}\Big) = \frac{1}{2} \mathcal{D}_{\text{KL}}(P_{\text{base}} \parallel M) + \frac{1}{2} \mathcal{D}_{\text{KL}}(P_{\text{atual}} \parallel M), \quad \text{onde } M = \frac{1}{2}(P_{\text{base}} + P_{\text{atual}})$$

O estudo empírico de Chen et al. (Stanford/Berkeley, 2023) citado no capítulo demonstrou alterações brutais de performance entre versões datadas de APIs da OpenAI (março de 2023 versus junho de 2023), onde a acurácia do GPT-4 na identificação de números primos despencou de **$97{,}6\%$ para $2{,}4\%$**, e o modelo Voiceflow registrou queda de **$10\%$** na classificação de intenções ao migrar do `gpt-3.5-turbo-0301` para o `gpt-3.5-turbo-1106`.

## 🧱 Hipóteses e condições de validade

- A detecção de drift em modelos proprietários exige a execução disciplinada de baterias de testes com temperatura travada em zero ($T=0$) para assegurar que divergências observadas decorram de alterações reais no modelo e não de ruído estocástico de amostragem.

## ✅ Quando usar

- Mandatório em qualquer aplicação corporativa construída sobre APIs de modelos de fundação gerenciadas por terceiros.
- Monitoramento de conformidade em setores regulados onde a previsibilidade das respostas é exigência contratual ou legal.

## 🚫 Quando não usar

- Em modelos de pesos abertos totalmente auto-hospedados em servidores próprios onde os arquivos de peso estão congelados em disco e os prompts são imutáveis (onde o drift de modelo é fisicamente impossível).

## ⚠️ Limitações e armadilhas

- **Confundir adaptação do usuário com quebra de modelo:** Uma queda na extensão das respostas pode não ser um defeito do LLM, mas uma consequência de os usuários estarem enviando prompts mais curtos e objetivos.
- **Falsos alarmes em pequenas amostras:** Disparar alertas de drift após inspecionar apenas 10 conversas atípicas de um único usuário que explorou casos de borda exóticos.

## 🔍 Comparações

| Vetor de Drift | O que mudou? | Quem causou? | Como diagnosticar? |
|---|---|---|---|
| **Modelo Subjacente** | Pesos, alinhamento ou infra da API | O provedor da nuvem (OpenAI, Google) | Testes canários com temperatura zero |
| **Comportamento do Usuário**| Estilo, vocabulário e intenções | Os clientes finais da aplicação | Análise de distribuição de prompts de entrada |
| **Prompt de Sistema** | Instruções de base do produto | Engenheiro da própria equipe | Controle de versão de software (Git/Hash) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

A empresa Voiceflow opera um assistente conversacional:

- Na segunda-feira, a taxa de acerto na classificação de intenções dos clientes era de **92%**.
- Na quarta-feira, a acurácia cai subitamente para **82%**, disparando reclamações de clientes cujas mensagens estavam sendo roteadas para os setores errados.
- O engenheiro investiga o Git: nenhum código nem prompt foi alterado pela equipe (**zero drift de sistema**).
- Ele analisa as mensagens dos usuários: as pessoas continuam fazendo as mesmas perguntas normais de sempre (**zero drift de usuário**).
- Ele roda a suíte de testes canários e descobre que o provedor da nuvem atualizou silenciosamente o endpoint da API para uma nova versão calibrada para ser mais concisa. A nova versão do provedor quebrou a classificação estruturada da empresa, comprovando um caso clássico de **Underlying Model Drift**.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/observabilidade-logs-e-traces-em-ia.md|Observabilidade, Logs e Traces em IA]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/desenvolvimento-orientado-por-avaliacao.md|Desenvolvimento Orientado por Avaliação]]
- [[redes/ai-engineering/conceitos/roteadores-e-gateways-de-modelos.md|Roteadores e Gateways de Modelos]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (representa a disciplina de auditoria de desvios temporais).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/templates-de-chat-e-prompts-de-sistema.md|Templates de Chat e Prompts de Sistema]]
- [[redes/ai-engineering/conceitos/modelos-abertos-versus-apis-proprietarias.md|Modelos Abertos versus APIs Proprietárias]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 10 — AI Engineering Architecture and User Feedback
- **Localização:** Páginas 471–472
- **Evidência:** Chip Huyen formaliza as três origens de drift em sistemas de modelos de fundação, analisa a pesquisa de Chen et al. (2023) comprovando oscilações radicais de acurácia entre versões de APIs da OpenAI (Figura 4-9) e relata casos empíricos reais como a queda de 10% de acerto enfrentada pela Voiceflow.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as três origens estruturais de drift em sistemas baseados em modelos de fundação descritas no texto?
2. O que é o *Underlying Model Drift* e por que ele afeta predominantemente aplicações que consomem APIs comerciais fechadas?
3. Qual foi a constatação empírica do estudo de Chen et al. (2023) sobre o comportamento de versões do GPT-4 entre março e junho de 2023?
4. Como a adaptação comportamental dos usuários finais (*User Behavior Drift*) pode alterar as métricas operacionais da aplicação ao longo do tempo?
5. O que são testes sintéticos canários (*canary tests*) e como eles isolam alterações introduzidas pelo provedor da API?
6. Como o caso prático documentado pela empresa Voiceflow exemplifica os riscos de atualizações não notificadas em modelos de linguagem?
7. Por que calcular o hash criptográfico do prompt de sistema é a primeira etapa de triagem na investigação de um drift?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
