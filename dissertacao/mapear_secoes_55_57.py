import docx

doc_path = r'f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_resultados_parciais_20261013_entrega.docx'
doc = docx.Document(doc_path)

with open('conferir_secoes_55_56_57.txt', 'w', encoding='utf-8') as f:
    for i in range(750, 835):
        f.write(f"[P{i}] {doc.paragraphs[i].text}\n")

print("Seções 5.5, 5.6 e 5.7 mapeadas com sucesso!")
