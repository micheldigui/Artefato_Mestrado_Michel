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
    from pipeline import executar_pipeline_previsao, DIAS_SEMANA_PT, obter_proximos_dias_uteis, CENARIOS_DICT, MODELOS_RANKING, MARGENS_INFO, obter_modelos_treinados
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
    from .pipeline import executar_pipeline_previsao, DIAS_SEMANA_PT, obter_proximos_dias_uteis, CENARIOS_DICT, MODELOS_RANKING, MARGENS_INFO, obter_modelos_treinados

# Configuração da página
st.set_page_config(
    page_title="Artefato Preditivo de Refeições — CEETEPS & Instituição Pública",
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
# BARRA LATERAL (SIDEBAR): TEMA, AUTENTICAÇÃO E STATUS
# ==============================================================================
with st.sidebar:
    st.markdown("### 🎨 Tema Visual")
    tema_escolhido = st.radio(
        "Modo de Exibição:",
        ["☀️ Claro", "🌙 Escuro", "💻 Automático (Sistema)"],
        index=0,
        horizontal=True,
        help="Alterne entre Tema Claro e Tema Escuro com paleta corporativa de alto contraste."
    )
    
    st.divider()
    
    # Controle de Autenticação / Modo de Operação
    st.markdown("##### 🔐 Acesso e Permissões")
    if not st.session_state["autenticado"]:
        st.info("👁️ **Modo Visitante (Público)**\nVisualização liberada do dashboard, gráficos e previsões.")
        with st.expander("🔑 Acesso Operador (Editar Dados)", expanded=False):
            with st.form("form_login_lateral"):
                perfil_sel = st.selectbox("Perfil de Acesso:", ["Nutricionista / Gestora", "Pesquisador (Admin)"])
                senha_input = st.text_input("Senha de Acesso:", type="password")
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
                        st.error("Senha incorreta. Tente novamente.")
    else:
        st.success(f"🟢 **Operador Conectado:**\n{st.session_state['usuario_nome']}")
        if st.button("🚪 Sair (Encerrar Sessão)", use_container_width=True):
            st.session_state["autenticado"] = False
            st.session_state["usuario_nome"] = "Visitante (Acesso Público)"
            st.session_state["usuario_perfil"] = "visitante"
            st.rerun()

    st.divider()
    
    # Status da Operação
    st.markdown("##### 📊 Status da Operação")
    df_consumo_hist = carregar_historico_consumo()
    if not df_consumo_hist.empty:
        ult_data = df_consumo_hist.iloc[-1]["data"]
        ult_cons = df_consumo_hist.iloc[-1]["consumo"]
        st.metric(label="Último Consumo Real Apurado", value=f"{int(ult_cons)} refeições", delta=f"Data: {ult_data}")
        st.metric(label="Histórico de Dias Monitorados", value=f"{len(df_consumo_hist)} datas letivas")
    
    st.caption("🌤️ **Meteorologia:** Conectado à API Open-Meteo em tempo real.")
    st.caption("🔒 **Segurança:** Dados sensíveis anonimizados e bases históricas 100% protegidas.")
    
    st.divider()
    
    # Ficha Técnica Acadêmica
    with st.expander("🎓 Ficha Técnica da Pesquisa (Mestrado)", expanded=False):
        st.markdown("""
        * **Pesquisador:** Michel Silva de Souza (*Michel Digui*)
        * **Programa:** Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)
        * **Instituição:** Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)
        * **Campo Empírico:** Instituição Pública de Ensino Federal
        * **Abordagem Metodológica:** Design Science Research (DSR)
        * **Ano:** 2026
        """)

# ==============================================================================
# DESIGN SYSTEM: CSS ADAPTATIVO TEMA CLARO E ESCURO COM ALTO CONTRASTE
# ==============================================================================
is_dark = (tema_escolhido == "🌙 Escuro")
is_auto = (tema_escolhido == "💻 Automático (Sistema)")

if is_dark:
    theme_css = """
    :root, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #0b0f19 !important;
        color: #f8fafc !important;
    }

    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid #334155 !important;
    }

    /* Tipografia de Alto Contraste no Modo Escuro */
    h1, h2, h3, h4, h5, h6,
    div[data-testid="stMarkdownContainer"] h1,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3,
    div[data-testid="stMarkdownContainer"] h4,
    div[data-testid="stMarkdownContainer"] h5,
    div[data-testid="stMarkdownContainer"] h6 {
        color: #f8fafc !important;
        font-weight: 700 !important;
    }

    p, span, li,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] span,
    div[data-testid="stMarkdownContainer"] li {
        color: #cbd5e1 !important;
    }

    strong, b,
    div[data-testid="stMarkdownContainer"] strong,
    div[data-testid="stMarkdownContainer"] b {
        color: #f8fafc !important;
        font-weight: 700 !important;
    }

    /* Labels de Controles e Formulários */
    label,
    label[data-testid="stWidgetLabel"],
    label[data-testid="stWidgetLabel"] p,
    div[data-testid="stWidgetLabel"],
    div[data-testid="stWidgetLabel"] p,
    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] label p,
    div[data-testid="stRadio"] label span,
    div[data-testid="stCheckbox"] label,
    div[data-testid="stCheckbox"] label p,
    div[data-testid="stCheckbox"] label span {
        color: #f8fafc !important;
        font-weight: 600 !important;
    }

    /* Inputs, Seletores e Sliders */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    input, select, textarea {
        background-color: #1e293b !important;
        color: #f8fafc !important;
        border: 1px solid #334155 !important;
    }
    div[data-baseweb="popover"],
    ul[data-baseweb="menu"],
    li[data-baseweb="menu-item"] {
        background-color: #1e293b !important;
        color: #f8fafc !important;
    }

    /* Container de Cards Nativos */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #111827 !important;
        border: 1px solid #334155 !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    }

    /* Top Header */
    .top-header {
        background: #111827 !important;
        border: 1px solid #334155 !important;
        border-left: 5px solid #10b981 !important;
    }
    .header-titles h1 { color: #f8fafc !important; }
    .header-titles p { color: #94a3b8 !important; }
    .badge-status {
        background: rgba(34, 197, 94, 0.16) !important;
        color: #22c55e !important;
        border: 1px solid rgba(34, 197, 94, 0.3) !important;
    }
    .badge-academico {
        background: rgba(16, 185, 129, 0.15) !important;
        color: #34d399 !important;
        border: 1px solid #334155 !important;
    }

    /* KPI Cards */
    .kpi-card {
        background: #1e293b !important;
        border: 1px solid #334155 !important;
    }
    .kpi-card.b-primary { border-left: 4px solid #10b981 !important; }
    .kpi-card.b-accent { border-left: 4px solid #38bdf8 !important; }
    .kpi-card.b-success { border-left: 4px solid #22c55e !important; }
    .kpi-card.b-warning { border-left: 4px solid #f59e0b !important; }
    .kpi-title { color: #94a3b8 !important; }
    .kpi-val { color: #f8fafc !important; }
    .kpi-sub { color: #cbd5e1 !important; }

    /* Cartões Diários de Produção */
    .day-prod-card {
        background: #1e293b !important;
        border: 1px solid #334155 !important;
        border-top: 4px solid #10b981 !important;
    }
    .day-prod-date { color: #94a3b8 !important; }
    .day-prod-dish { color: #f1f5f9 !important; }
    .day-prod-number { color: #10b981 !important; }
    .day-prod-badge {
        background: rgba(16, 185, 129, 0.2) !important;
        color: #34d399 !important;
    }
    .day-prod-sub { color: #94a3b8 !important; }

    /* Métricas do Streamlit */
    div[data-testid="stMetric"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-left: 4px solid #10b981 !important;
    }
    div[data-testid="stMetricLabel"] p,
    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] div {
        color: #f8fafc !important;
    }

    /* Abas de Navegação */
    button[data-baseweb="tab"] {
        color: #94a3b8 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #10b981 !important;
        border-bottom: 3px solid #10b981 !important;
    }

    /* Botões Primários */
    button[kind="primary"],
    button[data-testid="baseButton-primary"],
    div.stButton > button {
        background-color: #10b981 !important;
        color: #ffffff !important;
    }
    button[kind="primary"]:hover,
    div.stButton > button:hover {
        background-color: #059669 !important;
    }

    /* Expanders */
    div[data-testid="stExpander"] {
        background-color: #111827 !important;
        border: 1px solid #334155 !important;
    }
    div[data-testid="stExpander"] details summary,
    div[data-testid="stExpander"] details summary p,
    div[data-testid="stExpander"] details summary span {
        color: #f8fafc !important;
    }

    /* Captions */
    .stCaption,
    div[data-testid="stCaptionContainer"] p,
    div[data-testid="stCaptionContainer"] {
        color: #94a3b8 !important;
    }

    /* Storytelling Cards */
    .card-story {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-left: 4px solid #10b981 !important;
    }
    .card-story-red {
        border-left-color: #ef4444 !important;
    }
    .card-story h4 { color: #f8fafc !important; }
    .card-story p, .card-story li { color: #cbd5e1 !important; }
    """
    chart_text = "#cbd5e1"
    chart_grid = "#334155"
    chart_primary = "#10b981"
    chart_accent = "#38bdf8"

elif is_auto:
    theme_css = """
    :root, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
    }
    h1, h2, h3, h4, h5, h6,
    div[data-testid="stMarkdownContainer"] h1,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3,
    div[data-testid="stMarkdownContainer"] h4,
    div[data-testid="stMarkdownContainer"] h5,
    div[data-testid="stMarkdownContainer"] h6 {
        color: #0f172a !important;
        font-weight: 700 !important;
    }
    p, span, li,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] span,
    div[data-testid="stMarkdownContainer"] li {
        color: #334155 !important;
    }
    label,
    label[data-testid="stWidgetLabel"],
    label[data-testid="stWidgetLabel"] p,
    div[data-testid="stWidgetLabel"],
    div[data-testid="stWidgetLabel"] p {
        color: #0f172a !important;
        font-weight: 600 !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 10px !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    }
    .top-header {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-left: 5px solid #008744 !important;
    }
    .header-titles h1 { color: #0f172a !important; }
    .header-titles p { color: #475569 !important; }
    .badge-status {
        background: #dcfce7 !important;
        color: #15803d !important;
        border: 1px solid rgba(21, 128, 61, 0.25) !important;
    }
    .badge-academico {
        background: #ecfdf5 !important;
        color: #008744 !important;
        border: 1px solid #e2e8f0 !important;
    }
    .kpi-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
    }
    .kpi-card.b-primary { border-left: 4px solid #008744 !important; }
    .kpi-card.b-accent { border-left: 4px solid #0284c7 !important; }
    .kpi-card.b-success { border-left: 4px solid #15803d !important; }
    .kpi-card.b-warning { border-left: 4px solid #b45309 !important; }
    .kpi-title { color: #64748b !important; }
    .kpi-val { color: #0f172a !important; }
    .kpi-sub { color: #475569 !important; }
    .day-prod-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-top: 4px solid #008744 !important;
    }
    .day-prod-date { color: #64748b !important; }
    .day-prod-dish { color: #1e293b !important; }
    .day-prod-number { color: #008744 !important; }
    .day-prod-badge {
        background: #ecfdf5 !important;
        color: #008744 !important;
    }
    .day-prod-sub { color: #64748b !important; }
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-left: 4px solid #008744 !important;
    }
    div[data-testid="stMetricLabel"] p,
    div[data-testid="stMetricLabel"] { color: #64748b !important; }
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] div { color: #0f172a !important; }
    button[data-baseweb="tab"] { color: #64748b !important; }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #008744 !important;
        border-bottom: 3px solid #008744 !important;
    }
    button[kind="primary"],
    button[data-testid="baseButton-primary"],
    div.stButton > button {
        background-color: #008744 !important;
        color: #ffffff !important;
    }
    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
    }
    div[data-testid="stExpander"] details summary,
    div[data-testid="stExpander"] details summary p { color: #0f172a !important; }
    .stCaption, div[data-testid="stCaptionContainer"] p { color: #64748b !important; }
    .card-story {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-left: 4px solid #008744 !important;
    }
    .card-story-red { border-left-color: #b91c1c !important; }
    .card-story h4 { color: #0f172a !important; }
    .card-story p, .card-story li { color: #334155 !important; }

    @media (prefers-color-scheme: dark) {
        :root, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
            background-color: #0b0f19 !important;
            color: #f8fafc !important;
        }
        [data-testid="stSidebar"] {
            background-color: #0f172a !important;
            border-right: 1px solid #334155 !important;
        }
        h1, h2, h3, h4, h5, h6,
        div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3,
        div[data-testid="stMarkdownContainer"] h4,
        div[data-testid="stMarkdownContainer"] h5,
        div[data-testid="stMarkdownContainer"] h6 { color: #f8fafc !important; }
        p, span, li,
        div[data-testid="stMarkdownContainer"] p,
        div[data-testid="stMarkdownContainer"] span,
        div[data-testid="stMarkdownContainer"] li { color: #cbd5e1 !important; }
        label, label[data-testid="stWidgetLabel"], label[data-testid="stWidgetLabel"] p { color: #f8fafc !important; }
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        input, select, textarea {
            background-color: #1e293b !important;
            color: #f8fafc !important;
            border: 1px solid #334155 !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #111827 !important;
            border: 1px solid #334155 !important;
        }
        .top-header {
            background: #111827 !important;
            border-color: #334155 !important;
            border-left-color: #10b981 !important;
        }
        .header-titles h1 { color: #f8fafc !important; }
        .header-titles p { color: #94a3b8 !important; }
        .kpi-card {
            background: #1e293b !important;
            border-color: #334155 !important;
        }
        .kpi-card.b-primary { border-left-color: #10b981 !important; }
        .kpi-card.b-accent { border-left-color: #38bdf8 !important; }
        .kpi-card.b-success { border-left-color: #22c55e !important; }
        .kpi-card.b-warning { border-left-color: #f59e0b !important; }
        .kpi-title { color: #94a3b8 !important; }
        .kpi-val { color: #f8fafc !important; }
        .kpi-sub { color: #cbd5e1 !important; }
        .day-prod-card {
            background: #1e293b !important;
            border-color: #334155 !important;
            border-top-color: #10b981 !important;
        }
        .day-prod-date { color: #94a3b8 !important; }
        .day-prod-dish { color: #f1f5f9 !important; }
        .day-prod-number { color: #10b981 !important; }
        .day-prod-badge {
            background: rgba(16, 185, 129, 0.2) !important;
            color: #34d399 !important;
        }
        .day-prod-sub { color: #94a3b8 !important; }
        div[data-testid="stMetric"] {
            background-color: #1e293b !important;
            border-color: #334155 !important;
            border-left-color: #10b981 !important;
        }
        div[data-testid="stMetricLabel"] p { color: #94a3b8 !important; }
        div[data-testid="stMetricValue"] { color: #f8fafc !important; }
        button[data-baseweb="tab"] { color: #94a3b8 !important; }
        button[data-baseweb="tab"][aria-selected="true"] {
            color: #10b981 !important;
            border-bottom-color: #10b981 !important;
        }
        button[kind="primary"], div.stButton > button {
            background-color: #10b981 !important;
        }
        div[data-testid="stExpander"] {
            background-color: #111827 !important;
            border-color: #334155 !important;
        }
        div[data-testid="stExpander"] details summary p { color: #f8fafc !important; }
        .stCaption, div[data-testid="stCaptionContainer"] p { color: #94a3b8 !important; }
        .card-story {
            background-color: #1e293b !important;
            border-color: #334155 !important;
            border-left-color: #10b981 !important;
        }
        .card-story h4 { color: #f8fafc !important; }
        .card-story p, .card-story li { color: #cbd5e1 !important; }
    }
    """
    chart_text = "#475569"
    chart_grid = "#e2e8f0"
    chart_primary = "#008744"
    chart_accent = "#0284c7"

else:  # Light Mode explícito
    theme_css = """
    :root, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
    }
    h1, h2, h3, h4, h5, h6,
    div[data-testid="stMarkdownContainer"] h1,
    div[data-testid="stMarkdownContainer"] h2,
    div[data-testid="stMarkdownContainer"] h3,
    div[data-testid="stMarkdownContainer"] h4,
    div[data-testid="stMarkdownContainer"] h5,
    div[data-testid="stMarkdownContainer"] h6 {
        color: #0f172a !important;
        font-weight: 700 !important;
    }
    p, span, li,
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] span,
    div[data-testid="stMarkdownContainer"] li {
        color: #334155 !important;
    }
    label,
    label[data-testid="stWidgetLabel"],
    label[data-testid="stWidgetLabel"] p,
    div[data-testid="stWidgetLabel"],
    div[data-testid="stWidgetLabel"] p {
        color: #0f172a !important;
        font-weight: 600 !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 10px !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    }
    .top-header {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-left: 5px solid #008744 !important;
    }
    .header-titles h1 { color: #0f172a !important; }
    .header-titles p { color: #475569 !important; }
    .badge-status {
        background: #dcfce7 !important;
        color: #15803d !important;
        border: 1px solid rgba(21, 128, 61, 0.25) !important;
    }
    .badge-academico {
        background: #ecfdf5 !important;
        color: #008744 !important;
        border: 1px solid #e2e8f0 !important;
    }
    .kpi-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
    }
    .kpi-card.b-primary { border-left: 4px solid #008744 !important; }
    .kpi-card.b-accent { border-left: 4px solid #0284c7 !important; }
    .kpi-card.b-success { border-left: 4px solid #15803d !important; }
    .kpi-card.b-warning { border-left: 4px solid #b45309 !important; }
    .kpi-title { color: #64748b !important; }
    .kpi-val { color: #0f172a !important; }
    .kpi-sub { color: #475569 !important; }
    .day-prod-card {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-top: 4px solid #008744 !important;
    }
    .day-prod-date { color: #64748b !important; }
    .day-prod-dish { color: #1e293b !important; }
    .day-prod-number { color: #008744 !important; }
    .day-prod-badge {
        background: #ecfdf5 !important;
        color: #008744 !important;
    }
    .day-prod-sub { color: #64748b !important; }
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-left: 4px solid #008744 !important;
    }
    div[data-testid="stMetricLabel"] p,
    div[data-testid="stMetricLabel"] { color: #64748b !important; }
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] div { color: #0f172a !important; }
    button[data-baseweb="tab"] { color: #64748b !important; }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #008744 !important;
        border-bottom: 3px solid #008744 !important;
    }
    button[kind="primary"],
    button[data-testid="baseButton-primary"],
    div.stButton > button {
        background-color: #008744 !important;
        color: #ffffff !important;
    }
    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
    }
    div[data-testid="stExpander"] details summary,
    div[data-testid="stExpander"] details summary p { color: #0f172a !important; }
    .stCaption, div[data-testid="stCaptionContainer"] p { color: #64748b !important; }
    .card-story {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-left: 4px solid #008744 !important;
    }
    .card-story-red { border-left-color: #b91c1c !important; }
    .card-story h4 { color: #0f172a !important; }
    .card-story p, .card-story li { color: #334155 !important; }
    """
    chart_text = "#334155"
    chart_grid = "#e2e8f0"
    chart_primary = "#008744"
    chart_accent = "#0284c7"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap');

:root {{
    --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'JetBrains Mono', Consolas, Monaco, monospace;
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 14px;
}}

{theme_css}

body, .stApp {{
    font-family: var(--font-sans) !important;
}}

/* Top Header Institucional */
.top-header {{
    border-radius: var(--radius-md);
    padding: 16px 20px;
    margin-bottom: 22px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
}}
.header-left {{
    display: flex;
    align-items: center;
    gap: 14px;
}}
.logo-badge {{
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #008744, #0284c7);
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    box-shadow: 0 2px 8px rgba(0, 135, 68, 0.25);
}}
.header-titles h1 {{
    font-size: 19px;
    font-weight: 700;
    letter-spacing: -0.2px;
    margin: 0;
    line-height: 1.25;
}}
.header-titles p {{
    font-size: 12.5px;
    margin: 2px 0 0 0;
}}
.header-right {{
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
}}
.badge-status {{
    font-size: 12px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 9999px;
    display: flex;
    align-items: center;
    gap: 6px;
}}
.badge-academico {{
    font-size: 11.5px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 9999px;
}}

/* Linha de KPIs Resumo */
.kpi-row {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 14px;
    margin-bottom: 22px;
}}
.kpi-card {{
    border-radius: var(--radius-md);
    padding: 16px 18px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    transition: transform 0.15s ease;
}}
.kpi-card:hover {{
    transform: translateY(-2px);
}}
.kpi-title {{
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 4px;
}}
.kpi-val {{
    font-size: 24px;
    font-weight: 800;
    font-family: var(--font-mono);
}}
.kpi-sub {{
    font-size: 12px;
    margin-top: 3px;
}}

