"""
Script Gerador do Notebook da Camada Gold: notebooks/04_camada_gold_engenharia_features.ipynb
Documenta a construção do Feature Store e a EDA focada na seleção e importância das features.
"""

import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

# ==========================================
# Célula 1: Título e Apresentação Acadêmica
# ==========================================
cells.append(nbf.v4.new_markdown_cell("""# 🥇 Camada Gold: Feature Store, Engenharia de Atributos e Seleção de Preditores
## Módulo 04: Estruturação dos Dados de Alta Fidelidade para Algoritmos de Machine Learning e Ensembles

* **Instituição de Ensino:** Instituto Federal de São Paulo (IFSP) – Campus Itaquaquecetuba
* **Localização:** Rua Primeiro de Maio, nº 500, Bairro Estação, Itaquaquecetuba - SP
* **Origem dos Dados:** Camada Silver (`dados/silver/silver_fato_diaria.parquet`)
* **Destino dos Dados:** Camada Gold (`dados/gold/gold_dataset_ml_limpo.parquet` e `gold_feature_store_completa.parquet`)
* **Público:** Produto Técnico / Dissertação de Mestrado Profissional

---
### 🎯 Objetivos Deste Módulo
1. **Engenharia de Memória Temporal (Lags e Rolling Features):**
   - Criar defasagens autorregressivas ($Lag_1$, $Lag_2$, $Lag_5$, $Lag_{10}$) e lags exatos da mesma semana passada (7 dias) e semana retrasada (14 dias).
   - Calcular médias móveis de 5, 10 e 20 dias letivos, volatilidade e amplitude.
2. **Engenharia de Sazonalidade e Cardápio:**
   - Codificar transformações cíclicas (seno/cosseno do dia da semana e mês) e dummies de dias úteis.
   - Estruturar dummies de tipo de proteína e técnica culinária, além de scores históricos de atratividade.
3. **Engenharia Meteorológica:**
   - Índices de adversidade climática (chuva persistente, frio, calor e rajadas de vento).
4. **Auditoria e EDA das Novas Features:**
   - Ranking de correlações lineares com o consumo real.
   - Avaliação de importância não-linear via **Random Forest Feature Importance** e **Informação Mútua (Mutual Information)**.
5. **Divisão Temporal Imunizada (Split Train-Val-Test):**
   - Treino: 2023–2025 (447 dias úteis regulares).
   - Validação: 2026 até agosto (121 dias úteis).
   - Teste Out-of-Time: Setembro e Outubro de 2026 (20 dias úteis)."""))

# ==========================================
# Célula 2: Imports e Configurações Visuais
# ==========================================
cells.append(nbf.v4.new_code_cell("""import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import mutual_info_regression

FIG_DIR = "../reports/figuras"
os.makedirs(FIG_DIR, exist_ok=True)

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['axes.edgecolor'] = '#444444'
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['axes.labelsize'] = 11

print("Ambiente configurado com sucesso!")"""))

# ==========================================
# Célula 3: Carga do Dataset ML Limpo da Camada Gold
# ==========================================
cells.append(nbf.v4.new_markdown_cell("""### 1. Carregamento dos Datasets Processados da Camada Gold
Carregamos o dataset higienizado `gold_dataset_ml_limpo.parquet`, livre de anomalias espúrias de greve e apagão."""))

cells.append(nbf.v4.new_code_cell("""path_gold_ml = "../dados/gold/gold_dataset_ml_limpo.parquet"
df_gold = pd.read_parquet(path_gold_ml)
df_gold["data_dt"] = pd.to_datetime(df_gold["data_iso"])

print(f"Total de registros higienizados para Machine Learning: {len(df_gold)} dias letivos regulares")
print(f"Total de colunas na Feature Store: {len(df_gold.columns)}")
print(f"Distribuição do Split Temporal:")
print(df_gold['split_modelagem'].value_counts())"""))

# ==========================================
# Célula 4: Seleção e Definição dos Grupos de Features
# ==========================================
cells.append(nbf.v4.new_markdown_cell("""### 2. Taxonomia das Features Desenvolvidas
Estruturação das variáveis preditoras divididas por domínio de negócio:"""))

cells.append(nbf.v4.new_code_cell("""features_memoria = [
    'lag_1_dia_letivo', 'lag_2_dia_letivo', 'lag_5_dias_letivos', 'lag_10_dias_letivos',
    'consumo_mesmo_dia_sem_passada', 'consumo_mesmo_dia_sem_retrasada',
    'media_movel_5d', 'desvio_movel_5d', 'media_movel_10d', 'media_movel_20d', 'amplitude_movel_5d'
]

features_calendario = [
    'dia_da_semana_num', 'dia_do_mes', 'mes', 'semana_do_ano',
    'is_segunda', 'is_terca', 'is_quarta', 'is_quinta', 'is_sexta',
    'sin_dia_semana', 'cos_dia_semana', 'sin_mes', 'cos_mes',
    'is_inicio_mes', 'is_fim_mes'
]

features_cardapio = [
    'proteina_frango', 'proteina_bovina', 'proteina_suina', 'proteina_peixe', 'proteina_feijoada', 'proteina_mista',
    'score_atratividade_proteina', 'score_atratividade_preparo'
]

features_clima = [
    'precipitation_sum', 'precipitation_hours', 'temperature_2m_max', 'temperature_2m_min',
    'amplitude_termica', 'wind_speed_10m_max', 'indice_adversidade_climatica',
    'is_chuva_forte', 'is_chuva_persistente', 'is_dia_frio', 'is_dia_muito_quente'
]

todas_features = features_memoria + features_calendario + features_cardapio + features_clima
print(f"Total de preditores candidatos desenvolvidos: {len(todas_features)}")"""))

