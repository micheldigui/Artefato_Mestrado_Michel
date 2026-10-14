# 🧠 Adaptação de Modelos

**Rede:** `ai-engineering`   **Área:** `desenvolvimento`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 10–12, 40

## 📝 Definição

### Definição formal

A **Adaptação de Modelos** (*Model Adaptation*) é o conjunto de técnicas de engenharia pelas quais um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] pré-treinado e generalista é direcionado para atender a requisitos funcionais, semânticos, estilísticos ou factuais de uma tarefa ou domínio específico.

As estratégias de adaptação dividem-se em duas categorias fundamentais:

1. **Métodos baseados em contexto:** operam em tempo de inferência sem modificar os pesos matemáticos do modelo ([[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]] e [[redes/ai-engineering/conceitos/rag.md|RAG]]);
2. **Métodos paramétricos:** alteram ou expandem os pesos internos do modelo através de novo treinamento supervisionado ([[redes/ai-engineering/conceitos/finetuning.md|finetuning]]).

1. **Métodos baseados em contexto:** operam em tempo de inferência sem modificar os pesos matemáticos do modelo ([[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]] e [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]]);
2. **Métodos paramétricos:** alteram ou expandem os pesos internos do modelo através de novo treinamento supervisionado ([[redes/ai-engineering/conceitos/ajuste-fino.md|finetuning]]).

### Em linguagem simples

É o ato de pegar uma IA inteligente "de prateleira" e ensiná-la a trabalhar do jeito específico que a sua empresa precisa. Em vez de criar um modelo novo, você escolhe se vai apenas explicar o que quer nas instruções, dar documentos para ela consultar na hora ou treiná-la um pouco mais para mudar seu comportamento interno.

### Escopo e distinções

Constitui a atividade central do engenheiro de IA. Não abrange o pré-treinamento fundamental da arquitetura base. Diferencia-se pela escolha estratégica entre custo, volume de dados disponíveis e necessidade de controle determinístico sobre o modelo.

## 🧩 Problema que resolve

Modelos de fundação "crus" são excessivamente genéricos, propensos a prolixidade e desprovidos de informações proprietárias de empresas ou de padrões estilísticos específicos de marcas. A adaptação de modelos resolve o descompasso entre o conhecimento amplo e vago da IA de prateleira e a precisão exigida pelos produtos comerciais.

## 💡 Intuição

Pense em contratar um graduado excelente para sua empresa:

- **Engenharia de Prompt:** Você dá uma folha com orientações claras e exemplos da tarefa antes de ele começar o trabalho daquele dia.
- **RAG:** Você entrega a chave do arquivo confidencial da empresa para que ele consulte os relatórios internos sempre que precisar redigir algo.
- **Finetuning:** Você o matricula em um curso intensivo de especialização de três semanas para mudar seus hábitos e automatizar o jargão técnico da área.

## ⚙️ Como funciona

O processo de decisão e aplicação de adaptação segue uma ordem de maturidade técnica:

### Etapas

1. **Linha de base com prompt puro:** Testa-se o modelo padrão aplicando regras claras e exemplos na instrução de entrada ([[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]]).
2. **Injeção de contexto factual:** Caso o modelo falhe por desconhecer informações privadas ou recentes, implementa-se um pipeline de recuperação para alimentar o contexto ([[redes/ai-engineering/conceitos/rag.md|RAG]]).
3. **Ajuste comportamental:** Se o modelo tiver as informações, mas falhar em seguir formatos complexos, manter o tom de voz ou se o custo de prompts longos for proibitivo, parte-se para a atualização de pesos ([[redes/ai-engineering/conceitos/finetuning.md|finetuning]]).
4. **Composição mista:** Em produção madura, combina-se frequentemente RAG (para conhecimento atualizado) sobre um modelo previamente ajustado via finetuning (para formatos e brevidade).

1. **Linha de base com prompt puro:** Testa-se o modelo padrão aplicando regras claras e exemplos na instrução de entrada ([[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]]).
2. **Injeção de contexto factual:** Caso o modelo falhe por desconhecer informações privadas ou recentes, implementa-se um pipeline de recuperação para alimentar o contexto ([[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]]).
3. **Ajuste comportamental:** Se o modelo tiver as informações, mas falhar em seguir formatos complexos, manter o tom de voz ou se o custo de prompts longos for proibitivo, parte-se para a atualização de pesos ([[redes/ai-engineering/conceitos/ajuste-fino.md|finetuning]]).
4. **Composição mista:** Em produção madura, combina-se frequentemente RAG (para conhecimento atualizado) sobre um modelo previamente ajustado via finetuning (para formatos e brevidade).

