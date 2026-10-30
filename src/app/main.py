"""
Interface Web Operacional do Artefato — Apoio à Decisão e Storytelling da Pesquisa
Pesquisa: Artefato Analítico-Preditivo para Planejamento da Produção de Refeições e Combate ao Desperdício
Autor: Michel Silva de Souza (Michel Digui)
Programa: Programa de Pós-Graduação em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)
Instituição: Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)
Campo de Aplicação Empírica: Restaurante Estudantil do IFSP Campus Itaquaquecetuba
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
    from pipeline import executar_pipeline_previsao, DIAS_SEMANA_PT, obter_proximos_dias_uteis, CENARIOS_DICT, MODELOS_RANKING, MARGENS_INFO
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
    from .pipeline import executar_pipeline_previsao, DIAS_SEMANA_PT, obter_proximos_dias_uteis, CENARIOS_DICT, MODELOS_RANKING, MARGENS_INFO

# Configuração da página
st.set_page_config(
    page_title="Artefato Preditivo de Refeições — CEETEPS & IFSP",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Adaptativa — Foco em Usabilidade, Alto Contraste e Leitura Confortável
st.markdown("""
<style>
    /* Topo Institucional Limpo e Elegante */
    .if-header-box {
        background: linear-gradient(135deg, #005a2b 0%, #004220 50%, #0f172a 100%) !important;
        border-radius: 12px;
        padding: 18px 24px;
        color: #ffffff !important;
        margin-bottom: 20px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-left: 6px solid #ef4444;
    }
    .if-badge-mestrado {
        background: #ef4444 !important;
        color: #ffffff !important;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
        white-space: nowrap;
        text-align: center;
    }

    /* Cards de Decisão Operacional em Destaque */
    .card-decisao-topo {
        background-color: rgba(16, 185, 129, 0.08);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-left: 5px solid #10b981;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 16px;
    }
    .card-alerta-topo {
        background-color: rgba(239, 68, 68, 0.08);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-left: 5px solid #ef4444;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 16px;
    }

    /* Estilização dos Métricas Padrão */
    div[data-testid="stMetric"] {
        background-color: rgba(128, 128, 128, 0.06) !important;
        border: 1px solid rgba(128, 128, 128, 0.2) !important;
        border-top: 4px solid #10b981 !important;
        border-radius: 10px !important;
        padding: 12px 14px !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04) !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 13px !important;
        font-weight: 600 !important;
        opacity: 0.9 !important;
    }
    div[data-testid="stMetricValue"] {
        color: #10b981 !important;
        font-weight: 800 !important;
        font-size: 22px !important;
    }
    div[data-testid="stMetricDelta"] {
        font-weight: 600 !important;
        font-size: 11.5px !important;
    }

    /* Botões Primários no Verde Oficial */
    button[kind="primary"],
    button[data-testid="baseButton-primary"],
    div.stButton > button {
        background-color: #008744 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 8px 20px !important;
        font-size: 14.5px !important;
        box-shadow: 0 2px 6px rgba(0, 135, 68, 0.25) !important;
    }
    button[kind="primary"]:hover,
    div.stButton > button:hover {
        background-color: #006633 !important;
    }

    /* Abas de Navegação */
    button[data-baseweb="tab"] {
        font-weight: 700 !important;
        font-size: 14px !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #10b981 !important;
        border-bottom: 3px solid #10b981 !important;
    }

    /* Cards de Storytelling */
    .card-story {
        background-color: rgba(128, 128, 128, 0.06);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-left: 5px solid #10b981;
        border-radius: 8px;
        padding: 16px 18px;
        margin-bottom: 14px;
    }
    .card-story-red {
        border-left-color: #ef4444;
    }
