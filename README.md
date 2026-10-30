# 🍽️ Artefato Analítico-Preditivo para Planejamento da Produção de Refeições e Combate ao Desperdício

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![DSR](https://img.shields.io/badge/Metodologia-Design_Science_Research_(DSR)-orange.svg)](docs/trajetoria_do_artefato.md)
[![PPG-GTSP](https://img.shields.io/badge/Programa-PPG--GTSP-green.svg)](https://posgraduacao.cps.sp.gov.br/)
[![Corte Qualificação](https://img.shields.io/badge/Qualificação-31%2F08%2F2026%20(N%3D73)-purple.svg)](dissertacao/AUDITORIA_QUALIFICACAO_RECALCULO_N73.md)
[![Licença](https://img.shields.io/badge/Licença-MIT-lightgrey.svg)](LICENSE)

> **Pesquisa de Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)**  
> **Área de Concentração:** Sistemas Produtivos  
> **Linha de Pesquisa:** Linha 2 — Sistemas de Informação e Tecnologias Digitais  
> **Autor / Mestrando:** Michel Silva de Souza  
> **Orientador:** Prof. Dr. Carlos Hideo Arima  
> **Coorientador:** Prof. Dr. Rafael Nobre Orsi  
> **Campo de Aplicação Empírica:** Restaurante Estudantil de Instituição Pública de Ensino Federal (Anonimizado — LGPD)  
> **Abordagem Metodológica:** Design Science Research (DSR)  

---

## 📌 Visão Geral do Projeto

Este repositório contém o código-fonte, dados tratados, cadernos de experimentação, visualizações em alta resolução e o artefato computacional preditivo desenvolvido para apoiar o planejamento de compras e preparo de refeições no restaurante estudantil de uma **Instituição Pública de Ensino Federal**.

O projeto resolve o problema da **assimetria informacional e descompasso entre demanda e oferta** no restaurante estudantil gratuito:
1. **Regime Histórico de Reservas Discentes (2023 a 2025):** Formulários voluntários preenchidos pelos estudantes apresentaram descontinuidade funcional, gerando alto índice de déficit potencial (63,8% dos dias com falta de reservas e MAE de 27,10 ref/dia).
2. **Regime Institucional da Nutricionista (2026):** Estimativa empírica fixa baseada em experiência clínica, resultando em sobreoferta preventiva para evitar desabastecimento (saldo de +1.898 refeições em 123 datas e MAE de 26,21 ref/dia).
3. **Solução Desenvolvida (Artefato com IA Híbrida e Margens Conformal):** Combina modelos supervisionados multivariados em duas janelas temporais ($t+1$ e $t+2$), calibração de incerteza não-paramétrica (*Conformal Prediction*) e modelo híbrido decisório (50% IA + 50% Nutricionista), alcançando o menor erro absoluto médio do projeto (**MAE de 20,20 ref/dia**) com mínima taxa de descarte.

---

## 🏛️ Metodologia e Arquitetura do Artefato

A pesquisa adota a metodologia **Design Science Research (DSR)** (Peffers et al., 2007), estruturada em seis etapas rigorosas:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ 1. Identificação│ ──> │ 2. Definição de │ ──> │ 3. Projeto e    │
│    do Problema  │     │    Objetivos    │     │    Construção   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                         │
┌─────────────────┐     ┌─────────────────┐              ▼
│ 6. Comunicação  │ <── │ 5. Avaliação    │ <── ┌─────────────────┐
│    e Defesa     │     │    Experimental │     │ 4. Demonstração │
└─────────────────┘     └─────────────────┘     │    Operacional  │
                                                └─────────────────┘
```

### Arquitetura de Dados (Medallion)
* **Camada Bronze (Raw Data):** Consumo verificado da catraca biométrica, formulários de reservas do SUAP, cardápios digitalizados (proteínas e preparos), calendários letivos e dados meteorológicos da API pública **Open-Meteo**.
* **Camada Silver (Harmonização):** Padronização temporal diária, tratamento de nulos, isolamento de feriados/emendas e auditoria de qualidade cadastral (`silver_fato_diaria.parquet`).
* **Camada Gold (Feature Store):** Engenharia de 106 atributos explicativos com zero vazamento (*lags* 1 a 10 dias, médias móveis 5d/10d, scores de atratividade de pratos, ciclos trigonométricos de calendário e índices de adversidade climática).

### Horizontes Operacionais de Decisão
* **Horizonte $t+2$ (Compras de Secos / 10 a 14 dias de antecedência):** Previsão puramente autônoma baseada em calendário, inércia de demanda e previsão climática estendida (Open-Meteo).
* **Horizonte $t+1$ (Preparo e Perecíveis / 3 a 7 dias de antecedência):** Previsão refinada na sexta-feira anterior via *re-forecast*, incorporando o quantitativo fornecido pela nutricionista institucional.

---

## 📊 Principais Resultados da Qualificação (Corte em 31/08/2026)

Conforme laudo formal de auditoria ([`AUDITORIA_QUALIFICACAO_RECALCULO_N73.md`](dissertacao/AUDITORIA_QUALIFICACAO_RECALCULO_N73.md)), a dissertação adota corte temporal em **31 de agosto de 2026**, preservando quatro recortes de análise:

### 1. Confronto Consolidado dos Regimes Operacionais
| Regime / Abordagem | Período / Amostra | Sobra Potencial (ref.) | Déficit Potencial (ref.) | % Dias com Falta | MAE (ref./dia) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Reservas dos Alunos (Histórico)** | 2023 a 2025 ($N=458$) | 2.916 | 9.494 | 63,8% | 27,10 |
| **Censo Nutricionista (2026)** | Fev–Ago/2026 ($N=123$) | 2.561 | 663 | 39,0% | 26,21 |
| **Nutricionista Isolada (Pareado)** | Coorte 2026 ($N=73$) | 1.198 | 508 | 43,8% | 23,37 |
| **IA Pura — Ridge $t+1$ (Pareado)** | Coorte 2026 ($N=73$) | 1.046 | 535 | 43,8% | 21,67 |
| **Modelo Híbrido 50/50 (Ótimo)** | Coorte 2026 ($N=73$) | **1.037** | **437** | **45,2%** | **20,20** |
| **IA + Conformal P85 (+18 ref)** | Coorte 2026 ($N=73$) | 1.994 | **167** | **15,1%** | 29,62 |

> *Nota metodológica:* Sobras e déficits representam desvios potenciais de planejamento em relação à catraca e não equivalem a descarte físico de alimentos ou falta real de atendimento.

### 2. Políticas de Margem de Segurança Decisória (N=73)
* **IA Pura (Ridge):** Equilíbrio preditivo com MAE de 21,67 e viés central controlado.
* **Conformal P75 (+10 ref):** Reduz a taxa de dias com falta para 24,7%.
* **Conformal P85 (+18 ref):** Proporciona **84,9% de índice de proteção estudantil**, restringindo os dias de déficit a apenas 15,1%.
* **Conformal P90 (+29 ref):** Política de segurança máxima para semanas críticas (apenas 11,0% de dias com falta).
* **Modelo Híbrido 50/50:** Menor volume acumulado de desperdício financeiro (R$ 8.818,54 de sobra acumulada) com o menor erro diário global.

---

## 🗂️ Estrutura do Repositório

```text
ARTEFATO/
├── dados/
│   ├── bronze/                   # Dados brutos originais (consumo, reservas, cardápios, clima)
│   ├── silver/                   # Tabelas tratadas e fatos diários (silver_fato_diaria.parquet)
│   └── gold/                     # Feature store ML e resultados consolidados dos experimentos
├── dissertacao/
│   ├── AUDITORIA_QUALIFICACAO_RECALCULO_N73.md  # Laudo técnico e pericial de recálculos
│   ├── INVENTARIO_SINCRONIZACAO_QUALIFICACAO.md # Inventário completo de sincronização
│   ├── figuras/                  # 28 figuras oficiais da dissertação em 300 DPI (sem duplicatas)
│   ├── recalculos_qualificacao_20260831/        # CSVs auditados com métricas oficiais (N=73)
│   └── backup_antes_sincronizacao_20261014/    # Cópias de segurança prévias à limpeza
├── docs/                         # Catálogo de referências ABNT e memoriais técnicos
├── notebooks/                    # Cadernos Jupyter numerados em ordem de execução:
│   ├── 01_coleta_clima_api.ipynb
│   ├── 02_camada_silver_qualidade_dados.ipynb
│   ├── 03_analise_exploratoria_eda.ipynb
│   ├── 04_camada_gold_engenharia_features.ipynb
│   ├── 05_modelagem_cenarios_e_algoritmos.ipynb
│   ├── 06_avaliacao_visual_e_comparativo_modelos.ipynb
│   ├── 07_experimentos_janelas_temporais_e_habitos.ipynb
│   ├── 08_margem_seguranca_e_modelo_hibrido.ipynb
│   ├── 09_analise_efeito_compensatorio_e_regimes.ipynb
│   └── 10_geracao_figuras_dissertacao.ipynb
├── reports/                      # Relatórios, tabelas exportadas e gráficos temáticos
├── src/
│   ├── app/                      # Interface operacional interativa em Streamlit
│   ├── gerar_todas_figuras_dissertacao.py  # Script gerador oficial das figuras 07 a 28
│   └── exportar_tabelas_resultados.py      # Consolidador oficial de tabelas e métricas
├── executar_app.py               # Launcher da aplicação web de apoio à decisão
└── requirements.txt              # Dependências do ecossistema Python
```

---

## 🚀 Como Reproduzir o Projeto

### 1. Pré-requisitos
* Python 3.12+ instalado ([python.org](https://www.python.org/))
* Git instalado

### 2. Clonagem e Instalação do Ambiente
```bash
# Clonar o repositório
git clone https://github.com/micheldigui/Artefato_Mestrado_Michel.git
cd Artefato_Mestrado_Michel

# Criar e ativar ambiente virtual
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Linux/macOS:
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Execução dos Experimentos e Geração de Resultados
```bash
# 1. Exportar e consolidar tabelas oficiais auditadas (N=73)
python src/exportar_tabelas_resultados.py

# 2. Gerar todas as 28 figuras oficiais da dissertação em 300 DPI
python src/gerar_todas_figuras_dissertacao.py
```

### 4. Execução dos Cadernos Jupyter
Os cadernos em `notebooks/` podem ser executados sequencialmente (`02` a `10`) via Jupyter Lab, Jupyter Notebook ou VS Code:
```bash
jupyter lab
```

### 5. Execução do Aplicativo Interativo de Decisão (Streamlit)
Para testar a interface do artefato voltada à nutricionista e equipe gestora:
```bash
python executar_app.py
```
Acesse a aplicação no navegador em `http://localhost:8501`.

---

## 📄 Referências e Documentação Adicional

* **Memorial de Trajetória do Artefato:** [`docs/trajetoria_do_artefato.md`](docs/trajetoria_do_artefato.md)
* **Formulação Matemática e Margens de Segurança:** [`docs/referencias_margens_seguranca_e_modelagem.md`](docs/referencias_margens_seguranca_e_modelagem.md)
* **Catálogo ABNT (NBR 6023:2018):** [`docs/catalogo_referencias_academicas_abnt.md`](docs/catalogo_referencias_academicas_abnt.md)
* **Laudo Técnico Pericial de Qualificação:** [`dissertacao/AUDITORIA_QUALIFICACAO_RECALCULO_N73.md`](dissertacao/AUDITORIA_QUALIFICACAO_RECALCULO_N73.md)

---

## 👤 Equipe da Pesquisa e Contato
 
* **Mestrando / Autor:** Michel Silva de Souza  
* **Orientador:** Prof. Dr. Carlos Hideo Arima  
* **Coorientador:** Prof. Dr. Rafael Nobre Orsi  
* **Programa:** Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)  
* **GitHub:** [@micheldigui](https://github.com/micheldigui)  
* **Repositório Oficial:** [Artefato_Mestrado_Michel](https://github.com/micheldigui/Artefato_Mestrado_Michel)
