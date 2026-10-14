import docx

doc_m = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
for i in range(870, 895):
    print(f"P{i:04d}: {doc_m.paragraphs[i].text.encode('ascii', errors='replace').decode()[:80]}")
