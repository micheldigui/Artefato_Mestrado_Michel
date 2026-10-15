import json
import docx

with open('auditoria_elementos_completos.json', 'r', encoding='utf-8') as f:
    rep = json.load(f)

print("=== TABELAS MAPEADAS NO CORPO DO TEXTO ===")
for t in rep['tabelas']:
    print(f"P{t['p_idx']}: Tabela {t['num']} - {t['title']}")

print("\n=== QUADROS MAPEADOS NO CORPO DO TEXTO ===")
for q in rep['quadros']:
    print(f"P{q['p_idx']}: Quadro {q['num']} - {q['title']}")

print("\n=== FIGURAS MAPEADAS NO CORPO DO TEXTO (AMOSTRA 16 A 25) ===")
for fig in rep['figuras']:
    if fig['num'] in [6, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]:
        print(f"P{fig['p_idx']}: Figura {fig['num']} - {fig['title']} | Imagem: {fig['img_file']}")
