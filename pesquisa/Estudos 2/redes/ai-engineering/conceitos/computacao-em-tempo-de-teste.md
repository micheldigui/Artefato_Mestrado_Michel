---
title: "Computação em Tempo de Teste"
type: "conceito"
network: "ai-engineering"
aliases:
  - test time compute
  - inference-time compute
tags:
  - inferencia
  - ai-engineering
---

# 🧠 Computação em Tempo de Teste (Test Time Compute)

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 96–99

## 📝 Definição

### Definição formal

A **Computação em Tempo de Teste** (*Test Time Compute* ou *Inference-Time Compute*) é a estratégia algorítmica de alocação expandida de recursos computacionais durante a fase de inferência de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]], gerando múltiplos caminhos candidatos de resposta para uma mesma consulta e empregando mecanismos de seleção, busca (como *beam search*), votação por autoconsistência ou validação por **modelos verificadores** (*verifiers*) para identificar a saída ideal, maximizando o desempenho do sistema sem alterar os parâmetros do modelo original.

### Em linguagem simples

É a estratégia de fazer o modelo "pensar mais e rascunhar várias vezes" antes de dar a resposta definitiva. Em vez de aceitar o primeiro texto que o modelo cospe na tela, o sistema gera 5 ou 10 rascunhos diferentes e usa um modelo juiz especializado para escolher qual rascunho está certo, ou faz uma votação para ver qual resultado matemático apareceu mais vezes.

### Escopo e distinções

O termo utiliza "tempo de teste" por convenção histórica da pesquisa em aprendizado de máquina, mas refere-se estritamente à execução em produção na inferência. Representa uma mudança de paradigma: em vez de gastar milhões para treinar um modelo 30 vezes maior, você usa um modelo menor e gasta mais computação gerando e filtrando opções sob demanda.

## 🧩 Problema que resolve

Resolve a barreira de acurácia em tarefas complexas de raciocínio passo a passo, como provas de matemática, lógica e geração de código de missão crítica. Modelos autorregressivos tomam decisões probabilísticas palavra por palavra; se errarem um cálculo na terceira linha, todo o restante do raciocínio desmorona. Gerar múltiplos caminhos e validar a melhor solução elimina falhas pontuais de amostragem.

## 💡 Intuição

Pense em um estudante resolvendo uma questão discursiva difícil em um concurso público concorrido.
- Se ele escrever a resposta diretamente na folha de respostas definitiva à caneta (**inferência padrão de tentativa única**), qualquer deslize de atenção anula a questão.
- Se a prova permitir folhas de rascunho (**computação em tempo de teste**), o estudante resolve a mesma conta de três maneiras diferentes no rascunho. Ele compara os resultados, detecta que cometeu um erro de sinal na primeira tentativa e passa para a folha definitiva apenas a solução confirmada.

## ⚙️ Como funciona

O pipeline desdobra-se em geração de candidatos e seleção crítica:

### Etapas

1. **Variação de sementes:** O sistema recebe a solicitação do usuário e dispara $N$ requisições paralelas (ou sequenciais) com temperatura moderada para diversificar as abordagens.
2. **Geração dos rascunhos:** O modelo produz $N$ trajetórias completas de resposta.
3. **Mecanismo de seleção:** A melhor opção é selecionada através de uma destas táticas:
   - **Logprob Médio Mais Alto:** Escolhe o candidato cuja média geométrica das probabilidades dos tokens foi mais alta.
   - **Autoconsistência (*Self-Consistency*):** Comum em matemática e código: se 7 de 10 rascunhos chegaram ao número `42`, a resposta `42` é escolhida por voto majoritário.
   - **Modelo Verificador (*Verifier*):** Um modelo neural especializado treinado para validar se a resposta está correta pontua cada rascunho e seleciona o vencedor.
   - **Heurísticas determinísticas:** Em SQL ou código, executa-se o código em um ambiente isolado (*sandbox*) e escolhe-se o primeiro rascunho que compilar sem erros.

### Entradas e saídas

- **Entradas:** Prompt complexo e uma cota de computação alocada (número de rascunhos $N$).
- **Saídas:** A resposta final mais robusta e factualmente validada dentre os candidatos gerados.

## 📐 Formulação matemática

Seja $\mathcal{Y} = \{y^{(1)}, y^{(2)}, \dots, y^{(N)}\}$ o conjunto de $N$ respostas candidatas amostradas independentemente de $\pi_\theta(y \mid x)$. 
Sob um modelo verificador $V(x, y) \in \mathbb{R}$, a seleção **Best-of-N** é formulada como:

$$y^* = \arg\max_{y \in \mathcal{Y}} V(x, y)$$

