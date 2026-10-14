# Inventário de Leitura de `docs`

Legenda de status:
- `lido`: li o conteúdo diretamente nesta revisão.
- `resumo_existente`: já havia resumo útil no acervo e foi aproveitado.
- `duplicado`: arquivo duplicado exato de outro item.
- `pendente`: ainda falta leitura integral detalhada.
- `fora_do_escopo`: não é artigo útil para o projeto ou é material administrativo/visual.

## Raiz de `docs`

| Arquivo | Tipo | Status | Observação |
|---|---|---:|---|
| `docs/dicas_orientador.txt` | txt | `lido` | Diretrizes do orientador; muito relevante para DSR, escrita e escopo |
| `docs/Informacoes sobre o programa de mestrado.txt` | txt | `lido` | Regras, missão, linhas e regimento do programa |
| `docs/dissertacao_v1.docx` | docx | `lido` | Versão extensa da dissertação |
| `docs/dissertacao_v1.pdf` | pdf | `lido` | Versão PDF da dissertação |
| `docs/EAD_Aditive_Multiplicative_27_10_revisado.ipynb` | ipynb | `lido_parcial` | Estrutura e células iniciais lidas; falta leitura integral célula por célula |

## `docs/revista`

| Arquivo | Tipo | Status | Observação |
|---|---|---:|---|
| `docs/revista/revista.docx` | docx | `lido` | Artigo em versão anterior |
| `docs/revista/revista_atualizada.docx` | docx | `lido` | Artigo em versão mais madura |
| `docs/revista/revista.pdf` | pdf | `lido_parcial` | Conteúdo consistente com as versões `.docx` |
| `docs/revista/texto_revista.txt` | txt | `lido` | Texto-base do artigo |
| `docs/revista/sumissão.txt` | txt | `lido` | Normas editoriais da revista |
| `docs/revista/~$vista_atualizada.docx` | docx | `fora_do_escopo` | Arquivo temporário do Word |

## `docs/Referencias_IA`

| Arquivo | Tipo | Status | Observação |
|---|---|---:|---|
| `docs/Referencias_IA/Resumo_Guia_Acesso.md` | md | `lido` | Guia de acesso e papel das referências |
| `docs/Referencias_IA/Simon_1996_Sciences_of_Artificial.pdf` | pdf | `lido_parcial` | Base filosófica do artificial/design |
| `docs/Referencias_IA/baixados_manual/Design_Science_in_Information_Systems_Research.pdf` | pdf | `lido_parcial` | Hevner et al. 2004 |
| `docs/Referencias_IA/baixados_manual/Peffers_2007_A Design Science Research Methodology for Information Systems Research.pdf` | pdf | `lido_parcial` | Peffers et al. 2007 |
| `docs/Referencias_IA/baixados_manual/Positioning and Presenting DSR for Maximum Impact.pdf` | pdf | `fora_do_escopo` | Arquivo salvo incorretamente; conteúdo real é um paper de dinâmica de fluidos, não DSR |
| `docs/Referencias_IA/baixados_manual/redictive Analytics in Information Systems Research.pdf` | pdf | `lido_parcial` | Fundamento para analytics preditivo em IS |
| `docs/Referencias_IA/BERT_Devlin_2018.pdf` | pdf | `lido_parcial` | Base do BERT |
| `docs/Referencias_IA/Attention_Is_All_You_Need_2017.pdf` | pdf | `lido_parcial` | Base Transformer |
| `docs/Referencias_IA/XGBoost_Chen_2016.pdf` | pdf | `lido_parcial` | Base do algoritmo |
| `docs/Referencias_IA/CatBoost_Dorogush_2018.pdf` | pdf | `lido_parcial` | Base do algoritmo |
| `docs/Referencias_IA/RMSE_vs_MAE_Chai_2014.pdf` | pdf | `lido_parcial` | Apoio para métricas |

## `docs/resumos_artigos`

Status geral:
- Resumos existentes lidos e aproveitados.
- Catálogo consolidado criado nesta revisão.

| Grupo | Status | Observação |
|---|---:|---|
| `resumos_artigos/*.md` sobre artigos científicos | `resumo_existente` | Base principal da triagem bibliográfica atual |
| `analise_sintopica_*.md` | `lido` | Síntese consolidada do corpus |
| `lote07_documentacao_tecnica_interna_consolidado.md` | `lido` | Resume documentação técnica interna |
| `catalogo_aproveitamento_artigos.md` | `lido` | Criado nesta revisão |

