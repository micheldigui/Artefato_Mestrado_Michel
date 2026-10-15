import json

p = r'f:\PROJETOS\ARTEFATO\notebooks\03_analise_exploratoria_eda.ipynb'
with open(p, 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open(r'f:\PROJETOS\ARTEFATO\dissertacao\auditoria_nb03_eda.txt', 'w', encoding='utf-8') as out:
    for idx, cell in enumerate(nb['cells']):
        src = ''.join(cell.get('source', []))
        if any(k in src.lower() for k in ['dia_semana', 'dia_da_semana', 'proteina', 'preparo', 'chuva', 'precipitacao', 'temperatura', 'autocorrelacao', 'acf', 'pearson', 'spearman', 'ano']):
            out.write(f"=== CÉLULA {idx} ({cell.get('cell_type')}) ===\n")
            out.write(src + "\n\n")
            # outputs se houver texto
            outputs = cell.get('outputs', [])
            for o in outputs:
                if 'text' in o:
                    out.write("[OUTPUT TEXT]:\n" + "".join(o['text']) + "\n")
            out.write("="*80 + "\n\n")

print("Notebook 03 inspecionado com sucesso!")
