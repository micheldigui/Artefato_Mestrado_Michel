# 🧠 Ajuste Fino (Finetuning)

**Rede:** `ai-engineering`   **Área:** `treinamento`

**Rede:** `ai-engineering`  
areas: `aprendizado-de-maquina`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 11, 41–42, 307–319

## 📝 Definição

### Definição formal

O **Ajuste Fino** (*Finetuning*) é o processo de aprendizado por transferência no qual um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] já pré-treinado tem todos ou uma fração de seus parâmetros internos de peso $\theta$ atualizados através de treinamento supervisionado adicional com gradiente descendente sobre um conjunto de dados especializado e rotulado.

O processo de continuar o treinamento de um modelo de fundação pré-treinado utilizando um conjunto de dados específico de uma tarefa, atualizando os pesos internos da rede neural para especializar o seu comportamento.

### Em linguagem simples

É pegar um modelo que já sabe tudo sobre a língua comum e dar a ele um treinamento extra intensivo focado exclusivamente na tarefa da sua empresa. Você altera as conexões neurais do próprio modelo para que ele aprenda a pensar, falar e estruturar respostas de uma maneira específica, sem que você precise lembrá-lo a cada mensagem.

É o ato de "dar uma aula particular" ou especialização para a IA, treinando-a com exemplos práticos para que ela aprenda a se comportar de uma maneira muito específica (como adotar um tom de voz corporativo ou gerar código em uma linguagem rara).

### Escopo e distinções

Não se confunde com o pré-treinamento (*pre-training*), que consome meses e milhões de dólares em dados brutos. O ajuste fino consome ordens de grandeza menos computação e dados, focando em especialização. Também difere da [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]] e do [[redes/ai-engineering/conceitos/rag.md|RAG]], pois o finetuning modifica fisicamente os pesos do modelo.

Não se confunde com o pré-treinamento (*pre-training*), que consome meses e milhões de dólares em dados brutos. O ajuste fino consome ordens de grandeza menos computação e dados, focando em especialização. Também difere da [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]] e do [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]], pois o finetuning modifica fisicamente os pesos do modelo.

Diferencia-se do RAG: o finetuning altera permanentemente os pesos e o estilo de comportamento da rede, enquanto o RAG apenas injeta informações factuais externas de forma temporária via prompt.

## 🧩 Problema que resolve

Resolve a ineficiência de contexto e a instabilidade comportamental. Modelos que operam exclusivamente com prompts longos gastam excesso de tokens de entrada a cada requisição para serem lembrados de formatações complexas (ex.: código customizado, termos jurídicos raros ou JSON estrito). O finetuning "grava" essas preferências diretamente na estrutura interna do modelo, viabilizando respostas ultrarrápidas, concisas e com prompts mínimos.

Resolve a dificuldade de induzir modelos gerais a seguirem formatos rígidos de saída (como JSON estruturado) ou adotarem personas e estilos complexos apenas através de instruções textuais em *prompts*.

## 💡 Intuição

Pense em um piloto de avião comercial experiente que é contratado para pilotar um novo modelo de jato executivo. Ele não precisa aprender do zero o que é sustentação aerodinâmica, altitude ou navegação por rádio (pré-treinamento). Ele precisa apenas passar por algumas sessões em um simulador específico daquela aeronave para adaptar seus reflexos e comandos operacionais (ajuste fino).

Pense em um médico recém-formado (modelo de fundação): ele sabe medicina geral, mas para virar um cirurgião cardíaco de elite, ele precisa fazer residência médica e cirurgias práticas supervisionadas (ajuste fino).

## ⚙️ Como funciona

O processo parte dos pesos consolidados da fase prévia:

### Etapas

1. **Curadoria do conjunto de ajuste:** Montagem de pares de alta qualidade contendo solicitações e respostas ideais `(instrução, resposta_esperada)`.
2. **Carregamento do modelo base:** O modelo de fundação é instanciado com seus pesos pré-treinados congelados ou preparados para atualização.
3. **Passagem direta (*forward pass*):** O modelo processa a instrução e gera sua predição.
4. **Cálculo da perda supervisionada:** A predição é comparada com a resposta ideal da curadoria.
5. **Retropropagação e atualização de pesos:** O algoritmo de otimização ajusta a totalidade dos pesos (*Full Finetuning*) ou uma matriz compacta de adaptadores auxiliares (técnicas de PEFT/LoRA).
6. **Avaliação comparativa:** O modelo ajustado é avaliado para assegurar que ganhou a habilidade desejada sem sofrer degradação catastrófica de suas capacidades gerais.

