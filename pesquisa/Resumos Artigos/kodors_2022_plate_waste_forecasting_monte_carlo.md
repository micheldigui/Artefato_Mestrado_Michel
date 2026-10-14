# Resumo de Artigo Científico: Kodors et al. (2022)

## Referência Completa
**Autores:** Kodors, S.; Zvaigzne, A.; Litavniece, L.; Lonska, J.; Silicka, I.; Kotane, I.; Deksne, J.
**Título:** Plate Waste Forecasting Using the Monte Carlo Method for Effective Decision Making in Latvian Schools.
**Ano:** 2022
**Journal:** Nutrients, Vol. 14(587).
**DOI:** [10.3390/nu14030587](https://doi.org/10.3390/nu14030587)
**Caminho Local:** `d:\PROJETOS\PRODUTO_MESTRADO\docs\artigos\Novos Artigos\wos\out (1).pdf`

## Resumo
Este estudo na Letônia propôs a criação de um "Sistema de Previsão Dirigida a Dados" para antecipar a geração de sobras nos refeitórios de escolas secundárias. Pela enorme dificuldade de obter dados na época (devido às restrições em escolas geradas pela COVID-19), impossibilitando o treino de algoritmos reais de *Machine Learning*, os autores recorreram a um **Simulador Numérico de Monte Carlo**, alimentado marginalmente por pesquisas genéricas com pais de alunos, para tentar prever artificialmente a demanda, obtendo uma taxa de erro de previsão de ~10% (MAPE).

## Principais Tópicos
- **Abordagem Feature-based Sintética:** Quando faltam dados estatísticos consolidados de fluxo de caixa ou de balanças empíricas, simuladores estatísticos puros (como o método de Monte Carlo) podem forçar o cômputo e criar "Gêmeos Digitais" da operação para o diretor.
- **Ecossistema Fechado:** As cantinas de escolas e campi universitários são, do ponto de vista algorítmico, o ambiente perfeito e "controlado" para disparos de otimização contínua rumo ao Zero *Food Waste*.

## Conclusão
Tecnologias de previsão (Forecasting) podem e devem atuar como o pilar de tomada de decisões de gestores de restaurantes de massa.

## Pertinência para o Projeto
**Alta.** Você utilizará esse artigo no seu seminário para justificar a superioridade evolutiva da sua dissertação! Os autores (Kodors, 2022) precisaram montar uma predição cega (simulação artificial de Monte Carlo) porque não tinham um dataset massivo dos alunos no refeitório por problemas de acesso pela Covid. A sua pesquisa de Mestrado soluciona e supera essa dor metodológica diretamente: usando o Histórico Real de catracas e lixo e aplicando Algoritmos Supervisionados robustos (Tree-Based), seu projeto eleva o rigor que esse estudo de 2022 tentou, mas empacou pela falta de base de dados massiva.
