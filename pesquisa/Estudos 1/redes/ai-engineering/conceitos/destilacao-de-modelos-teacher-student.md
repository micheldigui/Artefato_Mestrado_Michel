# 🧠 Destilação de Modelos (Teacher-Student)

**Rede:** `ai-engineering`   **Área:** `modelagem`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 395–396

## 📝 Definição

### Definição formal

A **Destilação de Modelos** (*Model Distillation* ou *Knowledge Distillation*, Hinton et al., 2015) é a técnica de compressão e transferência de conhecimento no qual um modelo compacto e de menor complexidade computacional (**Aluno / *Student***) é treinado para reproduzir o comportamento preditivo, o raciocínio ou as distribuições de probabilidade de saída geradas por um modelo substancialmente maior, mais poderoso e computacionalmente pesado (**Professor / *Teacher***), mantendo uma fração expressiva do desempenho do modelo original com menor latência e custo reduzido de inferência.

### Em linguagem simples

É o treinamento de mestre e aprendiz. O professor é uma IA gigantesca, pesada e caríssima (como um modelo de 70 bilhões de parâmetros). O aluno é uma IA levinha e rápida (como um modelo de 7 bilhões ou menos). Você faz o aluno observar milhares de respostas dadas pelo professor até que o aluno aprenda a resolver as mesmas tarefas quase com a mesma perfeição, mas gastando dez vezes menos memória e respondendo muito mais rápido.

### Escopo e distinções

Na era clássica do aprendizado profundo, a destilação era feita comparando os vetores de *logits* contínuos suaves do professor diretamente com os do aluno (como no DistilBERT, Sanh et al., 2019). Na era dos modelos de fundação via API, a destilação opera predominantemente através de **dados sintéticos de caixa-preta**: o professor gera textos, explicações passo a passo e códigos, e o aluno passa por [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|SFT]] sobre essas saídas.

## 🧩 Problema que resolve

Resolve a inviabilidade econômica de se implantar modelos massivos em produção para tarefas repetitivas. Servir um modelo de 70B ou 175B parâmetros para atender milhões de consultas diárias gera faturas astronômicas de nuvem e latência inaceitável para usuários móveis. A destilação transfere as competências centrais daquele domínio para um modelo leve que cabe em hardware comercial ou dispositivos de borda (*edge*).

## 💡 Intuição

Pense em um consultor executivo internacional com 40 anos de experiência (o modelo professor) que cobra R$ 5.000,00 por hora de consultoria. A empresa contrata um jovem analista dedicado e inteligente (o modelo aluno) para acompanhar o consultor durante três meses. O analista anota como o mestre analisa balanços, copia seus modelos de relatório e absorve suas técnicas essenciais. Ao final do trimestre, o consultor é dispensado e o analista assume a rotina diária da empresa: ele cobra um salário normal, entrega os pareceres muito mais rápido e acerta $95\%$ das mesmas coisas que o consultor cobraria uma fortuna para fazer.

## ⚙️ Como funciona

O processo articula-se em três etapas de curadoria e transferência:

### Etapas

1. **Seleção do Modelo Professor:** Escolhe-se o modelo mais competente disponível no mercado (ex.: GPT-4o, Claude 3.5 Sonnet ou um Llama 3-70B).
2. **Geração do Corpus de Transferência:**
   - Despacha-se milhares de prompts variados e complexos para o modelo professor;
   - O professor gera respostas contendo explicações encadeadas (*Chain-of-Thought*), formatações estruturadas e códigos depurados.
3. **Treinamento do Modelo Aluno:** O modelo de fundação menor (ex.: Llama 3-8B ou Mistral-7B) é submetido a ajuste fino supervisionado sobre os dados gerados pelo professor.
4. **Bootstrapping Inverso (Caso Nemotron-4):** Em cenários avançados de pesquisa, o processo pode se inverter: modelos menores atuam como professores parciais para gerar volumes massivos de dados sintéticos que alimentam um modelo aluno que é, na verdade, **maior** que o professor (como no Nemotron-4 340B da NVIDIA, que usou o Mixtral 8x7B para sintetizar seus dados).

### Entradas e saídas

- **Entradas:** Conhecimento latente do modelo professor e prompts de especialização.
- **Saídas:** Modelo aluno comprimido, otimizado para inferência de alta velocidade e baixo custo.

## 📐 Formulação matemática

Na destilação clássica por concordância de probabilidades de Hinton et al., a função de perda balanceia a perda de entropia cruzada com os dados reais ($y$) e a divergência de Kullback-Leibler em relação às probabilidades do professor suavizadas por uma temperatura de destilação $T$:

$$\mathcal{L}_{\text{distil}} = (1 - \alpha) \mathcal{L}_{\text{CE}}\Big(p_{\text{aluno}}, y\Big) + \alpha T^2 \mathcal{D}_{\text{KL}}\left( \text{softmax}\left(\frac{z_{\text{professor}}}{T}\right) \;\Bigg\|\; \text{softmax}\left(\frac{z_{\text{aluno}}}{T}\right) \right)$$

Onde $z$ representa os logits brutos e $\alpha$ regula o peso relativo entre o dado real e a imitação do professor.
Na destilação contemporânea baseada puramente em texto sintético gerado por APIs fechadas (sem acesso aos logits do professor), a perda colapsa na perda de SFT padrão sobre a sequência $Y_{\text{professor}}$ gerada pelo professor:

