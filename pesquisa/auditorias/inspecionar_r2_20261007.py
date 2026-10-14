from pathlib import Path
import json, re
import pdfplumber
from lxml import etree
import zipfile

root=Path(r'F:\PRODUTO_MESTRADO')
out=root/'pesquisa/auditorias/r2_20261007'
out.mkdir(parents=True,exist_ok=True)
sources={}
for file in (root/'pesquisa').glob('*.pdf'):
    if 'catboost' in file.name.lower(): continue
    with pdfplumber.open(file) as pdf:
        pages=[p.extract_text() or '' for p in pdf.pages]
    sources[file.name]={'pages':len(pages),'text':pages}
    (out/(file.stem+'.txt')).write_text('\n\n'.join(f'PÁGINA PDF {i+1}\n{t}' for i,t in enumerate(pages)),encoding='utf-8')
    print('\n',file.name)
    for i,t in enumerate(pages):
        if re.search(r'0\.2|holdout|SQUARING|squaring|2\.7|predictive accuracy',t):
            print('PÁGINA',i+1, ' '.join(t.split())[:900])
(out/'pdfs_extraidos.json').write_text(json.dumps(sources,ensure_ascii=False),encoding='utf-8')
with zipfile.ZipFile(root/'dissertacao/Dissertacao_Michel_qualificacao_resultados_parciais_20261006.docx') as z:
    doc=etree.fromstring(z.read('word/document.xml'))
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
ps=[''.join(p.xpath('.//w:t/text()',namespaces=ns)) for p in doc.xpath('//w:body/w:p',namespaces=ns)]
for i in [426,594,804]:
    print('CONTEXTO',i,'\n'+'\n'.join(ps[i-3:i+5]))