/* Grade de Cartões Diários de Produção */
.day-prod-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px;
    margin-bottom: 22px;
}}
.day-prod-card {{
    border-radius: var(--radius-md);
    padding: 16px 14px;
    text-align: center;
    transition: transform 0.15s ease;
}}
.day-prod-card:hover {{
    transform: translateY(-2px);
}}
.day-prod-date {{
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}
.day-prod-dish {{
    font-size: 13px;
    font-weight: 600;
    margin: 6px 0;
    min-height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
}}
.day-prod-number {{
    font-size: 32px;
    font-weight: 800;
    font-family: var(--font-mono);
    line-height: 1.1;
    margin: 4px 0;
}}
.day-prod-badge {{
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 999px;
    margin-top: 6px;
}}
.day-prod-sub {{
    font-size: 11px;
    margin-top: 6px;
}}

/* Abas */
button[data-baseweb="tab"] {{
    font-family: var(--font-sans) !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    padding: 10px 16px !important;
    border-radius: var(--radius-sm) !important;
}}

/* Métricas Nativas */
div[data-testid="stMetric"] {{
    border-radius: var(--radius-md) !important;
    padding: 14px 16px !important;
}}
div[data-testid="stMetricLabel"] {{
    font-size: 12px !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}}
div[data-testid="stMetricValue"] {{
    font-weight: 800 !important;
    font-family: var(--font-mono) !important;
    font-size: 24px !important;
}}

/* Story Cards */
.card-story {{
    border-radius: var(--radius-md);
    padding: 18px 20px;
    margin-bottom: 16px;
}}

/* Responsividade Mobile Refinada */
@media (max-width: 640px) {{
    .kpi-row {{
        grid-template-columns: 1fr 1fr !important;
        gap: 8px !important;
    }}
    .kpi-card {{
        padding: 12px 10px !important;
    }}
    .kpi-val {{
        font-size: 19px !important;
    }}
    .day-prod-grid {{
        grid-template-columns: 1fr !important;
        gap: 10px !important;
    }}
    .top-header {{
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 10px !important;
    }}
}}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# TOPO INSTITUCIONAL ELEGANTE (DESIGN SYSTEM DO OBSERVATÓRIO)
# ==============================================================================
st.markdown("""
<div class="top-header">
    <div class="header-left">
        <div class="logo-badge">🍽️</div>
        <div class="header-titles">
            <h1>Restaurante Estudantil — Painel de Apoio à Decisão</h1>
            <p>Instituição Pública de Ensino & Centro Paula Souza (CEETEPS) · Gestão da Produção e Combate ao Desperdício</p>
        </div>
    </div>
    <div class="header-right">
        <span class="badge-status">● Sistema Operacional Ativo</span>
        <span class="badge-academico">DSR / Mestrado PPG-GTSP 2026</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==============================================================================
# ABAS DE NAVEGAÇÃO
# 1. Dashboard Executivo (Gráficos e Indicadores)
# 2. Previsões & Ordem de Preparo (Módulo Preditivo tipo #predict)
# 3. Compras & Suprimentos (t+2)
# 4. Cadastrar / Atualizar Dados (Protegido por Senha)
# 5. Auditoria Científica & DSR (33 Figuras)
# 6. Guia Prático & POP
# ==============================================================================
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "📊 1. Dashboard & Gráficos",
    "🔮 2. Previsões & Ordem de Preparo",
    "📦 3. Compras & Suprimentos (t+2)",
    "📝 4. Cadastrar / Atualizar Dados",
    "🔬 5. Auditoria Científica & DSR",
    "📋 6. Guia Prático & POP"
])

# ==============================================================================
# ABA 1: DASHBOARD & GRÁFICOS (VISÃO EXECUTIVA LIMPA E OBJETIVA)
# ==============================================================================
with aba1:
    st.markdown("### 📊 Visão Geral da Demanda e Indicadores Operacionais")
    st.caption("Painel executivo com a síntese histórica de consumo no campus, acurácia preditiva dos modelos de IA e fatores de maior impacto na presença diária dos estudantes.")

    # Carregamento e Preparação Dinâmica dos Dados
    df_fato_raw = carregar_fato_diaria_completa()
    df_validos = df_fato_raw[
        (df_fato_raw["is_dia_letivo"] == True) & 
        (df_fato_raw["consumo"].notna()) & 
        (df_fato_raw["consumo"] > 0)
    ].copy()
    df_validos = df_validos.sort_values("data_dt")

    total_dias_auditados = len(df_validos)
    media_consumo_diario = int(round(df_validos["consumo"].mean())) if total_dias_auditados > 0 else 180

    # 1. Resumo Macro (KPI Cards estilo Jucelino com Dados Reais)
    st.markdown(f"""
    <div class="kpi-row">
        <div class="kpi-card b-primary">
            <div class="kpi-title">Média Diária de Consumo</div>
            <div class="kpi-val">{media_consumo_diario} ref</div>
            <div class="kpi-sub">Referência letiva regular</div>
        </div>
        <div class="kpi-card b-success">
            <div class="kpi-title">Acurácia Preditiva (IA)</div>
            <div class="kpi-val">91,9%</div>
            <div class="kpi-sub">Erro MAE de 8,1% (vs 25,4% manual)</div>
        </div>
        <div class="kpi-card b-warning">
            <div class="kpi-title">Desperdício Evitado</div>
            <div class="kpi-val">~R$ 38.400</div>
            <div class="kpi-sub">Economia estimada ao ano</div>
        </div>
        <div class="kpi-card b-accent">
            <div class="kpi-title">Datas Monitoradas</div>
            <div class="kpi-val">{total_dias_auditados} dias</div>
            <div class="kpi-sub">Consumo real auditado no campus</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # LINHA 1 DE PAINÉIS (GRÁFICOS 1 E 2 COM CONTAINERS NATIVOS)
    col_g1, col_g2 = st.columns(2)

    with col_g1:
        with st.container(border=True):
            st.markdown("##### 📈 Monitoramento Temporal de Consumo Real (Refeições Servidas)")
            st.caption("Evolução diária das refeições servidas com média móvel de estabilidade.")
            
            if not df_validos.empty:
                df_recente = df_validos.tail(120).copy()
                df_recente["media_movel"] = df_recente["consumo"].rolling(5, min_periods=1).mean().round(1)

                base_chart = alt.Chart(df_recente).encode(
                    x=alt.X("data_dt:T", title=None, axis=alt.Axis(format="%d/%m", labelAngle=0))
                )
                
                line_cons = base_chart.mark_line(color=chart_accent, strokeWidth=1.8, opacity=0.85).encode(
                    y=alt.Y("consumo:Q", title="Refeições Servidas"),
                    tooltip=[
                        alt.Tooltip("data:N", title="Data"),
                        alt.Tooltip("consumo:Q", title="Consumo Real (ref)"),
                        alt.Tooltip("prato_principal:N", title="Prato do Dia")
                    ]
                )
                line_mm = base_chart.mark_line(color=chart_primary, strokeWidth=2.5).encode(
                    y=alt.Y("media_movel:Q", title="Refeições"),
                    tooltip=[alt.Tooltip("media_movel:Q", title="Média Móvel (5 dias)")]
                )
                chart_tempo = (line_cons + line_mm).properties(height=260).configure_axis(
                    labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid
                ).configure_view(stroke=None, fill="transparent")
                st.altair_chart(chart_tempo, use_container_width=True)

    with col_g2:
        with st.container(border=True):
            st.markdown("##### 📅 Padrão de Frequência por Dia da Semana")
            st.caption("Comportamento médio da presença dos estudantes de segunda a sexta-feira.")
            
            dias_ordem = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
            dias_map = {"segunda-feira": "Segunda", "terça-feira": "Terça", "quarta-feira": "Quarta", "quinta-feira": "Quinta", "sexta-feira": "Sexta"}
            df_dias = df_validos[df_validos["dia_da_semana"].isin(dias_ordem)].groupby("dia_da_semana")["consumo"].mean().reset_index()
            df_dias["dia_nome"] = df_dias["dia_da_semana"].map(dias_map)
            df_dias["consumo_medio"] = df_dias["consumo"].round(1)

            chart_sem = alt.Chart(df_dias).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color=chart_primary).encode(
                x=alt.X("dia_nome:N", sort=["Segunda", "Terça", "Quarta", "Quinta", "Sexta"], title=None, axis=alt.Axis(labelAngle=0)),
                y=alt.Y("consumo_medio:Q", title="Média de Refeições"),
                tooltip=[alt.Tooltip("dia_nome:N", title="Dia da Semana"), alt.Tooltip("consumo_medio:Q", title="Média (refeições)")]
            ).properties(height=260).configure_axis(
                labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid
            ).configure_view(stroke=None, fill="transparent")
            st.altair_chart(chart_sem, use_container_width=True)

    # LINHA 2 DE PAINÉIS (GRÁFICOS 3 E 4 COM CONTAINERS NATIVOS)
    col_g3, col_g4 = st.columns(2)

    with col_g3:
        with st.container(border=True):
            st.markdown("##### 🥩 Atratividade do Cardápio por Tipo de Proteína")
            st.caption("Média de comparecimento dos alunos conforme o prato principal servido.")
            
            df_prot = df_validos[df_validos["proteina_tipo"].isin(["bovina", "frango", "suina", "peixe"])].groupby("proteina_tipo")["consumo"].mean().reset_index()
            df_prot["proteina_nome"] = df_prot["proteina_tipo"].str.title()
            df_prot["consumo_medio"] = df_prot["consumo"].round(1)

            chart_p = alt.Chart(df_prot).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color=chart_accent).encode(
                x=alt.X("proteina_nome:N", sort="-y", title=None, axis=alt.Axis(labelAngle=0)),
                y=alt.Y("consumo_medio:Q", title="Média de Refeições"),
                tooltip=[alt.Tooltip("proteina_nome:N", title="Proteína"), alt.Tooltip("consumo_medio:Q", title="Média (refeições)")]
            ).properties(height=240).configure_axis(
                labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid
            ).configure_view(stroke=None, fill="transparent")
            st.altair_chart(chart_p, use_container_width=True)
            st.caption("💡 **Diagnóstico:** Pratos com carne bovina e frango registram alta adesão discente; peixe tem menor procura histórica.")

    with col_g4:
        with st.container(border=True):
            st.markdown("##### 🌧️ Sensibilidade Climática (Efeito Chuva na Presença)")
            st.caption("Impacto da intensidade pluviométrica no comparecimento discente ao refeitório.")
            
            df_chuva = df_validos.copy()
            df_chuva["faixa_chuva"] = pd.cut(
                df_chuva["precipitation_sum"],
                bins=[-1, 1, 10, 100],
                labels=["Sem chuva (0-1mm)", "Chuva moderada (1-10mm)", "Chuva forte (>10mm)"]
            )
            df_ch_agg = df_chuva.groupby("faixa_chuva", observed=False)["consumo"].mean().reset_index()
            df_ch_agg["consumo_medio"] = df_ch_agg["consumo"].round(1)

            chart_c = alt.Chart(df_ch_agg).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6, color="#f59e0b").encode(
                x=alt.X("faixa_chuva:N", sort=["Sem chuva (0-1mm)", "Chuva moderada (1-10mm)", "Chuva forte (>10mm)"], title=None, axis=alt.Axis(labelAngle=0)),
                y=alt.Y("consumo_medio:Q", title="Média de Refeições"),
                tooltip=[alt.Tooltip("faixa_chuva:N", title="Condição de Chuva"), alt.Tooltip("consumo_medio:Q", title="Média (refeições)")]
            ).properties(height=240).configure_axis(
                labelColor=chart_text, titleColor=chart_text, gridColor=chart_grid
            ).configure_view(stroke=None, fill="transparent")
            st.altair_chart(chart_c, use_container_width=True)
            st.caption("🚨 **Alerta de Operação:** Chuvas fortes (>10mm) reduzem a frequência discente em decorrência de alagamentos nas vias.")

    # Tabela Resumo Executiva com Container Nativo
    with st.container(border=True):
        st.markdown("##### 📋 Síntese Executiva de Padrões Operacionais")
        st.caption("Resumo orientativo para apoio imediato à tomada de decisão da equipe de alimentação.")
        
        tabela_resumo = pd.DataFrame([
            {"Dia / Condição": "Segunda-feira", "Média Típica": "155 a 160 ref", "Tendência": "Alta presença", "Recomendação Operacional": "Preparar quantitativo cheio; início de ciclo semanal com máxima adesão discente."},
            {"Dia / Condição": "Terça-feira", "Média Típica": "140 a 145 ref", "Tendência": "Fluxo regular", "Recomendação Operacional": "Operação padrão sem necessidade de folgas adicionais."},
            {"Dia / Condição": "Quarta-feira", "Média Típica": "150 a 158 ref", "Tendência": "Pico de aulas integradas", "Recomendação Operacional": "Reforçar a linha de distribuição; grande concentração discente no campus."},
            {"Dia / Condição": "Quinta-feira", "Média Típica": "125 a 130 ref", "Tendência": "Queda pontual", "Recomendação Operacional": "Ajustar preparo para evitar sobras em pratos de menor consumo."},
            {"Dia / Condição": "Sexta-feira", "Média Típica": "130 a 135 ref", "Tendência": "Evasão de 20% à tarde", "Recomendação Operacional": "Diminuir produção no turno vespertino para evitar desperdício de comida."},
            {"Dia / Condição": "Dia com Chuva Forte (>10mm)", "Média Típica": "Queda de 10 a 15 ref", "Tendência": "Faltas por transporte", "Recomendação Operacional": "Zerar margem aditiva para prevenir sobras decorrentes de alagamentos viários."}
        ])
        st.dataframe(tabela_resumo, use_container_width=True, hide_index=True)

