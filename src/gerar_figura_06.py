import matplotlib.pyplot as plt
import matplotlib.patches as patches

def criar_figura_06_fluxo_operacional(caminho_saida="dissertacao/figuras/figura_06_fluxo_operacional_artefato.png"):
    # Dimensões e resolução de alto impacto acadêmico
    fig, ax = plt.subplots(figsize=(12, 12.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Paleta de Cores
    c_navy = '#1e3a8a'      # Azul Marinho Principal
    c_slate = '#334155'     # Cinza Ardósia Escuro
    c_teal = '#0f766e'      # Verde Petróleo (Preparo)
    c_amber = '#c2410c'     # Laranja Âmbar (Compras)
    c_border = '#cbd5e1'    # Borda sutil
    c_bg_subtle = '#f8fafc' # Fundo neutro
    c_blue_accent = '#2563eb'

    # ====================================================
    # 1. BLOCO SUPERIOR: DISPARADOR SEMANAL (y: 83.5 a 97.5)
    # ====================================================
    w_top = 90
    h_top = 14.0
    x_top = 5
    y_top = 83.5

    # Painel
    box_top = patches.FancyBboxPatch((x_top, y_top), w_top, h_top, boxstyle="round,pad=0.2,rounding_size=1.0",
                                     facecolor='#ffffff', edgecolor=c_border, linewidth=1.4, zorder=2)
    ax.add_patch(box_top)

    # Cabeçalho do topo
    h_head_top = 3.8
    head_top = patches.FancyBboxPatch((x_top, y_top + h_top - h_head_top), w_top, h_head_top,
                                      boxstyle="round,pad=0.2,rounding_size=1.0",
                                      facecolor=c_navy, edgecolor=c_navy, linewidth=1, zorder=3)
    ax.add_patch(head_top)
    ax.add_patch(patches.Rectangle((x_top, y_top + h_top - h_head_top), w_top, 1.2,
                                   facecolor=c_navy, edgecolor=c_navy, zorder=3))

    ax.text(x_top + 2.5, y_top + h_top - 1.9, "DISPARADOR SEMANAL: SEXTA-FEIRA (14h00)",
            fontsize=11.5, fontweight='bold', color='#ffffff', va='center', zorder=4)
    ax.text(x_top + w_top - 2.5, y_top + h_top - 1.9, "Ingestão Automática de Dados",
            fontsize=9.0, fontweight='bold', color='#ffffff', va='center', ha='right', zorder=4,
            bbox=dict(boxstyle="round,pad=0.25", facecolor=(1, 1, 1, 0.22), edgecolor='none'))

    # 4 Cards internos compactos de insumos
    insumos = [
        ("Histórico Catraca", "Série de consumo auditada"),
        ("Cardápio Semanal", "Perfil proteico e cocção"),
        ("Previsão do Tempo", "Chuva e temperatura (API)"),
        ("Calendário Letivo", "Filtro de dias úteis ativos")
    ]
    w_pill = 20.2
    gap_pill = 2.1
    x_pill_start = 7.3
    y_pill = 85.0
    h_pill = 7.0

    for i, (titulo_i, desc_i) in enumerate(insumos):
        xi = x_pill_start + i * (w_pill + gap_pill)
        pill = patches.FancyBboxPatch((xi, y_pill), w_pill, h_pill, boxstyle="round,pad=0.2,rounding_size=0.6",
                                      facecolor=c_bg_subtle, edgecolor='#e2e8f0', linewidth=1.2, zorder=4)
        ax.add_patch(pill)
        ax.text(xi + w_pill/2, y_pill + 4.7, titulo_i, fontsize=9.2, fontweight='bold',
                color=c_navy, ha='center', va='center', zorder=5)
        ax.text(xi + w_pill/2, y_pill + 2.2, desc_i, fontsize=7.8,
                color=c_slate, ha='center', va='center', zorder=5)

    # Setas saindo do topo para os dois horizontes
    ax.annotate('', xy=(26.5, 78.5), xytext=(26.5, 83.5),
                arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=1.8, shrinkA=1, shrinkB=1, mutation_scale=13),
                zorder=6)
    ax.annotate('', xy=(73.5, 78.5), xytext=(73.5, 83.5),
                arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=1.8, shrinkA=1, shrinkB=1, mutation_scale=13),
                zorder=6)

    # ====================================================
    # 2. HORIZONTE t+1: PREPARO DIÁRIO (y: 42.5 a 78.5)
    # ====================================================
    w_card = 43.5
    h_card = 36.0
    x_t1 = 5
    y_cards = 42.5

    box_t1 = patches.FancyBboxPatch((x_t1, y_cards), w_card, h_card, boxstyle="round,pad=0.2,rounding_size=1.0",
                                    facecolor='#ffffff', edgecolor=c_border, linewidth=1.4, zorder=2)
    ax.add_patch(box_t1)

    # Cabeçalho t+1 (com duas linhas integradas para nunca haver sobreposição)
    h_head_mid = 5.2
    head_t1 = patches.FancyBboxPatch((x_t1, y_cards + h_card - h_head_mid), w_card, h_head_mid,
                                     boxstyle="round,pad=0.2,rounding_size=1.0",
                                     facecolor=c_teal, edgecolor=c_teal, linewidth=1, zorder=3)
    ax.add_patch(head_t1)
    ax.add_patch(patches.Rectangle((x_t1, y_cards + h_card - h_head_mid), w_card, 1.2,
                                   facecolor=c_teal, edgecolor=c_teal, zorder=3))

    ax.text(x_t1 + 2.2, y_cards + h_card - 1.8, "HORIZONTE t+1: PREPARO DIÁRIO",
            fontsize=10.5, fontweight='bold', color='#ffffff', va='center', zorder=4)
    ax.text(x_t1 + 2.2, y_cards + h_card - 3.7, "Operação de Curto Prazo • Antecedência: 3 a 7 dias úteis",
            fontsize=8.0, fontweight='medium', color='#ccfbf1', va='center', zorder=4)

    itens_t1 = [
        ("INFORMAÇÕES DISPONÍVEIS",
         "Cardápio fechado (proteínas e técnicas de cocção);\n"
         "Previsão meteorológica refinada (curto prazo);\n"
         "Quantitativo planejado pela Nutricionista."),
        
        ("MODELO PREDITIVO RECOMENDADO",
         "Modelo Híbrido Ótimo (Blattberg & Hoch, 1990):\n"
         "• Fronteira de Pareto: 50% IA + 50% Nutricionista\n"
         "• Menor erro global da pesquisa: MAE = 21,43 ref/dia"),
        
        ("DIRETRIZ DE PROTEÇÃO (PERDA ASSIMÉTRICA)",
         "Margem de Segurança Contra Desabastecimento:\n"
         "• Margem Híbrida Calibrada (+12 refeições)  OU\n"
         "• Margem Conformal P75 (+10 refeições)"),
        
        ("FINALIDADE OPERACIONAL",
         "Apoiar degelo, corte, cocção e distribuição diária,\n"
         "evitando sobras sem expor estudantes ao desabastecimento.")
    ]

    y_cursor_t1 = y_cards + h_card - h_head_mid - 2.0
    for tit, dsc in itens_t1:
        ax.text(x_t1 + 2.2, y_cursor_t1, tit, fontsize=8.2, fontweight='bold', color=c_teal, va='top', zorder=5)
        ax.text(x_t1 + 2.2, y_cursor_t1 - 1.7, dsc, fontsize=7.6, color=c_slate, va='top', linespacing=1.28, zorder=5)
        y_cursor_t1 -= 7.4

    # ====================================================
    # 3. HORIZONTE t+2: COMPRAS E ESTOQUE (y: 42.5 a 78.5)
    # ====================================================
    x_t2 = 51.5
    box_t2 = patches.FancyBboxPatch((x_t2, y_cards), w_card, h_card, boxstyle="round,pad=0.2,rounding_size=1.0",
                                    facecolor='#ffffff', edgecolor=c_border, linewidth=1.4, zorder=2)
    ax.add_patch(box_t2)

    head_t2 = patches.FancyBboxPatch((x_t2, y_cards + h_card - h_head_mid), w_card, h_head_mid,
                                     boxstyle="round,pad=0.2,rounding_size=1.0",
                                     facecolor=c_amber, edgecolor=c_amber, linewidth=1, zorder=3)
    ax.add_patch(head_t2)
    ax.add_patch(patches.Rectangle((x_t2, y_cards + h_card - h_head_mid), w_card, 1.2,
                                   facecolor=c_amber, edgecolor=c_amber, zorder=3))

    ax.text(x_t2 + 2.2, y_cards + h_card - 1.8, "HORIZONTE t+2: COMPRAS E ESTOQUE",
            fontsize=10.5, fontweight='bold', color='#ffffff', va='center', zorder=4)
    ax.text(x_t2 + 2.2, y_cards + h_card - 3.7, "Planejamento de Longo Prazo • Antecedência: 10 a 14 dias úteis",
            fontsize=8.0, fontweight='medium', color='#ffedd5', va='center', zorder=4)

    itens_t2 = [
        ("INFORMAÇÕES DISPONÍVEIS",
         "Cardápio preliminar e calendário acadêmico oficial;\n"
         "Previsão climática antecipada via Open-Meteo;\n"
         "Sem quantitativo prévio da nutricionista."),
        
        ("MODELO PREDITIVO RECOMENDADO",
         "Regressão Linear Regularizada (Ridge com Clima):\n"
         "• Modelagem preditiva puramente autônoma (IA pura)\n"
         "• MAE = 28,67 ref/dia (supera baseline inercial)"),
        
        ("DIRETRIZ DE PROTEÇÃO (PERDA ASSIMÉTRICA)",
         "Blindagem de Suprimentos (Conformal Prediction):\n"
         "• Margem Conformal P85 (+19 refeições adicionadas)\n"
         "• Reduz taxa de falta alimentar de 43,4% para 15,7%"),
        
        ("FINALIDADE OPERACIONAL",
         "Disparar pedidos de compras de gêneros secos e estocáveis,\n"
         "com arredondamento para múltiplos de embalagem.")
    ]

    y_cursor_t2 = y_cards + h_card - h_head_mid - 2.0
    for tit, dsc in itens_t2:
        ax.text(x_t2 + 2.2, y_cursor_t2, tit, fontsize=8.2, fontweight='bold', color=c_amber, va='top', zorder=5)
        ax.text(x_t2 + 2.2, y_cursor_t2 - 1.7, dsc, fontsize=7.6, color=c_slate, va='top', linespacing=1.28, zorder=5)
        y_cursor_t2 -= 7.4

    # ====================================================
    # FAIXA DE TRANSIÇÃO: REFORECAST SEMANAL (y: 33.5 a 38.5)
    # ====================================================
    # Caixa elegante entre os blocos
    x_rf = 10
    w_rf = 80
    y_rf = 34.0
    h_rf = 4.2

    box_rf = patches.FancyBboxPatch((x_rf, y_rf), w_rf, h_rf, boxstyle="round,pad=0.2,rounding_size=0.8",
                                    facecolor='#eff6ff', edgecolor='#93c5fd', linewidth=1.3, zorder=4)
    ax.add_patch(box_rf)

    # Seta tracejada dinâmica saindo de t+2 (à direita) e entrando em t+1 (à esquerda)
    ax.annotate('', xy=(12.5, y_rf + h_rf/2), xytext=(87.5, y_rf + h_rf/2),
                arrowprops=dict(arrowstyle="-|>", color=c_blue_accent, lw=1.8, 
                                linestyle='--', shrinkA=2, shrinkB=2, mutation_scale=12),
                zorder=5)

    ax.text(50, y_rf + h_rf/2, 
            "Na sexta-feira seguinte: atualização preditiva (Reforecast) das mesmas refeições para o horizonte t+1",
            fontsize=8.0, fontweight='bold', color=c_blue_accent, ha='center', va='center', zorder=6,
            bbox=dict(boxstyle="square,pad=0.15", facecolor='#eff6ff', edgecolor='none'))

    # Setas verticais saindo da base dos cards para o bloco de Governança
    # Card t+1 desce direto para Governança
    ax.annotate('', xy=(26.5, 27.5), xytext=(26.5, 34.0),
                arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=1.8, shrinkA=1, shrinkB=1, mutation_scale=13),
                zorder=6)
    # Card t+2 desce direto para Governança
    ax.annotate('', xy=(73.5, 27.5), xytext=(73.5, 34.0),
                arrowprops=dict(arrowstyle="-|>", color='#64748b', lw=1.8, shrinkA=1, shrinkB=1, mutation_scale=13),
                zorder=6)

    # ====================================================
    # 4. BLOCO INFERIOR: GOVERNANÇA E CONTROLE (y: 8.5 a 27.5)
    # ====================================================
    y_bot = 8.5
    h_bot = 19.0
    box_bot = patches.FancyBboxPatch((x_top, y_bot), w_top, h_bot, boxstyle="round,pad=0.2,rounding_size=1.0",
                                     facecolor='#ffffff', edgecolor=c_border, linewidth=1.4, zorder=2)
    ax.add_patch(box_bot)

    head_bot = patches.FancyBboxPatch((x_top, y_bot + h_bot - h_head_top), w_top, h_head_top,
                                      boxstyle="round,pad=0.2,rounding_size=1.0",
                                      facecolor=c_navy, edgecolor=c_navy, linewidth=1, zorder=3)
    ax.add_patch(head_bot)
    ax.add_patch(patches.Rectangle((x_top, y_bot + h_bot - h_head_top), w_top, 1.2,
                                   facecolor=c_navy, edgecolor=c_navy, zorder=3))

    ax.text(x_top + 2.5, y_bot + h_bot - 1.9, "GOVERNANÇA DECISÓRIA, MODO SOMBRA E RETROALIMENTAÇÃO",
            fontsize=11.5, fontweight='bold', color='#ffffff', va='center', zorder=4)
    ax.text(x_top + w_top - 2.5, y_bot + h_bot - 1.9, "Auditoria Contínua & Compliance",
            fontsize=9.0, fontweight='bold', color='#ffffff', va='center', ha='right', zorder=4,
            bbox=dict(boxstyle="round,pad=0.25", facecolor=(1, 1, 1, 0.22), edgecolor='none'))

    # 3 Pilares em colunas perfeitamente espaçadas
    pilares = [
        ("Soberania Decisória (DSS)",
         "O artefato opera exclusivamente como\n"
         "apoio à decisão; a nutricionista gestora\n"
         "detém autoridade total para alterar o plano\n"
         "com base em fatores contextuais."),
        
        ("Modo Sombra (Shadow Run)",
         "Previsões, parâmetros climáticos e planos\n"
         "são salvos com timestamp imutável,\n"
         "garantindo rastreabilidade histórica e\n"
         "transparência para auditorias de controle."),
        
        ("Retroalimentação Ex-Post",
         "Confronto contínuo entre consumo real e\n"
         "quantitativo produzido (sobras e faltas),\n"
         "alimentando o ajuste dinâmico das bandas\n"
         "conformais e recalibração dos modelos.")
    ]

    w_col = 27.6
    gap_col = 2.4
    x_col_start = 7.2
    y_col_box = 10.2
    h_col_box = 12.0

    for i, (tit_p, dsc_p) in enumerate(pilares):
        xp = x_col_start + i * (w_col + gap_col)
        box_p = patches.FancyBboxPatch((xp, y_col_box), w_col, h_col_box, boxstyle="round,pad=0.2,rounding_size=0.6",
                                       facecolor=c_bg_subtle, edgecolor='#e2e8f0', linewidth=1.1, zorder=4)
        ax.add_patch(box_p)
        ax.text(xp + 1.8, y_col_box + h_col_box - 2.0, tit_p, 
                fontsize=8.8, fontweight='bold', color=c_navy, va='top', zorder=5)
        ax.text(xp + 1.8, y_col_box + h_col_box - 4.4, dsc_p, 
                fontsize=7.6, color=c_slate, va='top', linespacing=1.35, zorder=5)

    # Nota acadêmica de rodapé
    ax.text(5, 5.0, 
            "Nota: Margens com garantia de cobertura finita fundamentadas em Conformal Prediction (Angelopoulos & Bates, 2021).\n"
            "Modelo Híbrido fundamentado na teoria de combinação linear de julgamento e modelo de Blattberg & Hoch (1990).",
            fontsize=8.0, fontstyle='italic', color='#64748b', va='top')

    plt.tight_layout()
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close()
    print(f"Figura 6 recriada com sucesso em: {caminho_saida}")

if __name__ == '__main__':
    criar_figura_06_fluxo_operacional()
