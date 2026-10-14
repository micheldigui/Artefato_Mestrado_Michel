"""
Inspecionar diferencas de conteudo detalhadas entre Antigravity e Codex:
- No Capitulo 1
- No Capitulo 3
- No Capitulo 5
- No Capitulo 6
"""

import docx
import difflib

PATH_AG = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
PATH_CD = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_codex.docx"

doc_ag = docx.Document(PATH_AG)
doc_cd = docx.Document(PATH_CD)

def print_diff_section(sec_name, start_ag, end_ag, start_cd, end_cd):
    print(f"\n==========================================")
    print(f"=== DIFERENCAS NO {sec_name} ===")
    print(f"==========================================")
    
    p_ag = [p.text.strip() for p in doc_ag.paragraphs[start_ag:end_ag] if p.text.strip()]
    p_cd = [p.text.strip() for p in doc_cd.paragraphs[start_cd:end_cd] if p.text.strip()]
    
    matcher = difflib.SequenceMatcher(None, p_ag, p_cd)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            continue
        elif tag == 'replace':
            print(f"\n[SUBSTITUICAO] AG({i1}:{i2}) vs CD({j1}:{j2}):")
            for idx in range(i1, i2):
                print(f"  - AG: {p_ag[idx][:120]}...")
            for jdx in range(j1, j2):
                print(f"  + CD: {p_cd[jdx][:120]}...")
        elif tag == 'delete':
            print(f"\n[APENAS NO ANTIGRAVITY] AG({i1}:{i2}):")
            for idx in range(i1, i2):
                print(f"  - AG: {p_ag[idx][:120]}...")
        elif tag == 'insert':
            print(f"\n[APENAS NO CODEX] CD({j1}:{j2}):")
            for jdx in range(j1, j2):
                print(f"  + CD: {p_cd[jdx][:120]}...")

# 1 Introducao: AG P293 a P335, CD P293 a P335
print_diff_section("CAPITULO 1 (INTRODUCAO)", 293, 335, 293, 335)

# 6 Consideracoes Parciais: AG P834 a P841, CD P826 a P837
print_diff_section("CAPITULO 6 (CONSIDERACOES)", 834, 841, 826, 837)
