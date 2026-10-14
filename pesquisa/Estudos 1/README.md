# Segundo cérebro de Machine Learning

Este vault transforma materiais de estudo em redes separadas e conectadas de forma intencional:

- `_sistema/MOC_Segundo_Cerebro.md`: índice global das redes;
- `redes/<network_id>/conceitos/`: nós de conhecimento da rede;
- `redes/<network_id>/fontes/`: materiais catalogados, sem links conceituais;
- `redes/<network_id>/MOC.md`: mapa de cada domínio;
- `inbox/`: materiais ainda não classificados.

## Fluxo para um novo resumo

1. Coloque os `.txt` dos materiais na pasta de entrada da rede.
2. Execute na raiz do projeto:

   ```powershell
   py -3 .\pipeline_indexer.py --dir .\ML_Livros --out .\second_brain --network-id machine-learning --provider extrativo
   ```

3. Abra `_sistema/MOC_Segundo_Cerebro.md` no Obsidian e entre no MOC da rede.
4. Revise a nota do livro e transforme descobertas próprias nas seções `Notas pessoais` das notas canônicas.

Cada nota em `conceitos/` é uma ficha de estudo completa: definição, intuição, funcionamento, problema que resolve, hipóteses, quando usar, limitações, relações, exemplo mental, perguntas de revisão e evidência das fontes. O frontmatter separa `source_ids` (rastreabilidade) de `source_evidence` (ocorrências e seções indicadas no sumário); nenhum livro vira nó do grafo.
5. Se houver Ollama local, gere sínteses mais interpretativas com:

   ```powershell
   py -3 .\pipeline_indexer.py --dir .\ML_Livros --out .\second_brain --network-id machine-learning --provider ollama --model qwen2.5:7b
   ```

Para criar outra rede, copie `_sistema/network-profile.example.json`, ajuste a ontologia e execute:

```powershell
py -3 .\pipeline_indexer.py --dir .\materiais_irma --out .\second_brain --profile .\second_brain\_sistema\network-profile.example.json --network-id prova-irma --network-name "Preparação para prova"
```

O modo extrativo não inventa conteúdo: usa a ontologia, as definições editoriais do perfil, o sumário e a frequência de termos encontrados. A evidência automática é uma pista de rastreabilidade, não uma validação final nem substituto da leitura do capítulo. As notas canônicas são a camada de estudo; a frequência serve apenas como pista para decidir onde ler primeiro.

## Regra de manutenção

O pipeline pode regenerar notas canônicas e notas de fontes. Antes de rodá-lo novamente, preserve suas ideias pessoais em uma cópia, em um arquivo separado ou em um bloco que o pipeline passe a proteger. Fontes ficam em metadados e não são usadas como nós da rede.

## Reconciliacao de conceitos repetidos

Quando uma saida compilada de um novo capitulo for colocada na pasta de entrada do script, o splitter compara os conceitos com as notas canonicas existentes usando caminho, slug, titulo e aliases.

- conceitos novos sao gravados em `conceitos/`;
- conceitos repetidos nao sobrescrevem a nota canonica;
- o conteudo recebido e preservado em `revisao/repeticoes/`;
- cada repeticao e registrada em `revisao/repeticoes.log`;
- todas as repeticoes pendentes sao reunidas em `revisao/validacao-ia-repeticoes.txt`, que ja contem o prompt, as notas canonicas e as candidatas;
- a segunda execucao pula arquivos sem alteracao usando o hash registrado em `.split_obsidian_state.json`.

Execucao normal:

```powershell
.\split_obsidian_output.ps1
```

Para processar varios capitulos separados em uma pasta:

```powershell
.\split_obsidian_output.ps1 -InputRoot .\entradas\ai-engineering
```

Para processar um unico arquivo compilado, com varios blocos `===ARQUIVO: ...===`:

```powershell
.\split_obsidian_output.ps1 -InputFile .\entradas\ai-engineering-livro-completo.md
```

`-InputFile` e `-InputRoot` sao modos exclusivos. O arquivo unico pode ser gerado a partir do JSON, desde que convertido para Markdown mantendo os marcadores de arquivo. Em todos os modos, o splitter continua identificando somente arquivos compilados e ignorando notas Markdown ja splitadas.

Para forcar uma nova analise e atualizar os artefatos de revisao:

```powershell
.\split_obsidian_output.ps1 -Reprocess -Overwrite
```

O arquivo `revisao/validacao-ia-repeticoes.txt` deve ser enviado para a segunda analise da IA. A resposta deve ser somente JSON, seguindo o schema do proprio arquivo. O campo `action` pode ser `incorporate`, `discard` ou `manual_review`; depois, um aplicador pode usar essas decisoes para atualizar as notas canonicas com seguranca.
