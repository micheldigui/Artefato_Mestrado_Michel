"""
Interface Web Operacional do Artefato - Suporte à Decisão da Nutricionista
Desenvolvido no Padrão de Identidade Visual do Instituto Federal (IF)
Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (CEETEPS / IFSP)
"""

import os
import sys

# Garante importação limpa dos módulos locais em src/app
app_dir = os.path.dirname(os.path.abspath(__file__))
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
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
        CSV_CONSUMO_ATUALIZADO
    )
    import pipeline
    importlib.reload(pipeline)
    from pipeline import executar_pipeline_previsao, DIAS_SEMANA_PT, obter_proximos_dias_uteis
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
        CSV_CONSUMO_ATUALIZADO
    )
    from .pipeline import executar_pipeline_previsao, DIAS_SEMANA_PT, obter_proximos_dias_uteis

# Configuração da página Streamlit
st.set_page_config(
    page_title="Artefato de Previsão de Refeições — Instituto Federal",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização visual no Manual de Identidade Visual do Instituto Federal (IF)
# Verde Oficial: #006633 | Vermelho Oficial: #c8102e | Branco: #ffffff | Apoio: #f8fafc / #1e293b
st.markdown("""
<style>
    /* Estilização Geral e Cores do Instituto Federal */
    :root {
        --if-green: #006633;
        --if-green-dark: #004d26;
        --if-green-light: #e8f5e9;
        --if-red: #c8102e;
        --if-red-dark: #9b0b23;
        --if-text: #1e293b;
        --if-bg: #f8fafc;
        --if-card-bg: #ffffff;
    }

    /* Topo Institucional */
    .if-header-box {
        background: linear-gradient(135deg, #006633 0%, #004d26 100%);
        border-radius: 10px;
        padding: 16px 24px;
        color: #ffffff;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .if-title-area {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .if-logo-grid {
        display: grid;
        grid-template-columns: repeat(3, 11px);
        grid-gap: 3px;
        background: transparent;
        padding: 4px;
    }
    .if-dot {
        width: 11px;
        height: 11px;
        border-radius: 2px;
        background-color: #ffffff;
    }
    .if-dot-red {
        background-color: #c8102e !important;
        border-radius: 50%;
    }
    .if-title {
        font-size: 22px;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin: 0;
        color: #ffffff;
    }
    .if-subtitle {
        font-size: 13px;
        font-weight: 400;
        color: #e2e8f0;
        margin-top: 2px;
    }
    .if-badge-mestrado {
        background-color: #c8102e;
        color: #ffffff;
        font-size: 11px;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        white-space: nowrap;
    }

    /* Botões Primários no Verde do Instituto Federal */
    div.stButton > button:first-child[kind="primary"] {
        background-color: #006633 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:first-child[kind="primary"]:hover {
        background-color: #004d26 !important;
        box-shadow: 0 4px 12px rgba(0, 102, 51, 0.25) !important;
        transform: translateY(-1px);
    }

    /* Cards de Métricas (Ajustados para Contraste Perfeito no Tema Escuro) */
    div[data-testid="stMetric"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-top: 4px solid #006633 !important;
        border-radius: 8px !important;
        padding: 12px 16px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2) !important;
    }
    div[data-testid="stMetric"]:hover {
        border-top-color: #c8102e !important;
        transition: border-color 0.3s ease;
    }
    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 13px !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetricLabel"] > div {
        color: #94a3b8 !important;
    }
    div[data-testid="stMetricValue"] {
        color: #22c55e !important;
        font-weight: 800 !important;
        font-size: 26px !important;
    }
    div[data-testid="stMetricValue"] > div {
        color: #22c55e !important;
    }
    div[data-testid="stMetricDelta"] {
        color: #38bdf8 !important;
        font-weight: 500 !important;
    }
    div[data-testid="stMetricDelta"] > div {
        color: #38bdf8 !important;
    }

    /* Abas */
    button[data-baseweb="tab"] {
        font-weight: 600 !important;
        font-size: 14px !important;
        color: #94a3b8 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #22c55e !important;
        border-bottom-color: #006633 !important;
    }

    /* Alertas e Caixas de Apoio do Guia */
    .card-guia {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-left: 4px solid #006633 !important;
        border-radius: 8px !important;
        padding: 18px 20px !important;
        margin-bottom: 16px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.25) !important;
    }
    .card-guia p, .card-guia div, .card-guia span {
        color: #f1f5f9 !important;
        font-size: 14px !important;
        line-height: 1.6 !important;
    }
    .card-guia b {
        color: #38bdf8 !important; /* Destaque em azul claro nítido para os tópicos */
        font-weight: 700 !important;
    }
    .card-guia i {
        color: #a7f3d0 !important; /* Destaque verde menta suave */
    }
    .passo-numero {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 28px;
        height: 28px;
        background-color: #006633;
        color: #ffffff !important;
        border-radius: 50%;
        font-weight: 700;
        font-size: 14px;
        margin-right: 10px;
    }
    .passo-titulo {
        font-size: 17px !important;
        font-weight: 700 !important;
        color: #4ade80 !important;
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho com Identidade Visual do Instituto Federal
st.markdown("""
<div class="if-header-box">
    <div class="if-title-area">
        <div class="if-logo-grid">
            <div class="if-dot if-dot-red"></div>
            <div class="if-dot"></div>
            <div class="if-dot"></div>
            <div class="if-dot"></div>
            <div class="if-dot"></div>
            <div class="if-dot"></div>
            <div class="if-dot"></div>
            <div class="if-dot"></div>
            <div class="if-dot"></div>
        </div>
        <div>
            <div class="if-title">🍽️ Artefato de Apoio à Decisão: Previsão de Refeições Escolares</div>
            <div class="if-subtitle">INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA | CEETEPS — Pesquisa Aplicada em Sistemas Produtivos</div>
        </div>
    </div>
    <div class="if-badge-mestrado">Mestrado Profissional</div>
</div>
""", unsafe_allow_html=True)

# Barra Lateral Informativa
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 15px;">
        <div style="font-size: 32px;">🏛️</div>
        <div style="font-weight: 700; color: #006633; font-size: 16px;">Instituto Federal</div>
        <div style="font-size: 12px; color: #64748b;">Gestão Alimentar & IA</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Painel Operacional")
    st.info("Este artefato combina a sensibilidade da nutricionista com algoritmos de Machine Learning e margens de proteção alimentar.")
    
    df_consumo_hist = carregar_historico_consumo()
    if not df_consumo_hist.empty:
        ult_data = df_consumo_hist.iloc[-1]["data"]
        ult_cons = df_consumo_hist.iloc[-1]["consumo"]
        st.metric(label="Último Consumo Registrado", value=f"{int(ult_cons)} ref", delta=f"Data: {ult_data}")
        st.metric(label="Total de Dias Históricos", value=f"{len(df_consumo_hist)} dias")
    
    st.divider()
    st.caption("🔒 **Ambiente Seguro**: Os notebooks e bases originais da dissertação permanecem 100% imutáveis.")

# Abas de navegação (5 abas completas com Guia Passo a Passo)
aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "📝 1. Registro Diário (Catraca)",
    "📋 2. Cardápio & Nutricionista",
    "⏱️ 3. Previsão — Janela Curta (t+1: Preparo)",
    "📅 4. Previsão — Janela Longa (t+2: Compras)",
    "📖 5. Guia de Uso & Passo a Passo"
])

# -------------------------------------------------------------
# ABA 1: REGISTRO DIÁRIO DE CONSUMO
# -------------------------------------------------------------
with aba1:
    st.subheader("📝 Lançamento e Edição do Consumo Efetivo (Almoço)")
    st.write("Consulte uma data para verificar ou editar o registro existente, ou insira um novo lançamento da catraca. O histórico e o arquivo CSV são atualizados automaticamente.")
    
    col_d1, col_d2 = st.columns([1, 2])
    with col_d1:
        data_lancamento = st.date_input("Data do Atendimento", value=date.today())
    
    data_iso_sel = data_lancamento.strftime("%Y-%m-%d")
    data_fmt_sel = data_lancamento.strftime("%d/%m/%Y")
    consumo_existente = consultar_consumo_por_data(data_iso_sel)
    
    with col_d2:
        if consumo_existente is not None:
            st.info(f"📌 **Registro Existente Encontrado:** Na data **{data_fmt_sel}**, constam **{int(consumo_existente)} refeições** servidas. Você pode editar o valor abaixo.")
            val_init = int(consumo_existente)
            texto_btn = "✏️ Atualizar / Salvar Edição de Consumo"
            tipo_acao = "atualizado"
        else:
            st.success(f"✨ Nenhum registro cadastrado para **{data_fmt_sel}**. Digite a quantidade da catraca abaixo para cadastrar.")
            val_init = 0
            texto_btn = "💾 Cadastrar Novo Consumo"
            tipo_acao = "cadastrado"
            
    col1, col2 = st.columns([2, 2])
    with col1:
        consumo_input = st.number_input(
            "Refeições Servidas (Catraca/Contagem)",
            min_value=0,
            max_value=500,
            value=val_init,
            step=1,
            key=f"input_cons_{data_iso_sel}"
        )
    with col2:
        st.write("")
        st.write("")
        btn_salvar_consumo = st.button(texto_btn, type="primary", use_container_width=True)
        
    if btn_salvar_consumo:
        salvar_consumo_diario(data_iso_sel, consumo_input)
        st.success(f"Consumo de **{consumo_input} refeições** na data **{data_fmt_sel}** {tipo_acao} com sucesso! A base CSV foi atualizada.")
        st.rerun()
        
    st.divider()
    col_tit_h, col_btn_h = st.columns([3, 1])
    with col_tit_h:
        st.subheader("Últimos Registros Salvos no Histórico Operacional")
    with col_btn_h:
        df_completo_csv = carregar_historico_consumo().sort_values("data_iso", ascending=False)
        csv_bytes = df_completo_csv[["data", "data_iso", "consumo"]].to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            label="📥 Baixar Histórico em CSV",
            data=csv_bytes,
            file_name="historico_consumo_atualizado.csv",
            mime="text/csv",
            key="btn_down_hist_csv"
        )
        
    df_exibicao = df_completo_csv.head(15).copy()
    if "data_dt" in df_exibicao.columns:
        df_exibicao["dia_semana"] = df_exibicao["data_dt"].dt.dayofweek.map(DIAS_SEMANA_PT)
    else:
        df_exibicao["dia_semana"] = pd.to_datetime(df_exibicao["data_iso"]).dt.dayofweek.map(DIAS_SEMANA_PT)
    df_exibicao["consumo_int"] = df_exibicao["consumo"].astype(int)
    
    df_tabela_limpa = df_exibicao[["data", "dia_semana", "consumo_int"]].rename(columns={
        "data": "Data do Atendimento",
        "dia_semana": "Dia da Semana",
        "consumo_int": "Refeições Servidas (Catraca)"
    })
    st.dataframe(df_tabela_limpa, use_container_width=True, hide_index=True)

# -------------------------------------------------------------
# ABA 2: PLANEJAMENTO SEMANAL DA NUTRICIONISTA
# -------------------------------------------------------------
with aba2:
    st.subheader("📋 Programação de Cardápio e Estimativa da Nutricionista")
    st.write("Preencha o cardápio e a estimativa inicial para os próximos dias de atendimento. Esses dados alimentam a **Janela Curta ($t+1$)** e o **Modelo Híbrido**.")
    
    # Próximos 5 dias úteis sincronizados com a Janela Curta t+1
    dias_t1 = obter_proximos_dias_uteis(num_dias=5)
    df_plan_existente = carregar_planejamento_nutricionista()
    
    opcoes_proteina = ["Frango", "Bovina", "Suína", "Peixe", "Ovo / Vegetariano"]
    opcoes_preparo = ["Assado / Grelhado", "Ensopado / Molho", "Frito"]
    cardapios_padrao = [
        ("Filé de Frango Grelhado", 0, 0, 170),
        ("Carne Bovina ao Molho com Legumes", 1, 1, 175),
        ("Isca de Peixe Crocante", 3, 2, 160),
        ("Cubos Suínos Acebolados", 2, 0, 170),
        ("Feijoada Tradicional Escolar", 1, 1, 180)
    ]
    
    st.write("---")
    st.markdown("##### 🗓️ Dias da Próxima Janela de Preparo (t+1):")
    linhas_planejadas = []
    cols = st.columns(5)
    
    for i, dt in enumerate(dias_t1):
        data_iso = dt.strftime("%Y-%m-%d")
        data_fmt = dt.strftime("%d/%m/%Y")
        dia_nome = DIAS_SEMANA_PT[dt.weekday()]
        
        # Verifica se já há registro salvo previamente
        reg_salvo = df_plan_existente[df_plan_existente["data_iso"] == data_iso]
        if not reg_salvo.empty:
            prato_init = reg_salvo.iloc[0].get("prato_principal", cardapios_padrao[i % 5][0])
            prot_init = reg_salvo.iloc[0].get("proteina_tipo", "Frango").capitalize()
            idx_prot = opcoes_proteina.index(prot_init) if prot_init in opcoes_proteina else 0
            prep_init = reg_salvo.iloc[0].get("preparo_tipo", "Assado / Grelhado")
            idx_prep = opcoes_preparo.index(prep_init) if prep_init in opcoes_preparo else 0
            nutri_init = int(reg_salvo.iloc[0].get("planejado_nutri", cardapios_padrao[i % 5][3]))
        else:
            prato_init, idx_prot, idx_prep, nutri_init = cardapios_padrao[i % 5]
            
        with cols[i]:
            st.markdown(f"**{dia_nome}**  \n`{data_fmt}`")
            prato = st.text_input(f"Prato", value=prato_init, key=f"prato_t1_{i}")
            prot = st.selectbox(f"Proteína", opcoes_proteina, index=idx_prot, key=f"prot_t1_{i}")
            prep = st.selectbox(f"Preparo", opcoes_preparo, index=idx_prep, key=f"prep_t1_{i}")
            qtd_nutri = st.number_input(f"Estimativa Nutri (ref)", min_value=0, max_value=350, value=nutri_init, step=5, key=f"nutri_t1_{i}")
            
            linhas_planejadas.append({
                "data_dt": pd.to_datetime(dt),
                "data": data_fmt,
                "data_iso": data_iso,
                "dia_semana": dia_nome,
                "prato_principal": prato,
                "proteina_tipo": prot,
                "preparo_tipo": prep,
                "planejado_nutri": float(qtd_nutri)
            })
            
    st.write("")
    btn_salvar_planejamento = st.button("📋 Salvar Programação da Nutricionista", type="primary", use_container_width=True)
    if btn_salvar_planejamento:
        df_plan_salvar = pd.DataFrame(linhas_planejadas)
        salvar_planejamento_semanal(df_plan_salvar)
        # Limpa cache de predição para forçar recalculo com a nova estimativa
        if "df_pred_t1" in st.session_state:
            del st.session_state["df_pred_t1"]
        st.success("Programação e estimativas da nutricionista salvas com sucesso! Agora você pode gerar a previsão na Aba 3.")

# -------------------------------------------------------------
# ABA 3: PREVISÃO — JANELA CURTA (t+1: PREPARO NA COZINHA)
# -------------------------------------------------------------
with aba3:
    st.subheader("⏱️ Janela Curta (t+1) — Apoio ao Preparo Diário e Perecíveis")
    st.write("Horizonte operacional de **3 a 7 dias** (semana seguinte imediata). Foco no preparo diário na cozinha, carnes que descongelam 48h antes e hortifrúti.")
    
    with st.expander("🔧 Selecionar Dados e Configurar Cenário de Predição (t+1)", expanded=True):
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("**1. Fontes de Dados a Utilizar:**")
            usar_clima_t1 = st.checkbox("🌦️ Incluir Previsão Climática (Chuva & Temperatura via API Open-Meteo)", value=True, key="chk_clima_t1")
            usar_cardapio_t1 = st.checkbox("🍲 Incluir Cardápio e Proteínas (Cadastrado na Aba 2)", value=True, key="chk_card_t1")
            usar_nutri_t1 = st.checkbox("👩‍🍳 Incluir Estimativa Humana da Nutricionista (Modelo Híbrido)", value=True, key="chk_nutri_t1")
            
        with col_c2:
            st.markdown("**2. Parâmetros do Modelo e Margem:**")
            if usar_nutri_t1:
                peso_ia_t1 = st.slider("Ponderação IA vs. Nutricionista (α)", min_value=0.0, max_value=1.0, value=0.5, step=0.1,
                                       help="0.5 = 50% IA + 50% Nutri (Ponto ótimo comprovado no Capítulo 5 da pesquisa).", key="slider_peso_t1")
                st.caption(f"Composição: **{int(peso_ia_t1*100)}% Machine Learning** + **{int((1-peso_ia_t1)*100)}% Nutricionista**")
            else:
                peso_ia_t1 = 1.0
                st.info("Predição 100% Autônoma por Inteligência Artificial (sem intervenção humana).")
                
            tipo_margem_t1 = st.selectbox(
                "Margem de Segurança Operacional:",
                [
                    "Recomendada da Pesquisa",
                    "Moderada (+10 ref)",
                    "Prudencial (+19 ref)",
                    "Predição Pura (+0 ref)",
                    "Personalizada"
                ],
                index=0,
                key="sel_margem_t1"
            )
            margem_custom_t1 = 0
            if tipo_margem_t1 == "Personalizada":
                margem_custom_t1 = st.slider("Refeições de Margem Adicional:", 0, 30, 12, key="slider_margem_t1")
                
        btn_gerar_t1 = st.button("🚀 Calcular Previsão de Preparo (t+1)", type="primary", use_container_width=True, key="btn_calc_t1")

    if "df_pred_t1" not in st.session_state or btn_gerar_t1:
        with st.spinner("Processando cenário selecionado para a Janela Curta (t+1)..."):
            st.session_state["df_pred_t1"] = executar_pipeline_previsao(
                horizonte_alvo="Semana_t1",
                usar_clima=usar_clima_t1,
                usar_cardapio=usar_cardapio_t1,
                usar_nutri=usar_nutri_t1,
                peso_ia=peso_ia_t1 if usar_nutri_t1 else 1.0,
                tipo_margem=tipo_margem_t1,
                margem_adicional=margem_custom_t1
            )

    df_t1 = st.session_state["df_pred_t1"]
    
    # Cards de Resumo Operacional t+1
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total da Semana a Preparar", f"{int(df_t1['recomendacao_final'].sum())} ref")
    with c2:
        st.metric("Média Diária Recomendada", f"{int(df_t1['recomendacao_final'].mean())} ref/dia")
    with c3:
        st.metric("Média da IA Pura", f"{int(df_t1['ia_pura'].mean())} ref/dia")
    with c4:
        if usar_nutri_t1 and df_t1["estimativa_nutri"].notna().any():
            st.metric("Média da Nutricionista", f"{int(df_t1['estimativa_nutri'].dropna().mean())} ref/dia")
        else:
            st.metric("Margem Aplicada", f"+{int(df_t1['margem_aplicada'].iloc[0])} ref")

    st.write("---")
    
    # Grade de Apoio ao Preparo
    st.subheader("📋 Grade de Preparo Diário da Cozinha (t+1)")
    cols_t1 = [
        "data", "dia_semana", "prato_principal", "proteina_tipo",
        "chuva_mm", "temp_max_c", "estimativa_nutri", "ia_pura",
        "pred_base_combinada", "margem_aplicada", "recomendacao_final", "alertas"
    ]
    rename_t1 = {
        "data": "Data",
        "dia_semana": "Dia",
        "prato_principal": "Cardápio",
        "proteina_tipo": "Proteína",
        "chuva_mm": "Chuva (mm)",
        "temp_max_c": "Temp (°C)",
        "estimativa_nutri": "Nutri (ref)",
        "ia_pura": "IA Pura",
        "pred_base_combinada": "Híbrido Base",
        "margem_aplicada": "Margem (+)",
        "recomendacao_final": "Recomendação de Preparo",
        "alertas": "Alertas da Cozinha"
    }
    df_tabela_t1 = df_t1[cols_t1].rename(columns=rename_t1)
    st.dataframe(df_tabela_t1, use_container_width=True, hide_index=True)
    
    # Gráfico Comparativo Interativo
    st.subheader("📈 Curva de Demanda Prevista para a Semana de Preparo")
    vars_grafico_t1 = ["ia_pura", "recomendacao_final"]
    if usar_nutri_t1 and df_t1["estimativa_nutri"].notna().any():
        vars_grafico_t1.append("estimativa_nutri")
        
    df_melt_t1 = df_t1.melt(
        id_vars=["data", "dia_semana"],
        value_vars=vars_grafico_t1,
        var_name="Estratégia",
        value_name="Refeições"
    )
    mapa_legenda_t1 = {
        "ia_pura": "IA Pura (Sem Margem)",
        "recomendacao_final": "Recomendação Oficial de Preparo",
        "estimativa_nutri": "Planejado pela Nutricionista"
    }
    df_melt_t1["Estratégia"] = df_melt_t1["Estratégia"].map(mapa_legenda_t1)
    
    graf_t1 = alt.Chart(df_melt_t1).mark_line(point=True).encode(
        x=alt.X("dia_semana:N", title="Dia da Semana", sort=None),
        y=alt.Y("Refeições:Q", title="Volume de Refeições", scale=alt.Scale(zero=False)),
        color=alt.Color("Estratégia:N", title="Estratégia", scale=alt.Scale(range=["#006633", "#c8102e", "#2563eb"])),
        tooltip=["dia_semana", "Estratégia", "Refeições"]
    ).properties(height=320)
    st.altair_chart(graf_t1, use_container_width=True)
    
    # Alertas Operacionais de Cozinha
    st.subheader("⚠️ Alertas de Produção para a Cozinha")
    for _, row in df_t1.iterrows():
        if row["alertas"] != "Operação normal":
            st.warning(f"**{row['dia_semana']} ({row['data']})**: {row['alertas']} ➔ Preparar **{int(row['recomendacao_final'])} refeições**.")
            
    # Exportação
    csv_t1 = df_tabela_t1.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="📥 Exportar Ficha de Preparo Semanal (CSV/Excel)",
        data=csv_t1,
        file_name="programacao_preparo_t1.csv",
        mime="text/csv",
        key="btn_down_t1"
    )

# -------------------------------------------------------------
# ABA 4: PREVISÃO — JANELA LONGA (t+2: COMPRAS ANTECIPADAS)
# -------------------------------------------------------------
with aba4:
    st.subheader("📅 Janela Longa (t+2) — Apoio a Compras e Suprimentos de Secos")
    st.write("Horizonte operacional de **8 a 14 dias** (pós-semana seguinte). Foco em ordens de compra antecipadas de gêneros não perecíveis, estocáveis e comunicação com fornecedores.")
    
    with st.expander("🔧 Selecionar Dados e Configurar Cenário de Compras (t+2)", expanded=True):
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.markdown("**1. Fontes de Dados a Utilizar:**")
            usar_clima_t2 = st.checkbox("🌦️ Incluir Tendência Meteorológica de 14 dias (Open-Meteo)", value=True, key="chk_clima_t2")
            st.info("💡 Na Janela Longa, o modelo opera de forma autônoma com base em defasagens históricas, calendário e projeção climática, sem depender da estimativa diária humana.")
            
        with col_l2:
            st.markdown("**2. Política de Proteção de Estoque / Almoxarifado:**")
            tipo_margem_t2 = st.selectbox(
                "Política de Segurança para Compras de Secos:",
                [
                    "Prudencial (+19 ref - Conformal P85 - Recomendada para Compras)",
                    "Moderada (+10 ref - Conformal P75)",
                    "Predição Pura (+0 ref)",
                    "Personalizada"
                ],
                index=0,
                key="sel_margem_t2"
            )
            margem_custom_t2 = 0
            if "Personalizada" in tipo_margem_t2:
                margem_custom_t2 = st.slider("Refeições de Margem Adicional para Compras:", 0, 35, 19, key="slider_margem_t2")
                
        btn_gerar_t2 = st.button("📦 Calcular Projeção de Compras (t+2)", type="primary", use_container_width=True, key="btn_calc_t2")

    margem_param_t2 = "Prudencial (+19 ref)" if "Prudencial" in tipo_margem_t2 else ("Moderada (+10 ref)" if "Moderada" in tipo_margem_t2 else ("Predição Pura (+0 ref)" if "Pura" in tipo_margem_t2 else "Personalizada"))

    if "df_pred_t2" not in st.session_state or btn_gerar_t2:
        with st.spinner("Processando projeção antecipada de suprimentos para a Janela Longa (t+2)..."):
            st.session_state["df_pred_t2"] = executar_pipeline_previsao(
                horizonte_alvo="Pos_Semana_t2",
                usar_clima=usar_clima_t2,
                usar_cardapio=False,
                usar_nutri=False,
                tipo_margem=margem_param_t2,
                margem_adicional=margem_custom_t2
            )

    df_t2 = st.session_state["df_pred_t2"]
    
    # Cards de Resumo Operacional t+2
    cl1, cl2, cl3, cl4 = st.columns(4)
    with cl1:
        st.metric("Volume Semanal para Compras", f"{int(df_t2['recomendacao_final'].sum())} ref", help="Volume total provisionado para dimensionamento de pedidos de secos e estocáveis.")
    with cl2:
        st.metric("Média Diária Prevista", f"{int(df_t2['recomendacao_final'].mean())} ref/dia")
    with cl3:
        st.metric("Demanda Base (IA Pura)", f"{int(df_t2['ia_pura'].mean())} ref/dia")
    with cl4:
        st.metric("Margem de Segurança Adotada", f"+{int(df_t2['margem_aplicada'].iloc[0])} ref", delta="Proteção de Suprimento")

    st.write("---")
    
    # Grade de Programação de Compras
    st.subheader("📦 Programação Antecipada de Suprimentos (t+2)")
    cols_t2 = [
        "data", "dia_semana", "chuva_mm", "temp_max_c",
        "ia_pura", "margem_aplicada", "recomendacao_final", "alertas"
    ]
    rename_t2 = {
        "data": "Data",
        "dia_semana": "Dia",
        "chuva_mm": "Chuva Prevista (mm)",
        "temp_max_c": "Temp Máx (°C)",
        "ia_pura": "Demanda Base (IA)",
        "margem_aplicada": "Margem Estoque (+)",
        "recomendacao_final": "Provisionamento de Compras",
        "alertas": "Observações de Calendário"
    }
    df_tabela_t2 = df_t2[cols_t2].rename(columns=rename_t2)
    st.dataframe(df_tabela_t2, use_container_width=True, hide_index=True)
    
    # Gráfico de Demanda Projetada t+2
    st.subheader("📈 Curva de Demanda Projetada para Suprimentos (t+2)")
    df_melt_t2 = df_t2.melt(
        id_vars=["data", "dia_semana"],
        value_vars=["ia_pura", "recomendacao_final"],
        var_name="Estratégia",
        value_name="Refeições"
    )
    mapa_legenda_t2 = {
        "ia_pura": "Demanda Base Prevista (IA Pura)",
        "recomendacao_final": "Volume de Compra com Margem de Segurança"
    }
    df_melt_t2["Estratégia"] = df_melt_t2["Estratégia"].map(mapa_legenda_t2)
    
    graf_t2 = alt.Chart(df_melt_t2).mark_line(point=True).encode(
        x=alt.X("dia_semana:N", title="Dia da Semana", sort=None),
        y=alt.Y("Refeições:Q", title="Volume de Refeições", scale=alt.Scale(zero=False)),
        color=alt.Color("Estratégia:N", title="Estratégia", scale=alt.Scale(range=["#006633", "#c8102e"])),
        tooltip=["dia_semana", "Estratégia", "Refeições"]
    ).properties(height=320)
    st.altair_chart(graf_t2, use_container_width=True)
    
    # Orientações para a Gestão de Compras
    st.subheader("💡 Recomendações para Pedidos a Fornecedores")
    st.info("""
    - **Gêneros Secos e Grãos (Arroz, Feijão, Óleo, Farináceos):** Utilize o volume total acumulado da semana para emitir pedidos com antecedência mínima de 10 dias úteis.
    - **Proteção contra Rupturas:** A política de compras com Margem Prudencial P85 (+19 refeições/dia) garante que variações atípicas de comparecimento escolar não esgotem o estoque central da unidade.
    - **Reconciliação no horizonte t+1:** Ao entrar na semana imediatamente anterior ao preparo, consulte a **Aba 3 (Janela Curta)** para refinar o quantitativo fino dos itens perecíveis (carnes e hortifrúti).
    """)
    
    # Exportação de Compras
    csv_t2 = df_tabela_t2.to_csv(index=False).encode("utf-8-sig")
    st.download_button(
        label="📥 Exportar Programação de Compras (CSV/Excel)",
        data=csv_t2,
        file_name="programacao_compras_t2.csv",
        mime="text/csv",
        key="btn_down_t2"
    )

# -------------------------------------------------------------
# ABA 5: GUIA DE USO & PASSO A PASSO
# -------------------------------------------------------------
with aba5:
    st.subheader("📖 Guia do Usuário: Como Operar o Artefato no Dia a Dia")
    st.write("Este manual passo a passo foi elaborado para orientar a nutricionista e a equipe de gestão da cantina escolar no uso diário e semanal do sistema.")
    
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        st.markdown("""
        <div class="card-guia">
            <div class="passo-titulo"><span class="passo-numero">1</span> Registro Diário (Catraca)</div>
            <p>
                <b>Quando fazer:</b> Todos os dias úteis, ao encerrar o almoço (aprox. 14h00).<br>
                <b>O que fazer:</b> Na <b>Aba 1</b>, insira o número real de alunos atendidos na catraca e clique em <i>Salvar</i>.<br>
                <b>Por que é vital:</b> Os algoritmos supervisionados utilizam essas informações para atualizar imediatamente as defasagens (lags de 5 e 10 dias) e as médias móveis recentes.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-guia">
            <div class="passo-titulo"><span class="passo-numero">2</span> Programação Semanal de Cardápio</div>
            <p>
                <b>Quando fazer:</b> Toda quinta ou sexta-feira da semana anterior.<br>
                <b>O que fazer:</b> Na <b>Aba 2</b>, confira os pratos planejados, proteínas e a sua estimativa inicial (ex.: 170 refeições) e clique em <i>Salvar Programação</i>.<br>
                <b>Por que é vital:</b> A atratividade da proteína (ex.: feijoada/bovina atrai mais; peixe tem menor adesão) e a sua experiência humana entram diretamente no cálculo preditivo.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_g2:
        st.markdown("""
        <div class="card-guia">
            <div class="passo-titulo"><span class="passo-numero">3</span> Janela Curta (t+1: Preparo da Cozinha)</div>
            <p>
                <b>Quando fazer:</b> No início da semana de atendimento e com 48h de antecedência.<br>
                <b>O que fazer:</b> Na <b>Aba 3</b>, ative o <i>Modelo Híbrido</i> e a previsão do tempo. O sistema combinará <b>50% da sua estimativa + 50% do Machine Learning + Margem ótima (+12 ref)</b>.<br>
                <b>Objetivo:</b> Dimensionar carnes que precisam descongelar e hortifrúti, evitando desperdício de sobras e garantindo que nenhum aluno fique sem refeição.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card-guia">
            <div class="passo-titulo"><span class="passo-numero">4</span> Janela Longa (t+2: Compras de Secos)</div>
            <p>
                <b>Quando fazer:</b> A cada 10 a 14 dias úteis de antecedência.<br>
                <b>O que fazer:</b> Na <b>Aba 4</b>, consulte o volume semanal acumulado com <i>Margem Prudencial (+19 ref)</i>.<br>
                <b>Objetivo:</b> Emitir ordens de compra ao almoxarifado/fornecedores para gêneros secos e estocáveis (arroz, feijão, óleo, sal), com margem robusta que protege contra rupturas de estoque.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("📚 Glossário de Termos e Conceitos da Pesquisa")
    
    with st.expander("🔍 Entenda os Modelos e Métricas da Tela"):
        st.markdown("""
        * **IA Pura (Machine Learning):** Previsão matemática gerada pelos modelos regulares Lasso e Ridge combinados, considerando o histórico de consumo, dia da semana, previsão de chuva e tipo de carne. Não possui margem de segurança.
        * **Híbrido Base (IA + Nutricionista):** Média ponderada calculada como $(0.5 \\times \\text{IA}) + (0.5 \\times \\text{Nutricionista})$. Os experimentos da dissertação comprovaram que a combinação 50/50 reduz em até 44% os erros severos em comparação com o uso exclusivo da experiência humana ou da IA pura.
        * **Margem Residual Recomendada (+12 ref):** Margem estatística calibrada no percentil 85 dos resíduos do modelo híbrido. Ela eleva ligeiramente a produção para zerar o risco de faltas alimentares sem gerar sobras volumosas.
        * **Margem Prudencial (+19 ref):** Margem conformal P85 aplicada quando o modelo roda de forma puramente autônoma (especialmente para compras de suprimentos na Janela Longa $t+2$).
        * **Efeito Climático (API Open-Meteo):** Precipitações superiores a 15 mm causam retração comprovada no comparecimento de alunos no campus, acionando alertas amarelos para a equipe de cozinha não produzir excesso.
        * **Efeito Sexta-Feira:** Redução histórica média de ~28% no consumo devido à dinâmica pedagógica do contraturno escolar, devidamente compensada pelos algoritmos.
        """)
