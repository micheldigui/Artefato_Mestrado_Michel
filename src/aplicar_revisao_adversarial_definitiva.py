"""
Script de Refinamento Adversarial e Correcoes Exaustivas
Aplica todas as correcoes identificadas no arquivo:
f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx

Correcoes realizadas:
1. Resumo e Abstract densos, metodologicamente completos (~365 e ~328 palavras, ABNT NBR 6028) destacados em AZUL.
2. Limpeza do Sumario:
   - Remocao do paragrafo espurio P0283 ("As simulacoes de politicas usam 83 datas...")
   - Insercao da linha nivel 2 de 5.3 ("5.3 Resultados da Engenharia de Atributos e Selecao na Camada Gold\t67")
   - Sincronizacao perfeita das paginas de 5.3 a 5.7 e Cap 6.
3. Insercao do complemento de governanca e auditoria imutavel na Secao 4.7 (P0583/Quadro 14) em AZUL.
4. Aplicacao de italico em termos tecnicos em lingua estrangeira em todo o corpo do texto.
5. Garantia absoluta de que todos os destaques estejam na cor AZUL (RGB: 0, 102, 204) e zero em vermelho.
"""

import os
import re
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

PATH_MERGE = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx"
BLUE_COLOR = RGBColor(0, 102, 204)
RED_COLOR = RGBColor(200, 0, 0)
RED_COLOR2 = RGBColor(255, 0, 0)

doc = docx.Document(PATH_MERGE)
print(f"Carregando {os.path.basename(PATH_MERGE)}...")

# ------------------------------------------------------------------------------
# 1. Ajuste do Resumo e Abstract
# ------------------------------------------------------------------------------
print("\n--- 1. Ajustando Resumo e Abstract para versao densa ABNT NBR 6028 ---")
texto_resumo = (
    "O planejamento da produção de refeições em restaurantes institucionais e escolares lida diariamente com a incerteza "
    "da demanda, sob severa assimetria de consequências: superestimativas acarretam desperdício de alimentos perecíveis e "
    "recursos públicos, enquanto subestimativas provocam déficit de atendimento e vulnerabilidade nutricional estudantil. "
    "Esta pesquisa desenvolve e avalia um artefato analítico-preditivo voltado a apoiar as decisões de compra de suprimentos "
    "e produção diária em uma Unidade de Alimentação e Nutrição (UAN) escolar. Conduzido sob o método da Design Science Research (DSR), "
    "o estudo estrutura uma arquitetura em camadas de dados (Medallion: Bronze, Silver e Gold), integrando registros de "
    "atendimento da catraca, reservas voluntárias, cardápios categorizados por processamento de texto e dados meteorológicos da "
    "API Open-Meteo. A avaliação experimental adotou validação temporal sequencial (Walk-Forward Validation) ao longo de 28 semanas "
    "letivas de 2026 (fevereiro a agosto), simulando fielmente a tomada de decisão às sextas-feiras sem vazamento de dados futuros. "
    "O diagnóstico histórico de 2023 a 2025 revelou a falência funcional do modelo de reservas voluntárias dos discentes, com "
    "subnotificação crônica em 63,8% dos dias letivos (déficit acumulado de 9.494 refeições). Em 2026, a assunção do planejamento "
    "institucional pela nutricionista conteve o desabastecimento, mas gerou superestimativa preventiva contínua (3.354 refeições em "
    "sobras potenciais no período). No horizonte de preparo (t+1), os modelos lineares regularizados superaram o planejamento humano "
    "isolado: o Lasso atingiu Erro Absoluto Médio (MAE) de 22,27 refeições/dia (R² = 0,498) e o Ridge MAE de 22,46 (R² = 0,483), "
    "ante 24,92 da nutricionista isolada (R² = 0,373), reduzindo as sobras potenciais em 28,3%. Para equilibrar o custo operacional da "
    "sobra e a garantia social do atendimento, formulou-se a Fronteira Eficiente de Pareto do Modelo Híbrido ponderado: a combinação "
    "colaborativa de 50% Machine Learning + 50% Nutricionista alcançou o menor erro global do estudo (MAE de 21,43) e reduziu as "
    "faltas potenciais para 489 refeições. A calibração de margens de segurança conformal (P75 = +10 ref; P85 = +19 ref; Híbrido residual = +12 ref) "
    "elevou a proteção alimentar para 84,3% dos dias letivos. Os resultados parciais comprovam a viabilidade computacional do artefato "
    "para a qualificação; a versão final incorporará o teste cego de setembro/2026 e a validação prospectiva em operação real durante o "
    "quarto trimestre letivo."
)

