"""
Interface Web Operacional do Artefato — Apoio à Decisão e Storytelling da Pesquisa
Pesquisa: Artefato Analítico-Preditivo para Planejamento da Produção de Refeições e Combate ao Desperdício
Autor: Michel Silva de Souza (Michel Digui)
Programa: Programa de Pós-Graduação em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)
Instituição: Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)
Área de Concentração: Sistemas Produtivos
Linha de Pesquisa: Linha 2 — Sistemas de Informação e Tecnologias Digitais
Campo de Aplicação Empírica: Restaurante Estudantil do IFSP Campus Itaquaquecetuba
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
        consultar_dados_completos_data,
        salvar_edicao_operacional_completa,
        listar_ultimas_edicoes,
        carregar_fato_diaria_completa,
        CSV_CONSUMO_ATUALIZADO
    )
    from .pipeline import executar_pipeline_previsao, DIAS_SEMANA_PT, obter_proximos_dias_uteis

# Configuração da página
st.set_page_config(
    page_title="Artefato Preditivo de Refeições — CEETEPS & IFSP",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Adaptativa com Alto Contraste para Tema Claro (Light) e Tema Escuro (Dark)
st.markdown("""
<style>
    /* Topo Institucional com Alto Contraste */
    .if-header-box {
        background: linear-gradient(135deg, #005a2b 0%, #004220 50%, #0f172a 100%) !important;
        border-radius: 12px;
        padding: 20px 24px;
        color: #ffffff !important;
        margin-bottom: 22px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-left: 6px solid #ef4444;
    }
    .if-badge-mestrado {
        background: #ef4444 !important;
        color: #ffffff !important;
        padding: 7px 16px;
        border-radius: 20px;
        font-size: 11.5px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
        white-space: nowrap;
        text-align: center;
    }

    /* Cards de Métricas Operacionais — Sem Forçar Cores Fixas que Quebram no Dark/Light */
    div[data-testid="stMetric"] {
        background-color: rgba(128, 128, 128, 0.07) !important;
        border: 1px solid rgba(128, 128, 128, 0.25) !important;
        border-top: 4px solid #10b981 !important;
        border-radius: 10px !important;
        padding: 12px 14px !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-top-color 0.2s ease !important;
    }
    div[data-testid="stMetric"]:hover {
        border-top-color: #ef4444 !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 14px rgba(0, 0, 0, 0.12) !important;
    }
    div[data-testid="stMetricLabel"] {
        color: inherit !important;
        opacity: 0.9 !important;
        font-size: 13.5px !important;
        font-weight: 600 !important;
        white-space: normal !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.25 !important;
    }
    div[data-testid="stMetricValue"] {
        color: #10b981 !important;
        font-weight: 800 !important;
        font-size: 21px !important;
        white-space: normal !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.2 !important;
        margin-top: 3px !important;
    }
    div[data-testid="stMetricDelta"] {
        font-weight: 600 !important;
        font-size: 12px !important;
        white-space: normal !important;
        word-break: break-word !important;
    }

    /* Botões Primários e Botões de Submissão no Verde Oficial */
    button[kind="primary"],
    button[data-testid="baseButton-primary"],
    button[data-testid="stBaseButton-primary"],
    div.stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #008744 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 10px 22px !important;
        font-size: 15px !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 2px 6px rgba(0, 135, 68, 0.3) !important;
    }
    button[kind="primary"]:hover,
    button[data-testid="baseButton-primary"]:hover,
    button[data-testid="stBaseButton-primary"]:hover,
    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: #006633 !important;
        box-shadow: 0 4px 14px rgba(0, 135, 68, 0.45) !important;
        transform: translateY(-1px);
    }

    /* Abas Superiores com Alto Contraste */
    button[data-baseweb="tab"] {
        font-weight: 700 !important;
        font-size: 14.5px !important;
        color: inherit !important;
        opacity: 0.75 !important;
    }
    button[data-baseweb="tab"]:hover {
        opacity: 1 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #10b981 !important;
        border-bottom: 3px solid #10b981 !important;
        opacity: 1 !important;
    }

    /* Caixas de Destaque e Storytelling Adaptativas */
    .card-story {
        background-color: rgba(128, 128, 128, 0.08) !important;
        border: 1px solid rgba(128, 128, 128, 0.25) !important;
        border-left: 5px solid #10b981 !important;
        border-radius: 8px !important;
        padding: 16px 20px !important;
        margin-bottom: 16px !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05) !important;
    }
    .card-story-red {
        border-left-color: #ef4444 !important;
    }
    .card-story h4 {
        color: #10b981 !important;
        margin-top: 0;
        margin-bottom: 8px;
        font-weight: 700;
    }
    .card-story-red h4 {
        color: #ef4444 !important;
    }
    .card-story p, .card-story li {
        color: inherit !important;
        font-size: 14px !important;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# Topo Institucional
st.markdown("""
<div class="if-header-box">
    <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
        <div style="font-size: 32px;">🍽️</div>
        <div>
            <div style="font-size: 20px; font-weight: 800; color: #ffffff !important; line-height: 1.25; margin-bottom: 3px;">Artefato Analítico-Preditivo de Refeições Escolares</div>
            <div style="font-size: 13px; color: #f1f5f9 !important; line-height: 1.4;">Centro Paula Souza (CEETEPS) — PPG em Gestão e Tecnologia em Sistemas Produtivos</div>
            <div style="font-size: 12px; color: #e2e8f0 !important; opacity: 0.9;">Aplicação Empírica: Restaurante Estudantil do IFSP Campus Itaquaquecetuba</div>
        </div>
    </div>
    <div class="if-badge-mestrado">CEETEPS / PPG-GTSP</div>
</div>
""", unsafe_allow_html=True)

# Barra Lateral Informativa
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 14px;">
        <div style="font-size: 34px;">🏭</div>
        <div style="font-weight: 800; color: #10b981; font-size: 16px; letter-spacing: -0.3px;">CEETEPS — Centro Paula Souza</div>
        <div style="font-size: 12px; font-weight: 600; opacity: 0.85;">PPG em Gestão e Tecnologia em Sistemas Produtivos</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    **Pesquisador:**  
    Michel Silva de Souza (*Michel Digui*)  
    
    **Mestrado Profissional:**  
    Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)  
    
    **Instituição Mantenedora:**  
    Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)  
    
    **Área de Concentração:**  
    Sistemas Produtivos  
    
    **Linha de Pesquisa:**  
    Sistemas de Informação e Tecnologias Digitais  
    
    **Campo de Estudo Aplicado:**  
    IFSP Campus Itaquaquecetuba  
    
    **Orientação Metodológica:**  
    Design Science Research (DSR)  
    """)
    st.divider()
    
    df_consumo_hist = carregar_historico_consumo()
    if not df_consumo_hist.empty:
        ult_data = df_consumo_hist.iloc[-1]["data"]
        ult_cons = df_consumo_hist.iloc[-1]["consumo"]
        st.metric(label="Último Consumo Real Registrado", value=f"{int(ult_cons)} ref", delta=f"Data: {ult_data}")
        st.metric(label="Total de Dias Cadastrados", value=f"{len(df_consumo_hist)} dias")
    
    st.divider()
    st.caption("🔒 **Garantia de Imutabilidade**: Os cadernos e bases da qualificação permanecem 100% seguros e inalterados.")

# Abas de Navegação
aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "📅 1. Cockpit Diário & Gestão por Data (Ver / Editar)",
    "⏱️ 2. Previsão Janela Curta (t+1: Preparo)",
    "📦 3. Previsão Janela Longa (t+2: Compras)",
    "📖 4. Storytelling Metodológico & Galeria (DSR)",
    "📋 5. Guia de Uso & Procedimentos"
])

# ==============================================================================
# ABA 1: COCKPIT DIÁRIO & GESTÃO UNIFICADA POR DATA
# ==============================================================================
with aba1:
    st.subheader("📅 Cockpit de Dados Operacionais por Data")
    st.write(
        "Selecione qualquer data para inspecionar e editar instantaneamente todos os registros daquele dia: "
        "**reservas, consumo da catraca, cardápio, condições meteorológicas e status do calendário acadêmico**. "
        "Novos lançamentos e correções são sincronizados sem alterar os cadernos históricos."
    )
    
    col_d1, col_d2 = st.columns([1, 2])
    with col_d1:
        data_sel = st.date_input("Selecione a Data para Consulta ou Lançamento", value=date.today(), key="data_picker_aba1")
        
    data_iso = data_sel.strftime("%Y-%m-%d")
    data_fmt = data_sel.strftime("%d/%m/%Y")
    
    dados_dia = consultar_dados_completos_data(data_iso)
    
    with col_d2:
        if dados_dia["encontrado_base"]:
            st.info(f"📌 **Registro Localizado na Base para {data_fmt} ({dados_dia['dia_semana']})** — Você pode revisar ou editar qualquer parâmetro abaixo.")
        else:
            st.success(f"✨ **Nova Data ({data_fmt} / {dados_dia['dia_semana']})** — Preencha os campos abaixo para cadastrar na base operacional.")
            
    # Cards de status do dia
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        val_c1 = f"{int(dados_dia['consumo'])} ref" if dados_dia['consumo'] is not None else "Não apurado"
        delta_c1 = "Catraca física" if dados_dia['consumo'] is not None else "Aguardando contagem"
        st.metric("Consumo Real", val_c1, delta=delta_c1)
    with c2:
        val_c2 = f"{int(dados_dia['reservas'])} ref" if dados_dia['reservas'] is not None else "Não cadastrado"
        delta_c2 = "Portal SUAP" if dados_dia['reservas'] is not None else "Sem reservas no SUAP"
        st.metric("Reservas Alunos", val_c2, delta=delta_c2)
    with c3:
        val_c3 = f"{int(dados_dia['planejado_nutri'])} ref" if dados_dia['planejado_nutri'] is not None else "Não informado"
        delta_c3 = "Meta nutricional" if dados_dia['planejado_nutri'] is not None else "Pendente nutricionista"
        st.metric("Quantitativo Nutri", val_c3, delta=delta_c3)
    with c4:
        val_c4 = f"{dados_dia['temperature_2m_max']:.1f} °C"
        delta_c4 = f"Chuva: {dados_dia['precipitation_sum']:.1f} mm"
        st.metric("Previsão do Clima", val_c4, delta=delta_c4)

    st.markdown("---")
    st.markdown("#### ✏️ Formulário de Edição e Lançamento de Dados")
    
    with st.form("form_edicao_data"):
        col_f1, col_f2 = st.columns(2)
        
        with col_f1:
            st.markdown("##### 👥 Frequência e Atendimento")
            novo_consumo = st.number_input(
                "Consumo Real Apurado (Catraca)",
                min_value=0, max_value=500,
                value=int(dados_dia['consumo']) if dados_dia['consumo'] is not None else 0,
                step=1,
                help="Quantidade de refeições efetivamente registradas na catraca/contagem física."
            )
            novas_reservas = st.number_input(
                "Reservas dos Estudantes (SUAP)",
                min_value=0, max_value=500,
                value=int(dados_dia['reservas']) if dados_dia['reservas'] is not None else 0,
                step=1,
                help="Quantidade de reservas preenchidas no sistema pelos estudantes."
            )
            novo_planejado_nutri = st.number_input(
                "Quantitativo Institucional da Nutricionista",
                min_value=0, max_value=500,
                value=int(dados_dia['planejado_nutri']) if dados_dia['planejado_nutri'] is not None else 180,
                step=1,
                help="Quantitativo planejado pela nutricionista responsável."
            )
            
            st.markdown("##### 🎓 Calendário Acadêmico")
            is_letivo = st.checkbox("Dia Letivo Regular com Aulas", value=dados_dia["is_dia_letivo"])
            tipo_evento = st.selectbox(
                "Status / Evento do Calendário",
                ["Letivo Regular", "Cancelamento de Aulas / Sem Aula", "Feriado / Recesso", "Greve", "Evento Pedagógico / Sábado Letivo"],
                index=0 if dados_dia["is_dia_letivo"] else 1
            )

        with col_f2:
            st.markdown("##### 🍲 Cardápio do Almoço")
            prato_nome = st.text_input("Nome do Prato Principal", value=dados_dia["prato_principal"] or "Iscas de Frango Grelhado")
            
            opcoes_proteina = ["Bovina", "Frango", "Suína", "Peixe", "Ovo / Vegetariana"]
            idx_prot = 1
            for i, p in enumerate(opcoes_proteina):
                if p.lower() in dados_dia["proteina_tipo"].lower():
                    idx_prot = i
                    break
            proteina_sel = st.selectbox("Tipo de Proteína Principal", opcoes_proteina, index=idx_prot)
            
            opcoes_preparo = ["Assado / Grelhado", "Ensopado / Com Molho", "Frito / Empanado", "Cozido Simples"]
            idx_prep = 0
            for i, prep in enumerate(opcoes_preparo):
                if prep.lower()[:5] in dados_dia["preparo_tipo"].lower():
                    idx_prep = i
                    break
            preparo_sel = st.selectbox("Técnica Culinária de Preparo", opcoes_preparo, index=idx_prep)
            
            st.markdown("##### 🌦️ Informações Meteorológicas (Open-Meteo)")
            col_w1, col_w2 = st.columns(2)
            with col_w1:
                chuva_val = st.number_input("Precipitação Prevista (mm)", min_value=0.0, max_value=150.0, value=float(dados_dia["precipitation_sum"]), step=0.5)
            with col_w2:
                temp_val = st.number_input("Temperatura Máxima (°C)", min_value=0.0, max_value=45.0, value=float(dados_dia["temperature_2m_max"]), step=0.5)

        obs_texto = st.text_input("Observações Operacionais (Opcional)", value=dados_dia["observacao"])
        
        btn_salvar_data = st.form_submit_button("💾 Salvar / Atualizar Informações Desta Data", type="primary", use_container_width=True)

    if btn_salvar_data:
        dict_salvar = {
            "consumo": novo_consumo if novo_consumo > 0 else None,
            "reservas": novas_reservas if novas_reservas > 0 else None,
            "planejado_nutri": novo_planejado_nutri,
            "is_dia_letivo": is_letivo and ("Sem Aula" not in tipo_evento and "Feriado" not in tipo_evento),
            "evento_tipo": tipo_evento,
            "prato_principal": prato_nome,
            "proteina_tipo": proteina_sel,
            "preparo_tipo": preparo_sel,
            "precipitation_sum": chuva_val,
            "temperature_2m_max": temp_val,
            "observacao": obs_texto
        }
        salvar_edicao_operacional_completa(data_iso, dict_salvar)
        st.success(f"✅ Dados da data **{data_fmt}** atualizados e salvos com sucesso no ecossistema operacional!")
        st.rerun()

    # Histórico de alterações recentes
    st.markdown("---")
    st.markdown("##### 🕒 Últimas Edições Operacionais Salvas")
    df_ult = listar_ultimas_edicoes(8)
    if not df_ult.empty:
        cols_view = [c for c in ["timestamp_edicao", "data", "consumo", "reservas", "planejado_nutri", "prato_principal", "proteina_tipo", "is_dia_letivo"] if c in df_ult.columns]
        st.dataframe(df_ult[cols_view], use_container_width=True)
    else:
        st.caption("Nenhuma edição operacional recente registrada até o momento.")

# ==============================================================================
# ABA 2: PREVISÃO JANELA CURTA (t+1: PREPARO E HORTIFRÚTI)
# ==============================================================================
with aba2:
    st.subheader("⏱️ Previsão Operacional — Janela Curta (t+1: Próxima Semana)")
    st.write(
        "Utilizada na **sexta-feira anterior** para emissão de ordens de produção e compras de hortifrúti. "
        "Apresenta como **padrão recomendado os modelos campeões da pesquisa**: "
        "**Modelo Híbrido 50/50** (IA Ridge + Nutricionista, MAE 20,20) e **Margem Conformal P85 (+18 ref)**."
    )
    
    with st.expander("⚙️ Painel de Configuração e Ajuste Fino dos Modelos", expanded=False):
        c_conf1, c_conf2, c_conf3 = st.columns(3)
        with c_conf1:
            modelo_t1 = st.selectbox(
                "Modelo Base de Machine Learning",
                ["Híbrido 50/50 (Campeão Auditado)", "Ridge Regression (Linear L2)", "Lasso Regression (L1)", "Regressão Linear"],
                index=0
            )
            usar_nutri_t1 = st.checkbox("Combinar com Quantitativo da Nutricionista (Híbrido)", value=True)
        with c_conf2:
            usar_clima_t1 = st.checkbox("Considerar Previsão do Clima (Open-Meteo)", value=True)
            usar_cardapio_t1 = st.checkbox("Considerar Atratividade do Cardápio", value=True)
        with c_conf3:
            tipo_margem_t1 = st.selectbox(
                "Política de Margem de Segurança Decisória",
                [
                    "Conformal P85 (+18 ref / Padrão Pesquisa)",
                    "Conformal P75 (+10 ref / Moderada)",
                    "Conformal P90 (+29 ref / Máxima Proteção)",
                    "Predição Pura (+0 ref)"
                ],
                index=0
            )

    df_t1, df_feat_t1 = executar_pipeline_previsao(
        horizonte_alvo="Semana_t1",
        usar_clima=usar_clima_t1,
        usar_cardapio=usar_cardapio_t1,
        usar_nutri=usar_nutri_t1,
        modelo_escolhido=modelo_t1,
        tipo_margem=tipo_margem_t1
    )
    
    st.markdown("#### 📊 Grade de Previsão Semanal para a Produção ($t+1$)")
    cols_apres = ["data", "dia_semana", "prato_principal", "proteina_tipo", "chuva_mm", "temp_max_c", "estimativa_nutri", "ia_pura", "pred_base_combinada", "margem_aplicada", "recomendacao_final", "alertas"]
    st.dataframe(df_t1[cols_apres], use_container_width=True)
    
    # Gráfico de barras comparativo
    graf_data = []
    for _, r in df_t1.iterrows():
        graf_data.append({"Dia": f"{r['dia_semana'][:3]} ({r['data'][:5]})", "Valor": r["recomendacao_final"], "Série": "Recomendação com Margem"})
        graf_data.append({"Dia": f"{r['dia_semana'][:3]} ({r['data'][:5]})", "Valor": r["pred_base_combinada"], "Série": "Previsão Central (Base)"})
        if r["estimativa_nutri"] is not None:
            graf_data.append({"Dia": f"{r['dia_semana'][:3]} ({r['data'][:5]})", "Valor": r["estimativa_nutri"], "Série": "Nutricionista Institucional"})
            
    df_graf = pd.DataFrame(graf_data)
    chart_t1 = alt.Chart(df_graf).mark_bar().encode(
        x=alt.X("Série:N", title=None),
        y=alt.Y("Valor:Q", title="Refeições"),
        color=alt.Color("Série:N", scale=alt.Scale(domain=["Recomendação com Margem", "Previsão Central (Base)", "Nutricionista Institucional"], range=["#10b981", "#38bdf8", "#ef4444"])),
        column=alt.Column("Dia:N", title="Dias Úteis da Semana t+1")
    ).properties(height=320)
    st.altair_chart(chart_t1)
    
    # Exibição das Features Geradas
    with st.expander("🔍 Inspecionar Matriz de Features Geradas para Inferência (Transparência Algorítmica)", expanded=False):
        st.write("Abaixo estão os valores exatos das variáveis calculadas e alimentadas no modelo para cada dia útil:")
        st.dataframe(df_feat_t1, use_container_width=True)

# ==============================================================================
# ABA 3: PREVISÃO JANELA LONGA (t+2: COMPRAS E CONTRATOS)
# ==============================================================================
with aba3:
    st.subheader("📦 Previsão Operacional — Janela Longa (t+2: Semana Subsequente)")
    st.write(
        "Utilizada para **planejamento de contratos e compras de gêneros secos/estocáveis** com 10 a 14 dias de antecedência. "
        "Nesse horizonte, ainda não há cardápio detalhado nem quantitativo da nutricionista; a previsão opera de forma **autônoma** "
        "ancorada no calendário escolar, inércia de consumo e na previsão climática estendida do **Open-Meteo** (MAE 27,79 no modelo campeão)."
    )
    
    df_t2, df_feat_t2 = executar_pipeline_previsao(
        horizonte_alvo="Pos_Semana_t2",
        usar_clima=True,
        usar_cardapio=False,
        usar_nutri=False,
        modelo_escolhido="Ridge Regression (Linear L2)",
        tipo_margem="Conformal P85 (+18 ref / Padrão Pesquisa)"
    )
    
    c_tot1, c_tot2, c_tot3 = st.columns(3)
    total_semana = int(df_t2["recomendacao_final"].sum())
    media_dia = int(df_t2["recomendacao_final"].mean())
    with c_tot1:
        st.metric("Total Semanal Estimado", f"{total_semana:,} ref".replace(",", "."))
    with c_tot2:
        st.metric("Média Diária Prevista", f"{media_dia} ref/dia")
    with c_tot3:
        st.metric("Horizonte de Antecedência", "10 a 14 dias", delta="Compras de Secos")
        
    st.markdown("#### 📋 Grade de Planejamento de Compras ($t+2$)")
    st.dataframe(df_t2[["data", "dia_semana", "chuva_mm", "temp_max_c", "ia_pura", "margem_aplicada", "recomendacao_final", "alertas"]], use_container_width=True)
    
    with st.expander("🔍 Inspecionar Features da Janela Longa (t+2)", expanded=False):
        st.dataframe(df_feat_t2, use_container_width=True)

# ==============================================================================
# ABA 4: STORYTELLING METODOLÓGICO & GALERIA CIENTÍFICA (DSR)
# ==============================================================================
with aba4:
    st.subheader("📖 Storytelling Metodológico e Galeria Científica da Pesquisa")
    st.write(
        "Esta seção narra a trajetória científica completa do desenvolvimento do artefato, fundamentada na metodologia "
        "**Design Science Research (DSR)** (Peffers et al., 2007), apresentando o problema real, os dados auditados e a galeria visual em 300 DPI."
    )
    
    col_hist1, col_hist2 = st.columns(2)
    with col_hist1:
        st.markdown("""
        <div class="card-story">
            <h4>1. O Problema Real: Assimetria e Desperdício</h4>
            <p>No IFSP Campus Itaquaquecetuba, o almoço estudantil é gratuito. Historicamente, dois mecanismos foram utilizados:</p>
            <ul>
                <li><b>Reservas dos Alunos (2023–2025):</b> O preenchimento voluntário de formulários no SUAP entrou em descontinuidade funcional. Em <b>63,8% dos dias letivos</b> faltavam reservas, acumulando 9.494 refeições em déficit potencial e MAE de 27,10 ref/dia.</li>
                <li><b>Censo da Nutricionista (2026):</b> Para evitar desabastecimento, adotou-se quantitativo institucional empírico fixo, gerando sobreoferta sistemática (+1.898 refeições de saldo e MAE de 26,21 ref/dia).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_hist2:
        st.markdown("""
        <div class="card-story card-story-red">
            <h4>2. A Solução: Artefato Preditivo com IA Híbrida</h4>
            <p>O artefato proposto introduz três inovações integradas:</p>
            <ul>
                <li><b>Duas Janelas Temporais:</b> Suporte em t+2 (compras com 14 dias via Open-Meteo) e t+1 (re-forecast na sexta-feira).</li>
                <li><b>Modelo Híbrido 50/50:</b> Combinação linear ponderada que alcança o menor erro da pesquisa (<b>MAE 20,20 ref/dia</b>).</li>
                <li><b>Conformal Prediction:</b> Margem não-paramétrica calibrada (P85 com +18 ref) garantindo <b>84,9% de índice de proteção estudantil</b> contra desabastecimento.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Galeria de Figuras da Dissertação
    st.markdown("---")
    st.markdown("### 🖼️ Galeria Visual da Dissertação (Figuras Oficiais em 300 DPI)")
    
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
            ("figura_15_correlacao_atributos_consumo_pearson.png", "Figura 15 — Correlação linear de Pearson calculada dinamicamente na base Gold (N=568)")
        ],
        "Etapa 4: Efeito Compensatório e Confronto de Regimes": [
            ("figura_16_decomposicao_efeito_compensatorio.png", "Figura 16 — Decomposição do efeito compensatório (saldo líquido vs desvios diários)"),
            ("figura_17_painel_anual_sobras_faltas.png", "Figura 17 — Painel anual de sobras e déficits potenciais nas reservas discentes")
        ],
        "Etapa 5: Torneio Walk-Forward e Modelagem Preditiva (2026)": [
            ("figura_18_melhor_mae_por_cenario_horizonte.png", "Figura 18 — Melhor MAE obtido por cenário e horizonte de decisão (N=73)"),
            ("figura_19_comparacao_regressao_linear_t2_clima.png", "Figura 19 — Impacto preditivo da meteorologia Open-Meteo no horizonte t+2"),
            ("figura_20_comparacao_horizontes_5_algoritmos.png", "Figura 20 — Comparação de desempenho dos 5 principais algoritmos em t+1 e t+2"),
            ("figura_21_ranking_modelos.png", "Figura 21 — Ranking geral dos modelos preditivos vs benchmark humano da nutricionista")
        ],
        "Etapa 6: Modelo Híbrido, Margens Conformal e Monte Carlo": [
            ("figura_22_sobras_faltas_politicas.png", "Figura 22 — Balanço de sobras e déficits potenciais sob diferentes políticas"),
            ("figura_23_fronteira_equilibrio_modelo_hibrido.png", "Figura 23 — Fronteira de equilíbrio do modelo híbrido em função de alpha"),
            ("figura_24_distribuicao_erros_diarios.png", "Figura 24 — Distribuição estimada dos erros diários (KDE: Nutri vs IA vs Híbrido)"),
            ("figura_25_margens_seguranca_conformal.png", "Figura 25 — Efeito das margens de segurança Conformal Prediction"),
            ("figura_26_simulacao_faixas_risco_monte_carlo.png", "Figura 26 — Simulação de faixas de incerteza estocástica de Monte Carlo (P10 a P95)"),
            ("figura_27_tradeoff_custo_atendimento.png", "Figura 27 — Trade-off entre custo financeiro de desperdício e taxa de atendimento"),
            ("figura_28_comparacao_historica_consolidada.png", "Figura 28 — Confronto histórico consolidado dos regimes operacionais com o artefato")
        ]
    }
    
    categoria_sel = st.selectbox("Selecione o Bloco Temático da Pesquisa", list(categorias_fig.keys()))
    
    for arq, tit in categorias_fig[categoria_sel]:
        caminho_img = os.path.join(pasta_figuras, arq)
        if os.path.exists(caminho_img):
            st.markdown(f"##### {tit}")
            st.image(caminho_img, caption=tit, use_container_width=True)
            st.write("")
        else:
            st.warning(f"Arquivo não localizado na pasta ativa: {arq}")

    # Quadro de Autoria e Ficha Técnica
    st.markdown("---")
    st.markdown("### 🎓 Ficha Técnica e Autoria do Projeto")
    st.markdown("""
    * **Pesquisador e Desenvolvedor do Artefato:** Michel Silva de Souza (*Michel Digui*)
    * **Programa de Pós-Graduação:** Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)
    * **Modalidade:** Mestrado Profissional
    * **Instituição Mantenedora:** Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)
    * **Área de Concentração:** Sistemas Produtivos
    * **Linha de Pesquisa:** Linha 2 — Sistemas de Informação e Tecnologias Digitais
    * **Campo de Aplicação Empírica:** Restaurante Estudantil do IFSP Campus Itaquaquecetuba
    * **Abordagem Metodológica:** Design Science Research (DSR)
    * **Repositório Oficial:** [github.com/micheldigui/Artefato_Mestrado_Michel](https://github.com/micheldigui/Artefato_Mestrado_Michel)
    * **Ano de Qualificação:** 2026
    """)

# ==============================================================================
# ABA 5: GUIA OPERACIONAL & PROCEDIMENTOS
# ==============================================================================
with aba5:
    st.subheader("📋 Guia de Uso e Procedimentos Operacionais")
    st.markdown("""
    #### Rotina Operacional Recomendada para a Gestão do Refeitório
    
    1. **Diariamente (após as 14h):**
       - Acessar a **Aba 1 (Cockpit Diário)**.
       - Conferir a contagem da catraca e salvar o número de refeições servidas.
       - Caso haja cancelamento de aulas ou eventos climáticos severos, registrar o status no calendário.
       
    2. **Toda Sexta-feira (Janela Curta — t+1 para a Próxima Semana):**
       - Na **Aba 1**, cadastrar a grade de cardápio da próxima semana (prato, proteína e preparo) e o quantitativo planejado pela nutricionista.
       - Acessar a **Aba 2 (Previsão Janela Curta t+1)**.
       - Emitir a recomendação do **Modelo Híbrido 50/50 com Margem Conformal P85**.
       - Enviar a grade consolidada para a empresa terceirizada para compra de perecíveis e hortifrúti.
       
    3. **Quinzenalmente (Janela Longa — t+2 para Compras de Secos):**
       - Acessar a **Aba 3 (Previsão Janela Longa t+2)**.
       - Exportar o volume estimado semanal com antecedência de 14 dias para guiar pedidos de contratos e gêneros de despensa.
    """)
