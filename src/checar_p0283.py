import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
txt_procurar = "As simulações de políticas usam 83 datas pareadas"
for i, p in enumerate(doc.paragraphs):
    if txt_procurar in p.text:
        print(f"P{i:04d} [{p.style.name}]: {p.text[:100]}")
