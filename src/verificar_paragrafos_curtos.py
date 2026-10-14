import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")

print("=== VERIFICANDO PARAGRAFOS CURTOS NO CORPO DO TEXTO ===")
paragrafos_curtos = []

for i in range(293, 840):
    p = doc.paragraphs[i]
    txt = p.text.strip()
    if not txt:
        continue
    if p.style.name.startswith("Heading"):
        continue
    if txt.startswith("Figura ") or txt.startswith("Tabela ") or txt.startswith("Quadro ") or txt.startswith("Fonte:"):
        continue
    if txt.startswith("a)") or txt.startswith("b)") or txt.startswith("c)") or txt.startswith("d)") or txt.startswith("e)"):
        continue
    if txt.startswith("1.") or txt.startswith("2.") or txt.startswith("3.") or txt.startswith("4.") or txt.startswith("5."):
        continue
        
    palavras = len(txt.split())
    if palavras < 20:
        paragrafos_curtos.append((i, palavras, txt))

if not paragrafos_curtos:
    print("[SUCESSO] Nenhum paragrafo corrido no corpo tem menos de 20 palavras!")
else:
    print(f"Encontrados {len(paragrafos_curtos)} paragrafos curtos (< 20 palavras):")
    for idx, cnt, t in paragrafos_curtos:
        print(f"  P{idx:04d} ({cnt} palavras): {t}")
