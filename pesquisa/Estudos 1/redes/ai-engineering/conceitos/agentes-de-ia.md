# 🧠 Agentes de IA (AI Agents)

**Rede:** `ai-engineering`  
**Área:** `sistemas-autonomos`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG e Agentes
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

Um sistema autônomo estruturado sobre um modelo de fundação que percebe seu ambiente, decompõe objetivos complexos em planos sequenciais de ação, invoca ferramentas (*tools*) externas e executa loops de reflexão e correção para concluir tarefas multifacetadas.

### Em linguagem simples

É um sistema de IA que atua como um assistente autônomo: você dá uma missão a ele, e ele próprio planeja os passos, usa calculadoras, busca na web, avalia os resultados intermediários e corrige os próprios erros até terminar o trabalho.

### Escopo e distinções

Diferencia-se de um chatbot reativo tradicional: enquanto o chatbot apenas responde a uma única pergunta por vez, o agente executa loops cíclicos complexos de raciocínio e ação (*Reason + Act*) sem intervenção humana contínua.

## 🧩 Problema que resolve

Resolve a incapacidade de modelos estáticos de resolver tarefas abertas que exigem múltiplas etapas, uso de ferramentas externas computacionais e tomada iterativa de decisões no mundo real.

## 💡 Intuição

Pense na diferença entre um assistente de voz que apenas diz a previsão do tempo quando solicitado versus um assistente pessoal humano para quem você diz: "Organize minhas férias para o Rio de Janeiro" e ele próprio pesquisa passagens, compara preços, agenda hotéis e envia um relatório completo.

## ⚙️ Como funciona

### Etapas

1. **Percepção e Planejamento:** O modelo recebe o objetivo do usuário e gera um plano estruturado de ações (*task decomposition*).
2. **Execução de Ferramentas (*Tool Use*):** O agente invoca APIs externas, bancos de dados ou interpretadores de código.
3. **Observação e Reflexão:** O agente avalia a saída obtida pela ferramenta. Se houver falha, ele corrige o plano.
4. **Conclusão:** O ciclo repete-se até o objetivo ser atingido, momento em que a resposta final é entregue ao usuário.

### Entradas e saídas

- Entradas: Objetivo ou instrução complexa em linguagem natural + Inventário de ferramentas disponíveis.
- Saídas: Execução de ações no ambiente e entrega do resultado final da tarefa.

## 📐 Formulação matemática

Modelado formalmente como um Processo de Decisão de Markov (MDP) onde a política é gerada por um modelo estocástico condicional $M$:

$$a_t \sim M(a_t \mid s_t, \text{Inventário de Ferramentas})$$

Onde:
- $s_t$: Estado atual do ambiente (incluindo histórico e saídas de ferramentas anteriores).
- $a_t$: Ação escolhida no tempo $t$ (chamada de ferramenta ou resposta).

## 🧱 Hipóteses e condições de validade

- Supõe que o modelo de fundação possui capacidade de planejamento lógico suficiente e que as ferramentas acopladas possuem descrições claras e APIs estáveis.

## ✅ Quando usar

- Em automação de fluxos complexos de trabalho, assistentes de engenharia de software (*coding agents*), pesquisas de mercado automatizadas e tarefas multi-etapas.

## 🚫 Quando não usar

- Em tarefas simples de resposta direta onde o custo computacional e a latência de loops de agentes sejam desnecessários.

## ⚠️ Limitações e armadilhas

- **Acumulação de Erros:** O erro em um passo inicial contamina todo o plano subsequente.
- **Loops Infinitos:** O agente pode ficar preso repetindo a mesma ação sem sucesso, consumindo créditos excessivos de API.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[agentes-de-ia|Agentes de IA]] | Executar tarefas autônomas multi-etapas usando ferramentas. | Objetivo complexo + Ferramentas. | Ações executadas + Resultado final. | Operação cíclica autônoma (Planeja -> Age -> Reflete). |
| [[rag|RAG]] | Buscar fatos textuais para fundamentar respostas. | Consulta isolada + Documentos. | Resposta textual baseada em fatos. | Focado estritamente em recuperação de informação e geração estática. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um agente de programação (*coding agent*) que recebe um aviso de bug no GitHub, navega pelo repositório, localiza o arquivo com erro, escreve um teste unitário, corrige o código Python e abre um *pull request* sozinho.

## 🔗 Relações no grafo

### Pré-requisitos

- [[modelo-de-fundacao|Modelo de Fundação]]

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

### Alternativas

- [[geracao-aumentada-de-recuperacao-rag|Geração Aumentada de Recuperação (RAG)]]

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG e Agentes
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação conceitual e estrutural dos Agentes de IA, inventário de ferramentas, planejamento e ciclos de reflexão (*ReAct/Reflexion*).
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que são Agentes de IA (AI Agents)?
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
*Nota gerada a partir do capítulo Capítulo 6 — RAG e Agentes. A interpretação final deve ser revisada pelo estudante.*