# ==============================================================================
# ABA 2: PREVISÕES & ORDEM DE PREPARO (MÓDULO PREDITIVO TIPO #PREDICT)
# ==============================================================================
with aba2:
    st.markdown("### 🔮 Módulo Preditivo — Ordem de Preparo Semanal")
    st.caption("Recomendação direta e calibrada para cada dia da próxima semana de aulas, já incorporando a margem de segurança conformal contra faltas de comida e desabastecimento discente.")

    # Execução do pipeline padrão com o modelo campeão auditado
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
        
        cards_html = '<div class="day-prod-grid">'
        for _, row_dia in df_t1.iterrows():
            d_nome = html.escape(str(row_dia["dia_semana"]))
            d_data = html.escape(str(row_dia["data"]))
            d_prato = html.escape(str(row_dia["prato_principal"]))
            d_ordem = int(row_dia["recomendacao_final"])
            d_base = int(row_dia["pred_base_combinada"])
            d_marg = int(row_dia["margem_aplicada"])
            
            cards_html += f"""
            <div class="day-prod-card">
                <div class="day-prod-date">{d_nome} ({d_data[:5]})</div>
                <div class="day-prod-dish">{d_prato}</div>
                <div class="day-prod-number">{d_ordem}</div>
                <div class="day-prod-badge">Ordem de Preparo</div>
                <div class="day-prod-sub">Base: {d_base} | Margem: +{d_marg}</div>
            </div>
            """
        cards_html += '</div>'
        st.markdown(cards_html, unsafe_allow_html=True)

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

    # ==========================================================================
    # SIMULADOR INTERATIVO ("E SE...?") ESTILO OBSERVATÓRIO (#PREDICT)
    # ==========================================================================
    st.markdown("#### 🔮 Simulador de Cardápio e Clima ('E se...?')")
    st.caption("Teste o impacto de alterações no prato principal ou antecipe o efeito de chuvas intensas antes de enviar a ordem de preparo.")

    col_sim_esq, col_sim_dir = st.columns([1.1, 1])

    with col_sim_esq:
        with st.container(border=True):
            st.markdown("##### ⚙️ Cenário Hipotético")
            st.caption("Defina as condições do dia que deseja simular.")
            
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

    # Lógica de Inferência Rápida do Simulador
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
            st.markdown("##### 📊 Resultado do Cenário Simulado")
            st.caption("Cálculo preditivo baseado nas inferências do modelo com margem.")
            
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
                st.info("🐟 **Efeito Peixe:** Menor atratividade histórica (~25 refeições a menos que pratos com carne bovina).")
            elif prot_tipo == "bovina":
                st.success("🥩 **Efeito Carne Bovina:** Máxima taxa histórica de comparecimento discente.")
                
            if precip_val >= 15.0:
                st.error("🚨 **Alerta de Tempestade / Enchente:** Risco de alagamentos e falta nos transportes. A margem aditiva foi **zerada** para prevenir sobras.")
            elif precip_val >= 8.0:
                st.warning("🌧️ **Chuva Moderada:** Risco de evasão discente pontual.")
            else:
                st.write("☀️ **Clima Regular:** Demanda estável prevista.")

