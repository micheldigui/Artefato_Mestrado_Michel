# AI Engineering: Building Applications with Foundation Models — Capítulo 8

## Objetivo do capítulo

Apresentar as metodologias e práticas de engenharia de conjuntos de dados (*Dataset Engineering*) voltadas ao treinamento e à adaptação de modelos de fundação. O capítulo detalha o paradigma da IA centrada em dados (*Data-Centric AI*), formaliza o "trio de ouro" da curadoria (qualidade, cobertura e quantidade de dados), explora técnicas de aquisição e anotação (incluindo o mecanismo de *data flywheel*), examina métodos tradicionais e generativos de aumento e síntese de dados (como *Self-Instruct*, instrução reversa e simulações), discute a destilação de conhecimento (*Teacher-Student*), investiga os riscos estruturais associados a dados sintéticos (colapso de modelo, imitação superficial e linhagem obscura) e sistematiza os processos operacionais de inspeção manual, deduplicação, limpeza, filtragem e formatação de datasets para ajuste fino.

## Resumo do argumento central

Com a comoditização dos modelos de fundação e a disseminação de ferramentas de ajuste fino acessíveis, os dados tornaram-se o principal elemento de diferenciação competitiva e qualidade de sistemas de inteligência artificial. O desempenho de um modelo reflete a qualidade dos dados com que foi alimentado: conjuntos pequenos e refinados superam regularmente bases massivas, porém ruidosas (conforme evidenciado pelo estudo LIMA e pela família Yi). A curadoria eficaz apoia-se em um equilíbrio rigoroso entre qualidade (relevância, alinhamento, consistência, formato, unicidade e conformidade legal), cobertura (diversidade temática, de formatos e tarefas) e quantidade (respeitando retornos decrescentes e prevenindo o fenômeno de ossificação). 

Diante do esgotamento iminente de textos públicos na web, a síntese de dados via IA emergiu como um motor essencial de escalabilidade, viabilizando a geração de instruções ricas, dados de raciocínio passo a passo (*Chain-of-Thought*) e dados de uso de ferramentas que seriam caros ou inviáveis de obter manualmente. No entanto, o uso indiscriminado de dados sintéticos introduz armadilhas severas, como a imitação superficial de estilo sem profundidade lógica, a amplificação de vieses e o risco de colapso de modelo (*Model Collapse*). Consequentemente, pipelines modernos de dados exigem mecanismos estritos de verificação automatizada (funcional e por IA) aliados à inspeção manual humana exaustiva, técnicas avançadas de deduplicação (via MinHash e filtros de Bloom) e remoção rigorosa de ruídos para garantir alinhamento determinístico nos modelos resultantes.

## Conceitos identificados

- Curadoria de Dados e o Trio de Ouro
- Qualidade e Conformidade de Dados
- Diversidade e Cobertura de Dados
- Síntese de Dados Tradicional e Simulação
- Síntese de Instruções e Self-Instruct
- Verificação e Filtragem de Dados
- Colapso do Modelo e Riscos de Dados Sintéticos
- Destilação de Modelos (Teacher-Student)
- Inspeção e Deduplicação de Dados
- Modelo de Fundação
- Ajuste Fino (Finetuning)
- Ajuste Fino Supervisionado (SFT)
- Auto-supervisão
- Engenharia de IA

## Sequência lógica do capítulo

1. **A Visão Centrada em Dados (*Data-Centric AI*, pp. 364–365):** Transição de benchmarks centrados em algoritmos para competições centradas na melhoria de datasets (Andrew Ng, DataComp, DataPerf, dcbench).
2. **Curadoria de Dados (pp. 365–380):** O trio de ouro (qualidade, cobertura e quantidade); requisitos de dados para tarefas complexas (Chain-of-Thought e uso de ferramentas com novos formatos multi-mensagem no Llama 3); atributos de qualidade e o estudo LIMA (Zhou et al., 2023); diversidade e coberturas temáticas (análise da mistura de dados de pré-treino, SFT e RLHF no Llama 3); quantidade, retornos decrescentes, ossificação paramétrica e o experimento SNLI da OpenAI; estratégias de aquisição, *data flywheel* e canais de dados públicos.
3. **Aumento e Síntese de Dados (pp. 380–396):** Justificativas estratégicas para síntese (escala, cobertura de cauda longa, superação de limitações humanas e privacidade); métodos tradicionais (regras, templates, transformações visuais, perturbações adversárias e simulações com CARLA, Waymo e robótica); métodos generativos por IA (simulação de APIs com StableToolBench, self-play de AlphaGo e Dota 2, paráfrase com MetaMath e retrotradução); síntese de instruções (*Self-Instruct*, Alpaca, UltraChat e instrução reversa); estudo de caso do pipeline de síntese de código do Llama 3; verificação automatizada de dados; limitações críticas dos dados sintéticos (imitação superficial de Gudibande et al., colapso de modelo de Shumailov et al. e amplificação de vieses); destilação de conhecimento (*Teacher-Student*).
4. **Processamento de Dados (pp. 396–403):** Inspeção manual de dados e o valor da análise exploratória; técnicas de deduplicação (documental, intra-documental e cruzada via comparação pareada, hashing e vetores) e seus impactos no desempenho; limpeza e remoção de artefatos web (HTML, Markdown indesejado e PII); formatação estrita de chat templates e alinhamento de máscaras de perda (*prompt loss weight*).

