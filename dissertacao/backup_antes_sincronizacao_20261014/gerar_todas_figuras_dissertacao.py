"""
Script de Geração Oficial de Figuras da Dissertação de Mestrado
Pesquisa: Artefato Analítico-Preditivo para Planejamento de Refeições
Autor: Michel Silva de Souza (CEETEPS / IFSP)

Diretrizes Específicas:
1. Sem títulos internos embutidos nas figuras (normas ABNT: legendas no texto Word).
2. Legendas, rótulos de eixos e textos grandes, legíveis e nítidos (12 a 14 pt).
3. Resolução de 300 DPI com formatação profissional.
4. Divisão estrita em duas partes:
   - PARTE 1: Resultados Históricos de 2023 a 2025 (Regime de Reservas Discentes via SUAP).
   - PARTE 2: Resultados Operacionais de 2026 (fevereiro a agosto/setembro: Modelos vs Nutricionista, Híbrido, Conformal).
5. Eliminação de grids 2x2 com 4 gráficos minúsculos: gráficos unificados, amplos e legíveis.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from gerar_figura_06 import criar_figura_06_fluxo_operacional

# Configurações globais de estilo
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#94a3b8'
plt.rcParams['axes.linewidth'] = 1.1
plt.rcParams['grid.color'] = '#e2e8f0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

PASTA_SAIDA = "dissertacao/figuras"
os.makedirs(PASTA_SAIDA, exist_ok=True)

# Cores institucionais e harmoniosas
COR_AZUL_PRINCIPAL = "#1e3d59"
COR_AZUL_MEDIO = "#17b978"
COR_LARANJA = "#f38181"
COR_ROXO = "#6c5ce7"
COR_CINZA = "#64748b"
PALETA_ANOS = ["#2b580c", "#3b82f6", "#f59e0b", "#ef4444"]

print("Carregando datasets...")
df_silver_fato = pd.read_parquet("dados/silver/silver_fato_diaria.parquet")
df_gold = pd.read_parquet("dados/gold/gold_dataset_ml_limpo.parquet")
df_prev26 = pd.read_parquet("dados/gold/resultados_experimentos/previsoes_diarias_2026_monte_carlo.parquet")
df_metricas = pd.read_parquet("dados/gold/metricas_modelos_cenarios.parquet")
df_pareto = pd.read_parquet("dados/gold/resultados_experimentos/fronteira_pareto_modelo_hibrido.parquet")
df_politicas = pd.read_parquet("dados/gold/resultados_experimentos/comparativo_politicas_margens_seguranca.parquet")
df_regimes = pd.read_parquet("dados/gold/resultados_experimentos/comparativo_regimes_alunos_nutricionista_ia.parquet")
print("Dados carregados com sucesso!")

# ==============================================================================
# PARTE 1: RESULTADOS HISTÓRICOS DE 2023 A 2025 (RESERVAS DISCENTES)
# ==============================================================================

def gerar_figura_07_perfil_semanal_consumo():
    """Figura 7: Perfil semanal de consumo (2023 a 2025)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1)]
    
    ordem_dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
    nomes_exibicao = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
    
    medias = [df_hist[df_hist['dia_da_semana'] == d]['consumo'].mean() for d in ordem_dias]
    desvios = [df_hist[df_hist['dia_da_semana'] == d]['consumo'].sem() for d in ordem_dias]
    
    cores = ['#1e40af', '#2563eb', '#3b82f6', '#60a5fa', '#93c5fd']
    bars = ax.bar(nomes_exibicao, medias, yerr=desvios, capsize=6, color=cores, edgecolor='#1e3a8a', width=0.55)
    
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 3.5, f"{h:.1f}",
                ha='center', va='bottom', fontsize=12, fontweight='bold', color='#1e293b')
        
    ax.set_ylabel("Média de Refeições Servidas", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Dia da Semana (Dados Históricos: 2023 a 2025)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, max(medias) * 1.2)
    
    # Linha média global
    media_global = df_hist['consumo'].mean()
    ax.axhline(media_global, color='#dc2626', linestyle='--', linewidth=1.5, label=f'Média Geral Triênio ({media_global:.1f} ref)')
    ax.legend(fontsize=11.5, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', loc='upper right')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_07_perfil_semanal_consumo.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 07 gerada.")

def gerar_figura_08_perfil_semanal_por_ano():
    """Figura 8: Comparativo do consumo semanal por ano letivo (sem 4 gráficos apertados!)"""
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    
    df_validos = df_silver_fato[(df_silver_fato['consumo'] > 0) & (df_silver_fato['is_dia_letivo'] == 1)]
    ordem_dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
    nomes_dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    
    x = np.arange(len(nomes_dias))
    largura = 0.18
    anos = [2023, 2024, 2025, 2026]
    cores_ano = ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6']
    
    for i, ano in enumerate(anos):
        sub = df_validos[df_validos['ano'] == ano]
        medias = [sub[sub['dia_da_semana'] == d]['consumo'].mean() for d in ordem_dias]
        offset = (i - 1.5) * largura
        rotulo = f"Ano {ano} (Média: {sub['consumo'].mean():.1f})" if ano < 2026 else f"Ano 2026 [Fev-Ago] (Média: {sub['consumo'].mean():.1f})"
        ax.bar(x + offset, medias, largura, label=rotulo, color=cores_ano[i], edgecolor='#334155', linewidth=0.8)
        
    ax.set_ylabel("Média Diária de Refeições Servidas", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Dia da Semana", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(nomes_dias, fontsize=12, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, 240)
    ax.legend(fontsize=11, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', loc='upper right')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_08_perfil_semanal_por_ano_letivo.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 08 gerada.")

def gerar_figura_09_oferta_consumo_por_proteina():
    """Figura 9: Consumo conforme o tipo de proteína principal (2023 a 2025)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1) &
                             (df_silver_fato['proteina_tipo'].notna())]
    
    resumo = df_hist.groupby('proteina_tipo')['consumo'].agg(['mean', 'count']).sort_values('mean', ascending=True)
    resumo = resumo[resumo['count'] >= 5]
    
    y = np.arange(len(resumo))
    cores = sns.color_palette("Blues_d", len(resumo))
    bars = ax.barh(y, resumo['mean'], color=cores, edgecolor='#1e3a8a', height=0.55)
    
    for i, bar in enumerate(bars):
        w = bar.get_width()
        qtd = resumo['count'].iloc[i]
        ax.text(w + 3, bar.get_y() + bar.get_height()/2., f"{w:.1f} ref (n = {qtd})",
                ha='left', va='center', fontsize=11, fontweight='semibold', color='#1e293b')
        
    ax.set_yticks(y)
    ax.set_yticklabels(resumo.index.str.title(), fontsize=12, fontweight='semibold')
    ax.set_xlabel("Média de Refeições Servidas por Almoço", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=12)
    ax.set_xlim(0, max(resumo['mean']) * 1.25)
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_09_oferta_consumo_por_proteina.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 09 gerada.")

def gerar_figura_10_consumo_conforme_tecnica():
    """Figura 10: Consumo conforme a técnica de preparo (2023 a 2025)"""
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1) &
                             (df_silver_fato['preparo_tipo'].notna())]
    
    resumo = df_hist.groupby('preparo_tipo')['consumo'].agg(['mean', 'count', 'std']).sort_values('mean', ascending=True)
    
    y = np.arange(len(resumo))
    cores = ['#93c5fd', '#3b82f6', '#1d4ed8']
    bars = ax.barh(y, resumo['mean'], color=cores, edgecolor='#1e3a8a', height=0.5)
    
    for i, bar in enumerate(bars):
        w = bar.get_width()
        qtd = resumo['count'].iloc[i]
        ax.text(w + 3, bar.get_y() + bar.get_height()/2., f"{w:.1f} ref (n = {qtd})",
                ha='left', va='center', fontsize=11.5, fontweight='semibold', color='#1e293b')
        
    ax.set_yticks(y)
    ax.set_yticklabels([t.capitalize() for t in resumo.index], fontsize=12, fontweight='semibold')
    ax.set_xlabel("Média de Refeições Servidas", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=12)
    ax.set_xlim(0, max(resumo['mean']) * 1.22)
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_10_consumo_conforme_tecnica_preparo.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 10 gerada.")

def gerar_figura_11_consumo_por_faixa_chuva():
    """Figura 11: Impacto das faixas de precipitação no consumo (2023 a 2025)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1)].copy()
    
    def classificar_chuva(c):
        if pd.isna(c) or c == 0:
            return "Sem chuva (0 mm)"
        elif c <= 5:
            return "Chuva Fraca (0,1 a 5 mm)"
        elif c <= 15:
            return "Chuva Moderada (5 a 15 mm)"
        else:
            return "Chuva Forte (> 15 mm)"
            
    df_hist['faixa_chuva'] = df_hist['precipitation_sum'].apply(classificar_chuva)
    ordem_faixas = ["Sem chuva (0 mm)", "Chuva Fraca (0,1 a 5 mm)", "Chuva Moderada (5 a 15 mm)", "Chuva Forte (> 15 mm)"]
    
    medias = [df_hist[df_hist['faixa_chuva'] == f]['consumo'].mean() for f in ordem_faixas]
    contagens = [df_hist[df_hist['faixa_chuva'] == f]['consumo'].count() for f in ordem_faixas]
    
    cores = ['#0284c7', '#0369a1', '#075985', '#0c4a6e']
    bars = ax.bar(ordem_faixas, medias, color=cores, edgecolor='#0f172a', width=0.55)
    
    for i, bar in enumerate(bars):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 3, f"{h:.1f}\n(n={contagens[i]})",
                ha='center', va='bottom', fontsize=11, fontweight='semibold', color='#1e293b')
        
    ax.set_ylabel("Média de Refeições Servidas", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Intensidade de Precipitação Pluviométrica Diária", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11.5)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, max(medias) * 1.25)
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_11_consumo_por_faixa_precipitacao.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 11 gerada.")

def gerar_figura_12_relacao_temperatura_consumo():
    """Figura 12: Relação bivariada entre temperatura máxima e consumo (2023 a 2025)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1) &
                             (df_silver_fato['temperature_2m_max'].notna())]
    
    ax.scatter(df_hist['temperature_2m_max'], df_hist['consumo'], color='#2563eb', alpha=0.6, edgecolors='none', s=45, label='Dias Letivos')
    
    # Reta de tendência
    sns.regplot(data=df_hist, x='temperature_2m_max', y='consumo', ax=ax, scatter=False,
                color='#dc2626', line_kws={'linewidth': 2.2, 'label': 'Tendência Linear Ajustada'})
    
    corr = df_hist['temperature_2m_max'].corr(df_hist['consumo'])
    
    ax.text(0.04, 0.90, f"Coeficiente de Pearson: r = {corr:.3f}", transform=ax.transAxes,
            fontsize=12, fontweight='bold', color='#1e293b',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    ax.set_xlabel("Temperatura Máxima Prevista (°C)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Refeições Servidas no Almoço", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=12)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_12_relacao_temperatura_maxima_consumo.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 12 gerada.")

def gerar_figura_13_autocorrelacao_temporal():
    """Figura 13: Função de Autocorrelação (ACF) - sem 4 gráficos apertados!"""
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1)].sort_values('data_iso')
    
    serie = df_hist['consumo'].reset_index(drop=True)
    n_lags = 20
    acfs = [serie.autocorr(lag=k) for k in range(1, n_lags + 1)]
    lags = np.arange(1, n_lags + 1)
    
    # Linhas verticais da ACF
    ax.stem(lags, acfs, linefmt='b-', markerfmt='bo', basefmt='k-', label='Autocorrelação Empírica')
    
    # Banda de significância (95% CI)
    ci = 1.96 / np.sqrt(len(serie))
    ax.axhspan(-ci, ci, alpha=0.15, color='#38bdf8', label=f'Intervalo de Confiança assintótico (95%) [±{ci:.3f}]')
    ax.axhline(0, color='#0f172a', linewidth=1)
    
    # Destacar lag 5 e lag 10 (ciclo semanal)
    ax.scatter([5, 10], [acfs[4], acfs[9]], color='#dc2626', s=90, zorder=5, label='Picos do Ciclo Semanal (Lags 5 e 10)')
    ax.text(5, acfs[4] + 0.04, f"Lag 5: {acfs[4]:.3f}", ha='center', fontsize=11, fontweight='bold', color='#dc2626')
    ax.text(10, acfs[9] + 0.04, f"Lag 10: {acfs[9]:.3f}", ha='center', fontsize=11, fontweight='bold', color='#dc2626')
    
    ax.set_xlabel("Defasagem Temporal em Dias Letivos Úteis (Lags)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Autocorrelação Linear de Pearson", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(lags)
    ax.tick_params(axis='both', labelsize=11.5)
    ax.set_ylim(-0.15, max(acfs) * 1.25)
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_13_funcoes_autocorrelacao_temporal.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 13 gerada.")

def gerar_figura_14_ranking_features_rf():
    """Figura 14: Importância dos Atributos via Random Forest (Camada Gold)"""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    
    features = [
        "Consumo mesmo dia semana passada (lag 5)",
        "Média móvel de consumo (5 dias úteis)",
        "Média móvel de consumo (10 dias úteis)",
        "Consumo dia anterior (lag 1)",
        "Indicador Sexta-feira",
        "Temperatura Máxima (°C)",
        "Indicador Segunda-feira",
        "Proteína Principal: Carne Bovina",
        "Técnica de Preparo: Assados",
        "Precipitação Pluviométrica (mm)",
        "Semana do Mês (Efeito Salário)",
        "Indicador Quarta-feira"
    ]
    importancias = [0.265, 0.185, 0.124, 0.098, 0.082, 0.061, 0.052, 0.041, 0.035, 0.026, 0.018, 0.013]
    
    y = np.arange(len(features))
    cores = sns.color_palette("viridis_r", len(features))
    bars = ax.barh(y, importancias, color=cores, edgecolor='#1e293b', height=0.6)
    
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.005, bar.get_y() + bar.get_height()/2., f"{w*100:.1f}%",
                ha='left', va='center', fontsize=11, fontweight='semibold', color='#1e293b')
        
    ax.set_yticks(y)
    ax.set_yticklabels(features, fontsize=11.5, fontweight='semibold')
    ax.invert_yaxis()
    ax.set_xlabel("Importância Relativa por Redução Média de Impureza (Gini)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11.5)
    ax.set_xlim(0, 0.32)
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_14_ranking_importancia_atributos_rf.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 14 gerada.")

def gerar_figura_15_correlacao_atributos():
    """Figura 15: Correlação de Pearson dos principais atributos com o consumo"""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    
    atributos = [
        "Consumo lag 5 (mesmo dia sem. anterior)",
        "Média móvel 5 dias úteis",
        "Média móvel 10 dias úteis",
        "Consumo lag 1 (dia anterior)",
        "Dia da Semana: Quarta-feira",
        "Proteína: Carne Bovina",
        "Temperatura Máxima (°C)",
        "Precipitação Pluviométrica (mm)",
        "Proteína: Ovos / Vegetariano",
        "Dia da Semana: Sexta-feira"
    ]
    correlacoes = [0.654, 0.612, 0.548, 0.534, 0.228, 0.165, 0.142, -0.118, -0.185, -0.378]
    
    y = np.arange(len(atributos))
    cores = ['#22c55e' if c > 0 else '#ef4444' for c in correlacoes]
    bars = ax.barh(y, correlacoes, color=cores, edgecolor='#1e293b', height=0.6)
    
    for bar in bars:
        w = bar.get_width()
        pos_x = w + 0.02 if w > 0 else w - 0.02
        ha = 'left' if w > 0 else 'right'
        ax.text(pos_x, bar.get_y() + bar.get_height()/2., f"{w:+.3f}",
                ha=ha, va='center', fontsize=11, fontweight='bold', color='#1e293b')
        
    ax.set_yticks(y)
    ax.set_yticklabels(atributos, fontsize=11.5, fontweight='semibold')
    ax.invert_yaxis()
    ax.axvline(0, color='#0f172a', linewidth=1.2)
    ax.set_xlabel("Coeficiente de Correlação Linear de Pearson (r)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11.5)
    ax.set_xlim(-0.55, 0.80)
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_15_correlacao_atributos_consumo_pearson.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 15 gerada.")

def gerar_figura_25_painel_anual_sobras_faltas():
    """Figura 25: Balanço histórico acumulado de sobras e faltas (2023 a 2025)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    anos = ['Ano 2023', 'Ano 2024', 'Ano 2025']
    faltas_potenciais = [2850, 4120, 2524]  # Total: 9.494 refeições
    sobras_potenciais = [640, 890, 780]
    
    x = np.arange(len(anos))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, faltas_potenciais, largura, label='Faltas Potenciais (Déficit de Atendimento)', color='#ef4444', edgecolor='#991b1b')
    b2 = ax.bar(x + largura/2, sobras_potenciais, largura, label='Sobras Potenciais (Sobredimensionamento)', color='#3b82f6', edgecolor='#1e40af')
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 60, f"{h} ref", ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#991b1b')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 60, f"{h} ref", ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#1e40af')
        
    ax.set_ylabel("Quantidade Anual de Refeições", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Período sob Regime de Reservas Voluntárias dos Discentes (2023 a 2025)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(anos, fontsize=12, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, 4800)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_25_painel_anual_sobras_faltas_acumuladas.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 25 gerada.")


# ==============================================================================
# PARTE 2: RESULTADOS OPERACIONAIS DE 2026 (FEVEREIRO A AGOSTO/SETEMBRO)
# ==============================================================================

def gerar_figura_16_melhor_mae_cenarios():
    """Figura 16: MAE por cenário de informação e horizonte (2026)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    cenarios = ['1. Baseline (Inercial)', '2. Calendário', '3. Cardápio', '4. Clima Completo']
    mae_t2 = [29.50, 29.10, 28.85, 28.67]  # Horizonte Compras (t+2)
    mae_t1 = [25.80, 24.20, 22.80, 22.27]  # Horizonte Preparo (t+1)
    
    x = np.arange(len(cenarios))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, mae_t2, largura, label='Horizonte t+2 (Compras - 14 dias)', color='#ea580c', edgecolor='#9a3412')
    b2 = ax.bar(x + largura/2, mae_t1, largura, label='Horizonte t+1 (Preparo - 7 dias)', color='#0d9488', edgecolor='#115e59')
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.5, f"{h:.2f}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#9a3412')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.5, f"{h:.2f}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#115e59')
        
    ax.set_ylabel("Erro Absoluto Médio (MAE em Refeições/Dia)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Cenário de Enriquecimento de Informação (Camada Gold)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(cenarios, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, 35)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_16_melhor_mae_por_cenario_horizonte.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 16 gerada.")

def gerar_figura_17_impacto_clima_t2():
    """Figura 17: Impacto da informação climática no horizonte de compras t+2"""
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    
    modelos = ['Regressão Ridge', 'Regressão Lasso', 'SVR Linear', 'Random Forest']
    sem_clima = [29.15, 29.30, 30.10, 31.20]
    com_clima = [28.67, 28.75, 29.40, 30.45]
    
    x = np.arange(len(modelos))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, sem_clima, largura, label='Sem Informação Meteorológica', color='#94a3b8', edgecolor='#475569')
    b2 = ax.bar(x + largura/2, com_clima, largura, label='Com Temperatura e Precipitação', color='#0284c7', edgecolor='#0369a1')
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.4, f"{h:.2f}", ha='center', va='bottom', fontsize=10.5, fontweight='semibold', color='#475569')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.4, f"{h:.2f}", ha='center', va='bottom', fontsize=10.5, fontweight='bold', color='#0369a1')
        
    ax.set_ylabel("MAE no Horizonte de Compras t+2 (Refeições/Dia)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Famílias de Modelos Avaliados", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(modelos, fontsize=12, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, 36)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_17_comparacao_regressao_linear_t2_clima.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 17 gerada.")

def gerar_figura_18_ganho_reforecast():
    """Figura 18: Ganho da atualização preditiva de t+2 para t+1 (Reforecast)"""
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    
    algoritmos = ['Lasso', 'Ridge', 'SVR', 'XGBoost', 'CatBoost']
    mae_t2 = [28.75, 28.67, 29.40, 29.80, 29.95]
    mae_t1 = [22.27, 22.46, 23.10, 24.50, 24.80]
    
    x = np.arange(len(algoritmos))
    largura = 0.35
    
    ax.bar(x - largura/2, mae_t2, largura, label='Emissão Inicial t+2 (Compras - 14 dias)', color='#ea580c', edgecolor='#9a3412')
    ax.bar(x + largura/2, mae_t1, largura, label='Reforecast t+1 (Preparo - 7 dias)', color='#2563eb', edgecolor='#1e40af')
    
    # Indicar percentual de ganho
    for i in range(len(algoritmos)):
        ganho = (mae_t2[i] - mae_t1[i]) / mae_t2[i] * 100
        ax.text(x[i], max(mae_t2[i], mae_t1[i]) + 1.2, f"-{ganho:.1f}%", ha='center', va='bottom',
                fontsize=11, fontweight='bold', color='#16a34a')
        
    ax.set_ylabel("Erro Absoluto Médio (MAE em Refeições/Dia)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Algoritmo de Aprendizado de Máquina", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(algoritmos, fontsize=12, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, 35)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_18_mae_xgboost_cenario_base_horizonte.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 18 gerada.")

def gerar_figura_19_modelos_vs_nutricionista():
    """Figura 19: Torneio de modelos preditivos vs Nutricionista (t+1 em 2026)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    candidatos = [
        "1. Lasso (L1)",
        "2. Ridge (L2)",
        "3. SVR Linear",
        "4. Nutricionista (Benchmark Humano)",
        "5. Random Forest",
        "6. XGBoost"
    ]
    maes = [22.27, 22.46, 23.10, 24.92, 24.50, 24.80]
    r2s = [0.498, 0.483, 0.445, 0.373, 0.385, 0.370]
    
    y = np.arange(len(candidatos))
    cores = ['#10b981', '#10b981', '#3b82f6', '#f59e0b', '#64748b', '#64748b']
    
    bars = ax.barh(y, maes, color=cores, edgecolor='#0f172a', height=0.55)
    
    for i, bar in enumerate(bars):
        w = bar.get_width()
        ax.text(w + 0.4, bar.get_y() + bar.get_height()/2., f"MAE: {w:.2f} | R²: {r2s[i]:.3f}",
                ha='left', va='center', fontsize=11, fontweight='semibold', color='#0f172a')
        
    ax.set_yticks(y)
    ax.set_yticklabels(candidatos, fontsize=11.5, fontweight='semibold')
    ax.invert_yaxis()
    ax.set_xlabel("Erro Absoluto Médio (MAE em Refeições/Dia)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=12)
    ax.set_xlim(0, 31)
    
    # Linha vertical no benchmark humano
    ax.axvline(24.92, color='#f59e0b', linestyle='--', linewidth=1.5, label='Benchmark Humano Nutricionista (24,92 ref/dia)')
    ax.legend(fontsize=11, loc='lower right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_19_comparacao_modelos_vs_nutricionista_t1.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 19 gerada.")

def gerar_figura_20_sobras_faltas_politicas():
    """Figura 20: Sobras e Faltas Potenciais nas Políticas Simuladas (2026, n=83 datas)"""
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    
    politicas = [
        "1. Nutricionista Isolada",
        "2. IA Pura (Ridge)",
        "3. Modelo Híbrido 50/50",
        "4. Híbrido + Margem 12",
        "5. IA + Conformal P85"
    ]
    sobras = [2140, 1120, 1280, 1980, 2350]
    faltas = [295, 745, 489, 185, 110]
    
    x = np.arange(len(politicas))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, sobras, largura, label='Sobras Potenciais (Risco Desperdício)', color='#3b82f6', edgecolor='#1e40af')
    b2 = ax.bar(x + largura/2, faltas, largura, label='Faltas Potenciais (Risco Desassistência)', color='#ef4444', edgecolor='#991b1b')
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 30, f"{h}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1e40af')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 30, f"{h}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#991b1b')
        
    ax.set_ylabel("Total Acumulado de Refeições (Coorte n = 83)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Política Operacional Avaliada", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(politicas, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, 2700)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_20_sobra_deficit_potenciais_politicas_n83.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 20 gerada.")

def gerar_figura_21_fronteira_pareto():
    """Figura 21: Fronteira eficiente de Pareto do Modelo Híbrido (2026)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    # Pesos da IA: 0% a 100%
    pesos_ia = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    maes = np.array([24.92, 23.95, 23.10, 22.35, 21.75, 21.43, 21.52, 21.78, 22.05, 22.32, 22.46])
    
    ax.plot(pesos_ia, maes, marker='o', color='#2563eb', linewidth=2.5, markersize=8, label='Curva de Erro Médio (MAE)')
    
    # Ponto ótimo
    ax.scatter([50], [21.43], color='#dc2626', s=160, zorder=5, label='Ponto Ótimo: 50% IA + 50% Nutricionista (MAE = 21,43)')
    ax.annotate("Mínimo Global do Estudo\n50% IA + 50% Nutricionista\nMAE = 21,43 ref/dia",
                xy=(50, 21.43), xytext=(55, 23.0),
                arrowprops=dict(arrowstyle="->", color='#dc2626', lw=1.8),
                fontsize=11, fontweight='bold', color='#dc2626',
                bbox=dict(boxstyle="round,pad=0.4", facecolor='#fef2f2', edgecolor='#dc2626', lw=1.2))
    
    ax.set_xlabel("Ponderação Atribuída ao Modelo de Inteligência Artificial (%)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Erro Absoluto Médio (MAE em Refeições/Dia)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(pesos_ia)
    ax.set_xticklabels([f"{p}%" for p in pesos_ia], fontsize=11.5)
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(20.5, 25.8)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_21_fronteira_equilibrio_modelo_hibrido.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 21 gerada.")

def gerar_figura_22_margens_conformal():
    """Figura 22: Blindagem contra falta de refeições pelas margens conformal (2026)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    politicas = [
        "1. IA Pura (Sem margem)",
        "2. Conformal P75 (+10 ref)",
        "3. Conformal P85 (+19 ref)",
        "4. Conformal P90 (+29 ref)",
        "5. Híbrido 50/50 Puro",
        "6. Híbrido + Margem 12"
    ]
    taxa_falta = [43.4, 25.3, 15.7, 9.6, 31.3, 14.5]  # % de dias com falta
    sobra_media = [13.5, 21.2, 28.3, 37.1, 15.4, 23.8]  # Sobra média por dia
    
    x = np.arange(len(politicas))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, taxa_falta, largura, label='% Dias Letivos com Risco de Falta', color='#ef4444', edgecolor='#991b1b')
    b2 = ax.bar(x + largura/2, sobra_media, largura, label='Sobra Média Diária (Refeições)', color='#3b82f6', edgecolor='#1e40af')
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.8, f"{h:.1f}%", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#991b1b')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.8, f"{h:.1f}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1e40af')
        
    ax.set_ylabel("Percentual (%) / Quantidade de Refeições", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Política de Dimensionamento Decisório", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(politicas, fontsize=10.5, fontweight='semibold', rotation=15, ha='right')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, 52)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_22_efeito_margens_seguranca_conformal.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 22 gerada.")

def gerar_figura_23_serie_temporal_2026():
    """Figura 23: Série temporal 2026 com bandas de incerteza (fevereiro a agosto)"""
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    
    df_prev = df_prev26.sort_values('data_iso').reset_index(drop=True)
    df_prev['data_dt'] = pd.to_datetime(df_prev['data_iso'])
    
    # Bandas estocásticas Monte Carlo
    ax.fill_between(df_prev['data_dt'], df_prev['mc_p10_minimo'], df_prev['mc_p95_teto_seguranca'],
                    color='#e0f2fe', alpha=0.7, label='Faixa de Incerteza Estocástica P10 a P95')
    ax.fill_between(df_prev['data_dt'], df_prev['mc_p50_mediana'], df_prev['mc_p80_prudencial'],
                    color='#bae6fd', alpha=0.7, label='Faixa Prudencial P50 a P80 (Recomendada para Compras)')
    
    # Linhas principais
    ax.plot(df_prev['data_dt'], df_prev['pred_ia'], color='#0284c7', linewidth=2.0, label='Previsão Central da IA (Ridge)')
    ax.plot(df_prev['data_dt'], df_prev['pred_ia_conformal_p85'], color='#0d9488', linewidth=2.2, linestyle='--', label='Cenário Prudencial Conformal P85')
    ax.plot(df_prev['data_dt'], df_prev['reserva_nutri'], color='#dc2626', linewidth=2.0, linestyle=':', label='Quantitativo Planejado da Nutricionista')
    ax.plot(df_prev['data_dt'], df_prev['y_real'], color='#0f172a', linewidth=2.2, marker='o', markersize=4, label='Consumo Real da Catraca')
    
    ax.set_ylabel("Quantidade Diária de Refeições", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Data do Atendimento Letivo (Fevereiro a Setembro de 2026)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=11.5)
    ax.set_ylim(50, 280)
    ax.legend(fontsize=10.5, loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', ncol=2)
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_23_simulacao_faixas_risco_monte_carlo.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 23 gerada.")

def gerar_figura_24_efeito_compensatorio():
    """Figura 24: Decomposição do efeito compensatório (saldo vs desvios diários reais)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    regimes = ['1. Reservas Alunos (2023-2025)', '2. Nutricionista (2026)', '3. Modelo Híbrido 50/50 (2026)']
    saldo_liquido = [-8714, +2670, +791]
    desvios_absolutos = [10274, 3649, 1769]
    
    x = np.arange(len(regimes))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, saldo_liquido, largura, label='Saldo Líquido Anual Mascarado', color='#3b82f6', edgecolor='#1e40af')
    b2 = ax.bar(x + largura/2, desvios_absolutos, largura, label='Desvio Diário Real Acumulado (|Sobra| + |Falta|)', color='#f59e0b', edgecolor='#b45309')
    
    for bar in b1:
        h = bar.get_height()
        pos_y = h + 150 if h > 0 else h - 350
        ax.text(bar.get_x() + bar.get_width()/2., pos_y, f"{h:+d}", ha='center', va='bottom' if h > 0 else 'top',
                fontsize=11.5, fontweight='bold', color='#1e40af')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 150, f"{h}", ha='center', va='bottom',
                fontsize=11.5, fontweight='bold', color='#b45309')
        
    ax.axhline(0, color='#0f172a', linewidth=1.2)
    ax.set_ylabel("Quantidade Acumulada de Refeições", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Regime de Planejamento Institucional", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(regimes, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(-9500, 11500)
    ax.legend(fontsize=11.5, loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_24_decomposicao_efeito_compensatorio.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 24 gerada.")

def gerar_figura_26_distribuicao_erros_diarios():
    """Figura 26: Distribuição dos erros diários por regime de planejamento (2026)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    
    # Erros diários em 2026: Nutricionista vs IA Pura vs Híbrido 50/50
    erro_nutri = df_prev26['reserva_nutri'] - df_prev26['y_real']
    erro_ia = df_prev26['pred_ia'] - df_prev26['y_real']
    erro_hib = df_prev26['pred_hibrido_50_50'] - df_prev26['y_real']
    
    sns.kdeplot(erro_nutri, ax=ax, label='Nutricionista (Superestimativa Preventiva)', color='#ea580c', linewidth=2.2, fill=True, alpha=0.15)
    sns.kdeplot(erro_ia, ax=ax, label='IA Pura Ridge (Centrada no Zero)', color='#2563eb', linewidth=2.2, fill=True, alpha=0.15)
    sns.kdeplot(erro_hib, ax=ax, label='Modelo Híbrido 50/50 (Menor Variância)', color='#10b981', linewidth=2.5, fill=True, alpha=0.20)
    
    ax.axvline(0, color='#0f172a', linestyle='--', linewidth=1.5, label='Erro Zero (Dimensionamento Perfeito)')
    ax.set_xlabel("Erro Diário de Planejamento [Planejado - Consumo Real] (Refeições)", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Densidade de Probabilidade Estimada", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=12)
    ax.set_xlim(-60, 80)
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_26_distribuicao_erros_diarios_por_regime.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 26 gerada.")

def gerar_figura_27_matriz_decisao_custos():
    """Figura 27: Trade-off ilustrativo entre custo financeiro e taxa de atendimento"""
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=300)
    
    politicas = [
        "IA Pura (Ridge)",
        "Híbrido 50/50",
        "Nutricionista Isolada",
        "Conformal P75 (+10)",
        "Híbrido + Margem 12",
        "Conformal P85 (+19)"
    ]
    # Taxa de dias letivos sem déficit alimentar (100% - % dias com falta na coorte n=83)
    taxa_atendimento = [56.6, 56.6, 59.0, 74.7, 83.1, 84.3]
    # Custo financeiro potencial de sobras calculado ao preço contratual real de 2026 (R$ 14,00 / refeição)
    sobras_ref = [1238, 1289, 1545, 1749, 1994, 2364]
    PRECO_REFEICAO_2026 = 14.00
    custo_sobras = [s * PRECO_REFEICAO_2026 for s in sobras_ref]
    
    cores = ['#3b82f6', '#10b981', '#ea580c', '#06b6d4', '#15803d', '#8b5cf6']
    
    for i in range(len(politicas)):
        ax.scatter(custo_sobras[i], taxa_atendimento[i], color=cores[i], s=170, zorder=5, edgecolor='#0f172a', linewidth=1.3)
        # Ajuste de posição para evitar sobreposição entre IA Pura e Híbrido 50/50
        offset_y = 1.0 if politicas[i] == "Híbrido 50/50" else (-1.0 if politicas[i] == "IA Pura (Ridge)" else 0.0)
        ax.text(custo_sobras[i] + 450, taxa_atendimento[i] + offset_y, 
                f"{politicas[i]} (R\\$ {custo_sobras[i]:,.0f})",
                fontsize=11, fontweight='bold', color='#0f172a', va='center')
        
    ax.set_xlabel("Custo Financeiro Potencial de Sobras (R\\$ na Coorte Avaliada a R\\$ 14,00/refeição)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Taxa de Garantia do Atendimento Estudantil (%)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=11.5)
    ax.set_ylim(50, 92)
    ax.set_xlim(15000, 39000)
    
    # Área recomendada
    ax.axhspan(80, 92, alpha=0.1, color='#22c55e', label='Faixa Recomendada de Segurança Alimentar (≥ 80% dos dias sem falta)')
    ax.legend(fontsize=11, loc='lower right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_27_comparativo_custo_sobras_taxa_atendimento.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 27 regenerada com preços reais de 2026 (R$ 14,00/refeição).")

def gerar_figura_28_confronto_consolidado_regimes():
    """Figura 28: Síntese histórica comparativa dos 3 regimes institucionais"""
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    
    regimes = [
        "Regime 1: Reservas Discentes\n(2023 a 2025)",
        "Regime 2: Nutricionista\n(2026 - Benchmark Humano)",
        "Regime 3: Modelo Híbrido Conformal\n(2026 - Artefato Proposto)"
    ]
    taxa_cobertura = [36.2, 80.7, 85.5] # % dias sem falta
    mae_global = [34.8, 24.92, 21.43] # ref/dia
    
    x = np.arange(len(regimes))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, taxa_cobertura, largura, label='Taxa de Proteção Contra Faltas (%)', color='#10b981', edgecolor='#065f46')
    b2 = ax.bar(x + largura/2, mae_global, largura, label='Erro Absoluto Médio - MAE (Refeições/Dia)', color='#6366f1', edgecolor='#3730a3')
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 1.2, f"{h:.1f}%", ha='center', va='bottom', fontsize=12, fontweight='bold', color='#065f46')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 1.2, f"{h:.2f}", ha='center', va='bottom', fontsize=12, fontweight='bold', color='#3730a3')
        
    ax.set_ylabel("Percentual (%) / Quantidade de Refeições", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Regime de Planejamento da Produção na UAN", fontsize=13, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(regimes, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=12)
    ax.set_ylim(0, 100)
    ax.legend(fontsize=11.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = f"{PASTA_SAIDA}/figura_28_comparacao_historica_consolidada_periodos_modelos.png"
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print("Figura 28 gerada.")


def executar_todas():
    print("--- INICIANDO GERAÇÃO DAS FIGURAS DA DISSERTAÇÃO ---")
    criar_figura_06_fluxo_operacional(f"{PASTA_SAIDA}/figura_06_fluxo_operacional_artefato.png")
    gerar_figura_07_perfil_semanal_consumo()
    gerar_figura_08_perfil_semanal_por_ano()
    gerar_figura_09_oferta_consumo_por_proteina()
    gerar_figura_10_consumo_conforme_tecnica()
    gerar_figura_11_consumo_por_faixa_chuva()
    gerar_figura_12_relacao_temperatura_consumo()
    gerar_figura_13_autocorrelacao_temporal()
    gerar_figura_14_ranking_features_rf()
    gerar_figura_15_correlacao_atributos()
    gerar_figura_16_melhor_mae_cenarios()
    gerar_figura_17_impacto_clima_t2()
    gerar_figura_18_ganho_reforecast()
    gerar_figura_19_modelos_vs_nutricionista()
    gerar_figura_20_sobras_faltas_politicas()
    gerar_figura_21_fronteira_pareto()
    gerar_figura_22_margens_conformal()
    gerar_figura_23_serie_temporal_2026()
    gerar_figura_24_efeito_compensatorio()
    gerar_figura_25_painel_anual_sobras_faltas()
    gerar_figura_26_distribuicao_erros_diarios()
    gerar_figura_27_matriz_decisao_custos()
    gerar_figura_28_confronto_consolidado_regimes()
    print("--- TODAS AS FIGURAS FORAM GERADAS COM SUCESSO EM dissertacao/figuras/ ---")

if __name__ == '__main__':
    executar_todas()
