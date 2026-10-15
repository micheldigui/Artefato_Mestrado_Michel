import docx
import re
import json
import unicodedata
from collections import defaultdict

doc_path = r'f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_resultados_parciais_20261013_antigravity.docx'
doc = docx.Document(doc_path)

def norm(text):
    if not text:
        return ""
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII').lower().strip()

# ==============================================================================
# 1. PARSE DE REFERÊNCIAS BIBLIOGRÁFICAS (Parágrafos 867 a 955)
# ==============================================================================
references = []
for i in range(867, 956):
    p = doc.paragraphs[i]
    txt = p.text.strip()
    if not txt:
        continue
    
    # Extrair anos
    years = re.findall(r'\b(19\d\d|20\d\d)\b', txt)
    
    # Extrair autores: pegar tudo antes do primeiro ponto ou do título
    # Geralmente: "SOBRENOME, P. N.; OUTRO, A."
    dot_split = txt.split('.')
    author_chunk = dot_split[0]
    if ';' in txt and (len(dot_split) > 1 and len(dot_split[0]) < 15):
        # se o primeiro ponto era de abreviação ex: "ACI, M."
        # pegar até o ponto final dos autores
        # ex: "ACI, M.; YERGÖK, D. Título..."
        parts = txt.split('. ')
        author_chunk = parts[0]
    
    # Pegar todos os sobrenomes em maiúsculas com mais de 2 letras
    caps_words = re.findall(r'\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{2,}\b', author_chunk)
    # Filtrar siglas que não são autores se houver
    caps_words = [w for w in caps_words if w not in ['DOI', 'HTTP', 'HTTPS', 'URL', 'ISSN', 'ISBN', 'IN', 'SP']]
    
    references.append({
        'p_idx': i,
        'full_text': txt,
        'authors_caps': caps_words,
        'norm_authors': [norm(w) for w in caps_words],
        'years': years,
        'first_author': caps_words[0] if caps_words else "DESCONHECIDO",
        'citations_matched': []
    })

print(f"Total de referências encontradas na seção final: {len(references)}")

# ==============================================================================
# 2. PARSE DE CITAÇÕES NO CORPO DO TEXTO (Parágrafos 0 a 865 e Tabelas)
# ==============================================================================
citations_found = []

def extract_citations(text, loc_label):
    # Citações entre parênteses: (SILVA, 2020) ou (SILVA; SANTOS, 2020) ou (SILVA et al., 2020)
    for m in re.finditer(r'\(([^)]*?\b(?:19\d\d|20\d\d)[a-z]?[^)]*?)\)', text):
        raw_inside = m.group(1).strip()
        # Se for menção a data/lei/artigo sem autor, pular
        if any(bad in raw_inside.lower() for bad in ['lei nº', 'art.', 'decreto', 'acesso em', 'portaria']):
            continue
        # Dividir por ';'
        parts = raw_inside.split(';')
        for part in parts:
            part = part.strip()
            y_m = re.search(r'\b(19\d\d|20\d\d)[a-z]?\b', part)
            if y_m:
                year = y_m.group(0)
                author_part = part[:y_m.start()].rstrip(',').strip()
                if author_part and not any(bad in author_part.lower() for bad in ['figura', 'quadro', 'tabela', 'secao', 'anexo', 'apendice']):
                    citations_found.append({
                        'loc': loc_label,
                        'type': 'parenthetical',
                        'raw': f"({part})",
                        'author_str': author_part,
                        'norm_authors': [norm(w) for w in re.findall(r'\b[A-ZÁÉÍÓÚÂÊÔÃÕÇa-záéíóúâêôãõç]{2,}\b', author_part) if norm(w) not in ['et', 'al', 'e', 'and', 'de', 'da', 'do']],
                        'year': year,
                        'context': text
                    })

    # Citações narrativas: Silva (2020), Silva e Souza (2020), Silva et al. (2020)
    for m in re.finditer(r'\b([A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+(?:\s+et\s+al\.)?(?:\s+e\s+[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]+)?)\s*\(((?:19\d\d|20\d\d)[a-z]?)\)', text):
        author_part = m.group(1).strip()
        year = m.group(2).strip()
        if not any(bad in author_part.lower() for bad in ['figura', 'quadro', 'tabela', 'secao', 'anexo', 'apendice', 'capitulo', 'versao']):
            citations_found.append({
                'loc': loc_label,
                'type': 'narrative',
                'raw': f"{author_part} ({year})",
                'author_str': author_part,
                'norm_authors': [norm(w) for w in re.findall(r'\b[A-Za-z]{2,}\b', author_part) if norm(w) not in ['et', 'al', 'e', 'and', 'de', 'da', 'do']],
                'year': year,
                'context': text
            })

