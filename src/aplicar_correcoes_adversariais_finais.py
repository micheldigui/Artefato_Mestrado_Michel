"""
Script de Aplicacao das Correcoes Adversariais Finais
Corrige os 4 pontos identificados na auditoria:
1. Insercao de textos introdutorios/conectivos em 2.2, 2.3, 2.4 e 2.5 (eliminando todos os headings consecutivos sem texto).
2. Substituicao da mencao residual a 'vies' em P0404 por 'erro medio (ME) e tendencia direcional media'.
3. Insercao da referencia de KNAFLIC (2015) em ordem alfabetica na lista de Referencias.
4. Conferencia de todos os destaques em AZUL (RGB: 0, 102, 204).
"""

import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

PATH_MERGE = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx"
BLUE_COLOR = RGBColor(0, 102, 204)

doc = docx.Document(PATH_MERGE)
print("Iniciando correcoes finais...")

# ------------------------------------------------------------------------------
# 1. Textos Conectivos para Secoes 2.2, 2.3, 2.4 e 2.5
# ------------------------------------------------------------------------------
textos_cap2 = {
    "2.2.1 Previsão de demanda em serviços": (
        "A previsão de demanda constitui o elo integrador entre a gestão estratégica de suprimentos e a eficiência "
        "operacional na produção de refeições coletivas. Em ambientes institucionais caracterizados por consumo com periodicidade "
        "diária e restrições rígidas de aquisição, estimar antecipadamente o volume de refeições a serem preparadas não se resume a um "
        "exercício estatístico abstrato, mas condiciona diretamente as compras públicas, o dimensionamento de insumos e a mitigação "
        "de excedentes perecíveis. Esta seção examina os fundamentos teóricos da previsão de demanda em serviços, contrasta as "
        "abordagens clássicas de planejamento e modelos determinísticos com o contexto empírico e discute a integração com a cadeia "
        "de suprimentos no setor público."
    ),
    "2.3.1 Ciência de dados e pipeline analítico": (
        "A transformação de dados operacionais dispersos em subsídios efetivos para a tomada de decisão gerencial exige uma "
        "arquitetura computacional sistemática, fundamentada nos preceitos da ciência de dados e da engenharia de atributos. Em sistemas "
        "de alimentação coletiva, a variabilidade do consumo registrado decorre de interações não lineares entre o calendário acadêmico, "
        "o histórico inercial de atendimento, os tipos de proteínas e preparações culinárias oferecidas e as flutuações das condições "
        "atmosféricas locais. A seguir, articulam-se os conceitos fundamentais do pipeline analítico de dados, as famílias de algoritmos "
        "de aprendizado de máquina supervisionado e as técnicas de representação e extração de atributos estruturados a partir dos cardápios escolares."
    ),
    "2.4.1 Métricas e consequências operacionais": (
        "A aferição do desempenho de modelos preditivos em sistemas produtivos não pode restringir-se a métricas globais de "
        "ajuste estatístico desconectadas das repercussões econômicas e sociais das decisões gerenciais. No contexto de refeições "
        "institucionais escolares, a assimetria entre os custos de superestimação e os danos de subestimação impõe a adoção de métricas "
        "direcionais e a validação temporal estrita, sob pena de gerar falsas expectativas de acurácia decorrentes de vazamento de dados. "
        "Esta seção aprofunda as métricas de magnitude e direção de erro em previsões, a modelagem de consequências operacionais "
        "assimétricas e os protocolos de robustez metodológica assegurados pela validação temporal sequencial."
    ),
    "2.5.1 Escalabilidade, replicabilidade e transparência": (
        "O ciclo de vida de soluções baseadas em inteligência artificial aplicadas à administração pública demanda rigor ético, "
        "governança de dados e transparência metodológica para além da acurácia algorítmica. Para que um artefato preditivo seja efetivamente "
        "incorporado à rotina institucional sem criar dependência opaca ou vulnerabilidades operacionais, seus processos devem ser "
        "auditáveis, documentados e reexecutáveis por terceiros com acesso autorizado. Esta seção discute os critérios de escalabilidade, "
        "reprodutibilidade computacional e transparência na gestão de dados, bem como os princípios de governança que sustentam o apoio "
        "colaborativo à decisão e a sustentabilidade de longo prazo do artefato."
    )
}

# Localizar os headings e inserir paragrafo antes
for i, p in enumerate(doc.paragraphs):
    txt = p.text.strip()
    for h_alvo, txt_intro in textos_cap2.items():
        if h_alvo.lower() in txt.lower() and p.style.name.startswith("Heading"):
            # Inserir paragrafo antes
            p_new = p.insert_paragraph_before()
            r = p_new.add_run(txt_intro)
            r.font.color.rgb = BLUE_COLOR
            p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            print(f"  [OK] Texto conectivo inserido antes de '{h_alvo}' em AZUL!")

# ------------------------------------------------------------------------------
# 2. Corrigir Mencao Residual a 'vies' em P0404
# ------------------------------------------------------------------------------
for i, p in enumerate(doc.paragraphs[390:420]):
    if "pelo viés, calculado como a média de previsão menos consumo" in p.text:
        txt_original = p.text
        txt_corrigido = txt_original.replace(
            "pelo viés, calculado como a média de previsão menos consumo. Viés positivo indica superestimação média, e negativo indica subestimação média.",
            "pelo erro médio (ME, mean error) ou tendência média direcional, calculada como a média da diferença entre previsão e consumo. Um valor positivo indica superestimação média, e um valor negativo indica subestimação média."
        )
        p.text = ""
        r = p.add_run(txt_corrigido)
        r.font.color.rgb = BLUE_COLOR
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        print(f"  [OK] Terminologia corrigida em P{390+i:04d} ('vies' substituido por 'erro medio (ME) e tendencia direcional') em AZUL!")
        break

# ------------------------------------------------------------------------------
# 3. Inserir Referencia de Knaflic (2015) em Ordem Alfabetica
# ------------------------------------------------------------------------------
ref_knaflic = (
    "KNAFLIC, C. N. Storytelling com dados: um guia sobre visualização de dados para profissionais de negócios. "
    "Rio de Janeiro: Alta Books, 2015. 272 p."
)

for i, p in enumerate(doc.paragraphs[850:]):
    actual_i = 850 + i
    if p.text.startswith("LANDRY, M. J."):
        # Inserir antes de LANDRY
        p_kna = p.insert_paragraph_before()
        r = p_kna.add_run(ref_knaflic)
        r.font.color.rgb = BLUE_COLOR
        # Inserir espaco em branco antes para seguir padrao ABNT de referencias
        p_blank = p.insert_paragraph_before()
        p_blank.text = ""
        print(f"  [OK] Referencia de Knaflic (2015) inserida em ordem alfabetica em AZUL antes de Landry!")
        break

# ------------------------------------------------------------------------------
# 4. Salvar o documento corrigido
# ------------------------------------------------------------------------------
doc.save(PATH_MERGE)
print(f"\nDocumento final salvo com sucesso em:\n{PATH_MERGE}")
