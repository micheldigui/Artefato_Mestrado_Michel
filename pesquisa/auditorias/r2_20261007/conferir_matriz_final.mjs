import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const dir='F:/PRODUTO_MESTRADO/pesquisa/auditorias/r2_20261007';
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('F:/PRODUTO_MESTRADO/pesquisa/matriz_artigos.xlsx'));
for(const [sheetName,range,name] of [['Página2','A1:B6','final_contagem.png'],['Página1','N78:R82','final_notas.png'],['Página2','A82:E88','final_inclusoes.png']]){
  const image=await wb.render({sheetName,range,scale:1,format:'png'});
  await fs.writeFile(dir+'/'+name,new Uint8Array(await image.arrayBuffer()));
}
console.log(JSON.stringify(wb.worksheets.getItem('Página2').getRange('A1:B6').values));
