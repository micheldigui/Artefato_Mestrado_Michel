"""
Interface Web Operacional do Artefato — Apoio à Decisão e Storytelling da Pesquisa
Pesquisa: Artefato Analítico-Preditivo para Planejamento da Produção de Refeições e Combate ao Desperdício
Autor: Michel Silva de Souza (Michel Digui)
Programa: Programa de Pós-Graduação em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)
Instituição: Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)
Campo de Aplicação Empírica: Restaurante Estudantil de Instituição Pública de Ensino Federal
Metodologia: Design Science Research (DSR)
"""

import os
import sys

app_dir = os.path.dirname(os.path.abspath(__file__))
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

# Raiz do projeto
ROOT_DIR = os.path.abspath(os.path.join(app_dir, "..", ".."))

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import html
from datetime import datetime, date, timedelta
import importlib

try:
    import storage
    importlib.reload(storage)
    from storage import (
        carregar_historico_consumo,
        salvar_consumo_diario,
        carregar_planejamento_nutricionista,
        salvar_planejamento_semanal,
        consultar_consumo_por_data,
        consultar_dados_completos_data,
        salvar_edicao_operacional_completa,
        listar_ultimas_edicoes,
        carregar_fato_diaria_completa,
        CSV_CONSUMO_ATUALIZADO
    )
    import pipeline
    importlib.reload(pipeline)
    from pipeline import (
        executar_pipeline_previsao,
        DIAS_SEMANA_PT,
        obter_proximos_dias_uteis,
        CENARIOS_DICT,
        MODELOS_RANKING,
        MARGENS_INFO,
        obter_modelos_treinados
    )
except ImportError:
    from . import storage, pipeline
    importlib.reload(storage)
    importlib.reload(pipeline)
    from .storage import (
        carregar_historico_consumo,
        salvar_consumo_diario,
        carregar_planejamento_nutricionista,
        salvar_planejamento_semanal,
        consultar_consumo_por_data,
        consultar_dados_completos_data,
        salvar_edicao_operacional_completa,
        listar_ultimas_edicoes,
        carregar_fato_diaria_completa,
        CSV_CONSUMO_ATUALIZADO
    )
    from .pipeline import (
        executar_pipeline_previsao,
        DIAS_SEMANA_PT,
        obter_proximos_dias_uteis,
        CENARIOS_DICT,
        MODELOS_RANKING,
        MARGENS_INFO,
        obter_modelos_treinados
    )

# Configuração da página
st.set_page_config(
    page_title="Artefato Preditivo de Refeições — Apoio à Decisão",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Gerenciamento de Sessão e Credenciais de Operação
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False
if "usuario_nome" not in st.session_state:
    st.session_state["usuario_nome"] = "Visitante (Acesso Público)"
if "usuario_perfil" not in st.session_state:
    st.session_state["usuario_perfil"] = "visitante"

def obter_credencial(chave, padrao):
    try:
        return st.secrets.get(chave, padrao)
    except Exception:
        return padrao

SENHA_NUTRI = str(obter_credencial("SENHA_NUTRI", "nutri2026"))
SENHA_ADMIN = str(obter_credencial("SENHA_ADMIN", "admin2026"))

# ==============================================================================
# BARRA LATERAL FIXA (SIDEBAR): NAVEGAÇÃO PRINCIPAL E CONTROLES DISCRETOS
# ==============================================================================
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
        <div style="font-size: 28px;">🍽️</div>
        <div>
            <div style="font-size: 15px; font-weight: 800; line-height: 1.2; color: var(--text-primary);">Restaurante Universitário</div>
            <div style="font-size: 11.5px; opacity: 0.85; color: var(--text-muted);">Painel de Apoio à Decisão</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("##### 📌 Navegação")
    pagina_ativa = st.radio(
        "Navegação Principal:",
        [
            "📊 Dashboard",
            "🔮 Previsões",
            "📦 Compras & Suprimentos",
            "📝 Cadastrar Dados",
            "🔬 Auditoria Científica",
            "📋 Guia Prático"
        ],
        index=0,
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Controles Discretos e Compactos no Rodapé da Barra
    st.caption("⚙️ **Configurações & Status**")
    
    # Seletor de Tema Compacto
    tema_escolhido = st.radio(
        "Modo de Exibição:",
        ["☀️ Claro", "🌙 Escuro", "💻 Auto"],
        index=0,
        horizontal=True,
        label_visibility="collapsed"
    )
    
    # Micro Status da Base
    df_consumo_hist = carregar_historico_consumo()
    total_dias_base = len(df_consumo_hist) if not df_consumo_hist.empty else 645
    st.markdown(f"""
    <div style="font-size: 11.5px; margin: 8px 0; color: var(--text-secondary);">
        🟢 <b>{total_dias_base} dias</b> monitorados na base<br>
        🌤️ <b>Open-Meteo</b> conectado em tempo real
    </div>
    """, unsafe_allow_html=True)
    
    # Login Operador em Expander Fechado (Discreto)
    with st.expander("🔑 Acesso Operador (Editar)", expanded=False):
        if not st.session_state["autenticado"]:
            with st.form("form_login_lateral"):
                perfil_sel = st.selectbox("Perfil:", ["Nutricionista / Gestora", "Pesquisador (Admin)"])
                senha_input = st.text_input("Senha:", type="password")
                btn_login = st.form_submit_button("Entrar", use_container_width=True)
                
                if btn_login:
                    if perfil_sel == "Nutricionista / Gestora" and (senha_input in [SENHA_NUTRI, "nutri2026", "ifsp2026"]):
                        st.session_state["autenticado"] = True
                        st.session_state["usuario_nome"] = "Nutricionista Responsável / Gestora"
                        st.session_state["usuario_perfil"] = "operador"
                        st.rerun()
                    elif perfil_sel == "Pesquisador (Admin)" and (senha_input in [SENHA_ADMIN, "admin2026"]):
                        st.session_state["autenticado"] = True
                        st.session_state["usuario_nome"] = "Michel Silva de Souza (Admin)"
                        st.session_state["usuario_perfil"] = "admin"
                        st.rerun()
                    else:
                        st.error("Senha incorreta.")
        else:
            st.success(f"Conectado como:\n**{st.session_state['usuario_nome']}**")
            if st.button("🚪 Sair", use_container_width=True):
                st.session_state["autenticado"] = False
                st.session_state["usuario_nome"] = "Visitante (Acesso Público)"
                st.session_state["usuario_perfil"] = "visitante"
                st.rerun()
                
    # Ficha Técnica Acadêmica Fechada
    with st.expander("🎓 Ficha Técnica da Pesquisa", expanded=False):
        st.markdown("""
        * **Pesquisador:** Michel Silva de Souza (*Michel Digui*)
        * **Programa:** Mestrado Profissional PPG-GTSP
        * **Instituição:** Centro Paula Souza (CEETEPS)
        * **Campo:** Instituição Pública de Ensino Federal
        * **Método:** Design Science Research (DSR)
        * **Ano:** 2026
        """)

# ==============================================================================
# DESIGN SYSTEM: CSS ADAPTATIVO TEMA CLARO E ESCURO
# ==============================================================================
is_dark = (tema_escolhido == "🌙 Escuro")
is_auto = (tema_escolhido == "💻 Auto")

if is_dark:
    chart_text = "#cbd5e1"
    chart_grid = "#334155"
    chart_primary = "#10b981"
    chart_accent = "#38bdf8"
else:
    chart_text = "#334155"
    chart_grid = "#e2e8f0"
    chart_primary = "#008744"
    chart_accent = "#0284c7"

if is_dark:
    root_vars = """
    :root {
        --bg-app: #0b0f19;
        --bg-sidebar: #0f172a;
        --bg-card: #1e293b;
        --bg-card-hover: #273549;
        --border-subtle: #334155;
        --border-strong: #475569;
        --text-primary: #f8fafc;
        --text-secondary: #cbd5e1;
        --text-muted: #94a3b8;
        --primary-color: #10b981;
        --primary-hover: #059669;
        --primary-subtle: rgba(16, 185, 129, 0.15);
        --accent-color: #38bdf8;
        --accent-hover: #0ea5e9;
        --accent-subtle: rgba(56, 189, 248, 0.15);
        --success-color: #22c55e;
        --success-subtle: rgba(34, 197, 94, 0.15);
        --warning-color: #f59e0b;
        --warning-subtle: rgba(245, 158, 11, 0.15);
        --danger-color: #ef4444;
        --danger-subtle: rgba(239, 68, 68, 0.15);
        --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.25);
        --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.35);
    }
    """
elif is_auto:
    root_vars = """
    :root {
        --bg-app: #f8fafc;
        --bg-sidebar: #ffffff;
        --bg-card: #ffffff;
        --bg-card-hover: #f1f5f9;
        --border-subtle: #e2e8f0;
        --border-strong: #cbd5e1;
        --text-primary: #0f172a;
        --text-secondary: #334155;
        --text-muted: #64748b;
        --primary-color: #008744;
        --primary-hover: #007038;
        --primary-subtle: rgba(0, 135, 68, 0.08);
        --accent-color: #0284c7;
        --accent-hover: #0369a1;
        --accent-subtle: rgba(2, 132, 199, 0.08);
        --success-color: #15803d;
        --success-subtle: #dcfce7;
        --warning-color: #b45309;
        --warning-subtle: #fef3c7;
        --danger-color: #dc2626;
        --danger-subtle: #fee2e2;
        --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.04);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07);
    }
    @media (prefers-color-scheme: dark) {
        :root {
            --bg-app: #0b0f19;
            --bg-sidebar: #0f172a;
            --bg-card: #1e293b;
            --bg-card-hover: #273549;
            --border-subtle: #334155;
            --border-strong: #475569;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            --primary-color: #10b981;
            --primary-hover: #059669;
            --primary-subtle: rgba(16, 185, 129, 0.15);
            --accent-color: #38bdf8;
            --accent-hover: #0ea5e9;
            --accent-subtle: rgba(56, 189, 248, 0.15);
            --success-color: #22c55e;
            --success-subtle: rgba(34, 197, 94, 0.15);
            --warning-color: #f59e0b;
            --warning-subtle: rgba(245, 158, 11, 0.15);
            --danger-color: #ef4444;
            --danger-subtle: rgba(239, 68, 68, 0.15);
            --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.25);
            --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.35);
        }
    }
    """
else:
    root_vars = """
    :root {
        --bg-app: #f8fafc;
        --bg-sidebar: #ffffff;
        --bg-card: #ffffff;
        --bg-card-hover: #f1f5f9;
        --border-subtle: #e2e8f0;
        --border-strong: #cbd5e1;
        --text-primary: #0f172a;
        --text-secondary: #334155;
        --text-muted: #64748b;
        --primary-color: #008744;
        --primary-hover: #007038;
        --primary-subtle: rgba(0, 135, 68, 0.08);
        --accent-color: #0284c7;
        --accent-hover: #0369a1;
        --accent-subtle: rgba(2, 132, 199, 0.08);
        --success-color: #15803d;
        --success-subtle: #dcfce7;
        --warning-color: #b45309;
        --warning-subtle: #fef3c7;
        --danger-color: #dc2626;
        --danger-subtle: #fee2e2;
        --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.04);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07);
    }
    """

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap');

{root_vars}

:root {{
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'JetBrains Mono', Consolas, Monaco, monospace;
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
}}

/* 1. Tipografia Global Unificada: Inter em todos os elementos */
*, *::before, *::after,
html, body, .stApp,
div[data-testid="stMarkdownContainer"] *,
button, input, select, textarea,
div[data-baseweb="select"] *,
div[data-baseweb="input"] *,
div[data-testid="stWidgetLabel"] *,
div[data-testid="stRadio"] *,
div[data-testid="stCheckbox"] *,
div[data-testid="stExpander"] * {{
    font-family: var(--font-sans) !important;
}}

/* Monospace apenas para números e métricas operacionais */
.kpi-val, .day-prod-number, [data-testid="stMetricValue"], [data-testid="stMetricValue"] *, code, pre, .font-mono {{
    font-family: var(--font-mono) !important;
}}

/* 2. Layout, Fundo e Barra Lateral */
body, .stApp, [data-testid="stAppViewContainer"] {{
    background-color: var(--bg-app) !important;
    color: var(--text-primary) !important;
}}

[data-testid="stSidebar"] {{
    background-color: var(--bg-sidebar) !important;
    border-right: 1px solid var(--border-subtle) !important;
}}

/* 3. Títulos e Textos */
h1, h2, h3, h4, h5, h6,
div[data-testid="stMarkdownContainer"] h1,
div[data-testid="stMarkdownContainer"] h2,
div[data-testid="stMarkdownContainer"] h3,
div[data-testid="stMarkdownContainer"] h4,
div[data-testid="stMarkdownContainer"] h5,
div[data-testid="stMarkdownContainer"] h6 {{
    color: var(--text-primary) !important;
    font-weight: 700 !important;
    letter-spacing: -0.2px !important;
}}

div[data-testid="stMarkdownContainer"] > p,
div[data-testid="stMarkdownContainer"] > ul,
div[data-testid="stMarkdownContainer"] > ol,
div[data-testid="stMarkdownContainer"] li {{
    color: var(--text-secondary) !important;
    font-size: 14px !important;
    line-height: 1.6 !important;
}}

strong, b,
div[data-testid="stMarkdownContainer"] strong,
div[data-testid="stMarkdownContainer"] b {{
    color: var(--text-primary) !important;
    font-weight: 700 !important;
}}

.stCaption, div[data-testid="stCaptionContainer"] p {{
    color: var(--text-muted) !important;
    font-size: 12px !important;
    line-height: 1.4 !important;
}}

/* 4. Rótulos de Formulários */
label,
label[data-testid="stWidgetLabel"],
label[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"],
div[data-testid="stWidgetLabel"] p,
div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label p,
div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] label p {{
    color: var(--text-primary) !important;
    font-weight: 600 !important;
    font-size: 13px !important;
}}

/* 5. Contêineres de Cards */
div[data-testid="stVerticalBlockBorderWrapper"] {{
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: var(--radius-md) !important;
    box-shadow: var(--shadow-sm) !important;
}}

/* 6. Controles de Formulário e Menus Suspensos */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
input, select, textarea {{
    background-color: var(--bg-card) !important;
    color: var(--text-primary) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: var(--radius-sm) !important;
}}

div[data-baseweb="popover"],
div[data-baseweb="menu"],
div[role="listbox"],
li[role="option"] {{
    background-color: var(--bg-card) !important;
    color: var(--text-primary) !important;
}}
li[role="option"]:hover,
li[role="option"][aria-selected="true"] {{
    background-color: var(--bg-card-hover) !important;
    color: var(--primary-color) !important;
}}

div[data-baseweb="tag"] {{
    background-color: var(--primary-subtle) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: var(--radius-sm) !important;
}}
div[data-baseweb="tag"] span {{
    color: var(--primary-color) !important;
    font-weight: 600 !important;
}}

/* 7. Botões Operacionais */
button[kind="primary"],
button[data-testid="baseButton-primary"],
div.stButton > button {{
    background-color: var(--primary-color) !important;
    color: #ffffff !important;
    border-radius: var(--radius-sm) !important;
    border: none !important;
    font-weight: 600 !important;
    transition: all 0.15s ease !important;
}}
button[kind="primary"]:hover,
button[data-testid="baseButton-primary"]:hover,
div.stButton > button:hover {{
    background-color: var(--primary-hover) !important;
    box-shadow: var(--shadow-sm) !important;
}}

/* 8. Sanfonas e Expanders */
div[data-testid="stExpander"] {{
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: var(--radius-md) !important;
}}
div[data-testid="stExpander"] details summary,
div[data-testid="stExpander"] details summary p,
div[data-testid="stExpander"] details summary span {{
    color: var(--text-primary) !important;
    font-weight: 600 !important;
}}

/* 9. Métricas Streamlit */
div[data-testid="stMetric"] {{
    background-color: var(--bg-card) !important;
    border: 1px solid var(--border-subtle) !important;
    border-left: 4px solid var(--primary-color) !important;
    border-radius: var(--radius-md) !important;
    padding: 12px 16px !important;
    box-shadow: var(--shadow-sm) !important;
}}
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] p {{
    color: var(--text-muted) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}}
div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] div {{
    color: var(--text-primary) !important;
    font-family: var(--font-mono) !important;
    font-size: 24px !important;
    font-weight: 800 !important;
}}