## Documentação interna útil em `docs/arquivos`

| Arquivo | Status | Observação |
|---|---:|---|
| `Análise de Relevância de Variáveis e Coluna Alvo.pdf` | `lido` | Explica por que a unidade de análise é diária e discute descarte de variáveis individuais no agregado |
| `Descrição das Colunas do Dataset Adaptado ().pdf` | `lido` | Documenta o schema inicial do dataset adaptado |
| `Documentação do Dataset Adaptado v2 ().pdf` | `lido` | Explica regras de dias letivos, feriados e emendas no dataset v2 |
| `Documentação__Integração_dos_Algoritmos_de_Predição.pdf` | `lido` | Descreve a arquitetura híbrida Flask + scripts offline de treino/predição |
| `Lista_de_Tarefas_Recomendações_de_Variáveis_e_Algoritmos.pdf` | `lido` | Checklist operacional já concluído |
| `Recomendações_de_Algoritmos_de_Machine_Learning_para_Predição.pdf` | `lido` | Recomenda XGBoost/LightGBM e afins para o horizonte de previsão |
| `Recomendações_de_Variáveis_Adicionais_para_Predição_de_Demanda.pdf` | `lido` | Lista variáveis adicionais prioritárias para elevar acurácia |
| `Relatório_de_Recomendações__Variáveis_e_Algoritmos_para_Predição.pdf` | `lido` | Consolida recomendações de variáveis e algoritmos com foco no IFSP |
| `Representação Visual do Sistema de Coleta e Predição.pdf` | `lido` | Resume arquitetura, fluxo de dados e interfaces do sistema |
| `Sistema_de_Coleta_de_Dados_para_Predição_de_Demanda_de_Refeições.pdf` | `lido` | Manual detalhado do sistema Flask de coleta e armazenamento |
| `Síntese de Variáveis e Algoritmos dos Artigos Analisados.pdf` | `lido` | Síntese operacional da literatura já convertida em recomendações |
| `Relato-Tecnico_2025_SIMPROF.pdf` | `lido` | Marco de EDA, Word2Vec e decomposição sazonal do projeto |
| `Relato-Tecnico_2025_SINGEP_CN.pdf` | `lido` | Enquadra o problema como cadeia de suprimentos e sistema produtivo |
| `relato_tecnico_simprof24.pdf` | `lido` | Versão inicial do projeto com regressão linear, formulário e dashboards |
| `Relatório de Novos Artigos Encontrados Online.pdf` | `lido` | Registro de prospecção bibliográfica complementar |
| `Relatório de Seleção de Artigos.pdf` | `lido` | Explica critérios e recorte da seleção bibliográfica |

## Artigos centrais já confirmados em `docs/arquivos`

| Arquivo | Classificação | Observação |
|---|---:|---|
| `1-s2.0-S0038012121000331-main.pdf` | `essencial` | Malefors et al. (2022); attendance forecasting em catering público com economia e redução de desperdício |
| `1-s2.0-S0959652623044232-main.pdf` | `essencial` | Rodrigues et al. (2024); previsão de curto prazo em food catering com redução prática de refeições desperdiçadas |
| `csam-30-5-485.pdf` | `essencial` | Kim et al. (2023); Word2Vec para cardápio e ensemble/stacking para prever clientes em cafeteria |
| `Forecasting and Modelling of Food Demand Supply Chain using Machine Learning.pdf` | `essencial` | Chaudhari et al. (2025); conecta previsão, supply chain e boosting |
| `s10163-023-01706-8.pdf` | `essencial` | Tang et al. (2023); previsão de resíduos alimentares em catering com ML |
| `Network-science-and-explainable-AIbased-life-cycle-management-of-sustainability-models_2024_Public-Library-of-Science.pdf` | `essencial` | Ipkovich et al. (2024); útil para XAI, SHAP e gestão do ciclo de vida dos modelos |
| `sustainability-17-00379.pdf` | `essencial` | Turker (2025); campus dining, variáveis contextuais e previsão de demanda/alimentação |
| `1-s2.0-S0959652624000799-main.pdf` | `apoio` | Akhter et al. (2024); comportamento de desperdício entre universitários |
| `foods-14-00126.pdf` | `apoio` | Lonska et al. (2025); intervenções contra plate waste em escolas |
| `1-s2.0-S0278612524000335-main.pdf` | `apoio` | Leng et al. (2024); enquadramento em Indústria 5.0 |
| `1-s2.0-S0924224424003637-main.pdf` | `apoio` | Upcycling em restaurantes e catering; útil para contexto de sustentabilidade, não para o core preditivo |
| `1-s2.0-S0924224425001062-main.pdf` | `apoio` | IA e segurança alimentar em catering aéreo; contexto lateral |
| `1-s2.0-S2949824424001800-main.pdf` | `nao_prioritario` | Reardon et al. (2024); práticas de chefs e desperdício em restaurantes, pouco aderente ao núcleo do RU |

