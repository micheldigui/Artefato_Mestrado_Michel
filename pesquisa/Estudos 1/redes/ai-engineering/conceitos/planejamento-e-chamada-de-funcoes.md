# 🧠 Planejamento e Chamada de Funções (Function Calling)

**Rede:** `ai-engineering`   **Área:** `agentes`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 6 — RAG and Agents
- Localização: Páginas 281–292

## 📝 Definição

### Definição formal

O **Planejamento e Chamada de Funções** (*Planning and Function Calling*) compreende a mecânica algorítmica e a interface estruturada pelas quais um [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|agente de IA]] decompõe um objetivo abstrato em uma trajetória viável de passos de computação e invoca programas de software externos:

- **Planejamento (*Planning*):** A capacidade do modelo de formular roteiros operacionais (*trajectories*) que delimitam a sequência de estados, decisões e ações exigidas para atingir a meta sob restrições de tempo e recursos;
- **Chamada de Funções (*Function Calling*):** A habilidade nativa da rede neural de emitir saídas estritamente estruturadas (em JSON) contendo o identificador canônico de uma função e os argumentos nominais extraídos ou deduzidos do contexto, permitindo que a aplicação hospedeira execute o código determinístico correspondente.

### Em linguagem simples

Planejar é quando a IA monta um plano de ação na cabeça antes de sair fazendo besteira. A Chamada de Funções (*Function Calling*) é a maneira padronizada que a IA tem de "apertar os botões" dos outros sistemas: em vez de apenas falar frases bonitas, ela cospe um bloquinho de código formatado dizendo com precisão: *"Chame a função `consultar_clima` para a cidade de `São Paulo`"*.

### Escopo e distinções

O modelo de linguagem **não executa a função diretamente em seu silício**. O modelo apenas gera o texto estruturado que expressa a intenção de execução; é o código da aplicação de software em volta que intercepta esse texto, executa a função no mundo real e devolve a resposta para o modelo continuar pensando.

## 🧩 Problema que resolve

Resolve a barreira de comunicação entre a linguagem natural ambígua e os sistemas de software determinísticos. Sem *function calling*, desenvolvedores precisavam usar expressões regulares frágeis para tentar descobrir se a IA estava pedindo para rodar um comando; com o suporte nativo calibrado no pós-treinamento, o modelo emite chamadas perfeitas garantidas por gramáticas de decodificação.

## 💡 Intuição

Pense em um executivo estrangeiro que não fala português contratando uma secretária executiva no Brasil:

- O executivo (**o modelo de fundação**) dita em inglês uma ordem de alto nível: `"Quero me hospedar perto da praia no Rio amanhã"`.
- A secretária entende a intenção e redige uma ordem de serviço técnica no sistema corporativo (**Function Calling**): `reserva_hotel(cidade="Rio de Janeiro", regiao="Copacabana", data="2026-09-18")`.
- O sistema de reservas do hotel processa a ordem de serviço e devolve o voucher confirmado.

## ⚙️ Como funciona

O planejamento moderno exige desacoplar formalmente o plano da sua execução real:

### Etapas

1. **Declaração do Inventário de Funções:** A aplicação envia para a API do modelo uma lista contendo as assinaturas em JSON Schema de todas as ferramentas disponíveis (nome, descrição e tipos de parâmetros).
2. **Geração do Plano de Ação:** O modelo avalia o comando do usuário e gera uma decomposição de ações, que pode seguir diferentes **fluxos de controle**:
   - *Sequencial:* Passo B depende estritamente do término do Passo A;
   - *Paralelo:* Múltiplas ferramentas independentes são acionadas ao mesmo tempo;
   - *Ramificação Condicional (IF/ELSE):* Ação seguinte depende do resultado retornado pela anterior;
   - *Loop (WHILE/FOR):* Repetição de varredura até que uma condição de parada seja satisfeita.
3. **Validação do Plano:** O software valida o plano gerado contra heurísticas e diretrizes de segurança antes de disparar ferramentas perigosas.
4. **Emissão da Chamada (*Tool Call*):** O modelo produz a saída estruturada com `name: "nome_funcao"` e `arguments: "{...}"`.
5. **Execução no Host:** A aplicação executa a função localmente (ex.: consulta um banco SQL ou chama uma API externa).
6. **Injeção da Observação:** O retorno da ferramenta é encapsulado sob a tag de papel de ferramenta (`role: "tool"`) e realimentado no contexto do modelo para orientar o próximo passo.

### Entradas e saídas

- **Entradas:** Descrições de esquemas de ferramentas e solicitação contextual do usuário.
- **Saídas:** Objetos de chamada de função (`tool_calls`) prontos para execução no runtime da aplicação.

## 📐 Formulação matemática

O processo de planejamento atua como um problema de busca em árvore sobre um grafo de estados $\mathcal{S}$ e ações $\mathcal{A}$. 
Dado o estado atual $s_t$, a política do modelo de fundação parametriza a distribuição sobre a próxima ação estruturada $a_t \in \mathcal{A}$ e seus argumentos $\theta_{\text{args}}$:

$$P(a_t, \theta_{\text{args}} \mid s_t; \Theta_{\text{modelo}}) = P(a_t \mid s_t) \cdot P(\theta_{\text{args}} \mid s_t, a_t)$$

