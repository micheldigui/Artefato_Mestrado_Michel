import matplotlib.pyplot as plt
import numpy as np
import os

# Configurar estilo acadêmico limpo
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300

PASTA_SAIDA = r'f:\PROJETOS\ARTEFATO\dissertacao\figuras'
os.makedirs(PASTA_SAIDA, exist_ok=True)

# ==============================================================================
# 1. FIGURA 16: DECOMPOSIÇÃO DO EFEITO COMPENSATÓRIO (RECALCULADA)
# ==============================================================================
def gerar_figura_16_corrigida():
    fig, ax = plt.subplots(figsize=(10, 5.8), dpi=300)
    
    regimes = [
        '1. Reservas Discentes\n(2023–2025; N=458)',
        '2. Nutricionista\n(fev-ago/2026; N=140)',
        '3. Modelo Híbrido 50/50\n(coorte 2026; N=83)'
    ]
    # Valores exatos das Tabelas 3, 4 e 7
    saldo_liquido = [-6578, +2670, +800]
    desvios_absolutos = [12410, 4038, 1778]
    
    x = np.arange(len(regimes))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, saldo_liquido, largura, label='Saldo Líquido Aparente (Soma dos Desvios)', color='#2563eb', edgecolor='#1e40af')
    b2 = ax.bar(x + largura/2, desvios_absolutos, largura, label='Desvios Diários Potenciais (|Sobra| + |Déficit|)', color='#d97706', edgecolor='#b45309')
    
    # Rótulos nas barras
    for bar in b1:
        h = bar.get_height()
        pos_y = h + 250 if h > 0 else h - 550
        ax.text(bar.get_x() + bar.get_width()/2., pos_y, f"{h:+d}", ha='center', va='bottom' if h > 0 else 'top',
                fontsize=11.5, fontweight='bold', color='#1e40af')
        
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 250, f"{h:,}".replace(',', '.'), ha='center', va='bottom',
                fontsize=11.5, fontweight='bold', color='#b45309')
        
    ax.axhline(0, color='#0f172a', linewidth=1.2)
    ax.set_ylabel("Quantidade Acumulada de Refeições", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Regime de Planejamento e Amostra Avaliada", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(regimes, fontsize=11, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=11)
    ax.set_ylim(-8500, 14500)
    ax.grid(axis='y', linestyle='--', alpha=0.3, color='#94a3b8')
    ax.legend(fontsize=11, loc='upper left', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_16_decomposicao_efeito_compensatorio_atualizada.png')
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Figura 16 atualizada salva em: {caminho}")

# ==============================================================================
# 2. FIGURA 17: PAINEL ANUAL DE SOBRAS E FALTAS ACUMULADAS (RECALCULADA)
# ==============================================================================
def gerar_figura_17_corrigida():
    fig, ax = plt.subplots(figsize=(9.5, 5.5), dpi=300)
    
    anos = ['Ano 2023 (N=181)', 'Ano 2024 (N=157)', 'Ano 2025 (N=120)']
    # Valores exatos da Tabela 3
    faltas_potenciais = [1174, 4524, 3796]  # Total: 9.494 refeições
    sobras_potenciais = [1916, 334, 666]    # Total: 2.916 refeições
    
    x = np.arange(len(anos))
    largura = 0.35
    
    b1 = ax.bar(x - largura/2, faltas_potenciais, largura, label='Déficit Potencial Acumulado (Subdimensionamento)', color='#dc2626', edgecolor='#991b1b')
    b2 = ax.bar(x + largura/2, sobras_potenciais, largura, label='Sobra Potencial Acumulada (Sobredimensionamento)', color='#2563eb', edgecolor='#1e40af')
    
    for bar in b1:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 60, f"{h:,} ref".replace(',', '.'), ha='center', va='bottom',
                fontsize=11, fontweight='bold', color='#991b1b')
        
    for bar in b2:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., h + 60, f"{h:,} ref".replace(',', '.'), ha='center', va='bottom',
                fontsize=11, fontweight='bold', color='#1e40af')
        
    ax.set_ylabel("Quantidade Anual de Refeições", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xlabel("Período sob Regime de Reservas Voluntárias dos Discentes (2023 a 2025)", fontsize=12.5, fontweight='semibold', color='#0f172a')
    ax.set_xticks(x)
    ax.set_xticklabels(anos, fontsize=11.5, fontweight='semibold')
    ax.tick_params(axis='y', labelsize=11)
    ax.set_ylim(0, 5200)
    ax.grid(axis='y', linestyle='--', alpha=0.3, color='#94a3b8')
    ax.legend(fontsize=11, loc='upper right', frameon=True, facecolor='#ffffff', edgecolor='#cbd5e1')
    
    plt.tight_layout()
    caminho = os.path.join(PASTA_SAIDA, 'figura_17_painel_anual_sobras_faltas_atualizada.png')
    plt.savefig(caminho, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Figura 17 atualizada salva em: {caminho}")

gerar_figura_16_corrigida()
gerar_figura_17_corrigida()
