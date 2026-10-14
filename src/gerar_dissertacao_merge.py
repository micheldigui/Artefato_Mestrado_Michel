"""
Script para geracao da versao definitiva de MERGE:
f:\\PROJETOS\\ARTEFATO\\dissertacao\\Dissertacao_Michel_qualificacao_merge.docx

Regras mandatorias:
- Dissertacao_Michel_qualificacao_antigravity.docx e Dissertacao_Michel_qualificacao_codex.docx permanecem INTACTOS.
- Todas as alteracoes, adicoes e melhorias no arquivo MERGE ficam na cor AZUL (RGB: 0, 102, 204).
- Fusao do melhor do Antigravity (imagens 300 DPI, Resumo e Abstract densos de 415 palavras, 3 referencias completas, tabela de custos a R$ 14,00 e R$ 17,36, eliminacao do vies) com o melhor do Codex (paragrafo de abertura do Cap 1, refinamentos conceituais, correcoes no Cap 4 e Cap 6).
- Numeracao continua no Capitulo 5 (5.1 a 5.7), sincronizada com as 28 figuras e 8 tabelas.
- Atualizacao e alinhamento do Sumario e Listas Pre-Textuais.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import shutil
import re

PATH_MERGE = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx"
BLUE_COLOR = RGBColor(0, 102, 204)

doc = docx.Document(PATH_MERGE)

print("Iniciando sintese e merge editorial...")

# 1. Converter todos os runs vermelhos existentes para AZUL
print("Convertendo elementos destacados para AZUL...")
runs_azuis = 0
for p in doc.paragraphs:
    for r in p.runs:
        if r.font.color and r.font.color.rgb:
            # Qualquer cor destacada (vermelho) vira AZUL
            if r.font.color.rgb != BLUE_COLOR:
                r.font.color.rgb = BLUE_COLOR
                runs_azuis += 1

for t in doc.tables:
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                for r in p.runs:
                    if r.font.color and r.font.color.rgb:
                        if r.font.color.rgb != BLUE_COLOR:
                            r.font.color.rgb = BLUE_COLOR
                            runs_azuis += 1

print(f"Total de runs convertidos para AZUL: {runs_azuis}")

# 2. Incorporar melhorias do Codex no Capitulo 1 (Introducao)
print("Incorporando melhorias do Codex no Capitulo 1...")
p_intro_idx = None
for i, p in enumerate(doc.paragraphs):
    if p.text.strip() == "1 INTRODUÇÃO" or p.text.strip() == "1 INTRODUO":
        p_intro_idx = i
        break

# Inserir o paragrafo inicial de contextualizacao do Codex logo apos 1 INTRODUCAO
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

# Verificar se ja nao esta inserido
p_next_intro = doc.paragraphs[p_intro_idx + 1]
if "A produção de refeições em restaurantes institucionais envolve decisões" not in p_next_intro.text:
    p_new_intro = p_next_intro.insert_paragraph_before()
    r = p_new_intro.add_run(texto_abertura_codex)
    r.font.color.rgb = BLUE_COLOR
    p_new_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    print("  [OK] Paragrafo inicial do Codex incorporado na Introducao!")

# Refinar formulacao da pergunta de pesquisa (1.2) e objetivos (1.3)
for p in doc.paragraphs[p_intro_idx: p_intro_idx + 35]:
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
        print("  [OK] Pergunta de pesquisa refinada com mencao ao Open-Meteo!")

    if "a) integrar e documentar os dados de consumo registrado" in p.text and "Open-Meteo" not in p.text:
        novo_obj_a = (
            "a) integrar e documentar os dados de consumo registrado, cardápio, calendário e variáveis meteorológicas do Open-Meteo, "
            "preparando configurações analíticas ampliadas com histórico prévio;"
        )
        p.text = ""
        r = p.add_run(novo_obj_a)
        r.font.color.rgb = BLUE_COLOR
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        print("  [OK] Objetivo especifico a) refinado com mencao ao Open-Meteo!")

# 3. Incorporar melhorias do Codex no Capitulo 4 (Modelo Sistemico)
print("Incorporando melhorias do Codex no Capitulo 4...")
for i, p in enumerate(doc.paragraphs[540:610]):
    if "4.7 Fluxo operacional e saídas para a gestão" in p.text or "4.7 Fluxo operacional" in p.text:
        # Localizar paragrafo de governanca para adicionar complemento de auditoria
        for j in range(i, i + 15):
            pj = doc.paragraphs[j]
            if "Cada emissão preserva" not in pj.text and "Ao final de cada semana" in pj.text:
                texto_governança_codex = (
                    " Cada emissão preserva separadamente a previsão contínua, o plano após aplicação da política e o "
                    "quantitativo final deliberado pela equipe, acompanhados de carimbo de data e hora. A nutricionista e a "
                    "gestora podem consultar previsões anteriores e compará-las aos consumos registrados à medida que novas "
                    "semanas são concluídas."
                )
                r = pj.add_run(texto_governança_codex)
                r.font.color.rgb = BLUE_COLOR
                print("  [OK] Complemento de auditoria imutavel do Codex incorporado na Secao 4.7!")
                break

# 4. Numeracao Continua no Capitulo 5 (5.1 a 5.7)
print("Harmonizando a numeracao das secoes do Capitulo 5 para sequencia continua (5.1 a 5.7)...")
# O Antigravity tinha:
# 5.1 -> 5.1.1, 5.1.2
# 5.2 -> 5.2.1, 5.2.2, 5.2.3, 5.2.4
# 5.2.5 e 5.2.6 viram 5.3 Resultados da Engenharia de Atributos e Selecao na Camada Gold (5.3.1 e 5.3.2)
# 5.3 Torneio de Modelos vira 5.4 Resultados do Torneio de Modelos (5.4.1, 5.4.2, 5.4.3)
# 5.5 Politicas Operacionais vira 5.5 Resultados das Politicas de Decisao Operacional (5.5.1, 5.5.2, 5.5.3)
# 5.6 Regimes de Planejamento permanece 5.6 (5.6.1, 5.6.2, 5.6.3)
# 5.7 Sintese Economica permanece 5.7 (5.7.1, 5.7.2)

mapa_renumeracao = [
    ("5.2.5 Resultados da Engenharia de Variáveis", "5.3.1 Resultados da Engenharia de Variáveis na Camada Gold"),
    ("5.2.6 Resultados da seleção de atributos", "5.3.2 Resultados da Seleção de Atributos na Camada Gold"),
    ("5.3 Resultados do torneio de modelos", "5.4 Resultados do Torneio de Modelos Preditivos (Fevereiro a Agosto de 2026)"),
    ("5.3.1 Metodologia Experimental", "5.4.1 Metodologia Experimental da Validação Temporal Walk-Forward"),
    ("5.3.2 Resultados Comparativos", "5.4.2 Resultados Comparativos entre Cenários e Horizontes"),
    ("5.3.3 Ranking do Torneio", "5.4.3 Ranking do Torneio de Algoritmos vs. Benchmark da Nutricionista (t+1)"),
]

# Inserir o titulo 5.3 antes de 5.3.1 se nao existir
for i, p in enumerate(doc.paragraphs[600:750]):
    actual_i = 600 + i
    if "5.2.5 Resultados da Engenharia de Variáveis" in p.text:
        # Inserir Heading 2: 5.3 Resultados da Engenharia de Atributos e Selecao na Camada Gold
        p_new_h53 = p.insert_paragraph_before()
        p_new_h53.style = doc.styles["Heading 2"]
        r = p_new_h53.add_run("5.3 Resultados da Engenharia de Atributos e Seleção na Camada Gold")
        r.font.color.rgb = BLUE_COLOR
        r.bold = True
        
        # Inserir texto conectivo para 5.3
        p_new_t53 = p.insert_paragraph_before()
        r = p_new_t53.add_run(
            "A etapa de modelagem preditiva supervisionada requer a estruturação sistemática das informações em variáveis "
            "explicativas com capacidade de capturar os padrões empíricos identificados na análise exploratória. Na Camada Gold, "
            "a base de dados foi expandida para 106 atributos computados, abrangendo defasagens inerciais de consumo, médias móveis, "
            "variáveis de calendário escolar e indicadores meteorológicos antecipados. A seguir, apresentam-se os resultados da "
            "construção desse repositório analítico de variáveis e os critérios objetivos empregados para a seleção dos atributos mais "
            "informativos para os algoritmos de aprendizado de máquina."
        )
        r.font.color.rgb = BLUE_COLOR
        p_new_t53.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        print("  [OK] Secao 5.3 e texto conectivo inseridos com sucesso!")
        break

# Aplicar renumeracao de titulos no texto
for p in doc.paragraphs[600:750]:
    for antigo, novo in mapa_renumeracao:
        if antigo.lower() in p.text.lower() and p.style.name.startswith("Heading"):
            p.text = ""
            r = p.add_run(novo)
            r.font.color.rgb = BLUE_COLOR
            r.bold = True
            print(f"  [OK] Titulo renumerado: {novo[:50]}...")

# 5. Incorporar melhorias do Codex no Capitulo 6 (Consideracoes Parciais)
print("Incorporando melhorias redacionais do Codex no Capitulo 6...")
p_c6_idx = None
for i, p in enumerate(doc.paragraphs[800:]):
    actual_i = 800 + i
    if p.text.strip() == "6 CONSIDERAÇÕES PARCIAIS" or p.text.strip() == "6 CONSIDERAES PARCIAIS":
        p_c6_idx = actual_i
        break

if p_c6_idx:
    # Substituir os paragrafos de consideracoes pelo texto lapidado do Codex
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
    
    # Atualizar os 6 paragrafos subsequentes a 6 CONSIDERACOES PARCIAIS
    for k, txt_c6 in enumerate(textos_c6):
        target_p = doc.paragraphs[p_c6_idx + 1 + k]
        target_p.text = ""
        r = target_p.add_run(txt_c6)
        r.font.color.rgb = BLUE_COLOR
        target_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    print("  [OK] Consideracoes Parciais atualizadas com redacao lapidada do Codex em AZUL!")

# 6. Atualizar o Sumario para refletir exatamente a numeracao continua
print("Atualizando Sumario para a numeracao continua (5.1 a 5.7)...")
for p in doc.paragraphs[218:295]:
    txt = p.text
    if "5.2.5" in txt or "5.2.6" in txt:
        p.text = ""
    elif "5.3 Resultados do torneio" in txt:
        p.text = ""
        r = p.add_run("5.3 Resultados da Engenharia de Atributos e Seleção na Camada Gold\t67\n5.4 Resultados do Torneio de Modelos Preditivos (Fev. a Ago. de 2026)\t69")
        r.font.color.rgb = BLUE_COLOR
    elif "5.3.1" in txt:
        p.text = txt.replace("5.3.1", "5.4.1")
        for r in p.runs:
            r.font.color.rgb = BLUE_COLOR
    elif "5.3.2" in txt:
        p.text = txt.replace("5.3.2", "5.4.2")
        for r in p.runs:
            r.font.color.rgb = BLUE_COLOR
    elif "5.3.3" in txt:
        p.text = txt.replace("5.3.3", "5.4.3")
        for r in p.runs:
            r.font.color.rgb = BLUE_COLOR

# Salvar o documento final de merge
doc.save(PATH_MERGE)
print(f"\nDocumento de MERGE salvo com sucesso em:\n{PATH_MERGE}")