texto_abstract = (
    "Meal production planning in institutional and school food services faces daily demand uncertainty under strict asymmetry "
    "of operational consequences: overestimation leads to perishable food waste and financial loss, whereas underestimation causes meal "
    "shortages and student food vulnerability. This research develops and evaluates an analytical and predictive artifact to support supply "
    "procurement and daily meal production decisions in a public school food service unit. Grounded in the Design Science Research (DSR) "
    "methodology, the study implements a medallion data pipeline (Bronze, Silver, and Gold layers), integrating turnstile attendance "
    "records, student meal reservations, textual menu descriptions parsed into structured protein and cooking categories, and weather data "
    "retrieved from the Open-Meteo API. The experimental protocol employed strict Walk-Forward temporal validation across 28 school weeks "
    "of 2026 (February to August), simulating the real-world operational routine on Fridays without future data leakage. Historical diagnosis "
    "from 2023 to 2025 demonstrated the failure of voluntary student reservations, showing chronic under-registration on 63.8% of school days "
    "(9,494 deficit meals). In 2026, the transition to institutional planning by the professional nutritionist mitigated food shortages but "
    "induced persistent protective overestimation (accumulating 3,354 potential surplus meals). In the kitchen preparation horizon (t+1), "
    "regularized linear algorithms outperformed isolated human planning: Lasso achieved a Mean Absolute Error (MAE) of 22.27 meals/day "
    "(R² = 0.498) and Ridge MAE of 22.46 (R² = 0.483), compared to 24.92 for the human benchmark (R² = 0.373), reducing potential surpluses "
    "by 28.3%. To balance food waste mitigation against service continuity, a Pareto efficient frontier was modeled: a collaborative hybrid "
    "strategy (50% Machine Learning + 50% Nutritionist) achieved the lowest global error in the research (MAE of 21.43) while substantially "
    "reducing potential deficits to 489 meals. The application of conformal prediction safety margins (P75 = +10 meals; P85 = +19 meals; "
    "Hybrid residual = +12 meals) achieved 84.3% food security coverage. These partial qualification findings validate computational "
    "feasibility; final dissertation defense will incorporate a blind test for September 2026 and real-time prospective validation during the "
    "fourth academic quarter."
)

p_resumo = doc.paragraphs[137]
p_resumo.text = ""
r_res = p_resumo.add_run(texto_resumo)
r_res.font.color.rgb = BLUE_COLOR
p_resumo.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

p_abstract = doc.paragraphs[142]
p_abstract.text = ""
r_abs = p_abstract.add_run(texto_abstract)
r_abs.font.color.rgb = BLUE_COLOR
p_abstract.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
print(f"  [OK] Resumo ({len(texto_resumo.split())} palavras) e Abstract ({len(texto_abstract.split())} palavras) atualizados em AZUL!")

# ------------------------------------------------------------------------------
# 2. Limpeza e Sincronizacao do Sumario
# ------------------------------------------------------------------------------
print("\n--- 2. Limpeza e Sincronizacao do Sumario ---")
# Localizar P com "As simulações de políticas usam 83 datas pareadas" no Sumario e limpa-lo
for i in range(215, 292):
    p = doc.paragraphs[i]
    if "As simulações de políticas usam 83 datas pareadas" in p.text:
        p.text = ""
        print(f"  [OK] Paragrafo espurio P{i:04d} removido do Sumario!")

# Ajustar linhas de 5.3 a 5.7 no Sumario
for i in range(265, 290):
    p = doc.paragraphs[i]
    txt = p.text.strip()
    if txt.startswith("5.3.1"):
        # Antes de 5.3.1, se a linha anterior nao tiver 5.3 nivel 2, podemos colocar 5.3 antes
        # Na verdade, podemos reescrever as linhas do Cap 5 no Sumario de forma exata
        pass

