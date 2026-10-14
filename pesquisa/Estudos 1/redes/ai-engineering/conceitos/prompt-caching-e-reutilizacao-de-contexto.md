# 🧠 Prompt Caching e Reutilização de Contexto

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Inference Optimization
- Localização: Páginas 443–444

## 📝 Definição

### Definição formal

O **Prompt Caching** (*Prefix Caching* ou *Context Caching*, Gim et al., 2023) é a técnica de otimização no nível de serviço de inferência na qual os estados intermediários computados durante a fase de prefill (especificamente as representações em tensores do [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|KV Cache]]) correspondentes a prefixos ou segmentos textuais estáticos e idênticos compartilhados por múltiplas requisições (como instruções de sistema longas, poucos exemplos demonstrativos ou documentos de referência em RAG) são persistidos na memória da GPU ou em armazenamento rápido, permitindo que requisições subsequentes reutilizem diretamente esses tensores pré-calculados, eliminando a computação redundante de atenção e barateando custos operacionais.

### Em linguagem simples

É salvar a "leitura prévia" de textos que nunca mudam. Se a sua empresa coloca um manual de 50 páginas ou uma instrução de sistema gigantesca em todas as perguntas que os clientes fazem, a IA tradicionalmente gastava tempo e cobrava dinheiro para reler essas mesmas 50 páginas a cada clique. O Prompt Caching faz a IA ler o manual uma única vez e guardar a memória dessa leitura pronta; nas perguntas seguintes, ela pula a leitura e vai direto para a resposta, reduzindo o tempo de espera e dando descontos de até 90% na fatura de tokens.

### Escopo e distinções

Diferencia-se do cache semântico tradicional. O cache semântico devolve uma resposta inteira pronta para perguntas similares. O Prompt Caching atua **dentro do fluxo de inferência da rede neural**: ele não devolve a resposta final pronta; ele acelera o processamento do **começo do texto**, permitindo que o modelo gere respostas completamente inéditas para perguntas novas.

## 🧩 Problema que resolve

Resolve a penalidade financeira e de latência imposta por prompts com contextos estáticos volumosos. Em fluxos de trabalho corporativos com copilotos de código que anexam repositórios inteiros ou assistentes jurídicos que operam sobre contratos extensos, pagar repetidamente para a GPU processar os mesmos 50.000 tokens de entrada a cada mensagem de diálogo tornava as aplicações financeiramente insustentáveis.

## 💡 Intuição

Pense em um consultor de investimentos que atende clientes durante o dia:
- **Sem Prompt Caching:** Antes de cada cliente novo sentar na cadeira, o consultor é obrigado a ler novamente do zero o relatório econômico de 200 páginas do Banco Central. Ele passa 40 minutos lendo o relatório antes de dar o primeiro "bom dia" ao cliente (**latência TTFT gigante**).
- **Com Prompt Caching:** O consultor lê o relatório uma única vez no início da manhã e coloca post-its coloridos nas páginas principais (**o cache na memória**). Quando os clientes chegam ao longo do dia, ele atende instantaneamente porque o relatório já está fresco e assimilado em sua mente.

## ⚙️ Como funciona

O mecanismo baseia-se na detecção de casamento de prefixos (*prefix matching*):

### Etapas

1. **Recepção da Requisição:** A aplicação envia o prompt contendo um segmento de cabeçalho compartilhado (ex.: System Prompt de 2.000 tokens) seguido pela pergunta dinâmica do usuário.
2. **Identificação do Prefixo em Cache:** O motor de inferência verifica se o hash ou a sequência inicial de tokens coincide com blocos de KV Cache já armazenados na memória rápida.
3. **Pulo do Prefill Redundante (*Cache Hit*):**
   - O modelo não executa cálculos matriciais para os primeiros 2.000 tokens;
   - Os tensores de $K$ e $V$ correspondentes são carregados instantaneamente da tabela de cache.
4. **Execução Restrita:** A GPU processa em modo prefill apenas os tokens novos e dinâmicos específicos daquela pergunta (ex.: 20 tokens).
5. **Decodificação Imediata:** O modelo emite o primeiro token da resposta com latência mínima (**redução dramática do TTFT**).

### Entradas e saídas

- **Entradas:** Prompts com sobreposições estruturais de texto em suas posições iniciais.
- **Saídas:** Resposta gerada de forma autônoma com redução de até 90% no custo faturado de tokens de entrada e queda drástica no tempo de resposta.

## 📐 Formulação matemática

A latência da fase de prefill para uma sequência de entrada dividida entre um prefixo estático de comprimento $P_{\text{cache}}$ e uma consulta dinâmica $P_{\text{novo}}$ transforma-se de:

$$T_{\text{prefill\_sem\_cache}} \propto (P_{\text{cache}} + P_{\text{novo}})^2$$

Para:

$$T_{\text{prefill\_com\_cache}} \propto P_{\text{novo}}^2 + \text{Overhead}_{\text{leitura\_cache}}$$

Como tipicamente $P_{\text{cache}} \gg P_{\text{novo}}$ (ex.: $100.000$ tokens de cache contra $50$ tokens de pergunta nova), a economia temporal atinge ordens de grandeza.
A tabela empírica documentada no capítulo com base nos dados da Anthropic (2024) formaliza os ganhos práticos:

