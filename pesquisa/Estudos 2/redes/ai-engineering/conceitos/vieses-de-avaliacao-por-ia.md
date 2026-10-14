# 🧠 Vieses de Avaliação por IA

**Rede:** `ai-engineering`   **Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 144–145

## 📝 Definição

### Definição formal

Os **Vieses de Avaliação por IA** (*Biases of AI as a Judge*) são distorções estatísticas, estruturais e comportamentais sistemáticas e reprodutíveis manifestadas por modelos de fundação quando empregados na função de julgamento avaliativo, levando à atribuição de pontuações que não refletem a qualidade factual ou intrínseca das saídas avaliadas. 

Os três vieses canônicos documentados na literatura técnica são:

1. **Viés de Auto-preferência (*Self-bias*):** A tendência estatística de um modelo favorecer sistematicamente saídas geradas por ele mesmo ou por modelos da mesma família de arquitetura e alinhamento;
2. **Viés de Posição (*Position bias*):** A assimetria de julgamento induzida pela ordem em que os candidatos são apresentados no prompt, com forte favorecimento para a primeira opção apresentada (*first-position bias*);
3. **Viés de Verbosidade (*Verbosity bias*):** A forte propensão de juízes neurais atribuírem notas superiores a respostas extensas, detalhadas e prolixas, mesmo quando contêm erros factuais ou quando uma resposta concisa seria superior.

### Em linguagem simples

São os "pontos cegos" e preconceitos matemáticos que uma IA examinadora tem na hora de dar notas. Uma IA julgando tende a achar que os próprios textos dela são os melhores do mundo, tende a votar no primeiro candidato que aparece na folha de teste e quase sempre dá nota mais alta para quem escreveu uma redação enorme e enrolada, mesmo que uma resposta curta de duas linhas estivesse muito mais certa.

### Escopo e distinções

Não se confundem com preconceitos sociais ou discriminação de gênero e raça nos dados de treinamento (embora também possam ocorrer). Trata-se de vieses algorítmicos ligados à mecânica da atenção e à distribuição estatística de preferências aprendidas no pós-treinamento.

## 🧩 Problema que resolve

Mapear esses vieses resolve a armadilha de aceitar pontuações de juízes de IA como verdades incontestáveis. Saber que esses vieses existem permite aplicar contramedidas de engenharia (como inverter a ordem dos candidatos, penalizar a extensão do texto ou calibrar notas cruzadas) para purificar os dados de avaliação.

## 💡 Intuição

Pense em um concurso de oratória com um jurado humano cansado:

- Se um orador fala por 20 minutos usando palavras difíceis e postura imponente, o jurado assume que ele é muito inteligente, mesmo que o discurso não tenha chegado a conclusão nenhuma (**viés de verbosidade**).
- Se o jurado assiste a 10 apresentações seguidas, ele presta atenção no primeiro concorrente da manhã e já está exausto no último (**viés de posição**).
- E se um dos concorrentes for aluno formado na mesma faculdade que o jurado estudou, o jurado sentirá uma simpatia inconsciente pelo seu estilo de fala (**viés de auto-preferência**).

## ⚙️ Como funciona

Cada viés possui um mecanismo subjacente específico:

### Etapas

1. **Operação do Viés de Auto-preferência:** A rede neural do juiz foi treinada com a mesma distribuição probabilística de seus próprios pesos. Quando ele lê um texto gerado por ele mesmo, as palavras seguintes são aquelas com as maiores probabilidades em sua própria matriz de atenção, gerando alta familiaridade intrínseca e resultando em notas infladas (estudos mostram que o GPT-4 se favorece com $+10\%$ de vitórias e o Claude-v1 com $+25\%$).
2. **Operação do Viés de Posição:** A atenção do Transformer tende a dedicar mais peso aos primeiros tokens estruturados que aparecem no contexto. Em disputas par a par (A vs. B), a opção apresentada como "Opção A" ganha estatisticamente mais disputas do que quando colocada como "Opção B".
3. **Operação do Viés de Verbosidade:** O juiz confunde extensão com completeza de raciocínio. Estudos (Wu e Aji, 2023) comprovaram que juízes de ponta preferem respostas de 100 palavras com erros factuais graves a respostas perfeitas de 50 palavras sem erros.
4. **Contramedidas de Engenharia:**
   - Para anular o viés de posição: executa-se cada avaliação duas vezes, invertendo as ordens (A vs B e depois B vs A), aceitando o resultado apenas em caso de coerência mútua;
   - Para o viés de verbosidade: impõe-se limites estritos de caracteres ou instruções que penalizam prolixidade.

### Entradas e saídas

- **Entradas:** Par de respostas avaliadas por um juiz neural.
- **Saídas:** Escore potencialmente distorcido que exige algoritmos de desenviesamento (*debiasing*).

## 📐 Formulação matemática