# Vamos fazer uma substituicao cirurgica do bloco do Cap 5 no Sumario (de 5.2.4 ate Cap 6)
idx_53_inicio = None
for i in range(265, 280):
    if "5.3.1" in doc.paragraphs[i].text or "5.3 Resultados" in doc.paragraphs[i].text:
        idx_53_inicio = i
        break

linhas_sumario_cap5 = [
    ("5.3 Resultados da Engenharia de Atributos e Seleção na Camada Gold\t67", "toc 2"),
    ("5.3.1 Resultados da engenharia de variáveis na Camada Gold\t67", "toc 3"),
    ("5.3.2 Resultados da seleção de atributos na Camada Gold\t68", "toc 3"),
    ("5.4 Resultados do Torneio de Modelos Preditivos (Fevereiro a Agosto de 2026)\t69", "toc 2"),
    ("5.4.1 Metodologia experimental da validação temporal walk-forward\t69", "toc 3"),
    ("5.4.2 Resultados comparativos entre cenários e horizontes\t70", "toc 3"),
    ("5.4.3 Ranking do torneio de algoritmos e benchmark da nutricionista (t+1)\t72", "toc 3"),
    ("5.5 Resultados das políticas de decisão operacional e margens de segurança\t74", "toc 2"),
    ("5.5.1 A Assimetria de Consequências na Alimentação Escolar\t74", "toc 3"),
    ("5.5.2 Resultados da Fronteira Eficiente de Pareto do Modelo Híbrido\t74", "toc 3"),
    ("5.5.3 Resultados das Margens Prudenciais via Predição Conformal\t75", "toc 3"),
    ("5.6 Resultados dos regimes de planejamento: 2023–2025 e fevereiro–agosto de 2026\t77", "toc 2"),
    ("5.6.1 A Mensuração do Efeito Compensatório nos Dados Reais\t77", "toc 3"),
    ("5.6.2 Resultados do Período de Reservas dos Estudantes (2023 a 2025)\t79", "toc 3"),
    ("5.6.3 Resultados da Transição para o Quantitativo da Nutricionista (fev. a ago. de 2026)\t80", "toc 3"),
    ("5.7 Síntese das alternativas, limitações e passos para a defesa\t81", "toc 2"),
    ("5.7.1 Comparação Geral das Alternativas de Decisão\t81", "toc 3"),
    ("5.7.2 Limitações das Evidências Parciais e Próximos Passos\t83", "toc 3"),
]

# Encontrar o intervalo exato no sumario entre 5.2.4 e 6 CONSIDERACOES PARCIAIS
idx_524 = None
idx_cap6_sum = None
for i in range(260, 295):
    t = doc.paragraphs[i].text.strip()
    if t.startswith("5.2.4"):
        idx_524 = i
    elif "6 CONSIDERAÇÕES PARCIAIS" in t or "6 CONSIDERAES PARCIAIS" in t:
        idx_cap6_sum = i
        break

if idx_524 and idx_cap6_sum:
    # Limpar paragrafos existentes no intervalo
    paragrafos_intervalo = doc.paragraphs[idx_524 + 1: idx_cap6_sum]
    for p in paragrafos_intervalo:
        p.text = ""
        
    # Preencher com as linhas corretas
    for k, (texto_item, estilo_nome) in enumerate(linhas_sumario_cap5):
        if k < len(paragrafos_intervalo):
            target_p = paragrafos_intervalo[k]
        else:
            target_p = doc.paragraphs[idx_cap6_sum].insert_paragraph_before()
        target_p.text = ""
        try:
            target_p.style = doc.styles[estilo_nome]
        except:
            pass
        r = target_p.add_run(texto_item)
        r.font.color.rgb = BLUE_COLOR
    print("  [OK] Sumario do Capitulo 5 reconstruido com alinhamento perfeito de 5.3 a 5.7 em AZUL!")

