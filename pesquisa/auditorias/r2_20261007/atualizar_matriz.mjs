import fs from 'node:fs/promises';
import { FileBlob, SpreadsheetFile } from '@oai/artifact-tool';
const dir='F:/PRODUTO_MESTRADO/pesquisa/auditorias/r2_20261007';
const book=await SpreadsheetFile.importXlsx(await FileBlob.load(dir+'/matriz_artigos_antes_da_inclusao.xlsx'));
const main=book.worksheets.getItem('Página1');
const summary=book.worksheets.getItem('Página2');
if(process.argv.includes('--inspect-only')){
  for(const [name,range,file] of [['Página1','N76:R77','antes_notas.png'],['Página2','A1:B6','antes_contagens.png']]){
    const im=await book.render({sheetName:name,range,scale:1.2,format:'png'});
    await fs.writeFile(dir+'/'+file,new Uint8Array(await im.arrayBuffer()));
  }
  console.log('Prévias originais salvas.');process.exit(0);
}
const rows=JSON.parse(await fs.readFile(dir+'/novas_referencias.json','utf8'));
for(let r=78;r<=82;r++) main.getRange(`A${r}:R${r}`).copyFrom(main.getRange('A77:R77'),'all');
main.getRange('A78:R82').values=rows;
main.getRange('A78:R82').format.wrapText=true;
main.getRange('A78:R82').format.autofitRows();
for(let r=1;r<=4;r++){
  const old=summary.getRange(`B${r}`).formulas[0][0];
  summary.getRange(`B${r}`).formulas=[[old.replaceAll('$R$76','$R$82')]];
}
summary.getRange('A6').values=[['Total de referências']];
summary.getRange('A83:E83').copyFrom(summary.getRange('A8:E8'),'all');
summary.getRange('A82').values=[['Inclusões para a interpretação do R² — 07/10/2026']];
summary.getRange('A84:E88').values=rows.map(r=>[r[0],r[3],r[2],r[1],r[17]]);
summary.getRange('A84:E88').format.wrapText=true;
summary.getRange('A84:E88').format.autofitRows();
book.recalculate();
console.log(JSON.stringify(summary.getRange('A1:B6').values));
for(const [name,range,file] of [['Página1','N78:R82','depois_notas.png'],['Página2','A1:B6','depois_contagens.png']]){
  const im=await book.render({sheetName:name,range,scale:1.2,format:'png'});
  await fs.writeFile(dir+'/'+file,new Uint8Array(await im.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(book)).save(dir+'/matriz_edicao_artifact.xlsx');
console.log('Edição de células exportada para integração com o arquivo original.');
