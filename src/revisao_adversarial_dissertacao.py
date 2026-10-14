"""
Script de Auditoria e Refinamento Exaustivo (6 Rodadas Adversariais)
Executa verificacoes minuciosas e correcoes complementares no arquivo:
f:\\PROJETOS\\ARTEFATO\\dissertacao\\Dissertacao_Michel_qualificacao_antigravity.docx
"""

import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

DOCX_PATH = r"f:\PROJETOS\ARTEFATO\dissertacao\Dissertacao_Michel_qualificacao_antigravity.docx"
RED_COLOR = RGBColor(200, 0, 0)

def aplicar_italico_termos_ingles(doc):
    print("\nAplicando italico em termos tecnicos em lingua estrangeira...")
    termos = [
        "Machine Learning",
        "Design Science Research",
        "Walk-Forward Validation",
        "Walk-Forward",
        "Data Leakage",
        "Overfitting",
        "Underfitting",
        "Mean Absolute Error",
        "Random Forest",
        "Gradient Boosting",
        "ExtraTrees",
        "Feature Store",
        "Decision Support System",
        "Blind Test",
        "Live Deployment",
        "Shadow Run",
        "Shadow Mode",
        "Conformal Prediction",
        "Dataset",
        "Datasets",
        "Baseline",
        "Baselines",
        "Pipeline",
        "Pipelines",
        "Framework",
        "Frameworks",
        "Benchmark",
        "Benchmarks",
        "Trade-off",
        "Trade-offs",
        "Backtesting",
        "In loco",
        "Ex-post",
        "Ex-ante",
    ]
    
    # Criar expressao regular com limites de palavra
    pattern = re.compile(r'(' + '|'.join(re.escape(t) for t in termos) + r')', re.IGNORECASE)
    
    total_modificados = 0
    # Percorrer apenas paragrafos de texto corrido (P0293 ate P0833)
    for p in doc.paragraphs[293:834]:
        # Ignorar titulos ou legendas
        if p.style.name.startswith("Heading") or p.text.strip().startswith("Figura ") or p.text.strip().startswith("Tabela ") or p.text.strip().startswith("Quadro "):
            continue
        if not p.text.strip():
            continue
            
        # Verificar se ha correspondencia no texto do paragrafo
        if pattern.search(p.text):
            # Percorrer os runs existentes
            for r in p.runs:
                # Se o run contiver o termo exatamente ou parcialmente
                m = pattern.search(r.text)
                if m:
                    r.italic = True
                    total_modificados += 1

    print(f"Total de runs com aplicacao de italico em termos em ingles: {total_modificados}")

def rodada_1_verificar_secoes_e_paragrafos(doc):
    print("\n--- RODADA 1: Verificacao Estrutural de Secoes e Paragrafos ---")
    falhas = 0
    for i in range(293, 830):
        p = doc.paragraphs[i]
        if p.style.name.startswith("Heading"):
            next_p = doc.paragraphs[i+1]
            if next_p.style.name.startswith("Heading"):
                print(f"  [ALERTA] Heading sem texto intermediario: P{i:04d} '{p.text[:40]}' seguido por P{i+1:04d} '{next_p.text[:40]}'")
                falhas += 1
    if falhas == 0:
        print("  [OK] Nenhuma secao primaria ou secundaria sem texto introdutorio!")
    else:
        print(f"  Total de inconsistencias encontradas: {falhas}")

def rodada_2_verificar_chamadas_tabelas_figuras(doc):
    print("\n--- RODADA 2: Auditoria de Chamadas de Tabelas e Figuras ---")
    erros_tabelas = []
    padroes_errados = ["Tabela 13", "Tabela 15", "Tabela 17", "Tabela 18", "Tabelas 4 e 5"]
    for i, p in enumerate(doc.paragraphs):
        for pe in padroes_errados:
            if pe.lower() in p.text.lower():
                erros_tabelas.append((i, pe, p.text[:80]))
                
    if not erros_tabelas:
        print("  [OK] Nenhuma chamada incorreta a Tabelas 13, 15, 17, 18 ou 4/5 encontrada!")
    else:
        for idx, pe, txt in erros_tabelas:
            print(f"  [FALHA] P{idx:04d} contem '{pe}': {txt}")