</style>
""", unsafe_allow_html=True)

# Topo Institucional
st.markdown("""
<div class="if-header-box">
    <div style="display: flex; align-items: center; gap: 16px; flex-wrap: wrap;">
        <div style="font-size: 32px;">🍽️</div>
        <div>
            <div style="font-size: 20px; font-weight: 800; color: #ffffff !important; line-height: 1.25; margin-bottom: 2px;">Restaurante Estudantil — Painel de Apoio à Decisão</div>
            <div style="font-size: 13px; color: #f1f5f9 !important; line-height: 1.4;">IFSP Campus Itaquaquecetuba & Centro Paula Souza (CEETEPS)</div>
            <div style="font-size: 11.5px; color: #e2e8f0 !important; opacity: 0.9;">Previsão de Demanda, Dimensionamento de Cardápio e Combate ao Desperdício de Alimentos</div>
        </div>
    </div>
    <div class="if-badge-mestrado">PPG-GTSP / CEETEPS</div>
</div>
""", unsafe_allow_html=True)

# Barra Lateral Executiva e Funcional
with st.sidebar:
    st.markdown("### 📋 Painel de Controle")
    st.caption("Ambiente Operacional do Restaurante Escolar")
    
    # Modo de Exibição
    modo_visao = st.radio(
        "Perfil de Visualização:",
        ["👩‍🍳 Visão Operacional (Nutrição & Gestão)", "🔬 Visão Avançada (Auditoria & Métricas)"],
        index=0,
        help="A Visão Operacional exibe recomendações diretas para a rotina diária. A Visão Avançada permite inspecionar hiperparâmetros, cenários de machine learning e matrizes de features."
    )
    is_avancado = "Avançada" in modo_visao

    st.divider()
    st.markdown("##### 📊 Status da Operação")
    
    df_consumo_hist = carregar_historico_consumo()
    if not df_consumo_hist.empty:
        ult_data = df_consumo_hist.iloc[-1]["data"]
        ult_cons = df_consumo_hist.iloc[-1]["consumo"]
        st.metric(label="Último Consumo Apurado (Catraca)", value=f"{int(ult_cons)} refeições", delta=f"Data: {ult_data}")
        st.metric(label="Histórico de Dias Monitorados", value=f"{len(df_consumo_hist)} datas letivas")
    
    st.caption("🌤️ **Meteorologia:** Conectado à API Open-Meteo em tempo real.")
    st.caption("🔒 **Segurança:** Dados sensíveis anonimizados e bases históricas 100% protegidas.")
    
    st.divider()
    
    # Informações Acadêmicas Organizadas em Expander (Sem Poluir a Barra)
    with st.expander("🎓 Ficha Técnica da Pesquisa (Mestrado)", expanded=False):
        st.markdown("""
        * **Pesquisador:** Michel Silva de Souza (*Michel Digui*)
        * **Programa:** Mestrado Profissional em Gestão e Tecnologia em Sistemas Produtivos (PPG-GTSP)
        * **Instituição:** Centro Estadual de Educação Tecnológica Paula Souza (CEETEPS)
        * **Campo Empírico:** IFSP Campus Itaquaquecetuba
        * **Abordagem Metodológica:** Design Science Research (DSR)
        * **Ano:** 2026
        """)

# Abas de Navegação Reorganizadas por Ordem de Uso Real
aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "🍽️ 1. Painel da Semana (Ordem de Preparo)",
    "🔮 2. Simulador Rápido ('E se...?')",
    "📦 3. Compras & Contratos (Próximos 14 dias)",
    "📝 4. Cadastrar / Atualizar Dados",
    "🔬 5. Auditoria Científica & Metodologia (DSR)",
    "📋 6. Guia Prático de Rotina"
])

# ==============================================================================
# ABA 1: PAINEL DA SEMANA (RECOMENDAÇÃO DIRETA PARA A COZINHA)
# ==============================================================================
with aba1:
    st.subheader("🍽️ Grade Semanal de Previsão e Quantidades de Preparo")
    st.write(
        "Este painel fornece à **Nutricionista Responsável Técnica e à Gestora do Restaurante** a "
        "quantidade exata de refeições a serem preparadas para cada dia da próxima semana útil, "
        "incorporando o histórico de consumo, o cardápio planejado e as condições do clima."
    )
    
    # Controles de Configuração (Modo Avançado vs Modo Padrão Ótimo)
    if is_avancado:
        with st.expander("⚙️ Configurações Avançadas de Modelagem (Ajuste Fino de Algoritmos)", expanded=True):
            col_c1, col_c2, col_c3 = st.columns(3)
            with col_c1:
                cenario_t1 = st.selectbox("Cenário de Features:", list(CENARIOS_DICT.keys()), index=0, key="cfg_cen_t1")
            with col_c2:
                modelo_t1 = st.selectbox("Algoritmo Ativo:", list(MODELOS_RANKING.keys()), index=0, key="cfg_mod_t1")
            with col_c3:
                margem_t1 = st.selectbox("Margem de Segurança Conformal:", list(MARGENS_INFO.keys()), index=0, key="cfg_mar_t1")
    else:
        # Configuração Campeã Auditada Fixa como Padrão Transparente
        cenario_t1 = "Cenário 1 (Histórico + Calendário + Cardápio + Clima)"
        modelo_t1 = "Híbrido 50/50 (Campeão Absoluto)"
        margem_t1 = "Conformal P85 (+18 ref / 84,9% Proteção) - Campeã Auditada"

    # Execução do pipeline de previsão
    df_t1, df_feat_t1 = executar_pipeline_previsao(
        horizonte_alvo="Semana_t1",
        cenario_escolhido=cenario_t1,
        modelo_escolhido=modelo_t1,
        tipo_margem=margem_t1
    )
    
    if not df_t1.empty:
        # Destaques Rápidos da Semana
        total_semana = int(df_t1["recomendacao_final"].sum())
        media_dia = int(df_t1["recomendacao_final"].mean())
        primeiro_dia = df_t1.iloc[0]
        
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Total Semanal Recomendado", f"{total_semana:,} refeições".replace(",", "."), delta="5 dias úteis")
        with m2:
            st.metric("Média de Preparo Diário", f"{media_dia} ref/dia", delta="Equilíbrio seguro")
        with m3:
            st.metric("Próximo Dia Útil", f"{int(primeiro_dia['recomendacao_final'])} refeições", delta=f"{primeiro_dia['dia_semana']} ({primeiro_dia['data']})")
        with m4:
            st.metric("Política de Segurança Ativa", "+12 a +18 ref", delta="Proteção estudantil > 85%")
            
        st.markdown("---")
        
        # Tabela Semanal Executiva e Amigável
        st.markdown("#### 📋 Tabela Operacional de Produção Diária")
        
        df_exibir = pd.DataFrame()
        df_exibir["Data"] = df_t1["data"]
        df_exibir["Dia da Semana"] = df_t1["dia_semana"]
        df_exibir["Prato Principal"] = df_t1["prato_principal"]
        df_exibir["Proteína"] = df_t1["proteina_tipo"].str.title()
        df_exibir["Previsão Base"] = df_t1["pred_base_combinada"].astype(int).astype(str) + " ref"
        df_exibir["Margem Segura"] = "+" + df_t1["margem_aplicada"].astype(int).astype(str) + " ref"
        df_exibir["👉 Ordem de Preparo (Final)"] = df_t1["recomendacao_final"].astype(int).astype(str) + " refeições"
        
        # Faixa de Atendimento Seguro (Min - Max)
        faixa_min = (df_t1["pred_base_combinada"] - 8).clip(lower=0).astype(int)
        faixa_max = (df_t1["recomendacao_final"] + 8).astype(int)
        df_exibir["Faixa Sugerida (Mín - Máx)"] = faixa_min.astype(str) + " a " + faixa_max.astype(str) + " ref"
        
        # Alertas Práticos
        def formatar_alertas(al_list):
            if isinstance(al_list, list) and al_list:
                return " | ".join(al_list)
            return "☀️ Operação regular"
            
        df_exibir["Alertas Operacionais"] = df_t1["alertas"].apply(formatar_alertas)
        
        st.dataframe(df_exibir, use_container_width=True, hide_index=True)
        
        # Botão de Exportação para Rotina da Cozinha
        col_exp1, col_exp2 = st.columns([1, 3])
        with col_exp1:
            csv_grade = df_exibir.to_csv(index=False, sep=";").encode("utf-8-sig")
            st.download_button(
                label="📥 Baixar Tabela em Planilha (CSV)",
                data=csv_grade,
                file_name=f"grade_preparo_refeicoes_{date.today().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
            
        st.markdown("---")
        
        # Gráfico Visual de Barras
        st.markdown("#### 📊 Visualização Gráfica do Planejamento da Semana")
        graf_dados = []
        for _, r in df_t1.iterrows():
            graf_dados.append({"Dia": f"{r['dia_semana'][:3]} ({r['data'][:5]})", "Valor": r["recomendacao_final"], "Tipo": "Recomendação Final com Margem"})
            graf_dados.append({"Dia": f"{r['dia_semana'][:3]} ({r['data'][:5]})", "Valor": r["pred_base_combinada"], "Tipo": "Previsão Central de Demanda"})
            if r["estimativa_nutri"] is not None:
                graf_dados.append({"Dia": f"{r['dia_semana'][:3]} ({r['data'][:5]})", "Valor": r["estimativa_nutri"], "Tipo": "Quantitativo Inicial Nutricionista"})
                
        df_g = pd.DataFrame(graf_dados)
        chart = alt.Chart(df_g).mark_bar().encode(
            x=alt.X("Tipo:N", title=None, axis=alt.Axis(labels=False, ticks=False)),
            y=alt.Y("Valor:Q", title="Quantidade de Refeições"),
            color=alt.Color("Tipo:N", scale=alt.Scale(domain=["Recomendação Final com Margem", "Previsão Central de Demanda", "Quantitativo Inicial Nutricionista"], range=["#10b981", "#38bdf8", "#f59e0b"]), legend=alt.Legend(title="Indicadores de Planejamento")),
            column=alt.Column("Dia:N", title="Dias da Semana de Produção")
        ).properties(height=280)
        st.altair_chart(chart, use_container_width=True)
        
        # Inspeção de Features no Modo Avançado
        if is_avancado:
            with st.expander("🔍 Inspecionar Matriz Completa de Features (Transparência Algorítmica)", expanded=False):
                st.write("Variáveis computadas e alimentadas nos estimadores de regressão:")
                st.dataframe(df_feat_t1, use_container_width=True)

# ==============================================================================
# ABA 2: SIMULADOR INTERATIVO ("E SE...?")
# ==============================================================================
with aba2:
    st.subheader("🔮 Simulador Rápido de Cardápio e Clima ('E se...?')")
    st.write(
        "Esta ferramenta permite à **Nutricionista e à Gestora do Restaurante simular cenários hipotéticos antes de definir a ordem de preparo**. "
        "Você pode testar o efeito de mudar o prato principal ou antecipar o impacto de chuvas fortes na presença dos estudantes."
    )
    
    col_sim1, col_sim2 = st.columns([1.2, 1])
    with col_sim1:
        st.markdown("##### ⚙️ Escolha o Cenário que Deseja Simular")
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
        
    # Mapeamento do cenário simulado
    precip_val = 0.0 if "0 mm" in clima_sim else (3.0 if "3 mm" in clima_sim else (10.0 if "10 mm" in clima_sim else 30.0))
    prot_tipo = "bovina" if "Bovina" in prot_sim else ("frango" if "Frango" in prot_sim else ("suina" if "Suína" in prot_sim else ("peixe" if "Peixe" in prot_sim else "ovo")))
    dia_num_map = {"Segunda-feira": 0, "Terça-feira": 1, "Quarta-feira": 2, "Quinta-feira": 3, "Sexta-feira": 4}
    dia_num = dia_num_map[dia_sim_nome]
    
    # Vetor de inferência rápida
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
    
    df_tr = pipeline.construir_dataset_treino()
    m_ridge, _, _, _, m_cat, c_feat = pipeline.treinar_modelos(df_tr)
    X_s = np.array([[vetor_sim[c] for c in c_feat]])
    
    pred_ia_s = float(m_ridge.predict(X_s)[0])
    margem_s = 12.0 if (usar_margem_sim and precip_val < 15.0) else 0.0
    pred_final_s = int(round(pred_ia_s + margem_s))
    
    with col_sim2:
        st.markdown("##### 📊 Recomendação do Modelo para o Cenário")
        st.metric(
            "Quantidade Sugerida de Refeições",
            f"{pred_final_s} refeições", 
            delta=f"{pred_final_s - 180:+d} ref vs média padrão (180 ref)"
        )
        
        st.markdown("---")
        st.markdown("**💡 Dicas e Alertas Práticos do Sistema:**")
        if dia_num == 4:
            st.warning("⚠️ **Efeito Sexta-feira:** Historicamente, cerca de 20% dos estudantes não comparecem na sexta-feira à tarde.")
        if prot_tipo == "peixe":
            st.info("🐟 **Efeito Peixe:** Menor atratividade histórica no restaurante (~25 refeições a menos que carne bovina).")
        elif prot_tipo == "bovina":
            st.success("🥩 **Efeito Carne Bovina:** Prato com maior índice de comparecimento no campus.")
            
        if precip_val >= 15.0:
            st.error("🚨 **Alerta de Tempestade / Enchente:** Risco alto de bloqueio de vias e falta nos ônibus. A margem aditiva foi **zerada** para prevenir sobras excessivas e descarte de comida.")
        elif precip_val >= 8.0:
            st.warning("🌧️ **Chuva Moderada:** Risco de evasão discente pontual.")
        else:
            st.write("☀️ **Clima Regular:** Demanda estável prevista.")

# ==============================================================================
# ABA 3: COMPRAS & CONTRATOS (JANELA LONGA t+2: 14 DIAS)
# ==============================================================================
with aba3:
    st.subheader("📦 Planejamento de Compras e Estoque — Janela Longa (10 a 14 dias)")
    st.write(
        "Utilizada pela **Gestora do Restaurante e pela Equipe de Compras** para dimensionar a aquisição "
        "de gêneros secos, alimentos de despensa e estimar o faturamento contratual da semana subsequente."
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
        st.markdown("#### 📋 Grade de Planejamento Quinzenal")
        
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
# ABA 4: CADASTRAR / ATUALIZAR DADOS (SIMPLES E DIRETO)
# ==============================================================================
with aba4:
    st.subheader("📝 Lançamento e Atualização de Informações do Refeitório")
    st.write(
        "Utilize este formulário simples para registrar o cardápio da próxima semana ou "
        "atualizar a contagem da catraca do dia anterior. As alterações são sincronizadas com segurança."
    )
    
    col_d1, col_d2 = st.columns([1, 2])
    with col_d1:
        data_sel = st.date_input("Selecione a Data:", value=date.today(), key="data_picker_aba4")
        
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
                "Consumo Real Verificado (Catraca)",
                min_value=0, max_value=500,
                value=int(dados_dia['consumo']) if dados_dia['consumo'] is not None else 0,
                step=1,
                help="Quantidade real de alunos que passaram na catraca."
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
        dict_salvar = {
            "consumo": novo_consumo if novo_consumo > 0 else None,
            "reservas": int(dados_dia['reservas']) if dados_dia['reservas'] is not None else None,
            "planejado_nutri": novo_planejado_nutri,
            "is_dia_letivo": is_letivo,
            "evento_tipo": "Letivo Regular" if is_letivo else "Sem Aula",
            "prato_principal": prato_nome,
            "proteina_tipo": proteina_sel,
            "preparo_tipo": dados_dia["preparo_tipo"] or "Grelhado",
            "precipitation_sum": chuva_val,
            "temperature_2m_max": temp_val,
            "observacao": "Registro operacional via interface web"
        }
        salvar_edicao_operacional_completa(data_iso, dict_salvar)
        st.success(f"✅ Informações do dia **{data_fmt}** atualizadas com sucesso!")
        st.rerun()

# ==============================================================================
# ABA 5: AUDITORIA CIENTÍFICA & METODOLOGIA (DSR)
# ==============================================================================
with aba5:
    st.subheader("🔬 Fundamentação Teórica, DSR e Galeria Científica da Pesquisa")
    st.write(
        "Esta seção documenta a pesquisa acadêmica de mestrado desenvolvida no **Centro Paula Souza (CEETEPS)**, "
        "estruturada no método **Design Science Research (DSR)** e auditada com corte temporal rigoroso."
    )
    
    col_hist1, col_hist2 = st.columns(2)
    with col_hist1:
        st.markdown("""
        <div class="card-story">
            <h4>1. O Problema Real: Assimetria e Descompasso</h4>
            <p>No Restaurante Estudantil do IFSP Itaquaquecetuba, o almoço é gratuito. Historicamente, dois regimes operaram com limitações:</p>
            <ul>
                <li><b>Reservas dos Alunos (2023–2025):</b> O preenchimento voluntário de formulários no SUAP entrou em descontinuidade. Em <b>63,8% dos dias</b> faltavam reservas (déficit potencial de 9.494 refeições; MAE de 27,10 ref/dia).</li>
                <li><b>Censo Institucional da Nutrição (2026):</b> Para evitar desabastecimento, adotou-se quantitativo fixo com folga preventiva, gerando sobreoferta de +1.898 refeições em 123 datas (MAE de 26,21 ref/dia).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_hist2:
        st.markdown("""
        <div class="card-story card-story-red">
            <h4>2. A Solução: Artefato Preditivo com IA Híbrida</h4>
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
            ("figura_30_confronto_diario_setembro_ia_vs_nutricionista.png", "Figura 30 — Confronto em setembro/2026: Catraca real vs IA vs Nutrição"),
            ("figura_31_balanco_sobras_faltas_politicas_setembro.png", "Figura 31 — Balanço de sobras e faltas acumuladas em setembro sob 3 políticas"),
            ("figura_32_validacao_semana_retorno_outubro_catraca_vs_ia_nutri.png", "Figura 32 — Validação cega na semana de retorno pós-recesso de outubro"),
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
    st.subheader("📋 Procedimento Operacional Padrão (POP) — Rotina em 3 Minutos")
    st.markdown("""
    Este guia orienta a **Nutricionista Responsável Técnica e a Gestora do Restaurante** no uso do artefato:
    
    ---
    
    #### 🗓️ Rotina Semanal
    
    1. **Toda Sexta-feira (Planejamento da Produção t+1):**
       - Acesse a **Aba 4 (Cadastrar / Atualizar)** e informe os pratos previstos para a próxima semana.
       - Acesse a **Aba 1 (Painel da Semana)**:
         - Confira o número recomendado em **'👉 Ordem de Preparo'** para cada dia.
         - Clique em **'📥 Baixar Tabela em Planilha'** e envie a grade para a equipe de cozinha e fornecedora terceirizada.
       
    2. **Diariamente (Registro Rápido após as 14h):**
       - Acesse a **Aba 4** e digite o número de estudantes que passaram pela catraca. Isso mantém o modelo calibrado com a realidade do campus.
       
    3. **Quinzenalmente (Planejamento de Compras de Secos t+2):**
       - Acesse a **Aba 3 (Compras & Contratos)** para visualizar a demanda estimada das próximas duas semanas e dimensionar pedidos de gêneros estocáveis.
       
    ---
    
    #### ⚠️ Como Agir em Dias Especiais
    
    * **Dias de Chuva Forte / Tempestade (Alerta no Painel):**
      O sistema reduz automaticamente a margem de segurança para evitar desperdício de refeições decorrente de faltas nos transportes públicos.
    * **Sextas-feiras:**
      O modelo já compensa a queda habitual de 20% no comparecimento à tarde.
    * **Cardápio com Carne Bovina:**
      O modelo ajusta a quantidade para cima para garantir que nenhum aluno fique sem refeição.
    """)
