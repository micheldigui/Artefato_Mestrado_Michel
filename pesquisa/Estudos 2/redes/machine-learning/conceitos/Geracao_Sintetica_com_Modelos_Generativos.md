---
title: "Geração de Dados Sintéticos com Modelos Generativos"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "AI-Assisted_Statistics_for_Data_Scientists_3E_-_Peter_Bruce"
tags: [conceito, rede/machine-learning, data-augmentation, dados-sinteticos]
---

# Geração de Dados Sintéticos com Modelos Generativos

## Definição
Uso de modelos generativos, incluindo IA generativa, para produzir exemplos artificiais semelhantes aos dados de treino e ampliar variação em situações onde dados reais são escassos.

## Como funciona
O gerador aprende padrões dos exemplos disponíveis e sintetiza novas instâncias, como imagens com variações de cor, iluminação ou orientação. Os dados sintéticos precisam ser filtrados, rotulados/validados e avaliados junto à tarefa final.

## Quando usar
Como estratégia experimental quando a aquisição de dados reais é cara ou limitada e há critério confiável para verificar realismo, rótulos, diversidade e cobertura de subgrupos.

## Limitações
O gerador não inventa evidência confiável sobre regiões ausentes da amostra: vieses e lacunas podem ser reproduzidos. Artefatos podem confundir o classificador; dados sintéticos repetidamente gerados a partir de outros dados sintéticos podem degradar os modelos. Compare sempre com validação/teste de dados reais e audite duplicatas, fidelidade, diversidade e rótulos.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/SMOTE|SMOTE]]
- [[redes/machine-learning/conceitos/Amostragem_e_Representatividade|Amostragem e Representatividade]]
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-validation]]

## Evidências
Bruce et al., *AI-Assisted Statistics for Data Scientists*, 3ª ed., seção “Augmenting AI Training Data”: geração de variações sintéticas de estruturas de imagem, possíveis ganhos de variação para classes sub-representadas e limites por lacunas/artefatos nos dados de origem. O livro também nomeia a geração de dados de treino por LLM como “data augmentation”; esta nota foca a geração de exemplos de treino, não retrieval/context augmentation.
