from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
import json
p=Path(__file__).parent
imgs=[Image.open(p/f'image{i}.png').convert('RGB') for i in range(1,23)]
for a,b in [(1,6),(7,12),(13,18),(19,22)]:
 canvas=Image.new('RGB',(1600,((b-a+2)//2)*560),'#dddddd')
 draw=ImageDraw.Draw(canvas)
 for k,i in enumerate(range(a,b+1)):
  im=ImageOps.contain(imgs[i-1],(780,520))
  x=(k%2)*800; y=(k//2)*560
  draw.text((x+10,y+5),f'Figura {i}',fill='black')
  canvas.paste(im,(x+10,y+30))
 canvas.save(p/f'montagem_{a}_{b}.png')
bs=json.loads((p/'documento.json').read_text(encoding='utf-8'))
print('Referências listadas:',sum(b['i']>975 for b in bs))
