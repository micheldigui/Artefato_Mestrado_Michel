# Análise Sintópica: Lote 01 - Fundamentação do Sistema de Predição em Redes Alimentares

## 1. Definição do Problema e Terminologia Comum
Os autores (Onyeaka, 2025; Olawale, 2025; Clark, 2025) convergem na magnitude do problema: 1/3 da comida produzida mundialmente é desperdiçada, gerando custos trilionários e emissões massivas de CO2 (3.3 Gt anuais). 
- **Olawale (2025)** estabelece uma distinção crucial entre *Post-harvest losses* (falhas estruturais) e *Food Waste* (decisões de consumo), situando o projeto do Restaurante Universitário (RU) firmemente na categoria de **Food Waste**.
- **Chaudhari (2025)** e **Clark (2025)** identificam a **imprevisibilidade da demanda** como o driver primário do desperdício em cafeterias e serviços de refeições coletivas.

## 2. Convergência Metodológica (Machine Learning)
Há um consenso sobre a superioridade de modelos não-lineares frente aos métodos estatísticos tradicionais (como Regressão Linear Simples):
- **Boosting**: Chaudhari (2025) valida o **LightGBM** e o **XGBoost** como os mais eficazes para séries temporais de refeições.
- **Deep Learning**: Onyeaka (2025) e Olawale (2025) recomendam **LSTMs** quando há forte dependência de variáveis contextuais (clima e sazonalidade), o que justifica os testes realizados nos notebooks `07e` a `07i`.
- **Ensemble**: Rajendran (2025) destaca o **Random Forest** como modelo robusto para prever intenções subjetivas e lidar com dados psicográficos da comunidade.

## 3. Variáveis Críticas (Predictores)
Cruzando as visões, as variáveis essenciais para um modelo resiliente de RU são:
1. **Histórico de Consumo e Reservas** (Chaudhari, 2025).
2. **Dados Exógenos (Clima e Eventos)**: Olawale (2025) e Onyeaka (2025) provam que temperatura e umidade afetam a perecibilidade e a preferência alimentar.
3. **Engenharia de Lag**: Uso de *lag features* e Médias Móveis (EWMA) para capturar tendências de curto prazo (Chaudhari, 2025).

## 4. O "Gap" e a Contribuição do Artefato (DSR)
A literatura foca majoritariamente em cozinhas comerciais (hotéis e delivery). O projeto do RU introduz a **Sazonalidade Acadêmica Reunitiva** (Calendário Acadêmico) como fator determinante, um elemento menos explorado nos textos globais de 2025, o que confere ao trabalho do usuário o caráter de **Originalidade e Rigor** exigidos no mestrado.

## 5. Conclusão para o Seminário
A base teórica auditada fornece uma "Justificativa de Ouro": a aplicação de IA via DSR não é apenas uma melhoria técnica, mas uma necessidade de **Sustentabilidade (ESG)**, com potencial de reduzir perdas em cozinhas institucionais em até **50-53%** (baseado nos dados de Winnow e Leanpath citados por Clark, 2025).
