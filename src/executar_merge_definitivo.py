"""
Script Mestre de Merge e Refinamento Editorial Definitivo
Gera: f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx

Base: Dissertacao_Michel_qualificacao_antigravity.docx (preserva imagens 300 DPI, sincronia 1-28 de figuras e 1-8 de tabelas, Resumo ABNT 415 palavras, referencias completas e tabelas financeiras)
Fusao com Codex:
1. Paragrafo de abertura do Cap 1 (Dhir et al., Steen et al., Malefors et al.)
2. Refinamento de pergunta de pesquisa (1.2) e objetivo a) (1.3) com Open-Meteo
3. Complemento de auditoria imutavel e governanca no Cap 4 (Secao 4.7)
4. Reestruturacao de numerao no Cap 5:
   - 5.3 Resultados da Engenharia de Atributos e Selecao na Camada Gold (5.3.1 e 5.3.2)
   - 5.4 Resultados do Torneio de Modelos Preditivos (Fev. a Ago. de 2026) (5.4.1, 5.4.2, 5.4.3)
   - 5.5 Resultados das Politicas de Decisao Operacional e Margens de Seguranca (5.5.1, 5.5.2, 5.5.3)
   - 5.6 Resultados dos Regimes de Planejamento: 2023-2025 e Fev.-Ago. de 2026 (5.6.1, 5.6.2, 5.6.3)
   - 5.7 Sintese dos Resultados Economicos, Limitacoes e Passos para a Defesa Final (5.7.1, 5.7.2)
5. Redacao lapidada das Consideracoes Parciais do Cap 6 do Codex
6. Atualizacao do Sumario
7. Destaque MANDATORIO de TODAS as modificacoes e adicoes na cor AZUL (RGB: 0, 102, 204)
8. Conversao de todos os runs vermelhos para AZUL
"""

import shutil
import os
import re
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

SRC_ANTIGRAVITY = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
DST_MERGE = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx"
BLUE_COLOR = RGBColor(0, 102, 204)
RED_COLOR = RGBColor(200, 0, 0)
RED_COLOR2 = RGBColor(255, 0, 0)

print(f"Copiando base '{os.path.basename(SRC_ANTIGRAVITY)}' para '{os.path.basename(DST_MERGE)}'...")
shutil.copyfile(SRC_ANTIGRAVITY, DST_MERGE)

doc = docx.Document(DST_MERGE)
print(f"Documento carregado. Total de paragrafos: {len(doc.paragraphs)}, Tabelas: {len(doc.tables)}")

# ==============================================================================
# ETAPA 1: Converter todos os runs vermelhos ou destacados para AZUL
# ==============================================================================
print("\n--- ETAPA 1: Conversao de destaques existentes para AZUL ---")
convertidos_p = 0
for p in doc.paragraphs:
    for r in p.runs:
        if r.font.color and r.font.color.rgb:
            # Qualquer cor nao preta (vermelho) vira azul
            if r.font.color.rgb in (RED_COLOR, RED_COLOR2) or (r.font.color.rgb != BLUE_COLOR and r.font.color.rgb != RGBColor(0,0,0)):
                r.font.color.rgb = BLUE_COLOR
                convertidos_p += 1

convertidos_t = 0
for t in doc.tables:
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for r in p.runs:
                    if r.font.color and r.font.color.rgb:
                        if r.font.color.rgb in (RED_COLOR, RED_COLOR2) or (r.font.color.rgb != BLUE_COLOR and r.font.color.rgb != RGBColor(0,0,0)):
                            r.font.color.rgb = BLUE_COLOR
                            convertidos_t += 1

print(f"Runs convertidos para AZUL: {convertidos_p} em paragrafos, {convertidos_t} em tabelas.")

# ==============================================================================
# ETAPA 2: Incorporar Paragrafo de Abertura do Codex no Capitulo 1
# ==============================================================================
print("\n--- ETAPA 2: Incorporacao do Paragrafo de Abertura do Codex no Cap 1 ---")
p_intro_idx = None
for i, p in enumerate(doc.paragraphs):
    if p.text.strip().upper() == "1 INTRODUÇÃO" or p.text.strip().upper() == "1 INTRODUO":
        p_intro_idx = i
        break

