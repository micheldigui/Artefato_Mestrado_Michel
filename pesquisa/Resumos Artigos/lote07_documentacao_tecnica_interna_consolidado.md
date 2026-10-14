# Resumo Consolidado — Lote 07: Documentação Técnica Interna do Projeto

## Tipo de Documentos
Este lote é composto por **13 documentos técnicos internos** gerados ao longo do desenvolvimento do projeto de Dissertação. Não são artigos científicos externos — são relatórios, especificações e sínteses produzidas pelo próprio pesquisador (ou por ferramentas de IA em suporte ao desenvolvimento). São fontes primárias de valor metodológico e arquitetural para a Dissertação.

---

## Grupo A: Documentação do Dataset

### 01 — `Análise de Relevância de Variáveis e Coluna Alvo.pdf`
**Conteúdo:** Análise técnica justificando por que `MATRÍCULA_IQ` e `TURMA` foram excluídas como features preditivas no modelo agregado diário:
- `MATRÍCULA_IQ`: identificador único — não prediz demanda agregada; foi usada para calcular `actual_demand`.
- `TURMA` (Curso/Série): potencial futuro para modelos mais granulares, mas risco de overfitting com o volume atual de dados.
- Features alternativas implementadas: `day_of_week` e `event_type` (NORMAL, FERIADO, EVENTO_ESCOLAR, PERIODO_PROVAS, FIM_DE_SEMANA).
- **Variável alvo confirmada:** `actual_demand` = total de refeições efetivamente servidas por dia.

### 02 — `Descrição das Colunas do Dataset Adaptado (dref_adaptado.csv)`
**Conteúdo:** Dicionário de dados completo do dataset base. Colunas descritas:
| Feature | Descrição |
|---------|-----------|
| `day_of_week` | Dia da semana (Seg=0, Dom=6) |
| `month`, `day_of_year` | Temporais derivadas da DATA |
| `main_dish` | TRADICIONAL / VEGETARIANO / SEM CARDAPIO |
| `max_temp_forecast` | Temperatura máxima prevista (°C) — fictícia na v1 |
| `rain_forecast` | Chuva prevista (0/1) — fictícia na v1 |
| `event_type` | NORMAL / FERIADO / EVENTO_ESCOLAR / PERIODO_PROVAS / FIM_DE_SEMANA |
| `lag_1d` a `lag_7d` | Histórico de demanda dos 7 dias anteriores |
| `actual_demand` | Variável alvo — refeições servidas no dia |

### 03 — `Documentação do Dataset Adaptado v2 (dref_adaptado_v2.csv)`
**Conteúdo:** Regras de criação da versão v2 do dataset, mais robusta:
- `actual_demand = 0` para todos os dias não letivos (fins de semana, feriados, pontes).
- Uso da biblioteca `holidays` para identificar feriados brasileiros.
- Regra de "ponte": se feriado na terça → segunda é ponte; se quinta → sexta é ponte.
- One-Hot Encoding aplicado a `main_dish` e `event_type` gerando colunas `dish_*` e `event_*`.
- Período coberto: 2023-02-06 a 2023-02-28 (fase inicial do projeto).

---

## Grupo B: Arquitetura do Sistema

### 04 — `Documentação: Integração dos Algoritmos de Predição`
**Conteúdo:** Especificação da **arquitetura desacoplada** do sistema Flask + ML:
- **Flask:** coleta dados (reservas, cardápios, eventos, clima) → SQLite.
- **`train_model.py`:** script offline que treina XGBoost e salva `.joblib`.
- **`predict_demand.py`:** carrega modelo, busca dados futuros e históricos do banco, salva previsões na tabela `predictions`.
- **`/admin/previsoes`:** nova rota Flask que exibe as previsões geradas ao administrador.
- *Nota:* Este documento descreve a versão operacional e implantável do sistema — é o produto tecnológico final da Dissertação.

### 11 — `Representação Visual do Sistema de Coleta e Predição`
**Conteúdo:** Descrição textual das interfaces do sistema Flask:
- Componentes: Aluno → Formulário de reserva; Admin → Dashboard, Importar calendário, Gerenciar cardápios, Inserir clima, Visualizar previsões.
- Mockup da tabela de previsões com colunas: Data, Demanda Prevista, Demanda Real, Versão do Modelo, Timestamp.

### 12 — `Sistema de Coleta de Dados para Predição de Demanda de Refeições`
**Conteúdo:** Manual de instalação e configuração completo do sistema Flask:
- Pré-requisitos Python, estrutura de diretórios, dependências (Flask, Flask-SQLAlchemy).
- Próximos passos: autenticação, API clima automática, deploy em produção (Gunicorn/Nginx).
- *Este é o manual do produto técnico-tecnológico da Dissertação.*