O viés de posição entre os modelos $M_1$ e $M_2$ é formalizado pela assimetria na taxa empírica de vitória $P(\text{vitória})$ em função da posição de apresentação $\pi \in \{\text{Posição 1}, \text{Posição 2}\}$:

$$P\Big(M_1 \succ M_2 \mid \pi(M_1) = 1\Big) \neq 1 - P\Big(M_2 \succ M_1 \mid \pi(M_2) = 1\Big)$$

O desenviesamento por permutação calcula a preferência agregada balanceando as duas probabilidades condicionais de ordem:

$$P_{\text{balanceado}}(M_1 \succ M_2) = \frac{1}{2} \left[ P(M_1 \succ M_2 \mid M_1 \text{ em 1}) + P(M_1 \succ M_2 \mid M_1 \text{ em 2}) \right]$$

## 🧱 Hipóteses e condições de validade

- A inversão de posições só funciona como neutralizadora do viés se o juiz não cair em impasses repetidos (*draws* induzidos pela contradição de ordem).

## ✅ Quando usar

- Auditoria obrigatória de qualquer benchmark ou pipeline de CI/CD que utilize [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como juiz]].
- Concepção de diretrizes de alinhamento e curadoria de dados sintéticos de preferência para evitar colapso de extensão em modelos novos.

## 🚫 Quando não usar

- Em avaliações exatas determinísticas ([[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional]]), pois o interpretador de código não sofre de vieses estilísticos nem favorece códigos mais longos.

## ⚠️ Limitações e armadilhas

- **A inflação da prolixidade corporativa:** Modelos treinados com dados de preferência gerados por juízes de IA tornam-se progressivamente mais prolixos e cansativos a cada geração se o viés de verbosidade não for neutralizado na raiz.
- **Custo dobrado:** A técnica padrão de desenviesamento de posição exige rodar a avaliação duas vezes com ordem invertida, duplicando a fatura de tokens da IA juiz.

## 🔍 Comparações

| Viés do Juiz | Como se manifesta? | Contramedida de Engenharia | Custo da Correção |
|---|---|---|---|
| **Auto-preferência** | Dá notas mais altas para si mesmo | Usar juízes de fornecedores concorrentes ou modelos neutros | Baixo |
| **Primeira Posição** | Prefere a primeira opção apresentada no prompt | Avaliação simétrica permutada (executar A/B e B/A) | Dobra o custo de inferência |
| **Verbosidade** | Prefere respostas longas e enroladas a curtas e exatas | Normalização de tamanho e penalidade explícita na rubrica | Mínimo |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma equipe quer comparar se o Modelo X é melhor que o Modelo Y para resumir laudos médicos.
O comando é: `"Qual é o órgão afetado?"`.

- O Modelo X responde em 4 palavras: `"O rim esquerdo (nefrite)"`. (100% correto).
- O Modelo Y responde em 120 palavras: `"Ao analisar detidamente o prontuário sob a ótica da nefrologia moderna, observa-se que o paciente apresenta uma condição inflamatória no fígado, que é um órgão vital..."` (Errou feio o órgão, mas usou termos bonitos e texto longo).

O **Juiz de IA descalibrado** lê as duas opções. Influenciado pelo **viés de verbosidade**, ele atribui a vitória ao Modelo Y, afirmando que Y foi "mais detalhado, completo e atencioso", ignorando que Y errou a informação clínica básica.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/avaliacao-comparativa.md|Avaliação Comparativa (Pairwise)]]
- [[redes/ai-engineering/conceitos/modelos-de-preferencia-e-juizes-especializados.md|Modelos de Preferência e Juízes Especializados]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (trata-se de limitações intrínsecas a serem mitigadas).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 144–145
- **Evidência:** O texto descreve em detalhe os vieses de self-bias (GPT-4 favorecendo-se em 10% e Claude-v1 em 25% no MT-Bench), first-position bias (oposto ao recency bias dos humanos) e verbosity bias (pesquisas de Wu e Aji comprovando que juízes preferem respostas de 100 palavras erradas a respostas de 50 palavras certas).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são os três vieses canônicos manifestados por modelos de fundação quando atuam como juízes de avaliação?
2. Como funciona o viés de auto-preferência (*self-bias*) e qual é a sua magnitude empírica documentada no GPT-4 e no Claude?
3. Por que o viés de posição dos LLMs (que favorece a primeira opção) é o oposto exato do viés de recência típico dos seres humanos?
4. Como o viés de verbosidade pode induzir uma equipe a lançar um modelo que comete mais erros factuais do que o modelo anterior?
5. Qual técnica matemática e algorítmica de engenharia é recomendada para neutralizar o viés de primeira posição em testes comparativos?
6. Qual é o impacto financeiro da aplicação de rotinas de desenviesamento por permutação sobre a fatura de tokens da aplicação?
7. Por que modelos de fundação mais modernos e maiores tendem empiricamente a sofrer menos do viés de verbosidade do que modelos mais antigos (como o GPT-3.5)?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
