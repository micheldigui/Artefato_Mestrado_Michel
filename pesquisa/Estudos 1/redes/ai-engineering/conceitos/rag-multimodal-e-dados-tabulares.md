# 🧠 RAG Multimodal e Dados Tabulares (Text-to-SQL)

**Rede:** `ai-engineering`  
**Área:** `recuperacao`

## Definição

São extensões de [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]] para responder com fontes que não são apenas documentos de texto contínuo:

- **RAG multimodal** recupera evidências como imagens, gráficos ou áudio e as fornece a um modelo que consegue interpretar essas modalidades. A recuperação pode usar metadados, índices específicos ou representações conjuntas texto-imagem, como embeddings contrastivos.
- **Text-to-SQL** interpreta uma pergunta sobre dados relacionais, consulta o esquema e os metadados, produz uma consulta SQL, executa-a sobre a base e apresenta os resultados ao modelo para gerar uma explicação. Os cálculos e filtros são realizados pelo banco de dados.

Apesar do nome, Text-to-SQL não precisa fazer busca vetorial dos registros: uma etapa de recuperação pode localizar tabelas e definições de esquema, enquanto o SQL seleciona e agrega os dados.

## Fluxos resumidos

### Multimodal

1. Catalogar arquivos, modalidade, origem e permissões.
2. Indexar descrições ou características visuais/sonoras adequadas à consulta.
3. Recuperar evidências relevantes e passá-las ao modelo multimodal.
4. Responder indicando a evidência visual ou sonora usada, quando possível.

### Text-to-SQL

1. Identificar a intenção, as tabelas relevantes e seus esquemas.
2. Gerar SQL compatível com o dialeto e os significados dos campos.
3. Validar a consulta, restringir permissões e executá-la em modo apropriado, de preferência somente leitura.
4. Conferir os resultados e produzir uma resposta explicativa com limites e unidades explícitos.

## Quando cada extensão ajuda

| Necessidade | Abordagem | Checagens principais |
|---|---|---|
| Pergunta depende de uma imagem, gráfico, documento visual ou áudio | RAG multimodal | Recuperação da modalidade correta, legibilidade/OCR, alinhamento entre evidência e resposta, permissões e qualidade do modelo multimodal. |
| Pergunta requer filtros, contagens, somas, médias ou agrupamentos em tabelas | Text-to-SQL | Esquema e dicionário de dados, unidade/denominador, filtros de data, validação da SQL, autorização e precisão dos resultados. |
| Pergunta combina documento narrativo e dados tabulares | Pipeline composto | Recuperar cada fonte com o método apropriado, reconciliar definições e informar qual fonte sustenta cada parte da resposta. |

## Limitações e segurança

- Uma recuperação correta não corrige um esquema ambíguo, um dado desatualizado ou uma métrica mal definida.
- SQL gerada pode ser sintaticamente válida e semanticamente errada. Valide tabelas, colunas, junções, granularidade, filtros, unidades e resultados plausíveis.
- Restrinja o executor por identidade e permissões; use consultas somente leitura, limites de custo/linhas e validação de consultas antes da execução. Não confie no modelo para impor autorização.
- Conteúdo recuperado pode conter instruções maliciosas. Trate documentos e campos como dados não confiáveis e aplique controles contra injeção de prompt.
- A resposta deve distinguir evidência recuperada de inferência e declarar quando não há suporte suficiente.

## Avaliação

Avalie os componentes separadamente e também o fluxo ponta a ponta:

- **Recuperação:** se a imagem, passagem, tabela ou esquema relevante aparece entre os candidatos e no contexto final.
- **Text-to-SQL:** validade e execução da consulta, correspondência semântica com a pergunta e correção do resultado em casos representativos.
- **Resposta:** correção, apoio nas evidências, unidades, citações e abstenção diante de dados insuficientes.
- **Operação:** latência, custo, controle de acesso e comportamento diante de mudanças no esquema ou nas fontes.

## Conexões

- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]]: arquitetura geral recuperar-e-gerar.
- [[redes/ai-engineering/conceitos/rag-multimodal-e-dados-tabulares-text-to-sql.md|Nota detalhada de RAG Multimodal e Text-to-SQL]]: exemplos e mecanismos do capítulo.
- [[redes/ai-engineering/conceitos/modelo-multimodal.md|Modelo Multimodal]] e [[redes/ai-engineering/conceitos/embeddings.md|Embeddings]]: interpretação e recuperação de conteúdo multimodal.
- [[redes/ai-engineering/conceitos/algoritmos-de-recuperacao-lexical-e-vetorial.md|Recuperação lexical e vetorial]]: localizar conteúdo e esquemas.
- [[redes/ai-engineering/conceitos/planejamento-e-chamada-de-funcoes-function-calling.md|Chamada de funções]]: executar consultas e ferramentas sob controle da aplicação.
- [[redes/ai-engineering/conceitos/agentes-de-ia.md|Agentes de IA]]: orquestração de etapas quando o fluxo exigir planejamento e ferramentas.

## Evidência nas fontes

Chip Huyen, *AI Engineering: Building Applications with Foundation Models*, cap. 6, pp. 273–275. A nota detalhada ligada acima registra os exemplos multimodais e Text-to-SQL do capítulo; confira a edição consultada antes de usar como citação acadêmica.