for i in range(0, 866):
    p = doc.paragraphs[i]
    if p.text.strip():
        extract_citations(p.text.strip(), f"p_{i}")

for t_idx, table in enumerate(doc.tables):
    for r_idx, row in enumerate(table.rows):
        for c_idx, cell in enumerate(row.cells):
            if cell.text.strip():
                extract_citations(cell.text.strip(), f"t_{t_idx}_r{r_idx}c{c_idx}")

print(f"Total de ocorrências de citações extraídas: {len(citations_found)}")

# ==============================================================================
# 3. CRUZAMENTO BIDIRECIONAL
# ==============================================================================
# A) Para cada citação no texto, encontrar se existe referência correspondente
unmatched_citations = []
for cit in citations_found:
    matched = False
    cit_year_num = re.sub(r'[a-z]', '', cit['year'])
    for ref in references:
        # Checar se ano bate
        year_match = (cit_year_num in ref['years']) or (cit['year'] in ref['years'])
        
        # Checar se pelo menos um autor chave bate
        author_match = False
        for ca in cit['norm_authors']:
            for ra in ref['norm_authors']:
                if ca == ra or (len(ca) > 3 and ca in ra) or (len(ra) > 3 and ra in ca):
                    author_match = True
                    break
            if author_match:
                break
        
        if author_match and year_match:
            matched = True
            ref['citations_matched'].append(cit['raw'])
            break
        elif author_match and not year_match:
            # Possível divergência de ano!
            pass
            
    if not matched:
        unmatched_citations.append(cit)

# B) Para cada referência, ver se foi citada
unreferenced_in_text = []
for ref in references:
    if len(ref['citations_matched']) == 0:
        # Fazer busca textual secundária (caso a regex de citação não tenha pego)
        found_in_corpus = False
        primary_author = ref['first_author']
        for i in range(0, 866):
            p_text = doc.paragraphs[i].text
            if primary_author.lower() in p_text.lower():
                # conferir se tem menção
                found_in_corpus = True
                ref['citations_matched'].append(f"menção textual em p_{i}")
                break
        if not found_in_corpus:
            for t_idx, table in enumerate(doc.tables):
                for row in table.rows:
                    for cell in row.cells:
                        if primary_author.lower() in cell.text.lower():
                            found_in_corpus = True
                            ref['citations_matched'].append(f"menção textual em tabela {t_idx}")
                            break
                    if found_in_corpus:
                        break
                if found_in_corpus:
                    break
        if not found_in_corpus:
            unreferenced_in_text.append(ref)

