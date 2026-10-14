"""
Gerador das Novas Figuras Conceituais e Metodológicas (1 a 6) da Dissertação
Foco: MÁXIMA LEGIBILIDADE PARA IMPRESSÃO/LEITURA NA DISSERTAÇÃO (Word/PDF)
- Orientação: Horizontal (Landscape amplo: 15 x 7.5 polegadas, 300 DPI)
- Estrutura: Duas Camadas limpas e bem arejadas
- Conteúdo: SINTÉTICO (sem parágrafos longos, apenas termos-chave e conceitos essenciais)
- Tipografia: GRANDES FONTES (12pt a 15pt) e alto contraste para visualização imediata
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

PASTA_SAIDA = r"f:\PROJETOS\ARTEFATO\dissertacao\figuras"
os.makedirs(PASTA_SAIDA, exist_ok=True)

# Paleta Cromática Acadêmica Limpa
C_NAVY = '#0f172a'         # Slate 900
C_BLUE_DARK = '#1e3a8a'    # Blue 900
C_BLUE = '#2563eb'         # Blue 600
C_TEAL_DARK = '#134e4a'    # Teal 900
C_TEAL = '#0f766e'         # Teal 700
C_AMBER_DARK = '#78350f'   # Amber 900
C_AMBER = '#b45309'        # Amber 700
C_SLATE = '#1e293b'        # Slate 800 (texto com alto contraste)
C_BORDER = '#94a3b8'       # Slate 400
C_LINE = '#64748b'         # Slate 500

def salvar_figura(fig, nome_arquivo):
    caminho = os.path.join(PASTA_SAIDA, nome_arquivo)
    fig.tight_layout()
    fig.savefig(caminho, dpi=300, bbox_inches='tight', facecolor='#ffffff')
    plt.close(fig)
    print(f"[OK] {nome_arquivo} gerada com sucesso ({os.path.getsize(caminho):,} bytes)")

# ==============================================================================
# FIGURA 1: Aplicação da Design Science Research na Pesquisa
# ==============================================================================
def gerar_figura_01():
    fig, ax = plt.subplots(figsize=(15, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Container Camada 1: DSR
    c1 = patches.FancyBboxPatch((2, 53), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.5, zorder=1)
    ax.add_patch(c1)
    # Banner Camada 1
    b1_h = patches.FancyBboxPatch((4, 91.5), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=2)
    ax.add_patch(b1_h)
    ax.text(50, 93.6, "CAMADA 1: CICLO METODOLÓGICO DA DESIGN SCIENCE RESEARCH (PEFFERS ET AL., 2007)",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    # Container Camada 2: Dissertação
    c2 = patches.FancyBboxPatch((2, 3), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#f0fdfa', edgecolor='#99f6e4', linewidth=1.5, zorder=1)
    ax.add_patch(c2)
    # Banner Camada 2
    b2_f = patches.FancyBboxPatch((4, 4.2), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor=C_TEAL, edgecolor=C_TEAL, zorder=2)
    ax.add_patch(b2_f)
    ax.text(50, 6.3, "CAMADA 2: INSTANCIAÇÃO EMPÍRICA NA DISSERTAÇÃO (RESTAURANTE ESCOLAR DO IFES)",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    etapas = [
        ("1. Identificação\ndo Problema", "Definir a relevância e\nlacunas práticas da\ndemanda institucional.",
         "Incerteza diária;\nassimetria severa entre\nsobras e déficit de alunos."),
        ("2. Definição dos\nObjetivos", "Estabelecer metas\nquantitativas para o\nartefato preditivo.",
         "Previsões integradas para\ncompras (t+2) e\npreparo diário (t+1)."),
        ("3. Concepção e\nDesenvolvimento", "Construir a solução\nartefatual, pipeline de\ndados e modelos.",
         "Arquitetura Medallion,\nFeature Store Gold (106 vars)\ne torneio com 12 modelos."),
        ("4. Demonstração\nRetrospectiva", "Aplicar o artefato em\nambiente simulado ou\ncontexto real.",
         "Simulação Walk-Forward\nem 28 semanas de 2026 e\nhistórico 2023-2025."),
        ("5. Avaliação\nExperimental", "Medir o desempenho\ncomparativo frente aos\nmétodos vigentes.",
         "Torneio vs. Nutricionista,\nModelo Híbrido 50/50 e\nMargens Conformal P85."),
        ("6. Comunicação\nCientífica", "Disseminar o rigor e a\nutilidade prática da\nsolução artefatual.",
         "Dissertação de mestrado,\nartigos acadêmicos e\nrepositório no GitHub.")
    ]

    w_box = 14.5
    h_box = 33.0
    y_l1 = 56.5
    y_l2 = 10.5
    gap_x = 1.6
    x_start = 3.6

    for i, (tit, dsr_txt, diss_txt) in enumerate(etapas):
        x = x_start + i * (w_box + gap_x)

        # Caixa Camada 1
        b1 = patches.FancyBboxPatch((x, y_l1), w_box, h_box, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor='#ffffff', edgecolor='#93c5fd', linewidth=1.4, zorder=4)
        ax.add_patch(b1)
        hb1 = patches.FancyBboxPatch((x, y_l1 + h_box - 9.0), w_box, 9.0, boxstyle="round,pad=0.2,rounding_size=0.6",
                                     facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=5)
        ax.add_patch(hb1)
        ax.add_patch(patches.Rectangle((x, y_l1 + h_box - 9.0), w_box, 2.5, facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=5))
        ax.text(x + w_box/2, y_l1 + h_box - 4.5, tit, fontsize=10.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)
        ax.text(x + w_box/2, y_l1 + (h_box - 9.0)/2, dsr_txt, fontsize=9.8, color=C_SLATE,
                ha='center', va='center', zorder=6, linespacing=1.25)

        # Caixa Camada 2
        b2 = patches.FancyBboxPatch((x, y_l2), w_box, h_box, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor='#ffffff', edgecolor='#5eead4', linewidth=1.4, zorder=4)
        ax.add_patch(b2)
        hb2 = patches.FancyBboxPatch((x, y_l2 + h_box - 6.5), w_box, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                     facecolor=C_TEAL, edgecolor=C_TEAL, zorder=5)
        ax.add_patch(hb2)
        ax.add_patch(patches.Rectangle((x, y_l2 + h_box - 6.5), w_box, 2.5, facecolor=C_TEAL, edgecolor=C_TEAL, zorder=5))
        ax.text(x + w_box/2, y_l2 + h_box - 3.2, f"Etapa {i+1} no Projeto", fontsize=9.8, fontweight='bold',
                color='#ffffff', ha='center', va='center', zorder=6)
        ax.text(x + w_box/2, y_l2 + (h_box - 6.5)/2, diss_txt, fontsize=9.5, color=C_SLATE,
                ha='center', va='center', zorder=6, linespacing=1.25)

        # Conector vertical entre caixas (pelo canal y=43.5 a y=56.5)
        ax.annotate('', xy=(x + w_box/2, y_l2 + h_box + 0.5), xytext=(x + w_box/2, y_l1 - 0.5),
                    arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=1.8, mutation_scale=11), zorder=7)

        # Conector horizontal Camada 1
        if i < 5:
            ax.annotate('', xy=(x + w_box + gap_x - 0.1, y_l1 + h_box - 4.5), xytext=(x + w_box + 0.1, y_l1 + h_box - 4.5),
                        arrowprops=dict(arrowstyle="-|>", color=C_BORDER, lw=1.6, mutation_scale=9), zorder=7)

    # Rótulo central no vão
    ax.text(50, 50.0, "Instanciação Empírica e Operacional dos Conceitos DSR no Artefato da Pesquisa",
            fontsize=10.0, fontweight='bold', color=C_BLUE_DARK, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.35", facecolor='#ffffff', edgecolor='#bfdbfe', lw=1.2), zorder=8)

    salvar_figura(fig, "figura_01_aplicacao_dsr_pesquisa.png")

# ==============================================================================
# FIGURA 2: Síntese Metodológica da Pesquisa
# ==============================================================================
def gerar_figura_02():
    fig, ax = plt.subplots(figsize=(15, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Camada A
    c1 = patches.FancyBboxPatch((2, 53), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#eff6ff', edgecolor='#bfdbfe', linewidth=1.5, zorder=1)
    ax.add_patch(c1)
    b1_h = patches.FancyBboxPatch((4, 91.5), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=2)
    ax.add_patch(b1_h)
    ax.text(50, 93.6, "CAMADA A: INGESTÃO, ARQUITETURA DE DADOS E CARACTERIZAÇÃO EXPLORATÓRIA",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    # Camada B
    c2 = patches.FancyBboxPatch((2, 3), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#f0fdf4', edgecolor='#bbf7d0', linewidth=1.5, zorder=1)
    ax.add_patch(c2)
    b2_f = patches.FancyBboxPatch((4, 4.2), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor='#166534', edgecolor='#166534', zorder=2)
    ax.add_patch(b2_f)
    ax.text(50, 6.3, "CAMADA B: ENGENHARIA DE ATRIBUTOS, TORNEIO PREDITIVO E POLÍTICAS DE DECISÃO",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    blocos_cima = [
        ("1. Fontes Primárias", [
            "• Catraca eletrônica (consumo real)",
            "• Sistema SUAP (reservas dos alunos)",
            "• Cardápios semanais em PDF",
            "• Clima horário (API Open-Meteo)"
        ]),
        ("2. Camadas Medallion", [
            "• Bronze: dados brutos imutáveis",
            "• Silver: harmonização e tipagem",
            "• Calendário letivo e feriados",
            "• Rastreabilidade total com carimbo"
        ]),
        ("3. Análise Exploratória", [
            "• Padrões de assimetria da demanda",
            "• Efeito de tipos de carnes e cocção",
            "• Sensibilidade à chuva e temperatura",
            "• Autocorrelação e efeito memória"
        ])
    ]

    blocos_baixo = [
        ("4. Feature Store Gold", [
            "• 106 atributos computados",
            "• Lags inerciais (t-1 a t-5)",
            "• Médias e desvios móveis",
            "• Seleção de features sem leakage"
        ]),
        ("5. Validação Walk-Forward", [
            "• 28 semanas letivas de 2026",
            "• Emissões pontuais às sextas-feiras",
            "• Horizonte t+1: preparo (3 a 7 dias)",
            "• Horizonte t+2: compras (10 a 14 dias)"
        ]),
        ("6. Políticas de Decisão", [
            "• Torneio de 12 modelos preditivos",
            "• Modelo Híbrido Colaborativo (50/50)",
            "• Margens Conformal de Proteção P85",
            "• Mitigação drástica do déficit de alunos"
        ])
    ]

    w_card = 29.5
    h_card = 33.0
    gap_card = 3.5
    x_init = 4.0

    for i, (tit, itens) in enumerate(blocos_cima):
        x = x_init + i * (w_card + gap_card)
        b = patches.FancyBboxPatch((x, 56.5), w_card, h_card, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#3b82f6', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 56.5 + h_card - 6.5), w_card, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 56.5 + h_card - 6.5), w_card, 2.5, facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=5))
        ax.text(x + w_card/2, 56.5 + h_card - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 56.5 + h_card - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

        if i < 2:
            ax.annotate('', xy=(x + w_card + gap_card - 0.2, 56.5 + h_card/2), xytext=(x + w_card + 0.2, 56.5 + h_card/2),
                        arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=1.8, mutation_scale=11), zorder=7)

    for i, (tit, itens) in enumerate(blocos_baixo):
        x = x_init + i * (w_card + gap_card)
        b = patches.FancyBboxPatch((x, 10.5), w_card, h_card, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#10b981', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 10.5 + h_card - 6.5), w_card, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor='#065f46', edgecolor='#065f46', zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 10.5 + h_card - 6.5), w_card, 2.5, facecolor='#065f46', edgecolor='#065f46', zorder=5))
        ax.text(x + w_card/2, 10.5 + h_card - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 10.5 + h_card - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

        if i < 2:
            ax.annotate('', xy=(x + w_card + gap_card - 0.2, 10.5 + h_card/2), xytext=(x + w_card + 0.2, 10.5 + h_card/2),
                        arrowprops=dict(arrowstyle="-|>", color='#059669', lw=1.8, mutation_scale=11), zorder=7)

    # Conector Ortogonal Limpo no Vão Central
    x_b3 = x_init + 2 * (w_card + gap_card) + w_card/2
    x_b4 = x_init + w_card/2
    y_canal = 50.0

    ax.plot([x_b3, x_b3, x_b4, x_b4], [56.5, y_canal, y_canal, 43.5],
            color=C_SLATE, lw=2.0, linestyle='--', zorder=7)
    ax.annotate('', xy=(x_b4, 43.5), xytext=(x_b4, 44.8),
                arrowprops=dict(arrowstyle="-|>", color=C_SLATE, lw=2.0, mutation_scale=12), zorder=8)

    ax.text(50, y_canal, "Alimentação da Feature Store Gold e Modelagem Preditiva",
            fontsize=10.0, fontweight='bold', color=C_SLATE, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.35", facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.2), zorder=9)

    salvar_figura(fig, "figura_02_sintese_metodologica.png")

# ==============================================================================
# FIGURA 3: Pipeline de Dados em Camadas (Medallion)
# ==============================================================================
def gerar_figura_03():
    fig, ax = plt.subplots(figsize=(15, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    c1 = patches.FancyBboxPatch((2, 53), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#fff7ed', edgecolor='#fed7aa', linewidth=1.5, zorder=1)
    ax.add_patch(c1)
    b1_h = patches.FancyBboxPatch((4, 91.5), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor='#9a3412', edgecolor='#9a3412', zorder=2)
    ax.add_patch(b1_h)
    ax.text(50, 93.6, "CAMADA 1: ARMAZENAMENTO E TRATAMENTO ESTRUTURAL (BRONZE E SILVER)",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    c2 = patches.FancyBboxPatch((2, 3), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.5, zorder=1)
    ax.add_patch(c2)
    b2_f = patches.FancyBboxPatch((4, 4.2), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=2)
    ax.add_patch(b2_f)
    ax.text(50, 6.3, "CAMADA 2: ENGENHARIA DE FEATURES (GOLD) E CONSUMO ANALÍTICO-DECISÓRIO",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    c1_cards = [
        ("Fontes Primárias Brutas", "#78350f", [
            "• Catraca de refeições (atendimento)",
            "• Sistema SUAP (reservas registradas)",
            "• Cardápios semanais em PDF",
            "• Clima diário (Open-Meteo)"
        ]),
        ("Camada Bronze (Raw)", "#c2410c", [
            "• Dados brutos imutáveis",
            "• Preservação de formatos originais",
            "• Carimbo de data/hora na carga",
            "• Rastreabilidade total da origem"
        ]),
        ("Camada Silver (Conformed)", "#d97706", [
            "• Saneamento e tipagem padronizada",
            "• Normalização de textos do cardápio",
            "• Integração com calendário letivo",
            "• Tabela fato diária consolidada"
        ])
    ]

    c2_cards = [
        ("Camada Gold (Feature Store)", "#1e3a8a", [
            "• Matriz com 106 atributos computados",
            "• Lags históricos de demanda (t-1 a t-5)",
            "• Médias móveis e desvios móveis",
            "• Flags de atratividade e clima local"
        ]),
        ("Consumo: Análise Exploratória", "#2563eb", [
            "• Caracterização estatística da demanda",
            "• Identificação de padrões semanais",
            "• Relevância de proteínas e cocção",
            "• Diagnóstico do triênio 2023-2025"
        ]),
        ("Consumo: Modelagem e Decisão", "#0f766e", [
            "• Torneio preditivo Walk-Forward",
            "• Modelo Híbrido 50/50 (IA + Nutricionista)",
            "• Margens Conformal P85 (+19 refeições)",
            "• Suporte operacional a compras e preparo"
        ])
    ]

    w_card = 29.5
    h_card = 33.0
    gap_card = 3.5
    x_init = 4.0

    for i, (tit, cor_h, itens) in enumerate(c1_cards):
        x = x_init + i * (w_card + gap_card)
        b = patches.FancyBboxPatch((x, 56.5), w_card, h_card, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#fb923c', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 56.5 + h_card - 6.5), w_card, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=cor_h, edgecolor=cor_h, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 56.5 + h_card - 6.5), w_card, 2.5, facecolor=cor_h, edgecolor=cor_h, zorder=5))
        ax.text(x + w_card/2, 56.5 + h_card - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 56.5 + h_card - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

        if i < 2:
            ax.annotate('', xy=(x + w_card + gap_card - 0.2, 56.5 + h_card/2), xytext=(x + w_card + 0.2, 56.5 + h_card/2),
                        arrowprops=dict(arrowstyle="-|>", color='#ea580c', lw=1.8, mutation_scale=11), zorder=7)

    for i, (tit, cor_h, itens) in enumerate(c2_cards):
        x = x_init + i * (w_card + gap_card)
        b = patches.FancyBboxPatch((x, 10.5), w_card, h_card, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#60a5fa', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 10.5 + h_card - 6.5), w_card, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=cor_h, edgecolor=cor_h, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 10.5 + h_card - 6.5), w_card, 2.5, facecolor=cor_h, edgecolor=cor_h, zorder=5))
        ax.text(x + w_card/2, 10.5 + h_card - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 10.5 + h_card - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

        if i < 2:
            ax.annotate('', xy=(x + w_card + gap_card - 0.2, 10.5 + h_card/2), xytext=(x + w_card + 0.2, 10.5 + h_card/2),
                        arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=1.8, mutation_scale=11), zorder=7)

    # Conector Ortogonal
    x_silver = x_init + 2 * (w_card + gap_card) + w_card/2
    x_gold = x_init + w_card/2
    y_canal = 50.0

    ax.plot([x_silver, x_silver, x_gold, x_gold], [56.5, y_canal, y_canal, 43.5],
            color=C_BLUE_DARK, lw=2.0, linestyle='--', zorder=7)
    ax.annotate('', xy=(x_gold, 43.5), xytext=(x_gold, 44.8),
                arrowprops=dict(arrowstyle="-|>", color=C_BLUE_DARK, lw=2.0, mutation_scale=12), zorder=8)

    ax.text(50, y_canal, "Enriquecimento Temporal e Engenharia de Atributos (Silver → Gold)",
            fontsize=10.0, fontweight='bold', color=C_BLUE_DARK, ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.35", facecolor='#ffffff', edgecolor='#93c5fd', lw=1.2), zorder=9)

    salvar_figura(fig, "figura_03_pipeline_dados_camadas.png")

# ==============================================================================
# FIGURA 4: Protocolo de Modelagem e Validação Temporal (Walk-Forward)
# ==============================================================================
def gerar_figura_04():
    fig, ax = plt.subplots(figsize=(15, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    c1 = patches.FancyBboxPatch((2, 53), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#f8fafc', edgecolor='#cbd5e1', linewidth=1.5, zorder=1)
    ax.add_patch(c1)
    b1_h = patches.FancyBboxPatch((4, 91.5), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=2)
    ax.add_patch(b1_h)
    ax.text(50, 93.6, "CAMADA 1: DINÂMICA DA ORIGEM TEMPORAL SEMANAL (SEXTAS-FEIRAS - SEM VAZAMENTO)",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    c2 = patches.FancyBboxPatch((2, 3), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#f0fdfa', edgecolor='#99f6e4', linewidth=1.5, zorder=1)
    ax.add_patch(c2)
    b2_f = patches.FancyBboxPatch((4, 4.2), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor=C_TEAL, edgecolor=C_TEAL, zorder=2)
    ax.add_patch(b2_f)
    ax.text(50, 6.3, "CAMADA 2: HORIZONTES DE PREVISÃO E PROGRESSÃO SEQUENCIAL AO LONGO DE 2026",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    cards_l1 = [
        ("1. Treino em Expansão", C_NAVY, [
            "• Histórico auditado desde 2023",
            "• Treino até semana N-1 de cada ciclo",
            "• Re-treinamento semanal contínuo",
            "• Ordem cronológica estrita preservada"
        ]),
        ("2. Ponto de Decisão", C_AMBER, [
            "• Emissão às sextas-feiras (14h00)",
            "• Bloqueio absoluto de dados futuros",
            "• Congelamento das variáveis disponíveis",
            "• Geração simultânea de t+1 e t+2"
        ]),
        ("3. Avaliação Out-of-Sample", '#047857', [
            "• Teste cego nas semanas futuras",
            "• Métricas: MAE, RMSE, WAPE e R²",
            "• Aferição pontual de sobras de comida",
            "• Contabilização estrita do déficit de alunos"
        ])
    ]

    cards_l2 = [
        ("Horizonte t+1: Preparo", C_TEAL, [
            "• Antecedência de 3 a 7 dias letivos",
            "• Dimensionamento da cocção diária",
            "• Pareamento com a nutricionista",
            "• Base para Modelo Híbrido e Conformal"
        ]),
        ("Horizonte t+2: Compras", C_AMBER, [
            "• Antecedência de 10 a 14 dias letivos",
            "• Aquisição planejada de perecíveis",
            "• Baseado em histórico e cardápio",
            "• Avaliado com e sem meteorologia"
        ]),
        ("Iteração em 28 Semanas", C_BLUE_DARK, [
            "• Coorte de 09/fev a 28/ago de 2026",
            "• 83 datas pareadas com Nutricionista",
            "• Expansão progressiva do aprendizado",
            "• Robustez estatística em vários regimes"
        ])
    ]

    w_card = 29.5
    h_card = 33.0
    gap_card = 3.5
    x_init = 4.0

    for i, (tit, cor_h, itens) in enumerate(cards_l1):
        x = x_init + i * (w_card + gap_card)
        b = patches.FancyBboxPatch((x, 56.5), w_card, h_card, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 56.5 + h_card - 6.5), w_card, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=cor_h, edgecolor=cor_h, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 56.5 + h_card - 6.5), w_card, 2.5, facecolor=cor_h, edgecolor=cor_h, zorder=5))
        ax.text(x + w_card/2, 56.5 + h_card - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 56.5 + h_card - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

        if i < 2:
            ax.annotate('', xy=(x + w_card + gap_card - 0.2, 56.5 + h_card/2), xytext=(x + w_card + 0.2, 56.5 + h_card/2),
                        arrowprops=dict(arrowstyle="-|>", color=C_SLATE, lw=1.8, mutation_scale=11), zorder=7)

    for i, (tit, cor_h, itens) in enumerate(cards_l2):
        x = x_init + i * (w_card + gap_card)
        b = patches.FancyBboxPatch((x, 10.5), w_card, h_card, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#5eead4', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 10.5 + h_card - 6.5), w_card, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=cor_h, edgecolor=cor_h, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 10.5 + h_card - 6.5), w_card, 2.5, facecolor=cor_h, edgecolor=cor_h, zorder=5))
        ax.text(x + w_card/2, 10.5 + h_card - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 10.5 + h_card - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

    # Conectores verticais
    ax.annotate('', xy=(x_init + w_card/2, 43.5), xytext=(x_init + w_card/2, 56.5),
                arrowprops=dict(arrowstyle="-|>", color=C_TEAL, lw=2.0, mutation_scale=12), zorder=7)
    ax.annotate('', xy=(x_init + w_card + gap_card + w_card/2, 43.5), xytext=(x_init + w_card + gap_card + w_card/2, 56.5),
                arrowprops=dict(arrowstyle="-|>", color=C_AMBER, lw=2.0, mutation_scale=12), zorder=7)
    ax.annotate('', xy=(x_init + 2*(w_card + gap_card) + w_card/2, 43.5), xytext=(x_init + 2*(w_card + gap_card) + w_card/2, 56.5),
                arrowprops=dict(arrowstyle="-|>", color=C_BLUE_DARK, lw=2.0, mutation_scale=12), zorder=7)

    # Rótulos no vão
    ax.text(x_init + w_card/2, 50.0, "Alimenta t+1", fontsize=9.5, fontweight='bold', color=C_TEAL,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor='#ffffff', edgecolor='#99f6e4', lw=1.1), zorder=8)
    ax.text(x_init + w_card + gap_card + w_card/2, 50.0, "Alimenta t+2", fontsize=9.5, fontweight='bold', color=C_AMBER,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor='#ffffff', edgecolor='#fed7aa', lw=1.1), zorder=8)
    ax.text(x_init + 2*(w_card + gap_card) + w_card/2, 50.0, "Validação 2026", fontsize=9.5, fontweight='bold', color=C_BLUE_DARK,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor='#ffffff', edgecolor='#bfdbfe', lw=1.1), zorder=8)

    salvar_figura(fig, "figura_04_protocolo_modelagem_validacao.png")

# ==============================================================================
# FIGURA 5: Arquitetura Sistêmica do Artefato
# ==============================================================================
def gerar_figura_05():
    fig, ax = plt.subplots(figsize=(15, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    c1 = patches.FancyBboxPatch((2, 53), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#eff6ff', edgecolor='#bfdbfe', linewidth=1.5, zorder=1)
    ax.add_patch(c1)
    b1_h = patches.FancyBboxPatch((4, 91.5), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=2)
    ax.add_patch(b1_h)
    ax.text(50, 93.6, "CAMADA 1: NÚCLEO COMPUTACIONAL ANALÍTICO E PREDITIVO (PIPELINE PYTHON)",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    c2 = patches.FancyBboxPatch((2, 3), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#f0fdf4', edgecolor='#bbf7d0', linewidth=1.5, zorder=1)
    ax.add_patch(c2)
    b2_f = patches.FancyBboxPatch((4, 4.2), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor='#166534', edgecolor='#166534', zorder=2)
    ax.add_patch(b2_f)
    ax.text(50, 6.3, "CAMADA 2: AMBIENTE DE DECISÃO OPERACIONAL, GOVERNANÇA E GESTÃO DO RESTAURANTE",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    mods_top = [
        ("Módulo 1: Dados", [
            "• Ingestão Bronze",
            "• Saneamento Silver",
            "• Calendário acadêmico",
            "• API Open-Meteo"
        ]),
        ("Módulo 2: Features", [
            "• 106 variáveis Gold",
            "• Lags inerciais",
            "• Médias móveis",
            "• Seleção sem vazamento"
        ]),
        ("Módulo 3: Modelos", [
            "• Modelos lineares",
            "• Modelos em árvore",
            "• Previsões t+1 e t+2",
            "• Histórico de resíduos"
        ]),
        ("Módulo 4: Decisão", [
            "• Modelo Híbrido 50/50",
            "• Margens Conformal P85",
            "• Faixas de incerteza",
            "• Mitigação de déficits"
        ])
    ]

    w_top = 22.2
    h_top = 33.0
    gap_top = 2.4
    x_init_top = 4.0

    for i, (tit, itens) in enumerate(mods_top):
        x = x_init_top + i * (w_top + gap_top)
        b = patches.FancyBboxPatch((x, 56.5), w_top, h_top, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#3b82f6', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 56.5 + h_top - 6.5), w_top, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 56.5 + h_top - 6.5), w_top, 2.5, facecolor=C_BLUE_DARK, edgecolor=C_BLUE_DARK, zorder=5))
        ax.text(x + w_top/2, 56.5 + h_top - 3.2, tit, fontsize=11.0, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 56.5 + h_top - 10.5
        for item in itens:
            ax.text(x + 1.8, y_text, item, fontsize=10.0, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

        if i < 3:
            ax.annotate('', xy=(x + w_top + gap_top - 0.2, 56.5 + h_top/2), xytext=(x + w_top + 0.2, 56.5 + h_top/2),
                        arrowprops=dict(arrowstyle="-|>", color=C_BLUE, lw=1.8, mutation_scale=10), zorder=7)

    mods_bot = [
        ("Interface com a Nutricionista", '#047857', [
            "• Entrada do Quantitativo Institucional",
            "• Consulta a cenários preditivos diários",
            "• Ajustes operacionais e soberania final",
            "• Programação balanceada da cocção"
        ]),
        ("Interface com Suprimentos", C_AMBER, [
            "• Antecipação de compras t+2 (10-14 dias)",
            "• Dimensionamento de perecíveis e carnes",
            "• Mitigação de desperdícios e descartes",
            "• Pedidos regulares para fornecedores"
        ]),
        ("Auditoria e Governança", C_NAVY, [
            "• Registro de previsões com carimbo temporal",
            "• Confronto sistemático ex-post com catraca",
            "• Rastreabilidade total de alterações humanas",
            "• Repositório aberto e base para recalibração"
        ])
    ]

    w_bot = 29.5
    h_bot = 33.0
    gap_bot = 3.5
    x_init_bot = 4.0

    for i, (tit, cor_h, itens) in enumerate(mods_bot):
        x = x_init_bot + i * (w_bot + gap_bot)
        b = patches.FancyBboxPatch((x, 10.5), w_bot, h_bot, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#10b981', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 10.5 + h_bot - 6.5), w_bot, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=cor_h, edgecolor=cor_h, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 10.5 + h_bot - 6.5), w_bot, 2.5, facecolor=cor_h, edgecolor=cor_h, zorder=5))
        ax.text(x + w_bot/2, 10.5 + h_bot - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 10.5 + h_bot - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

    # Conectores verticais bidirecionais
    ax.annotate('', xy=(18.75, 43.5), xytext=(18.75, 56.5),
                arrowprops=dict(arrowstyle="<|-|>", color='#047857', lw=2.0, mutation_scale=11), zorder=7)
    ax.annotate('', xy=(51.75, 43.5), xytext=(51.75, 56.5),
                arrowprops=dict(arrowstyle="<|-|>", color=C_AMBER, lw=2.0, mutation_scale=11), zorder=7)
    ax.annotate('', xy=(84.75, 43.5), xytext=(84.75, 56.5),
                arrowprops=dict(arrowstyle="<|-|>", color=C_NAVY, lw=2.0, mutation_scale=11), zorder=7)

    ax.text(18.75, 50.0, "Decisão de Preparo (t+1)", fontsize=9.2, fontweight='bold', color='#047857',
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor='#ffffff', edgecolor='#a7f3d0', lw=1.1), zorder=8)
    ax.text(51.75, 50.0, "Planejamento Compras (t+2)", fontsize=9.2, fontweight='bold', color=C_AMBER,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor='#ffffff', edgecolor='#fed7aa', lw=1.1), zorder=8)
    ax.text(84.75, 50.0, "Auditoria e Governança", fontsize=9.2, fontweight='bold', color=C_NAVY,
            ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor='#ffffff', edgecolor='#cbd5e1', lw=1.1), zorder=8)

    salvar_figura(fig, "figura_05_arquitetura_sistemica_artefato.png")

# ==============================================================================
# FIGURA 6: Fluxo Operacional Integrado do Artefato
# ==============================================================================
def gerar_figura_06():
    fig, ax = plt.subplots(figsize=(15, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    c1 = patches.FancyBboxPatch((2, 53), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#fffbeb', edgecolor='#fde68a', linewidth=1.5, zorder=1)
    ax.add_patch(c1)
    b1_h = patches.FancyBboxPatch((4, 91.5), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor='#92400e', edgecolor='#92400e', zorder=2)
    ax.add_patch(b1_h)
    ax.text(50, 93.6, "CAMADA 1: CICLO DE COMPRAS DE SUPRIMENTOS (HORIZONTE t+2: 10 A 14 DIAS)",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    c2 = patches.FancyBboxPatch((2, 3), 96, 44, boxstyle="round,pad=0.2,rounding_size=1.0",
                                facecolor='#f0fdfa', edgecolor='#99f6e4', linewidth=1.5, zorder=1)
    ax.add_patch(c2)
    b2_f = patches.FancyBboxPatch((4, 4.2), 92, 4.3, boxstyle="round,pad=0.2,rounding_size=0.6",
                                  facecolor='#0f766e', edgecolor='#0f766e', zorder=2)
    ax.add_patch(b2_f)
    ax.text(50, 6.3, "CAMADA 2: CICLO DE PREPARO E COCÇÃO NA COZINHA (HORIZONTE t+1: 3 A 7 DIAS)",
            fontsize=12, fontweight='bold', color='#ffffff', ha='center', va='center', zorder=3)

    etapas_compras = [
        ("Etapa 1: Ingestão de Dados", C_AMBER, [
            "• Histórico auditado da catraca",
            "• Calendário letivo acadêmico",
            "• Cardápio preliminar da semana",
            "• Previsão climática estendida"
        ]),
        ("Etapa 2: Previsão para t+2", '#d97706', [
            "• Execução do modelo supervisionado",
            "• Feature Store na Camada Gold",
            "• Projeção diária para a Semana N+2",
            "• Emissão na sexta-feira às 14h00"
        ]),
        ("Etapa 3: Emissão do Pedido", '#78350f', [
            "• Quantitativo gerencial de compras",
            "• Pedido formal de carnes e insumos",
            "• Atendimento aos prazos do fornecedor",
            "• Controle preventivo de desperdícios"
        ])
    ]

    etapas_preparo = [
        ("Etapa 4: Atualização Semanal", '#0f766e', [
            "• Estimativa prévia da nutricionista",
            "• Previsão climática de curto prazo",
            "• Histórico auditado mais recente",
            "• Recalibração da matriz de entrada"
        ]),
        ("Etapa 5: Híbrido & Margem P85", '#047857', [
            "• Modelo Híbrido 50/50 (IA + Nutri)",
            "• Margem Conformal (+19 refeições)",
            "• 84,3% de proteção alimentar",
            "• Menor déficit do estudo (489 ref)"
        ]),
        ("Etapa 6: Cocção e Auditoria", C_BLUE_DARK, [
            "• Produção diária na cozinha da UAN",
            "• Soberania da decisão da nutricionista",
            "• Aferição real na catraca eletrônica",
            "• Registro imutável para governança"
        ])
    ]

    w_box = 29.5
    h_box = 33.0
    gap_box = 3.5
    x_init = 4.0

    for i, (tit, cor_h, itens) in enumerate(etapas_compras):
        x = x_init + i * (w_box + gap_box)
        b = patches.FancyBboxPatch((x, 56.5), w_box, h_box, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#f59e0b', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 56.5 + h_box - 6.5), w_box, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=cor_h, edgecolor=cor_h, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 56.5 + h_box - 6.5), w_box, 2.5, facecolor=cor_h, edgecolor=cor_h, zorder=5))
        ax.text(x + w_box/2, 56.5 + h_box - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 56.5 + h_box - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

        if i < 2:
            ax.annotate('', xy=(x + w_box + gap_box - 0.2, 56.5 + h_box/2), xytext=(x + w_box + 0.2, 56.5 + h_box/2),
                        arrowprops=dict(arrowstyle="-|>", color='#b45309', lw=1.8, mutation_scale=11), zorder=7)

    for i, (tit, cor_h, itens) in enumerate(etapas_preparo):
        x = x_init + i * (w_box + gap_box)
        b = patches.FancyBboxPatch((x, 10.5), w_box, h_box, boxstyle="round,pad=0.2,rounding_size=0.6",
                                   facecolor='#ffffff', edgecolor='#14b8a6', linewidth=1.4, zorder=4)
        ax.add_patch(b)
        hb = patches.FancyBboxPatch((x, 10.5 + h_box - 6.5), w_box, 6.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                                    facecolor=cor_h, edgecolor=cor_h, zorder=5)
        ax.add_patch(hb)
        ax.add_patch(patches.Rectangle((x, 10.5 + h_box - 6.5), w_box, 2.5, facecolor=cor_h, edgecolor=cor_h, zorder=5))
        ax.text(x + w_box/2, 10.5 + h_box - 3.2, tit, fontsize=11.5, fontweight='bold', color='#ffffff',
                ha='center', va='center', zorder=6)

        y_text = 10.5 + h_box - 10.5
        for item in itens:
            ax.text(x + 2.0, y_text, item, fontsize=10.2, color=C_SLATE, va='top', zorder=6)
            y_text -= 5.5

        if i < 2:
            ax.annotate('', xy=(x + w_box + gap_box - 0.2, 10.5 + h_box/2), xytext=(x + w_box + 0.2, 10.5 + h_box/2),
                        arrowprops=dict(arrowstyle="-|>", color='#0f766e', lw=1.8, mutation_scale=11), zorder=7)

    # Conector Ortogonal
    x_e3 = x_init + 2 * (w_box + gap_box) + w_box/2
    x_e4 = x_init + w_box/2
    y_canal = 50.0

    ax.plot([x_e3, x_e3, x_e4, x_e4], [56.5, y_canal, y_canal, 43.5],
            color='#0f766e', lw=2.0, linestyle='--', zorder=7)
    ax.annotate('', xy=(x_e4, 43.5), xytext=(x_e4, 44.8),
                arrowprops=dict(arrowstyle="-|>", color='#0f766e', lw=2.0, mutation_scale=12), zorder=8)

    ax.text(50, y_canal, "Avanço de 7 Dias: O Pedido de Compras se Converte no Ciclo de Preparo",
            fontsize=10.0, fontweight='bold', color='#0f766e', ha='center', va='center',
            bbox=dict(boxstyle="round,pad=0.35", facecolor='#ffffff', edgecolor='#5eead4', lw=1.2), zorder=9)

    salvar_figura(fig, "figura_06_fluxo_operacional_artefato.png")

if __name__ == "__main__":
    print("Iniciando geracao das novas Figuras 1 a 6 em formato horizontal (2 camadas, texto sintetico e legivel)...")
    gerar_figura_01()
    gerar_figura_02()
    gerar_figura_03()
    gerar_figura_04()
    gerar_figura_05()
    gerar_figura_06()
    print("Todas as 6 figuras foram recriadas com sucesso!")