### Entradas e saídas

- **Entradas:** Requisitos de produto, dados proprietários, métricas de avaliação e um modelo de fundação base.
- **Saídas:** Um sistema adaptado operando com taxas de acerto e custos compatíveis com o objetivo de negócio.

## 📐 Formulação matemática

A adaptação é a busca pela política ótima $\pi^*$ que maximiza o alinhamento com a métrica de negócio $\mathcal{M}$:

$$\pi^* = \arg\max_{\pi \in \Pi} \mathbb{E}_{(x, y) \sim \mathcal{D}_{\text{tarefa}}} \left[ \mathcal{M}\big(\pi(x), y\big) \right]$$

Onde o espaço de busca $\Pi$ varia conforme a estratégia:

- Em **Prompting**: $\pi(x) = f_\theta(P_{\text{template}}(x))$;
- Em **RAG**: $\pi(x) = f_\theta(x, \text{Retriever}(x))$;
- Em **Finetuning**: $\pi(x) = f_{\theta + \Delta\theta}(x)$.

## 🧱 Hipóteses e condições de validade

- O modelo de fundação original possui capacidade latente de raciocínio suficiente para executar a tarefa após a adaptação.
- Existência de dados de qualidade e em quantidade compatível com o método escolhido (dezenas para prompting, milhares para finetuning).

## ✅ Quando usar

- Universal: todo produto de IA construído com base em modelos de fundação requer pelo menos uma técnica de adaptação para ter utilidade prática.

## 🚫 Quando não usar

- Se o modelo de prateleira já resolver a tarefa com precisão de 100% via consulta direta sem nenhuma formatação ou contexto específico exigido (caso raro na prática).

## ⚠️ Limitações e armadilhas

- **Início precoce por finetuning:** Iniciar projetos diretamente por ajuste fino de pesos antes de esgotar o ganho de engenharia de prompt e RAG gera desperdício de tempo e custos de computação.
- **Sobrecarga de contexto:** Injetar contexto excessivo via RAG pode saturar a janela de atenção do modelo, degradando a resposta (*lost-in-the-middle*).

## 🔍 Comparações

| Técnica de Adaptação | Modifica Pesos? | Volume de Dados Requerido | Custo Inicial | Principal Benefício |
|---|---|---|---|---|
| **Prompt Engineering** | Não | 1 a 10 exemplos | Mínimo | Velocidade extrema de iteração |
| **RAG** | Não | Base documental existente | Médio | Conhecimento factual atualizado |
| **Finetuning** | Sim | Centenas a milhares de pares | Alto | Consistência de formato e redução de tokens |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma imobiliária quer um assistente que redija descrições atraentes de apartamentos de luxo no estilo característico da sua marca.

1. *Primeira tentativa:* Usa um modelo de fundação comercial puro. As descrições são corretas, mas usam jargões genéricos.
2. *Adaptação via Prompt:* O engenheiro adiciona à instrução 3 exemplos perfeitos de anúncios antigos da marca. O resultado melhora sensivelmente.
3. *Adaptação via Finetuning:* A imobiliária pega 2.000 anúncios premiados do seu acervo e treina um modelo leve aberto. Agora o modelo já gera nativamente o tom aristocrático exigido sem precisar que o desenvolvedor gaste centenas de tokens de instruções a cada requisição.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]
- [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]]

### Alternativas

- Treinamento de modelos específicos do zero (*from scratch*).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]
- [[redes/ai-engineering/conceitos/rag.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/finetuning.md|Ajuste Fino (Finetuning)]]

- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]
- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 10–12, 40
- **Evidência:** Chip Huyen introduz prompt engineering, RAG e finetuning como as três principais técnicas de adaptação de modelos, demarcando que adaptar um modelo poderoso é exponencialmente mais barato e rápido do que construí-lo do zero.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é adaptação de modelos e qual o seu papel dentro da Engenharia de IA?
2. Quais são as duas grandes categorias nas quais as técnicas de adaptação se dividem em relação aos pesos do modelo?
3. Quais são as vantagens relativas da Engenharia de Prompt em comparação com o Finetuning para projetos em estágio inicial?
4. Por que a introdução do RAG transformou a necessidade de atualização frequente de pesos para conhecimento factual?
5. Qual é o erro comum cometido por equipes que decidem aplicar finetuning precocemente?
6. Como as três principais técnicas de adaptação podem ser combinadas em uma arquitetura corporativa madura?
7. Qual critério de dados deve orientar a escolha entre usar apenas prompt engineering ou partir para finetuning?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
