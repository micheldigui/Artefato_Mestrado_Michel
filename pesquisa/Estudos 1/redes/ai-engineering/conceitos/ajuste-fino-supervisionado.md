# 🧠 Ajuste Fino Supervisionado (SFT)

**Rede:** `ai-engineering`  
**Área:** `treinamento`

## Definição

O **ajuste fino supervisionado** (*supervised fine-tuning*, SFT) adapta um modelo pré-treinado usando exemplos de entrada e resposta desejada. No caso de um assistente, esses exemplos costumam ser instruções, conversas ou tarefas acompanhadas de respostas revisadas. O modelo atualiza pesos para aumentar a probabilidade das respostas-alvo segundo o objetivo de treinamento.

O SFT é uma etapa de pós-treinamento e uma forma de treinamento; **não é sinônimo de ajuste fino eficiente em parâmetros**. O objetivo SFT pode ser aplicado atualizando todos os pesos ou usando uma técnica PEFT como LoRA.

## Para que serve

- Ensinar formato de conversa e seguimento de instruções.
- Adaptar tom, estilo de resposta, estrutura ou comportamento a uma tarefa recorrente.
- Melhorar desempenho em tarefas demonstráveis por exemplos de qualidade.

SFT não é a escolha padrão para inserir conhecimento factual que muda com frequência. Para informação externa atualizada, considere [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|RAG]]; para comportamento simples, compare primeiro com instruções e exemplos em contexto.

## Fluxo de trabalho

1. **Definir objetivo e avaliação:** descreva a tarefa e os critérios de sucesso antes de preparar os exemplos.
2. **Curar demonstrações:** verifique correção, cobertura, consistência, licenças e dados sensíveis; use o formato de conversa esperado pelo modelo.
3. **Separar dados:** mantenha treino, validação e teste em unidades independentes e remova duplicatas ou exemplos contaminantes entre partições.
4. **Treinar:** ajuste o modelo base com os exemplos. Em modelos de conversa, a perda costuma focar os tokens da resposta-alvo; o mascaramento exato depende do formato e do objetivo.
5. **Avaliar e comparar:** compare com o modelo base e uma linha de base por métricas da tarefa, comportamento em casos difíceis, regressões, segurança e custo.
6. **Implantar e monitorar:** controle versão do modelo, template de conversa e dados; acompanhe qualidade e mudanças dos casos de uso.

## Dados e limitações

- A qualidade, cobertura e consistência das demonstrações limitam o que o SFT pode ensinar.
- O modelo pode imitar erros, vieses ou respostas excessivamente confiantes presentes nos exemplos.
- Bons resultados no conjunto de treino não garantem generalização; divisão e avaliação precisam refletir o uso real.
- SFT não garante veracidade, segurança ou obediência perfeita. Avalie cada propriedade separadamente.
- Uma adaptação intensa pode prejudicar capacidades anteriores; compare o modelo adaptado com o modelo base em tarefas relevantes.

## Como se relaciona a outras técnicas

- [[redes/ai-engineering/conceitos/pos-treinamento-e-alinhamento.md|Pós-Treinamento e Alinhamento]]: SFT fornece demonstrações supervisionadas; pode anteceder a otimização com preferências.
- [[redes/ai-engineering/conceitos/otimizacao-direta-de-preferencia-dpo.md|DPO]] e [[redes/ai-engineering/conceitos/rlhf.md|RLHF]]: usam sinais de preferência e têm objetivos diferentes do par prompt-resposta do SFT.
- [[redes/ai-engineering/conceitos/ajuste-fino-eficiente-em-parametros-peft.md|PEFT]] e [[redes/ai-engineering/conceitos/lora.md|LoRA]]: reduzem quais parâmetros são treinados; podem ser usados para executar SFT.
- [[redes/ai-engineering/conceitos/finetuning.md|Ajuste Fino (Finetuning)]]: conceito mais amplo de atualização de um modelo pré-treinado.
- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]]: ajuda a decidir entre prompting, recuperação e treinamento.

Para detalhes de dados de demonstração, objetivo de treinamento e exemplos, veja [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado-sft.md|A nota detalhada sobre SFT]].

## Evidência nas fontes

Chip Huyen, *AI Engineering: Building Applications with Foundation Models*, cap. 2, seção de pós-treinamento, pp. 78–88; o resumo local também destaca SFT nas pp. 80–83. Use essas páginas como localizadores para conferir na edição consultada.