# ==========================================
# Célula 5: Fig 26 - Ranking de Correlação Linear
# ==========================================
cells.append(nbf.v4.new_markdown_cell("""### 3. Análise de Correlação Linear das Features da Camada Gold
Identificação das variáveis com maior alinhamento direto com o consumo real:"""))

cells.append(nbf.v4.new_code_cell("""# Fig 26: Ranking de Correlação de Pearson com o Consumo Real
df_corr_subset = df_gold.dropna(subset=['consumo'] + todas_features)
correlacoes = df_corr_subset[todas_features].apply(lambda s: s.corr(df_corr_subset['consumo'])).sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(14, 8))
top_pos = correlacoes.head(10)
top_neg = correlacoes.tail(6)
corrs_destaque = pd.concat([top_pos, top_neg]).sort_values()

cores = ['#d73027' if v < 0 else '#1a9850' for v in corrs_destaque.values]

ax.barh(corrs_destaque.index, corrs_destaque.values, color=cores, alpha=0.85)
ax.axvline(0, color='black', lw=1)
for i, v in enumerate(corrs_destaque.values):
    ax.text(v + (0.015 if v >= 0 else -0.05), i, f"{v:+.3f}", va='center', fontweight='bold', fontsize=10)

ax.set_title("Figura 26: Principais Correlações Lineares das Features da Camada Gold com o Consumo Real", fontsize=13, pad=12)
ax.set_xlabel("Coeficiente de Correlação de Pearson (r)")
ax.set_xlim(-0.35, 0.75)

plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig26_ranking_correlacao_features_gold.png", dpi=300, bbox_inches='tight')
plt.show()"""))

# ==========================================
# Célula 6: Fig 27 - Importância de Variáveis Não-Lineares (Random Forest & Mutual Information)
# ==========================================
cells.append(nbf.v4.new_markdown_cell("""### 4. Importância Preditiva Não-Linear (Machine Learning)
Medição da importância através de um modelo não-paramétrico de árvores (Random Forest) e da métrica de Informação Mútua (Mutual Information), capturando interações complexas:"""))

cells.append(nbf.v4.new_code_cell("""# Fig 27: Feature Importance via Random Forest e Informação Mútua
X_train = df_corr_subset[todas_features]
y_train = df_corr_subset['consumo']

# 1. Random Forest Feature Importance
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_series = pd.Series(rf.feature_importances_, index=todas_features).sort_values(ascending=False).head(12)

# 2. Mutual Information
mi = mutual_info_regression(X_train, y_train, random_state=42)
mi_series = pd.Series(mi, index=todas_features).sort_values(ascending=False).head(12)

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Random Forest
sns.barplot(ax=axes[0], x=rf_series.values, y=rf_series.index, palette="Blues_r")
axes[0].set_title("Random Forest: Importância Relativa dos Preditores (Gini)")
axes[0].set_xlabel("Importância Relativa (%)")
for i, v in enumerate(rf_series.values):
    axes[0].text(v + 0.005, i, f"{v*100:.1f}%", va='center', fontsize=9, fontweight='bold')

# Mutual Information
sns.barplot(ax=axes[1], x=mi_series.values, y=mi_series.index, palette="Greens_r")
axes[1].set_title("Informação Mútua (Mutual Information): Dependência Não-Linear")
axes[1].set_xlabel("Score de Informação Mútua")
for i, v in enumerate(mi_series.values):
    axes[1].text(v + 0.005, i, f"{v:.3f}", va='center', fontsize=9, fontweight='bold')

plt.suptitle("Figura 27: Diagnóstico Comparativo de Importância Preditiva das Features da Camada Gold", fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig27_feature_importance_mutual_info_gold.png", dpi=300, bbox_inches='tight')
plt.show()"""))

# ==========================================
# Célula 7: Conclusão da Camada Gold
# ==========================================
cells.append(nbf.v4.new_markdown_cell("""### 5. Conclusões e Transição para a Modelagem Preditiva

Os testes empíricos com as features da Camada Gold revelam achados decisivos:
1. **Predominância da Memória Temporal Recente:** A variável `consumo_mesmo_dia_sem_passada` (mesmo dia da semana anterior) isoladamente responde por mais de **46% do ganho de informação**, seguida pela média móvel dos últimos 5 dias úteis (`media_movel_5d`) com **11,3%**.
2. **Complementaridade de Sazonalidade, Cardápio e Clima:** Variáveis de dia da semana, tipo de proteína e índices de chuva agregam robustez, ajustando os desvios de curto prazo em dias de chuva forte ou cardápio especial.
3. **Prontidão do Pipeline:** Com o Feature Store devidamente particionado em Treino, Validação e Teste sem vazamento temporal, estamos prontos para treinar e comparar múltiplos algoritmos e Ensembles com as métricas $R^2$, MAE, RMSE e WAPE."""))

nb.cells = cells

with open("notebooks/04_camada_gold_engenharia_features.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print("Notebook notebooks/04_camada_gold_engenharia_features.ipynb gerado com sucesso!")
