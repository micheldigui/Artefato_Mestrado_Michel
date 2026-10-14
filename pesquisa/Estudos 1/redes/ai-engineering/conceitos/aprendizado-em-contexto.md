# 🧠 Aprendizado em Contexto (In-Context Learning)

**Rede:** `ai-engineering`  
**Área:** `engenharia-de-prompt`

**Rede:** `ai-engineering`   **Área:** `desenvolvimento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 5 — Engenharia de Prompt
- Localização: localização não informada no material recebido

- AI Engineering: Building Applications with Foundation Models — Capítulo 5 — Prompt Engineering
- Localização: Páginas 213–215

## 📝 Definição

### Definição formal

A capacidade emergente de grandes modelos de linguagem de inferir e executar novas tarefas complexas em tempo de inferência, utilizando unicamente os exemplos e instruções fornecidos no prompt de entrada, sem alteração dos pesos da rede neural.

O **Aprendizado em Contexto** (*In-Context Learning* — ICL) é a propriedade comportamental emergente de [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]] em que o sistema infere o mapeamento funcional de uma tarefa arbitrária, seu formato de saída e suas restrições operacionais a partir de descrições e demonstrações exemplares (*shots*) fornecidas exclusivamente dentro da sequência de entrada (*prompt*), condicionando a distribuição de probabilidades de geração sem executar retropropagação (*backpropagation*) e sem atualizar nenhum parâmetro de peso da rede neural.

### Em linguagem simples

É a habilidade da IA de aprender a fazer uma tarefa na hora, apenas lendo as orientações e exemplos que você colocou no texto antes de fazer a pergunta, sem precisar passar por um novo treinamento computacional.

É a habilidade da IA de "aprender na hora", apenas lendo o que você colocou na mensagem. Em vez de precisar passar por um treinamento demorado que mude a fiação interna do cérebro do modelo, basta você mostrar a ele dois ou três exemplos de como fazer o trabalho (como pares de pergunta e resposta) para que ele entenda o padrão e continue fazendo o mesmo para a próxima pergunta.

### Escopo e distinções

Diferencia-se do ajuste fino (*finetuning*): no aprendizado em contexto, o aprendizado é temporário e volátil (restringindo-se à janela de contexto da requisição atual), enquanto no finetuning os parâmetros da rede são modificados permanentemente.

Distingue-se do aprendizado tradicional de máquina e do [[redes/ai-engineering/conceitos/ajuste-fino.md|ajuste fino]], onde os pesos matemáticos $\theta$ são permanentemente alterados. No ICL, a parametrização do modelo permanece estática; a mudança ocorre estritamente no estado de ativação temporário provocado pelo contexto de entrada. Varia de **Zero-Shot** (nenhum exemplo demonstrativo fornecido) a **Few-Shot** (múltiplos pares de demonstração).

## 🧩 Problema que resolve

Resolve a necessidade de realizar modificações estruturais custosas ou retreinamentos de modelos toda vez que uma nova variação de tarefa precisa ser executada por um sistema de IA.

Resolve a rigidez temporal e o custo de adaptação dos modelos clássicos. Se um software ou uma lei muda de versão hoje, atualizar um modelo tradicional exigiria coletar dados, re-treinar a rede e homologar novos pesos. Com o aprendizado em contexto, basta injetar as alterações recentes e exemplos atualizados na janela de entrada para que o modelo processe a nova realidade instantaneamente, atuando como um mecanismo prático de aprendizado contínuo.

## 💡 Intuição

Pense em um especialista em culinária que nunca fez um prato boliviano específico: se você entregar a ele uma receita detalhada com três exemplos de preparo (contexto), ele conseguirá executar o prato perfeitamente na hora, sem precisar fazer uma faculdade nova de gastronomia.

Conforme a metáfora proposta por François Chollet (criador do Keras) citada no texto: um grande modelo de fundação não é uma função estática única, mas uma gigantesca **biblioteca de programas computacionais latentes**. Ele contém internamente um programa para escrever poemas, outro para traduzir textos médicos e outro para formatar dados em tabelas. O ICL é o mecanismo que utiliza os exemplos do prompt como uma "chave de ignição" para ativar o programa correto dentro dessa vasta biblioteca.

## ⚙️ Como funciona

O mecanismo baseia-se na capacidade da atenção de capturar correlações entre sequências adjacentes:

### Etapas

1. O desenvolvedor ou usuário monta um prompt contendo a descrição da tarefa, regras e, opcionalmente, exemplos demonstrativos (*few-shot*).
2. O prompt é tokenizado e injetado na janela de contexto do modelo de fundação.
3. O modelo processa a totalidade do contexto em paralelo durante a fase de *Prefill*.
4. A rede neural ativa os padrões latentes correspondentes na inferência e gera a resposta alinhada aos exemplos do prompt.

1. **Estruturação do Prompt:** O engenheiro redige uma instrução acompanhada de $K$ pares de demonstração representativos da tarefa:

$$(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), \dots, (x^{(K)}, y^{(K)})$$

2. **Inclusão da Consulta Alvo:** Adiciona-se a nova entrada $x_{\text{novo}}$ sem o gabarito.
3. **Processamento da Atenção:** As matrizes de atenção do Transformer calculam as relações cruzadas entre as demonstrações anteriores e a consulta alvo.
4. **Indução do Padrão:** A rede neural identifica o padrão de transformação latente (ex.: sintaxe, tom de voz, brevidade) exemplificado nos pares.
5. **Geração Condicionada:** O modelo emite $y_{\text{novo}}$ reproduzindo a mesma lógica formal inferida das demonstrações.

### Entradas e saídas

- Entradas: Prompt estruturado contendo contexto, instruções e exemplos demonstrativos.
- Saídas: Resposta gerada que demonstra a assimilação da tarefa descrita.

- **Entradas:** Contexto com exemplos estruturados e a nova entrada a ser processada.
- **Saídas:** Resposta gerada que preserva a coerência estilística e lógica apresentada nas demonstrações.

## 📐 Formulação matemática

Representado empiricamente pela probabilidade condicional gerativa do modelo $M$ parametrizado por pesos congelados $\Theta$:

$$P(y \mid x, C_k)$$

Onde:
- $x$: Entrada ou consulta alvo.
- $C_k$: Contexto contendo $k$ exemplos de demonstração (*few-shot prompts*).
- $y$: Resposta gerada alinhada ao contexto.

Em termos de modelagem probabilística, o ICL condiciona a previsão da sequência de saída $Y$ tanto à nova entrada $X$ quanto ao conjunto de suporte de exemplos $\mathcal{S}_{\text{exemplos}} = \{(x^{(k)}, y^{(k)})\}_{k=1}^K$:

$$P\Big(Y \mid X, \mathcal{S}_{\text{exemplos}}; \theta^*\Big) = \prod_{t=1}^T P\Big(y_t \mid y_{<t}, X, \mathcal{S}_{\text{exemplos}}; \theta^*\Big)$$

Onde os pesos $\theta^*$ permanecem rigorosamente congelados. A eficiência da amostra (*sample efficiency*) no ICL é tal que a acurácia frequentemente se eleva de forma expressiva ao transitar de $K=0$ para $K \in [3, 5]$, com retornos decrescentes conforme $K$ cresce além do limite de atenção útil.

## 🧱 Hipóteses e condições de validade

- Requer que a janela de contexto do modelo seja suficientemente ampla para acomodar as instruções e os exemplos explicativos sem truncamento de dados.

- O modelo de fundação base deve possuir capacidade de raciocínio contextual e escala suficientes para inferir regras a partir de demonstrações (propriedade que se consolidou historicamente a partir do GPT-3 de 175B).
- A totalidade dos exemplos de demonstração e a nova consulta devem caber com folga dentro do limite da janela de contexto suportada pelo modelo.

## ✅ Quando usar

- Na prototipagem rápida, tarefas flexíveis de uso geral, manipulação de dados textuais variáveis e implantações onde não há infraestrutura para realizar ajuste fino (*finetuning*).

- Primeira estratégia de validação técnica de qualquer nova tarefa na camada de aplicação da [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]].
- Tarefas onde os formatos de resposta são específicos ou proprietários e não constam com clareza nos dados de treino público.
- Casos onde se dispõe de apenas 3 a 10 exemplos perfeitos de demonstração.

## 🚫 Quando não usar

- Em cenários que exigem consistência ultra-rígida a nível de parâmetros, otimização extrema de latência de entrada (prompts longos custam mais) ou restrições severas de espaço de contexto.

- Em aplicações de escala industrial massiva onde o custo financeiro e a latência de enviar repetidamente dezenas de exemplos em cada uma de milhões de chamadas tornam o sistema proibitivo em comparação a um modelo ajustado via [[redes/ai-engineering/conceitos/ajuste-fino.md|finetuning]].

## ⚠️ Limitações e armadilhas

- Sensibilidade à ordem dos exemplos (*order bias*): a posição e a sequência dos exemplos no prompt podem alterar drasticamente a qualidade da resposta do modelo.
- Limite estrito imposto pelo tamanho máximo da janela de contexto do modelo.

- **Consumo de janela de contexto:** Incluir muitos exemplos longos reduz o espaço disponível para a consulta real do usuário e para a injeção de documentos de RAG.
- **Sensibilidade à ordem e formatação:** Estudos comprovam que a ordem em que os exemplos são apresentados no prompt pode alterar drasticamente a acurácia final do modelo.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[aprendizado-em-contexto|Aprendizado em Contexto]] | Ensinar tarefas em tempo de inferência via texto. | Prompt estruturado com instruções/exemplos. | Resposta gerada adaptada. | Volátil, temporário, sem alteração de pesos. |
| [[finetuning|Finetuning]] | Especializar o modelo permanentemente via treino. | Dataset estruturado de treino + Pesos base. | Novo conjunto de pesos de modelo. | Permanente, altera a estrutura matemática interna da rede. |

| Dimensão | Aprendizado em Contexto (Few-Shot) | Ajuste Fino (*Finetuning*) |
|---|---|---|
| **Alteração de pesos ($\theta$)** | Nula ($\theta$ congelado) | Permanente (gradiente descendente) |
| **Volume de dados** | 1 a 20 exemplos | Centenas a milhares de exemplos |
| **Latência por chamada** | Maior (mais tokens de entrada para ler) | Menor (o modelo já internalizou o padrão) |
| **Custo por requisição** | Mais caro em faturas de API | Mais barato em tokens de entrada |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Enviar ao GPT-4 uma lista com três nomes de empresas seguidos de suas respectivas siglas e, logo abaixo, pedir a sigla de uma quarta empresa, fazendo com que o modelo acerte o padrão sem ter passado por nenhum treinamento prévio específico para aquilo.

Uma equipe precisa classificar se postagens curtas contêm ironia ou sarcasmo.

- *Abordagem Zero-Shot:* Prompt: `"Diga se a frase é sarcástica: 'Adoro quando o ônibus quebra na chuva.'"`. O modelo hesita e gera uma explicação longa e indecisa.
- *Abordagem Few-Shot (ICL):*

Prompt: `"Classifique o sentimento em SARCÁSTICO ou LITERAL.` `Texto: 'O dia está ensolarado e agradável.' -> LITERAL` `Texto: 'Que maravilha, derrubei café no teclado novo!' -> SARCÁSTICO` `Texto: 'Adoro quando o ônibus quebra na chuva.' ->"` Ao ler as demonstrações, a atenção do modelo ativa imediatamente o padrão sintático e emite sem preâmbulos: `"SARCÁSTICO"`.

## 🔗 Relações no grafo

### Pré-requisitos

- [[modelo-de-fundacao|Modelo de Fundação]]

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]
- [[redes/ai-engineering/conceitos/templates-de-chat-e-prompts-de-sistema.md|Templates de Chat e Prompts de Sistema]]

### Alternativas

- [[finetuning|Finetuning]]

- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

- [[redes/ai-engineering/conceitos/decomposicao-e-encadeamento-de-prompts.md|Decomposição e Encadeamento de Prompts]]
- [[redes/ai-engineering/conceitos/cadeia-de-pensamento.md|Cadeia de Pensamento (Chain-of-Thought - CoT)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 5 — Engenharia de Prompt
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação conceitual do aprendizado em contexto (*in-context learning*) e sua equivalência funcional como substituto dinâmico para o retreinamento estrutural.
- **Confiança:** alta

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 5 — Prompt Engineering
- **Localização:** Páginas 213–215
- **Evidência:** Chip Huyen aborda a consagração do termo in-context learning a partir do artigo clássico do GPT-3 de Brown et al. (2020), explica a analogia de François Chollet sobre ativação de programas latentes e analisa a transição de eficiência entre regimes zero-shot e few-shot em modelos de diferentes escalas.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Aprendizado em Contexto (In-Context Learning)?
2. Que problema ele resolve?
3. Como ele funciona passo a passo?
4. Quais hipóteses precisam ser verdadeiras?
5. Quando ele deve ou não deve ser utilizado?
6. Com qual conceito ele pode ser confundido?
7. Como eu verificaria seu funcionamento em um caso novo?

1. O que é o Aprendizado em Contexto (*In-Context Learning*) e em que ele difere formalmente do aprendizado supervisionado tradicional?
2. Como a metáfora de François Chollet descreve o papel dos exemplos de demonstração na ativação de "programas latentes" dentro do LLM?
3. De que maneira o ICL atua como um mecanismo prático de aprendizado contínuo para evitar que modelos fiquem obsoletos?
4. Qual é a distinção operacional entre uma abordagem de prompt *Zero-Shot* e uma abordagem *Few-Shot*?
5. Quais são as penalidades financeiras e de latência decorrentes do uso excessivo de exemplos extensos dentro do prompt?
6. Por que modelos de escala mais avançada (como o GPT-4) apresentam menor dependência de grandes conjuntos de *shots* do que modelos mais antigos (como o GPT-3)?
7. Como a ordenação física dos exemplos demonstrativos no texto pode induzir vieses no resultado final da inferência?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

---
*Nota gerada a partir do capítulo Capítulo 5 — Engenharia de Prompt. A interpretação final deve ser revisada pelo estudante.*