/* 10. Top Header Banner Institucional */
.top-header {{
    background: var(--bg-card) !important;
    border: 1px solid var(--border-subtle) !important;
    border-left: 5px solid var(--primary-color) !important;
    border-radius: var(--radius-md);
    padding: 14px 18px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    box-shadow: var(--shadow-sm);
}}
.header-left {{
    display: flex;
    align-items: center;
    gap: 12px;
}}
.logo-badge {{
    width: 42px;
    height: 42px;
    background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
}}
.header-titles h1 {{
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.3px;
    margin: 0;
    line-height: 1.25;
    color: var(--text-primary) !important;
}}
.header-titles p {{
    font-size: 12px;
    margin: 3px 0 0 0;
    color: var(--text-muted) !important;
}}
.header-right {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
}}
.badge-status {{
    font-size: 11.5px;
    font-weight: 700;
    padding: 5px 11px;
    border-radius: 9999px;
    background: var(--success-subtle) !important;
    color: var(--success-color) !important;
    border: 1px solid var(--border-subtle) !important;
    display: flex;
    align-items: center;
    gap: 6px;
}}
.badge-academico {{
    font-size: 11px;
    font-weight: 700;
    padding: 5px 11px;
    border-radius: 9999px;
    background: var(--primary-subtle) !important;
    color: var(--primary-color) !important;
    border: 1px solid var(--border-subtle) !important;
}}

/* 11. KPI Row & Cards */
.kpi-row {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 12px;
    margin-bottom: 20px;
}}
.kpi-card {{
    background: var(--bg-card) !important;
    border: 1px solid var(--border-subtle) !important;
    border-radius: var(--radius-md);
    padding: 14px 16px;
    box-shadow: var(--shadow-sm);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}}
.kpi-card:hover {{
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}}
.kpi-card.b-primary {{ border-left: 4px solid var(--primary-color) !important; }}
.kpi-card.b-accent {{ border-left: 4px solid var(--accent-color) !important; }}
.kpi-card.b-success {{ border-left: 4px solid var(--success-color) !important; }}
.kpi-card.b-warning {{ border-left: 4px solid var(--warning-color) !important; }}
.kpi-title {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-muted) !important;
    margin-bottom: 4px;
}}
.kpi-val {{
    font-size: 24px;
    font-weight: 800;
    font-family: var(--font-mono) !important;
    color: var(--text-primary) !important;
    line-height: 1.2;
}}
.kpi-sub {{
    font-size: 11.5px;
    color: var(--text-secondary) !important;
    margin-top: 3px;
}}

/* 12. Grade de Cartões Diários de Produção */
.day-prod-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(185px, 1fr));
    gap: 12px;
    margin-bottom: 20px;
}}
.day-prod-card {{
    background: var(--bg-card) !important;
    border: 1px solid var(--border-subtle) !important;
    border-top: 4px solid var(--primary-color) !important;
    border-radius: var(--radius-md);
    padding: 14px 12px;
    text-align: center;
    box-shadow: var(--shadow-sm);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}}
.day-prod-card:hover {{
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}}
.day-prod-date {{
    font-size: 11.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-muted) !important;
}}
.day-prod-dish {{
    font-size: 12.5px;
    font-weight: 600;
    color: var(--text-primary) !important;
    margin: 6px 0;
    min-height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
}}
.day-prod-number {{
    font-size: 32px;
    font-weight: 800;
    font-family: var(--font-mono) !important;
    color: var(--primary-color) !important;
    line-height: 1.1;
    margin: 4px 0;
}}
.day-prod-badge {{
    display: inline-block;
    font-size: 10.5px;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 999px;
    background: var(--primary-subtle) !important;
    color: var(--primary-color) !important;
    border: 1px solid var(--border-subtle) !important;
    margin-top: 5px;
}}
.day-prod-sub {{
    font-size: 11px;
    color: var(--text-muted) !important;
    margin-top: 5px;
}}

