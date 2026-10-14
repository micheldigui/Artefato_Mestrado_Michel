"""
Script para comparacao textual aprofundada entre Antigravity e Codex por secao.
Gera relatorio detalhado destacando contribuicoes unicas de cada versao.
"""

import docx
import difflib

PATH_AG = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
PATH_CD = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_codex.docx"

doc_ag = docx.Document(PATH_AG)
doc_cd = docx.Document(PATH_CD)

def extrair_secoes(doc):
    secoes = {}
    current_sec = "PRE-TEXTUAL"
    secoes[current_sec] = []
    
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if p.style.name.startswith("Heading 1"):
            current_sec = t
            secoes[current_sec] = []
        elif p.style.name.startswith("Heading 2") or p.style.name.startswith("Heading 3"):
            secoes[current_sec].append((i, "HEADING", t))
        else:
            if t:
                secoes[current_sec].append((i, "TEXT", t))
                
    return secoes

secoes_ag = extrair_secoes(doc_ag)
secoes_cd = extrair_secoes(doc_cd)

print("=== CAPITULOS IDENTIFICADOS ===")
print("AG:", list(secoes_ag.keys()))
print("CD:", list(secoes_cd.keys()))

print("\n=== COMPARACAO CAPITULO A CAPITULO ===")
for sec in secoes_ag.keys():
    if sec not in secoes_cd:
        print(f"Secao '{sec}' presente apenas no Antigravity!")
        continue
        
    items_ag = secoes_ag[sec]
    items_cd = secoes_cd[sec]
    
    text_ag = "\n".join([t for _, tipo, t in items_ag if tipo == "TEXT"])
    text_cd = "\n".join([t for _, tipo, t in items_cd if tipo == "TEXT"])
    
    words_ag = len(text_ag.split())
    words_cd = len(text_cd.split())
    
    sim = difflib.SequenceMatcher(None, text_ag, text_cd).ratio()
    print(f"\n[{sec}]")
    print(f"  Palavras: AG={words_ag:,} | CD={words_cd:,} | Similaridade={sim*100:.1f}%")
    
    if sim < 0.98:
        # Mostrar diferencas resumidas
        diff_lines = list(difflib.unified_diff(
            text_ag.splitlines()[:15],
            text_cd.splitlines()[:15],
            fromfile="Antigravity",
            tofile="Codex",
            lineterm=""
        ))
        if diff_lines:
            print("  Primeiras diferencas encontradas:")
            for l in diff_lines[:8]:
                print("   ", l[:100])