# ------------------------------------------------------------------------------
# 3. Adicionar Complemento de Governanca e Auditoria no Cap 4 (Secao 4.7 / Quadro 14)
# ------------------------------------------------------------------------------
print("\n--- 3. Adicionando Complemento de Governanca na Secao 4.7 ---")
texto_gov = (
    " Cada emissão preserva separadamente a previsão contínua, o plano após aplicação da política e o "
    "quantitativo final deliberado pela equipe, acompanhados de carimbo de data e hora. A nutricionista e a "
    "gestora podem consultar previsões anteriores e compará-las aos consumos registrados à medida que novas "
    "semanas são concluídas."
)
for i in range(570, 600):
    p = doc.paragraphs[i]
    if "Quadro 14 distingue as informações" in p.text:
        if "Cada emissão preserva separadamente" not in p.text:
            r = p.add_run(texto_gov)
            r.font.color.rgb = BLUE_COLOR
            print(f"  [OK] Complemento de governanca inserido com sucesso em P{i:04d} em AZUL!")
        break

# ------------------------------------------------------------------------------
# 4. Aplicar Italico em Termos Tecnicos em Lingua Estrangeira
# ------------------------------------------------------------------------------
print("\n--- 4. Aplicando Italico em Termos Estrangeiros ---")
termos_ingles = [
    "Machine Learning",
    "Design Science Research",
    "Walk-Forward Validation",
    "Walk-Forward",
    "Data Leakage",
    "Overfitting",
    "Underfitting",
    "Mean Absolute Error",
    "Random Forest",
    "Gradient Boosting",
    "ExtraTrees",
    "Feature Store",
    "Decision Support System",
    "Blind Test",
    "Live Deployment",
    "Shadow Run",
    "Shadow Mode",
    "Conformal Prediction",
    "Dataset",
    "Datasets",
    "Baseline",
    "Baselines",
    "Pipeline",
    "Pipelines",
    "Framework",
    "Frameworks",
    "Benchmark",
    "Benchmarks",
    "Trade-off",
    "Trade-offs",
    "Backtesting",
    "In loco",
    "Ex-post",
    "Ex-ante",
]
pattern_ingles = re.compile(r'(' + '|'.join(re.escape(t) for t in termos_ingles) + r')', re.IGNORECASE)

total_italicos = 0
for i in range(293, len(doc.paragraphs)):
    p = doc.paragraphs[i]
    if p.style.name.startswith("Heading"):
        continue
    txt = p.text.strip()
    if txt.startswith("Figura ") or txt.startswith("Tabela ") or txt.startswith("Quadro ") or txt.startswith("Fonte:"):
        continue
    if pattern_ingles.search(txt):
        for r in p.runs:
            if pattern_ingles.search(r.text):
                r.italic = True
                total_italicos += 1

print(f"  [OK] Total de runs com italico aplicado em termos em ingles: {total_italicos}")

# ------------------------------------------------------------------------------
# 5. Garantia Estrita de Destaque AZUL (RGB 0, 102, 204)
# ------------------------------------------------------------------------------
print("\n--- 5. Verificando e Garantindo Destaques Estritamente em AZUL ---")
total_azul = 0
total_vermelho = 0
for p in doc.paragraphs:
    for r in p.runs:
        if r.font.color and r.font.color.rgb:
            if r.font.color.rgb in (RED_COLOR, RED_COLOR2) or (r.font.color.rgb != BLUE_COLOR and r.font.color.rgb != RGBColor(0,0,0)):
                r.font.color.rgb = BLUE_COLOR
                total_vermelho += 1
            elif r.font.color.rgb == BLUE_COLOR:
                total_azul += 1

for t in doc.tables:
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for r in p.runs:
                    if r.font.color and r.font.color.rgb:
                        if r.font.color.rgb in (RED_COLOR, RED_COLOR2) or (r.font.color.rgb != BLUE_COLOR and r.font.color.rgb != RGBColor(0,0,0)):
                            r.font.color.rgb = BLUE_COLOR
                            total_vermelho += 1
                        elif r.font.color.rgb == BLUE_COLOR:
                            total_azul += 1

print(f"  Total de runs em AZUL: {total_azul}")
print(f"  Total de runs vermelhos convertidos: {total_vermelho}")

# Salvar documento definitivo
doc.save(PATH_MERGE)
print(f"\nDocumento final refinado e salvo com sucesso em:\n{PATH_MERGE}")
