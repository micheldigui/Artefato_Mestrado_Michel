import zipfile
import os
import shutil

docx_path = r'f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_resultados_parciais_20261013_entrega.docx'
out_dir = r'f:\PROJETOS\ARTEFATO\scratch_entrega_imgs'

if os.path.exists(out_dir):
    shutil.rmtree(out_dir)
os.makedirs(out_dir, exist_ok=True)

with zipfile.ZipFile(docx_path, 'r') as z:
    media_files = [f for f in z.namelist() if f.startswith('word/media/')]
    print(f"Total de arquivos de mídia encontrados no docx: {len(media_files)}")
    for f in media_files:
        z.extract(f, out_dir)

# Listar imagens extraídas
extracted_media = os.listdir(os.path.join(out_dir, 'word', 'media'))
print(f"Total de imagens extraídas: {len(extracted_media)}")
for m in sorted(extracted_media):
    size = os.path.getsize(os.path.join(out_dir, 'word', 'media', m))
    print(f"   {m} ({size} bytes)")