if p_intro_idx is not None:
    texto_abertura_codex = (
        "A produção de refeições em restaurantes institucionais envolve decisões diárias tomadas sob incerteza. "
        "Antes que o consumo real seja observado, a gestão precisa estimar quantas refeições deverão ser preparadas, "
        "considerando restrições de tempo, insumos, equipe, cardápio, calendário acadêmico e comportamento dos usuários. "
        "A literatura sobre serviços de alimentação indica que o desperdício resulta de fatores operacionais, "
        "comportamentais e contextuais, incluindo planejamento, presença, aceitação do cardápio e controle da demanda "
        "(Dhir et al., 2020; Steen et al., 2018; Malefors et al., 2022). Quando a produção fica acima da demanda, pode haver "
        "excedente e risco de desperdício de alimentos, trabalho e recursos públicos. Quando fica abaixo, há risco de falta "
        "de atendimento."
    )
    p_next = doc.paragraphs[p_intro_idx + 1]
    if "A produção de refeições em restaurantes institucionais" not in p_next.text:
        p_new = p_next.insert_paragraph_before()
        r = p_new.add_run(texto_abertura_codex)
        r.font.color.rgb = BLUE_COLOR
        p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        print(f"  [OK] Paragrafo inicial do Codex inserido em P{p_intro_idx + 1:04d}!")

    # Refinar Pergunta de Pesquisa (1.2) e Objetivo a) (1.3)
    for p in doc.paragraphs[p_intro_idx: p_intro_idx + 40]:
        if "Em que medida um artefato que integra" in p.text and "Open-Meteo" not in p.text:
            novo_problema = (
                "Em que medida um artefato que integra o histórico de consumo, o cardápio e o calendário, e que incorpora "
                "variáveis meteorológicas do Open-Meteo e referências de planejamento conforme sua disponibilidade em cada regime, "
                "pode apoiar as decisões de compras e produção de refeições em um restaurante institucional, considerando os erros "
                "de previsão, os excessos e déficits potenciais e a antecedência das estimativas?"
            )
            p.text = ""
            r = p.add_run(novo_problema)
            r.font.color.rgb = BLUE_COLOR
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            print("  [OK] Pergunta de pesquisa refinada com Open-Meteo em AZUL!")

        if "a) integrar e documentar os dados de consumo registrado" in p.text and "Open-Meteo" not in p.text:
            novo_obj_a = (
                "a) integrar e documentar os dados de consumo registrado, cardápio, calendário e variáveis meteorológicas do Open-Meteo, "
                "preparando configurações analíticas ampliadas com histórico prévio;"
            )
            p.text = ""
            r = p.add_run(novo_obj_a)
            r.font.color.rgb = BLUE_COLOR
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            print("  [OK] Objetivo especifico a) refinado com Open-Meteo em AZUL!")

# ==============================================================================
# ETAPA 3: Complemento de Auditoria e Governanca no Capitulo 4 (Secao 4.7)
# ==============================================================================
print("\n--- ETAPA 3: Complemento de Auditoria e Governanca no Cap 4 (4.7) ---")
for i, p in enumerate(doc.paragraphs):
    if "4.7 Fluxo operacional e saídas para a gestão" in p.text or "4.7 Fluxo operacional" in p.text:
        # Procurar o paragrafo que fala de "Ao final de cada semana"
        for j in range(i, min(i + 15, len(doc.paragraphs))):
            pj = doc.paragraphs[j]
            if "Ao final de cada semana" in pj.text and "Cada emissão preserva" not in pj.text:
                texto_governança_codex = (
                    " Cada emissão preserva separadamente a previsão contínua, o plano após aplicação da política e o "
                    "quantitativo final deliberado pela equipe, acompanhados de carimbo de data e hora. A nutricionista e a "
                    "gestora podem consultar previsões anteriores e compará-las aos consumos registrados à medida que novas "
                    "semanas são concluídas."
                )
                r = pj.add_run(texto_governança_codex)
                r.font.color.rgb = BLUE_COLOR
                print(f"  [OK] Complemento de auditoria imutavel adicionado em P{j:04d} em AZUL!")
                break
        break

