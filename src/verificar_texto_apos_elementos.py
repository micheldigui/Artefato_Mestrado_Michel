import docx

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")

print("=== VERIFICANDO SE HA TEXTO APOS CADA FIGURA, QUADRO E TABELA ===")

total_elementos = 0
elementos_sem_texto_apos = []

for i, p in enumerate(doc.paragraphs[293:]):
    actual_i = 293 + i
    txt = p.text.strip()
    
    # Se for uma legenda de Figura, Quadro ou Tabela
    is_legenda = False
    tipo = None
    if txt.startswith("Figura ") and ("-" in txt or ":" in txt):
        is_legenda = True
        tipo = "Figura"
    elif txt.startswith("Quadro ") and ("-" in txt or ":" in txt):
        is_legenda = True
        tipo = "Quadro"
    elif txt.startswith("Tabela ") and ("-" in txt or ":" in txt):
        is_legenda = True
        tipo = "Tabela"
        
    if is_legenda:
        total_elementos += 1
        # Vamos avancar para passar a imagem/tabela e a "Fonte:"
        # Apos a fonte, deve haver um paragrafo de texto corrido antes do proximo Heading
        j = actual_i + 1
        achou_fonte = False
        achou_texto_apos = False
        proximo_heading = False
        
        while j < len(doc.paragraphs):
            pj = doc.paragraphs[j]
            t = pj.text.strip()
            
            if pj.style.name.startswith("Heading"):
                proximo_heading = True
                break
                
            if "Fonte:" in t or "Fonte" in t:
                achou_fonte = True
                # O proximo paragrafo com texto substancial deve ser texto analitico
                k = j + 1
                while k < len(doc.paragraphs):
                    pk = doc.paragraphs[k]
                    tk = pk.text.strip()
                    if pk.style.name.startswith("Heading"):
                        break
                    if tk and not tk.startswith("Figura ") and not tk.startswith("Tabela ") and not tk.startswith("Quadro "):
                        achou_texto_apos = True
                        break
                    k += 1
                break
            j += 1
            
        if not achou_texto_apos:
            elementos_sem_texto_apos.append((actual_i, txt))
            print(f"  [ALERTA] P{actual_i:04d} '{txt[:60]}' SEM texto apos a fonte antes do proximo heading!")

if not elementos_sem_texto_apos:
    print(f"\n[SUCESSO] Todos os {total_elementos} elementos visuais possuem texto explicativo logo apos!")
else:
    print(f"\n[FALHAS] {len(elementos_sem_texto_apos)} elementos visuais estao sem texto apos.")
