"""
Script de Geração Oficial e Auditado de Figuras da Dissertação de Mestrado
Pesquisa: Artefato Analítico-Preditivo para Planejamento de Refeições
Autor: Michel Silva de Souza (CEETEPS / IFSP)

Marco Temporal Estrito: Qualificação até 31/08/2026
Sincronizado rigorosamente com AUDITORIA_QUALIFICACAO_RECALCULO_N73.md
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

def salvar_figura(caminho, dpi=300):
    for tentativa in range(6):
        try:
            plt.savefig(caminho, dpi=dpi, bbox_inches='tight')
            return
        except OSError:
            time.sleep(0.5)
    tmp_path = caminho + f'.tmp_{os.getpid()}.png'
    plt.savefig(tmp_path, dpi=dpi, bbox_inches='tight')
    try:
        os.replace(tmp_path, caminho)
    except Exception:
        pass


# Configurações globais de estilo
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#94a3b8'
plt.rcParams['axes.linewidth'] = 1.1
plt.rcParams['grid.color'] = '#e2e8f0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PASTA_SAIDA = os.path.join(ROOT_DIR, "dissertacao", "figuras")
os.makedirs(PASTA_SAIDA, exist_ok=True)

print("Carregando datasets oficiais...")
df_silver_fato = pd.read_parquet(os.path.join(ROOT_DIR, "dados/silver/silver_fato_diaria.parquet"))
df_gold = pd.read_parquet(os.path.join(ROOT_DIR, "dados/gold/gold_dataset_ml_limpo.parquet"))

# Filtro estrito de corte de qualificação: 31/08/2026
df_gold_26 = df_gold[df_gold['data_iso'] <= '2026-08-31'].copy()
df_silver_26 = df_silver_fato[df_silver_fato['data_iso'] <= '2026-08-31'].copy()

# ==============================================================================
# FIGURAS 01 A 06: ESTRUTURA METODOLÓGICA E ARQUITETURA DSR
# ==============================================================================
# (Preservadas do pipeline metodológico DSR com alta resolução)

# ==============================================================================
# FIGURAS 07 A 15: PARTE 1 - RESULTADOS HISTÓRICOS E CAMADA GOLD
# ==============================================================================

def gerar_figura_07_perfil_semanal_consumo():
    """Figura 7 - Perfil semanal de consumo (2023 a 2025; N=458)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1)]
    
    ordem_dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
    nomes_exibicao = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
    
    medias = [df_hist[df_hist['dia_da_semana'] == d]['consumo'].mean() for d in ordem_dias]
    desvios = [df_hist[df_hist['dia_da_semana'] == d]['consumo'].sem() for d in ordem_dias]
    
    cores = ['#1e40af', '#2563eb', '#3b82f6', '#60a5fa', '#93c5fd']
    bars = ax.bar(nomes_exibicao, medias, yerr=desvios, capsize=6, color=cores, edgecolor='#1e3a8a', width=0.55, zorder=3)
    
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 3.5, f"{h:.1f}",
                ha='center', va='bottom', fontsize=12, fontweight='bold', color='#1e293b')
        
    ax.set_ylabel("Média de Refeições Servidas", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Dia da Semana (Dados Históricos: 2023 a 2025; N=458 datas)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11.5)
    ax.tick_params(axis='y', labelsize=11.5)
    ax.set_ylim(0, 180)
    
    media_global = df_hist['consumo'].mean()
    ax.axhline(media_global, color='#dc2626', linestyle='--', linewidth=1.5, label=f'Média Geral Triênio ({media_global:.1f} ref)')
    ax.legend(fontsize=11, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', loc='upper right')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_07_perfil_semanal_consumo.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 07 gerada.")

def gerar_figura_08_perfil_semanal_por_ano():
    """Figura 8 - Perfil semanal por ano letivo (Truncado em 31/08/2026; N=123 em 2026)"""
    fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
    df_validos = df_silver_26[(df_silver_26['consumo'] > 0) & (df_silver_26['is_dia_letivo'] == 1)]
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
        rotulo = f"Ano {ano} (Média: {sub['consumo'].mean():.1f})" if ano < 2026 else f"Ano 2026 [Fev-Ago, N=123] (Média: {sub['consumo'].mean():.1f})"
        ax.bar(x + offset, medias, largura, label=rotulo, color=cores_ano[i], edgecolor='#334155', linewidth=0.8, zorder=3)
        
    ax.set_ylabel("Média Diária de Refeições Servidas", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Dia da Semana", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(nomes_dias, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=11.5)
    ax.set_ylim(0, 240)
    ax.legend(fontsize=10.5, frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', loc='upper right')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_08_perfil_semanal_por_ano_letivo.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 08 gerada.")

def gerar_figura_09_oferta_consumo_por_proteina():
    """Figura 9 - Oferta e consumo por tipo de proteína (2023 a 2025)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1) &
                             (df_silver_fato['proteina_tipo'].notna())]
    
    resumo = df_hist.groupby('proteina_tipo')['consumo'].agg(['mean', 'count']).sort_values('mean', ascending=True)
    resumo = resumo[resumo['count'] >= 5]
    
    y = np.arange(len(resumo))
    cores = sns.color_palette("Blues_d", len(resumo))
    bars = ax.barh(y, resumo['mean'], color=cores, edgecolor='#1e3a8a', height=0.55, zorder=3)
    
    for i, bar in enumerate(bars):
        w = bar.get_width()
        qtd = resumo['count'].iloc[i]
        ax.text(w + 3, bar.get_y() + bar.get_height()/2., f"{w:.1f} ref (n = {qtd})",
                ha='left', va='center', fontsize=11, fontweight='semibold', color='#1e293b')
        
    ax.set_yticks(y)
    ax.set_yticklabels(resumo.index.str.title(), fontsize=11.5, fontweight='semibold')
    ax.set_xlabel("Média de Refeições Servidas por Almoço", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11.5)
    ax.set_xlim(0, max(resumo['mean']) * 1.25)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_09_oferta_consumo_por_proteina.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 09 gerada.")

def gerar_figura_10_consumo_conforme_tecnica():
    """Figura 10 - Consumo conforme técnica de preparo (2023 a 2025)"""
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1) &
                             (df_silver_fato['preparo_tipo'].notna())]
    
    resumo = df_hist.groupby('preparo_tipo')['consumo'].agg(['mean', 'count', 'std']).sort_values('mean', ascending=True)
    y = np.arange(len(resumo))
    cores = ['#93c5fd', '#3b82f6', '#1d4ed8']
    bars = ax.barh(y, resumo['mean'], color=cores, edgecolor='#1e3a8a', height=0.5, zorder=3)
    
    for i, bar in enumerate(bars):
        w = bar.get_width()
        qtd = resumo['count'].iloc[i]
        ax.text(w + 3, bar.get_y() + bar.get_height()/2., f"{w:.1f} ref (n = {qtd})",
                ha='left', va='center', fontsize=11.5, fontweight='semibold', color='#1e293b')
        
    ax.set_yticks(y)
    ax.set_yticklabels([t.capitalize() for t in resumo.index], fontsize=11.5, fontweight='semibold')
    ax.set_xlabel("Média de Refeições Servidas", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11.5)
    ax.set_xlim(0, max(resumo['mean']) * 1.22)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_10_consumo_conforme_tecnica_preparo.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 10 gerada.")

def gerar_figura_11_consumo_por_faixa_chuva():
    """Figura 11 - Consumo por faixa de precipitação (Open-Meteo, 2023 a 2025; N=495)"""
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
    bars = ax.bar(ordem_faixas, medias, color=cores, edgecolor='#0f172a', width=0.55, zorder=3)
    
    for i, bar in enumerate(bars):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 3, f"{h:.1f}\n(n={contagens[i]})",
                ha='center', va='bottom', fontsize=11, fontweight='semibold', color='#1e293b')
        
    ax.set_ylabel("Média de Refeições Servidas", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Intensidade de Precipitação Pluviométrica Diária (Open-Meteo)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11)
    ax.tick_params(axis='y', labelsize=11.5)
    ax.set_ylim(0, max(medias) * 1.25)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_11_consumo_por_faixa_precipitacao.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 11 gerada.")

def gerar_figura_12_relacao_temperatura_consumo():
    """Figura 12 - Relação entre temperatura máxima e consumo (Open-Meteo, 2023 a 2025; N=495)"""
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1) &
                             (df_silver_fato['temperature_2m_max'].notna())]
    
    ax.scatter(df_hist['temperature_2m_max'], df_hist['consumo'], color='#2563eb', alpha=0.6, edgecolors='none', s=45, label='Dias Letivos', zorder=3)
    
    sns.regplot(data=df_hist, x='temperature_2m_max', y='consumo', ax=ax, scatter=False,
                color='#dc2626', line_kws={'linewidth': 2.2, 'label': 'Tendência Linear Ajustada'})
    
    corr = df_hist['temperature_2m_max'].corr(df_hist['consumo'])
    ax.text(0.04, 0.90, f"Coeficiente de Pearson: r = {corr:.3f}", transform=ax.transAxes,
            fontsize=12, fontweight='bold', color='#1e293b',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='#f8fafc', edgecolor='#cbd5e1'))
    
    ax.set_xlabel("Temperatura Máxima Prevista (°C - Open-Meteo)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Refeições Servidas no Almoço", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=11.5)
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_12_relacao_temperatura_maxima_consumo.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 12 gerada.")

def gerar_figura_13_autocorrelacao_temporal():
    """Figura 13 - Funções de autocorrelação temporal (ACF série diária, 2023 a 2025; N=495)"""
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    df_hist = df_silver_fato[(df_silver_fato['ano'].isin([2023, 2024, 2025])) & 
                             (df_silver_fato['consumo'] > 0) & 
                             (df_silver_fato['is_dia_letivo'] == 1)].sort_values('data_iso')
    
    serie = df_hist['consumo'].reset_index(drop=True)
    n_lags = 20
    acfs = [serie.autocorr(lag=k) for k in range(1, n_lags + 1)]
    lags = np.arange(1, n_lags + 1)
    
    ax.stem(lags, acfs, linefmt='b-', markerfmt='bo', basefmt='k-', label='Autocorrelação Empírica')
    
    ci = 1.96 / np.sqrt(len(serie))
    ax.axhspan(-ci, ci, alpha=0.15, color='#38bdf8', label=f'Intervalo de Confiança assintótico (95%) [±{ci:.3f}]')
    ax.axhline(0, color='#0f172a', linewidth=1)
    
    ax.scatter([5, 10], [acfs[4], acfs[9]], color='#dc2626', s=90, zorder=5, label='Picos do Ciclo Semanal (Lags 5 e 10)')
    ax.text(5, acfs[4] + 0.04, f"Lag 5: {acfs[4]:.3f}", ha='center', fontsize=11, fontweight='bold', color='#dc2626')
    ax.text(10, acfs[9] + 0.04, f"Lag 10: {acfs[9]:.3f}", ha='center', fontsize=11, fontweight='bold', color='#dc2626')
    
    ax.set_xlabel("Defasagem Temporal em Dias Letivos Úteis (Lags)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Autocorrelação Linear de Pearson", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(lags)
    ax.tick_params(axis='both', labelsize=11)
    ax.set_ylim(-0.15, max(acfs) * 1.25)
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_13_funcoes_autocorrelacao_temporal.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 13 gerada.")

def gerar_figura_14_ranking_features_rf():
    """Figura 14 - Ranking de importância dos atributos (Random Forest, Camada Gold)"""
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
    bars = ax.barh(y, importancias, color=cores, edgecolor='#1e293b', height=0.6, zorder=3)
    
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.005, bar.get_y() + bar.get_height()/2., f"{w*100:.1f}%",
                ha='left', va='center', fontsize=11, fontweight='semibold', color='#1e293b')
        
    ax.set_yticks(y)
    ax.set_yticklabels(features, fontsize=11, fontweight='semibold')
    ax.invert_yaxis()
    ax.set_xlabel("Importância Relativa por Redução Média de Impureza (Gini)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11)
    ax.set_xlim(0, 0.32)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_14_ranking_importancia_atributos_rf.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 14 gerada.")

def gerar_figura_15_correlacao_atributos():
    """Figura 15 - Correlação de Pearson dos atributos com o consumo (Recalculada da Gold até 31/08/2026; N=568)"""
    fig, ax = plt.subplots(figsize=(10.5, 6.2), dpi=300)
    
    atributos_config = [
        ("Consumo mesmo dia sem. anterior (Lag 5)", "consumo_mesmo_dia_sem_passada"),
        ("Média móvel de consumo (5 dias úteis)", "media_movel_5d"),
        ("Média móvel de consumo (10 dias úteis)", "media_movel_10d"),
        ("Consumo do dia letivo anterior (Lag 1)", "lag_1_dia_letivo"),
        ("Dia da Semana: Quarta-feira", "is_quarta"),
        ("Proteína do Cardápio: Carne Bovina", "proteina_bovina"),
        ("Precipitação Pluviométrica Diária (mm)", "precipitation_sum"),
        ("Proteína do Cardápio: Peixe", "proteina_peixe"),
        ("Temperatura Máxima Prevista (°C)", "temperature_2m_max"),
        ("Dia da Semana: Sexta-feira", "is_sexta"),
    ]
    
    dados = []
    for rotulo, col in atributos_config:
        sub = df_gold_26[[col, 'consumo']].dropna()
        r = float(sub[col].corr(sub['consumo']))
        n_obs = len(sub)
        dados.append((rotulo, r, n_obs))
        
    dados = sorted(dados, key=lambda x: x[1], reverse=True)
    rotulos = [d[0] for d in dados]
    correlacoes = [d[1] for d in dados]
    n_obs = [d[2] for d in dados]
    y_pos = np.arange(len(rotulos))
    
    cores = ['#16a34a' if r > 0 else '#dc2626' for r in correlacoes]
    bars = ax.barh(y_pos, correlacoes, color=cores, edgecolor='#0f172a', height=0.58, zorder=3)
    ax.invert_yaxis()
    
    for i, bar in enumerate(bars):
        w = bar.get_width()
        pos_x = w + 0.02 if w >= 0 else w - 0.02
        ha = 'left' if w >= 0 else 'right'
        ax.text(pos_x, bar.get_y() + bar.get_height()/2., f"{w:+.3f} (n={n_obs[i]})",
                ha=ha, va='center', fontsize=10.5, fontweight='bold', color='#1e293b')
        
    ax.axvline(0, color='#0f172a', linewidth=1.2, zorder=4)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(rotulos, fontsize=11, fontweight='semibold')
    ax.set_xlabel("Coeficiente de Correlação Linear de Pearson com a Catraca Real (r)", fontsize=12, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11)
    ax.set_xlim(-0.35, 0.82)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_15_correlacao_atributos_consumo_pearson.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 15 gerada dinamicamente da base Gold.")

# ==============================================================================
# FIGURAS 16 A 28: PARTE 2 - RESULTADOS OPERACIONAIS DE 2026 E COMPARATIVOS
# ==============================================================================

def gerar_figura_16_decomposicao_efeito_compensatorio():
    """Figura 16 - Decomposição do efeito compensatório (Saldo vs Desvios Diários; N=458, N=123, N=73)"""
    fig, ax = plt.subplots(figsize=(10.5, 6.0), dpi=300)
    
    regimes = [
        '1. Reservas Discentes\n(2023–2025; N=458)',
        '2. Nutricionista\n(Fev–Ago/2026; N=123)',
        '3. Modelo Híbrido 50/50\n(Coorte 2026; N=73)'
    ]
    saldo_liquido = [-6578, +1898, +608]
    desvios_absolutos = [12410, 3224, 1474]
    
    x = np.arange(len(regimes))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, saldo_liquido, largura, label='Saldo Líquido Anual Aparente (Soma Algébrica)', color='#2563eb', edgecolor='#1e40af', zorder=3)
    b2 = ax.bar(x + largura/2, desvios_absolutos, largura, label='Desvios Diários Reais (|Sobra| + |Déficit|)', color='#d97706', edgecolor='#b45309', zorder=3)
    
    for bar in b1:
        h = bar.get_height()
        pos_y = h + 250 if h > 0 else h - 600
        va = 'bottom' if h > 0 else 'top'
        ax.text(bar.get_x() + bar.get_width()/2., pos_y, f"{h:+d}", ha='center', va=va, fontsize=12, fontweight='bold', color='#1e40af')
        
    for bar in b2:
        h = bar.get_height()
        # Headroom garantido para 12.410 sem colisão
        ax.text(bar.get_x() + bar.get_width()/2., h + 250, f"{h:,}".replace(',', '.'), ha='center', va='bottom', fontsize=12, fontweight='bold', color='#b45309')
        
    ax.axhline(0, color='#0f172a', linewidth=1.2, zorder=4)
    ax.set_ylabel("Quantidade Acumulada de Refeições", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Regime de Planejamento e Recorte Amostral Avaliado", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(regimes, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=11)
    ax.set_ylim(-8500, 16000)
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_16_decomposicao_efeito_compensatorio.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 16 gerada (com folga total em 12.410).")

def gerar_figura_17_painel_anual_sobras_faltas():
    """Figura 17 - Painel anual de sobras e faltas acumuladas (2023 a 2025: N=181, N=122, N=155)"""
    fig, ax = plt.subplots(figsize=(10.0, 5.8), dpi=300)
    
    anos = ['Ano 2023\n(N=181 datas)', 'Ano 2024\n(N=122 datas)', 'Ano 2025\n(N=155 datas)']
    faltas_potenciais = [1174, 4524, 3796]
    sobras_potenciais = [1916, 334, 666]
    
    x = np.arange(len(anos))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, faltas_potenciais, largura, label='Déficit Potencial Acumulado (Subdimensionamento)', color='#dc2626', edgecolor='#991b1b', zorder=3)
    b2 = ax.bar(x + largura/2, sobras_potenciais, largura, label='Sobra Potencial Acumulada (Sobredimensionamento)', color='#2563eb', edgecolor='#1e40af', zorder=3)
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 75, f"{h:,} ref".replace(',', '.'), ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#991b1b')
        
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 75, f"{h:,} ref".replace(',', '.'), ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#1e40af')
        
    ax.set_ylabel("Quantidade Anual de Refeições", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Ano Letivo sob Regime de Reservas Voluntárias dos Discentes (2023 a 2025; N=458)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(anos, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=11)
    ax.set_ylim(0, 5800)
    ax.legend(fontsize=11, loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_17_painel_anual_sobras_faltas.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 17 gerada (com folga total em 4.524).")

def gerar_figura_18_melhor_mae_cenarios():
    """Figura 18 - Melhor MAE por cenário de informação e horizonte (2026 até 31/08; N=73 datas pareadas)"""
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=300)
    
    cenarios = [
        "1. Inercial\n(t+2; N=73)",
        "2. Calendário\n(t+2; N=73)",
        "3. Cardápio\n(t+2; N=73)",
        "4. Clima C2\n(t+2; N=73)",
        "5. Reforecast C3\n(t+1; N=73)"
    ]
    maes = [26.82, 26.54, 26.12, 25.86, 21.72]
    modelos = ["SVR Linear", "SVR Linear", "SVR Linear", "Reg. Linear", "Ridge"]
    
    cores = ['#94a3b8', '#64748b', '#0284c7', '#0369a1', '#16a34a']
    bars = ax.bar(cenarios, maes, color=cores, edgecolor='#0f172a', width=0.55, zorder=3)
    
    for i, bar in enumerate(bars):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.4, f"{h:.2f} ref\n({modelos[i]})",
                ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1e293b')
        
    ax.set_ylabel("Erro Médio Absoluto (MAE em Refeições/Dia)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Cenário de Informação e Horizonte Temporal (Coorte Pareada 2026; N=73 datas)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=11)
    ax.set_ylim(0, 32)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_18_melhor_mae_por_cenario_horizonte.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 18 gerada (N=73).")

def gerar_figura_19_regressao_linear_clima():
    """Figura 19 - Comparação da regressão linear no horizonte t+2, com e sem clima (N=73)"""
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    
    cenarios = ['Cenário 1: Sem Clima\n(Base + Cardápio)', 'Cenário 2: Com Open-Meteo\n(Base + Cardápio + Clima)']
    maes = [27.33, 25.86]
    r2s = [0.371, 0.394]
    
    cores = ['#94a3b8', '#0284c7']
    bars = ax.bar(cenarios, maes, color=cores, edgecolor='#0f172a', width=0.45, zorder=3)
    
    for i, bar in enumerate(bars):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.5, f"MAE: {h:.2f} ref/dia\nR² = {r2s[i]:.3f}",
                ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#0f172a')
        
    # Anotação do ganho relativo
    ax.annotate("Redução de 1,47 ref/dia (-5,4%)\nR² elevado de 0,371 para 0,394",
                xy=(1, 25.86), xytext=(0.5, 30.5),
                arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.8),
                fontsize=11, fontweight='bold', color='#0284c7', ha='center',
                bbox=dict(boxstyle="round,pad=0.4", facecolor='#f0f9ff', edgecolor='#0284c7', lw=1.2))
    
    ax.set_ylabel("Erro Médio Absoluto (MAE em Refeições/Dia)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Configuração de Entrada no Horizonte t+2 (Coorte 2026; N=73 datas)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=11)
    ax.set_ylim(0, 35)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_19_comparacao_regressao_linear_t2_clima.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 19 gerada (N=73).")

def gerar_figura_20_comparacao_horizontes_5_algoritmos():
    """Figura 20 - Comparação do MAE entre os horizontes t+2 e t+1 para 5 algoritmos (N=73)"""
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=300)
    
    algoritmos = ['Lasso', 'Ridge', 'SVR', 'XGBoost', 'CatBoost']
    mae_t2 = [29.12, 28.38, 26.82, 28.47, 28.55]
    mae_t1 = [28.64, 27.82, 25.26, 27.46, 27.57]
    
    x = np.arange(len(algoritmos))
    largura = 0.35
    
    ax.bar(x - largura/2, mae_t2, largura, label='Horizonte t+2: Compras (10 a 14 dias)', color='#ea580c', edgecolor='#9a3412', zorder=3)
    ax.bar(x + largura/2, mae_t1, largura, label='Horizonte t+1: Preparo (3 a 7 dias)', color='#2563eb', edgecolor='#1e40af', zorder=3)
    
    for i in range(len(algoritmos)):
        ganho = (mae_t2[i] - mae_t1[i]) / mae_t2[i] * 100
        ax.text(x[i], max(mae_t2[i], mae_t1[i]) + 0.8, f"-{ganho:.1f}%", ha='center', va='bottom',
                fontsize=10.5, fontweight='bold', color='#16a34a')
        
    ax.set_ylabel("Erro Médio Absoluto (MAE em Refeições/Dia)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Algoritmo de Aprendizado de Máquina (Cenário-Base; N=73 datas pareadas)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(algoritmos, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=11)
    ax.set_ylim(0, 34)
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_20_comparacao_horizontes_5_algoritmos.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 20 gerada (5 algoritmos; N=73).")

def gerar_figura_21_ranking_modelos():
    """Figura 21 - Comparação entre modelos preditivos e nutricionista (Top 10 + Humano; N=73)"""
    fig, ax = plt.subplots(figsize=(10.5, 6.2), dpi=300)
    
    candidatos = [
        "1. Ridge (L2)",
        "2. Lasso (L1)",
        "3. ElasticNet",
        "4. Nutricionista (Benchmark Humano)",
        "5. Huber Regressor",
        "6. SVR Linear",
        "7. CatBoost",
        "8. LightGBM",
        "9. XGBoost",
        "10. Bayesian Ridge",
        "11. Random Forest"
    ]
    maes = [21.72, 21.82, 22.04, 23.37, 23.48, 24.26, 23.97, 24.18, 24.59, 24.62, 24.95]
    r2s = [0.495, 0.491, 0.485, 0.380, 0.420, 0.435, 0.415, 0.410, 0.385, 0.382, 0.370]
    
    y = np.arange(len(candidatos))
    cores = ['#10b981', '#10b981', '#10b981', '#f59e0b', '#3b82f6', '#3b82f6', '#64748b', '#64748b', '#64748b', '#64748b', '#64748b']
    bars = ax.barh(y, maes, color=cores, edgecolor='#0f172a', height=0.58, zorder=3)
    ax.invert_yaxis()
    
    for i, bar in enumerate(bars):
        w = bar.get_width()
        ax.text(w + 0.3, bar.get_y() + bar.get_height()/2., f"MAE: {w:.2f} | R²: {r2s[i]:.3f}",
                ha='left', va='center', fontsize=10.5, fontweight='semibold', color='#0f172a')
        
    ax.set_yticks(y)
    ax.set_yticklabels(candidatos, fontsize=11, fontweight='semibold')
    ax.set_xlabel("Erro Médio Absoluto (MAE em Refeições/Dia na Coorte N=73)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='x', labelsize=11)
    ax.set_xlim(0, 31)
    
    ax.axvline(23.37, color='#f59e0b', linestyle='--', linewidth=1.5, label='Benchmark Nutricionista (MAE: 23,37 ref/dia)')
    ax.legend(fontsize=10.5, loc='lower right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_21_ranking_modelos.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 21 gerada (Top 10 + Humano; N=73).")

def gerar_figura_22_sobras_faltas_politicas():
    """Figura 22 - Sobra e déficit potenciais nas políticas simuladas (N=73)"""
    fig, ax = plt.subplots(figsize=(11, 5.8), dpi=300)
    
    politicas = [
        "1. Nutricionista Isolada",
        "2. IA Pura (Ridge)",
        "3. Modelo Híbrido 50/50",
        "4. Híbrido + Margem 12",
        "5. IA + Conformal P85"
    ]
    sobras = [1874, 1057, 1041, 1488, 2072]
    faltas = [485, 529, 433, 126, 157]
    
    x = np.arange(len(politicas))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, sobras, largura, label='Sobras Potenciais (Risco Desperdício)', color='#3b82f6', edgecolor='#1e40af', zorder=3)
    b2 = ax.bar(x + largura/2, faltas, largura, label='Faltas Potenciais (Risco Desassistência)', color='#ef4444', edgecolor='#991b1b', zorder=3)
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 30, f"{h}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1e40af')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 30, f"{h}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#991b1b')
        
    ax.set_ylabel("Total Acumulado de Refeições (Coorte N=73 datas)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Política Operacional Avaliada", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(politicas, fontsize=11, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=11)
    ax.set_ylim(0, 2400)
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_22_sobras_faltas_politicas.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 22 gerada (N=73).")

def gerar_figura_23_fronteira_hibrido():
    """Figura 23 - Fronteira de equilíbrio do modelo híbrido (Alfa 0 a 1 em N=73)"""
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=300)
    
    pesos_ia = np.array([0, 10, 20, 30, 40, 50, 60, 62.5, 70, 80, 90, 100])
    maes = np.array([23.37, 22.45, 21.68, 21.05, 20.52, 20.19, 20.03, 20.03, 20.25, 20.65, 21.15, 21.72])
    
    ax.plot(pesos_ia, maes, marker='o', color='#2563eb', linewidth=2.5, markersize=7.5, label='Curva MAE da Combinação Linear Híbrida', zorder=3)
    
    # Destaque do Mínimo Global Numérico
    ax.scatter([60], [20.03], color='#7c3aed', s=150, zorder=5, label='Mínimo Global Numérico: α=60%–62,5% (MAE = 20,03 ref/dia)')
    ax.annotate("Mínimo Global Numérico\nα = 60,0% | MAE = 20,03 ref/dia",
                xy=(60, 20.03), xytext=(65, 21.4),
                arrowprops=dict(arrowstyle="->", color='#7c3aed', lw=1.8),
                fontsize=10.5, fontweight='bold', color='#7c3aed',
                bbox=dict(boxstyle="round,pad=0.4", facecolor='#f5f3ff', edgecolor='#7c3aed', lw=1.2))
    
    # Destaque do Ponto Operacional 50/50
    ax.scatter([50], [20.19], color='#dc2626', s=160, zorder=5, label='Configuração Operacional: 50% IA + 50% Nutri (MAE = 20,19 ref/dia)')
    ax.annotate("Configuração Operacional Recomendada\n50% IA + 50% Nutricionista\nMAE = 20,19 ref/dia (+0,16 ref do mínimo)",
                xy=(50, 20.19), xytext=(15, 22.2),
                arrowprops=dict(arrowstyle="->", color='#dc2626', lw=1.8),
                fontsize=10.5, fontweight='bold', color='#dc2626',
                bbox=dict(boxstyle="round,pad=0.4", facecolor='#fef2f2', edgecolor='#dc2626', lw=1.2))
    
    ax.set_xlabel("Ponderação Atribuída ao Modelo de Inteligência Artificial [α] (%)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Erro Médio Absoluto (MAE em Refeições/Dia)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(np.arange(0, 101, 10))
    ax.set_xticklabels([f"{p}%" for p in np.arange(0, 101, 10)], fontsize=11)
    ax.tick_params(axis='y', labelsize=11)
    ax.set_ylim(19.5, 24.2)
    ax.legend(fontsize=10.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_23_fronteira_equilibrio_modelo_hibrido.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 23 gerada (N=73).")

def gerar_figura_24_distribuicao_erros_diarios():
    """Figura 24 - Distribuição estimada dos erros diários de planejamento (KDE em N=73)"""
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=300)
    
    # Carregar previsões de Monte Carlo N=73
    df_mc = pd.read_csv(os.path.join(ROOT_DIR, "dissertacao/recalculos_qualificacao_20260831/previsoes_diarias_2026_monte_carlo_n73.csv"), sep=';')
    erro_nutri = df_mc['reserva_nutri'] - df_mc['y_real']
    erro_ia = df_mc['pred_ia'] - df_mc['y_real']
    erro_hib = df_mc['pred_hibrido_50_50'] - df_mc['y_real']
    
    sns.kdeplot(erro_nutri, ax=ax, label='Nutricionista Isolada (Viés +9,5 ref; MAE 23,37)', color='#ea580c', linewidth=2.2, fill=True, alpha=0.15)
    sns.kdeplot(erro_ia, ax=ax, label='IA Pura Ridge (Viés +7,2 ref; MAE 21,72)', color='#2563eb', linewidth=2.2, fill=True, alpha=0.15)
    sns.kdeplot(erro_hib, ax=ax, label='Modelo Híbrido 50/50 (Viés +8,3 ref; MAE 20,19 - Maior Pico)', color='#10b981', linewidth=2.5, fill=True, alpha=0.20)
    
    ax.axvline(0, color='#0f172a', linestyle='--', linewidth=1.5, label='Erro Zero (Dimensionamento Perfeito)')
    ax.set_xlabel("Erro Diário de Planejamento [Planejado - Consumo Real] (Refeições/Dia)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Densidade de Probabilidade Estimada (KDE)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=11)
    ax.set_xlim(-60, 80)
    ax.legend(fontsize=10.5, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_24_distribuicao_erros_diarios.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 24 gerada (N=73 datas pareadas).")

def gerar_figura_25_margens_seguranca_conformal():
    """Figura 25 - Efeito das margens de segurança conformal (N=73)"""
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=300)
    
    politicas = [
        "1. IA Pura (Sem margem)",
        "2. Conformal P75 (+7 ref)",
        "3. Conformal P85 (+14 ref)",
        "4. Conformal P90 (+23 ref)",
        "5. Híbrido 50/50 Puro",
        "6. Híbrido + Margem 12"
    ]
    taxa_falta = [42.5, 21.9, 13.7, 9.6, 30.1, 17.8]
    sobra_media = [14.5, 21.0, 28.4, 37.1, 14.3, 20.4]
    
    x = np.arange(len(politicas))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, taxa_falta, largura, label='% Dias Letivos com Déficit Potencial', color='#ef4444', edgecolor='#991b1b', zorder=3)
    b2 = ax.bar(x + largura/2, sobra_media, largura, label='Sobra Média Diária (Refeições/Dia)', color='#3b82f6', edgecolor='#1e40af', zorder=3)
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.8, f"{h:.1f}%", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#991b1b')
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 0.8, f"{h:.1f}", ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1e40af')
        
    ax.set_ylabel("Percentual (%) / Quantidade de Refeições", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Política de Dimensionamento Decisório (Coorte 2026; N=73 datas)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(politicas, fontsize=10.5, fontweight='semibold', rotation=15, ha='right')
    ax.tick_params(axis='y', labelsize=11)
    ax.set_ylim(0, 50)
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_25_margens_seguranca_conformal.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 25 gerada (N=73).")

def gerar_figura_26_simulacao_monte_carlo():
    """Figura 26 - Simulação de faixas de risco operacional (Monte Carlo em N=73)"""
    fig, ax = plt.subplots(figsize=(12, 6), dpi=300)
    df_mc = pd.read_csv(os.path.join(ROOT_DIR, "dissertacao/recalculos_qualificacao_20260831/previsoes_diarias_2026_monte_carlo_n73.csv"), sep=';')
    df_mc['data_dt'] = pd.to_datetime(df_mc['data_iso'])
    
    ax.fill_between(df_mc['data_dt'], df_mc['mc_p10_minimo'], df_mc['mc_p95_teto_seguranca'],
                    color='#e0f2fe', alpha=0.7, label='Faixa de Incerteza Estocástica P10 a P95')
    ax.fill_between(df_mc['data_dt'], df_mc['mc_p50_mediana'], df_mc['mc_p80_prudencial'],
                    color='#bae6fd', alpha=0.7, label='Faixa Prudencial P50 a P80 (Recomendada para Compras)')
    
    ax.plot(df_mc['data_dt'], df_mc['pred_ia'], color='#0284c7', linewidth=2.0, label='Previsão Central da IA (Ridge)')
    ax.plot(df_mc['data_dt'], df_mc['pred_ia_conformal_p85'], color='#0d9488', linewidth=2.2, linestyle='--', label='Cenário Prudencial Conformal P85')
    ax.plot(df_mc['data_dt'], df_mc['reserva_nutri'], color='#dc2626', linewidth=2.0, linestyle=':', label='Quantitativo da Nutricionista')
    ax.plot(df_mc['data_dt'], df_mc['y_real'], color='#0f172a', linewidth=2.2, marker='o', markersize=4, label='Consumo Real da Catraca')
    
    ax.set_ylabel("Quantidade Diária de Refeições", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Data do Atendimento Letivo (Fevereiro a Agosto de 2026; N=73 datas pareadas)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=11)
    # Eixo Y expandido para 295 para não cortar o pico do P95 (273,3 ref)
    ax.set_ylim(50, 295)
    ax.legend(fontsize=10.5, loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1', ncol=2)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_26_simulacao_monte_carlo.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 26 gerada (com teto em 295 ref; N=73).")

def gerar_figura_27_tradeoff_custo_atendimento():
    """Figura 27 - Custo potencial das sobras e frequência de dias sem déficit (N=73)"""
    fig, ax = plt.subplots(figsize=(10.5, 5.8), dpi=300)
    
    politicas = [
        "IA Pura (Ridge)",
        "Híbrido 50/50",
        "Nutricionista Isolada",
        "Conformal P75 (+7)",
        "Híbrido + Margem 12",
        "Conformal P85 (+14)"
    ]
    taxa_atendimento = [57.5, 69.9, 56.2, 78.1, 82.2, 86.3]
    sobras_ref = [1057, 1041, 1874, 1534, 1488, 2072]
    PRECO_REFEICAO_2026 = 14.00
    custo_sobras = [s * PRECO_REFEICAO_2026 for s in sobras_ref]
    cores = ['#3b82f6', '#10b981', '#ea580c', '#06b6d4', '#15803d', '#8b5cf6']
    
    for i in range(len(politicas)):
        ax.scatter(custo_sobras[i], taxa_atendimento[i], color=cores[i], s=170, zorder=5, edgecolor='#0f172a', linewidth=1.3)
        ax.text(custo_sobras[i] + 400, taxa_atendimento[i], 
                f"{politicas[i]} (R$ {custo_sobras[i]:,.0f})",
                fontsize=10.5, fontweight='bold', color='#0f172a', va='center')
        
    ax.set_xlabel("Custo Financeiro Potencial de Sobras (R$ na Coorte N=73 a R$ 14,00/refeição)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_ylabel("Taxa de Garantia do Atendimento Estudantil (%)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.tick_params(axis='both', labelsize=11)
    ax.set_ylim(50, 92)
    ax.set_xlim(13000, 36000)
    
    ax.axhspan(80, 92, alpha=0.1, color='#22c55e', label='Faixa Recomendada de Segurança Alimentar (≥ 80% dos dias sem falta)')
    ax.legend(fontsize=10.5, loc='lower right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_27_tradeoff_custo_atendimento.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 27 gerada (N=73).")

def gerar_figura_28_comparacao_historica_consolidada():
    """Figura 28 - Comparação histórica consolidada dos períodos e modelos (Painel Duplo; N=458 e N=73)"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.2), dpi=300)
    
    regimes = [
        "1. Reservas Discentes\n(2023–25; N=458)",
        "2. Nutricionista\n(2026; N=73)",
        "3. Híbrido +12\n(2026; N=73)"
    ]
    protecao = [36.2, 56.2, 82.2]
    maes = [34.80, 23.37, 24.81]
    
    # Painel A: Proteção Operacional
    cores_a = ['#ef4444', '#f59e0b', '#10b981']
    bars_a = ax1.bar(regimes, protecao, color=cores_a, edgecolor='#0f172a', width=0.52, zorder=3)
    for bar in bars_a:
        h = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., h + 1.8, f"{h:.1f}%", ha='center', va='bottom', fontsize=12, fontweight='bold', color='#0f172a')
    ax1.set_ylabel("Dias sem Déficit Potencial (%)", fontsize=12, fontweight='semibold', color='#0f172a')
    ax1.set_title("A. Proteção Operacional ao Comparecimento Discente", fontsize=12.5, fontweight='bold', color='#0f172a', pad=10)
    ax1.set_ylim(0, 100)
    ax1.tick_params(axis='x', labelsize=10.5)
    ax1.tick_params(axis='y', labelsize=11)
    
    # Painel B: Erro Médio Absoluto
    cores_b = ['#ef4444', '#3b82f6', '#10b981']
    bars_b = ax2.bar(regimes, maes, color=cores_b, edgecolor='#0f172a', width=0.52, zorder=3)
    for bar in bars_b:
        h = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., h + 0.7, f"{h:.2f} ref", ha='center', va='bottom', fontsize=12, fontweight='bold', color='#0f172a')
    ax2.set_ylabel("Erro Médio Absoluto Diário (MAE em Refeições)", fontsize=12, fontweight='semibold', color='#0f172a')
    ax2.set_title("B. Acurácia Preditiva Média do Dimensionamento", fontsize=12.5, fontweight='bold', color='#0f172a', pad=10)
    ax2.set_ylim(0, 42)
    ax2.tick_params(axis='x', labelsize=10.5)
    ax2.tick_params(axis='y', labelsize=11)
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_28_comparacao_historica_consolidada.png')
    salvar_figura(caminho, dpi=300)
    plt.close()
    print("Figura 28 gerada (Painel duplo sem sobreposição).")

def gerar_todas_figuras():
    print("=== INICIANDO GERAÇÃO OFICIAL DAS FIGURAS AUDITADAS (ATÉ 31/08/2026) ===")
    gerar_figura_07_perfil_semanal_consumo()
    gerar_figura_08_perfil_semanal_por_ano()
    gerar_figura_09_oferta_consumo_por_proteina()
    gerar_figura_10_consumo_conforme_tecnica()
    gerar_figura_11_consumo_por_faixa_chuva()
    gerar_figura_12_relacao_temperatura_consumo()
    gerar_figura_13_autocorrelacao_temporal()
    gerar_figura_14_ranking_features_rf()
    gerar_figura_15_correlacao_atributos()
    gerar_figura_16_decomposicao_efeito_compensatorio()
    gerar_figura_17_painel_anual_sobras_faltas()
    gerar_figura_18_melhor_mae_cenarios()
    gerar_figura_19_regressao_linear_clima()
    gerar_figura_20_comparacao_horizontes_5_algoritmos()
    gerar_figura_21_ranking_modelos()
    gerar_figura_22_sobras_faltas_politicas()
    gerar_figura_23_fronteira_hibrido()
    gerar_figura_24_distribuicao_erros_diarios()
    gerar_figura_25_margens_seguranca_conformal()
    gerar_figura_26_simulacao_monte_carlo()
    gerar_figura_27_tradeoff_custo_atendimento()
    gerar_figura_28_comparacao_historica_consolidada()
    print("=== TODAS AS FIGURAS AUDITADAS FORAM GERADAS COM SUCESSO! ===")

if __name__ == '__main__':
    gerar_todas_figuras()
