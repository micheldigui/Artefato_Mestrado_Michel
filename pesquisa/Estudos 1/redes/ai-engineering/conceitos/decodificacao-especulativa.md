# 🧠 Decodificação Especulativa (*Speculative Decoding*)

**Rede:** `ai-engineering`  
**Área:** `otimizacao-de-inferencia`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 9 — Otimização de Inferência
- Localização: localização não informada no material recebido

## 📝 Definição

### Definição formal

Uma técnica de aceleração de inferência para modelos autoregressivos que emprega um modelo de rascunho (*draft model*) menor e extremamente rápido para gerar múltiplos tokens candidatos de forma especulativa, os quais são posteriormente verificados em paralelo pelo modelo alvo (*target model*) em um único ciclo de computação na GPU.

### Em linguagem simples

É a estratégia do "estagiário e do sênior": um modelo menor e rápido escreve um rascunho de várias palavras rapidamente, e o modelo grande e inteligente apenas bate o olho em paralelo para verificar se concorda, acelerando a escrita sem perder a qualidade.

### Escopo e distinções

Diferencia-se da geração padrão porque converte a verificação de tokens sequenciais em uma operação paralela vetorizada, aproveitando os núcleos ociosos (*compute-bound*) da placa de vídeo durante a fase de decodificação.

## 🧩 Problema que resolve

Resolve o gargalo de velocidade da fase de *Decode*, onde o modelo grande fica ocioso e lento gerando apenas um token por vez devido às limitações de transferência de largura de banda de memória.

## 💡 Intuição

Imagine um escritor renomado (modelo alvo) escrevendo um livro: é muito mais rápido para ele ler e aprovar um parágrafo inteiro escrito por um assistente veloz (modelo de rascunho) do que ter que ditar cada sílaba sozinho, vagarosamente.

## ⚙️ How it works / Como funciona

### Etapas

1. **Rascunho:** O modelo menor (*draft*) gera rapidamente uma sequência de $K$ tokens candidatos.
2. **Verificação Paralela:** O modelo principal (*target*) processa esses $K$ tokens de uma só vez, em paralelo.
3. **Aceitação:** O modelo principal valida os tokens da esquerda para a direita. O maior subconjunto de tokens em que ambos os modelos concordam é aceito de uma só vez.
4. **Correção:** O modelo principal gera um token corretivo final para o ciclo.

### Entradas e saídas

- Entradas: Contexto atual, modelo de rascunho rápido e modelo principal de alta precisão.
- Saídas: Múltiplos tokens validados gerados em um único ciclo de verificação paralela.

## 📐 Formulação matemática

Baseia-se na amostragem por rejeição estocástica para garantir que a distribuição de probabilidade final gerada pela decodificação especulativa seja matematicamente idêntica àquela que seria gerada exclusivamente pelo modelo alvo grande:

$$P_{\text{target}}(x) \ge q(x)$$

Onde $q(x)$ representa a distribuição sugerida pelo modelo de rascunho, garantindo perdas matemáticas nulas (*lossless acceleration*).

## 🧱 Hipóteses e condições de validade

- Supõe que o modelo de rascunho compartilha o mesmo vocabulário e tokenizador do modelo principal e possui alta taxa de concordância de predição.

## ✅ Quando usar

- Em servidores de inferência de alto volume onde o custo de latência por token de saída (*TPOT*) precisa ser drasticamente reduzido sem alterar os pesos do modelo principal.

## 🚫 Quando não usar

- Em hardwares cujo nível de utilização de computação (*MFU*) já esteja saturado ao máximo, ou quando não houver um modelo de rascunho compatível disponível.

## ⚠️ Limitações e armadilhas

- Se o modelo de rascunho errar muito as predições, o sistema precisará rejeitar os candidatos com frequência, gerando um custo computacional adicional de verificação que pode tornar a inferência mais lenta do que o padrão.

## 🔍 Comparações

| Conceito | Objetivo | Entrada | Saída | Diferença principal |
|---|---|---|---|---|
| [[decodificacao-especulativa|Decodificação Especulativa]] | Acelerar o *Decode* usando um modelo rascunho + modelo alvo. | Contexto atual + Modelo rascunho + Modelo alvo. | Vários tokens validados por ciclo. | Utiliza dois modelos cooperativos (pequeno + grande) para acelerar a geração sem perda de qualidade. |
| [[decode-padrao|Decode Autoregressivo Padrão]] | Gerar texto sequencialmente palavra por palavra. | Contexto atual + Modelo único. | Um único token gerado por ciclo. | Executado por um único modelo de forma estritamente sequencial e lenta. |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O Llama 3 menor de 8B gera um trecho de 5 palavras para uma frase de código, e o Llama 3 maior de 70B bate o olho, valida as 5 palavras de uma só vez em um milissegundo, gerando um ganho de velocidade de 2x na tela do programador.

## 🔗 Relações no grafo

### Pré-requisitos

- [[prefill-e-decode|Prefill e Decode]]
- [[kv-cache|KV Cache]]

### Complementos

- [[engenharia-de-ia|Engenharia de IA]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo.

### Conceitos relacionados

- Nenhuma relação suficientemente sustentada pelo capítulo.

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 9 — Otimização de Inferência
- **Localização:** localização não informada no material recebido
- **Evidência:** Apresentação da decodificação especulativa (*speculative decoding*) como técnica de aceleração de inferência sem perda de acurácia.
- **Confiança:** alta

## ❓ Perguntas de revisão

1. O que é Decodificação Especulativa (Speculative Decoding)?
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
*Nota gerada a partir do capítulo Capítulo 9 — Otimização de Inferência. A interpretação final deve ser revisada pelo estudante.*
