---
title: "Detecção de Anomalias"
type: "conceito"
network: "machine-learning"
area: "Unsupervised Learning"
source_ids:
  - nenhum
source_evidence:
  - id: "nenhuma"
    matches: 0
    sections: []
evidence: "extraido_e_indexado"
confidence: "revisar"
tags:
  - conceito
  - rede/machine-learning
  - unsupervised-learning
status: "canônico"
---

# 🧠 Detecção de Anomalias

**Rede:** `machine-learning`

## 📚 Origem do conteúdo
As fontes abaixo são metadados de rastreabilidade. Elas não são nós da rede de conhecimento.

- *Nenhuma fonte foi mapeada automaticamente ainda.*

## 📝 Definição
Processo de identificar observações que se afastam do comportamento esperado da população ou do processo.

## 💡 Intuição
Uma anomalia é relativa ao contexto: o que é raro em uma situação pode ser normal em outra.

## ⚙️ Como funciona
Pode usar distância, densidade, isolamento, reconstrução ou modelos probabilísticos; o limiar converte um score em alerta.

## 🧩 Problema que resolve
Fraude, monitoramento, falhas, segurança e controle de qualidade quando há poucos rótulos de eventos anômalos.

## 🧱 Hipóteses e condições de validade
Antes de aplicar este conceito, explicite o tipo de dado, a unidade de análise, a variável-alvo e o que precisa permanecer estável entre treino e uso. Verifique também as hipóteses específicas descritas na definição, no mecanismo e nas limitações desta nota.

## ✅ Quando usar
Fraude, monitoramento, falhas, segurança e controle de qualidade quando há poucos rótulos de eventos anômalos.

## ⚠️ Limitações e armadilhas
Raridade não implica erro, mudanças de regime geram falsos positivos e o limiar deve considerar custo operacional.

## 🔗 Relações
- [[redes/machine-learning/conceitos/DBSCAN|DBSCAN]]
- [[redes/machine-learning/conceitos/Outliers|Outliers]]
- [[redes/machine-learning/conceitos/Matriz_de_Confusão|Matriz de Confusão]]
- [[redes/machine-learning/conceitos/Precision_e_Recall|Precision e Recall]]

## 🔍 Comparação para não confundir
Use as relações acima como roteiro de contraste: compare objetivo, entradas, hipótese principal, tipo de saída, custo computacional e forma de validação. A escolha não deve ser feita apenas pela frequência do termo nas fontes; ela depende do problema, dos dados e do erro que se deseja controlar.

## 📚 Evidência nas fontes consultadas
As referências abaixo registram onde o pipeline encontrou o conceito. A contagem indica ocorrências dos padrões de busca no texto extraído; as seções são pistas do sumário, não substituem a leitura crítica do capítulo.

- *Nenhuma evidência automática foi registrada para este conceito.*

## 🧪 Exemplo mental
Sinalizar transações fora do padrão de cada cliente e revisar os casos com maior score de anomalia.

## 🧠 Perguntas de revisão
1. Como eu explicaria **Detecção de Anomalias** sem repetir a definição?
2. Qual problema concreto este conceito resolve e qual é a variável de saída?
3. Quais hipóteses precisam ser verdadeiras para a aplicação ser confiável?
4. Que alternativa eu compararia e qual critério justificaria a escolha?
5. Como eu verificaria o comportamento em dados novos ou em um caso-limite?

## 📌 Notas pessoais
- [ ] Escrever uma explicação com minhas próprias palavras.
- [ ] Implementar ou revisar um exemplo pequeno.
- [ ] Registrar uma decisão, dúvida ou conexão nova.

---
*Nota canônica gerada pelo pipeline; preserve as seções pessoais ao regenerar.*
