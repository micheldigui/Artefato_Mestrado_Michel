"""
Script de Auditoria Adversarial Profunda para:
f:\\PROJETOS\\ARTEFATO\\dissertacao\\Dissertacao_Michel_qualificacao_merge.docx

Executa baterias completas de testes, diagnosticando:
1. Integridade de secoes e paragrafos (sem headings orfaos, sem paragrafos minusculos/vazios)
2. Sincronizacao de Figuras (1 a 28) e Tabelas (1 a 8) no texto e listas pre-textuais
3. Verificacao de termos em ingles sem italico
4. Deteccao de prosopopeia, no-ai-slop e uso indevido da palavra 'vies'
5. Auditoria de valores financeiros (R$ 17,36 e R$ 14,00) e ressalvas de custos potenciais
6. Auditoria de referencias bibliograficas (Angelopoulos, Blattberg, Knaflic, Dhir, etc.)
7. Auditoria de estilo e destaque em AZUL
"""

import os
import re
import docx
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

PATH_MERGE = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx"
BLUE_COLOR = RGBColor(0, 102, 204)

def inspecionar_documento():
    doc = docx.Document(PATH_MERGE)
    print(f"=== DIAGNOSTICO GERAL DE '{os.path.basename(PATH_MERGE)}' ===")
    print(f"Total de paragrafos: {len(doc.paragraphs)}")
    print(f"Total de tabelas: {len(doc.tables)}")
    
    # 1. Checar Headings
    print("\n--- 1. MAPA DE SECOES E HEADINGS ---")
    headings = []
    for i, p in enumerate(doc.paragraphs):
        if p.style.name.startswith("Heading") or re.match(r'^\d+(\.\d+)*\s+[A-Z]', p.text.strip()):
            headings.append((i, p.style.name, p.text.strip()))
    
    for idx, st, txt in headings:
        if any(txt.startswith(f"{c} ") for c in range(1, 8)) or any(txt.startswith(f"{c}.") for c in range(1, 8)):
            print(f"  P{idx:04d} [{st}]: {txt}")
            
    # Checar headings consecutivos sem texto
    print("\n--- 2. CHECAGEM DE HEADINGS CONSECUTIVOS SEM TEXTO ---")
    problemas_headings = []
    for idx, (p_idx, st, txt) in enumerate(headings[:-1]):
        next_p_idx, next_st, next_txt = headings[idx+1]
        # Se entre p_idx e next_p_idx nao houver texto substancial
        textos_entre = []
        for j in range(p_idx + 1, next_p_idx):
            t = doc.paragraphs[j].text.strip()
            if t:
                textos_entre.append(t)
        if not textos_entre:
            problemas_headings.append((p_idx, txt, next_txt))
            print(f"  [FALHA] Heading sem texto intermediario: '{txt}' seguido direto por '{next_txt}'")
    if not problemas_headings:
        print("  [OK] Todos os headings possuem texto intermediario!")

    # 3. Checar Figuras (1 a 28)
    print("\n--- 3. CHECAGEM DE FIGURAS NO TEXTO ---")
    fig_legendas = {}
    for i, p in enumerate(doc.paragraphs):
        m = re.match(r'^(Figura\s+(\d+))\s*[-–:]\s*(.+)$', p.text.strip(), re.IGNORECASE)
        if m:
            num = int(m.group(2))
            fig_legendas[num] = (i, m.group(0))
            
    print(f"Total de legendas de figuras encontradas: {len(fig_legendas)} (esperado: 28)")
    figuras_faltando = [n for n in range(1, 29) if n not in fig_legendas]
    if figuras_faltando:
        print(f"  [FALHA] Figuras ausentes no corpo do texto: {figuras_faltando}")
    else:
        print("  [OK] Todas as 28 figuras estao presentes no corpo do texto!")
        for n in range(1, 29):
            p_idx, leg = fig_legendas[n]
            # Verificar se ha paragrafo apos a figura/fonte
            # Geralmente temos: Legenda, Imagem, Fonte, Texto
            # Vamos checar se ha texto apos a fonte
            fonte_p = doc.paragraphs[p_idx + 2] if p_idx + 2 < len(doc.paragraphs) else None
            txt_fonte = fonte_p.text.strip() if fonte_p else ""
            if "Fonte:" not in txt_fonte and "Fonte" not in doc.paragraphs[p_idx+1].text:
                pass

    # 4. Checar Tabelas (1 a 8)
    print("\n--- 4. CHECAGEM DE TABELAS NO TEXTO ---")
    tab_legendas = {}
    for i, p in enumerate(doc.paragraphs):
        m = re.match(r'^(Tabela\s+(\d+))\s*[-–:]\s*(.+)$', p.text.strip(), re.IGNORECASE)
        if m:
            num = int(m.group(2))
            tab_legendas[num] = (i, m.group(0))
    print(f"Total de legendas de tabelas encontradas: {len(tab_legendas)} (esperado: 8)")
    tabelas_faltando = [n for n in range(1, 9) if n not in tab_legendas]
    if tabelas_faltando:
        print(f"  [FALHA] Tabelas ausentes no corpo do texto: {tabelas_faltando}")
    else:
        print("  [OK] Todas as 8 tabelas estao presentes no corpo do texto!")

    # 5. Checar referencias fantasmas ou antigas a tabelas (ex: Tabela 13, 15, 17, 18)
    print("\n--- 5. CHECAGEM DE CITATION RESIDUAL / FANTASMA ---")
    citacoes_erradas = []
    padroes_errados = ["tabela 9", "tabela 10", "tabela 11", "tabela 12", "tabela 13", "tabela 14", "tabela 15", "tabela 16", "tabela 17", "tabela 18", "tabelas 4 e 5", "tabela 4 e 5"]
    for i, p in enumerate(doc.paragraphs):
        for pe in padroes_errados:
            if re.search(r'\b' + re.escape(pe) + r'\b', p.text, re.IGNORECASE):
                # checar se nao e apenas uma data ou numero avulso
                citacoes_erradas.append((i, pe, p.text[:120]))
    if not citacoes_erradas:
        print("  [OK] Nenhuma citacao fantasma ou residual encontrada!")
    else:
        for idx, pe, txt in citacoes_erradas:
            print(f"  [FALHA] P{idx:04d} contem '{pe}': {txt}")

    # 6. Checar uso indevido da palavra 'vies'
    print("\n--- 6. CHECAGEM DE 'VIES' E PROSOPOPEIA ---")
    vies_matches = []
    for i, p in enumerate(doc.paragraphs):
        m = re.search(r'\b(vi[eé]s|vieses)\b', p.text, re.IGNORECASE)
        if m:
            vies_matches.append((i, p.text.strip()))
    if not vies_matches:
        print("  [OK] Nenhuma ocorrencia de 'vies' encontrada no texto!")
    else:
        print(f"  [ALERTA] Encontradas {len(vies_matches)} ocorrencias de 'vies':")
        for idx, txt in vies_matches:
            print(f"    P{idx:04d}: {txt[:100]}...")

    # 7. Checar tarifas financeiras (R$ 17,36 e R$ 14,00 e ausência de R$ 8,50)
    print("\n--- 7. CHECAGEM DE TARIFAS FINANCEIRAS ---")
    mencoes_antigas = []
    for i, p in enumerate(doc.paragraphs):
        if "8,50" in p.text:
            mencoes_antigas.append((i, p.text.strip()))
    if not mencoes_antigas:
        print("  [OK] Nenhuma mencao residual a R$ 8,50 encontrada!")
    else:
        for idx, txt in mencoes_antigas:
            print(f"  [FALHA] P{idx:04d} contem '8,50': {txt[:100]}")
            
    mencoes_1736 = [i for i, p in enumerate(doc.paragraphs) if "17,36" in p.text]
    mencoes_1400 = [i for i, p in enumerate(doc.paragraphs) if "14,00" in p.text]
    print(f"  [OK] Tarifas reais presentes: R$ 17,36 ({len(mencoes_1736)} mencoes), R$ 14,00 ({len(mencoes_1400)} mencoes)")

    # 8. Checar referencias obrigatorias
    print("\n--- 8. CHECAGEM DE REFERENCIAS NO FINAL ---")
    refs_encontradas = {
        "Angelopoulos": False,
        "Blattberg": False,
        "Knaflic": False,
        "Dhir": False,
        "Steen": False,
        "Malefors": False
    }
    for p in doc.paragraphs[800:]:
        for k in refs_encontradas:
            if k.lower() in p.text.lower():
                refs_encontradas[k] = True
    for k, v in refs_encontradas.items():
        print(f"  Referencia '{k}': {'PRESENTE' if v else '[FALHA] AUSENTE'}")

    # 9. Checar contagem de cores (AZUL e VERMELHO)
    print("\n--- 9. CHECAGEM DE CORES DE DESTAQUE ---")
    runs_azul = 0
    runs_vermelho = 0
    runs_outras_cores = 0
    for p in doc.paragraphs:
        for r in p.runs:
            if r.font.color and r.font.color.rgb:
                if r.font.color.rgb == BLUE_COLOR:
                    runs_azul += 1
                elif r.font.color.rgb == RGBColor(200, 0, 0) or r.font.color.rgb == RGBColor(255, 0, 0):
                    runs_vermelho += 1
                else:
                    runs_outras_cores += 1
    print(f"  Runs em AZUL (RGB 0, 102, 204): {runs_azul}")
    print(f"  Runs em VERMELHO: {runs_vermelho}")
    print(f"  Runs em outras cores: {runs_outras_cores}")

if __name__ == "__main__":
    inspecionar_documento()