1. Seleção de um modelo de fundação base adequado.
2. Criação ou aquisição de um dataset especializado de instrução e resposta.
3. Execução do treinamento de atualização de pesos com hiperparâmetros ajustados (como taxa de aprendizado reduzida).
4. Avaliação do modelo ajustado frente aos critérios de aceitação da aplicação.

### Entradas e saídas

- **Entradas:** Pesos de um modelo de fundação pré-treinado e um conjunto de dados supervisionado representativo.
- **Saídas:** Novos pesos de modelo (ou arquivos leves de adaptadores) especializados na tarefa.

- Entradas: Modelo de fundação base e dataset de adaptação supervisionada.
- Saídas: Um novo modelo especializado com pesos modificados.

## 📐 Formulação matemática

Diferente do pré-treino que parte de pesos aleatórios, o finetuning inicia de $\theta_{\text{base}}$ e otimiza para a distribuição de dados da tarefa $\mathcal{D}_{\text{alvo}}$:

$$\theta^* = \arg\min_\theta \sum_{(x, y) \in \mathcal{D}_{\text{alvo}}} \mathcal{L}\big(f_\theta(x), y\big) + \lambda \|\theta - \theta_{\text{base}}\|^2$$

Onde o termo de regularização impede que o modelo se desvie excessivamente de suas capacidades linguísticas originais, prevenindo o esquecimento catastrófico (*catastrophic forgetting*).

Dado um modelo com pesos pré-treinados $\Theta$, o ajuste fino otimiza esses pesos em direção a um conjunto de dados de adaptação $D_{fine}$ através de descida de gradiente:

$$\Theta_{novo} = \Theta - \eta \nabla_\Theta \sum_{(x,y) \in D_{fine}} \mathcal{L}(M_\Theta(x), y)$$

Onde:
- $\Theta$: Pesos iniciais do modelo de fundação.
- $\eta$: Taxa de aprendizado (*learning rate*).
- $\mathcal{L}$: Função de perda avaliando a divergência entre a predição $M_\Theta(x)$ e o alvo $y$.

## 🧱 Hipóteses e condições de validade

- O conjunto de dados de ajuste deve possuir altíssima consistência e ausência de ruído; a literatura comprova que poucas centenas de exemplos perfeitos superam milhares de dados ruidosos.
- O modelo base deve possuir representações prévias compatíveis com o domínio (ex.: ajustar para medicina um modelo que nunca viu termos biológicos no pré-treino gera resultados medíocres).

- Hipótese de que o modelo base possui capacidade representacional subjacente suficiente para assimilar os novos padrões sem sofrer degradação catastrófica de competências gerais anteriores.

## ✅ Quando usar

- Quando se deseja padronizar o estilo, brevidade ou estrutura de saída (ex.: geração impecável de código em sintaxe proprietária).
- Quando se quer reduzir o consumo de tokens de entrada eliminando prompts excessivamente longos.
- Para treinar modelos menores (ex.: 7B ou 8B parâmetros) para baterem o desempenho de modelos gigantescos (70B+) em um domínio delimitado.

## 🚫 Quando não usar

- Para adicionar informações factuais que se alteram com frequência semanal ou diária (onde o [[redes/ai-engineering/conceitos/rag.md|RAG]] é a solução correta).
- Na fase de exploração inicial de um produto, antes de validar se o caso de uso tem demanda real de mercado.

- Para adicionar informações factuais que se alteram com frequência semanal ou diária (onde o [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]] é a solução correta).
- Na fase de exploração inicial de um produto, antes de validar se o caso de uso tem demanda real de mercado.

- Para injetar fatos recentes, notícias ou dados corporativos dinâmicos que mudam diariamente (cenário ideal para RAG).

## ⚠️ Limitações e armadilhas

- **Esquecimento catastrófico (*Catastrophic Forgetting*):** Ao especializar-se intensamente em uma tarefa restrita, o modelo pode desaprender competências gerais de conversação ou raciocínio lógico.
- **Custo de manutenção e obsolescência:** Toda vez que o provedor do modelo base lança uma nova versão de fundação, o modelo ajustado precisa ser re-treinado para aproveitar os novos avanços.