# ==============================================================================
# ETAPA 4: Reestruturacao Continua das Secoes do Capitulo 5 (5.1 a 5.7)
# ==============================================================================
print("\n--- ETAPA 4: Reestruturacao Continua de Secoes do Cap 5 (5.1 a 5.7) ---")
# 1. Localizar P com "5.2.5 Resultados da Engenharia de Variáveis"
# Criar Heading 2 antes dele: "5.3 Resultados da Engenharia de Atributos e Seleção na Camada Gold"
# com paragrafo introdutorio conectivo em AZUL.
for i, p in enumerate(doc.paragraphs):
    if "5.2.5 Resultados da Engenharia de Variáveis" in p.text and p.style.name.startswith("Heading"):
        # Inserir Heading 2: 5.3
        p_h53 = p.insert_paragraph_before()
        p_h53.style = doc.styles["Heading 2"]
        r = p_h53.add_run("5.3 Resultados da Engenharia de Atributos e Seleção na Camada Gold")
        r.font.color.rgb = BLUE_COLOR
        r.bold = True
        
        # Inserir texto conectivo para 5.3
        p_t53 = p.insert_paragraph_before()
        r_t = p_t53.add_run(
            "A etapa de modelagem preditiva supervisionada requer a estruturação sistemática das informações em variáveis "
            "explicativas com capacidade de capturar os padrões empíricos identificados na análise exploratória. Na Camada Gold, "
            "a base de dados foi expandida para 106 atributos computados, abrangendo defasagens inerciais de consumo, médias móveis, "
            "variáveis de calendário escolar e indicadores meteorológicos antecipados. A seguir, apresentam-se os resultados da "
            "construção desse repositório analítico de variáveis e os critérios objetivos empregados para a seleção dos atributos mais "
            "informativos para os algoritmos de aprendizado de máquina."
        )
        r_t.font.color.rgb = BLUE_COLOR
        p_t53.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        print(f"  [OK] Secao 5.3 e texto conectivo inseridos antes de P{i:04d}!")
        break

# Mapa de renumeracao no corpo do texto
renomeacoes = [
    ("5.2.5 Resultados da Engenharia de Variáveis", "5.3.1 Resultados da Engenharia de Variáveis na Camada Gold"),
    ("5.2.6 Resultados da seleção de atributos", "5.3.2 Resultados da Seleção de Atributos na Camada Gold"),
    ("5.3 Resultados do torneio de modelos (fevereiro a agosto de 2026)", "5.4 Resultados do Torneio de Modelos Preditivos (Fevereiro a Agosto de 2026)"),
    ("5.3.1 Metodologia Experimental da Validação Temporal Walk-Forward", "5.4.1 Metodologia Experimental da Validação Temporal Walk-Forward"),
    ("5.3.2 Resultados Comparativos entre Cenários e Horizontes", "5.4.2 Resultados Comparativos entre Cenários e Horizontes"),
    ("5.3.3 Ranking do Torneio de Algoritmos vs. Benchmark da Nutricionista (t+1)", "5.4.3 Ranking do Torneio de Algoritmos vs. Benchmark da Nutricionista (t+1)"),
    # Secao 5.5 permanece 5.5
    # Secao 5.6 permanece 5.6
    # Secao 5.7 permanece 5.7
]

for p in doc.paragraphs[590:840]:
    if p.style.name.startswith("Heading"):
        for antigo, novo in renomeacoes:
            if antigo.lower() in p.text.lower():
                p.text = ""
                r = p.add_run(novo)
                r.font.color.rgb = BLUE_COLOR
                r.bold = True
                print(f"  [OK] Heading renumerado: {novo[:50]}...")

# ==============================================================================
# ETAPA 5: Incorporar Redacao Lapidada do Codex nas Consideracoes Parciais (Cap 6)
# ==============================================================================
print("\n--- ETAPA 5: Incorporacao de Consideracoes Parciais do Codex (Cap 6) ---")
p_c6_idx = None
for i, p in enumerate(doc.paragraphs[800:]):
    actual_i = 800 + i
    if p.text.strip().upper() == "6 CONSIDERAÇÕES PARCIAIS" or p.text.strip().upper() == "6 CONSIDERAES PARCIAIS":
        p_c6_idx = actual_i
        break