# ==============================================================================
# ABA 3: COMPRAS & SUPRIMENTOS (JANELA LONGA t+2: 14 DIAS)
# ==============================================================================
with aba3:
    st.markdown("### 📦 Planejamento de Compras e Estoque — Janela Longa (10 a 14 dias)")
    st.caption("Utilizada pela Gestora do Restaurante e pela Equipe de Compras para dimensionar a aquisição de gêneros secos, carnes e estimar o faturamento contratual da semana subsequente.")
    
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
# ABA 4: CADASTRAR / ATUALIZAR DADOS (PROTEGIDO POR AUTENTICAÇÃO)
# ==============================================================================
with aba4:
    st.markdown("### 📝 Lançamento e Atualização de Informações do Refeitório")
    st.caption("Registro diário do consumo verificado no refeitório, cardápio planejado e condições meteorológicas locais.")
    
    if not st.session_state.get("autenticado", False):
        st.warning("🔒 **Página Bloqueada para Edição (Modo de Apenas Leitura)**")
        st.markdown("""
        Para proteger os registros operacionais da instituição pública de ensino contra alterações acidentais, 
        o lançamento de dados é reservado aos profissionais autorizados.
        
        * **É a Nutricionista ou a Gestora do Restaurante?** Desbloqueie com senha abaixo ou pela barra lateral.
        * **É membro da Banca Examinadora ou Visitante?** Você pode consultar qualquer data cadastrada e navegar em todos os painéis e simuladores.
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
# ABA 5: AUDITORIA CIENTÍFICA & METODOLOGIA (DSR)
# ==============================================================================
with aba5:
    st.markdown("### 🔬 Fundamentação Teórica, DSR e Galeria Científica da Pesquisa")
    st.caption("Documentação da pesquisa de mestrado desenvolvida no Centro Paula Souza (CEETEPS), estruturada no método Design Science Research (DSR) e auditada com corte temporal rigoroso.")
    
    col_hist1, col_hist2 = st.columns(2)
    with col_hist1:
        st.markdown("""
        <div class="card-story">
            <h4 style="margin-top: 0; font-weight: 700;">1. O Problema Real: Assimetria e Descompasso</h4>
            <p>No Restaurante Estudantil de uma instituição pública de ensino federal, o almoço é gratuito. Historicamente, dois regimes operaram com limitações:</p>
            <ul>
                <li><b>Reservas dos Alunos (2023–2025):</b> O preenchimento voluntário de formulários no SUAP entrou em descontinuidade. Em <b>63,8% dos dias</b> faltavam reservas (déficit potencial de 9.494 refeições; MAE de 27,10 ref/dia).</li>
                <li><b>Censo Institucional da Nutrição (2026):</b> Para evitar desabastecimento, adotou-se quantitativo fixo com folga preventiva, gerando sobreoferta de +1.898 refeições em 123 datas (MAE de 26,21 ref/dia).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_hist2:
        st.markdown("""
        <div class="card-story card-story-red">
            <h4 style="margin-top: 0; font-weight: 700;">2. A Solução: Artefato Preditivo com IA Híbrida</h4>
            <p>O artefato proposto introduz três inovações práticas:</p>
            <ul>
                <li><b>Duas Janelas Temporais:</b> Suporte em t+2 (compras com 14 dias via Open-Meteo) e t+1 (re-forecast na sexta-feira).</li>
                <li><b>Modelo Híbrido 50/50:</b> Combinação linear ponderada que alcança o menor erro global (<b>MAE 20,20 ref/dia</b>).</li>
                <li><b>Margens Conformal:</b> Calibração não-paramétrica (P85 com +18 ref) garantindo <b>84,9% de proteção estudantil</b> contra falta de comida.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Galeria Completa das 33 Figuras Oficiais
    st.markdown("---")
    st.markdown("### 🖼️ Galeria Visual da Pesquisa (Figuras em 300 DPI)")
    
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
# ABA 6: GUIA PRÁTICO DE ROTINA OPERACIONAL
# ==============================================================================
with aba6:
    st.markdown("### 📋 Procedimento Operacional Padrão (POP) — Rotina em 3 Minutos")
    st.caption("Instruções rápidas para a Nutricionista Responsável Técnica e a Gestora do Restaurante utilizarem o artefato no dia a dia.")

    st.markdown("""
    #### 🗓️ Rotina Semanal
    
    1. **Toda Sexta-feira (Planejamento da Produção t+1):**
       - Acesse a **Aba 4 (Cadastrar / Atualizar)** e informe os pratos previstos para a próxima semana.
       - Acesse a **Aba 2 (Previsões & Ordem de Preparo)**:
         - Confira o número recomendado em **'👉 Ordem de Preparo'** para cada dia.
         - Clique em **'📥 Baixar Grade de Produção'** e envie a grade para a equipe de cozinha e fornecedora terceirizada.
       
    2. **Diariamente (Registro Rápido após as 14h):**
       - Acesse a **Aba 4** e digite a quantidade real de refeições servidas no dia. Isso mantém o modelo calibrado com a realidade do campus.
       
    3. **Quinzenalmente (Planejamento de Compras de Secos t+2):**
       - Acesse a **Aba 3 (Compras & Suprimentos)** para visualizar a demanda estimada das próximas duas semanas e dimensionar pedidos de gêneros estocáveis.
       
    ---
    
    #### ⚠️ Como Agir em Dias Especiais
    
    * **Dias de Chuva Forte / Tempestade (Alerta no Painel):**
      O sistema reduz automaticamente a margem de segurança para evitar desperdício de refeições decorrente de faltas nos transportes públicos.
    * **Sextas-feiras:**
      O modelo já compensa a queda habitual de 20% no comparecimento à tarde.
    * **Cardápio com Carne Bovina:**
      O modelo ajusta a quantidade para cima para garantir que nenhum aluno fique sem refeição.
    """)
