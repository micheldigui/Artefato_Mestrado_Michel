---
title: "Perfilamento e EDA Automatizada"
type: "conceito"
network: "machine-learning"
area: "EDA reprodutível"
status: "rascunho"
source_ids:
  - "OLULEYE-2023"
  - "AYD-HARRISON-2024"
tags:
  - conceito
  - eda
  - automacao
---

# Perfilamento e EDA Automatizada

## Definição

Perfilamento automatizado calcula e apresenta propriedades padronizadas de um conjunto de dados: tipos, volume, frequência, estatísticas, nulos, cardinalidade, correlação e alertas. EDA automatizada gera rapidamente uma primeira varredura; interpretação e investigação continuam sendo trabalho analítico.

## Fluxo de uso

1. Declarar a versão, origem, grão e filtros do conjunto.
2. Gerar perfil reprodutível e inspecionar alertas de tipo, ausência, duplicidade, cardinalidade, distribuição e associação.
3. Validar algumas observações nos registros de origem, sobretudo extrema e conversões.
4. Formular perguntas adicionais por domínio, período, grupo e alvo.
5. Registrar limitações conhecidas das ferramentas e a decisão manual subsequente.

## Aplicações

O perfil acelera inventário de muitas colunas e compara execuções. O laboratório EDA SQL Server fornece consultas explícitas para perfil, completude, cardinalidade, estatística descritiva, frequências, percentis, outliers, correlação e tempo; o relatório HTML apresenta essas tabelas.

## Limitações

Ferramentas não conhecem grão, semântica, momento de previsão, viés amostral, causalidade ou custo de erro sem contexto. Uma correlação automática pode misturar categorias, tempos e subgrupos. Volume de avisos pode criar falsa confiança. Não tomar sugestões de limpeza automática como decisão e não executar perfis completos em dados sensíveis sem considerar privacidade.

## Relações

- [[redes/machine-learning/conceitos/Analise_Exploratoria_de_Dados|Análise Exploratória de Dados]]
- [[redes/machine-learning/conceitos/Amostragem_e_Representatividade|Amostragem e Representatividade]]
- [[redes/machine-learning/conceitos/Estatisticas_Resistentes_e_Formas_de_Distribuicao|Estatísticas Resistentes e Formas de Distribuição]]
- [[redes/machine-learning/conceitos/Tratamento_de_Missing_Values|Tratamento de Missing Values]]
- [[redes/machine-learning/conceitos/Outliers|Outliers]]

## Evidência nas fontes

Oluleye (2023), capítulo 10, aborda pandas profiling, D-Tale, SweetViz, AutoViz e funções customizadas. O projeto registra material equivalente em `eda-sql-server/README.md`, consultas `01_eda_adventureworks.sql`/`02_eda_advanced_patterns.sql` e `python/eda_sql_report.py`.

## Perguntas de revisão

1. O perfil foi gerado no conjunto e grão corretos?
2. Quais alertas foram conferidos na origem e por segmento?
3. O que a automação não pode saber sem contexto?
4. Como reproduzir e comparar o relatório em outra versão dos dados?
