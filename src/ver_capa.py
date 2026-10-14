import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
for i in range(15):
    t = doc.paragraphs[i].text.strip()
    if t:
        print(f"P{i:02d}: {t}")