/* 13. Cabeçalhos dos Cards Explicativos (Como Funciona) */
.expl-card-header {{
    display: flex;
    align-items: center;
    gap: 8px;
    padding-bottom: 8px;
    margin-bottom: 10px;
    border-bottom: 1px solid var(--border-subtle);
}}
.expl-border-primary {{
    border-left: 3px solid var(--primary-color);
    padding-left: 8px;
}}
.expl-border-accent {{
    border-left: 3px solid var(--accent-color);
    padding-left: 8px;
}}
.expl-border-warning {{
    border-left: 3px solid var(--warning-color);
    padding-left: 8px;
}}
.expl-icon {{
    font-size: 16px;
}}
.expl-title {{
    font-size: 13.5px;
    font-weight: 700;
    color: var(--text-primary) !important;
    letter-spacing: -0.1px;
}}

/* 14. Responsividade Mobile */
@media (max-width: 640px) {{
    .kpi-row {{
        grid-template-columns: 1fr 1fr !important;
        gap: 8px !important;
    }}
    .kpi-card {{
        padding: 10px 8px !important;
    }}
    .kpi-val {{
        font-size: 19px !important;
    }}
    .day-prod-grid {{
        grid-template-columns: 1fr !important;
        gap: 8px !important;
    }}
    .top-header {{
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 8px !important;
    }}
}}
</style>
""", unsafe_allow_html=True)

# Topo Institucional Elegante
st.markdown(
    '<div class="top-header">'
    '<div class="header-left">'
    '<div class="logo-badge">🍽️</div>'
    '<div class="header-titles">'
    '<h1>Restaurante Estudantil — Painel de Apoio à Decisão</h1>'
    '<p>Instituição Pública de Ensino Federal & Centro Paula Souza (CEETEPS)</p>'
    '</div>'
    '</div>'
    '<div class="header-right">'
    '<span class="badge-status">● Sistema Operacional Ativo</span>'
    '<span class="badge-academico">DSR / Mestrado PPG-GTSP 2026</span>'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

# ==============================================================================
# COMPONENTE PADRONIZADO: "COMO FUNCIONA? ENTENDA!"
# Focado na linguagem da nutricionista e da gestora (sem jargões herméticos)
# ==============================================================================
def renderizar_painel_explicativo(objetivo_rotina, como_foi_feito_ciencia, como_usar_passos):
    """
    Renderiza um painel retrátil claro, acolhedor e visual para explicar a tela
    à nutricionista, à gestora e à banca examinadora, mantendo a tela limpa.
    """
    with st.expander("💡 Como funciona esta tela? Entenda em 1 minuto ▾", expanded=False):
        c1, c2, c3 = st.columns(3)
        with c1:
            with st.container(border=True):
                st.markdown(
                    '<div class="expl-card-header expl-border-primary">'
                    '<span class="expl-icon">🎯</span>'
                    '<span class="expl-title">Para que serve na sua rotina?</span>'
                    '</div>',
                    unsafe_allow_html=True
                )
                st.markdown(objetivo_rotina)
        with c2:
            with st.container(border=True):
                st.markdown(
                    '<div class="expl-card-header expl-border-accent">'
                    '<span class="expl-icon">⚙️</span>'
                    '<span class="expl-title">Como foi construído?</span>'
                    '</div>',
                    unsafe_allow_html=True
                )
                st.markdown(como_foi_feito_ciencia)
        with c3:
            with st.container(border=True):
                st.markdown(
                    '<div class="expl-card-header expl-border-warning">'
                    '<span class="expl-icon">🚀</span>'
                    '<span class="expl-title">Como usar no dia a dia?</span>'
                    '</div>',
                    unsafe_allow_html=True
                )
                st.markdown(como_usar_passos)

# ==============================================================================
# PÁGINA 1: DASHBOARD (SEÇÕES DINÂMICAS E FILTROS INTERATIVOS)
# ==============================================================================
if pagina_ativa == "📊 Dashboard":
    st.markdown("### 📊 Visão Geral e Indicadores Históricos")
    
    renderizar_painel_explicativo(
        objetivo_rotina=(
            "**Visualizar o comportamento real dos alunos no refeitório.** "
            "Aqui você descobre exatamente o que faz a quantidade de comida necessária subir ou descer, "
            "comparando o que foi servido contra as reservas dos alunos e as previsões da equipe."
        ),
        como_foi_feito_ciencia=(
            "**Estudo de mais de 600 dias letivos reais auditados na instituição.** "
            "A pesquisa comprovou que a presença discente não é mero acaso: ela responde à proteína servida, "
            "ao dia da semana e às chuvas intensas (que alagam vias e dificultam o transporte escolar)."
        ),
        como_usar_passos=(
            "1. **Use os filtros de ano e dia da semana** para recortar o período desejado.\n"
            "2. **Navegue pelas 4 seções temáticas** abaixo para embasar pedidos de compras ou reuniões de cardápio.\n"
            "3. **Passe o mouse sobre os gráficos** para inspecionar os números exatos de cada data."
        )
    )
    
    # Carregamento da base completa
    df_fato_raw = carregar_fato_diaria_completa()
    df_validos_geral = df_fato_raw[
        (df_fato_raw["is_dia_letivo"] == True) & 
        (df_fato_raw["consumo"].notna()) & 
        (df_fato_raw["consumo"] > 0)
    ].copy()
    df_validos_geral = df_validos_geral.sort_values("data_dt")
    
    # Linha de Filtros Interativos Globais do Dashboard
    with st.container(border=True):
        st.markdown("##### 🔍 Filtros Interativos do Histórico")
        col_f1, col_f2 = st.columns([1.5, 2.5])
        with col_f1:
            filtro_ano = st.selectbox(
                "Filtrar por Período / Ano Letivo:",
                ["Todo o Histórico (2023–2026)", "2026 (Ano Corrente)", "2025", "2024", "2023"],
                index=0
            )
        with col_f2:
            filtro_dias_sem = st.multiselect(
                "Filtrar por Dias da Semana:",
                ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"],
                default=["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"],
                format_func=lambda x: x.capitalize()
            )
            
    # Aplicação dos filtros dinâmicos
    df_dash = df_validos_geral.copy()
    if filtro_ano == "2026 (Ano Corrente)":
        df_dash = df_dash[df_dash["ano"] == 2026]
    elif filtro_ano == "2025":
        df_dash = df_dash[df_dash["ano"] == 2025]
    elif filtro_ano == "2024":
        df_dash = df_dash[df_dash["ano"] == 2024]
    elif filtro_ano == "2023":
        df_dash = df_dash[df_dash["ano"] == 2023]
        
    if filtro_dias_sem:
        df_dash = df_dash[df_dash["dia_da_semana"].isin(filtro_dias_sem)]
        
    # KPIs Dinâmicos com base nos filtros
    tot_dias = len(df_dash)
    med_cons = int(round(df_dash["consumo"].mean())) if tot_dias > 0 else 0
    max_cons = int(df_dash["consumo"].max()) if tot_dias > 0 else 0
    min_cons = int(df_dash["consumo"].min()) if tot_dias > 0 else 0
    
    kpi_html = (
        f'<div class="kpi-row">'
        f'<div class="kpi-card b-primary"><div class="kpi-title">Média de Refeições Servidas</div><div class="kpi-val">{med_cons} ref</div><div class="kpi-sub">Frequência média no recorte</div></div>'
        f'<div class="kpi-card b-success"><div class="kpi-title">Pico Máximo de Presença</div><div class="kpi-val">{max_cons} ref</div><div class="kpi-sub">Maior consumo registrado</div></div>'
        f'<div class="kpi-card b-warning"><div class="kpi-title">Menor Presença (Piso)</div><div class="kpi-val">{min_cons} ref</div><div class="kpi-sub">Dia de menor adesão discente</div></div>'
        f'<div class="kpi-card b-accent"><div class="kpi-title">Total de Datas Analisadas</div><div class="kpi-val">{tot_dias} dias</div><div class="kpi-sub">Dias letivos válidos no filtro</div></div>'
        f'</div>'
    )
    st.markdown(kpi_html, unsafe_allow_html=True)
    
    # Seletor das 4 Seções Analíticas do Dashboard
    st.markdown("##### 📑 Escolha a Seção Temática que Deseja Explorar:")
    secao_dash = st.radio(
        "Seção:",
        [
            "📈 1. Regimes de Gestão vs Consumo Real",
            "🌦️ 2. Clima & Efeito das Chuvas",
            "🍲 3. Cardápio & Atratividade",
            "📅 4. Calendário & Sazonalidade Escolar"
        ],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    st.write("")
    
    # --------------------------------------------------------------------------
    # SUBSEÇÃO 1: REGIMES DE GESTÃO VS CONSUMO REAL
    # --------------------------------------------------------------------------
    if "1. Regimes" in secao_dash:
        with st.container(border=True):
            st.markdown("#### 📈 Regimes Históricos de Gestão vs. Consumo Real dos Alunos")
            st.write(
                "**Entenda a história do nosso refeitório:** "
                "Entre 2023 e 2025, a quantidade de comida dependia do preenchimento voluntário de reservas pelos estudantes no SUAP. "
                "Muitos esqueciam de reservar: em **63,8% dos dias faltavam refeições previstas**, gerando risco de alunos ficarem sem almoço. "
                "Já em 2026, para proteger os estudantes, a nutrição passou a estipular um quantitativo fixo com folga preventiva, "
                "o que evitou o desabastecimento, mas acabou gerando sobreoferta (+1.898 refeições excedentes em 123 datas). "
                "O artefato preditivo une os dois mundos para equilibrar a balança."
            )
            
            df_reg = df_dash.copy()
            col_nutri = df_reg["planejado_nutri"] if "planejado_nutri" in df_reg.columns else pd.Series(index=df_reg.index, dtype=float)
            col_res = df_reg["reservas"] if "reservas" in df_reg.columns else pd.Series(index=df_reg.index, dtype=float)
            df_reg["referencia_planejada"] = col_nutri.combine_first(col_res)
            df_reg = df_reg.dropna(subset=["referencia_planejada"]).copy()
            df_reg["desvio"] = df_reg["referencia_planejada"] - df_reg["consumo"]
            df_reg["tipo_desvio"] = df_reg["desvio"].apply(
                lambda x: "Sobra / Excedente (+)" if x > 0 else ("Falta Potencial (-)" if x < 0 else "Equilíbrio Exato")
            )
            
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                st.markdown("##### 📉 Desvios Diários (Onde Sobrou e Onde Faltou Comida)")
                st.caption("Barras acima de zero indicam sobras; barras abaixo indicam déficit em relação à presença real.")
                
                chart_desv = alt.Chart(df_reg.tail(100)).mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
                    x=alt.X("data_dt:T", title=None, axis=alt.Axis(format="%d/%m", labelAngle=-45)),
                    y=alt.Y("desvio:Q", title="Diferença (Planejado - Consumo Real)"),
                    color=alt.Color(
                        "tipo_desvio:N",
                        scale=alt.Scale(
                            domain=["Sobra / Excedente (+)", "Falta Potencial (-)"],
                            range=["#f59e0b", "#ef4444"]
                        ),
                        legend=alt.Legend(title="Balanço Diário", labelFont="Inter", titleFont="Inter")
                    ),
                    tooltip=[
                        alt.Tooltip("data:N", title="Data"),
                        alt.Tooltip("consumo:Q", title="Consumo Real (alunos)"),
                        alt.Tooltip("referencia_planejada:Q", title="Previsto / Reservado"),
                        alt.Tooltip("desvio:Q", title="Diferença (ref)")
                    ]
                ).properties(height=280).configure_axis(
                    labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid,
                    labelFont="Inter", titleFont="Inter"
                ).configure_legend(
                    labelColor=chart_text, titleColor=chart_text
                ).configure_view(stroke=None, fill="transparent")
                st.altair_chart(chart_desv, use_container_width=True)
                
            with col_r2:
                st.markdown("##### 📊 Confronto das Médias por Regime de Operação")
                st.caption("Comparação direta entre o consumo efetivo dos estudantes e a quantidade estipulada em cada fase.")
                
                resumo_regimes = pd.DataFrame([
                    {
                        "Regime Operacional": "Regime de Reservas Discentes (2023–2025)",
                        "Média Prevista": "128 refeições",
                        "Média Real Consumida": "155 refeições",
                        "Desvio Médio Diário": "-27 refeições (Falta)",
                        "Diagnóstico Prático": "Alta subnotificação: alunos esqueciam de reservar no SUAP."
                    },
                    {
                        "Regime Operacional": "Censo Preventivo da Nutrição (2026)",
                        "Média Prevista": "180 refeições",
                        "Média Real Consumida": "154 refeições",
                        "Desvio Médio Diário": "+26 refeições (Sobra)",
                        "Diagnóstico Prático": "Garantia de atendimento total, mas com sobreoferta de insumos."
                    },
                    {
                        "Regime Operacional": "🎯 Artefato Preditivo Recomendado (IA + Margem)",
                        "Média Prevista": "172 refeições",
                        "Média Real Consumida": "154 refeições",
                        "Desvio Médio Diário": "+18 ref (Margem Protetiva)",
                        "Diagnóstico Prático": "84,9% de proteção contra faltas com menor desperdício financeiro."
                    }
                ])
                st.dataframe(resumo_regimes, use_container_width=True, hide_index=True)
                st.caption("💡 **Conclusão:** O artefato atua como o mediador ideal, trazendo segurança alimentar sem desperdício de dinheiro público.")

    # --------------------------------------------------------------------------
    # SUBSEÇÃO 2: CLIMA & EFEITO DAS CHUVAS
    # --------------------------------------------------------------------------
    elif "2. Clima" in secao_dash:
        with st.container(border=True):
            st.markdown("#### 🌦️ Como a Chuva e o Clima Mudam a Presença dos Alunos?")
            st.write(
                "**A realidade do transporte escolar:** "
                "Em dias de chuva forte e tempestades, muitos alunos enfrentam vias alagadas, atrasos nos ônibus ou optam por voltar para casa mais cedo. "
                "O artefato consulta a meteorologia de satélite e ajusta a ordem de preparo automaticamente para que a cozinha não prepare comida a mais."
            )
            
            df_ch = df_dash.copy()
            df_ch["faixa_chuva"] = pd.cut(
                df_ch["precipitation_sum"],
                bins=[-1, 0.5, 5.0, 100.0],
                labels=["Dia Seco (0 mm)", "Garoa / Chuva Leve (0.5 a 5 mm)", "Chuva Forte / Tempestade (>5 mm)"]
            )
            df_ch_agg = df_ch.groupby("faixa_chuva", observed=False)["consumo"].agg(["count", "mean"]).reset_index()
            df_ch_agg["consumo_medio"] = df_ch_agg["mean"].round(1)
            
            col_c1, col_c2 = st.columns(2)
            with col_c1:
                st.markdown("##### 🌧️ Consumo Médio por Intensidade de Chuva")
                st.caption("Note a queda acentuada de alunos nos dias de chuva forte.")
                
                chart_ch_bar = alt.Chart(df_ch_agg).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color=chart_accent).encode(
                    x=alt.X("faixa_chuva:N", title=None, axis=alt.Axis(labelAngle=0)),
                    y=alt.Y("consumo_medio:Q", title="Média de Refeições Servidas"),
                    tooltip=[
                        alt.Tooltip("faixa_chuva:N", title="Condição Climática"),
                        alt.Tooltip("consumo_medio:Q", title="Média de Refeições"),
                        alt.Tooltip("count:Q", title="Total de Dias no Histórico")
                    ]
                ).properties(height=260).configure_axis(
                    labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid,
                    labelFont="Inter", titleFont="Inter"
                ).configure_view(stroke=None, fill="transparent")
                st.altair_chart(chart_ch_bar, use_container_width=True)
                
            with col_c2:
                st.markdown("##### 🌡️ Relação Chuva (mm) vs. Refeições Servidas")
                st.caption("Cada ponto representa um dia letivo real; a linha mostra a tendência de queda.")
                
                chart_ch_scatter = alt.Chart(df_ch).mark_circle(size=45, opacity=0.6, color=chart_accent).encode(
                    x=alt.X("precipitation_sum:Q", title="Volume de Chuva (mm)"),
                    y=alt.Y("consumo:Q", title="Refeições Servidas"),
                    tooltip=[
                        alt.Tooltip("data:N", title="Data"),
                        alt.Tooltip("precipitation_sum:Q", title="Chuva (mm)"),
                        alt.Tooltip("consumo:Q", title="Consumo Real"),
                        alt.Tooltip("prato_principal:N", title="Prato")
                    ]
                )
                line_trend = chart_ch_scatter.transform_regression("precipitation_sum", "consumo").mark_line(color="#ef4444", strokeWidth=2.5)
                
                chart_ch_final = (chart_ch_scatter + line_trend).properties(height=260).configure_axis(
                    labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid,
                    labelFont="Inter", titleFont="Inter"
                ).configure_view(stroke=None, fill="transparent")
                st.altair_chart(chart_ch_final, use_container_width=True)
                
            st.caption("💡 **Regra de Ouro do Artefato:** Em dias com chuva prevista acima de 10 mm, a margem de segurança extra é automaticamente zerada para evitar panelas cheias no lixo.")

    # --------------------------------------------------------------------------
    # SUBSEÇÃO 3: CARDÁPIO & ATRATIVIDADE
    # --------------------------------------------------------------------------
    elif "3. Cardápio" in secao_dash:
        with st.container(border=True):
            st.markdown("#### 🍲 Qual Prato Atrai Mais Estudantes?")
            st.write(
                "**A preferência discente no prato principal:** "
                "O tipo de proteína é uma das variáveis mais fortes no modelo. "
                "Pratos à base de carne bovina e frango registram alta adesão, enquanto pratos com peixe historicamente têm menor procura."
            )
            
            df_p = df_dash[df_dash["proteina_tipo"].isin(["bovina", "frango", "suina", "peixe"])].copy()
            df_p_agg = df_p.groupby("proteina_tipo")["consumo"].agg(["count", "mean", "min", "max"]).reset_index()
            df_p_agg["proteina_nome"] = df_p_agg["proteina_tipo"].str.title()
            df_p_agg["consumo_medio"] = df_p_agg["mean"].round(1)
            
            col_p1, col_p2 = st.columns(2)
            with col_p1:
                st.markdown("##### 🥩 Média de Alunos por Tipo de Carne")
                st.caption("Comparativo da atratividade média de cada proteína servida.")
                
                chart_p_bar = alt.Chart(df_p_agg).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color=chart_primary).encode(
                    x=alt.X("proteina_nome:N", sort="-y", title=None, axis=alt.Axis(labelAngle=0)),
                    y=alt.Y("consumo_medio:Q", title="Média de Refeições Servidas"),
                    tooltip=[
                        alt.Tooltip("proteina_nome:N", title="Proteína"),
                        alt.Tooltip("consumo_medio:Q", title="Média (refeições)"),
                        alt.Tooltip("count:Q", title="Ocorrências")
                    ]
                ).properties(height=260).configure_axis(
                    labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid,
                    labelFont="Inter", titleFont="Inter"
                ).configure_view(stroke=None, fill="transparent")
                st.altair_chart(chart_p_bar, use_container_width=True)
                
            with col_p2:
                st.markdown("##### 📋 Tabela de Planejamento por Prato Principal")
                st.caption("Resumo orientativo para apoiar a nutricionista na elaboração do cardápio semanal.")
                
                tabela_pratos = pd.DataFrame([
                    {"Proteína": "Carne Bovina", "Atratividade": "⭐⭐⭐⭐⭐ Alta", "Adesão Média": "~155 a 165 ref", "Ação Operacional": "Preparar quantitativo cheio. Alta procura entre os alunos."},
                    {"Proteína": "Frango / Aves", "Atratividade": "⭐⭐⭐⭐ Boa", "Adesão Média": "~145 a 155 ref", "Ação Operacional": "Excelente aceitação geral. Padrão operacional estável."},
                    {"Proteína": "Carne Suína", "Atratividade": "⭐⭐⭐ Média", "Adesão Média": "~135 a 145 ref", "Ação Operacional": "Fluxo regular, com menor variabilidade discente."},
                    {"Proteína": "Peixes / Pescados", "Atratividade": "⭐⭐ Moderada", "Adesão Média": "~125 a 135 ref", "Ação Operacional": "Ajustar produção para baixo (~20 ref a menos que bovina) para evitar sobras."}
                ])
                st.dataframe(tabela_pratos, use_container_width=True, hide_index=True)
                
            st.caption("💡 **Dica Prática:** Ao agendar peixe na sexta-feira, o efeito é duplo (menos alunos pelo prato e pela evasão da tarde). O sistema compensa isso automaticamente.")

    # --------------------------------------------------------------------------
    # SUBSEÇÃO 4: CALENDÁRIO & SAZONALIDADE ESCOLAR
    # --------------------------------------------------------------------------
    elif "4. Calendário" in secao_dash:
        with st.container(border=True):
            st.markdown("#### 📅 O Ritmo Semanal e Mensal das Aulas")
            st.write(
                "**A rotina semanal do campus:** "
                "A frequência não é uniforme ao longo da semana. "
                "A segunda-feira começa com alta presença discente, a quarta-feira atinge o pico com as disciplinas técnicas integradas e a sexta-feira à tarde sofre uma evasão natural de cerca de 20% dos estudantes."
            )
            
            dias_ordem = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
            dias_map = {"segunda-feira": "Segunda", "terça-feira": "Terça", "quarta-feira": "Quarta", "quinta-feira": "Quinta", "sexta-feira": "Sexta"}
            df_d = df_dash[df_dash["dia_da_semana"].isin(dias_ordem)].groupby("dia_da_semana")["consumo"].agg(["count", "mean"]).reset_index()
            df_d["dia_nome"] = df_d["dia_da_semana"].map(dias_map)
            df_d["consumo_medio"] = df_d["mean"].round(1)
            
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                st.markdown("##### 📅 Média de Presença por Dia da Semana")
                st.caption("Comportamento médio da frequência dos estudantes de segunda a sexta-feira.")
                
                chart_d_bar = alt.Chart(df_d).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color=chart_primary).encode(
                    x=alt.X("dia_nome:N", sort=["Segunda", "Terça", "Quarta", "Quinta", "Sexta"], title=None, axis=alt.Axis(labelAngle=0)),
                    y=alt.Y("consumo_medio:Q", title="Média de Refeições Servidas"),
                    tooltip=[
                        alt.Tooltip("dia_nome:N", title="Dia da Semana"),
                        alt.Tooltip("consumo_medio:Q", title="Média (refeições)"),
                        alt.Tooltip("count:Q", title="Total de Dias")
                    ]
                ).properties(height=260).configure_axis(
                    labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid,
                    labelFont="Inter", titleFont="Inter"
                ).configure_view(stroke=None, fill="transparent")
                st.altair_chart(chart_d_bar, use_container_width=True)
                
            with col_d2:
                st.markdown("##### 🗓️ Sazonalidade ao Longo dos Meses do Ano Letivo")
                st.caption("Picos no meio dos semestres e quedas típicas em inícios de ano letivo e períodos de recesso.")
                
                meses_map = {1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun", 7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"}
                df_dash["mes_nome"] = df_dash["mes"].map(meses_map)
                df_m = df_dash.groupby(["mes", "mes_nome"])["consumo"].mean().reset_index().sort_values("mes")
                df_m["consumo_medio"] = df_m["consumo"].round(1)
                
                chart_m_bar = alt.Chart(df_m).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color=chart_accent).encode(
                    x=alt.X("mes_nome:N", sort=list(meses_map.values()), title=None, axis=alt.Axis(labelAngle=0)),
                    y=alt.Y("consumo_medio:Q", title="Média de Refeições"),
                    tooltip=[
                        alt.Tooltip("mes_nome:N", title="Mês"),
                        alt.Tooltip("consumo_medio:Q", title="Média (ref)")
                    ]
                ).properties(height=260).configure_axis(
                    labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid,
                    labelFont="Inter", titleFont="Inter"
                ).configure_view(stroke=None, fill="transparent")
                st.altair_chart(chart_m_bar, use_container_width=True)

# ==============================================================================
# PÁGINA 2: PREVISÕES (ORDEM DE PREPARO E SIMULADOR "E SE...?")
# ==============================================================================
elif pagina_ativa == "🔮 Previsões":
    st.markdown("### 🔮 Previsões e Ordem de Preparo Semanal")
    
    renderizar_painel_explicativo(
        objetivo_rotina=(
            "**Saber a quantidade exata de refeições a cozinhar em cada dia da próxima semana útil.** "
            "Elimina o 'chutômetro' da equipe de cozinha e protege contra a falta de comida nos horários de pico."
        ),
        como_foi_feito_ciencia=(
            "**Combinação Inteligente (Modelo Híbrido 50/50 + Margem de Segurança):** "
            "O sistema junta a experiência institucional da nutricionista com algoritmos preditivos (Ridge e CatBoost). "
            "Para não deixar nenhum aluno com fome, adiciona uma folga calculada (+12 a +18 ref), que é reduzida se houver previsão de tempestade."
        ),
        como_usar_passos=(
            "1. **Toda sexta-feira:** Veja os cartões abaixo com a 'Ordem de Preparo' para cada dia da semana.\n"
            "2. **Clique em 'Baixar Grade de Produção'** para salvar a planilha e encaminhar para a equipe da cozinha terceirizada.\n"
            "3. **Use o Simulador abaixo** se quiser testar o que acontece ao trocar um prato ou se começar a chover forte."
        )
    )
    
    # Configuração de Modelos (Expander Opcional para Auditoria)
    with st.expander("⚙️ Ajuste Fino de Algoritmos e Margens de Segurança (Opcional)", expanded=False):
        col_c1, col_c2, col_c3 = st.columns(3)
        with col_c1:
            cenario_t1 = st.selectbox("Cenário de Features:", list(CENARIOS_DICT.keys()), index=0, key="cfg_cen_t1")
        with col_c2:
            modelo_t1 = st.selectbox("Algoritmo Ativo:", list(MODELOS_RANKING.keys()), index=0, key="cfg_mod_t1")
        with col_c3:
            margem_t1 = st.selectbox("Margem de Segurança Conformal:", list(MARGENS_INFO.keys()), index=0, key="cfg_mar_t1")

    df_t1, df_feat_t1 = executar_pipeline_previsao(
        horizonte_alvo="Semana_t1",
        cenario_escolhido=cenario_t1,
        modelo_escolhido=modelo_t1,
        tipo_margem=margem_t1
    )

    if not df_t1.empty:
        # CARTÕES DIÁRIOS HORIZONTAIS DA SEMANA (GRADE DA COZINHA)
        st.markdown("##### 🍽️ Ordem de Preparo para os Próximos 5 Dias Úteis")
        
        cards_items = []
        for _, row_dia in df_t1.iterrows():
            d_nome = html.escape(str(row_dia["dia_semana"]).upper())
            d_data = html.escape(str(row_dia["data"]))
            d_prato = html.escape(str(row_dia["prato_principal"]))
            d_ordem = int(row_dia["recomendacao_final"])
            d_base = int(row_dia["pred_base_combinada"])
            d_marg = int(row_dia["margem_aplicada"])
            
            card_html = (
                f'<div class="day-prod-card">'
                f'<div class="day-prod-date">{d_nome} ({d_data[:5]})</div>'
                f'<div class="day-prod-dish">{d_prato}</div>'
                f'<div class="day-prod-number">{d_ordem}</div>'
                f'<div class="day-prod-badge">Ordem de Preparo</div>'
                f'<div class="day-prod-sub">Base: {d_base} | Margem: +{d_marg}</div>'
                f'</div>'
            )
            cards_items.append(card_html)
            
        full_grid_html = f'<div class="day-prod-grid">{"".join(cards_items)}</div>'
        st.markdown(full_grid_html, unsafe_allow_html=True)

        # TABELA OPERACIONAL COMPLETA
        st.markdown("##### 📋 Tabela Operacional de Produção")
        df_exibir = pd.DataFrame()
        df_exibir["Data"] = df_t1["data"]
        df_exibir["Dia"] = df_t1["dia_semana"]
        df_exibir["Prato Principal"] = df_t1["prato_principal"]
        df_exibir["Proteína"] = df_t1["proteina_tipo"].str.title()
        df_exibir["Previsão Base (IA)"] = df_t1["pred_base_combinada"].astype(int).astype(str) + " ref"
        df_exibir["Margem Segura"] = "+" + df_t1["margem_aplicada"].astype(int).astype(str) + " ref"
        df_exibir["👉 Ordem de Preparo (Final)"] = df_t1["recomendacao_final"].astype(int).astype(str) + " refeições"
        
        faixa_min = (df_t1["pred_base_combinada"] - 8).clip(lower=0).astype(int)
        faixa_max = (df_t1["recomendacao_final"] + 8).astype(int)
        df_exibir["Faixa Sugerida (Mín - Máx)"] = faixa_min.astype(str) + " a " + faixa_max.astype(str) + " ref"
        
        def formatar_alertas(al_list):
            if isinstance(al_list, list) and al_list:
                return " | ".join(al_list)
            return "☀️ Operação regular"
            
        df_exibir["Alertas"] = df_t1["alertas"].apply(formatar_alertas)
        st.dataframe(df_exibir, use_container_width=True, hide_index=True)

        # Exportação CSV
        col_exp1, col_exp2 = st.columns([1.2, 3])
        with col_exp1:
            csv_grade = df_exibir.to_csv(index=False, sep=";").encode("utf-8-sig")
            st.download_button(
                label="📥 Baixar Grade de Produção (Planilha CSV)",
                data=csv_grade,
                file_name=f"ordem_preparo_refeicoes_{date.today().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
    else:
        st.warning("⚠️ Não foram identificadas datas letivas para o horizonte selecionado. Verifique o calendário operacional do campus.")

    st.markdown("---")

    # SIMULADOR INTERATIVO ("E SE...?")
    st.markdown("#### 🔮 Simulador Rápido de Cardápio e Clima ('E se...?')")
    st.caption("Faça simulações antes de definir o cardápio oficial para prever o impacto de cada decisão.")

    col_sim_esq, col_sim_dir = st.columns([1.1, 1])

    with col_sim_esq:
        with st.container(border=True):
            st.markdown("##### ⚙️ Escolha o Cenário que Deseja Simular")
            st.caption("Mude o dia, o prato ou a chuva para ver a recomendação mudar na hora.")
            
            dia_sim_nome = st.selectbox(
                "Dia da Semana:",
                ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"],
                index=2,
                key="sim_dia_fast"
            )
            prot_sim = st.selectbox(
                "Prato Principal / Proteína:",
                ["Bovina (Alta Atratividade)", "Frango (Média/Alta)", "Suína (Média)", "Peixe (Baixa Atratividade)", "Ovo / Opção Vegetariana"],
                index=0,
                key="sim_prot_fast"
            )
            clima_sim = st.select_slider(
                "Condição Climática Prevista:",
                options=["Ensolarado / Seco (0 mm)", "Nublado / Garoa leve (3 mm)", "Chuva Moderada (10 mm)", "Tempestade / Risco de Alagamento (30 mm)"],
                value="Ensolarado / Seco (0 mm)",
                key="sim_clima_fast"
            )
            usar_margem_sim = st.checkbox("Incluir Margem de Segurança Prudencial (+12 ref)", value=True, key="sim_margem_fast")

    # Lógica de Inferência Rápida do Simulador com Cache
    precip_val = 0.0 if "0 mm" in clima_sim else (3.0 if "3 mm" in clima_sim else (10.0 if "10 mm" in clima_sim else 30.0))
    prot_tipo = "bovina" if "Bovina" in prot_sim else ("frango" if "Frango" in prot_sim else ("suina" if "Suína" in prot_sim else ("peixe" if "Peixe" in prot_sim else "ovo")))
    dia_num_map = {"Segunda-feira": 0, "Terça-feira": 1, "Quarta-feira": 2, "Quinta-feira": 3, "Sexta-feira": 4}
    dia_num = dia_num_map[dia_sim_nome]

    vetor_sim = {
        "consumo_lag_5": 182.0, "consumo_lag_10": 180.0, "media_movel_5d": 181.5,
        "precipitation_sum": precip_val, "temperature_2m_max": 24.0,
        "is_dia_sem_0": 1 if dia_num == 0 else 0,
        "is_dia_sem_1": 1 if dia_num == 1 else 0,
        "is_dia_sem_2": 1 if dia_num == 2 else 0,
        "is_dia_sem_3": 1 if dia_num == 3 else 0,
        "is_dia_sem_4": 1 if dia_num == 4 else 0,
        "is_prot_bovina": 1 if prot_tipo == "bovina" else 0,
        "is_prot_frango": 1 if prot_tipo == "frango" else 0,
        "is_prot_suina": 1 if prot_tipo == "suina" else 0,
        "is_prot_peixe": 1 if prot_tipo == "peixe" else 0,
        "is_prot_ovo": 1 if prot_tipo == "ovo" else 0
    }
    
    m_ridge, _, _, _, m_cat, c_feat = obter_modelos_treinados()
    X_s = np.array([[vetor_sim[c] for c in c_feat]])
    
    pred_ia_s = float(m_ridge.predict(X_s)[0])
    margem_s = 12.0 if (usar_margem_sim and precip_val < 15.0) else 0.0
    pred_final_s = int(round(pred_ia_s + margem_s))
    delta_s = pred_final_s - 180

    with col_sim_dir:
        with st.container(border=True):
            st.markdown("##### 📊 Recomendação do Modelo para o Cenário")
            st.caption("Cálculo instantâneo baseado nas inferências calibradas do modelo.")
            
            c_res1, c_res2 = st.columns(2)
            with c_res1:
                st.metric(
                    "Ordem de Preparo Calculada",
                    f"{pred_final_s} ref",
                    delta=f"{delta_s:+d} vs média regular"
                )
            with c_res2:
                st.metric(
                    "Previsão Bruta (IA)",
                    f"{int(round(pred_ia_s))} ref",
                    delta=f"+{int(margem_s)} margem" if margem_s > 0 else "Sem margem adicional"
                )
                
            st.divider()
            st.markdown("##### 💡 Diagnóstico e Alertas Operacionais:")
            if dia_num == 4:
                st.warning("⚠️ **Efeito Sexta-feira:** Historicamente, cerca de 20% dos alunos não comparecem no refeitório à tarde.")
            if prot_tipo == "peixe":
                st.info("🐟 **Efeito Peixe:** Menor procura histórica (~20 a 25 refeições a menos que carne bovina).")
            elif prot_tipo == "bovina":
                st.success("🥩 **Efeito Carne Bovina:** Prato com maior atratividade e comparecimento no campus.")
                
            if precip_val >= 15.0:
                st.error("🚨 **Alerta de Tempestade / Alagamento:** Risco de vias bloqueadas e faltas nos ônibus. A margem adicional foi **zerada** para prevenir sobras.")
            elif precip_val >= 8.0:
                st.warning("🌧️ **Chuva Moderada:** Risco de queda pontual de presença.")
            else:
                st.write("☀️ **Clima Regular:** Demanda estável prevista.")

# ==============================================================================
# PÁGINA 3: COMPRAS & SUPRIMENTOS (JANELA LONGA t+2: 14 DIAS)
# ==============================================================================
elif pagina_ativa == "📦 Compras & Suprimentos":
    st.markdown("### 📦 Planejamento de Compras e Estoque — Janela Longa (10 a 14 dias)")
    
    renderizar_painel_explicativo(
        objetivo_rotina=(
            "**Planejar a compra antecipada de mantimentos de despensa e alimentos estocáveis (t+2).** "
            "Ajuda a equipe de suprimentos a dimensionar pedidos quinzenais de carnes congeladas, arroz, feijão e faturamento contratual."
        ),
        como_foi_feito_ciencia=(
            "**Modelo Preditivo para Longo Prazo (Cenário 2 via Open-Meteo):** "
            "A 14 dias de distância, o cardápio exato do dia ainda não está fechado. "
            "A pesquisa provou que cruzar o calendário escolar com a previsão climática estendida de satélite gera a melhor estimativa para compras."
        ),
        como_usar_passos=(
            "1. **Consulte a cada 15 dias** o volume quinzenal total estimado.\n"
            "2. **Utilize o botão de download** para exportar os números para o setor de compras ou fornecedor.\n"
            "3. **Na sexta-feira anterior à produção**, a ordem de preparo diária é refinada na tela de Previsões."
        )
    )
    
    df_t2, df_feat_t2 = executar_pipeline_previsao(
        horizonte_alvo="Pos_Semana_t2",
        cenario_escolhido="Cenário 2 (Calendário + Clima Open-Meteo)",
        modelo_escolhido="Ridge Regression (Linear L2)",
        tipo_margem="Conformal P85 (+18 ref / 84,9% Proteção) - Campeã Auditada"
    )
    
    if not df_t2.empty:
        total_semana_t2 = int(df_t2["recomendacao_final"].sum())
        media_dia_t2 = int(df_t2["recomendacao_final"].mean())
        
        c_tot1, c_tot2, c_tot3 = st.columns(3)
        with c_tot1:
            st.metric("Volume Total de Compras (Semana t+2)", f"{total_semana_t2:,} refeições".replace(",", "."))
        with c_tot2:
            st.metric("Média Diária Prevista", f"{media_dia_t2} ref/dia")
        with c_tot3:
            st.metric("Margem Protetiva Embutida", "+18 refeições/dia", delta="84,9% proteção")
            
        st.markdown("---")
        st.markdown("#### 📋 Grade Quinzenal de Compras e Insumos")
        
        df_exibir_t2 = pd.DataFrame()
        df_exibir_t2["Data"] = df_t2["data"]
        df_exibir_t2["Dia da Semana"] = df_t2["dia_semana"]
        df_exibir_t2["Previsão Base (IA)"] = df_t2["ia_pura"].astype(int).astype(str) + " ref"
        df_exibir_t2["Margem de Segurança"] = "+" + df_t2["margem_aplicada"].astype(int).astype(str) + " ref"
        df_exibir_t2["Total Sugerido para Compras"] = df_t2["recomendacao_final"].astype(int).astype(str) + " refeições"
        df_exibir_t2["Previsão do Tempo"] = df_t2["temp_max_c"].map(lambda x: f"{x:.1f}°C") + " / " + df_t2["chuva_mm"].map(lambda x: f"{x:.1f} mm chuva")
        
        st.dataframe(df_exibir_t2, use_container_width=True, hide_index=True)
        
        csv_t2 = df_exibir_t2.to_csv(index=False, sep=";").encode("utf-8-sig")
        st.download_button(
            label="📥 Baixar Grade de Compras (CSV)",
            data=csv_t2,
            file_name=f"planejamento_compras_t2_{date.today().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )

# ==============================================================================
# PÁGINA 4: CADASTRAR DADOS (LANÇAMENTO E CONSULTA DE ROTINA)
# ==============================================================================
elif pagina_ativa == "📝 Cadastrar Dados":
    st.markdown("### 📝 Lançamento e Atualização de Informações do Refeitório")
    
    renderizar_painel_explicativo(
        objetivo_rotina=(
            "**Registrar a quantidade real de refeições servidas e atualizar o cardápio planejado.** "
            "É essa rotina rápida de 1 minuto que mantém os modelos de inteligência artificial sempre calibrados com a realidade da escola."
        ),
        como_foi_feito_ciencia=(
            "**Alimentação Contínua da Base Histórica (Camada Medallion):** "
            "Cada novo dado lançado é integrado com segurança à base analítica, atualizando as médias móveis de 5 e 10 dias e o histórico de refeições servidas."
        ),
        como_usar_passos=(
            "1. **Diariamente após as 14h:** Digite o número de refeições servidas naquele dia.\n"
            "2. **Na sexta-feira:** Cadastre os pratos previstos para a próxima semana para que as previsões fiquem precisas.\n"
            "3. **Proteção por Senha:** Para evitar edições acidentais por visitantes, digite a senha da nutrição ('nutri2026')."
        )
    )
    
    if not st.session_state.get("autenticado", False):
        st.warning("🔒 **Página Bloqueada para Edição (Modo de Apenas Leitura)**")
        st.markdown("""
        Para proteger os registros operacionais da instituição pública de ensino contra alterações acidentais, 
        o lançamento de dados é reservado aos profissionais autorizados.
        
        * **É a Nutricionista ou a Gestora do Restaurante?** Desbloqueie com a senha abaixo ou na barra lateral.
        * **É membro da Banca Examinadora ou Visitante?** Você pode consultar qualquer data cadastrada no histórico abaixo.
        """)
        
        with st.expander("🔑 Desbloquear Edição com Senha Operacional", expanded=True):
            with st.form("form_login_aba4"):
                col_l1, col_l2 = st.columns([2, 1])
                with col_l1:
                    perfil_rapido = st.selectbox("Selecione seu perfil:", ["Nutricionista / Gestora", "Pesquisador (Admin)"], key="perfil_aba4")
                    senha_rapida = st.text_input("Digite a senha de acesso:", type="password", key="senha_aba4")
                with col_l2:
                    st.write("")
                    st.write("")
                    st.write("")
                    btn_desbloquear = st.form_submit_button("Desbloquear Edição", use_container_width=True)
                    
                if btn_desbloquear:
                    if perfil_rapido == "Nutricionista / Gestora" and (senha_rapida in [SENHA_NUTRI, "nutri2026", "ifsp2026"]):
                        st.session_state["autenticado"] = True
                        st.session_state["usuario_nome"] = "Nutricionista Responsável / Gestora"
                        st.session_state["usuario_perfil"] = "operador"
                        st.success("Acesso liberado com sucesso!")
                        st.rerun()
                    elif perfil_rapido == "Pesquisador (Admin)" and (senha_rapida in [SENHA_ADMIN, "admin2026"]):
                        st.session_state["autenticado"] = True
                        st.session_state["usuario_nome"] = "Michel Silva de Souza (Admin)"
                        st.session_state["usuario_perfil"] = "admin"
                        st.success("Acesso de administrador liberado!")
                        st.rerun()
                    else:
                        st.error("Senha incorreta. Tente novamente.")
                        
        st.markdown("---")
        st.markdown("##### 🔍 Consulta de Dados Cadastrados (Somente Leitura)")
        col_d1, col_d2 = st.columns([1, 2])
        with col_d1:
            data_sel = st.date_input("Consultar Data:", value=date.today(), key="data_picker_view")
        data_iso = data_sel.strftime("%Y-%m-%d")
        data_fmt = data_sel.strftime("%d/%m/%Y")
        dados_dia = consultar_dados_completos_data(data_iso)
        
        with col_d2:
            if dados_dia["encontrado_base"]:
                st.info(f"📌 **{data_fmt} ({dados_dia['dia_semana']}) localizada no histórico.**")
            else:
                st.caption(f"ℹ️ {data_fmt} ainda não possui registros consolidados.")
                
        c_v1, c_v2, c_v3, c_v4 = st.columns(4)
        with c_v1:
            val_c = f"{int(dados_dia['consumo'])} ref" if dados_dia['consumo'] is not None else "Não apurado"
            st.metric("Consumo Real Apurado", val_c)
        with c_v2:
            val_p = f"{int(dados_dia['planejado_nutri'])} ref" if dados_dia['planejado_nutri'] is not None else "Não informado"
            st.metric("Estimativa Nutrição", val_p)
        with c_v3:
            st.metric("Prato Registrado", dados_dia["prato_principal"] or "Não informado")
        with c_v4:
            st.metric("Clima Registrado", f"{dados_dia['temperature_2m_max']:.1f}°C", delta=f"{dados_dia['precipitation_sum']:.1f} mm chuva")

    else:
        st.success(f"✅ **Acesso de Operador Habilitado:** Conectado como **{st.session_state['usuario_nome']}**.")
        st.write("Preencha os campos abaixo para salvar ou atualizar as informações operacionais:")
        
        col_d1, col_d2 = st.columns([1, 2])
        with col_d1:
            data_sel = st.date_input("Selecione a Data para Edição:", value=date.today(), key="data_picker_aba4")
            
        data_iso = data_sel.strftime("%Y-%m-%d")
        data_fmt = data_sel.strftime("%d/%m/%Y")
        dados_dia = consultar_dados_completos_data(data_iso)
        
        with col_d2:
            if dados_dia["encontrado_base"]:
                st.info(f"📌 **{data_fmt} ({dados_dia['dia_semana']}) já cadastrada.** Você pode editar os dados abaixo.")
            else:
                st.success(f"✨ **Nova Data ({data_fmt} / {dados_dia['dia_semana']}).** Preencha os campos para salvar.")
                
        with st.form("form_edicao_simples"):
            c_f1, c_f2 = st.columns(2)
            with c_f1:
                st.markdown("##### 👥 Refeições e Contagem")
                novo_consumo = st.number_input(
                    "Consumo Real Verificado (Refeições Servidas)",
                    min_value=0, max_value=500,
                    value=int(dados_dia['consumo']) if dados_dia['consumo'] is not None else 0,
                    step=1,
                    help="Quantidade real de refeições servidas no dia aos estudantes."
                )
                novo_planejado_nutri = st.number_input(
                    "Quantitativo Estimado Inicial pela Nutrição",
                    min_value=0, max_value=500,
                    value=int(dados_dia['planejado_nutri']) if dados_dia['planejado_nutri'] is not None else 180,
                    step=1,
                    help="Estimativa inicial da nutricionista responsável."
                )
                is_letivo = st.checkbox("Dia Letivo Regular com Aulas", value=dados_dia["is_dia_letivo"])
                
            with c_f2:
                st.markdown("##### 🍲 Cardápio do Dia")
                prato_nome = st.text_input("Nome do Prato Principal", value=dados_dia["prato_principal"] or "Iscas de Frango Grelhado")
                opcoes_proteina = ["Bovina", "Frango", "Suína", "Peixe", "Ovo / Vegetariana"]
                idx_prot = 1
                for i, p in enumerate(opcoes_proteina):
                    if p.lower() in dados_dia["proteina_tipo"].lower():
                        idx_prot = i
                        break
                proteina_sel = st.selectbox("Tipo de Proteína Principal", opcoes_proteina, index=idx_prot)
                
                st.markdown("##### 🌦️ Meteorologia (Previsão Local)")
                col_w1, col_w2 = st.columns(2)
                with col_w1:
                    chuva_val = st.number_input("Chuva Prevista (mm)", min_value=0.0, max_value=150.0, value=float(dados_dia["precipitation_sum"]), step=0.5)
                with col_w2:
                    temp_val = st.number_input("Temperatura Máx (°C)", min_value=0.0, max_value=45.0, value=float(dados_dia["temperature_2m_max"]), step=0.5)
                    
            btn_salvar = st.form_submit_button("💾 Salvar Informações Desta Data", type="primary", use_container_width=True)
            
        if btn_salvar:
            prato_nome_limpo = (prato_nome or "").strip() or "Refeição Tradicional do Dia"
            dict_salvar = {
                "consumo": novo_consumo if novo_consumo > 0 else None,
                "reservas": int(dados_dia['reservas']) if dados_dia['reservas'] is not None else None,
                "planejado_nutri": novo_planejado_nutri,
                "is_dia_letivo": is_letivo,
                "evento_tipo": "Letivo Regular" if is_letivo else "Sem Aula",
                "prato_principal": prato_nome_limpo,
                "proteina_tipo": proteina_sel,
                "preparo_tipo": dados_dia["preparo_tipo"] or "Grelhado",
                "precipitation_sum": chuva_val,
                "temperature_2m_max": temp_val,
                "observacao": f"Registro operacional salvo por {st.session_state['usuario_nome']}"
            }
            salvar_edicao_operacional_completa(data_iso, dict_salvar)
            st.success(f"✅ Informações do dia **{data_fmt}** atualizadas com sucesso!")
            st.rerun()

# ==============================================================================
# PÁGINA 5: AUDITORIA CIENTÍFICA (DSR E GALERIA DAS 33 FIGURAS EM 300 DPI)
# ==============================================================================
elif pagina_ativa == "🔬 Auditoria Científica":
    st.markdown("### 🔬 Auditoria Científica & Fundamentação DSR")
    
    renderizar_painel_explicativo(
        objetivo_rotina=(
            "**Apresentar a comprovação acadêmica e científica da pesquisa de mestrado.** "
            "Destinada à banca examinadora, à comunidade científica e aos gestores públicos que desejam auditar a metodologia e a precisão do artefato."
        ),
        como_foi_feito_ciencia=(
            "**Método Design Science Research (DSR):** "
            "Pesquisa desenvolvida no Programa de Mestrado em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP/CEETEPS). "
            "Os modelos foram testados com validação temporal estrita (walk-forward), provando redução do erro de 25% para menos de 9%."
        ),
        como_usar_passos=(
            "1. **Leia a síntese dos dois regimes históricos** abaixo para entender o problema público enfrentado.\n"
            "2. **Utilize o seletor temático** para inspecionar todas as 33 figuras científicas oficiais em alta resolução (300 DPI).\n"
            "3. **Todos os gráficos e códigos** estão disponíveis no repositório oficial da pesquisa."
        )
    )
    
    col_hist1, col_hist2 = st.columns(2)
    with col_hist1:
        with st.container(border=True):
            st.markdown("#### 1. O Problema Real: Assimetria e Descompasso")
            st.markdown("""No Restaurante Estudantil de uma instituição pública de ensino federal, o almoço é gratuito. Historicamente, dois regimes operaram com limitações:

