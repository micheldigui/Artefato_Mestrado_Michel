---
title: "Correção Funcional"
type: "conceito"
network: "ai-engineering"
aliases:
  - functional correctness
  - execution accuracy
  - pass@k
tags:
  - avaliacao
  - ai-engineering
---

# 🧠 Correção Funcional (pass@k)

**Rede:** `ai-engineering`   **Área:** `avaliacao`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 3 — Evaluation Methodology
- Localização: Páginas 126–127

## 📝 Definição

### Definição formal

A **Correção Funcional** (*Functional Correctness* ou *Execution Accuracy*) é um método objetivo de avaliação exata no qual as saídas geradas por um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] são validadas não pela sua similaridade superficial com um texto de referência, mas pela sua capacidade de executar com sucesso em um interpretador ou ambiente operacional e passar em uma bateria rigorosa de testes unitários ou verificações formais de estado. 

A métrica padrão é o **pass@k**, definida como a probabilidade não enviesada de que pelo menos uma dentre $k$ amostras de código geradas de forma independente pelo modelo resolva integralmente o problema proposto, passando em todos os casos de teste pré-estabelecidos.

### Em linguagem simples

É testar se o programa gerado pela IA realmente funciona na prática. Em vez de olhar se o código parece bonito ou se usa as mesmas variáveis de uma resposta humana, o sistema executa o código em um interpretador real (como Python ou banco SQL). Se o código compilar, rodar e devolver a resposta certa para todos os testes matemáticos exigidos, a IA ganha nota 10; se der erro ou falhar em um único teste, a nota é zero.

### Escopo e distinções

Diferencia-se radicalmente de métricas baseadas em sobreposição de texto como BLEU ou ROUGE. O capítulo pontua que no benchmark HumanEval, as pontuações de BLEU entre códigos corretos e incorretos eram quase indistinguíveis, comprovando que avaliar código por contagem de palavras não tem valor de engenharia.

## 🧩 Problema que resolve

Resolve a incapacidade de avaliar saídas técnicas e de programação através de similaridade de texto. Em computação, duas funções escritas de maneiras completamente diferentes (uma recursiva e outra iterativa, com nomes de variáveis distintos) podem ser ambas 100% corretas, enquanto uma função idêntica a um gabarito humano com a exceção de um sinal trocado de `+` para `-` está 100% quebrada. A correção funcional avalia a semântica operacional do resultado.

## 💡 Intuição

Pense em contratar um chaveiro para fabricar uma chave para sua porta.

- A **avaliação por similaridade de texto** seria como tirar uma foto da chave original e olhar se a chave nova é feita do mesmo metal prateado e tem o mesmo formato geral.
- A **correção funcional** é colocar a chave na fechadura, girar o trinco e ver se a porta realmente abre sem travar. Não importa se a chave nova é quadrada ou redonda; se ela abre a fechadura com perfeição em todas as tentativas, ela funciona.

## ⚙️ Como funciona

O pipeline de avaliação opera através de geração em lote e execução em ambiente isolado (*sandbox*):

### Etapas

1. **Definição do problema:** O modelo recebe a assinatura de uma função acompanhada de sua docstring explicativa e exemplos de comportamento (ex.: benchmark HumanEval ou MBPP).
2. **Geração de amostras ($n$):** O modelo gera $n$ soluções de código candidatas e independentes ($n \ge k$) com temperatura moderada para permitir diversidade estocástica.
3. **Execução em ambiente seguro (*Sandbox*):** Cada uma das $n$ soluções é executada sequencialmente ou em paralelo contra uma suíte de asserções determinísticas (`assert`).
4. **Contabilização dos sucessos ($c$):** Conta-se quantas amostras ($c$) passaram em $100\%$ dos testes unitários sem levantar nenhuma exceção de runtime.
5. **Cálculo estatístico:** Aplica-se a fórmula combinatória não enviesada do pass@k para derivar a taxa de sucesso.

### Entradas e saídas

- **Entradas:** Problema de programação e suíte de testes unitários com entradas e saídas esperadas.
- **Saídas:** Pontuação percentual pass@k (ex.: pass@1 de $75\%$, pass@10 de $92\%$).

## 📐 Formulação matemática

Para estimar o pass@k sem o viés estatístico de simplesmente gerar apenas $k$ amostras (o que teria alta variância), gera-se um número maior de amostras $n \ge k$ (por exemplo, $n = 200$) e conta-se o número de amostras corretas $c$. A formulação não enviesada introduzida por Chen et al. (OpenAI, 2021) é expressa como:

$$\text{pass@}k = \mathbb{E}_{\text{problemas}} \left[ 1 - \frac{\binom{n - c}{k}}{\binom{n}{k}} \right]$$

Onde:

