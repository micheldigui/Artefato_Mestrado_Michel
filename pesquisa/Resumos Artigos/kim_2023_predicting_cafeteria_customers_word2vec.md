# Resumo de Artigo Científico: Kim et al. (2023)

## Referência Completa
**Autores:** Kim, S.; Gu, N.; Moon, J.; Kim, K.; Hwang, Y.; Lee, K.
**Título:** Comparative analysis of model performance for predicting the customer of cafeteria using unstructured data.
**Ano:** 2023
**Journal:** Communications for Statistical Applications and Methods, Vol. 30(5), 485–499.
**DOI:** [10.29220/CSAM.2023.30.5.485](https://doi.org/10.29220/CSAM.2023.30.5.485)
**Caminho Local:** `d:\PROJETOS\PRODUTO_MESTRADO\docs\artigos\Novos Artigos\wos\csam-30-5-485.pdf`

## Resumo
O estudo propõe prever a quantidade de clientes num refeitório universitário coreano (Korea) usando Machine Learning em cima de dados não-estruturados. Os autores embutiram os nomes cruos dos cardápios (texto livre de receitas e ingredientes) em vetores computacionais por meio do algoritmo NLP **Word2Vec**. Em seguida, injetaram esses vetores num *Stacking Ensemble Model* de Árvores de Decisão (Random Forest, Gradient Boosting e CatBoost) para fazer a predição probabilística da demanda.

## Principais Tópicos
- **Engenharia de Texto (Embeddings):** Comprovaram a eficácia monstruosa de usar ferramentas analíticas de Processamento de Linguagem Natural (NLP) associadas à matemática para encontrar relações de atratividade entre nomes de pratos e afluxo de pessoas.
- **Modelos Triunfantes:** Os melhores algoritmos isolados foram da família "Boosting" em árvore, destacando-se o CatBoost. Adicionar os vetores textuais (Embeddings do cardápio) no modelo aumentou drasticamente a eficácia em 8%.
- **Impacto Temporal:** Embora o NLP e as propriedades intrínsecas da comida tenham uma taxa alta, as variáveis de data e calendário temporal (*Date variables*) ainda foram as com maior impacto unânime sobre o fluxo.

## Conclusão
Codificar o texto do cardápio usando NLP previne parcialidade do analista humano e potencializa matematicamente a modelagem preditiva, gerando um resultado altamente acurado e reduzindo o desperdício (*food waste*) em restaurantes corporativos e públicos.

## Pertinência para o Projeto
**Essencial (Ligação Direta com o Notebook 05 e 07b).** Este é, até o momento, um dos artigos mais perfeitamente espelhados metodologicamente com o seu projeto. Você usa BERT (modelo avançado de processamento de texto que evoluiu do Word2Vec) no Notebook 05 para gerar embeddings do cardápio do seu RU. E usa *Gradient Boosting e Árvores* depois, no pipeline. Eles fizeram exatamente a mesma lógica em 2023. Ao referenciar este texto da Coreia, a "inovação" do seu uso de IA processando cardápios via NLP será completamente endossada pela literatura internacional.
