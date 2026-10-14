"""
Gera a Figura 25: Estrutura de Dependência Temporal e Memória Histórica do Consumo de Refeições
Salva em reports/figuras/fig25_autocorrelacao_memoria_temporal.png
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Arial'

df = pd.read_parquet('dados/silver/silver_fato_diaria.parquet')
df_c = df[df['consumo'].notna()].sort_values('data_iso').copy()

df_c['lag_1'] = df_c['consumo'].shift(1)
df_c['lag_5'] = df_c['consumo'].shift(5)
df_c['media_movel_5d'] = df_c['consumo'].rolling(5).mean().shift(1)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

corr_lag1 = df_c['consumo'].corr(df_c['lag_1'])
corr_lag5 = df_c['consumo'].corr(df_c['lag_5'])
corr_ma5 = df_c['consumo'].corr(df_c['media_movel_5d'])

# 1. Lag 1 (Hoje vs Ontem)
sns.regplot(ax=axes[0, 0], data=df_c, x='lag_1', y='consumo',
            scatter_kws={'alpha': 0.45, 'color': '#1f77b4', 's': 35}, line_kws={'color': 'darkred', 'lw': 2})
axes[0, 0].set_title(f"1. Memória Imediata: Consumo de Hoje (yt) x Ontem (yt-1)\n(Correlação r = {corr_lag1:.3f})", fontsize=12)
axes[0, 0].set_xlabel("Consumo no Dia Letivo Anterior (yt-1) [Refeições]")
axes[0, 0].set_ylabel("Consumo no Dia Atual (yt) [Refeições]")

# 2. Lag 5 (Hoje vs Semana Passada)
sns.regplot(ax=axes[0, 1], data=df_c, x='lag_5', y='consumo',
            scatter_kws={'alpha': 0.45, 'color': '#ff7f0e', 's': 35}, line_kws={'color': 'darkgreen', 'lw': 2})
axes[0, 1].set_title(f"2. Ciclo Semanal: Consumo de Hoje (yt) x Mesma Semana Passada (yt-5)\n(Correlação r = {corr_lag5:.3f})", fontsize=12)
axes[0, 1].set_xlabel("Consumo 5 Dias Úteis Atrás (yt-5) [Refeições]")
axes[0, 1].set_ylabel("Consumo no Dia Atual (yt) [Refeições]")

# 3. Autocorrelação (ACF de Lags 1 a 20)
lags_range = list(range(1, 21))
autocorrs = [df_c['consumo'].autocorr(lag=k) for k in lags_range]
n = len(df_c['consumo'].dropna())
conf_int = 1.96 / np.sqrt(n)

axes[1, 0].stem(lags_range, autocorrs, linefmt='b-', markerfmt='bo', basefmt='k-')
axes[1, 0].axhspan(-conf_int, conf_int, alpha=0.2, color='lightblue', label='Intervalo de Confiança 95%')
axes[1, 0].axhline(0, color='black', lw=1)
axes[1, 0].set_title("3. Função de Autocorrelação (ACF) - Memória Temporal de 1 a 20 Dias Úteis", fontsize=12)
axes[1, 0].set_xlabel("Defasagem Temporal em Dias Úteis (Lags)")
axes[1, 0].set_ylabel("Autocorrelação de Pearson")
axes[1, 0].set_xticks(lags_range)
axes[1, 0].legend(loc='upper right')

# 4. Média Móvel Recente (5 dias) vs Consumo Presente
sns.regplot(ax=axes[1, 1], data=df_c, x='media_movel_5d', y='consumo',
            scatter_kws={'alpha': 0.45, 'color': 'purple', 's': 35}, line_kws={'color': 'crimson', 'lw': 2})
axes[1, 1].set_title(f"4. Âncora de Curto Prazo: Consumo de Hoje x Média dos Últimos 5 Dias Úteis\n(Correlação r = {corr_ma5:.3f})", fontsize=12)
axes[1, 1].set_xlabel("Média Móvel dos Últimos 5 Dias Letivos [Refeições]")
axes[1, 1].set_ylabel("Consumo no Dia Atual (yt) [Refeições]")

plt.suptitle("Figura 25: Estrutura de Dependência Temporal e Memória Histórica do Consumo de Refeições", fontsize=15, y=0.99)
plt.tight_layout()

os.makedirs('reports/figuras', exist_ok=True)
caminho_fig = 'reports/figuras/fig25_autocorrelacao_memoria_temporal.png'
plt.savefig(caminho_fig, dpi=300, bbox_inches='tight')
print(f"[OK] Figura salva com sucesso em: {caminho_fig}")