Na abordagem por autoconsistência para problemas com resposta final discreta $A(y)$:

$$a^* = \arg\max_{a} \sum_{i=1}^N \mathbb{I}\Big(A(y^{(i)}) = a\Big)$$

O experimento da OpenAI (Cobbe et al., 2021) demonstrou que aplicar um verificador sobre múltiplos rascunhos em tarefas matemáticas gerou um ganho de acurácia equivalente a aumentar o tamanho físico do modelo em $30\times$.

## 🧱 Hipóteses e condições de validade

- As trajetórias candidatas devem possuir diversidade suficiente; se a temperatura for zero, todas as $N$ saídas serão idênticas e a técnica não gerará ganhos.
- O custo financeiro e a latência de gerar $N$ respostas devem ser compatíveis com as restrições da aplicação.

## ✅ Quando usar

- Tarefas com gabarito formal ou verificabilidade clara: matemática, geração de consultas SQL, programação e raciocínio lógico.
- Aplicações assíncronas ou batch onde a latência de vários segundos ou minutos não incomoda o usuário (ex.: relatórios financeiros profundos).

## 🚫 Quando não usar

- Em chatbots conversacionais ultrarrápidos de atendimento ao cliente com restrições rígidas de latência sub-segundo e orçamentos minúsculos por chamada.

## ⚠️ Limitações e armadilhas

- **Multiplicação linear de custos:** Gerar 5 rascunhos multiplica o consumo de tokens e a fatura da API por 5.
- **Enganação do Verificador (*Adversarial outputs*):** O estudo da OpenAI mostrou que gerar amostras em excesso (acima de 400 candidatos) pode degradar a performance, pois aumenta a probabilidade estatística de surgir um rascunho absurdo com características superficiais que enganam o modelo verificador.

## 🔍 Comparações

| Estratégia de Ganho | Como atua? | Momento do Gasto | Custo por Usuário |
|---|---|---|---|
| **Escala de Parâmetros** | Treinar um modelo 30x maior | Único (no pré-treino) | Altíssimo em toda requisição |
| **Computação em Tempo de Teste** | Gerar $N$ opções e filtrar com verificador | Dinâmico (na inferência) | Sob demanda (gasta apenas em tarefas difíceis) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um assistente de banco de dados recebe a ordem: `"Escreva uma query PostgreSQL complexa para calcular o churn mensal dos últimos 5 anos"`.
O sistema utiliza um modelo de 8B parâmetros com temperatura $0{,}7$ e gera 4 rascunhos de SQL.
- O rascunho 1 esquece de tratar divisão por zero.
- O rascunho 2 usa uma função inexistente no PostgreSQL.
- O rascunho 3 executa perfeitamente na sandbox e retorna os dados esperados.
- O rascunho 4 entra em loop de execução lenta.
O sistema descarta as opções 1, 2 e 4 e entrega a opção 3 ao usuário. O usuário teve a impressão de que o modelo de 8B é tão inteligente quanto um modelo de 70B.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]

### Complementos

- [[redes/ai-engineering/conceitos/amostragem-top-k-e-top-p.md|Amostragem Top-k e Top-p]]
- [[redes/ai-engineering/conceitos/aprendizado-por-reforco-com-feedback-humano.md|Aprendizado por Reforço com Feedback Humano (RLHF)]] (modelos de recompensa utilizados como verificadores)

### Alternativas

- Uso de modelos massivos de parâmetros densos em inferência de passagem única (*single-pass greedy*).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 96–99
- **Evidência:** O texto analisa o conceito de test time compute, destacando o trabalho de Cobbe et al. (2021) da OpenAI sobre verificadores matemáticos, a pesquisa da DeepMind (Snell et al., 2024) sobre a equivalência entre escalar computação na inferência versus parâmetros de modelo, e o uso de autoconsistência por votação.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Computação em Tempo de Teste (*Test Time Compute*) e como ela desafia a necessidade de aumentar o tamanho físico dos modelos?
2. Como funciona a estratégia de seleção Best-of-N com modelos verificadores (*verifiers*)?
3. O que é a técnica de autoconsistência (*self-consistency*) e em quais domínios ela é aplicável com facilidade?
4. Qual foi o impacto métrico documentado pela OpenAI ao aplicar verificadores em problemas matemáticos em comparação com a escala de parâmetros?
5. Quais são os principais custos e penalidades operacionais associados ao uso de múltiplos rascunhos de inferência?
6. Por que amostrar candidatos em excesso (ex.: centenas ou milhares de opções) pode levar à degradação da resposta final?
7. Como a Computação em Tempo de Teste pode ser integrada a pipelines de geração de código para contornar falhas de compilação?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
