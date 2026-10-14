import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
for i, p in enumerate(doc.paragraphs[330:435]):
    actual_i = 330 + i
    if p.style.name.startswith("Heading"):
        print(f"P{actual_i:04d} [{p.style.name}]: {p.text}")
