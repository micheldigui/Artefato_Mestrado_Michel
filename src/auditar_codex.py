"""
Raio-X minucioso comparando Antigravity e Codex em todas as dimensoes:
- Imagens embutidas
- Tabelas e precos (R$ 8,50 vs R$ 14,00 / R$ 17,36)
- Referencias bibliograficas
- Ocorrencias de vies
- Chamadas de tabelas
- Estrutura textual
"""

import docx

PATH_AG = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
PATH_CD = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_codex.docx"

doc_ag = docx.Document(PATH_AG)
doc_cd = docx.Document(PATH_CD)

print("=== 1. IMAGENS NO CODEX ===")
# Verificar imagens no Codex
imgs_cd = []
for p in doc_cd.paragraphs:
    for r in p.runs:
        blips = r._element.xpath('.//a:blip/@r:embed')
        if blips:
            rId = blips[0]
            target = doc_cd.part.rels[rId].target_ref
            imgs_cd.append(target)
print(f"Total de imagens no Codex: {len(imgs_cd)}")

print("\n=== 2. AUDITORIA FINANCEIRA NO CODEX ===")
mencoes_850_cd = [p.text for p in doc_cd.paragraphs if "8,50" in p.text]
print(f"Mencoes a '8,50' no Codex: {len(mencoes_850_cd)}")
for m in mencoes_850_cd:
    print("  CD:", m[:100])

mencoes_1400_cd = [p.text for p in doc_cd.paragraphs if "14,00" in p.text]
print(f"Mencoes a '14,00' no Codex: {len(mencoes_1400_cd)}")

mencoes_1736_cd = [p.text for p in doc_cd.paragraphs if "17,36" in p.text]
print(f"Mencoes a '17,36' no Codex: {len(mencoes_1736_cd)}")

# Verificar Tabela 8 no Codex
t8_cd = doc_cd.tables[23]
print("\nTabela 8 no Codex:")
for row in t8_cd.rows:
    print(" ", [c.text.replace('\n', ' ').strip() for c in row.cells])

print("\n=== 3. AUDITORIA DE REFERENCIAS NO CODEX ===")
refs_cd = [p.text for p in doc_cd.paragraphs[820:] if any(a in p.text.lower() for a in ['angelopoulos', 'blattberg', 'knaflic'])]
print(f"Referencias encontradas no Codex: {len(refs_cd)}")
for r in refs_cd:
    print("  CD Ref:", r[:80])

print("\n=== 4. AUDITORIA DE VIES NO CODEX ===")
vies_cd = [p.text for p in doc_cd.paragraphs if "viés" in p.text.lower() or "vies" in p.text.lower()]
print(f"Ocorrencias de vies no Codex: {len(vies_cd)}")
for v in vies_cd[:5]:
    print("  CD Vies:", v[:90])

print("\n=== 5. AUDITORIA DE CHAMADAS DE TABELAS NO CODEX ===")
chamadas_tabelas_cd = []
for p in doc_cd.paragraphs:
    for t_err in ["Tabela 13", "Tabela 15", "Tabela 17", "Tabela 18"]:
        if t_err.lower() in p.text.lower():
            chamadas_tabelas_cd.append((t_err, p.text[:80]))
print(f"Chamadas erradas de tabelas no Codex: {len(chamadas_tabelas_cd)}")
for t_err, txt in chamadas_tabelas_cd:
    print(f"  CD {t_err}: {txt}")