---

## Grupo C: Seleção e Síntese Bibliográfica (Fase Inicial)

### 08 — `Relatório de Novos Artigos Encontrados Online`
**Conteúdo:** Relatório de 4 novos artigos identificados com os critérios ML + Desperdício + Alimentação (2020-2025):
1. Onyeaka et al. (2025) — IA no sistema alimentar (ScienceDirect).
2. Artigo IJIRMPS (2025) — ML (XGBoost, LightGBM, SARIMA) para demand forecasting.
3. PMC/Frontiers (2025) — IA para gestão de desperdício em hotelaria (Leanpath, Winnow, Kitro).
4. Shiji Insights (2025) — Tecnologia para redução de food waste em hotéis.

### 09 — `Relatório de Seleção de Artigos`
**Conteúdo:** Metodologia de triagem aplicada às bases Scopus e WoS:
- Critérios: últimos 5 anos, ML/IA + (Previsão de Demanda OU Redução de Desperdício) + Serviços de Alimentação.
- De ~19 registros analisados, 4 foram selecionados.
- Documentação dos motivos de descarte (artigos fora do período, foco divergente, sem ML).

### 12 (Síntese) — `Síntese de Variáveis e Algoritmos dos Artigos Analisados`
**Conteúdo:** Síntese cruzada das variáveis e algoritmos identificados nos artigos selecionados:

**Variáveis Priorizadas pela Literatura:**
- Temporais: Data, Dia da Semana, Mês, Feriados, Eventos Acadêmicos.
- Histórico de Demanda: lags de dias anteriores (preditor mais forte).
- Cardápio: tipo de prato e aceitação histórica.
- Climáticas: temperatura e chuva.

**Algoritmos Mencionados:** SARIMA, Random Forest, XGBoost, LightGBM, Gradient Boosting, Deep Learning (genérico).

---

## Grupo D: Recomendações Técnicas

### 05 — `Lista de Tarefas - Recomendações de Variáveis e Algoritmos`
**Conteúdo:** Checklist interno confirmando que as tarefas de análise, síntese e recomendação foram cumpridas (001 a 007, todos marcados como [x]).

### 06 — `Recomendações de Algoritmos de Machine Learning para Predição`
**Conteúdo:** Recomendações formais de algoritmos para o contexto IFSP-ITQ:
- **Tier 1 (Mais Promissores):** XGBoost, LightGBM, Random Forest.
- **Tier 2 (Baseline/Complementar):** SARIMA, Prophet.
- **Tier 3 (Apenas se necessário):** LSTM/Redes Neurais (exige mais dados e recursos).
- **Estratégia sugerida:** Árvores primeiro → SARIMA como baseline → LSTM se necessário.

### 07 — `Recomendações de Variáveis Adicionais para Predição de Demanda`
**Conteúdo:** Matriz de priorização de variáveis para o IFSP:
- **Altamente Recomendadas:** Histórico de Demanda Agregada, Dia da Semana, Calendário Acadêmico/Eventos, Cardápio.
- **Recomendadas:** Temperatura máxima prevista, Previsão de chuva, Número de alunos esperados.
- **Menor Prioridade Inicial:** Turno do aluno.

### 10 — `Relatório de Recomendações: Variáveis e Algoritmos para Predição`
**Conteúdo:** Relatório consolidado reunindo as recomendações dos documentos 06 e 07 em formato de relatório formal para o IFSP-ITQ.

---

## ✅ Síntese Global do Lote 07

**Natureza:** Documentação técnica interna, não artigos científicos. Constituem o **registro histórico do pipeline de desenvolvimento** do projeto entre 2023-2025.

**Valor para a Dissertação:**
- **Capítulo de Metodologia:** Os documentos 01-03 (dicionário de dados, regras do dataset) e 04 (arquitetura Flask+ML) são a base para descrever o "produto tecnológico" desenvolvido.
- **Capítulo de Revisão Bibliográfica:** Os documentos 08-09-12 registram a metodologia de seleção de artigos e podem ser referenciados na seção de Método de Pesquisa.
- **Capítulo de Referencial Teórico:** Os documentos 06-07-10 (recomendações de variáveis e algoritmos) validam internamente as escolhas metodológicas antes mesmo de o pesquisador ter implementado os modelos avançados.

**Pertinência:** Alta como registro interno do desenvolvimento; não requerem resumos individuais para a seção de Referências da Dissertação.