| Cenário de Uso | Tamanho do Cache | Latência TTFT sem Cache | Latência TTFT com Cache | Redução de Custo |
|---|---|---|---|---|
| **Chat com Livro Completo** | 100.000 tokens | $11{,}5 \text{ s}$ | **$2{,}4 \text{ s}$ (queda de $79\%$)** | **$-90\%$** |
| **Many-Shot Prompting** | 10.000 tokens | $1{,}6 \text{ s}$ | **$1{,}1 \text{ s}$ (queda de $31\%$)** | **$-86\%$** |
| **Diálogo Multi-Turno** | Contexto longo | $\approx 10{,}0 \text{ s}$ | **$\approx 2{,}5 \text{ s}$ (queda de $75\%$)** | **$-53\%$** |

## 🧱 Hipóteses e condições de validade

- A sobreposição de texto deve ocorrer **obrigatoriamente a partir do primeiro token da sequência (o prefixo)**; se o texto dinâmico for inserido no início e o texto estático no final, o mecanismo de atenção causal quebra a compatibilidade do cache e invalida o reaproveitamento.
- A aplicação deve manter um volume de consultas com intervalo temporal menor que a política de expiração (*TTL*) do cache do provedor para evitar que o cache seja ejetado por inatividade.

## ✅ Quando usar

- Sistemas de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]] que utilizam documentos de base compartilhados por centenas de consultas consecutivas.
- Assistentes corporativos que utilizam prompts de sistema densos com dezenas de exemplos demonstrativos (*many-shot prompting*).
- Interfaces de conversação de múltiplos turnos longos, reaproveitando as mensagens anteriores a cada nova resposta.

## 🚫 Quando não usar

- Em requisições avulsas e esparsas onde cada entrada é completamente aleatória, sem nenhum texto de cabeçalho ou documento comum compartilhado.

## ⚠️ Limitações e armadilhas

- **Custo de Armazenamento do Cache:** Provedores de nuvem (como o Google Gemini) concedem descontos pesados no custo de processamento do token em cache, mas cobram uma taxa de manutenção horária pelo espaço de memória alocado para reter o cache; se a taxa de consultas for baixa, o custo de armazenamento pode superar a economia de inferência.
- **Quebras Inadvertidas de Hash de Prefixo:** Inserir timestamps dinâmicos (como a data de hoje ou a hora atual) no topo do System Prompt invalida o cache para todas as requisições subsequentes. Variáveis dinâmicas devem ser sempre posicionadas após o bloco estático em cache.

## 🔍 Comparações

| Dimensão | Cache Semântico Tradicional | Prompt Caching (Prefix Caching) |
|---|---|---|
| **O que é salvo?** | A resposta final inteira em texto | Os tensores de atenção ($K, V$) do início do prompt |
| **Flexibilidade da pergunta**| Nula (só funciona se a pergunta for similar) | **Total (a pergunta do usuário pode ser inédita)** |
| **Nível de Atuação** | No software externo antes da IA | **Dentro do motor de inferência da GPU** |
| **Capacidade Gerativa** | Não gera nada novo (devolve texto estático) | **Gera raciocínios e respostas 100% inéditas** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma plataforma de análise de contratos carrega a convenção coletiva de trabalho de um sindicato (um documento longo de 80 páginas e 30.000 tokens).
- Cem advogados diferentes acessam a plataforma para fazer perguntas distintas sobre o mesmo documento: *"Qual é o adicional de periculosidade?"*, *"Qual é o prazo de licença-maternidade?"*, etc.
- **Sem Prompt Caching:** O provedor processa os 30.000 tokens cem vezes ($3.000.000$ de tokens de entrada faturados) e cada advogado espera 5 segundos para a resposta começar a ser digitada.
- **Com Prompt Caching:** O documento é processado uma única vez na primeira chamada. Para as 99 perguntas seguintes, os 30.000 tokens são lidos do cache instantaneamente: o TTFT despenca para 0,3 segundo e a fatura do dia cai em quase 90%.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]
- [[redes/ai-engineering/conceitos/otimizacao-do-kv-cache-e-pagedattention.md|Otimização do KV Cache e PagedAttention]]

### Complementos

- [[redes/ai-engineering/conceitos/metricas-de-desempenho-de-inferencia.md|Métricas de Desempenho de Inferência]]
- [[redes/ai-engineering/conceitos/templates-de-chat-e-prompts-de-sistema.md|Templates de Chat e Prompts de Sistema]]

### Alternativas

- Cache de respostas semântico tradicional via similaridade vetorial.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]
- [[redes/ai-engineering/conceitos/gargalos-computacionais-e-intensidade-aritmetica.md|Gargalos Computacionais e Intensidade Aritmética]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Inference Optimization
- **Localização:** Páginas 443–444
- **Evidência:** Chip Huyen conceitua o prompt caching a partir de Gim et al. (2023), ilustra o mecanismo de prefixo reutilizado (Figura 9-17) e analisa a Tabela 9-3 detalhando os ganhos empíricos oficiais divulgados pela Anthropic e Google Gemini com reduções de até 90% em custos e 79% em tempo de primeiro token.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Prompt Caching (*Prefix Caching*) e qual componente da inferência de LLMs ele reutiliza?
2. Em que o Prompt Caching difere estruturalmente de um cache semântico tradicional de respostas?
3. Por que a inserção de variáveis dinâmicas (como horários ou dados do usuário) no início do prompt pode anular o benefício do Prompt Caching?
4. Quais foram os ganhos percentuais de latência (TTFT) e custo financeiro documentados pela Anthropic no processamento de livros com 100.000 tokens?
5. Qual é o trade-off econômico introduzido pela cobrança horária de retenção de cache em provedores como o Google Gemini?
6. Como o Prompt Caching atua para acelerar conversas interativas de múltiplos turnos ao longo de um diálogo extenso?
7. Por que a técnica é considerada especialmente revolucionária para sistemas corporativos baseados em RAG?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
