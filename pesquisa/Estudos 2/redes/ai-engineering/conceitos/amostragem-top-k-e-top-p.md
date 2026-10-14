# 🧠 Amostragem Top-k e Top-p

**Rede:** `ai-engineering`  
**Área:** `inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 2 — Understanding Foundation Models
- Localização: Páginas 94–95

## 📝 Definição

### Definição formal

A **Amostragem Top-k** e a **Amostragem Top-p** (*Nucleus Sampling*) são filtros algorítmicos de truncamento estocástico aplicados sobre a distribuição de probabilidades gerada por um [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|modelo de linguagem]]:
- **Top-k:** Trunca o vocabulário para conter estritamente os $k$ tokens de maior probabilidade, zerando a chance de todos os outros antes do sorteio.
- **Top-p (Núcleo):** Trunca dinamicamente o vocabulário para conter o menor subconjunto de tokens mais prováveis cuja soma cumulativa de probabilidades atinja o limiar de corte $p \in (0, 1]$.

### Em linguagem simples

São filtros de segurança estatística para impedir que o modelo fale absurdos. Em vez de deixar o sorteio aberto para todas as 100.000 palavras do dicionário (onde palavras estranhas poderiam ser sorteadas por puro azar), o Top-k permite escolher apenas entre as $k$ melhores opções fixas, e o Top-p permite escolher apenas entre as palavras mais sensatas que juntas formam a maior parte da probabilidade acumulada.

### Escopo e distinções

Diferenciam-se da [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|temperatura]], que apenas achata ou acentua as curvas de probabilidade. Top-k e Top-p eliminam fisicamente as caudas longas da distribuição (tokens de baixíssima probabilidade), prevenindo colapsos de coerência mesmo em temperaturas moderadas.

## 🧩 Problema que resolve

Evita que tokens situados na cauda longa da distribuição de probabilidade sejam selecionados em momentos de amostragem estocástica. Sem esses filtros, mesmo uma palavra com $0{,}001\%$ de chance pode ser sorteada se a frase for longa o bastante, inserindo um termo sem sentido no meio do texto e desencadeando alucinações subsequentes.

## 💡 Intuição

Pense em um técnico de futebol escalando um jogador:
- O **Top-k** ($k=5$) é uma regra rígida: "Você só pode escolher entre os 5 melhores jogadores do banco de reservas". Não importa se o 6º colocado é quase tão bom quanto o 5º, ele está sumariamente excluído.
- O **Top-p** ($p=0{,}90$) é uma regra inteligente: "Reúna os melhores jogadores até que eles representem $90\%$ da qualidade do time". Se em um dia de treino houver apenas 2 craques indiscutíveis que concentram quase toda a habilidade, o grupo terá 2 jogadores. Se em outro dia houver 15 atletas equilibrados, o grupo reunirá os 15. O tamanho do grupo adapta-se ao nível de certeza do contexto.

## ⚙️ Como funciona

Os filtros operam antes do sorteio aleatório final:

### Etapas

1. **Ordenação:** Os logits ou probabilidades de todos os tokens do vocabulário são ordenados em ordem decrescente de magnitude.
2. **Aplicação do filtro:**
   - *Se Top-k:* Mantém os primeiros $k$ tokens (ex.: $k = 50$) e descarta todo o restante do vocabulário ($k+1$ até $|V|$).
   - *Se Top-p:* Calcula-se a soma cumulativa das probabilidades a partir do primeiro colocado. O corte é feito assim que a soma ultrapassa $p$ (ex.: $p = 0{,}90$).
3. **Renormalização:** As probabilidades dos tokens que sobreviveram ao corte são recalculadas para que sua nova soma seja estritamente igual a $1$ ($100\%$).
4. **Sorteio:** Sorteia-se o próximo token exclusivamente dentro desse subconjunto filtrado.

### Entradas e saídas

- **Entradas:** Distribuição de probabilidade sobre o vocabulário e os hiperparâmetros de controle ($k$ inteiro, $p$ decimal entre 0 e 1).
- **Saídas:** Um espaço reduzido e seguro de tokens candidatos a partir do qual o próximo token será emitido.

## 📐 Formulação matemática

Dada uma sequência de tokens ordenados por probabilidade decrescente $p_1 \ge p_2 \ge \dots \ge p_{|V|}$:
- Na **Amostragem Top-k**, o conjunto elegível é estático:
  $$V^{(k)} = \{w_1, w_2, \dots, w_k\}$$
- Na **Amostragem Top-p (Núcleo)**, o conjunto elegível $V^{(p)}$ é o menor subconjunto tal que:
  $$\sum_{w_i \in V^{(p)}} P(w_i \mid \text{contexto}) \ge p$$
A probabilidade renormalizada de cada token sobrevivente $w_i \in V^{(p)}$ torna-se:

$$P'(w_i) = \frac{P(w_i \mid \text{contexto})}{\sum_{w_j \in V^{(p)}} P(w_j \mid \text{contexto})}$$

## 🧱 Hipóteses e condições de validade

- A aplicação de Top-p e Top-k pode ser combinada em sequência (frequentemente aplica-se Top-k primeiro para limitar a cauda extrema e Top-p em seguida para adaptação dinâmica).

## ✅ Quando usar

- **Top-p ($0{,}90$ a $0{,}95$):** Configuração recomendada como padrão da indústria para quase todas as aplicações de texto fluido e conversacional.
- **Top-k ($40$ a $100$):** Indicado quando se deseja restringir rigidamente o vocabulário ativo para evitar vocabulário exótico ou computação desnecessária de ordenação.

## 🚫 Quando não usar

- Em saídas puramente determinísticas de código e tarefas estritamente fechadas onde já se utiliza [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|temperatura zero]], tornando a filtragem de núcleo desnecessária (já que $T=0$ seleciona apenas o primeiro colocado).

## ⚠️ Limitações e armadilhas

- **Top-k rígido demais:** Se $k$ for fixado como muito pequeno (ex.: $k=2$) em um momento onde existem 10 sinônimos perfeitos igualmente prováveis, o modelo é forçado a ignorar 8 opções excelentes.
- **Top-k permissivo demais:** Se o modelo estiver respondendo uma pergunta de "Sim ou Não", e $k=50$, o modelo pode manter palavras absurdas entre os candidatos elegíveis caso a temperatura esteja alta. O Top-p contorna essa limitação adaptando o corte dinamicamente.

## 🔍 Comparações

| Dimensão | Top-k | Top-p (Nucleus Sampling) |
|---|---|---|
| **Critério de corte** | Número fixo de tokens ($k$) | Limiar cumulativo de probabilidade ($p$) |
| **Tamanho do conjunto** | Estático em todas as posições | Dinâmico (muda a cada palavra gerada) |
| **Sensibilidade ao contexto** | Baixa (ignora se o modelo tem certeza ou dúvida) | Alta (encolhe com certeza, expande com dúvida) |
| **Comportamento típico** | $k \in [40, 100]$ | $p \in [0{,}90, 0{,}95]$ |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Considere duas situações em um mesmo texto com **Top-p = 0.90**:
1. *Cenário de alta certeza:* O prompt é `"A capital da França é..."`. 
   O token `"Paris"` surge com $96\%$ de probabilidade. Como $96\% \ge 90\%$, o conjunto do núcleo $V^{(p)}$ contém **apenas 1 token** (`["Paris"]`). O modelo não corre nenhum risco de sortear outra palavra.
2. *Cenário de incerteza/aberto:* O prompt é `"Meu passatempo favorito é..."`.
   O modelo atribui: `"ler"` ($20\%$), `"correr"` ($18\%$), `"viajar"` ($15\%$), `"cozinhar"` ($12\%$), `"jogar"` ($10\%$), `"dormir"` ($9\%$), `"cantar"` ($8\%$). O algoritmo soma cumulativamente as palavras até ultrapassar $90\%$. Nesse caso, o conjunto de opções elegíveis expande-se dinamicamente para **6 tokens**.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-linguagem-autoregressivo.md|Modelo de Linguagem Autoregressivo]]
- [[redes/ai-engineering/conceitos/amostragem-e-temperatura.md|Amostragem e Temperatura]]

### Complementos

- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste.md|Computação em Tempo de Teste (Test Time Compute)]]

### Alternativas

- [[redes/ai-engineering/conceitos/amostragem-restrita-e-saidas-estruturadas.md|Amostragem Restrita e Saídas Estruturadas]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]
- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 2 — Understanding Foundation Models
- **Localização:** Páginas 94–95
- **Evidência:** O texto explica o funcionamento de Top-k e contrasta com a natureza dinâmica do Top-p (nucleus sampling), exemplificando como o Top-p se adapta contextualmente para expandir ou contrair o número de candidatos avaliados em situações de alta ou baixa certeza.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a diferença fundamental entre a Amostragem Top-k e a Amostragem Top-p (Nucleus Sampling)?
2. Por que o truncamento da cauda de probabilidade é necessário mesmo quando se utiliza uma temperatura baixa?
3. Como o Top-p se adapta dinamicamente entre contextos onde o modelo tem certeza absoluta e contextos com muitas respostas possíveis?
4. O que acontece com o cálculo de probabilidades dos tokens sobreviventes após o corte do Top-p?
5. Qual é a principal fraqueza do Top-k quando o modelo se depara com perguntas cujas respostas possíveis são estritamente binárias (Sim/Não)?
6. Quais são as faixas de valores de Top-p e Top-k consagradas como padrão de mercado para geração de texto fluido?
7. De que maneira a combinação simultânea de Temperatura, Top-k e Top-p pode ser orquestrada em uma chamada de inferência?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