# ==============================================================================
# 4. PALAVRAS EM INGLÊS / TERMOS ESTRANGEIROS SEM ITÁLICO
# ==============================================================================
# Lista de termos estrangeiros frequentes que devem estar em itálico segundo a ABNT
foreign_terms = [
    r'\bmachine learning\b',
    r'\brandom forests?\b',
    r'\bgradient boosting\b',
    r'\bxgboost\b',
    r'\blightgbm\b',
    r'\bcatboost\b',
    r'\bextra trees\b',
    r'\bwalk-forward\b',
    r'\bout-of-sample\b',
    r'\bin-sample\b',
    r'\bblind test\b',
    r'\bbaselines?\b',
    r'\bdata leakage\b',
    r'\bfeature stores?\b',
    r'\bfeature engineerings?\b',
    r'\bfeatures?\b',
    r'\btarget\b',
    r'\blags?\b',
    r'\brolling\b',
    r'\btrade-offs?\b',
    r'\bbenchmarks?\b',
    r'\bpipelines?\b',
    r'\bframeworks?\b',
    r'\boverfittings?\b',
    r'\bunderfittings?\b',
    r'\bensembles?\b',
    r'\blakehouse\b',
    r'\bmedallion\b',
    r'\bconformal prediction\b',
    r'\blive deployment\b',
    r'\btime series\b',
    r'\bbacktest(?:ing)?\b',
    r'\bgrid search\b',
    r'\bcross-validation\b',
    r'\bdata lake\b',
    r'\bdata warehouse\b',
    r'\bstate-of-the-art\b',
    r'\bclusters?\b',
    r'\bclustering\b',
    r'\bholdout\b',
    r'\blookahead bias\b',
    r'\bdata drift\b',
    r'\bconcept drift\b',
    r'\bground truth\b',
    r'\bfeedback\b',
    r'\bstandup\b',
    r'\bsprint\b',
    r'\bdeliverable\b',
    r'\bdeep learning\b',
    r'\bsoftwares?\b',
    r'\bhardware\b',
    r'\bdataset\b',
    r'\bdatasets\b',
    r'\bcheckpoint\b',
    r'\bcheckpoints\b'
]

unitalicized_foreign_words = []

for p_idx in range(0, 866):
    p = doc.paragraphs[p_idx]
    p_text = p.text
    if not p_text.strip():
        continue
    
    # Ignorar títulos de capítulos em caixa alta ou nomes de bibliotecas próprias se aplicável
    for term_pattern in foreign_terms:
        for m in re.finditer(term_pattern, p_text, re.IGNORECASE):
            term = m.group(0)
            start_char = m.start()
            end_char = m.end()
            
            # Verificar nos runs se esse trecho de caracteres está em itálico
            # Percorrer runs acumulando comprimento
            cur_pos = 0
            is_italic = True
            found_runs = []
            for r in p.runs:
                r_len = len(r.text)
                r_start = cur_pos
                r_end = cur_pos + r_len
                # Se sobrepõe com [start_char, end_char]
                if max(start_char, r_start) < min(end_char, r_end):
                    found_runs.append(r)
                    if not r.italic:
                        is_italic = False
                cur_pos = r_end
            
            if not is_italic:
                # Pegar contexto
                snippet_start = max(0, start_char - 30)
                snippet_end = min(len(p_text), end_char + 30)
                unitalicized_foreign_words.append({
                    'p_idx': p_idx,
                    'term': term,
                    'snippet': p_text[snippet_start:snippet_end],
                    'full_text': p_text
                })

# ==============================================================================
# 5. CONFERÊNCIA DE NUMERAÇÃO DE FIGURAS, TABELAS E QUADROS
# ==============================================================================
captions = []
for i in range(0, 866):
    txt = doc.paragraphs[i].text.strip()
    m_fig = re.match(r'^(Figura|Quadro|Tabela)\s+(\d+)\s*[-–—:]\s*(.*)', txt, re.IGNORECASE)
    if m_fig:
        captions.append({
            'p_idx': i,
            'type': m_fig.group(1).capitalize(),
            'num': int(m_fig.group(2)),
            'title': m_fig.group(3)
        })

# Salvar relatório consolidado
report = {
    'total_references': len(references),
    'unreferenced_in_text': [
        {'p_idx': r['p_idx'], 'authors': r['first_author'], 'text': r['full_text']}
        for r in unreferenced_in_text
    ],
    'total_citations_found': len(citations_found),
    'unmatched_citations': [
        {'loc': c['loc'], 'raw': c['raw'], 'author': c['author_str'], 'year': c['year'], 'context': c['context'][:120]}
        for c in unmatched_citations
    ],
    'unitalicized_foreign_count': len(unitalicized_foreign_words),
    'unitalicized_foreign_sample': unitalicized_foreign_words[:60],
    'captions_found': captions
}

with open(r'f:\PROJETOS\ARTEFATO\dissertacao\auditoria_completa_relatorio.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print("Auditoria concluída com sucesso! Resultados salvos em auditoria_completa_relatorio.json")