if p_c6_idx is not None:
    textos_c6 = [
        (
            "Esta pesquisa desenvolveu e avaliou parcialmente um artefato analítico-preditivo para apoiar o planejamento da "
            "produção de refeições em um restaurante institucional. A demonstração retrospectiva integrou consumo registrado, reservas, "
            "quantitativos institucionais, cardápios, calendário e dados meteorológicos do Open-Meteo, permitindo comparar previsões e "
            "simular políticas operacionais. Os resultados se restringem às coortes explicitadas neste trabalho; a efetividade operacional "
            "prospectiva em tempo real será avaliada na etapa posterior da pesquisa."
        ),
        (
            "Na decomposição anual do regime de reservas, o consumo registrado superou as reservas em 38,1% das datas de 2023, 82,8% em 2024 "
            "e 78,7% em 2025. Esses valores descrevem descompassos potenciais entre planejamento e consumo registrado; não medem desassistência "
            "física nem devem ser confundidos com a competição de modelos de 2026."
        ),
        (
            "Na comparação pareada de 83 datas de 2026, o Lasso apresentou MAE de 22,27 refeições/dia, ante 24,92 do benchmark institucional da nutricionista. "
            "A combinação colaborativa do Modelo Híbrido 50/50 atingiu MAE de 21,43 e o menor déficit potencial acumulado (489 refeições). A política "
            "prudencial com margem Conformal P85 (+19 refeições) reduziu a proporção de dias com déficit potencial de 43,4% para 15,7%, assegurando "
            "84,3% de proteção alimentar aos estudantes. Os resultados são retrospectivos e específicos às coortes e regras avaliadas."
        ),
        (
            "Os objetivos de integrar e preparar fontes heterogêneas, construir o pipeline analítico e comparar modelos e cenários foram atendidos "
            "computacionalmente. A avaliação em decisão real permanece parcial: não houve teste prospectivo com previsões registradas antes da produção, "
            "nem medição física de compras, custos, descarte de sobras em balança ou atendimento na catraca. As diferenças simuladas constituem estimativas "
            "potenciais de dimensionamento gerencial."
        ),
        (
            "Como contribuição para os sistemas produtivos, o estudo organiza um processo documentado e reexecutável no ambiente computacional para "
            "preparação, previsão e simulação sob incerteza, explicitando fontes, métricas e custos operacionais potenciais baseados nas tarifas "
            "contratuais reais de R$ 17,36 (2023-2025) e R$ 14,00 (2026). A combinação colaborativa de modelos preditivos e experiência da nutricionista "
            "permite examinar cenários e aplicar julgamento contextual, mantendo a soberania decisória final com a equipe gestora."
        ),
        (
            "A continuidade da pesquisa deverá avaliar o artefato em novas datas, com previsões e parâmetros registrados antes do serviço. "
            "Recomenda-se acompanhar a magnitude e a direção dos erros, os ajustes da equipe, a produção diária, as sobras medidas por protocolo "
            "e as ocorrências de atendimento. As margens de segurança deverão ser reavaliadas no teste cego de setembro e na validação prospectiva "
            "em modo sombra durante o quarto trimestre letivo de 2026, a ser apresentada no exame de defesa definitiva."
        )
    ]
    for k, txt_c6 in enumerate(textos_c6):
        target_p = doc.paragraphs[p_c6_idx + 1 + k]
        target_p.text = ""
        r = target_p.add_run(txt_c6)
        r.font.color.rgb = BLUE_COLOR
        target_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    print(f"  [OK] 6 paragrafos de Consideracoes Parciais atualizados em AZUL!")

# ==============================================================================
# ETAPA 6: Atualizar o Sumario para a Sequencia 5.1 a 5.7
# ==============================================================================
print("\n--- ETAPA 6: Atualizacao do Sumario ---")
# No Sumario (P0218 a P0290), ajustar as linhas correspondentes ao Cap 5
for p in doc.paragraphs[215:295]:
    txt = p.text.strip()
    if txt.startswith("5.2.5"):
        p.text = ""
    elif txt.startswith("5.2.6"):
        p.text = ""
    elif txt.startswith("5.3 Resultados do torneio"):
        p.text = ""
        r1 = p.add_run("5.3 Resultados da Engenharia de Atributos e Seleção na Camada Gold\t67\n")
        r1.font.color.rgb = BLUE_COLOR
        r2 = p.add_run("5.4 Resultados do Torneio de Modelos Preditivos (Fev. a Ago. de 2026)\t69")
        r2.font.color.rgb = BLUE_COLOR
    elif txt.startswith("5.3.1"):
        p.text = p.text.replace("5.3.1", "5.4.1")
        for r in p.runs:
            r.font.color.rgb = BLUE_COLOR
    elif txt.startswith("5.3.2"):
        p.text = p.text.replace("5.3.2", "5.4.2")
        for r in p.runs:
            r.font.color.rgb = BLUE_COLOR
    elif txt.startswith("5.3.3"):
        p.text = p.text.replace("5.3.3", "5.4.3")
        for r in p.runs:
            r.font.color.rgb = BLUE_COLOR

print("  [OK] Sumario harmonizado para sequencia 5.1 a 5.7!")

# ==============================================================================
# ETAPA 7: Salvar o Documento
# ==============================================================================
doc.save(DST_MERGE)
print(f"\nDocumento de MERGE salvo com sucesso em:\n{DST_MERGE}")
