---
title: "Transferência de Estilo para Aumento de Imagens"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Artificial Intelligence for Engineers"
tags: [conceito, rede/machine-learning, data-augmentation, imagens, deep-learning]
---

# Transferência de Estilo para Aumento de Imagens

## Definição
Transformação que combina o conteúdo estrutural de uma imagem com características de estilo de outra, como aparência de textura ou cor, para criar uma variante visual mantendo o objeto-alvo reconhecível.

## Como funciona
Uma rede separa representações associadas a conteúdo e estilo e compõe a imagem resultante com o conteúdo de uma amostra e o estilo de outra. É mais complexa que jitter fotométrico e precisa manter rótulo e estrutura da tarefa.

## Quando usar
Como estratégia de geração de variação visual quando o domínio inclui diversidade de estilos/captura e a classe depende do conteúdo que se pretende preservar.

## Limitações
O estilo transferido pode alterar características que definem a classe, introduzir artefatos ou criar uma distribuição artificial. Exige inspeção visual e avaliação em validação de dados reais; custo e complexidade são superiores a transformações simples.

## Relações
- [[redes/machine-learning/conceitos/Aumento_de_Dados|Aumento de Dados]]
- [[redes/machine-learning/conceitos/Geracao_Sintetica_com_Modelos_Generativos|Geração sintética com modelos generativos]]
- [[redes/machine-learning/conceitos/Transformacoes_Fotometricas_de_Imagens|Transformações fotométricas de imagens]]
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de atributos de imagens]]

## Evidências
*Artificial Intelligence for Engineers*, seção 8.5 sobre modelos avançados de augmentation, descreve neural style transfer como separação e recomposição de conteúdo e estilo.
