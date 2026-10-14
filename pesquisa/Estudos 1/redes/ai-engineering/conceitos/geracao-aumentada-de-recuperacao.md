# 🧠 Geração Aumentada de Recuperação (RAG)

**Rede:** `ai-engineering`  
**Área:** `recuperacao-de-informacao`

## Definição

A **Geração Aumentada de Recuperação** (*retrieval-augmented generation*, RAG) combina busca em uma coleção externa com um modelo gerador. Para responder a uma consulta, o sistema recupera passagens potencialmente relevantes e as fornece como contexto ao modelo.

RAG atua no contexto de inferência: por si só, não atualiza os pesos do modelo. Também não garante uma resposta correta; isso depende da qualidade e atualidade das fontes, da recuperação, da composição do contexto e da geração.

## Etapas principais

1. **Preparar e indexar:** organizar documentos, preservar metadados e permissões, dividi-los em unidades recuperáveis e criar os índices necessários.
2. **Interpretar a consulta:** normalizar ou reescrever a pergunta quando necessário.
3. **Recuperar candidatos:** buscar passagens por termos, vetores semânticos ou uma combinação dos dois.
4. **Filtrar ou reordenar:** avaliar relevância e selecionar o contexto que cabe no orçamento da janela.
5. **Gerar:** instruir o modelo a responder com base no contexto e sinalizar quando as fontes não sustentam uma resposta.
6. **Avaliar e atualizar:** medir recuperação e qualidade da resposta separadamente, atualizar o índice e respeitar controle de acesso.

## Quando considerar

- A resposta depende de documentos privados, extensos ou que mudam com o tempo.
- É útil devolver referências às passagens recuperadas para revisão ou auditoria.
- A informação não precisa ser memorizada nos parâmetros do modelo e pode ser recuperada no momento da consulta.

Se a tarefa não depende de consulta externa, prompting pode ser suficiente. Se a necessidade principal é adaptar um comportamento estável que exemplos conseguem demonstrar, compare SFT. Essas abordagens podem ser combinadas quando há motivos claros para ambas.

## Avaliação e riscos

Avalie o recuperador com métricas de ranking/recuperação e confira se os trechos certos chegam ao contexto. Avalie a geração quanto a correção, apoio nas fontes, citações e tratamento de evidência insuficiente. Faça também avaliação ponta a ponta.

Falhas comuns incluem documentos ausentes ou desatualizados, segmentação inadequada, busca que não retorna a evidência, excesso de contexto, citações que não sustentam a resposta, exposição de dados sem permissão e instruções maliciosas em conteúdo recuperado. RAG pode reduzir alguns erros factuais, mas não elimina alucinações nem substitui controles de segurança.

## Componentes relacionados

- [[redes/ai-engineering/conceitos/algoritmos-de-recuperacao-lexical-e-vetorial.md|Recuperação lexical e vetorial]] e [[redes/ai-engineering/conceitos/busca-hibrida-e-reciprocal-rank-fusion-rrf.md|Busca híbrida e Reciprocal Rank Fusion]]: métodos para formar e combinar candidatos.
- [[redes/ai-engineering/conceitos/estrategias-de-chunking-e-otimizacao-de-rag.md|Chunking e otimização de RAG]]: organização do conteúdo e ajuste do pipeline.
- [[redes/ai-engineering/conceitos/embeddings.md|Embeddings]]: representação vetorial usada por sistemas semânticos.
- [[redes/ai-engineering/conceitos/rag-multimodal-e-dados-tabulares-text-to-sql.md|RAG multimodal e dados tabulares]]: extensões além de documentos textuais.
- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]] e [[redes/ai-engineering/conceitos/agentes-de-ia.md|Agentes de IA]]: padrões de arquitetura relacionados.
- [[redes/ai-engineering/conceitos/finetuning.md|Ajuste Fino]]: alternativa ou complemento, conforme o tipo de necessidade.

Para a arquitetura detalhada e técnicas do capítulo, veja [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao-rag.md|A nota detalhada sobre RAG]].

## Evidência nas fontes

Chip Huyen, *AI Engineering: Building Applications with Foundation Models*, cap. 6, seção RAG, pp. 253–275. O resumo local cobre o pipeline retriever-generator, busca lexical/vetorial/híbrida, métricas, otimização de recuperação e modalidades tabulares e multimodais; confira a edição consultada para citação.