## Principais afirmações

- Na era dos modelos de fundação, a tecnologia base tornou-se uma commodity acessível; os dados proprietários com alta densidade informativa são o principal diferencial competitivo sustentável.
- Conjuntos pequenos de dados selecionados com rigor extremo de qualidade (ex.: 1.000 amostras no LIMA ou 10.000 no Yi) superam com folga centenas de milhares de exemplos ruidosos ou inconsistentes.
- Dados de código e matemática possuem valor desproporcional no treinamento: a inclusão concentrada dessas categorias na fase final (*annealing*) eleva expressivamente a capacidade geral de raciocínio de LLMs.
- O treinamento contínuo de modelos em grandes volumes de dados pode sofrer de ossificação (*ossification*), fenômeno no qual os pesos pré-treinados tornam-se rígidos e menos adaptáveis aos dados de ajuste fino do que redes menores ou treinadas do zero.
- Dados gerados por IA permitem superar certas limitações de dados humanos em tarefas onde o ser humano é naturalmente inconsistente ou incapaz de formular problemas de alta complexidade analítica.
- A imitação de modelos proprietários via destilação cega produz uma ilusão de competência: o modelo aluno absorve com facilidade o estilo formal do professor, mas falha em factualidade e em raciocínio sob distribuição adversária.
- O treinamento recursivo de modelos em dados sintéticos sem injeção contínua de novos dados humanos conduz inevitavelmente ao colapso do modelo (*Model Collapse*), destruindo as caudas longas da distribuição estatística.
- A inspeção manual e direta dos dados possui a maior relação valor-prestígio na engenharia de machine learning: quinze minutos de análise visual de amostras revelam problemas que horas de ajuste de hiperparâmetros não diagnosticam.

## Fórmulas ou procedimentos apresentados

- Proporção teórica ótima da mistura de dados pós-treino no Llama 3:

  $$\text{SFT:} \quad 52{,}7\% \text{ Conhecimento Geral}, \; 21{,}2\% \text{ Matemática/Raciocínio}, \; 14{,}9\% \text{ Código}, \; 3\% \text{ Multilíngue}, \; 8{,}1\% \text{ Exames}$$

- Pipeline de verificação e síntese de código (Llama 3):

  $$\text{Prompt} \to \text{Geração de Código} \to \text{Parser/Linter} \to \text{Testes Unitários em Sandbox} \to \text{Auto-correção}$$

- Formulação da divergência de colapso de modelo recursivo:

  $$\mathcal{D}_{\text{KL}}\Big(p_{\text{humano}}(x) \;\big\|\; q_{n+1}(x)\Big) > \mathcal{D}_{\text{KL}}\Big(p_{\text{humano}}(x) \;\big\|\; q_n(x)\Big)$$

- Deduplicação probabilística via filtros de Bloom e MinHash: mapeamento de $k$-shingles em tabelas hash para cálculo aproximado do coeficiente de Jaccard:

  $$J(A, B) = \frac{|A \cap B|}{|A \cup B|}$$

## Exemplos relevantes

- Estudo LIMA (Zhou et al., 2023): modelo Llama de 65B parâmetros ajustado com apenas 1.000 pares de instrução e resposta curados com rigor extremo foi preferido ou considerado equivalente ao GPT-4 em 43% das avaliações humanas.
- Estudo de ossificação por Hernandez et al. (2021): demonstração empírica de que modelos pequenos pré-treinados sofrem resistência plástica ao ajuste quando expostos a distribuições de domínio altamente divergentes.
- Experimento da Stanford com o Alpaca (Taori et al., 2023): uso de 175 sementes do Self-Instruct para gerar 52.000 instruções sintéticas via GPT-3 (text-davinci-003) a um custo de apenas US$ 500.
- Experimento de desduplicação de Hernandez et al. (2022): repetir apenas 0,1% dos dados 100 vezes durante o treino rebaixou o desempenho de um modelo de 800M parâmetros ao patamar de um modelo de 400M.

## Limitações e ressalvas

- As técnicas de síntese de instruções abordadas dependem da capacidade analítica do modelo gerador (professor); modelos professores fracos sintetizam dados com alucinações cumulativas.
- As formulações de mitigação de colapso de modelo baseadas em mistura de dados reais e sintéticos permanecem como campo empírico sem um limite matemático universal consolidado para a proporção ideal.

## Dúvidas em aberto

- Qual é o limiar exato de contaminação por dados sintéticos na internet aberta a partir do qual o pré-treinamento de novos modelos de fundação sofrerá degradação perceptível?
- Como desenvolver métodos de auditoria determinística que certifiquem a procedência de dados em modelos comerciais cujas empresas usaram síntese massiva?

## Localização da fonte

Capítulo 8, páginas 363 a 404 do livro impresso / arquivo de texto consolidado.