- $\binom{n}{k}$ é a combinação de $n$ elementos tomados $k$ a $k$;
- $\binom{n - c}{k}$ representa a quantidade de combinações compostas estritamente por amostras incorretas;
- Como consequência probabilística direta: $\text{pass@1} \le \text{pass@3} \le \text{pass@10} \le \dots \le \text{pass@100}$, uma vez que dar mais chances ($k$) ao modelo eleva a probabilidade de pelo menos uma solução estar correta.

## 🧱 Hipóteses e condições de validade

- A suíte de testes unitários deve ter alta cobertura de casos de borda (*edge cases*); testes fracos podem aprovar códigos errôneos que falhariam em cenários reais.
- A execução deve ocorrer em containers isolados sem acesso à rede externa para evitar execução acidental ou intencional de código destrutivo pelo modelo.

## ✅ Quando usar

- Avaliação de modelos e copilotos de programação de software (benchmarks como HumanEval, MBPP).
- Sistemas de geração de consultas a bancos de dados relacionais (Text-to-SQL em benchmarks como Spider, BIRD-SQL e WikiSQL).
- Avaliação de agentes em jogos (onde a pontuação final do jogo dita a correção funcional da IA).

## 🚫 Quando não usar

- Em geração de texto livre, redação de contratos, resumos literários ou conversação geral, onde não existem interpretadores determinísticos nem testes unitários de sintaxe.

## ⚠️ Limitações e armadilhas

- **Foco estrito em acerto funcional:** A métrica pass@k tradicional aprova códigos que funcionam, mas que podem ser terrivelmente ineficientes (consumo absurdo de memória, algoritmos $\mathcal{O}(N^3)$) ou completamente ilegíveis para engenheiros humanos.
- **Risco de segurança na avaliação:** Rodar código arbitrário gerado por IA na máquina do desenvolvedor sem sandbox pode disparar comandos perigosos de deleção de arquivos ou conexões maliciosas de rede.

## 🔍 Comparações

| Métrica | O que avalia? | Método de Cálculo | Sensibilidade a Sinônimos |
|---|---|---|---|
| **BLEU / ROUGE** | Sobreposição visual de texto | Contagem de n-grams | Péssima (penaliza sinônimos) |
| **pass@1** | Correção prática da 1ª tentativa | Execução contra asserções | Imune (foca no comportamento) |
| **pass@10** | Capacidade de resolver em 10 tentativas | Probabilidade combinatória | Imune (mede potencial do modelo) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O modelo recebe a tarefa de criar a função `tem_elementos_proximos(numeros, limite)` que retorna verdadeiro se dois números em uma lista estiverem a uma distância menor que o limite.
O modelo gera três rascunhos de código:

1. O rascunho A usa dois loops aninhados `for` e passa em 6 dos 7 testes, falhando quando a lista contém números negativos.
2. O rascunho B gera um erro de sintaxe `SyntaxError` e nem compila.
3. O rascunho C ordena a lista primeiro e compara elementos adjacentes, passando com sucesso por todas as 7 asserções de teste unitário.

Ao avaliar sob $k=3$ tentativas, como a amostra C obteve êxito pleno, a tarefa é computada como resolvida para o cálculo do pass@3.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/desafios-de-avaliacao-de-modelos-de-fundacao.md|Desafios de Avaliação de Modelos de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/computacao-em-tempo-de-teste-test-time-compute.md|Computação em Tempo de Teste (Test Time Compute)]]

### Alternativas

- [[redes/ai-engineering/conceitos/similaridade-lexical.md|Similaridade Lexical]]
- [[redes/ai-engineering/conceitos/similaridade-semantica.md|Similaridade Semântica]]

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ia-como-juiz.md|IA como Juiz (AI-as-a-Judge)]]
- [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 3 — Evaluation Methodology
- **Localização:** Páginas 126–127
- **Evidência:** Chip Huyen aborda a avaliação por correção funcional e execução em interpretadores, detalha o uso de asserções no benchmark HumanEval e MBPP, e demonstra por que a métrica pass@k da OpenAI é o padrão de validação empírica em geração de código e Text-to-SQL.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a definição de Correção Funcional e em que ela se distingue das métricas tradicionais de processamento de texto?
2. Como funciona a formulação matemática da métrica pass@k proposta por Chen et al. no artigo do HumanEval?
3. Por que a pontuação pass@1 é estatisticamente menor ou igual à pontuação pass@10 para um mesmo modelo?
4. Qual foi a constatação empírica da OpenAI sobre a correlação entre pontuações BLEU e a correção funcional real de soluções de código?
5. Como benchmarks de Text-to-SQL modernos (como BIRD-SQL) expandiram a correção funcional para avaliar também a eficiência de execução da consulta?
6. Quais são os riscos de segurança ao avaliar correção funcional e como a infraestrutura de sandbox mitiga esses perigos?
7. Por que um código gerado por IA pode atingir pontuação perfeita no pass@k e ainda assim ser considerado de baixa qualidade por um engenheiro sênior?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

