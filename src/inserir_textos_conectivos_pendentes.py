"""
Script para sanar todos os alertas de secoes sem texto introdutorio
e assegurar 100% de conformidade com as normas ABNT e orientacoes do exame.
"""

import docx
from docx.shared import RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

DOCX_PATH = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
RED_COLOR = RGBColor(200, 0, 0)

doc = docx.Document(DOCX_PATH)

TEXTOS_SECOES = [
    ("2.2 Previsão de demanda", (
        "A literatura clássica de administração da produção e engenharia de operações estabelece que a previsão de "
        "demanda constitui a base fundamental para o planejamento das necessidades de materiais e o dimensionamento "
        "da capacidade produtiva. Em serviços de alimentação coletiva, a gestão da cadeia de suprimentos enfrenta o desafio "
        "da perecibilidade dos insumos e da variabilidade estocástica do fluxo de usuários. A seguir, articulam-se os "
        "fundamentos teóricos da previsão de demanda em sistemas de serviços, as abordagens consagradas de planejamento e "
        "otimização da capacidade instalada e as estratégias logísticas voltadas à mitigação de estoques excessivos e "
        "perdas na cadeia de suprimentos."
    )),
    ("2.3 Ciência de dados", (
        "O avanço da ciência de dados e a disponibilidade crescente de registros transacionais automatizados transformaram "
        "a modelagem preditiva em ferramenta estratégica para o suporte à decisão operacional em sistemas produtivos. A "
        "estruturação de arquiteturas orientadas a pipelines analíticos permite integrar fontes heterogêneas de informação, "
        "promovendo a higienização, a transformação e a engenharia de atributos temporais. Nesta seção, contextualizam-se os "
        "princípios que regem os pipelines analíticos modernos e sistematizam-se as famílias de modelos de aprendizado de "
        "máquina aplicáveis à predição de demanda, fundamentando suas propriedades estatísticas e matemáticas."
    )),
    ("2.4 Avaliação preditiva", (
        "A eficácia de um artefato analítico em ambiente fabril ou de serviços depende criticamente da adequação de suas "
        "métricas de desempenho e da compreensão da estrutura de perdas associada aos erros de estimação. Em contextos "
        "institucionais com restrições operacionais rígidas, desvios positivos e negativos não acarretam as mesmas consequências "
        "gerenciais, exigindo metodologias de avaliação que transcendam as medidas estatísticas simétricas. A seguir, discutem-se "
        "as métricas fundamentais de acurácia preditiva, a formalização teórica da perda assimétrica e as abordagens modernas "
        "de quantificação não paramétrica de incerteza operacional."
    )),
    ("2.5 Transparência, replicabilidade", (
        "A sustentabilidade e a confiabilidade de soluções tecnológicas desenvolvidas no âmbito de pesquisas aplicadas "
        "requerem diretrizes explícitas de transparência, reprodutibilidade e governança de dados. Em consonância com os "
        "preceitos da Design Science Research, o artefato preditivo deve ser projetado para permitir sua replicação independente, "
        "auditoria de código e integração contínua nos sistemas legados da organização parceira. A seguir, apresentam-se os "
        "parâmetros de escalabilidade técnica, as práticas de ciência aberta e os protocolos de governança que asseguram a "
        "sustentação do artefato em regime de produção."
    )),
    ("5.3 Resultados do torneio de modelos", (
        "A seleção do algoritmo preditivo mais aderente à dinâmica operacional da UAN escolar foi conduzida por meio de um "
        "torneio empírico entre múltiplas famílias de modelos, submetidos a um protocolo rigoroso de validação temporal sequencial. "
        "Para capturar as distintas janelas de tomada de decisão da gestão institucional, o torneio estruturou-se em dois horizontes "
        "temporais complementares: o horizonte de médio prazo (t+2), voltado às requisições de compras e abastecimento de estoque "
        "de secos, e o horizonte de curto prazo (t+1), direcionado ao planejamento diário de descongelamento, cocção e preparo de "
        "refeições. A seguir, detalha-se a metodologia experimental do torneio e comparam-se os desempenhos algorítmicos frente ao "
        "benchmark empírico da nutricionista gestora."
    )),
    ("5.5 Resultados das políticas de decisão", (
        "Embora o torneio algorítmico indique a superioridade estatística das técnicas lineares regularizadas na minimização "
        "de métricas simétricas de resíduo, a gestão da produção de refeições escolares opera sob uma função de custo assimétrica, "
        "na qual o desabastecimento discente acarreta penalidades sociais consideravelmente mais severas do que o custo gerencial "
        "de sobras de balcão. Diante dessa assimetria, a presente seção submete os resultados brutos dos modelos preditivos à camada "
        "de decisão do artefato, avaliando duas intervenções complementares: a combinação colaborativa sob a Fronteira Eficiente "
        "de Pareto — que integra o conhecimento empírico da nutricionista gestora e as saídas algorítmicas — e a determinação "
        "de margens de segurança conformal não paramétricas, estruturadas para assegurar a cobertura estocástica dos níveis de "
        "serviço desejados pela gestão institucional."
    )),
    ("5.7 Síntese dos resultados econômicos", (
        "Nesta seção final do capítulo, os achados teóricos e empíricos são consolidados sob a ótica gerencial da tomada de "
        "decisão em sistemas produtivos de serviços de alimentação. Estrutura-se uma simulação financeira hipotética fundamentada "
        "nas tarifas contratuais reais de faturamento da UAN escolar, confrontando os custos potenciais de sobras de matéria-prima "
        "com os níveis de proteção alimentar discente alcançados por cada política de dimensionamento. Por fim, definem-se com "
        "transparência metodológica os limites e a abrangência das evidências parciais reportadas na etapa de qualificação, "
        "consolidando o roteiro para a realização do teste retrospectivo com alvo oculto e a validação prospectiva em modo sombra "
        "a ser submetida no exame de defesa definitiva."
    ))
]

for key_prefix, texto in TEXTOS_SECOES:
    for i in range(len(doc.paragraphs) - 1):
        p = doc.paragraphs[i]
        # Limpar caracteres acentuados para matching robusto
        p_clean = p.text.replace("ã", "a").replace("ç", "c").replace("é", "e").replace("ó", "o").replace("í", "i").replace("ê", "e")
        key_clean = key_prefix.replace("ã", "a").replace("ç", "c").replace("é", "e").replace("ó", "o").replace("í", "i").replace("ê", "e")
        
        if key_clean.lower() in p_clean.lower() and p.style.name.startswith("Heading"):
            next_p = doc.paragraphs[i + 1]
            if next_p.style.name.startswith("Heading"):
                print(f"Inserindo texto conectivo para: {key_prefix}...")
                p_new = next_p.insert_paragraph_before()
                r = p_new.add_run(texto)
                r.font.color.rgb = RED_COLOR
                p_new.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                break

doc.save(DOCX_PATH)
print("Textos conectivos inseridos e docx salvo com sucesso!")
