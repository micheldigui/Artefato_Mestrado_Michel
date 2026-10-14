import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
for i in range(592, 608):
    p = doc.paragraphs[i]
    print(f"P{i:04d} [{p.style.name}]: {p.text.encode('ascii', errors='replace').decode()}")
