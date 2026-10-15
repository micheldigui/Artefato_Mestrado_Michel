import docx

doc = docx.Document(r'f:\PROJETOS\ARTEFATO\dissertacao\bck_dissertacao\Dissertacao_Michel_qualificacao_merge.docx')

with open('secao55_detalhe.txt', 'w', encoding='utf-8') as f:
    for i in range(765, 815):
        f.write(f"[P{i}] {doc.paragraphs[i].text}\n")

print("Seção 5.5 mapeada com sucesso!")
