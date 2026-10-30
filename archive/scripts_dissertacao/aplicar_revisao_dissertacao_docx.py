"""
Script completo e auditado de aplicacao das melhorias da dissertacao de mestrado.
Arquivo alvo: f:\\PROJETOS\\ARTEFATO\\dissertacao\\Dissertacao_Michel_qualificacao_antigravity.docx
"""

import os
import re
import zipfile
import shutil
import tempfile
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

DOCX_PATH = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
FIGURAS_DIR = r"f:\PROJETOS\ARTEFATO\dissertacao\figuras"
TABELAS_DIR = r"f:\PROJETOS\ARTEFATO\dissertacao\tabelas"

RED_COLOR = RGBColor(200, 0, 0)

# Mapeamento oficial das 28 imagens
IMAGENS_MAP = {
    "image1.png": "figura_01_aplicacao_dsr_pesquisa.png",
    "image2.png": "figura_02_sintese_metodologica.png",
    "image3.png": "figura_03_pipeline_dados_camadas.png",
    "image4.png": "figura_04_protocolo_modelagem_validacao.png",
    "image5.png": "figura_05_arquitetura_sistemica_artefato.png",
    "image6.png": "figura_06_fluxo_operacional_artefato.png",
    "image7.png": "figura_07_perfil_semanal_consumo.png",
    "image8.png": "figura_08_perfil_semanal_por_ano_letivo.png",
    "image9.png": "figura_09_oferta_consumo_por_proteina.png",
    "image10.png": "figura_10_consumo_conforme_tecnica_preparo.png",
    "image11.png": "figura_11_consumo_por_faixa_precipitacao.png",
    "image12.png": "figura_12_relacao_temperatura_maxima_consumo.png",
    "image13.png": "figura_13_funcoes_autocorrelacao_temporal.png",
    "image14.png": "figura_14_ranking_importancia_atributos_rf.png",
    "image15.png": "figura_15_correlacao_atributos_consumo_pearson.png",
    "image16.png": "figura_16_melhor_mae_por_cenario_horizonte.png",
    "image17.png": "figura_17_comparacao_regressao_linear_t2_clima.png",
    "image18.png": "figura_18_mae_xgboost_cenario_base_horizonte.png",
    "image19.png": "figura_19_comparacao_modelos_vs_nutricionista_t1.png",
    "image20.png": "figura_20_sobra_deficit_potenciais_politicas_n83.png",
    "image21.png": "figura_21_fronteira_equilibrio_modelo_hibrido.png",
    "image22.png": "figura_22_efeito_margens_seguranca_conformal.png",
    "image23.png": "figura_23_simulacao_faixas_risco_monte_carlo.png",
    "image24.png": "figura_24_decomposicao_efeito_compensatorio.png",
    "image25.png": "figura_25_painel_anual_sobras_faltas_acumuladas.png",
    "image26.png": "figura_26_distribuicao_erros_diarios_por_regime.png",
    "image27.png": "figura_27_comparativo_custo_sobras_taxa_atendimento.png",
    "image28.png": "figura_28_comparacao_historica_consolidada_periodos_modelos.png",
}

