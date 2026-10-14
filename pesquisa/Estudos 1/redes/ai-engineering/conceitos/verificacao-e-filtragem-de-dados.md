# 🧠 Verificação e Filtragem de Dados

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 391–393, 401

## 📝 Definição

### Definição formal

A **Verificação e Filtragem de Dados** (*Data Verification and Filtering*) é o estágio do pipeline de engenharia de conjuntos de dados no qual amostras brutas ou geradas sinteticamente são submetidas a baterias de testes determinísticos, analíticos e semânticos para identificar, podar e descartar registros corrompidos, errôneos, factualmente incoerentes ou de baixo valor informativo antes de sua incorporação aos dados de treino de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]]. 

A verificação opera sobre três modalidades fundamentais de auditoria:

1. **Verificação Funcional Determinística:** Execução real de amostras de código e consultas estruturadas em interpretadores e suítes de testes unitários isoladas ([[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional]]);
2. **Verificadores Baseados em IA (*AI Verifiers*):** Modelos especializados ou classificadores treinados para auditar consistência factual e atribuir pontuações de utilidade;
3. **Filtragem Heurística e Poda (*Data Pruning*):** Regras determinísticas de superfície (limites de caracteres, padrões de regex, balanceamento de classes e métricas de complexidade informacional).

### Em linguagem simples

É a "fiscalização sanitária" dos dados de treino. Não basta coletar textos ou mandar a IA inventar milhares de perguntas; é preciso conferir se o que foi gerado está certo antes de deixar o modelo estudar por aquele material. Códigos de programação passam por compiladores reais para ver se rodam; textos passam por IAs examinadoras e filtros que cortam frases muito curtas, repetitivas ou que contenham erros óbvios.

### Escopo e distinções

Diferencia-se da avaliação final do modelo. Aqui, o objeto de teste **não é o modelo treinado, mas o dado de treino em si**. Conecta-se à disciplina de poda de dados (*data pruning*), que busca selecionar o menor subconjunto representativo que maximiza o aprendizado da rede.

## 🧩 Problema que resolve

Resolve a contaminação do modelo por dados sintéticos alucinados ou textos da web corrompidos. Treinar um modelo com dados sintéticos sem verificação funciona como um amplificador de erros: o modelo base assimila alucinações como fatos reais e aprende padrões de código quebrados, tornando o ajuste fino inútil ou destrutivo.

## 💡 Intuição

Pense em uma fábrica de alimentos que produz barras de cereais:

- Os ingredientes chegam do caminhão do fornecedor (**dados brutos ou sintéticos**).
- Antes de misturar os cereais na masseira, o lote passa por uma esteira com detectores de metal (**filtros determinísticos**), sensores ópticos que ejetam grãos estragados (**verificadores de IA**) e análises químicas de laboratório (**testes funcionais**). Apenas os ingredientes aprovados entram na receita final.

## ⚙️ Como funciona

O processo opera através de filtros sequenciais em cascata de complexidade crescente:

### Etapas

1. **Filtros Heurísticos de Superfície:**
   - Descarta amostras vazias, com tamanho inferior a um limiar (ex.: menos de 5 palavras) ou extensas demais para o contexto;
   - Remove amostras onde a resposta gerada é apenas a repetição literal da pergunta;
   - Descarta textos com densidade anormal de símbolos de formatação ou caracteres quebrados.
2. **Verificação Funcional em Ambiente Seguro (Sandbox):**
   - Para amostras de programação: o código passa por linters estáticos (como Flake8) e é executado contra testes unitários; amostras que levantam exceções são ejetadas ou enviadas para auto-correção.
3. **Auditoria por Verificadores de IA:**
   - Um modelo neural avalia a [[redes/ai-engineering/conceitos/consistencia-factual.md|consistência factual]] do par `(contexto, resposta)`;
   - Classificadores de tópicos confirmam se a amostra pertence ao domínio de interesse do produto.
4. **Poda de Dados Baseada em Dificuldade (*Data Pruning*):**
   - Calcula-se o valor informativo de cada exemplo; amostras triviais que o modelo já domina com perda zero são descartadas para liberar capacidade de treinamento para exemplos mais difíceis.

### Entradas e saídas

- **Entradas:** Dataset bruto consolidado ou fluxo de dados sintéticos recém-gerados.
- **Saídas:** Conjunto de dados purificado, com taxa de erros reduzida e alta densidade informativa.

## 📐 Formulação matemática

A poda de dados (*Data Pruning*, Sorscher et al., Meta, 2022) seleciona um subconjunto $\mathcal{S}^* \subset \mathcal{D}$ com tamanho $|\mathcal{S}^*| = K < |\mathcal{D}|$ que minimiza o erro de generalização através de uma métrica de pontuação informacional $s(x)$:

$$\mathcal{S}^* = \arg\max_{\mathcal{S} \subset \mathcal{D}, |\mathcal{S}| = K} \sum_{x \in \mathcal{S}} s(x)$$

