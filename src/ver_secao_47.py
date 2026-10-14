import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
for i in range(575, 592):
    print(f"P{i:04d}: {doc.paragraphs[i].text}")