# Titulos curtos padronizados (uma linha) das 28 figuras
TITULOS_FIGURAS = {
    1: "Figura 1 - Aplicação da Design Science Research na pesquisa",
    2: "Figura 2 - Síntese metodológica da pesquisa",
    3: "Figura 3 - Pipeline de dados em camadas",
    4: "Figura 4 - Protocolo de modelagem temporal",
    5: "Figura 5 - Arquitetura sistêmica do artefato",
    6: "Figura 6 - Fluxo operacional do artefato",
    7: "Figura 7 - Perfil semanal de consumo médio",
    8: "Figura 8 - Perfil semanal por ano letivo",
    9: "Figura 9 - Consumo por grupo proteico",
    10: "Figura 10 - Consumo por técnica de preparo",
    11: "Figura 11 - Consumo por faixa de chuva",
    12: "Figura 12 - Temperatura máxima e consumo",
    13: "Figura 13 - Autocorrelação temporal (ACF)",
    14: "Figura 14 - Importância dos atributos (Random Forest)",
    15: "Figura 15 - Correlação dos atributos com consumo",
    16: "Figura 16 - MAE por cenário e horizonte",
    17: "Figura 17 - Impacto do clima no Ridge (t+2)",
    18: "Figura 18 - Ganho do reforecast (t+2 para t+1)",
    19: "Figura 19 - Modelos preditivos vs Nutricionista",
    20: "Figura 20 - Sobras e faltas por política",
    21: "Figura 21 - Fronteira de Pareto (Modelo Híbrido)",
    22: "Figura 22 - Efeito das margens conformal",
    23: "Figura 23 - Simulação Monte Carlo e faixas de risco",
    24: "Figura 24 - Decomposição do efeito compensatório",
    25: "Figura 25 - Sobras e faltas anuais (2023-2025)",
    26: "Figura 26 - Distribuição dos erros nos regimes",
    27: "Figura 27 - Custo de sobras vs Atendimento",
    28: "Figura 28 - Comparativo histórico dos regimes",
}

def etapa_1_substituir_imagens_no_zip():
    print("\n--- ETAPA 1: Substituicao das 28 imagens no pacote DOCX ---")
    temp_dir = tempfile.mkdtemp()
    temp_zip = os.path.join(temp_dir, "doc.zip")
    shutil.copy2(DOCX_PATH, temp_zip)
    
    extract_dir = os.path.join(temp_dir, "extracted")
    with zipfile.ZipFile(temp_zip, 'r') as zf:
        zf.extractall(extract_dir)
        
    media_dir = os.path.join(extract_dir, "word", "media")
    substituidas = 0
    for img_target, fig_src in IMAGENS_MAP.items():
        src_path = os.path.join(FIGURAS_DIR, fig_src)
        dst_path = os.path.join(media_dir, img_target)
        if os.path.exists(src_path) and os.path.exists(dst_path):
            shutil.copy2(src_path, dst_path)
            substituidas += 1
            print(f"  [OK] {img_target} <- {fig_src}")
        else:
            print(f"  [AVISO] Nao encontrado: src={src_path} dst={dst_path}")
            
    print(f"Total de imagens substituidas no zip: {substituidas}/28")
    
    # Recompactar
    output_docx = os.path.join(temp_dir, "repacked.docx")
    with zipfile.ZipFile(output_docx, 'w', zipfile.ZIP_DEFLATED) as zf_out:
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, extract_dir)
                zf_out.write(full_path, rel_path)
                
    shutil.copy2(output_docx, DOCX_PATH)
    shutil.rmtree(temp_dir)
    print("Pacote DOCX atualizado com imagens de 300 DPI com sucesso!")

