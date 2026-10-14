from pathlib import Path
from lxml import etree
import zipfile, json, hashlib
from collections import Counter
import openpyxl
root=Path(r'F:\PRODUTO_MESTRADO')
out=root/'pesquisa/auditorias/revisao_geral_20261007'
out.mkdir(exist_ok=True)
f=root/'dissertacao/Dissertacao_Michel_qualificacao_resultados_parciais_20261006.docx'
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
with zipfile.ZipFile(f) as z:
 d=etree.fromstring(z.read('word/document.xml'))
 blocks=[]
 for i,e in enumerate(d.find('w:body',ns)):
  if e.tag.endswith('}p'):
   t=''.join(e.xpath('.//w:t/text()',namespaces=ns))
   if t.strip(): blocks.append({'i':i,'type':'p','text':t})
  elif e.tag.endswith('}tbl'):
   rows=[[''.join(c.xpath('.//w:t/text()',namespaces=ns)) for c in r.findall('w:tc',ns)] for r in e.findall('w:tr',ns)]
   blocks.append({'i':i,'type':'table','rows':rows})
 comments=[]
 if 'word/comments.xml' in z.namelist():
  for c in etree.fromstring(z.read('word/comments.xml')):
   comments.append({'id':c.get('{'+ns['w']+'}id'),'text':''.join(c.xpath('.//w:t/text()',namespaces=ns))})
 fields=d.xpath('//w:instrText/text()',namespaces=ns)
 rels=etree.fromstring(z.read('word/_rels/document.xml.rels'))
 relmap={r.get('Id'):r.get('Target') for r in rels}
 media=[]
 for i,e in enumerate(d.find('w:body',ns)):
  for im in e.xpath('.//*[local-name()="blip"]'):
   target=relmap.get(im.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'))
   if target:
    name=Path(target).name
    (out/name).write_bytes(z.read('word/'+target))
    media.append({'i':i,'file':name})
 anchors=[]
 for b in d.find('w:body',ns):
  ids=b.xpath('.//w:commentRangeStart/@w:id',namespaces=ns)
  if ids: anchors.append({'ids':ids,'text':''.join(b.xpath('.//w:t/text()',namespaces=ns))})
 (out/'imagens_e_comentarios.json').write_text(json.dumps({'images':media,'anchors':anchors},ensure_ascii=False,indent=2),encoding='utf-8')
 meta={'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'comments':comments,'fields':fields,'insertions':len(d.xpath('//w:ins',namespaces=ns)),'deletions':len(d.xpath('//w:del',namespaces=ns))}
 (out/'documento.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
 (out/'metadados.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
 text='\n\n'.join(f"[{b['i']}] "+(b['text'] if b['type']=='p' else '\n'.join(' | '.join(r) for r in b['rows'])) for b in blocks)
 (out/'documento_completo.txt').write_text(text,encoding='utf-8')
 chunks=[blocks[n:n+160] for n in range(0,len(blocks),160)]
 for n,bs in enumerate(chunks):
  (out/f'parte_{n+1}.txt').write_text('\n\n'.join(f"[{b['i']}] "+(b['text'] if b['type']=='p' else '\n'.join(' | '.join(r) for r in b['rows'])) for b in bs),encoding='utf-8')
 wb=openpyxl.load_workbook(root/'pesquisa/matriz_artigos.xlsx',read_only=True,data_only=True)
 rows=list(wb['Página1'].iter_rows(min_row=2,values_only=True))
 refs=[r for r in rows if r[0]]
 matrix={'total':len(refs),'classes':dict(Counter(str(r[17]).strip() for r in refs)), 'rows':refs}
 (out/'matriz.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
 print(json.dumps({'blocks':len(blocks),'chunks':len(chunks),'tables':sum(b['type']=='table' for b in blocks),'matrix_total':len(refs),'classes':matrix['classes'],'comments':comments,'insertions':meta['insertions'],'deletions':meta['deletions']},ensure_ascii=False))
