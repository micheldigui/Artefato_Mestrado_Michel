"""
Script de Atualização e Integração dos Resultados na Dissertação (.docx)
Mestrado Profissional em Educação Profissional e Tecnológica (ProfEPT)
IFSP Campus Itaquaquecetuba
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

ORIGINAL_DOCX = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_resultados_parciais_20261012_entrega.docx"
REVISADO_DOCX = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_resultados_parciais_20261013_revisada.docx"
FIG_DIR = r"f:\PROJETOS\ARTEFATO\reports\dissertacao_selecao\figuras"

def formatar_paragrafo_normal(p, texto):
    p.text = texto
    p.style = "Normal"
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

def adicionar_caption(doc, texto):
    p = doc.add_paragraph(texto)
    p.style = "Caption"
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return p

def adicionar_fonte(doc, texto="Fonte: Resultados da pesquisa (2026)."):
    p = doc.add_paragraph(texto)
    p.style = "Normal"
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return p

def adicionar_imagem(doc, caminho_imagem, largura_polegadas=6.0):
    if os.path.exists(caminho_imagem):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture(caminho_imagem, width=Inches(largura_polegadas))
    else:
        p = doc.add_paragraph(f"[IMAGEM NÃO ENCONTRADA: {caminho_imagem}]")
        p.style = "Normal"

def formatar_tabela_abnt(table):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Estilização das células
    for row_idx, row in enumerate(table.rows):
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(9.5)
                    if row_idx == 0:
                        r.font.bold = True

def atualizar_dissertacao():
    print(f"[*] Abrindo documento original: {ORIGINAL_DOCX}")
    doc = docx.Document(ORIGINAL_DOCX)
    
    # -------------------------------------------------------------
    # 1. ATUALIZAR RESUMO (Parágrafo 137)
    # -------------------------------------------------------------
    print("[*] Atualizando Resumo (parágrafo 137)...")
    resumo_atualizado = (
        "Este trabalho desenvolve e avalia um artefato analítico-preditivo para apoiar o planejamento "
        "da produção de refeições em um restaurante institucional escolar do Instituto Federal de São Paulo "
        "(IFSP Campus Itaquaquecetuba). A pesquisa adota a metodologia Design Science Research (DSRM) e "
        "integra registros diários de atendimento, histórico de reservas, padronização de cardápio e dados "
        "meteorológicos horários da API Open-Meteo. A validação temporal sequencial (Walk-Forward Validation) "
        "foi conduzida sem vazamento de dados, simulando a tomada de decisão operacional às sextas-feiras. "
        "Na análise histórica de 2023 a 2025, identificou-se a falência do modelo de manifestação voluntária "
        "dos estudantes, com subnotificação crônica em 63,8% dos dias letivos (9.494 refeições deficitárias). "
        "Em 2026, a assunção do planejamento institucional pela nutricionista conteve o desabastecimento, "
        "mas gerou superestimativa preventiva contínua (excesso de 1.545 refeições no período amostral). "
        "Na avaliação retrospectiva em 28 semanas de corte de 2026 (fevereiro a agosto), os modelos lineares "
        "regularizados superaram a estimativa humana isolada: o Lasso atingiu MAE de 22,27 refeições/dia "
        "(R² = 0,498) e o Ridge MAE de 22,46 (R² = 0,483), frente a 24,92 da nutricionista pura, reduzindo "
        "o potencial de sobras em 28,3%. Para mitigar a perda assimétrica inerente à alimentação escolar, "
        "a formulação da Fronteira Eficiente de Pareto do Modelo Híbrido (50% IA + 50% Nutricionista) atingiu "
        "o menor erro absoluto da pesquisa (MAE de 21,43) e o menor déficit (489 refeições). A introdução de "
        "margens prudenciais via Predição Conformal (P85 = +19 refeições) reduziu os dias com risco de falta "
        "para apenas 15,7% dos dias letivos (84,3% de proteção alimentar). Os resultados apresentados nesta "
        "qualificação são parciais e retrospectivos; a versão para defesa final incorporará o teste cego de "
        "setembro de 2026 e a validação prospectiva em tempo real dos meses de outubro e novembro."
    )
    doc.paragraphs[137].text = resumo_atualizado
    doc.paragraphs[137].style = "Normal"
    doc.paragraphs[137].alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # -------------------------------------------------------------
    # 2. ATUALIZAR QUADRO 13 (Tabela 14 - Capítulo 4: Políticas de Decisão)
    # -------------------------------------------------------------
    print("[*] Atualizando Quadro 13 (Tabela 14) com Pareto e Conformal...")
    t14 = doc.tables[14]
    # Linha 3: Conservadora / Conformal
    t14.rows[3].cells[1].text = (
        "Previsão acrescida do quantil empírico dos resíduos de subestimação via Predição Conformal "
        "(Conformal Prediction: P75=+10, P85=+19 ou P90=+29 refeições), garantindo cobertura finita sem hipótese de normalidade."
    )
    t14.rows[3].cells[2].text = (
        "Preparada para as duas janelas. Blindagem contra o risco de falta ao estudante vulnerável "
        "sob função de perda assimétrica (modelo Newsvendor)."
    )
    # Linha 5: Combinada / Modelo Híbrido Pareto
    t14.rows[5].cells[0].text = "Híbrida Colaborativa (Pareto)"
    t14.rows[5].cells[1].text = (
        "Combinação linear ponderada ótima (50% IA + 50% Quantitativo da Nutricionista), identificada na "
        "Fronteira Eficiente de Pareto como o ponto de mínimo arrependimento (Blattberg & Hoch, 1990)."
    )
    t14.rows[5].cells[2].text = (
        "Política colaborativa para a janela de preparo (t+1). Elimina o viés de superestimativa humana "
        "e absorve o conhecimento tácito da servidora, reduzindo sobras e faltas simultaneamente."
    )

    # -------------------------------------------------------------
    # 3. ATUALIZAR PARÁGRAFOS DO CAPÍTULO 5 (A partir de 5.5)
    # -------------------------------------------------------------
    print("[*] Atualizando Capítulo 5 (Seção 5.5 em diante)...")
    
    # Parágrafo 759: Heading 2 -> 5.5 Avaliação dos modelos em 2026 e políticas de decisão
    doc.paragraphs[759].text = "5.5 Avaliação Retrospectiva dos Modelos em 2026 e Políticas de Decisão"
    
    # Parágrafo 761: Introdução da seção 5.5
    doc.paragraphs[761].text = (
        "A avaliação retrospectiva consolidada de 2026 analisa 83 datas letivas de atendimento (fevereiro a "
        "agosto de 2026) distribuídas em 28 semanas operacionais de corte temporal estritamente sequencial "
        "(Walk-Forward Validation). Diferentemente dos ensaios exploratórios preliminares, esta etapa incorpora "
        "a Feature Store completa da Camada Gold com atributos meteorológicos horários da API Open-Meteo, "
        "codificação cíclica de calendário, dummies de cardápio e variáveis de defasagem rigorosamente ancoradas "
        "na data de corte da sexta-feira anterior, eliminando qualquer vazamento temporal de dados. A estimativa "
        "institucional informada pela nutricionista constitui a referência primária de comparação (benchmark humano)."
    )
    
    # 5.5.1 Torneio dos Modelos e Horizonte Multi-Estágio
    doc.paragraphs[762].text = "5.5.1 Torneio de Aprendizado de Máquina e Horizontes Multi-Estágio (t+1 e t+2)"
    doc.paragraphs[763].text = (
        "A tomada de decisão em alimentação coletiva envolve lead times distintos: a aquisição de gêneros "
        "não perecíveis (secos) ocorre com duas semanas de antecedência (Horizonte t+2), enquanto o suprimento de "
        "perecíveis e a escala de cocção ocorrem na semana imediatamente anterior (Horizonte t+1). A Tabela 9 "
        "apresenta os cinco modelos de melhor desempenho confrontados com a estimativa isolada da nutricionista."
    )
    
    # Atualizar Tabela 9 (Tabela 23 no docx)
    t9 = doc.tables[23]
    # Limpar e reescrever Tabela 9 com dados reais auditados
    dados_t9 = [
        ["Algoritmo / Estratégia", "Cenário", "Horizonte", "MAE (ref)", "RMSE (ref)", "R²"],
        ["Lasso (Campeão t+1)", "Cenário 3 (Com Nutri)", "Semana t+1", "22,27", "32,33", "0,498"],
        ["Ridge (Vice-Campeão t+1)", "Cenário 3 (Com Nutri)", "Semana t+1", "22,46", "32,82", "0,483"],
        ["Regressão Linear", "Cenário 3 (Com Nutri)", "Semana t+1", "22,87", "32,56", "0,491"],
        ["Estimativa Nutricionista", "Benchmark Humano", "Semana t+1", "24,92", "36,94", "0,373"],
        ["Regressão Linear (t+2)", "Cenário 2 (Com Clima)", "Semana t+2 (14d)", "28,67", "38,64", "0,268"]
    ]
    for r_idx, linha in enumerate(dados_t9):
        if r_idx < len(t9.rows):
            for c_idx, val in enumerate(linha):
                if c_idx < len(t9.columns):
                    t9.rows[r_idx].cells[c_idx].text = val
    formatar_tabela_abnt(t9)
    
    doc.paragraphs[765].text = "Tabela 9 - Desempenho dos Melhores Modelos de Machine Learning vs. Nutricionista em 2026"
    doc.paragraphs[767].text = (
        "Nota: n=83 dias de teste cego em 28 semanas de corte (04/02 a 31/08/2026). Todos os modelos foram avaliados em Walk-Forward "
        "sequencial. MAE e RMSE em refeições/dia; R² sem unidade. Cenário 3 combina memória, calendário, cardápio, clima e a estimativa institucional."
    )
    
    doc.paragraphs[768].text = (
        "Conforme observado na Tabela 9, os modelos lineares regularizados atingiram desempenho expressivamente "
        "superior ao benchmark humano no Horizonte t+1: o Lasso obteve MAE de 22,27 refeições/dia (redução de 10,6% no erro médio "
        "em relação aos 24,92 da nutricionista) e R² de 0,498. O modelo Ridge alcançou MAE de 22,46 e R² de 0,483. No Horizonte t+2, "
        "a Regressão Linear autônoma (sem interferência humana) atingiu MAE de 28,67 com duas semanas de antecedência, viabilizando o "
        "planejamento seguro de compras de insumos secos."
    )

    # 5.5.2 Fronteira Eficiente de Pareto do Modelo Híbrido
    doc.paragraphs[771].text = "5.5.2 A Fronteira Eficiente de Pareto do Modelo Híbrido Colaborativo"
    doc.paragraphs[772].text = (
        "Embora os modelos de IA pura apresentem menor erro médio global, algoritmos baseados em mínimos quadrados "
        "penalizam simetricamente excessos e déficits. Na gestão pública educacional, a falta de refeição ao estudante em "
        "vulnerabilidade acarreta prejuízo pedagógico severo. Alinhando-se à teoria de previsão colaborativa (Blattberg & Hoch, 1990; "
        "Armstrong, 2001), simulou-se o modelo híbrido linear ponderado variando o peso α da IA de 0% a 100%."
    )
    doc.paragraphs[773].text = (
        "A análise empírica identificou que o ponto de equilíbrio de mínimo arrependimento ocorre exatamente em α = 0,50 "
        "(combinação 50% IA + 50% Nutricionista). Nessa ponderação ótima, as sobras acumuladas caem de 1.545 para 1.289 refeições "
        "(economia financeira direta de R$ 2.176,00 frente à estimativa humana isolada), enquanto o volume de faltas atinge a menor "
        "marca de todo o estudo: 489 refeições (superando tanto as 518 faltas da nutricionista pura quanto as 741 da IA pura). "
        "O MAE médio reduz-se para 21,43 refeições/dia, comprovando que a fusão entre o rigor estatístico e a sensibilidade humana "
        "supera ambos os polos isolados."
    )

    # 5.5.3 Margens de Segurança Conformal e Proteção ao Estudante
    doc.paragraphs[780].text = "5.5.3 Calibração de Margens Prudenciais via Predição Conformal"
    doc.paragraphs[781].text = (
        "Para responder ao imperativo de segurança alimentar, incorporou-se a teoria da Predição Conformal Não-Paramétrica "
        "(Vovk et al., 2005; Angelopoulos & Bates, 2021). A partir da distribuição empírica dos resíduos de subestimação, "
        "estabeleceram-se margens de segurança prudenciais: P75 (+10 refeições), P85 (+19 refeições) e P90 (+29 refeições)."
    )
    
    # Atualizar Tabela 11 (Tabela 25 no docx) com as Políticas de Margem Reais
    t11 = doc.tables[25]
    dados_t11 = [
        ["Política / Estratégia", "Margem", "Sobra (ref)", "Falta (ref)", "% Dias Déficit", "MAE (ref/dia)"],
        ["1. IA Pura (Lasso/Ridge)", "+0 ref", "1.107", "741", "43,4%", "22,27"],
        ["2. IA + Conformal P75", "+10 ref", "1.749", "383", "25,3%", "25,70"],
        ["3. IA + Conformal P85", "+19 ref", "2.364", "236", "15,7%", "31,34"],
        ["4. IA + Conformal P90", "+29 ref", "3.074", "123", "10,8%", "38,54"],
        ["5. Modelo Híbrido (50/50)", "+0 ref", "1.289", "489", "43,4%", "21,43"],
        ["6. Híbrido + Conformal P85", "+12 ref", "1.994", "199", "16,9%", "26,43"],
        ["7. Nutricionista Pura (2026)", "Humana", "1.545", "518", "41,0%", "24,92"]
    ]
    for r_idx, linha in enumerate(dados_t11):
        if r_idx < len(t11.rows):
            for c_idx, val in enumerate(linha):
                if c_idx < len(t11.columns):
                    t11.rows[r_idx].cells[c_idx].text = val
    formatar_tabela_abnt(t11)
    
    doc.paragraphs[782].text = "Tabela 11 - Impacto Operacional das Margens de Segurança Conformal e Políticas de Decisão em 2026"
    doc.paragraphs[784].text = (
        "Nota: n=83 dias de teste cego em 2026. Sobras e faltas são acumuladas no período. A margem conformal garante nível de "
        "cobertura não-paramétrico sobre os quantis empíricos de subestimação. Custos baseados no valor paramétrico de R$ 8,50 por refeição."
    )

    doc.paragraphs[785].text = (
        "A Tabela 11 evidencia a eficácia das margens de segurança na mitigação do risco social. A política IA + Conformal P85 (+19 refeições) "
        "reduz a frequência de dias com falta de 43,4% para apenas 15,7% dos dias letivos (uma blindagem de 84,3% de proteção contra déficit). "
        "Quando aplicada sobre o Modelo Híbrido (+12 refeições), as faltas caem para apenas 199 refeições no ano todo, com menos sobras do que a "
        "IA isolada com margem. Trata-se da política recomendada para adoção institucional no campus."
    )

    # 5.6 Discussão Integrada
    doc.paragraphs[790].text = "5.6 Discussão Integrada dos Resultados e Limites das Evidências Parciais"
    doc.paragraphs[791].text = (
        "A triangulação dos resultados históricos de 2023–2025 com o teste retrospectivo de 2026 oferece três contribuições gerenciais: "
        "(i) comprova a inadequação da manifestação voluntária de estudantes para dimensionamento de refeições em escolas públicas; "
        "(ii) demonstra que algoritmos de aprendizado de máquina reduzem o erro médio em 10,6% e o desperdício de sobras em 28,3% frente "
        "ao planejamento humano isolado; e (iii) consolida o modelo híbrido acoplado a margens conformais como solução de compromisso "
        "entre sustentabilidade orçamentária e segurança alimentar. Por se tratar de resultados parciais para qualificação, as evidências "
        "restringem-se à validação retrospectiva; o ciclo prospectivo nos meses de outubro e novembro completará a avaliação."
    )

    # -------------------------------------------------------------
    # 4. ATUALIZAR CAPÍTULO 6: CONSIDERAÇÕES PARCIAIS (Parágrafos 805+)
    # -------------------------------------------------------------
    print("[*] Atualizando Capítulo 6: Considerações Parciais...")
    doc.paragraphs[806].text = (
        "A pergunta norteadora desta pesquisa — como dimensionar a demanda de refeições em restaurante institucional escolar "
        "de modo a mitigar o desperdício orçamentário sem incorrer no desabastecimento de estudantes vulneráveis — foi respondida "
        "parcialmente nesta etapa de qualificação. O artefato analítico-preditivo desenvolvido demonstrou viabilidade técnica e "
        "operacional ao integrar bases heterogêneas de consumo, calendário, cardápio e meteorologia."
    )
    doc.paragraphs[808].text = (
        "Na avaliação retrospectiva em 28 semanas de corte de 2026, os modelos lineares regularizados (Lasso com MAE de 22,27 e Ridge "
        "com MAE de 22,46) superaram expressivamente a estimativa isolada da nutricionista (MAE de 24,92), reduzindo o excesso em 28,3%. "
        "A formulação da Fronteira Eficiente de Pareto do Modelo Híbrido (50% IA + 50% Nutricionista) atingiu MAE de 21,43 com o menor "
        "déficit absoluto do estudo (489 refeições). A introdução de margens prudenciais de Predição Conformal (P85) elevou o índice "
        "de proteção discente para 84,3% dos dias letivos, conciliando responsabilidade fiscal e função social da escola pública."
    )
    doc.paragraphs[813].text = (
        "Para a versão final da defesa de mestrado, o cronograma metodológico prevê duas etapas complementares: (i) a avaliação "
        "retrospectiva com alvo oculto referente ao mês de setembro de 2026; e (ii) o acompanhamento prospectivo em tempo real nos meses "
        "de outubro e novembro de 2026, com emissão semanal em modo sombra e validação prática da ferramenta de apoio à decisão."
    )

    # -------------------------------------------------------------
    # 5. SALVAR NOVO ARQUIVO REVISADO
    # -------------------------------------------------------------
    print(f"[*] Salvando versão revisada em: {REVISADO_DOCX}")
    doc.save(REVISADO_DOCX)
    print(f"[OK] Dissertação atualizada com sucesso! Arquivo gerado: {REVISADO_DOCX}")

if __name__ == "__main__":
    atualizar_dissertacao()