def etapa_2_atualizar_conteudo_docx():
    print("\n--- ETAPA 2: Atualizacao textual, metodologica e financeira no DOCX ---")
    doc = docx.Document(DOCX_PATH)
    
    # 1. Atualizar Titulos das Figuras (paragrafo anterior a cada grafico)
    print("Atualizando titulos das figuras para titulos curtos em 1 linha...")
    fig_count = 0
    for p_idx, p in enumerate(doc.paragraphs):
        for r in p.runs:
            blips = r._element.xpath('.//a:blip/@r:embed')
            if blips:
                fig_count += 1
                if fig_count in TITULOS_FIGURAS:
                    prev_p = doc.paragraphs[p_idx - 1]
                    novo_titulo = TITULOS_FIGURAS[fig_count]
                    if prev_p.text.strip() != novo_titulo:
                        print(f"  Fig {fig_count:02d}: '{prev_p.text.strip()}' -> '{novo_titulo}'")
                        prev_p.text = ""
                        run = prev_p.add_run(novo_titulo)
                        run.font.color.rgb = RED_COLOR
                        run.bold = True
                        prev_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # 2. Resumo Expandido (P0137)
    print("Atualizando Resumo Expandido (415 palavras)...")
    resumo_texto = (
        "O planejamento da produção de refeições em restaurantes institucionais e escolares lida diariamente "
        "com a incerteza da demanda, sob severa assimetria de consequências: superestimativas acarretam desperdício "
        "de alimentos perecíveis e recursos públicos, enquanto subestimativas provocam déficit de atendimento e "
        "vulnerabilidade nutricional estudantil. Esta pesquisa desenvolve e avalia um artefato analítico-preditivo "
        "voltado a apoiar as decisões de compra de suprimentos e produção diária em uma Unidade de Alimentação e "
        "Nutrição (UAN) escolar. Conduzido sob o método da Design Science Research (DSR), o estudo estrutura uma "
        "arquitetura em camadas de dados (Medallion: Bronze, Silver e Gold), integrando registros de atendimento da "
        "catraca, reservas voluntárias, cardápios categorizados por processamento de texto e dados meteorológicos "
        "da API Open-Meteo. A avaliação experimental adotou validação temporal sequencial (Walk-Forward Validation) "
        "ao longo de 28 semanas letivas de 2026 (fevereiro a agosto), simulando fielmente a tomada de decisão às sextas-feiras "
        "sem vazamento de dados futuros. O diagnóstico histórico de 2023 a 2025 revelou a falência funcional do modelo "
        "de reservas voluntárias dos discentes, com subnotificação crônica em 63,8% dos dias letivos (déficit acumulado "
        "de 9.494 refeições). Em 2026, a assunção do planejamento institucional pela nutricionista conteve o desabastecimento, "
        "mas gerou superestimativa preventiva contínua (3.354 refeições em sobras potenciais no período). No horizonte de "
        "preparo (t+1), os modelos lineares regularizados superaram o planejamento humano isolado: o Lasso atingiu Erro "
        "Absoluto Médio (MAE) de 22,27 refeições/dia (R² = 0,498) e o Ridge MAE de 22,46 (R² = 0,483), ante 24,92 da nutricionista "
        "isolada (R² = 0,373), reduzindo as sobras potenciais em 28,3%. Para equilibrar o custo operacional da sobra e a garantia "
        "social do atendimento, formulou-se a Fronteira Eficiente de Pareto do Modelo Híbrido ponderado: a combinação colaborativa "
        "de 50% Machine Learning + 50% Nutricionista alcançou o menor erro global do estudo (MAE de 21,43) e reduziu as faltas "
        "potenciais para 489 refeições. A calibração de margens de segurança conformal (P75 = +10 ref; P85 = +19 ref; Híbrido residual = "
        "+12 ref) elevou a proteção alimentar para 84,3% dos dias letivos. Os resultados parciais comprovam a viabilidade computacional "
        "do artefato para a qualificação; a versão final incorporará o teste cego de setembro/2026 e a validação prospectiva em operação "
        "real durante o quarto trimestre letivo."
    )
    p_resumo = doc.paragraphs[137]
    p_resumo.text = ""
    run_resumo = p_resumo.add_run(resumo_texto)
    run_resumo.font.color.rgb = RED_COLOR
    p_resumo.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    
    # 3. Abstract Expandido (P0142)
    print("Atualizando Abstract Expandido (415 palavras)...")
    abstract_texto = (
        "Meal production planning in institutional and school food services faces daily demand uncertainty under strict "
        "asymmetry of operational consequences: overestimation leads to perishable food waste and financial loss, whereas "
        "underestimation causes meal shortages and student food vulnerability. This research develops and evaluates an analytical "
        "and predictive artifact to support supply procurement and daily meal production decisions in a public school food service unit. "
        "Grounded in the Design Science Research (DSR) methodology, the study implements a medallion data pipeline (Bronze, Silver, "
        "and Gold layers), integrating turnstile attendance records, student meal reservations, textual menu descriptions parsed into "
        "structured protein and cooking categories, and weather data retrieved from the Open-Meteo API. The experimental protocol "
        "employed strict Walk-Forward temporal validation across 28 school weeks of 2026 (February to August), simulating the "
        "real-world operational routine on Fridays without future data leakage. Historical diagnosis from 2023 to 2025 demonstrated "
        "the failure of voluntary student reservations, showing chronic under-registration on 63.8% of school days (9,494 deficit meals). "
        "In 2026, the transition to institutional planning by the professional nutritionist mitigated food shortages but induced persistent "
        "protective overestimation (accumulating 3,354 potential surplus meals). In the kitchen preparation horizon (t+1), regularized "
        "linear algorithms outperformed isolated human planning: Lasso achieved a Mean Absolute Error (MAE) of 22.27 meals/day (R² = 0.498) "
        "and Ridge MAE of 22.46 (R² = 0.483), compared to 24.92 for the human benchmark (R² = 0.373), reducing potential surpluses by 28.3%. "
        "To balance food waste mitigation against service continuity, a Pareto efficient frontier was modeled: a collaborative hybrid "
        "strategy (50% Machine Learning + 50% Nutritionist) achieved the lowest global error in the research (MAE of 21.43) while "
        "substantially reducing potential deficits to 489 meals. The application of conformal prediction safety margins (P75 = +10 meals; "
        "P85 = +19 meals; Hybrid residual = +12 meals) achieved 84.3% food security coverage. These partial qualification findings validate "
        "computational feasibility; final dissertation defense will incorporate a blind test for September 2026 and real-time prospective "
        "validation during the fourth academic quarter."
    )
    p_abstract = doc.paragraphs[142]
    p_abstract.text = ""
    run_abstract = p_abstract.add_run(abstract_texto)
    run_abstract.font.color.rgb = RED_COLOR
    p_abstract.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # 4. Inserir Textos Conectivos de Transicao
    print("Inserindo textos conectivos de transicao para eliminar secoes sem texto...")
    # Para inserir texto logo apos um paragrafo especifico, usamos insert_paragraph_before no paragrafo seguinte
    # Secao 5.2 (antes de P0617 - 5.2.1)
    texto_transicao_52 = (
        "A modelagem preditiva supervisionada em sistemas produtivos de alimentação institucional requer a investigação "
        "prévia das propriedades empíricas que regem a série de demanda real. Nesta seção, a Análise Exploratória de Dados (EDA) "
        "é conduzida sobre a base higienizada e auditada da Camada Silver, estruturando-se em torno de quatro eixos analíticos "
        "fundamentais: a sazonalidade semanal atrelada à rotina pedagógica dos estudantes; o impacto dos atributos qualitativos "
        "do cardápio, categorizados em função do perfil proteico e dos métodos culinários de cocção; a sensibilidade estocástica "
        "do comparecimento físico discente frente às oscilações meteorológicas de precipitação e temperatura; e a dependência "
        "temporal inercial expressa pelas funções de autocorrelação. O isolamento desses padrões estatísticos subsidia a formulação "
        "da arquitetura de atributos preditivos construída na etapa subsequente na Camada Gold."
    )
    p_next_52 = doc.paragraphs[617]
    p_new_52 = p_next_52.insert_paragraph_before()
    r = p_new_52.add_run(texto_transicao_52)
    r.font.color.rgb = RED_COLOR
    p_new_52.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Secao 5.5 (antes de 5.5.1)
    texto_transicao_55 = (
        "Embora o torneio algorítmico indique a superioridade estatística das técnicas lineares regularizadas na minimização "
        "de métricas simétricas de resíduo, a gestão da produção de refeições escolares opera sob uma função de custo assimétrica, "
        "na qual o desabastecimento discente acarreta penalidades sociais consideravelmente mais severas do que o custo gerencial "
        "de sobras de balcão. Diante dessa assimetria, a presente seção submete os resultados brutos dos modelos preditivos à camada "
        "de decisão do artefato, avaliando duas intervenções complementares: a combinação colaborativa sob a Fronteira Eficiente "
        "de Pareto — que integra o conhecimento empírico da nutricionista gestora e as saídas algorítmicas — e a determinação "
        "de margens de segurança conformal não paramétricas, estruturadas para assegurar a cobertura estocástica dos níveis de "
        "serviço desejados pela gestão institucional."
    )
    # Procurar o paragrafo 5.5.1 A Assimetria de Consequencias
    for i, p in enumerate(doc.paragraphs):
        if "5.5.1 A Assimetria de Consequências" in p.text:
            p_new_55 = p.insert_paragraph_before()
            r = p_new_55.add_run(texto_transicao_55)
            r.font.color.rgb = RED_COLOR
            p_new_55.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            break

    # Secao 5.6 (antes de 5.6.1)
    texto_transicao_56 = (
        "A mensuração do impacto prático do artefato exige o confronto retrospectivo com as duas sistemáticas de dimensionamento "
        "de demanda previamente adotadas pela instituição de ensino: o modelo de manifestação voluntária por reservas discentes "
        "via sistema SUAP, praticado entre 2023 e 2025, e o planejamento institucional centralizado na nutricionista, adotado no "
        "ano letivo de 2026. A seguir, analisa-se inicialmente a decomposição do efeito compensatório nos dados de consumo real, "
        "demonstrando de que modo saldos líquidos anuais acumulados podem mascarar graves distorções operacionais diárias. Em "
        "sequência, quantificam-se os desvios de subdimensionamento e superdimensionamento inerentes a cada período histórico, "
        "estabelecendo a linha de base para a avaliação comparativa dos regimes."
    )
    for i, p in enumerate(doc.paragraphs):
        if "5.6.1 A Mensuração do Efeito Compensatório" in p.text:
            p_new_56 = p.insert_paragraph_before()
            r = p_new_56.add_run(texto_transicao_56)
            r.font.color.rgb = RED_COLOR
            p_new_56.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            break

    # Secao 5.7 (antes de 5.7.1)
    texto_transicao_57 = (
        "Nesta seção final do capítulo, os achados teóricos e empíricos são consolidados sob a ótica gerencial da tomada de "
        "decisão em sistemas produtivos de serviços de alimentação. Estrutura-se uma simulação financeira hipotética fundamentada "
        "nas tarifas contratuais reais de faturamento da UAN escolar, confrontando os custos potenciais de sobras de matéria-prima "
        "com os níveis de proteção alimentar discente alcançados por cada política de dimensionamento. Por fim, definem-se com "
        "transparência metodológica os limites e a abrangência das evidências parciais reportadas na etapa de qualificação, "
        "consolidando o roteiro para a realização do teste retrospectivo com alvo oculto e a validação prospectiva em modo sombra "
        "a ser submetida no exame de defesa definitiva."
    )
    for i, p in enumerate(doc.paragraphs):
        if "5.7.1 Comparação Geral das Alternativas" in p.text or "5.7.1 Comparao Geral das Alternativas" in p.text:
            p_new_57 = p.insert_paragraph_before()
            r = p_new_57.add_run(texto_transicao_57)
            r.font.color.rgb = RED_COLOR
            p_new_57.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            break

    # 5. Correcao das 9 Chamadas de Tabelas Incorretas e Custos Financeiros
    print("Corrigindo chamadas de tabelas e atualizando precos contratuais reais...")
    for p in doc.paragraphs:
        txt = p.text
        # Chamada 1: P0689
        if "A Tabela 13 sintetiza o melhor MAE registrado" in txt:
            p.text = ""
            r = p.add_run("A Tabela 3 sintetiza o melhor MAE registrado em cada combinação de cenário e horizonte na avaliação temporal de fevereiro a agosto de 2026.")
            r.font.color.rgb = RED_COLOR
        # Chamada 2: P0711
        elif "A Tabela 13 confronta os métodos preditivos avaliados no horizonte de preparo" in txt or "A Tabela 13 confronta os mtodos preditivos" in txt:
            p.text = ""
            r = p.add_run("A Tabela 4 confronta os métodos preditivos avaliados no horizonte de preparo (t+1) com a estimativa da nutricionista, na coorte pareada de 83 datas entre fevereiro e agosto de 2026.")
            r.font.color.rgb = RED_COLOR
        # Chamada 3: P0740
        elif "conforme a Tabela 15;" in txt:
            novo = txt.replace("Tabela 15", "Tabela 5")
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = RED_COLOR
        # Chamada 4: P0742
        elif "o menor entre as alternativas da Tabela 15" in txt:
            novo = txt.replace("Tabela 15", "Tabela 5")
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = RED_COLOR
        # Chamada 5: P0758
        elif "A análise da Figura 22 e da Tabela 15 elucida" in txt or "A anlise da Figura 22 e da Tabela 15 elucida" in txt:
            novo = txt.replace("Tabela 15", "Tabela 5")
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = RED_COLOR
        # Chamada 6: P0771
        elif "As Tabelas 4 e 5 apresentam os resultados anuais por regime" in txt:
            p.text = ""
            r = p.add_run("As Tabelas 6 e 7 apresentam os resultados anuais por regime: as reservas discentes de 2023 a 2025 e o quantitativo institucional de fevereiro a agosto de 2026.")
            r.font.color.rgb = RED_COLOR
        # Chamada 7: P0791
        elif "conforme a Tabela 17." in txt:
            novo = txt.replace("Tabela 17", "Tabela 7")
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = RED_COLOR
        # Chamada 8 e 9: P0805, P0809, P0810, P0813
        elif "A Figura 27 compara custos paramétricos ilustrativos das sobras potenciais" in txt or "A Figura 27 compara custos paramtricos" in txt:
            p.text = ""
            r = p.add_run(
                "A Figura 27 confronta o custo financeiro potencial das sobras com a taxa observada de garantia do atendimento "
                "estudantil (dias sem falta), aplicando a tarifa contratual real vigente de 2026 de R$ 14,00 por refeição. "
                "Ressalta-se que o cálculo constitui simulação gerencial de planejamento, não correspondendo a pesagens físicas de "
                "descarte ou a alunos impedidos de se alimentar."
            )
            r.font.color.rgb = RED_COLOR
        elif "Na coorte de 83 datas da Tabela 15" in txt:
            p.text = ""
            r = p.add_run(
                "Na coorte pareada de 83 datas avaliada na Tabela 5, o parâmetro institucional da nutricionista incorreu em "
                "déficit potencial em 41,0% dos dias letivos e acumulou 1.545 refeições em sobras (equivalentes a R$ 21.630,00 a "
                "R$ 14,00/refeição). Em contrapartida, a combinação colaborativa do Modelo Híbrido 50/50 conteve as sobras para "
                "1.289 refeições (R$ 18.046,00), propiciando uma economia de R$ 3.584,00 com redução simultânea das faltas para 489 refeições. "
                "Quando se adota a política de proteção da Margem Híbrida Calibrada (+12), o nível de serviço atinge 83,1% dos dias sem déficit, "
                "gerando 1.994 refeições em sobras (R$ 27.916,00), o que representa um custo R$ 5.180,00 inferior à margem Conformal P85 (+19), "
                "que atinge R$ 33.096,00 (2.364 refeições)."
            )
            r.font.color.rgb = RED_COLOR
        elif "A Tabela 18 consolida numericamente esses indicadores." in txt:
            p.text = ""
            r = p.add_run("A Tabela 8 consolida numericamente esses indicadores e o confronto econômico-operacional entre as alternativas.")
            r.font.color.rgb = RED_COLOR
        elif "Nota: custos ilustrativos calculados pelo parâmetro de R$ 8,50 por refeição" in txt or "Nota: custos ilustrativos calculados pelo parmetro de R$ 8,50" in txt:
            p.text = ""
            r = p.add_run(
                "Nota: custos financeiros potenciais calculados a partir das tarifas contratuais reais auditadas da UAN escolar: "
                "valor teto de R$ 17,36 por refeição para o período histórico (2023 a 2025 - concessão Tryx) e tarifa contratual "
                "vigente de R$ 14,00 por refeição para o ano letivo de 2026 (concessão vigente). Os desvios computados constituem "
                "grandezas teóricas de dimensionamento e planejamento gerencial, não correspondendo a pesagens físicas de restos de balcão "
                "ou a registros de estudantes desassistidos na catraca."
            )
            r.font.color.rgb = RED_COLOR

    # 6. Correcao da palavra "vies"
    print("Adequando rigor terminologico: substituindo 'vies' por Erro Medio Direcional / Natureza retrospectiva...")
    for p in doc.paragraphs:
        txt = p.text
        if "Essas métricas informam a magnitude do erro; sua direção é examinada pelo viés" in txt or "sua direo  examinada pelo vis" in txt:
            novo = txt.replace("pelo viés", "pelo Erro Médio Direcional (Mean Error - ME)").replace("pelo vis", "pelo Erro Médio Direcional (Mean Error - ME)")
            novo = novo.replace("Viés positivo", "Erro direcional positivo").replace("Vis positivo", "Erro direcional positivo")
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = RED_COLOR
        elif "Viés (Bias) e Coeficiente de Determinação (R²):" in txt or "Vis (Bias) e Coeficiente de Determinao (R):" in txt:
            novo = txt.replace("Viés (Bias)", "Erro Médio Direcional (Mean Error - ME)").replace("Vis (Bias)", "Erro Médio Direcional (Mean Error - ME)")
            novo = novo.replace("O viés indicou", "O erro médio direcional indicou").replace("O vis indicou", "O erro médio direcional indicou")
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = RED_COLOR
        elif "Viés da avaliação retrospectiva:" in txt or "Vis da avaliao retrospectiva:" in txt:
            novo = txt.replace("Viés da avaliação retrospectiva:", "Natureza retrospectiva da avaliação:").replace("Vis da avaliao retrospectiva:", "Natureza retrospectiva da avaliação:")
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = RED_COLOR
        elif "Recomenda-se acompanhar erro, viés, ajustes da equipe" in txt or "Recomenda-se acompanhar erro, vis" in txt:
            novo = txt.replace("viés", "erro médio direcional").replace("vis", "erro médio direcional")
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = RED_COLOR

    # 7. Atualizacao dos Dados da Tabela 8 (Table 23)
    print("Atualizando celulas da Tabela 8 com as tarifas reais (R$ 17,36 e R$ 14,00)...")
    t8 = doc.tables[23]
    # Header: Custo ilustrativo* -> Custo Potencial Sobras (R$)
    t8.rows[0].cells[5].text = ""
    r = t8.rows[0].cells[5].paragraphs[0].add_run("Custo Potencial Sobras (R$)")
    r.font.color.rgb = RED_COLOR
    r.bold = True
    
    # Valores de custos reais
    custos_t8 = [
        "R$ 50.621,76", # 2.916 * 17.36 (2023-25 Tryx)
        "R$ 17.332,00", # 1.238 * 14.00 (Ridge)
        "R$ 24.486,00", # 1.749 * 14.00 (P75)
        "R$ 33.096,00", # 2.364 * 14.00 (P85)
        "R$ 43.036,00", # 3.074 * 14.00 (P90)
        "R$ 18.046,00", # 1.289 * 14.00 (Hibrido 50/50)
        "R$ 27.916,00", # 1.994 * 14.00 (Hibrido +12)
        "R$ 21.630,00", # 1.545 * 14.00 (Nutricionista)
    ]
    for idx, custo in enumerate(custos_t8):
        row = t8.rows[idx + 1]
        row.cells[5].text = ""
        r = row.cells[5].paragraphs[0].add_run(custo)
        r.font.color.rgb = RED_COLOR
        r.bold = True
        row.cells[5].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

    # 8. Insercao das 3 Referencias Bibliograficas Faltantes em ordem alfabetica
    print("Inserindo as 3 obras faltantes na lista final de Referencias...")
    # Angelopoulos (antes de B... ou no inicio se comeca com A)
    # Blattberg (antes de BOX ou BREIMAN)
    # Knaflic (entre KIM e KOBLITZ ou K...)
    
    # Vamos localizar onde inserir
    p_ref_header = None
    for i, p in enumerate(doc.paragraphs):
        if p.text.strip() == "REFERÊNCIAS" or p.text.strip() == "REFERNCIAS":
            p_ref_header = i
            break
            
    print(f"Secao de Referencias localizada no paragrafo P{p_ref_header:04d}")
    
    # Inserir Angelopoulos & Bates
    ref_angelopoulos = "ANGELOPOULOS, A. N.; BATES, S. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. arXiv preprint arXiv:2107.07511, 2021. Disponível em: https://arxiv.org/abs/2107.07511."
    ref_blattberg = "BLATTBERG, R. C.; HOCH, S. J. Database models and managerial intuition: 50% model + 50% manager. Management Science, v. 36, n. 8, p. 887-899, 1990. DOI: https://doi.org/10.1287/mnsc.36.8.887."
    ref_knaflic = "KNAFLIC, C. N. Storytelling com dados: um guia sobre visualização de dados para profissionais de negócios. Rio de Janeiro: Alta Books, 2015. 272 p."

    # Localizar pontos exatos de insercao alfabetica
    # Angelopoulos: antes da primeira referencia que comeca com B ou C
    for i in range(p_ref_header + 1, len(doc.paragraphs)):
        t = doc.paragraphs[i].text.strip()
        if t and (t.startswith("B") or t.startswith("C")):
            p_new = doc.paragraphs[i].insert_paragraph_before()
            r = p_new.add_run(ref_angelopoulos)
            r.font.color.rgb = RED_COLOR
            p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            print("  [OK] Inserida referencia de Angelopoulos & Bates (2021)")
            break

    # Blattberg: antes de BOX ou BREIMAN
    for i in range(p_ref_header + 1, len(doc.paragraphs)):
        t = doc.paragraphs[i].text.strip()
        if t and (t.startswith("BOX") or t.startswith("BREIMAN")):
            p_new = doc.paragraphs[i].insert_paragraph_before()
            r = p_new.add_run(ref_blattberg)
            r.font.color.rgb = RED_COLOR
            p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            print("  [OK] Inserida referencia de Blattberg & Hoch (1990)")
            break

    # Knaflic: antes de KOBLITZ ou KUHN
    for i in range(p_ref_header + 1, len(doc.paragraphs)):
        t = doc.paragraphs[i].text.strip()
        if t and (t.startswith("KOBLITZ") or t.startswith("KUHN")):
            p_new = doc.paragraphs[i].insert_paragraph_before()
            r = p_new.add_run(ref_knaflic)
            r.font.color.rgb = RED_COLOR
            p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            print("  [OK] Inserida referencia de Knaflic (2015)")
            break

    # 9. Atualizar a Lista de Figuras Pré-Textual
    print("Atualizando a Lista de Figuras pré-textual com os 28 títulos curtos...")
    p_lista_fig = None
    for i, p in enumerate(doc.paragraphs[:250]):
        if "LISTA DE FIGURAS" in p.text:
            p_lista_fig = i
            break
            
    if p_lista_fig:
        # Encontrar os paragrafos da lista de figuras (ate LISTA DE QUADROS)
        p_lista_quadros = None
        for i in range(p_lista_fig + 1, p_lista_fig + 40):
            if "LISTA DE QUADROS" in doc.paragraphs[i].text:
                p_lista_quadros = i
                break
        if p_lista_quadros:
            print(f"Lista de Figuras compreendida entre P{p_lista_fig:04d} e P{p_lista_quadros:04d}")
            fig_idx = 1
            for p_curr in doc.paragraphs[p_lista_fig + 1: p_lista_quadros]:
                if re.match(r"^Figura\s+\d+", p_curr.text.strip()):
                    if fig_idx in TITULOS_FIGURAS:
                        # Extrair numero e pagina se existir tabulacao
                        partes = p_curr.text.split("\t")
                        pag = partes[-1] if len(partes) > 1 else ""
                        novo_txt = TITULOS_FIGURAS[fig_idx] + (f"\t{pag}" if pag else "")
                        p_curr.text = ""
                        r = p_curr.add_run(novo_txt)
                        r.font.color.rgb = RED_COLOR
                        fig_idx += 1

    # Salvar o documento modificado
    doc.save(DOCX_PATH)
    print("Documento DOCX salvo com todas as melhorias e alteracoes em VERMELHO com sucesso!")

if __name__ == "__main__":
    etapa_1_substituir_imagens_no_zip()
    etapa_2_atualizar_conteudo_docx()
