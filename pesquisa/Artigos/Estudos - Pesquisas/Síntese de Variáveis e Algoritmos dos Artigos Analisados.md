---
source_file: "Síntese de Variáveis e Algoritmos dos Artigos Analisados.pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Síntese de Variáveis e Algoritmos dos Artigos Analisados.pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "9fffc8f47b4020bcbf49f16f54800030d482d3c05a0817041826ba3111888a5c"
extracted_at: "2026-09-20T00:55:17.225816"
---

## Síntese de Variáveis e Algoritmos dos Artigos Analisados

## Variáveis Relevantes para Predição de Demanda (Identificadas/Implícitas nos Artigos)

Com base na análise dos relatórios ( relatorio\_selecao\_artigos.md , relatorio\_novos\_artigos.md ) e nos resumos/palavras-chave dos artigos selecionados, as seguintes categorias de variáveis são frequentemente consideradas importantes para a predição de demanda de refeições e gestão de desperdício:

## Dados Temporais: 1.

- Data da Refeição: (Já coletada) Essencial para identificar padrões sazonais e tendências. ◦
- Dia da Semana: Padrões de consumo podem variar significativamente entre dias úteis e fins de semana (se aplicável). ◦
- Período do Ano/Mês: Sazonalidade (ex: meses mais quentes/frios, proximidade de férias). ◦
- Datas Especiais/Feriados: Feriados nacionais, locais ou acadêmicos que impactam a presença dos alunos. ◦
- Eventos Acadêmicos: Semanas de provas, eventos especiais no campus, início/fim de semestre. ◦
- Histórico de Demanda: Quantidade de refeições servidas/reservadas em dias/períodos anteriores é um dos preditores mais fortes. ◦

## Dados dos Alunos/Consumidores: 2.

- Identificação do Aluno: (Já coletada) Permite analisar padrões individuais, embora a predição agregada seja o objetivo principal. ◦
- Série/Ano: (Já coletada) Pode haver diferenças de padrão entre séries. ◦
- Curso: (Já coletado) Diferentes cursos podem ter horários ou culturas distintas que afetam a demanda por refeições. ◦
- Histórico de Reservas/Consumo Individual: Se disponível e permitido, pode refinar a predição. ◦
- Número Total de Alunos Matriculados/Elegíveis: Define o universo potencial de consumidores. ◦
- Dados Demográficos Agregados (se disponíveis e relevantes): Ex: Turno (manhã, tarde, noite). ◦

## Dados da Refeição/Menu: 3.

- Tipo de Refeição: Almoço, jantar, lanche (se houver variação). ◦
- Cardápio Específico: A popularidade de certos pratos pode influenciar a demanda no dia em que são servidos. Histórico de aceitação de pratos. ◦
- Preço (se aplicável): Embora no caso do IFSP possa ser subsidiado, variações de custo (se existirem) podem impactar. ◦

## Fatores Externos: 4.

- Condições Climáticas: Temperatura, chuva (podem influenciar a decisão de comer no campus vs. fora). ◦
- Eventos Locais (fora do campus): Eventos na cidade que possam atrair os alunos. ◦
- Dados Operacionais (Mencionados mais para gestão/desperdício, mas podem correlacionar com demanda): 5.
- Níveis de estoque (menos direto para predição de demanda inicial). ◦
- Dados de desperdício real (feedback para ajustar modelos futuros). ◦

## Algoritmos de Machine Learning Mencionados

Os artigos e publicações analisados mencionam uma variedade de técnicas, desde abordagens gerais até algoritmos específicos:

## Termos Gerais: ·

- Machine Learning (ML) ◦
- Artificial Intelligence (AI) ◦
- Predictive Analytics ◦
- Data Mining ◦
- Modelos de Séries Temporais: ·
- SARIMA (Seasonal Autoregressive Integrated Moving Average): Explicitamente mencionado no artigo do IJIRMPS. ◦
- Modelos de Regressão/Classificação (Supervisionados): ·
- Random Forest: Mencionado no artigo sobre tecnologias eficientes. ◦
- XGBoost (Extreme Gradient Boosting): Mencionado no artigo do IJIRMPS. ◦
- LightGBM (Light Gradient Boosting Machine): Mencionado no artigo do IJIRMPS. ◦
- Gradient Boosting (Geral): Mencionado no artigo do IJIRMPS. ◦
- Support Vector Machines (SVM): Incluído nas palavras-chave gerais de ML. ◦

## Redes Neurais / Deep Learning: ·

- Mencionado nos highlights do artigo da ScienceDirect, mas sem detalhamento específico nos trechos analisados. ◦

## Outros: ·

- Algoritmos não especificados (mencionados genericamente). ◦

Esta síntese servirá de base para as próximas etapas de recomendação.