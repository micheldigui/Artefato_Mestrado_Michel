---
title: "Aumento de Dados (Data Augmentation)"
type: "conceito"
network: "machine-learning"
area: "Aumento de Dados"
status: "canônico"
source_ids:
  - "Deep_Learning_with_PyTorch_2Ed_Final_-_Howard_Huang"
  - "Hands-On_Machine_Learning_with_Scikit-Learn-Keras-and-TensorFlow-2nd-Edition-Aurelien-Geron"
  - "AI_and_ML_for_Coders_Applying_Core_ML_-_Suddhasatwa_Bhaumik"
  - "AI-Assisted_Statistics_for_Data_Scientists_3E_-_Peter_Bruce"
  - "Artificial Intelligence for Engineers"
  - "Machine_Learning_Hero_Master_Data_-_Cuantum_Technologies"
  - "Mastering_Computer_Vision_with_Python_-_Sohail"
  - "Mastering_NLP_From_Foundations_to_Agents_2E_-_Lior_Gazit"
  - "Hands_on_Machine_Learning_with_scikit_-_Tarek_Amr"
tags:
  - conceito
  - rede/machine-learning
  - feature-engineering
  - data-augmentation
---

# Aumento de Dados (Data Augmentation)

## Definição
Conjunto de transformações aplicadas a exemplos de treinamento para produzir variantes plausíveis que ampliem a diversidade observada pelo modelo. Uma transformação só é válida quando preserva a semântica relevante e o rótulo da tarefa.

## Intuição
O modelo aprende a reconhecer a estrutura importante do exemplo em vez de memorizar exatamente sua forma original. Variantes correlacionadas não equivalem a novas observações independentes; augmentation pode regularizar e reduzir sobreajuste, mas não cria informação sobre situações ausentes do domínio.

## Técnicas mapeadas

### Imagens: geometria, aparência e ruído
- [[redes/machine-learning/conceitos/Espelhamento_de_Imagens|Espelhamento (flip)]]
- [[redes/machine-learning/conceitos/Translacao_de_Imagens|Translação aleatória]]
- [[redes/machine-learning/conceitos/Recorte_Aleatorio_de_Imagens|Recorte aleatório]]
- [[redes/machine-learning/conceitos/Redimensionamento_e_Zoom_de_Imagens|Redimensionamento e zoom]]
- [[redes/machine-learning/conceitos/Rotacao_de_Imagens|Rotação]]
- [[redes/machine-learning/conceitos/Deformacoes_Geometricas_de_Imagens|Shear, perspectiva e deformação elástica]]
- [[redes/machine-learning/conceitos/Transformacoes_Fotometricas_de_Imagens|Brilho, contraste e saturação]]
- [[redes/machine-learning/conceitos/Adicao_de_Ruido_em_Dados|Adição de ruído]]
- [[redes/machine-learning/conceitos/Transferencia_de_Estilo_para_Aumento_de_Imagens|Transferência de estilo]]
- [[redes/machine-learning/conceitos/MixUp|MixUp]] — mistura de pares de entradas e rótulos; técnica relacionada de augmentation/regularização.

### Texto e NLP
- [[redes/machine-learning/conceitos/Aumento_de_Dados_Textuais_EDA|EDA textual]] — substituição, inserção, troca e exclusão de palavras.
- [[redes/machine-learning/conceitos/Back_Translation|Back translation (retrotradução)]]

### Classificação desbalanceada/tabular
- [[redes/machine-learning/conceitos/Oversampling_e_Bootstrap|Oversampling aleatório e bootstrap]]
- [[redes/machine-learning/conceitos/SMOTE|SMOTE]]
- [[redes/machine-learning/conceitos/ADASYN|ADASYN]]

### Dados sintéticos
- [[redes/machine-learning/conceitos/Geracao_Sintetica_com_Modelos_Generativos|Geração sintética com modelos generativos]]

As técnicas de séries temporais só devem virar nós específicos quando as fontes ou o domínio sustentarem transformações válidas. A coleção consultada não forneceu evidência suficiente para recomendar jittering, warping ou geração de janelas como métodos gerais para a tese.
## Como aplicar
1. Defina a hipótese de invariância: quais mudanças no dado não deveriam mudar o rótulo ou a previsão?
2. Escolha transformações compatíveis com domínio, unidade de análise e objetivo; comece com intensidade conservadora.
3. Gere amostras apenas no conjunto de treino de cada fold, após a separação. Em séries temporais, use partição temporal e histórico disponível no instante de previsão.
4. Mantenha validação e teste com dados reais, sem augmentation, para medir generalização à distribuição de interesse.
5. Compare o mesmo pipeline com e sem augmentation, mantendo split, modelo e métrica; registre diversidade, desempenho por subgrupo/classe e exemplos inválidos.
6. Se o método for estocástico, controle sementes e compare várias execuções quando houver orçamento suficiente.

## Quando pode ajudar
- Dados de imagem limitados, quando há transformações realistas que preservam rótulos.
- Classificação com classes raras, após comparar reamostragem, pesos de classe e ajuste de limiar com a métrica operacional apropriada.
- Regularização quando o modelo sobreajusta e as transformações representam variações que ocorrerão em uso.

## Limitações e armadilhas