- Risco de esquecimento catastrófico (*catastrophic forgetting*), onde o modelo perde habilidades gerais que possuía antes do ajuste.
- Custos computacionais de treinamento e manutenção de checkpoints customizados.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[finetuning|Finetuning]] | Especializar comportamento e formato alterando os pesos. | Dataset de pares de instrução e resposta. | Modelo com pesos modificados. | Modifica permanentemente a rede neural interna. |
| [[rag|RAG]] | Fornecer fatos dinâmicos externos via contexto. | Consulta do usuário + Documentos recuperados. | Resposta fundamentada factual. | Não altera pesos; atua puramente na camada de prompt. |

| Critério | Ajuste Fino (*Finetuning*) | Engenharia de Prompt |
|---|---|---|
| **Efeito no modelo** | Altera permanentemente os pesos | Não altera nenhum peso |
| **Custo por requisição** | Menor (prompt curto) | Maior (prompt longo com exemplos) |
| **Gargalo de adoção** | Exige coleta e validação de dados de treino | Exige tempo de desenho e iteração de prompt |
| **Hospedagem** | Exige servir pesos customizados | Usa diretamente APIs padrão de mercado |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma fintech possui um sistema de análise de crédito que exige que todas as saídas sigam rigorosamente um formato de arquivo de configuração interno complexo. Usando engenharia de prompt pura, o modelo erra a sintaxe em $12\%$ dos casos e gasta 1.500 tokens de instruções explicativas por chamada.
A equipe coleta 800 análises históricas perfeitamente preenchidas e executa o **ajuste fino** de um modelo leve de código aberto. O novo modelo passa a responder diretamente na sintaxe da empresa com $99{,}8\%$ de acerto sintático e exige um prompt de entrada de apenas 50 tokens.

Pegar o modelo Llama 3 genérico e treiná-lo com 5.000 exemplos de petições jurídicas brasileiras para que ele aprenda a redigir documentos legais rigorosamente dentro dos padrões exigidos pelos tribunais do país.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]

- [[modelo-de-fundacao|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]]
- [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]]

- [[engenharia-de-ia|Engenharia de IA]]

### Alternativas

- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]
- [[redes/ai-engineering/conceitos/rag.md|Geração Aumentada de Recuperação (RAG)]]

- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]
- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]

- [[rag|RAG]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]
- [[redes/ai-engineering/conceitos/desafio-da-ultima-milha-em-ia.md|Desafio da Última Milha em IA]]

- Nenhuma relação suficientemente sustentada pelo capítulo.

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 11, 41–42, 307–319
- **Evidência:** Chip Huyen define o finetuning como o treinamento contínuo que altera pesos para adaptar o modelo a tarefas específicas, ressaltando a distinção de que finetuning serve primariamente para "forma e comportamento", enquanto RAG serve para "fatos".
- **Confiança:** Alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introdução à Construção de Aplicações de IA com Modelos de Fundação
- **Localização:** localização não informada no material recebido
- **Evidência:** Definição do ajuste fino (*finetuning*) como técnica de adaptação interna de modelos para customização de tarefas.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. Qual é a definição de finetuning e em que ele difere formalmente do pré-treinamento de um modelo?
2. Por que o ajuste fino é considerado uma técnica paramétrica de adaptação de modelos?
3. O que fundamenta a célebre máxima de engenharia: "Finetuning é para forma, RAG é para fatos"?
4. O que é o fenômeno do esquecimento catastrófico (*catastrophic forgetting*) durante o ajuste fino?
5. Quais são as vantagens financeiras e de latência ao se adotar finetuning em sistemas com altíssimo volume de requisições?
6. Por que a curadoria de poucos exemplos de alta qualidade costuma ser superior a conjuntos maciços e ruidosos no ajuste fino?
7. Qual é o risco de se realizar o ajuste fino antes de esgotar as possibilidades da engenharia de prompt?

1. O que é Ajuste Fino (Finetuning)?
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

## ✅ Когда usar / Quando usar

- Quando a aplicação exige padronização rigorosa de formato de saída, adoção de personas complexas ou especialização profunda em um domínio com vocabulário restrito.