Nas APIs de ponta, o desenvolvedor pode configurar o hiperparâmetro de controle de ferramentas $\text{tool\_choice}$:

- $\text{tool\_choice} = \text{"none"}$: Força $P(a_t = \text{texto}) = 1$;
- $\text{tool\_choice} = \text{"required"}$: Força $P(a_t \in \mathcal{A}_{\text{ferramentas}}) = 1$;
- $\text{tool\_choice} = \text{"auto"}$: O modelo calibra dinamicamente a necessidade da ferramenta.

## 🧱 Hipóteses e condições de validade

- A inferência pressupõe modelos que passaram por pós-treinamento específico com amostras sintéticas de function calling para evitar alucinações de argumentos ou chamadas de funções inexistentes.

## ✅ Quando usar

- Integração de modelos com bancos de dados relacionais e APIs de serviços web corporativos.
- Automação de pipelines onde a resposta da IA deve alimentar diretamente variáveis em outros programas de software sem necessidade de parsing manual por regex.

## 🚫 Quando não usar

- Consultas onde toda a informação exigida já consta com clareza dentro do contexto do prompt original, onde disparar chamadas de função vazias gera latência e custos inúteis.

## ⚠️ Limitações e armadilhas

- **Alucinação de parâmetros:** O modelo pode acertar o nome da função perfeitamente, mas inventar um valor fictício para um parâmetro obrigatório caso o dado não tenha sido fornecido pelo usuário.
- **Sobrecarga de contexto por esquemas:** Declarar dezenas ou centenas de ferramentas na API consome milhares de tokens de entrada antes mesmo de o usuário digitar sua pergunta, encarecendo a fatura e aproximando o modelo do efeito *lost-in-the-middle*.

## 🔍 Comparações

| Abordagem de Controle | Como opera? | Robustez a Falhas | Flexibilidade |
|---|---|---|---|
| **Plano em Texto Livre** | O modelo escreve o que vai fazer em parágrafos | Baixa (difícil de automatizar por código) | Alta |
| **Function Calling Nativo** | Emissão de objetos JSON validados por gramática | **Altíssima (garante conformidade sintática)** | Estruturada |
| **Plano em Linguagem Natural com Tradutor** | Modelo planeja em texto; um submodelo traduz para código | Alta (robusto a mudanças de nomes de APIs) | Máxima |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um usuário pergunta: `"Quantos quilos pesam 40 libras?"`.
A aplicação declarou previamente a ferramenta `lbs_to_kg(lbs: float)`.
O modelo de fundação analisa a pergunta e, em vez de responder com texto, devolve a chamada estruturada:

```json
{
  "tool_calls": [
    {
      "name": "lbs_to_kg",
      "arguments": "{\"lbs\": 40.0}"
    }
  ]
}
```

A aplicação intercepta a mensagem, roda a função matemática simples em Python `40.0 * 0.453592 = 18.1437`, e envia de volta para o modelo: `{"role": "tool", "content": "18.14 kg"}`. O modelo lê o dado e finaliza para o usuário: `"40 libras equivalem a aproximadamente 18,14 quilos"`.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/agentes-de-ia-e-ferramentas.md|Agentes de IA e Inventário de Ferramentas]]
- [[redes/ai-engineering/conceitos/amostragem-restrita-e-saidas-estruturadas.md|Amostragem Restrita e Saídas Estruturadas]]

### Complementos

- [[redes/ai-engineering/conceitos/reflexao-e-correcao-de-erros-em-agentes.md|Reflexão e Correção de Erros em Agentes (ReAct e Reflexion)]]
- [[redes/ai-engineering/conceitos/avaliacao-e-modos-de-falha-de-agentes.md|Avaliação e Modos de Falha de Agentes]]

### Alternativas

- Parsing manual de texto livre através de expressões regulares complexas.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/rag-multimodal-e-dados-tabulares.md|RAG Multimodal e Dados Tabulares (Text-to-SQL)]]
- [[redes/ai-engineering/conceitos/sistemas-de-memoria-para-ia.md|Sistemas de Memória para IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 6 — RAG and Agents
- **Localização:** Páginas 281–292
- **Evidência:** Chip Huyen discute o debate sobre se LLMs autorregressivos conseguem planejar (citando as críticas de Yann LeCun e Kambhampati), detalha a implementação de pseudocódigo de Function Calling nas APIs modernas, analisa a granularidade de planos e formaliza os quatro fluxos de controle complexos (sequencial, paralelo, branching e loops).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Function Calling e por que ele não significa que a rede neural executa o código internamente?
2. Por que o desacoplamento formal entre a geração do plano e sua execução física é indispensável para a segurança de agentes?
3. Quais são os quatro fluxos de controle fundamentais que podem estruturar a trajetória de execução de um agente?
4. Como o debate entre Yann LeCun e pesquisadores de LLMs caracteriza as limitações de planejamento de modelos autorregressivos puros?
5. Qual é o perigo de declarar centenas de ferramentas simultâneas no esquema de uma API de modelo de fundação?
6. Como funciona a abordagem de planejamento em dois níveis (plano em linguagem natural seguido por um modelo tradutor de chamadas)?
7. O que acontece quando o modelo de fundação emite uma chamada de função com parâmetros obrigatórios alucinados?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