- Uma transformação pode mudar o rótulo (por exemplo, inverter um sinal cuja orientação tenha significado) ou criar exemplos fisicamente impossíveis.
- Oversampling antes do split causa vazamento: cópias ou vizinhos sintéticos correlacionados podem aparecer em treino e validação.
- SMOTE pode interpolar categorias codificadas numericamente sem sentido, regiões de fronteira ou dados com estrutura temporal; variantes apropriadas ao tipo de dado são necessárias.
- Aumentar o conjunto não corrige amostragem enviesada, mudança de distribuição, erro de rótulo nem ausência de cobertura de subgrupos.
- Em regressão e séries temporais, métodos para classes minoritárias não devem ser transferidos automaticamente.
- Transformações aleatórias excessivas podem reduzir desempenho ou ensinar invariâncias erradas.

## Relações

### Diagnóstico e representação dos dados
- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]] — identifica estrutura, qualidade e segmentos onde a estratégia pode ser testada.
- [[redes/machine-learning/conceitos/Amostragem_e_Representatividade|Amostragem e Representatividade]] — augmentation não corrige amostra enviesada nem substitui cobertura da população.
- [[redes/machine-learning/conceitos/Feature_Engineering|Feature Engineering]] — transformações e representações dos dados.

### Técnicas por tipo de dado
- [[redes/machine-learning/conceitos/Imbalanced_Data|Dados desbalanceados]] — pesos, oversampling e SMOTE para tarefas de classificação.
- [[redes/machine-learning/conceitos/Extracao_de_Atributos_de_Imagens|Extração de atributos de imagens]] — transformações de imagem no pipeline de treino.
- [[redes/machine-learning/conceitos/Representacao_de_Texto_para_ML|Representação de texto para ML]] — preservação do sentido em qualquer variação textual.
- [[redes/machine-learning/conceitos/Engenharia_de_Atributos_Temporais|Engenharia de atributos temporais]] — ordem, corte de previsão e histórico disponível.
- [[redes/machine-learning/conceitos/Diagnostico_Exploratorio_de_Series_Temporais|Diagnóstico exploratório de séries temporais]] — sazonalidade, dependência e mudanças temporais que limitam transformações válidas.

### Treino e avaliação
- [[redes/machine-learning/conceitos/Pipelines_de_Feature_Engineering|Pipelines de Feature Engineering sem vazamento]] — aplicar reamostragem/transformações somente no treino.
- [[redes/machine-learning/conceitos/Cross-Validation|Cross-validation]] — validar o ganho sem contaminação entre folds.
- [[redes/machine-learning/conceitos/Selecao_de_Modelos_Orientada_pelo_EDA|Seleção de modelos orientada pelo EDA]] — comparar hipóteses e baselines.
- [[redes/machine-learning/conceitos/Overfitting_e_Underfitting|Overfitting e underfitting]] — augmentation pode atuar como regularização, mas precisa de evidência de generalização.
- [[redes/machine-learning/conceitos/Deep_Learning___Redes_Neurais|Deep Learning e redes neurais]] — família de modelos onde transformações de entrada são frequentes.
- [[redes/machine-learning/conceitos/Precision_e_Recall|Precision e Recall]], [[redes/machine-learning/conceitos/F1-Score|F1-score]] e [[redes/machine-learning/conceitos/RMSE_e_MAE|RMSE e MAE]] — métricas devem refletir a tarefa e permanecer avaliadas em dados reais.
## Evidências nas fontes consultadas

- Howard Huang, *Deep Learning with PyTorch*, 2ª ed., cap. 14: “Preventing overfitting with data augmentation” (p. 409), técnicas específicas (p. 410) e avaliação de melhoria (p. 415). O TXT extraído contém o sumário e a discussão do capítulo.
- Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*, 2ª ed., cap. 14, seção “Data Augmentation” (o TXT aponta p. 464); descreve variantes realistas e deslocamentos/flips de imagens.
- Suddhasatwa Bhaumik, *AI and ML for Coders: Applying Core ML*: trecho de `ImageDataGenerator` sobre rotação, reescala e zoom, aplicado a treino, sem página verificável no TXT.
- Peter Bruce et al., *AI-Assisted Statistics for Data Scientists*, 3ª ed., seções “Oversampling and Up/Down Weighting”, “Data Generation” e “Augmenting AI Training Data”: bootstrap, SMOTE e geração com IA, além de limitações.
- *Artificial Intelligence for Engineers*, seção 8.5: EDA textual, back translation, color augmentation e transferência neural de estilo.
- *Mastering Computer Vision with Python*: pipeline com recorte, flip, rotação e `ColorJitter`.
- *Machine Learning Hero Master Data*, seção 3.6.1: variações geométricas, fotométricas e ruído.
- Lior Gazit, *Mastering NLP: From Foundations to Agents*, seção de dados desbalanceados: oversampling, SMOTE e ADASYN.
- Howard Huang, cap. 14, exercício 14.8, sugere implementar MixUp.

As referências e passagens foram localizadas em `fontes/referencias-ia-ml/txt/`. As páginas são mantidas apenas quando identificáveis no sumário/texto extraído; conferir a edição impressa antes de citação acadêmica formal.

## Aplicação ao contexto da tese
Para a previsão de consumo diário, augmentation não deve ser tratado como etapa automática. Primeiro verificar em [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|EDA]] se o erro se concentra em períodos, níveis ou condições específicas; definir quais invariantes seriam válidas no processo de consumo; preservar ordem temporal e avaliar por partições futuras. Comparar qualquer transformação apenas contra baselines em validação temporal composta por observações reais. Não usar SMOTE sem que o problema seja reformulado como classificação com classes significativas e sem demonstrar adequação.




