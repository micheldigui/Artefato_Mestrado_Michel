import docx
import re

doc = docx.Document(r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_merge.docx")
for i, p in enumerate(doc.paragraphs):
    m = re.match(r'^(Figura\s+([1-4]))\s*[-–:]\s*(.+)$', p.text.strip(), re.IGNORECASE)
    if m:
        print(f"P{i:04d}: {m.group(0)}")