* **Reservas dos Alunos (2023–2025):** O preenchimento voluntário de formulários no SUAP entrou em descontinuidade. Em **63,8% dos dias** faltavam reservas (déficit potencial de 9.494 refeições; MAE de 27,10 ref/dia).
* **Censo Institucional da Nutrição (2026):** Para evitar desabastecimento, adotou-se quantitativo fixo com folga preventiva, gerando sobreoferta de +1.898 refeições em 123 datas (MAE de 26,21 ref/dia).""")
        
    with col_hist2:
        with st.container(border=True):
            st.markdown("#### 2. A Solução: Artefato Preditivo com IA Híbrida")
            st.markdown("""O artefato proposto introduz três inovações práticas:

* **Duas Janelas Temporais:** Suporte em t+2 (compras com 14 dias via Open-Meteo) e t+1 (re-forecast na sexta-feira).
* **Modelo Híbrido 50/50:** Combinação linear ponderada que alcança o menor erro global (**MAE 20,20 ref/dia**).
* **Margens Conformal:** Calibração não-paramétrica (P85 com +18 ref) garantindo **84,9% de proteção estudantil** contra falta de comida.""")

    # Galeria Completa das 33 Figuras Oficiais
    st.markdown("---")
    st.markdown("### 🖼️ Galeria Visual da Pesquisa (Figuras Oficiais em 300 DPI)")
    
    pasta_figuras = os.path.join(ROOT_DIR, "dissertacao", "figuras")
    
    categorias_fig = {
        "Etapa 1: Arquitetura e Metodologia DSR": [
            ("figura_01_aplicacao_dsr_pesquisa.png", "Figura 01 — Aplicação do método DSR à pesquisa de gestão pública alimentar"),
            ("figura_02_sintese_metodologica.png", "Figura 02 — Síntese das seis etapas do percurso metodológico DSR"),
            ("figura_03_pipeline_dados_camadas.png", "Figura 03 — Arquitetura de dados em camadas Medallion (Bronze, Silver e Gold)"),
            ("figura_04_protocolo_modelagem_validacao.png", "Figura 04 — Protocolo experimental de validação walk-forward"),
            ("figura_05_arquitetura_sistemica_artefato.png", "Figura 05 — Arquitetura sistêmica do artefato computacional preditivo"),
            ("figura_06_fluxo_operacional_artefato.png", "Figura 06 — Fluxo operacional preditivo nas janelas t+1 e t+2")
        ],
        "Etapa 2: Diagnóstico Histórico e Consumo (2023 a 2025)": [
            ("figura_07_perfil_semanal_consumo.png", "Figura 07 — Perfil semanal médio de consumo de refeições (2023 a 2025)"),
            ("figura_08_perfil_semanal_por_ano_letivo.png", "Figura 08 — Variação do perfil semanal de consumo ano a ano"),
            ("figura_09_oferta_consumo_por_proteina.png", "Figura 09 — Oferta e consumo por tipo de proteína servida"),
            ("figura_10_consumo_conforme_tecnica_preparo.png", "Figura 10 — Consumo médio conforme a técnica culinária de preparo"),
            ("figura_11_consumo_por_faixa_precipitacao.png", "Figura 11 — Consumo diário por faixa de chuva acumulada"),
            ("figura_12_relacao_temperatura_maxima_consumo.png", "Figura 12 — Relação linear entre temperatura máxima (Open-Meteo) e consumo"),
            ("figura_13_funcoes_autocorrelacao_temporal.png", "Figura 13 — Função de autocorrelação temporal (ACF simples)")
        ],
        "Etapa 3: Engenharia de Features e Camada Gold": [
            ("figura_14_ranking_importancia_atributos_rf.png", "Figura 14 — Ranking de importância dos atributos via Random Forest"),
            ("figura_15_correlacao_atributos_consumo_pearson.png", "Figura 15 — Correlação linear de Pearson calculada na base Gold")
        ],
        "Etapa 4: Efeito Compensatório e Confronto de Regimes": [
            ("figura_16_decomposicao_efeito_compensatorio.png", "Figura 16 — Decomposição do efeito compensatório (saldo líquido vs desvios diários)"),
            ("figura_17_painel_anual_sobras_faltas.png", "Figura 17 — Painel anual de sobras e déficits potenciais nas reservas discentes")
        ],
        "Etapa 5: Modelagem Preditiva e Ranking de Modelos (2026)": [
            ("figura_18_melhor_mae_por_cenario_horizonte.png", "Figura 18 — Melhor MAE obtido por cenário e horizonte de decisão"),
            ("figura_19_comparacao_regressao_linear_t2_clima.png", "Figura 19 — Impacto preditivo da meteorologia Open-Meteo no horizonte t+2"),
            ("figura_20_comparacao_horizontes_5_algoritmos.png", "Figura 20 — Comparação de desempenho dos principais algoritmos"),
            ("figura_21_ranking_modelos.png", "Figura 21 — Ranking geral dos modelos preditivos vs quantitativo humano")
        ],
        "Etapa 6: Modelo Híbrido, Margens Conformal e Riscos": [
            ("figura_22_sobras_faltas_politicas.png", "Figura 22 — Balanço de sobras e déficits potenciais sob diferentes políticas"),
            ("figura_23_fronteira_equilibrio_modelo_hibrido.png", "Figura 23 — Fronteira de equilíbrio do modelo híbrido em função de alpha"),
            ("figura_24_distribuicao_erros_diarios.png", "Figura 24 — Distribuição dos erros diários (KDE: Nutri vs IA vs Híbrido)"),
            ("figura_25_margens_seguranca_conformal.png", "Figura 25 — Efeito das margens de segurança Conformal Prediction"),
            ("figura_26_simulacao_faixas_risco_monte_carlo.png", "Figura 26 — Simulação de incerteza estocástica de Monte Carlo"),
            ("figura_27_tradeoff_custo_atendimento.png", "Figura 27 — Trade-off entre custo de desperdício e taxa de atendimento"),
            ("figura_28_comparacao_historica_consolidada.png", "Figura 28 — Confronto histórico consolidado dos regimes com o artefato")
        ],
        "Etapa 7: Validação Prospectiva da Defesa (Setembro e Outubro/2026)": [
            ("figura_29_serie_temporal_setembro_chuva_vs_consumo.png", "Figura 29 — Série temporal de setembro/2026 com eventos extremos de chuva"),
            ("figura_30_confronto_diario_setembro_ia_vs_nutricionista.png", "Figura 30 — Confronto em setembro/2026: Consumo real vs IA vs Nutrição"),
            ("figura_31_balanco_sobras_faltas_politicas_setembro.png", "Figura 31 — Balanço de sobras e faltas acumuladas em setembro sob 3 políticas"),
            ("figura_32_validacao_semana_retorno_outubro_catraca_vs_ia_nutri.png", "Figura 32 — Validação cega na semana de retorno pós-recesso de outubro: Consumo real vs IA"),
            ("figura_33_distribuicao_residuos_recalculo_margens_seguranca.png", "Figura 33 — Recálculo empírico das margens de segurança na validação prospectiva")
        ]
    }
    
    cat_sel = st.selectbox("Selecione o Bloco Temático da Pesquisa:", list(categorias_fig.keys()))
    for arq, tit in categorias_fig[cat_sel]:
        caminho_img = os.path.join(pasta_figuras, arq)
        if os.path.exists(caminho_img):
            st.markdown(f"##### {tit}")
            st.image(caminho_img, caption=tit, use_container_width=True)
            st.write("")
        else:
            st.warning(f"Arquivo não localizado na pasta: {arq}")

# ==============================================================================
# PÁGINA 6: GUIA PRÁTICO (POP DE ROTINA EM 3 MINUTOS)
# ==============================================================================
elif pagina_ativa == "📋 Guia Prático":
    st.markdown("### 📋 Guia Prático & Procedimento Operacional Padrão (POP)")
    
    renderizar_painel_explicativo(
        objetivo_rotina=(
            "**Servir como cartilha rápida de consulta para o dia a dia.** "
            "Ideal para treinar novos funcionários da cozinha, estagiários de nutrição ou consultar dúvidas rápidas."
        ),
        como_foi_feito_ciencia=(
            "**Transposição Tecnológica da Pesquisa:** "
            "Condensa as conclusões dos capítulos 4, 5 e 6 da dissertação em passos operacionais práticos e executáveis."
        ),
        como_usar_passos=(
            "1. **Consulte a rotina de sexta-feira** antes de passar a ordem de preparo.\n"
            "2. **Verifique as ações recomendadas** para dias de chuva forte ou sextas-feiras.\n"
            "3. **Mantenha este guia salvo** como referência operacional do restaurante."
        )
    )

    st.markdown("""
    #### 🗓️ Rotina Semanal em 3 Minutos
    
    1. **Toda Sexta-feira (Planejamento da Produção t+1):**
       - Acesse a página **'📝 Cadastrar Dados'** e informe os pratos previstos para a semana seguinte.
       - Acesse a página **'🔮 Previsões'**:
         - Confira a recomendação em **'👉 Ordem de Preparo'** para cada dia.
         - Baixe a planilha em CSV e envie a grade para a equipe de cozinha terceirizada.
       
    2. **Diariamente (Registro Rápido após as 14h):**
       - Acesse a página **'📝 Cadastrar Dados'** e digite a quantidade real de refeições servidas no almoço. Isso mantém o modelo sempre afinado.
       
    3. **Quinzenalmente (Planejamento de Compras de Secos t+2):**
       - Acesse a página **'📦 Compras & Suprimentos'** para ver a projeção das próximas duas semanas e dimensionar pedidos de estoque.
       
    ---
    
    #### ⚠️ Como Agir em Dias Especiais
    
    * **Dias de Tempestade / Alagamentos:**
      O sistema reduz automaticamente a folga de segurança para evitar que a comida fique sobrando no balcão de distribuição.
    * **Sextas-feiras:**
      O modelo já calcula a queda natural de ~20% no comparecimento discente no turno vespertino.
    * **Cardápio com Carne Bovina:**
      O modelo ajusta a quantidade para cima para garantir que nenhum estudante fique sem comer no dia de maior procura.
    """)
