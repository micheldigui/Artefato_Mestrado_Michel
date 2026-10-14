# 🧠 Engenharia de IA (AI Engineering)

**Rede:** `ai-engineering`  
**Área:** `fundamentos`

## 📚 Origem do conteúdo

- *AI Engineering: Building Applications with Foundation Models*, capítulo 1, “Introduction to Building AI Applications with Foundation Models”. A cópia de revisão não informa páginas confiáveis.

## 📝 Definição

Engenharia de IA é a disciplina de engenharia de software voltada a projetar, construir, avaliar e operar aplicações que incorporam modelos de IA pré-treinados, em especial modelos de fundação. Seu trabalho integra o modelo a dados, contexto, ferramentas e interfaces de produto e controla qualidade, segurança, latência e custo em uso real.

## 💡 Intuição

O modelo é um componente de uma aplicação, não o produto completo. O trabalho de Engenharia de IA consiste em escolher esse componente e construir ao seu redor o fluxo que o torna útil, verificável e operável para uma tarefa concreta.

## ⚙️ Como funciona

Um ciclo típico de Engenharia de IA inclui:

1. **Definir a tarefa e os critérios de sucesso:** especificar usuários, entradas, saídas aceitáveis, riscos e custos toleráveis.
2. **Selecionar uma abordagem:** escolher modelo, provedor e modalidade de adaptação compatíveis com os requisitos.
3. **Preparar o contexto e as capacidades:** estruturar instruções, recuperar informação externa quando necessário, conectar ferramentas e, se houver evidência, ajustar o modelo.
4. **Construir a aplicação:** integrar componentes, dados, interfaces, controles e tratamento de falhas.
5. **Avaliar:** testar qualidade, consistência, segurança, cobertura e desempenho em casos representativos, incluindo casos difíceis.
6. **Implantar e monitorar:** acompanhar qualidade, latência, custo, mudanças nos dados e versões dos modelos; usar feedback para orientar melhorias.

As principais formas de adaptação incluem métodos em contexto, como [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|engenharia de prompt]] e [[redes/ai-engineering/conceitos/rag.md|RAG]], e métodos que atualizam parâmetros, como [[redes/ai-engineering/conceitos/ajuste-fino.md|ajuste fino]]. [[redes/ai-engineering/conceitos/agentes-de-ia.md|Agentes de IA]] e ferramentas são opções de arquitetura para tarefas que exigem ações em várias etapas, não requisitos de toda aplicação.

## 🧩 Problema que resolve

Transforma as capacidades gerais de modelos de IA em funcionalidades de software que atendam a requisitos concretos. Isso exige lidar com saídas probabilísticas, contexto incompleto, falhas, dados privados, integrações, experiência do usuário e operação contínua.

## 🧱 Hipóteses e condições de validade

- O modelo escolhido tem capacidade adequada à tarefa ou pode ser adaptado dentro do orçamento disponível.
- A qualidade pode ser avaliada em exemplos representativos do uso esperado; uma demonstração isolada não prova confiabilidade.
- Respostas do modelo são tratadas como saídas que precisam de validação compatível com o risco. Regras críticas podem exigir verificações determinísticas ou revisão humana.
- Dados, permissões e integrações estão disponíveis de forma segura e legal para o uso proposto.

## ✅ Quando usar

Quando uma aplicação precisa incorporar compreensão, geração ou transformação de conteúdo por modelos de IA, e o comportamento resultante pode ser avaliado e governado no contexto do produto.

## 🚫 Quando não usar

Não use um modelo probabilístico como único mecanismo quando a tarefa exigir garantias estritas que ele não oferece, como cálculo exato, controle de segurança ou decisão regulada. Nesses casos, restrinja seu papel, valide a saída com lógica determinística ou escolha uma abordagem convencional adequada.

## ⚠️ Limitações e armadilhas

- **A última milha:** protótipos podem funcionar em exemplos felizes e falhar em entradas reais, exceções e fluxos de produção.
- **Qualidade variável:** alucinações, omissões, viés e sensibilidade ao contexto exigem avaliação e controles contínuos.
- **Mudanças externas:** versões de modelos, preços, limites de API e políticas de provedores podem alterar o comportamento ou a operação.
- **Custo e latência:** contexto extenso, múltiplas chamadas e agentes podem aumentar consumo e tempo de resposta.
- **Avaliação inadequada:** métricas agregadas ou testes poucos representativos podem ocultar falhas por grupo, tarefa ou condição.
- **Complexidade precoce:** RAG, agentes, fine-tuning e camadas arquiteturais devem responder a requisitos demonstrados, não ser adicionados por padrão.

## 🔍 Comparações

- **Engenharia de IA e Engenharia de ML:** Engenharia de IA enfatiza aplicações construídas com modelos já disponíveis e sua integração com contexto, ferramentas e produto. Engenharia de ML costuma enfatizar preparação de dados e desenvolvimento, treinamento e implantação de modelos preditivos. Há sobreposição; a divisão depende do sistema.
- **Engenharia de IA e [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]]:** a primeira é a disciplina e o conjunto de práticas; a pilha é um modelo para organizar camadas e componentes envolvidos.
- **Engenharia de IA e [[redes/ai-engineering/conceitos/arquitetura-de-engenharia-de-ia-em-camadas.md|Arquitetura de Engenharia de IA em Camadas]]:** a arquitetura descreve uma organização técnica possível para aplicações em produção; não é sinônimo da disciplina inteira.

## 🔗 Relações no grafo

### Fundamentos e componentes

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/modelo-de-linguagem.md|Modelo de Linguagem]]
- [[redes/ai-engineering/conceitos/pilha-de-engenharia-de-ia.md|Pilha de Engenharia de IA]]

### Adaptação e construção

- [[redes/ai-engineering/conceitos/engenharia-de-prompt.md|Engenharia de Prompt]]
- [[redes/ai-engineering/conceitos/rag.md|RAG]]
- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino]]
- [[redes/ai-engineering/conceitos/agentes-de-ia.md|Agentes de IA]]
- [[redes/ai-engineering/conceitos/arquitetura-de-engenharia-de-ia-em-camadas.md|Arquitetura de Engenharia de IA em Camadas]]

### Avaliação e operação

- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/desafio-da-ultima-milha-em-ia.md|Desafio da Última Milha em IA]]
- [[redes/ai-engineering/conceitos/humano-no-loop.md|Humano no Loop]]

## 📚 Evidência nas fontes consultadas

- *AI Engineering: Building Applications with Foundation Models*, capítulo 1: enquadra a Engenharia de IA como construção de aplicações sobre modelos de fundação e apresenta adaptação, design de contexto e integração como partes do trabalho.
- A descrição operacional desta nota organiza essas ideias em etapas de produto; é uma síntese conceitual, não uma transcrição de um único fluxo prescrito pelo capítulo.

## ❓ Perguntas de revisão

1. Qual parte da aplicação é responsabilidade da Engenharia de IA além de selecionar o modelo?
2. Como a tarefa será avaliada com entradas representativas do uso real?
3. Que falhas devem ser barradas por controles determinísticos ou revisão humana?
4. Como mudanças de modelo, custo e latência serão monitoradas?

---
*Nota canônica reconstruída a partir da cópia de revisão marcada como incorporada; referências de página não disponíveis nessa cópia.*
