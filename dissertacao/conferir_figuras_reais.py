import os
import docx
import re
from PIL import Image

doc_path = r'f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_resultados_parciais_20261013_entrega.docx'
doc = docx.Document(doc_path)
media_dir = r'f:\PROJETOS\ARTEFATO\scratch_entrega_imgs\word\media'

part = doc.part
rels = part.rels

print("=== VERIFICANDO IMAGENS INSERIDAS EM FIGURAS 6, 16, 17, 24 ===")

def inspect_fig(fig_num):
    for i, p in enumerate(doc.paragraphs):
        txt = p.text.strip()
        m = re.match(r'^Figura\s+' + str(fig_num) + r'\s*[-–—:]\s*(.*)', txt, re.IGNORECASE)
        if m and i > 200:
            print(f"\n--- FIGURA {fig_num} (P{i}): {m.group(1)} ---")
            # achar imagem
            for off in range(1, 4):
                if i + off < len(doc.paragraphs):
                    cand = doc.paragraphs[i + off]
                    xml = cand._p.xml
                    if 'blip' in xml or 'graphic' in xml:
                        embed_m = re.findall(r'r:embed="([^"]+)"', xml)
                        if embed_m:
                            t_ref = rels[embed_m[0]].target_ref
                            img_fn = os.path.basename(t_ref)
                            img_fp = os.path.join(media_dir, img_fn)
                            if os.path.exists(img_fp):
                                im = Image.open(img_fp)
                                sz = os.path.getsize(img_fp)
                                print(f"Imagem: {img_fn} | Dimensoes: {im.size} | Formato: {im.format} | Tamanho: {sz} bytes")
                            break
            # achar texto logo apos fonte
            for off in range(1, 6):
                cand = doc.paragraphs[i + off]
                if cand.text.strip() and not cand.text.strip().lower().startswith('fonte') and not any(r in cand._p.xml for r in ['graphic', 'blip']):
                    print(f"Texto logo após: {cand.text.strip()[:140]}...")
                    break

for fn in [6, 16, 17, 18, 21, 22, 23, 24, 25, 26, 27, 28]:
    inspect_fig(fn)