Onde a pontuação $s(x)$ pode derivar da margem de erro, da perplexidade sob o modelo base ou da distância no espaço de embeddings. Os autores comprovaram que a poda inteligente de dados permite quebrar a lei de potência clássica de escalonamento (*power law scaling*), atingindo o mesmo nível de acurácia com uma ordem de grandeza a menos de dados de treino.

## 🧱 Hipóteses e condições de validade

- Para verificação de código, deve existir um interpretador e uma suíte de asserções executáveis e idempotentes.
- Para filtros de IA, o modelo verificador deve possuir acurácia significativamente maior do que o modelo que sintetizou a amostra original para não aprovar alucinações sutis.

## ✅ Quando usar

- Mandatório na curadoria de qualquer conjunto de dados sintéticos produzidos por LLMs para evitar o [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|colapso do modelo]].
- Na preparação de dados raspados da internet para remoção de lixo textual antes de procedimentos de finetuning corporativo.

## 🚫 Quando não usar

- Não aplique podas agressivas sobre categorias de dados que representam eventos raros de cauda longa que o modelo precisa obrigatoriamente aprender a responder em produção.

## ⚠️ Limitações e armadilhas

- **Filtros heurísticos excessivamente restritivos:** Configurar regras rígidas de palavras proibidas que acabam descartando perguntas médicas ou legais perfeitamente legítimas contendo palavras sensíveis.
- **Custo computacional de verificadores neurais:** Usar modelos pesados de IA para auditar individualmente 10 milhões de amostras pode gerar custos de computação que superam o orçamento do próprio treinamento final.

## 🔍 Comparações

| Método de Verificação | Custo de Execução | Taxa de Falso Positivo | Aplicabilidade |
|---|---|---|---|
| **Heurísticas e Regex** | Quase zero (CPU) | Alta (regras rígidas demais) | Estrutura de texto e comprimento |
| **Execução Funcional (Sandbox)** | Baixo (tempo de CPU) | **Zero (o código roda ou não roda)**| Código, SQL e Matemática |
| **Verificadores por IA** | Moderado a Alto (GPUs) | Baixa a Média (depende do juiz) | Factualidade e estilo de prosa |
| **Poda Baseada em Perda (*Pruning*)**| Médio | Baixa | Otimização de volume de treino |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O time de engenharia da Meta sintetiza 3 milhões de problemas de programação para treinar o Llama 3.

- As funções são geradas por um LLM. Em vez de salvar os arquivos diretamente no banco de treino, cada função é despachada para um ambiente isolado (*sandbox*).
- O sistema roda um **linter estático** e detecta que $15\%$ das funções esqueceram de importar módulos como `math` ou `sys`.
- As funções que passam no linter são executadas contra 5 **testes unitários** automatizados. Cerca de $20\%$ falham na execução de casos com números negativos.
- Apenas as funções que compilam e passam em $100\%$ dos testes unitários são aprovadas para o dataset final. A base resultante é pura, imune a erros de compilação e pronta para ensinar o modelo a programar com rigor.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/qualidade-e-conformidade-de-dados.md|Qualidade e Conformidade de Dados]]

### Complementos

- [[redes/ai-engineering/conceitos/correcao-funcional.md|Correção Funcional (pass@k)]]
- [[redes/ai-engineering/conceitos/sintese-de-instrucoes-e-self-instruct.md|Síntese de Instruções e Self-Instruct]]

### Alternativas

- Treinamento cego sobre dados brutos sem etapas de auditoria intermediária.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|Colapso do Modelo e Riscos de Dados Sintéticos]]
- [[redes/ai-engineering/conceitos/inspecao-e-deduplicacao-de-dados.md|Inspeção e Deduplicação de Dados]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 391–393, 401
- **Evidência:** Chip Huyen discute a verificação de dados através de corretude funcional e verificadores por IA, apresenta as heurísticas clássicas de descarte do Self-Instruct (Wang et al., 2022) e analisa as métricas de poda de dados (data pruning) comprovadas por Sorscher et al. (Meta, 2022) para acelerar o aprendizado em ordens de magnitude.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a função da etapa de Verificação e Filtragem de Dados dentro da engenharia de conjuntos de dados?
2. Por que a verificação funcional por execução em interpretadores é a abordagem de maior autoridade para dados de programação?
3. Quais são as heurísticas clássicas de filtragem de superfície utilizadas no artigo seminal do Self-Instruct?
4. O que é a técnica de Poda de Dados (*Data Pruning*) e como o estudo da Meta (Sorscher et al., 2022) comprovou que ela pode quebrar leis de escala tradicionais?
5. Como os verificadores baseados em IA atuam na identificação de alucinações em amostras textuais sintéticas?
6. Qual é o perigo de se adotar filtros de regex e heurísticas excessivamente rígidas na preparação de datasets corporativos?
7. Por que dados sintéticos que contêm auto-correções baseadas em feedback de execução são especialmente valiosos para o treinamento de modelos de raciocínio?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
