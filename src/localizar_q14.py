import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
for i, p in enumerate(doc.paragraphs[570:600]):
    actual_i = 570 + i
    if "Quadro 14 distingue" in p.text:
        print(f"P{actual_i:04d}: {p.text.encode('ascii', errors='replace').decode()}")
