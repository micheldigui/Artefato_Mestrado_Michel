import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
print("Texto de P0586:")
print(doc.paragraphs[586].text.encode('ascii', errors='replace').decode())