## Artigos de apoio e enquadramento já confirmados em `docs/arquivos`

| Arquivo | Classificação | Observação |
|---|---:|---|
| `1-s2.0-S0956053X18303192-main.pdf` | `apoio` | Steen et al. (2018); fatores de risco para desperdício em escolas e pré-escolas |
| `1-s2.0-S0959652620329061-main.pdf` | `apoio` | Dhir et al. (2020); revisão sistemática sobre food waste em hospitalidade e food services |
| `1-s2.0-S095965262200837X-main.pdf` | `apoio_lateral` | Wu et al. (2022); intervenção por mídia social em comportamento alimentar |
| `1-s2.0-S2212267217304422-main.pdf` | `apoio` | Chapman et al. (2017); efeito de horário do almoço e recreio no consumo e no desperdício |
| `1-s2.0-S2352340921004224-main.pdf` | `apoio` | Eriksson et al. (2021); artigo de dados de attendance em escolas suecas |
| `1-s2.0-S2405844023075357-main.pdf` | `nao_prioritario` | Bathmanathan et al. (2023); sistema de gestão de resíduos em escola, pouco aderente ao core preditivo |
| `1-s2.0-S2666764921000035-main.pdf` | `essencial` | Xu et al. (2021); fundamento epistemológico e metodológico de ciência de dados |
| `1-s2.0-S2666789425000480-main.pdf` | `essencial` | Wicaksono et al. (2025); seleção de atributos e decisão orientada por ML em food service |
| `1-s2.0-S2773167724000165-main.pdf` | `nao_prioritario` | Review de tratamento biológico de resíduos orgânicos; contexto distante do problema do RU |
| `2015-new-school-meal-regulations-increase-fruit-consumption-and-do-not-increase-total-plate-waste.pdf` | `apoio` | Schwartz et al. (2015); mudanças regulatórias e plate waste em ambiente escolar |
| `2021 - Ensuring the Robustness and Reliability of Data-Driven Knowledge Discovery Models in Production and Manufacturing.pdf` | `essencial` | Tripathi et al. (2021); robustez, confiabilidade e GCRISP-DS |
| `2021-KeAI-Data science-connotation, methods, technologies, and development.pdf` | `essencial` | Duplicata temática/nominal de Xu et al. (2021) já usada como base de ciência de dados |
| `2024-JMS-Unlocking the power of industrial artificial intelligence towards Industry 5.0.pdf` | `apoio` | Duplicata nominal de Leng et al. (2024), útil para enquadramento em Indústria 5.0 |
| `Artificial intelligence in food system Innovative approach to.pdf` | `apoio` | Onyeaka et al. (2025); panorama macro de IA no sistema alimentar |
| `frai-04-576892.pdf` | `essencial` | Duplicata nominal do artigo de Tripathi et al. (2021) |
| `fnut-09-847547.pdf` | `apoio_lateral` | Scott e Ensaff (2022); hábitos alimentares no lockdown, útil só como pano de fundo |
| `environments-07-00103.pdf` | `apoio_lateral` | Sarić et al. (2020); determinantes ambientais e políticos das escolhas alimentares |
| `sensors-25-01548-v2.pdf` | `nao_prioritario` | Williams et al. (2025); pistache e imagens hiperespectrais, fora do escopo do RU |
| `sustainability-16-09279.pdf` | `apoio_lateral` | Stacchini et al. (2024); desperdício domiciliar entre universitários |
| `Sustainable farming with machine learning solutions for minimizing food waste.pdf` | `apoio` | Olawale et al. (2025); sustentabilidade e ML no agro, útil como contexto macro |

## Fechamento da sobra legível em `docs/arquivos`