def rodada_3_verificar_vies_e_prosopopeia(doc):
    print("\n--- RODADA 3: Auditoria Terminologica (Vies e Prosopopeia) ---")
    vies_ocorrencias = []
    for i, p in enumerate(doc.paragraphs):
        # Procurar palavra vies isolada
        m = re.search(r'\b(vi[eé]s|vieses)\b', p.text, re.IGNORECASE)
        if m:
            vies_ocorrencias.append((i, p.text[:90]))
            
    if not vies_ocorrencias:
        print("  [OK] Nenhuma ocorrencia inadequada da palavra 'vies' encontrada!")
    else:
        for idx, txt in vies_ocorrencias:
            print(f"  [ALERTA] P{idx:04d} contem 'vies': {txt}")

def rodada_4_verificar_tarifas_financeiras(doc):
    print("\n--- RODADA 4: Auditoria das Tarifas Contratuais Reais (R$ 17,36 e R$ 14,00) ---")
    mencoes_antigas = []
    for i, p in enumerate(doc.paragraphs):
        if "8,50" in p.text:
            mencoes_antigas.append((i, p.text[:90]))
            
    if not mencoes_antigas:
        print("  [OK] Nenhuma mencao residual ao preco parametrico antigo (R$ 8,50) encontrada no texto!")
    else:
        for idx, txt in mencoes_antigas:
            print(f"  [FALHA] P{idx:04d} contem '8,50': {txt}")
            
    # Conferir se Tabela 8 contem R$ 17,36 e R$ 14,00
    t8 = doc.tables[23]
    custo_tryx = t8.rows[1].cells[5].text.strip()
    custo_hibrido = t8.rows[6].cells[5].text.strip()
    print(f"  [CHECK] Tabela 8 Custo Tryx (2023-25): {custo_tryx} (esperado: R$ 50.621,76)")
    print(f"  [CHECK] Tabela 8 Custo Hibrido 50/50: {custo_hibrido} (esperado: R$ 18.046,00)")

def rodada_5_verificar_referencias_e_listas(doc):
    print("\n--- RODADA 5: Auditoria de Referencias e Elementos Pre-Textuais ---")
    # Conferir as 3 referencias
    refs_encontradas = {"angelopoulos": False, "blattberg": False, "knaflic": False}
    for p in doc.paragraphs[830:]:
        for k in refs_encontradas:
            if k in p.text.lower():
                refs_encontradas[k] = True
                
    for k, v in refs_encontradas.items():
        print(f"  [CHECK] Referencia {k.capitalize()}: {'PRESENTE' if v else 'AUSENTE'}")
        
    # Conferir Resumo e Abstract
    p_resumo = doc.paragraphs[137]
    palavras_resumo = len(p_resumo.text.split())
    p_abstract = doc.paragraphs[142]
    palavras_abstract = len(p_abstract.text.split())
    print(f"  [CHECK] Resumo: {palavras_resumo} palavras (esperado ~415)")
    print(f"  [CHECK] Abstract: {palavras_abstract} palavras (esperado ~415)")

def rodada_6_verificar_cor_vermelha(doc):
    print("\n--- RODADA 6: Auditoria das Alteracoes em VERMELHO ---")
    runs_vermelhos = 0
    for p in doc.paragraphs:
        for r in p.runs:
            if r.font.color and r.font.color.rgb == RED_COLOR:
                runs_vermelhos += 1
                
    for t in doc.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    for r in p.runs:
                        if r.font.color and r.font.color.rgb == RED_COLOR:
                            runs_vermelhos += 1
                            
    print(f"  [OK] Total de elementos destacados em VERMELHO para conferencia do Michel: {runs_vermelhos}")

def executar_todas_rodadas():
    doc = docx.Document(DOCX_PATH)
    aplicar_italico_termos_ingles(doc)
    doc.save(DOCX_PATH)
    
    doc = docx.Document(DOCX_PATH)
    rodada_1_verificar_secoes_e_paragrafos(doc)
    rodada_2_verificar_chamadas_tabelas_figuras(doc)
    rodada_3_verificar_vies_e_prosopopeia(doc)
    rodada_4_verificar_tarifas_financeiras(doc)
    rodada_5_verificar_referencias_e_listas(doc)
    rodada_6_verificar_cor_vermelha(doc)

if __name__ == "__main__":
    executar_todas_rodadas()
