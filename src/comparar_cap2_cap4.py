"""
Comparar paragrafos do Capitulo 2, 3 e 4 para encontrar melhorias textuais do Codex
"""

import docx
import difflib

PATH_AG = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
PATH_CD = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_codex.docx"

doc_ag = docx.Document(PATH_AG)
doc_cd = docx.Document(PATH_CD)

def comparar_intervalo(nome, p_start_ag, p_end_ag, p_start_cd, p_end_cd):
    print(f"\n=== COMPARANDO {nome} ===")
    t_ag = [p.text.strip() for p in doc_ag.paragraphs[p_start_ag:p_end_ag] if p.text.strip()]
    t_cd = [p.text.strip() for p in doc_cd.paragraphs[p_start_cd:p_end_cd] if p.text.strip()]
    
    diffs = 0
    matcher = difflib.SequenceMatcher(None, t_ag, t_cd)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag != 'equal':
            diffs += 1
            print(f"\nDiff #{diffs} [{tag}]:")
            for idx in range(i1, min(i1+2, i2)):
                print(f"  AG: {t_ag[idx][:100]}...")
            for jdx in range(j1, min(j1+2, j2)):
                print(f"  CD: {t_cd[jdx][:100]}...")
    if diffs == 0:
        print("100% IDENTICOS!")

# Cap 2: AG 328 a 431, CD 328 a 431
comparar_intervalo("CAPITULO 2 (FUNDAMENTACAO TEORICA)", 328, 431, 328, 431)

# Cap 4: AG 540 a 591, CD 540 a 591
comparar_intervalo("CAPITULO 4 (MODELO SISTEMICO)", 540, 591, 540, 591)