$$\mathcal{L}_{\text{SFT\_aluno}}(\theta) = -\sum_{j=1}^M \log P\Big(y_{j, \text{professor}} \;\Big|\; X, y_{<j, \text{professor}}; \theta\Big)$$

O caso do **DistilBERT** (Sanh et al., 2019) comprovou que é possível reduzir o tamanho do BERT em $40\%$, torná-lo $60\%$ mais rápido na inferência e preservar $97\%$ de sua capacidade de compreensão de linguagem.

## 🧱 Hipóteses e condições de validade

- A licença comercial do modelo professor deve autorizar explicitamente o uso de suas saídas para treinar outros modelos; violar termos de serviço de APIs fechadas gera passivos contratuais e riscos de bloqueio.
- As saídas do professor devem passar por [[redes/ai-engineering/conceitos/verificacao-e-filtragem-de-dados.md|verificação de dados]] para não transferir alucinações e preconceitos para o aluno.

## ✅ Quando usar

- Quando a empresa precisa reduzir custos operacionais de API em até $80\%$ a $90\%$ migrando de um modelo comercial fechado para um modelo próprio leve hospedado internamente.
- Aplicações com restrições extremas de latência de resposta que demandam modelos de menos de 8 bilhões de parâmetros rodando localmente.

## 🚫 Quando não usar

- Se a tarefa exigir conhecimento enciclopédico aberto massivo sobre milhões de tópicos mundiais dispersos que simplesmente não cabem fisicamente no número reduzido de parâmetros do modelo aluno.

## ⚠️ Limitações e armadilhas

- **O risco da imitação oca:** Conforme advertido pelo conceito de [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|imitação superficial]], o modelo aluno pode aprender a falar com o mesmo vocabulário pomposo do professor sem herdar a sua capacidade real de raciocinar sobre fatos novos.
- **Transmissão de vieses do professor:** Todos os pontos cegos e alucinações sistemáticas do modelo professor são internalizados como verdades absolutas pelo modelo aluno.

## 🔍 Comparações

| Característica | Modelo Professor (Teacher) | Modelo Aluno Destilado (Student) |
|---|---|---|
| **Escala de parâmetros** | Gigantesca (70B a centenas de bilhões) | Compacta (1B a 8B parâmetros) |
| **Custo por milhão de tokens** | Alto | **Extremamente baixo** |
| **Latência por token (TPOT)** | Mais lenta | **Ultrarrápida** |
| **Hospedagem em Edge** | Impossível em celulares comuns | **Perfeita para notebooks e dispositivos locais** |
| **Generalização fora de domínio** | Ampla e profunda | Focada nas tarefas destiladas |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O portal de notícias BuzzFeed precisava de um modelo de IA para gerar quizzes e artigos criativos em escala massiva para milhões de visitantes simultâneos.

- Usar a API do **GPT-3 (text-davinci-003)** diretamente em todas as requisições de milhões de usuários gerava uma fatura mensal de nuvem proibitiva.
- A equipe gerou milhares de exemplos perfeitos de quizzes utilizando o GPT-3 como **modelo professor**.
- Em seguida, pegou o modelo aberto e leve **Flan-T5** como **modelo aluno** e aplicou ajuste fino supervisionado com adaptadores LoRA sobre esses dados do professor.
- O resultado foi um modelo leve proprietário que reduziu o custo de inferência em **80%**, mantendo o mesmo estilo descontraído e engajador do modelo maior.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]

### Complementos

- [[redes/ai-engineering/conceitos/sintese-de-instrucoes-e-self-instruct.md|Síntese de Instruções e Self-Instruct]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Alternativas

- Quantização pura sem re-treino ou podas diretas de parâmetros.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|Colapso do Modelo e Riscos de Dados Sintéticos]]
- [[redes/ai-engineering/conceitos/quantizacao.md|Quantização]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 395–396
- **Evidência:** Chip Huyen formaliza a destilação de conhecimento baseada em Hinton et al. (2015), cita os ganhos históricos do DistilBERT (Sanh et al., 2019), analisa a destilação do Alpaca a partir do text-davinci-003, o caso corporativo do BuzzFeed com Flan-T5 e demonstra o bootstrapping em larga escala do Nemotron-4 340B da NVIDIA treinado a partir do Mixtral 8x7B.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Destilação de Modelos e qual é a analogia central do paradigma Professor-Aluno?
2. Quais são os benefícios de negócio em termos de custo de infraestrutura e latência proporcionados pela destilação?
3. Como o caso do DistilBERT (Sanh et al., 2019) quantificou empiricamente os trade-offs de tamanho, velocidade e retenção de capacidade?
4. Qual é a diferença técnica entre a destilação clássica via divergência de logits e a destilação moderna baseada em dados sintéticos de texto?
5. Por que as licenças comerciais de modelos de fundação frequentemente proíbem o uso de suas saídas para destilação de modelos concorrentes?
6. Como o projeto Nemotron-4 da NVIDIA ilustrou que um modelo aluno pode, em certos cenários, ser maior do que o modelo professor que gerou os dados?
7. Qual é o perigo da "imitação superficial" no processo de destilação de modelos de linguagem?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
