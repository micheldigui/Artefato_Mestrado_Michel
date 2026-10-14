"""
Inspecionar tabelas no Codex
"""
import docx

doc_cd = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_codex.docx")
for idx in [5, 11, 18, 19, 20, 21, 22, 23]:
    t = doc_cd.tables[idx]
    r1 = [c.text.replace("\n", " ").strip() for c in t.rows[0].cells[:4]]
    print(f"Table {idx:02d} ({len(t.rows)}x{len(t.columns)}): {r1}")
