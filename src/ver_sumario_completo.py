import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")

print("=== SUMARIO ATUAL NO ARQUIVO MERGE ===")
for i in range(215, 292):
    p = doc.paragraphs[i]
    t = p.text.strip()
    if t:
        print(f"P{i:04d} [{p.style.name}]: {t.encode('ascii', errors='replace').decode()}")
