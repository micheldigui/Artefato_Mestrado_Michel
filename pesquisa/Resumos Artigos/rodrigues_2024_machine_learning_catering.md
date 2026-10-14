# Resumo de Artigo Científico: Rodrigues et al. (2024)

## Referência Completa
**Autores:** Rodrigues, M.; Miguéis, V.; Freitas, S.; Machado, T.
**Título:** Machine learning models for short-term demand forecasting in food catering services: A solution to reduce food waste.
**Ano:** 2024
**Journal:** Journal of Cleaner Production, Vol. 435, 140265.
**DOI:** [10.1016/j.jclepro.2023.140265](https://doi.org/10.1016/j.jclepro.2023.140265)
**Caminho Local:** `d:\PROJETOS\PRODUTO_MESTRADO\docs\artigos\Novos Artigos\wos\1-s2.0-S0959652623044232-main.pdf`

## Resumo
A pesquisa propõe soluções baseadas em Machine Learning (ML) para a previsão de demanda de curto prazo (dia seguinte) no setor de serviços de alimentação (incluindo restaurantes universitários), visando combater a superprodução. O estudo baseia-se em dados de três cantinas e estuda a eficácia de algoritmos avançados para obter reduções acionáveis de desperdício sem aumentar o risco de falta de refeições (underproducing).

## Principais Tópicos
- **Modelos Testados:** Foram testadas duas abordagens *Causais* (Random Forest e LightGBM) e duas de *Séries Temporais* (Rede Neural LSTM e Transformers).
- **Variáveis (Features):** Uso intenso de variáveis externas como o menu do dia, feriados e dias de eventos acadêmicos atípicos (ex: semana "Queima das Fitas" em Portugal).
- **Resultados de Destaque:** Os modelos **Random Forest (RF)** e **LSTM** produziram as melhores previsões. A aplicação das previsões resultaria em uma redução do desperdício de refeições de **14% a 52%**, além de reduzir a demanda não atendida (falta de comida) em até 16% quando comparado com estimativas manuais de gerentes.

## Conclusão
Previsões de demanda auxiliadas por Machine Learning (especialmente Random Forest e Redes Neurais Long Short-Term Memory) superam enormemente processos empíricos (como adicionar 10% de margem de segurança no preparo), otimizando severamente as áreas ambiental e econômica de RUs.

## Pertinência para o Projeto
**Essencial.** O nível de correlação com a metodologia da sua dissertação é de quase 100%. Os autores também utilizam modelos de Boosting (como LightGBM e XGBoost avaliados no seu projeto) e validam redes neurais (LSTM). Apresenta estatísticas claras do benefício prático (redução de 50%+ em sobras) que você pode citar na justificativa do seu projeto.
