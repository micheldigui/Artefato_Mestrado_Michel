"""
Inspecionar as imagens embutidas no Codex e comparar seus hashes / tamanhos com as de Antigravity
"""

import docx
import zipfile
import os

PATH_AG = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
PATH_CD = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_codex.docx"

with zipfile.ZipFile(PATH_AG, 'r') as z_ag:
    ag_media = {f: len(z_ag.read(f)) for f in z_ag.namelist() if f.startswith('word/media/image')}

with zipfile.ZipFile(PATH_CD, 'r') as z_cd:
    cd_media = {f: len(z_cd.read(f)) for f in z_cd.namelist() if f.startswith('word/media/image')}

print("=== COMPARACAO DE TAMANHO DE IMAGENS (word/media/) ===")
for img_name in sorted(ag_media.keys()):
    sz_ag = ag_media.get(img_name, 0)
    sz_cd = cd_media.get(img_name, 0)
    diff = "IGUAL" if sz_ag == sz_cd else f"DIFERENTE (AG={sz_ag:,} vs CD={sz_cd:,})"
    print(f"{img_name}: {diff}")
