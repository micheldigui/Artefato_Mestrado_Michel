import docx
import re
from collections import defaultdict

doc = docx.Document('Dissertacao_Michel_qualificacao_resultados_parciais_20261013_antigravity.docx')

terms = [
    'machine learning', 'random forest', 'gradient boosting', 'xgboost', 'lightgbm', 
    'catboost', 'extra trees', 'walk-forward', 'out-of-sample', 'in-sample', 
    'blind test', 'baseline', 'baselines', 'data leakage', 'feature store', 
    'feature engineering', 'features', 'feature', 'target', 'lags', 'lag', 
    'rolling', 'trade-off', 'trade-offs', 'benchmark', 'benchmarks', 
    'pipeline', 'pipelines', 'framework', 'frameworks', 'overfitting', 
    'underfitting', 'ensemble', 'ensembles', 'lakehouse', 'medallion', 
    'conformal prediction', 'live deployment', 'time series', 'backtest', 
    'backtesting', 'grid search', 'cross-validation', 'data lake', 
    'data warehouse', 'holdout', 'data drift', 'concept drift', 'ground truth', 
    'dataset', 'datasets', 'checkpoint', 'checkpoints', 'lead time', 'split', 'splits'
]

term_patterns = []
for t in terms:
    pattern = r'\b' + re.escape(t) + r'\b'
    term_patterns.append((t, re.compile(pattern, re.IGNORECASE)))

unitalicized_by_term = defaultdict(list)
all_unitalicized = []

for p_idx in range(0, 866):
    p = doc.paragraphs[p_idx]
    p_text = p.text
    if not p_text.strip():
        continue
    
    if p_text.isupper() and len(p_text) < 80:
        continue

    for term_str, term_re in term_patterns:
        for m in term_re.finditer(p_text):
            s_idx, e_idx = m.start(), m.end()
            term_found = m.group(0)
            
            cur = 0
            is_it = True
            for r in p.runs:
                rlen = len(r.text)
                r_s, r_e = cur, cur + rlen
                if max(s_idx, r_s) < min(e_idx, r_e):
                    if not r.italic:
                        is_it = False
                cur = r_e
            
            if not is_it:
                c_start = max(0, s_idx - 30)
                c_end = min(len(p_text), e_idx + 30)
                ctx = p_text[c_start:c_end].replace('\n', ' ')
                unitalicized_by_term[term_str].append((p_idx, term_found, ctx))
                all_unitalicized.append({
                    'p_idx': p_idx,
                    'term': term_found,
                    'term_key': term_str,
                    'context': ctx
                })

print("=== AUDITORIA DE TERMOS EM INGLES SEM ITALICO ===")
total_unitalicized = len(all_unitalicized)
print(f"Total de ocorrencias sem italico: {total_unitalicized}\n")

# Agrupar por parágrafo para que o usuário saiba exatamente onde mexer
by_paragraph = defaultdict(list)
for item in all_unitalicized:
    by_paragraph[item['p_idx']].append((item['term'], item['context']))

print(f"Total de paragrafos afetados: {len(by_paragraph)}")

with open('termos_ingles_sem_italico.txt', 'w', encoding='utf-8') as f:
    f.write(f"AUDITORIA DE PALAVRAS EM INGLES SEM ITALICO NO DOCX\n")
    f.write(f"Total de termos identificados: {total_unitalicized}\n")
    f.write(f"Total de paragrafos afetados: {len(by_paragraph)}\n\n")
    
    f.write("RESUMO POR TERMO:\n")
    for term_str, occurrences in sorted(unitalicized_by_term.items(), key=lambda x: len(x[1]), reverse=True):
        f.write(f"- {term_str}: {len(occurrences)} ocorrencias\n")
    
    f.write("\n" + "="*80 + "\n")
    f.write("DETALHAMENTO POR PARAGRAFO:\n")
    f.write("="*80 + "\n\n")
    for p_idx in sorted(by_paragraph.keys()):
        f.write(f"[Paragrafo {p_idx}]:\n")
        for term, ctx in by_paragraph[p_idx]:
            f.write(f"   * Termo '{term}': ...{ctx}...\n")
        f.write("\n")

print("Arquivo 'termos_ingles_sem_italico.txt' gerado com sucesso!")