| Arquivo | Classificação | Observação |
|---|---:|---|
| `A predictive modelling approach to decoding consumer intention for adopting energy-efficient technologies in food supply chains.pdf` | `apoio` | Rajendran et al. (2025); intenção do consumidor e Random Forest em food supply chain |
| `Exploring the potential of AI-driven food waste management strategies used in the hospitality industry for application in household settings.pdf` | `apoio_lateral` | Clark et al. (2024); adaptação de estratégias de hotelaria para domicílios |
| `05 - How to Conduct Rigorous Supervised Machine Learning in Information.pdf` | `apoio_metodologico` | Kühl et al. (2021); rigor em supervised ML para Information Systems |
| `2018-State-of-the-art in artificial neural network applications-A survey .pdf` | `nao_prioritario` | Survey genérico de ANN; amplo demais para sustentar o problema do RU |
| `2021-Deep Learning for AI.pdf` | `nao_prioritario` | Visão geral de deep learning; útil só como pano de fundo técnico genérico |
| `2024-A Survey on Evaluation of Large Language Models.pdf` | `fora_do_escopo` | LLMs e avaliação ampla; não ajuda no problema central |
| `2024-A_Review_on_Large_Language_Models_Architectures_Applications_Taxonomies_Open_Issues_and_Challenges.pdf` | `fora_do_escopo` | Review geral de LLMs; fora do foco do RU |
| `2024-A_Survey_of_Decision_Trees_Concepts_Algorithms_and_Applications.pdf` | `nao_prioritario` | Survey genérico de árvores de decisão; amplo demais |
| `2024-Comparative analysis of optmization strategies for k-means clustering in Big Data context.pdf` | `fora_do_escopo` | K-means em big data; não aderente ao problema |
| `2024-Toward a responsible future- recommendations for AI-enabled clinical decision support.pdf` | `fora_do_escopo` | IA clínica; fora do escopo |
| `2025 - Large language models are less effective at clinical prediction task than locally trained machine learning.pdf` | `fora_do_escopo` | Comparação LLM vs ML em contexto clínico; fora do problema do RU |

## Pastas com muitos PDFs duplicados

| Pasta | Status | Observação |
|---|---:|---|
| `docs/arquivos` | `em_andamento` | Coleção-base principal com PDFs únicos e administrativos |
| `docs/Artigos` | `duplicado_parcial` | Grande parte duplica itens de `arquivos` |
| `docs/dissertacoes` | `duplicado` | Todos os 19 PDFs verificados são duplicados exatos de `docs/arquivos` |
| `docs/Artigos_Selecionados` | `fora_do_escopo` | Pasta vazia |

## Pastas fora do foco bibliográfico principal

| Pasta | Status | Observação |
|---|---:|---|
| `docs/assets` | `fora_do_escopo` | Imagens e extrações visuais |
| `docs/contrato_empresa` | `lido` | Material administrativo lido para contexto institucional; não sustenta a revisão bibliográfica |
| `docs/projeto_seminario` | `lido` | Estrutura da pesquisa lida; útil para alinhar problema, objetivos, DSR e referências centrais |

## Próximos blocos de leitura

1. Fechar leitura integral dos PDFs metodológicos centrais de `Referencias_IA`.
2. Fechar leitura dedicada dos PDFs únicos de `docs/arquivos` que sustentam o projeto.
3. Marcar, item a item, os PDFs administrativos e laterais como `fora_do_escopo`.

## Notas confirmadas nesta etapa

- A pasta `docs/dissertacoes` não precisa de leitura independente: os 19 PDFs são duplicados exatos de arquivos já presentes em `docs/arquivos`.
- O arquivo `docs/Referencias_IA/baixados_manual/Positioning and Presenting DSR for Maximum Impact.pdf` está com nome incorreto ou foi salvo errado; o conteúdo extraído é de um artigo sobre estabilidade de cavidades com tampa móvel.
- `docs/contrato_empresa` foi lida para contexto institucional e contratual do RU, mas não acrescenta base teórica ou metodológica para os notebooks.
- Parte dos PDFs com nome em hash dentro de `docs/arquivos` está protegida com AES; no ambiente atual o extrator disponível (`pypdf`) não consegue abrir esses arquivos sem suporte criptográfico adicional.
- Entre os PDFs com hash que abriram normalmente, já foi possível identificar pelo menos materiais de dissertação do programa, como `d07cf2eb303a86cb223eb9e0b47dd430.pdf` (Matriz de Pugh em linha automotiva) e `d98e5690802e0e7db9812401fb96623c.pdf` (Machine Learning para previsão de vendas no varejo), que servem mais como apoio metodológico lateral do que como literatura central do RU.
