from pathlib import Path
import json, hashlib, shutil, re
import openpyxl
from lxml import etree
import zipfile

ROOT=Path(r'F:\PRODUTO_MESTRADO')
OUT=ROOT/'pesquisa/auditorias/r2_20261007'
BOOK=ROOT/'pesquisa/matriz_artigos.xlsx'
DOC=ROOT/'dissertacao/Dissertacao_Michel_qualificacao_resultados_parciais_20261006.docx'
wb=openpyxl.load_workbook(BOOK)
rows=list(wb.worksheets[0].values)
assert len([r for r in rows[1:] if r[0]])==76
assert not any(str(r[0])=='A078' for r in rows)
papers=[
 dict(id='A078',source='1915006117.full.pdf',stem='2020-Salganik_Measuring_the_predictability_of_life_outcomes',year=2020,
 title='Measuring the predictability of life outcomes with a scientific mass collaboration',pt='Medição da previsibilidade de resultados de vida por uma colaboração científica em larga escala',
 authors='Matthew J. Salganik et al.',journal='Proceedings of the National Academy of Sciences, 117(15), 8398–8403',doi='10.1073/pnas.1915006117',category='Aproveitar parcialmente',score=4,
 relation='Limites da previsão de resultados humanos; avaliação fora da amostra',
 evidence='160 equipes construíram previsões para seis desfechos. Os melhores R² de holdout ficaram em torno de 0,20 para dificuldades materiais e desempenho escolar. O artigo considera a precisão limitada. PDF p. 4 (p. 3 do artigo), seção Results e Figura 3.',
 idea='Resultados humanos podem ser difíceis de prever mesmo com numerosas variáveis e modelos sofisticados. O exemplo contextualiza limites da previsão, sem estabelecer um R² mínimo ou declarar modelos de refeições adequados.',
 sentence='Salganik et al. (2020) encontraram capacidade preditiva limitada em desfechos sociais mesmo com uma base longitudinal extensa e modelos desenvolvidos por 160 equipes.',
 limits='O alvo é individual e social, diferente do consumo diário agregado. R² de holdout usa a média do treinamento no denominador. Não comparar diretamente com o R² convencional nem afirmar que o estudo considera 0,20 bom. Não permite atribuir o erro deste restaurante exclusivamente ao comportamento humano.',
 pages='PDF pp. 2–4: desenho e resultados. PDF p. 4: equação 1 e Figura 3. A primeira página do PDF é uma capa do repositório.'),
 dict(id='A079',source='Abelson1985.pdf',stem='1985-Abelson_A_variance_explanation_paradox',year=1985,
 title='A variance explanation paradox: When a little is a lot',pt='Um paradoxo da explicação da variância: quando pouco é muito',authors='Robert P. Abelson',journal='Psychological Bulletin, 97(1), 129–133',doi='10.1037/0033-2909.97.1.129',category='Apoio pontual',score=3,
 relation='Interpretação contextual da variância e relevância prática',
 evidence='Discussão conceitual, com exemplo de desempenho no beisebol, sobre pequenas influências sistemáticas que se acumulam em resultados relevantes. Resumo e discussão, pp. 129–133 (PDF pp. 1–5).',
 idea='Uma pequena proporção de variância associada a um fator não informa, isoladamente, sua importância prática, especialmente em processos repetidos.',
 sentence='Abelson (1985) discute que pequenas proporções de variância podem corresponder a influências relevantes quando seus efeitos se acumulam em acontecimentos repetidos.',
 limits='Artigo conceitual sobre variância e efeitos acumulados. Não define cortes de R² para previsão de refeições nem demonstra economia, desperdício evitado ou utilidade do artefato.',pages='PDF pp. 1–5, correspondentes às páginas 129–133 do periódico.'),
 dict(id='A080',source='funder-ozer-2019-evaluating-effect-size-in-psychological-research-sense-and-nonsense.pdf',stem='2019-Funder_Ozer_Evaluating_effect_size_in_psychological_research',year=2019,
 title='Evaluating effect size in psychological research: Sense and nonsense',pt='Avaliação do tamanho de efeito em pesquisa psicológica: sentido e equívocos',authors='David C. Funder; Daniel J. Ozer',journal='Advances in Methods and Practices in Psychological Science, 2(2), 156–168',doi='10.1177/2515245919847202',category='Apoio pontual',score=3,
 relation='Interpretação de tamanhos de efeito; contextualização dos indicadores',
 evidence='Recomenda interpretar tamanhos de efeito por referências conhecidas e consequências concretas. O arquivo contém a errata de 2020 na primeira página, DOI 10.1177/2515245920979282, que corrige o parágrafo Squaring the Correlation da p. 158.',
 idea='Classificações abstratas e percentuais de variância não substituem a avaliação da relevância no contexto. Utilizar a explicação corrigida sobre r e r².',
 sentence='Funder e Ozer (2019) recomendam avaliar a relevância dos resultados por referências conhecidas e consequências concretas, considerando o contexto de aplicação.',
 limits='Trata principalmente de correlação r e tamanho de efeito. Não converter as classificações de r em faixas para R² de regressão múltipla ou previsão fora da amostra. Errata de 2020 incorporada à leitura; não é um sexto artigo independente.',
 pages='PDF p. 1: errata de 2020. PDF pp. 2–14: artigo de 2019, pp. 156–168. Ver especialmente Squaring the Correlation e Benchmarks/Consequences.'),
 dict(id='A081',source='1101.0891v1.pdf',stem='2010-Shmueli_To_explain_or_to_predict',year=2010,
 title='To explain or to predict?',pt='Explicar ou prever?',authors='Galit Shmueli',journal='Statistical Science, 25(3), 289–310',doi='10.1214/10-STS330',category='Aproveitar fortemente',score=5,
 relation='Finalidade preditiva; desempenho fora da amostra; interpretação do R²',
 evidence='Distingue explicação causal de previsão e descreve implicações para coleta, atributos, seleção e avaliação. Seção 2.6.2: Model evaluation, PDF pp. 12–13. Metadados da primeira página confirmam publicação em 2010.',
 idea='Bom ajuste aos dados usados na estimação não garante desempenho preditivo em novas observações. Avaliar o R² nas previsões temporais, junto a erros na escala de refeições.',
 sentence='Shmueli (2010) distingue ajuste explicativo de desempenho preditivo, fundamentando a avaliação das previsões em observações não utilizadas no treinamento.',
 limits='Não define limiar de 0,50. A versão arXiv foi depositada em 2011, mas o artigo publicado é de 2010. É uma obra diferente de Predictive Analytics in Information Systems Research, de Shmueli e Koppius, já cadastrada como A059.',
 pages='PDF p. 1: ficha bibliográfica. PDF pp. 12–13: seção 2.6.2. PDF pp. 11–14: disponibilidade de atributos, avaliação e uso do modelo.'),
 dict(id='A082',source='1-s2.0-S0169207021001011-main.pdf',stem='2022-Posch_A_Bayesian_approach_for_predicting_food_and_beverage_sales',year=2022,
 title='A Bayesian approach for predicting food and beverage sales in staff canteens and restaurants',pt='Uma abordagem bayesiana para prever vendas de alimentos e bebidas em cantinas de funcionários e restaurantes',authors='Konstantin Posch; Christian Truden; Philipp Hungerländer; Jürgen Pilz',journal='International Journal of Forecasting, 38(1), 321–338',doi='10.1016/j.ijforecast.2021.06.001',category='Aproveitar fortemente',score=5,
 relation='Previsão de demanda em alimentação coletiva; variabilidade temporal',
 evidence='Avalia modelos aditivos generalizados em um restaurante e uma cantina, com séries de aproximadamente 20 meses. Descreve sazonalidades, mudanças de tendência, lacunas e valores atípicos. Resumo e introdução, PDF p. 1; resultados com WAPE, MAD e outras métricas, PDF pp. 15–17.',
 idea='Séries de demanda de refeições têm estruturas temporais e dados incompletos que devem ser considerados no protocolo e na interpretação das métricas.',
 sentence='Posch et al. (2022) descrevem sazonalidades, mudanças de tendência, lacunas e valores atípicos em séries de demanda de restaurantes e cantinas.',
 limits='Não fornece limite de aceitação de R² abaixo de 0,50. Seus resultados não são diretamente comparáveis aos do restaurante estudado. Publicação no volume de 2022; DOI e copyright remetem a 2021.',
 pages='PDF p. 1: metadados, resumo e contexto. PDF pp. 15–17: resultados e métricas; páginas do periódico 335–337.'),
]
payload=[]
for p in papers:
    dest=ROOT/'pesquisa/Artigos'/p['category']/(p['stem']+'.pdf')
    p['destination']=str(dest)
    p['sha256']=hashlib.sha256((ROOT/'pesquisa'/p['source']).read_bytes()).hexdigest()
    assert not dest.exists(),dest
    summary=ROOT/'pesquisa/Resumos Artigos'/(p['id']+'_'+p['stem']+'.md')
    p['summary']=str(summary)
    payload.append([p['id'],'https://doi.org/'+p['doi'],p['pt'],p['title'],p['year'],p['authors'],'Artigo científico',p['journal'],'https://doi.org/'+p['doi'],p['score'],p['relation'],'2.6.1 Métricas; 3.5 Avaliação preditiva; 5.7 Interpretação do R²',
        p['idea']+' PDF local: '+str(dest)+'. Ficha de leitura: '+str(summary),p['evidence'],p['idea'],p['sentence'],p['limits'],p['category']])
backup=OUT/'matriz_artigos_antes_da_inclusao.xlsx'
if not backup.exists():shutil.copy2(BOOK,backup)
(OUT/'novas_referencias.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'plano_organizacao.json').write_text(json.dumps({'papers':papers,'sha256_doc':hashlib.sha256(DOC.read_bytes()).hexdigest(),'total_antes':76,'total_depois':81},ensure_ascii=False,indent=2),encoding='utf-8')
print('Dados preparados: cinco artigos, IDs A078–A082; backup preservado.')
