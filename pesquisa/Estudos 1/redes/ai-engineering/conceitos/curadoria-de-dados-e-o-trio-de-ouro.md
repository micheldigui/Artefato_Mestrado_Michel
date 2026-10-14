# 🧠 Curadoria de Dados e o Trio de Ouro

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 365–377

## 📝 Definição

### Definição formal

A **Curadoria de Dados** (*Data Curation*) na [[redes/ai-engineering/conceitos/engenharia-de-ia.md|Engenharia de IA]] é a disciplina sistemática de seleção, auditoria, balanceamento e depuração de corpora de informação voltada a extrair o máximo desempenho de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] sob um orçamento computacional restrito. 

Seu arcabouço metodológico é governado pelo **Trio de Ouro (*Golden Data Trio*)**:

1. **Qualidade (*Data Quality*):** O grau de fidelidade factual, consistência sintática, alinhamento de comportamento e ausência de ruído nos exemplos de treino;
2. **Cobertura (*Data Coverage / Diversity*):** A representatividade e heterogeneidade de tópicos, tarefas, extensões e padrões de distribuição necessários para capacitar o modelo a responder com resiliência a situações fora da distribuição imediata;
3. **Quantidade (*Data Quantity*):** O volume de tokens ou pares rotulados calibrado contra a curva de retornos decrescentes e mitigador do fenômeno de **ossificação (*ossification*)**.

### Em linguagem simples

É o trabalho de selecionar os "melhores alimentos" para o cérebro da IA. Em vez de simplesmente jogar qualquer texto da internet no treinamento achando que quantidade resolve tudo, a equipe seleciona com cuidado exemplos impecáveis (Qualidade), garante que haja uma variedade grande de assuntos diferentes (Cobertura) e equilibra o tamanho da base de dados (Quantidade) para que o modelo aprenda de verdade sem viciar nem esquecer o que já sabia.

### Escopo e distinções

Diferencia-se da coleta cega de dados (*web scraping* bruto). A curadoria exige estabelecer uma especificação de engenharia: para tarefas com saídas complexas (como raciocínio em múltiplos passos e uso de ferramentas), o dataset deve conter demonstrações explícitas de estados intermediários e esquemas de controle compatíveis com a arquitetura do modelo.

## 🧩 Problema que resolve

Resolve a ineficiência econômica de treinar modelos com dados massivos, porém ruidosos. Evita o desperdício de tempo e recursos com conjuntos inchados que não trazem ganhos de acurácia em produção, além de prevenir a degradação comportamental causada pelo fenômeno da **ossificação**, no qual o modelo base torna-se rígido demais para assimilar novas distribuições de domínio especializado.

## 💡 Intuição

Pense no cardápio de treinamento de um atleta olímpico:

- **Qualidade:** Os alimentos devem ser frescos, ricos em nutrientes e livres de toxinas alimentares (se o atleta comer comida estragada, ele passa mal e não treina).
- **Cobertura:** O cardápio deve equilibrar proteínas, carboidratos, minerais e vitaminas (se ele comer apenas batata, terá carência de ferro e vitaminas).
- **Quantidade:** O volume calórico deve suprir o treino sem gerar obesidade mórbida (comer calorias em excesso traz retornos decrescentes e destrói o condicionamento físico do competidor).

## ⚙️ Como funciona

O processo de curadoria opera como uma esteira iterativa de planejamento, filtragem e dimensionamento:

### Etapas

1. **Mapeamento de Requisitos Comportamentais:** Identifica-se a modalidade exigida (respostas diretas, raciocínio passo a passo via Chain-of-Thought ou trajetórias com chamadas de função e mensagens de controle).
2. **Auditoria de Qualidade Preliminar:** Avalia-se se os exemplos são inequívocos e se o comportamento demonstrado reflete com precisão as diretrizes do produto.
3. **Equilíbrio de Cobertura de Domínio:** Calibra-se a mistura proporcional de áreas do conhecimento (conhecimento geral, matemática, raciocínio lógico e código).
4. **Estimativa de Escala e Retornos Decrescentes:** Treina-se o modelo com fatias reduzidas (ex.: 25%, 50% e 100% dos dados) para mapear a inclinação da curva de ganho de desempenho.
5. **Prevenção da Ossificação:** Se a base de ajuste fino for muito massiva ou divergir radicalmente da base de pré-treino, a equipe avalia se é mais vantajoso executar um pré-treino continuado em formato auto-supervisionado antes do SFT ou se compensa treinar um modelo específico do zero.

### Entradas e saídas

- **Entradas:** Metas de acurácia da aplicação, bases de dados brutas e orçamento de GPU.
- **Saídas:** Dataset balanceado, consistente e homologado para pipelines de pós-treinamento.

## 📐 Formulação matemática

O fenômeno dos **Retornos Decrescentes** em função da quantidade de dados de ajuste fino $N$ é modelado como uma relação log-linear:

$$\Delta_{\text{acurácia}} \propto \log(N)$$

Onde dobrar sucessivamente o volume de dados ($N \to 2N \to 4N$) entrega incrementos marginais de desempenho progressivamente menores:

$$\frac{d(\Delta_{\text{acurácia}})}{dN} = \frac{k}{N} \implies \lim_{N \to \infty} \frac{d(\Delta)}{dN} \to 0$$

A **Ossificação Paramétrica** (*Ossification*, Hernandez et al., 2021) descreve a perda de plasticidade na adaptação de um modelo com parâmetros $\theta$ previamente pré-treinados sob distribuição $\mathcal{D}_{\text{pre}}$ quando exposto a um dataset de finetuning $\mathcal{D}_{\text{ft}}$:

$$\|\nabla_\theta \mathcal{L}(\theta; \mathcal{D}_{\text{ft}})\| \ll \|\nabla_{\theta_{\text{random}}} \mathcal{L}(\theta_{\text{random}}; \mathcal{D}_{\text{ft}})\|$$

Onde a rede pré-treinada exibe resistência gradiente para escapar de mínimos locais estabelecidos na fase de pré-treino.

## 🧱 Hipóteses e condições de validade

- A superioridade de bases compactas pressupõe um modelo de fundação base já competente; modelos fracos de poucos parâmetros não conseguem generalizar a partir de pequenos conjuntos de alta qualidade com a mesma facilidade que modelos de grande porte.

## ✅ Quando usar

- Concepção de qualquer dataset para etapas de [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]], alinhamento de preferência e pré-treino continuado.
- Auditoria de dados para diagnosticar por que um pipeline de finetuning estagnou sem atingir o limiar de utilidade do negócio.

## 🚫 Quando não usar

- Em estratégias de adaptação puramente contextuais baseadas em engenharia de prompt simples, onde dados não são consumidos para ajuste de gradientes.

## ⚠️ Limitações e armadilhas

- **A falácia do inchaço de dados:** Contratar anotações manuais massivas de baixa qualidade acreditando que "o volume vai compensar o ruído". A literatura prova que 10.000 dados ruidosos geram modelos inferiores a 1.000 dados impecáveis.
- **Falta de diversidade de tarefas:** Conjuntos com milhares de exemplos idênticos focados em uma única sintaxe tornam o modelo frágil e incapaz de responder se o usuário alterar ligeiramente o comando.

## 🔍 Comparações

| Pilar da Curadoria | O que mede? | Sintoma de Falha se for Baixo | Métrica de Controle |
|---|---|---|---|
| **Qualidade** | Ausência de erros e clareza nos exemplos | Alucinações, respostas confusas e vícios | Taxa de concordância e inspeção manual |
| **Cobertura** | Variedade temática e estilística | Sobreajuste e incapacidade de generalizar | Entropia de tópicos e matriz de domínios |
| **Quantidade** | Volume absoluto de tokens/exemplos | Sub-aprendizado da sintaxe da tarefa | Curva de inclinação de perda de validação |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma startup quer treinar uma IA para resumir processos judiciais trabalhistas.

- *Cenário sem curadoria:* A equipe baixa 50.000 resumos de petições públicas da web. A maioria foi escrita por estagiários com erros gramaticais e estruturas inconsistentes. O modelo resultante fala com jargão confuso e erra cálculos de indenização.
- *Cenário com o Trio de Ouro:* A equipe seleciona apenas **800 processos** (**Quantidade enxuta**). Advogados seniores revisam cada um para garantir precisão jurídica absoluta (**Qualidade**). O conjunto abrange processos de 12 ramos diferentes: indústria, comércio, doméstico, tecnologia, etc. (**Cobertura**). O modelo resultante supera a versão anterior em todos os testes e foi treinado em um terço do tempo de GPU.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/ajuste-fino.md|Ajuste Fino (Finetuning)]]

### Complementos

- [[redes/ai-engineering/conceitos/qualidade-e-conformidade-de-dados.md|Qualidade e Conformidade de Dados]]
- [[redes/ai-engineering/conceitos/diversidade-e-cobertura-de-dados.md|Diversidade e Cobertura de Dados]]

### Alternativas

- Coleta massiva não curada de dados na web (*unfiltered web scraping*).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]
- [[redes/ai-engineering/conceitos/inspecao-e-deduplicacao-de-dados.md|Inspeção e Deduplicação de Dados]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 365–377
- **Evidência:** Chip Huyen formaliza o "trio de ouro" de curadoria de dados (qualidade, cobertura e quantidade), analisa os resultados do Llama 3 e da família Yi, discute os experimentos de retornos decrescentes de Chung et al. (2022) em relação ao número de tarefas e detalha o fenômeno de ossificação com base em Hernandez et al. (2021).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são os três componentes fundamentais do "Trio de Ouro" da curadoria de dados?
2. Por que um conjunto de dados pequeno e de altíssima qualidade é frequentemente superior a bases volumosas, porém ruidosas?
3. O que é o fenômeno da ossificação paramétrica (*ossification*) no treinamento contínuo de modelos de linguagem?
4. Como a relação entre a quantidade de dados e o ganho de acurácia reflete a lei dos retornos decrescentes?
5. De que forma a curadoria de dados para tarefas de raciocínio encadeado (Chain-of-Thought) difere da curadoria para respostas diretas?
6. Qual é a utilidade prática de se treinar modelos em fatias parciais de dados (25%, 50%, 100%) antes de consolidar o pipeline de treino?
7. Como a inclusão de dados com formatos e comprimentos heterogêneos fortalece a resiliência do modelo em produção?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Qualidade e Conformidade de Dados

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 368–369

## 📝 Definição

### Definição formal

A **Qualidade e Conformidade de Dados** (*Data Quality and Compliance*) é o conjunto de propriedades estruturais, semânticas, jurídicas e operacionais que determinam a aptidão de um dataset para guiar o aprendizado supervisionado ou por preferência de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]]. 

Estrutura-se em seis dimensões analíticas canônicas:

1. **Relevância (*Relevant*):** Alinhamento direto dos exemplos com a distribuição real das tarefas do produto;
2. **Alinhamento com Requisitos (*Aligned with task requirements*):** Aderência estrita aos critérios de negócio (ex.: factualidade, concisão ou criatividade);
3. **Consistência (*Consistent*):** Concordância mútua entre diferentes anotadores humanos e uniformidade de rótulos entre exemplos similares;
4. **Formatação Correta (*Correctly formatted*):** Ausência de artefatos residuais de raspagem (tags HTML, formatações de tabela quebradas, espaços extras);
5. **Unicidade Suficiente (*Sufficiently unique*):** Ausência de registros duplicados idênticos ou quase-idênticos que introduzam vieses;
6. **Conformidade Legal e Ética (*Compliant*):** Respeito incondicional a regulações de privacidade (LGPD, GDPR), remoção de dados pessoais identificáveis (PII) e observância a direitos autorais e licenças de dados.

### Em linguagem simples

É garantir que o material didático usado para ensinar a IA não contenha erros, não seja contraditório, não tenha sujeira de formatação de sites velhos e não viole as leis de privacidade. Se dois professores ensinam a mesma matéria de formas opostas, o aluno fica confuso; da mesma forma, se a base de treino tiver respostas malfeitas ou contraditórias, a IA se tornará imprevisível e insegura.

### Escopo e distinções

Não se confunde com métricas puramente matemáticas de tamanho de arquivo. Dados de alta qualidade são medidos pela sua **densidade informativa útil**. O estudo seminal LIMA (*Less Is More for Alignment*, Zhou et al., 2023) comprovou que treinar um modelo de 65B parâmetros em apenas 1.000 exemplos impecáveis gera respostas competitivas com os modelos mais caros do mercado.

## 🧩 Problema que resolve

Resolve a famosa máxima de computação *"garbage in, garbage out"* (se entra lixo, sai lixo). Elimina alucinações causadas por anotações imprecisas, impede processos jurídicos por vazamento de dados de clientes em respostas do modelo e evita a perda de tempo em pipelines de treino que não convergem devido a dados mal formatados.

## 💡 Intuição

Pense em um livro didático oficial adotado pelo Ministério da Educação para escolas públicas:

- Cada capítulo é revisado por especialistas para garantir que não haja erros científicos (**Alinhamento e Relevância**).
- Todos os professores seguem a mesma convenção ortográfica (**Consistência e Formato**).
- Os textos não trazem endereços residenciais ou dados bancários de ninguém (**Conformidade**).
- O livro não repete o mesmo exercício três vezes em páginas diferentes (**Unicidade**).

Estudar por esse livro forma alunos competentes; estudar por anotações rasgadas e rasuradas encontradas no chão gera estudantes confusos.

## ⚙️ Como funciona

O controle de qualidade e conformidade operacionaliza-se através de filtros em camadas:

### Etapas

1. **Elaboração da Diretriz de Anotação:** Cria-se um manual com regras semânticas inequívocas e exemplos de notas mínimas e máximas.
2. **Triagem de Relevância e Escopo:** Filtram-se exemplos que não correspondem às intenções operacionais do produto final.
3. **Higienização de Formato:** Scripts automatizados removem cabeçalhos web, tags XML/HTML órfãs, espaços em branco espúrios e normalizam caracteres Unicode.
4. **Varredura e Anonimização de PII:** Algoritmos dedicados e expressões regulares identificam e mascaram CPFs, e-mails, telefones e cartões de crédito.
5. **Auditoria de Concordância Inter-Anotador:** Calcula-se o percentual de consenso entre diferentes pessoas; amostras com pontuações divergentes são discutidas e reconciliadas.
6. **Validação de Licenças:** O setor jurídico certifica que a procedência dos dados autoriza o uso comercial sem restrições.

### Entradas e saídas

- **Entradas:** Dados brutos coletados internamente ou adquiridos de terceiros.
- **Saídas:** Dataset higienizado, auditado e juridicamente compatível com padrões industriais.

## 📐 Formulação matemática

A consistência de anotação entre múltiplos avaliadores sobre o conjunto de dados é quantificada por métricas de concordância inter-anotador, como o coeficiente **Kappa de Cohen** ($\kappa$) para dois anotadores:

$$\kappa = \frac{p_o - p_e}{1 - p_e}$$

Onde:

- $p_o$ é a proporção observada de concordância entre os rotuladores;
- $p_e$ é a probabilidade hipotética de concordância atribuível ao puro acaso.

Valores de $\kappa \ge 0{,}75$ indicam consistência sólida; valores baixos ($\kappa < 0{,}40$) evidenciam que as diretrizes de anotação estão confusas e precisam de reestruturação antes que os dados sejam usados no treino.

## 🧱 Hipóteses e condições de validade

- Assume que os avaliadores e especialistas que produzem ou revisam os dados possuem autoridade técnica no domínio e estão alinhados aos valores e políticas do produto.

## ✅ Quando usar

- Filtro mandatório antes de disparar qualquer procedimento de treinamento de modelo na camada de desenvolvimento.
- Concepção de datasets proprietários em setores altamente regulados (saúde, financeiro e jurídico).

## 🚫 Quando não usar

- Não há justificativa para ignorar qualidade e conformidade em aplicações corporativas de inteligência artificial.

## ⚠️ Limitações e armadilhas

- **Fadiga de Anotadores:** Pesquisas empíricas (Kern et al., 2024) comprovam que a qualidade das anotações humanas decai significativamente na segunda metade de um turno de trabalho devido ao cansaço e tédio, inserindo ruído silencioso no dataset.
- **Formatação de Chat Template Descalibrada:** Inserir dados de treino que utilizam quebras de linha ou cabeçalhos ligeiramente diferentes do esperado pelo modelo destrói a calibração de inferência.

## 🔍 Comparações

| Dimensão | Dados Ruidosos em Massa | Dados Curados sob o Estudo LIMA |
|---|---|---|
| **Volume de Amostras** | Centenas de milhares ($> 100.000$) | Compacto ($\approx 1.000$) |
| **Custo de Anotação** | Alto em volume total | Baixo a Médio (focado em especialistas) |
| **Consistência de Resposta** | Média a Baixa (estilos contraditórios) | **Altíssima (estilo unificado e polido)** |
| **Risco de Compliance** | Elevado (risco de vazamento de PII) | Praticamente nulo (auditoria individual) |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma fintech deseja treinar um modelo para atender clientes que pedem renegociação de dívidas.

- A equipe coleta 20.000 conversas de chats antigos. 
- Na **verificação de conformidade**, o filtro detecta que em 4.500 conversas os clientes digitaram seus números de cartão e senhas no chat; todos esses registros são mascarados por `[DADO_SENSÍVEL]`.
- Na **verificação de consistência**, eles descobrem que em 3.000 casos o atendente humano prometeu descontos que a política oficial do banco proíbe; esses exemplos são deletados do dataset para não ensinar a IA a dar descontos ilegais. 

O dataset final fica reduzido a 5.000 exemplos perfeitos, garantindo que o modelo aprenda apenas práticas financeiras aprovadas.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/inspecao-e-deduplicacao-de-dados.md|Inspeção e Deduplicação de Dados]]
- [[redes/ai-engineering/conceitos/verificacao-e-filtragem-de-dados.md|Verificação e Filtragem de Dados]]

### Alternativas

- Nenhuma relação suficientemente sustentada pelo capítulo (representa o conjunto canônico de requisitos de qualidade).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]
- [[redes/ai-engineering/conceitos/diretrizes-e-rubricas-de-avaliacao.md|Diretrizes e Rubricas de Avaliação]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 368–369
- **Evidência:** Chip Huyen conceitua os seis atributos de qualidade de dados (relevância, alinhamento, consistência, formato, unicidade e conformidade) e cita os resultados do artigo "LIMA: Less Is More for Alignment" (Zhou et al., 2023), que demonstrou que 1.000 exemplos selecionados alcançam competitividade direta contra o GPT-4.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as seis características canônicas que definem a qualidade e conformidade de um conjunto de dados para IA?
2. Qual foi a principal conclusão demonstrada pelo estudo científico LIMA (Zhou et al., 2023) sobre o volume de dados necessário para alinhamento?
3. Como a inconsistência de anotação entre diferentes especialistas prejudica o aprendizado de um modelo de fundação?
4. O que é a métrica Kappa de Cohen e qual é a sua aplicação na validação de diretrizes de rotulagem?
5. Por que a remoção de artefatos residuais de páginas web (como tags HTML) melhora a taxa de acerto do modelo ajustado?
6. Como o fenômeno da fadiga de anotadores humanos (Kern et al., 2024) afeta a integridade de conjuntos de dados longos?
7. Qual é a relação prática entre a diretriz de qualidade criada para avaliação e a especificação de dados usada no treinamento?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Diversidade e Cobertura de Dados

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 369–372

## 📝 Definição

### Definição formal

A **Diversidade e Cobertura de Dados** (*Data Coverage and Diversity*) é a propriedade estatística e representacional de um conjunto de treinamento que quantifica a dispersão e o equilíbrio heterogêneo de seus exemplos ao longo de múltiplos eixos ortogonais: domínios do conhecimento humano, tipologias de tarefas cognitivas (resumo, tradução, extração), distribuições de extensão de contexto, dialetos e formatos sintáticos de saída, garantindo que a parametrização do [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] não colapse em modos estreitos e preserve sua capacidade de generalização e raciocínio formal.

### Em linguagem simples

É a garantia de que a IA veja exemplos variados de verdade. Se você alimentar o modelo apenas com e-mails curtos e formais, ele se tornará incapaz de entender gírias, documentos longos ou código. Uma boa cobertura garante que o dataset misture assuntos técnicos, conversas casuais, textos em múltiplos idiomas e problemas de matemática para que a inteligência da IA seja ampla e resiliente.

### Escopo e distinções

A mistura ideal de dados varia conforme a fase do modelo. No pré-treinamento, o objetivo é absorver a estrutura estatística do mundo; no pós-treinamento supervisionado (SFT), o objetivo é cobrir a diversidade de pedidos dos usuários; e no alinhamento de preferência (RLHF/DPO), a diversidade equilibra as preferências subjetivas humanas.

## 🧩 Problema que resolve

Resolve a miopia operacional e o sobreajuste restrito (*narrow overfitting*). Modelos treinados com dados homogêneos perdem plasticidade, falham quando o usuário formula uma pergunta fora do padrão rígido de treino e podem sofrer quedas drásticas de raciocínio. A diversidade de tarefas e domínios força a rede neural a desenvolver representações latentes profundas e generalizáveis.

## 💡 Intuição

Pense na formação de um médico clínico geral:

- Se durante toda a faculdade e residência o médico atender apenas pacientes idosos com dor no joelho (**baixa cobertura e homogeneidade**), ele será incapaz de diagnosticar uma doença tropical em uma criança ou interpretar um eletrocardiograma de emergência.
- O currículo de medicina exige que o estudante passe por pediatria, cirurgia geral, psiquiatria, ginecologia e pronto-socorro (**alta diversidade e cobertura balanceada**), formando um profissional apto a lidar com a imprevisibilidade de qualquer paciente que entrar no consultório.

## ⚙️ Como funciona

A orquestração da diversidade opera através de matrizes de balanceamento de dados:

### Etapas

1. **Mapeamento de Eixos de Heterogeneidade:** Define-se os domínios necessários:
   - Domínio de Conhecimento: Ciências, Humanidades, Finanças, Notícias;
   - Domínio Estruturado: Código-fonte em múltiplas linguagens (Python, JS, SQL, Rust);
   - Domínio Racional: Problemas de matemática, dedução e quebra-cabeças lógicos;
   - Diversidade de Extensão: Amostras variando de 10 tokens a 32.000 tokens.
2. **Determinação da Mistura de Dados (*Data Mix*):** Modela-se a proporção exata de cada categoria em cada fase do treinamento.
3. **Injeção Estratégica de Código e Matemática:** Estudos empíricos provam que dados de código e matemática não servem apenas para ensinar a programar ou calcular; eles funcionam como catalisadores de raciocínio abstrato para o modelo inteiro.
4. **Recozimento de Dados (*Data Annealing*):** Na fase final do pré-treino, eleva-se progressivamente a proporção de dados de alta densidade informativa (código limpo e artigos matemáticos) acompanhada de uma redução na taxa de aprendizado, provocando saltos expressivos nos benchmarks de inteligência.

### Entradas e saídas

- **Entradas:** Corpora diversificados categorizados e rotulados tematicamente.
- **Saídas:** Um dataset combinado que maximiza o escore médio de avaliação multidimensional.

## 📐 Formulação matemática

O estudo empírico do **Llama 3** (Dubey et al., 2024) documenta como a distribuição proporcional ótima da mistura de dados se transforma drasticamente entre as etapas do ciclo de vida:

| Categoria Temática | Pré-Treinamento | Ajuste Fino Supervisionado (SFT) | Alinhamento de Preferência |
|---|---|---|---|
| **Conhecimento Geral (Inglês)** | $50{,}0\%$ | $52{,}66\%$ | $81{,}99\%$ |
| **Matemática e Raciocínio** | $25{,}0\%$ | $21{,}19\%$ | $5{,}89\%$ |
| **Programação e Código** | $17{,}0\%$ | $14{,}89\%$ | $6{,}93\%$ |
| **Multilíngue** | $8{,}0\%$ | $3{,}01\%$ | $5{,}19\%$ |
| **Tarefas Tipo Exame** | — | $8{,}14\%$ | — |
| **Contexto Longo** | — | $0{,}11\%$ | — |

No pré-treino e SFT, a soma de matemática e código compõe **mais de $36\%$ a $42\%$** de todo o treinamento, valor ordens de magnitude superior à presença natural dessas categorias na internet pública, comprovando que a cobertura deve ser artificialmente balanceada para privilégio de raciocínio formal.
O experimento de Zhou et al. (2023) com 2.000 amostras provou que modelos treinados em dados **diversos e de alta qualidade** superam em quase duas vezes a acurácia de modelos treinados apenas com qualidade sem diversidade.

## 🧱 Hipóteses e condições de validade

- A diversidade deve ser genuína e estrutural; adicionar centenas de variações cosméticas da mesma pergunta altera apenas o vocabulário superficial sem conferir ganho real de cobertura conceitual.

## ✅ Quando usar

- Concepção e calibração de pipelines de pré-treinamento e ajuste fino de modelos de fundação generalistas ou corporativos.
- Planejamento curricular de dados de modelos que atuarão como agentes autônomos em ambientes variados.

## 🚫 Quando não usar

- Em adaptadores LoRA hiper-especializados cujo único propósito contratual estrito seja executar uma única rotina determinística de formatação (onde a especialização extrema é o objetivo desejado).

## ⚠️ Limitações e armadilhas

- **O Dilema da Adição de Dados (*Data Addition Dilemma*, Shen et al., 2024):** Injetar dados heterogêneos desbalanceados ou de baixa compatibilidade distribucional pode, em certos cenários, degradar a performance do modelo em tarefas primárias em vez de aprimorá-la.
- **Sub-representação linguística:** Reservar menos de 5% a 8% para dados multilíngues perpetua a ineficiência de tokenização e eleva a taxa de erros em idiomas secundários.

## 🔍 Comparações

| Abordagem de Cobertura | Vantagem Primária | Ponto Cego Crítico |
|---|---|---|
| **Dataset Focado em Domínio Único** | Maestria rápida na tarefa específica | Perda catastrófica de capacidade de raciocínio geral |
| **Dataset Balanceado Multidomínio** | **Alta capacidade de transferência e generalização** | Exige esforço complexo de balanceamento de dados |
| **Raspagem Bruta sem Balanceamento** | Volume abundante e barato de dados | Reflete as assimetrias e vícios da internet aberta |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma equipe quer criar um assistente virtual para advogados tributaristas.

- Se o dataset contiver **apenas petições tributárias**, o modelo decora termos como "ICMS" e "imunidade tributária", mas falha miseravelmente quando o advogado pede para ele calcular a alíquota composta ou estruturar os dados em uma tabela JSON.
- A equipe aplica **alta cobertura**: insere 60% de petições jurídicas, 20% de exercícios de matemática financeira com passos de resolução e 20% de códigos Python e esquemas JSON. O modelo resultante passa a interpretar as leis, calcular os impostos com precisão e entregar a resposta estruturada diretamente na planilha do advogado.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]

### Complementos

- [[redes/ai-engineering/conceitos/qualidade-e-conformidade-de-dados.md|Qualidade e Conformidade de Dados]]
- [[redes/ai-engineering/conceitos/sintese-de-instrucoes-e-self-instruct.md|Síntese de Instruções e Self-Instruct]]

### Alternativas

- Treinamento em dados mono-temáticos puros.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]
- [[redes/ai-engineering/conceitos/fatiamento-de-dados-e-paradoxo-de-simpson.md|Fatiamento de Dados e Paradoxo de Simpson]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 369–372
- **Evidência:** Chip Huyen apresenta a Tabela 8-1 detalhando as proporções de dados em todas as fases do Llama 3 (Meta), discute a importância de código e matemática para o raciocínio global e analisa o experimento de Zhou et al. (2023) comparando modelos treinados sob diferentes regimes de qualidade versus diversidade (Figura 8-1).
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Cobertura e Diversidade de Dados e por que ela é indispensável para evitar o sobreajuste de modelos de fundação?
2. Por que conjuntos de dados de treinamento de LLMs contêm proporções artificialmente altas de código e matemática (frequentemente superiores a 35%)?
3. Como as proporções da mistura de dados se transformam entre o pré-treinamento, o SFT e o alinhamento de preferência no Llama 3?
4. O que é a técnica de "recozimento de dados" (*data annealing*) e qual o seu impacto na fase final de pré-treinamento?
5. Qual foi o resultado demonstrado pelo experimento de Zhou et al. (2023) ao comparar datasets que combinavam qualidade versus diversidade?
6. O que é o "Dilema da Adição de Dados" documentado por Shen et al. (2024)?
7. De que maneira a inclusão de diferentes extensões de contexto fortalece a resiliência do modelo contra o efeito *lost-in-the-middle*?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Síntese de Dados Tradicional e Simulação

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 380–386

## 📝 Definição

### Definição formal

A **Síntese de Dados Tradicional e Simulação** compreende as metodologias de geração procedural, algorítmica e mecânica de dados de treinamento concebidas sem a dependência obrigatória de grandes modelos de fundação generativos, estruturando-se em duas abordagens canônicas:

1. **Geração Baseada em Regras e Modelos (*Rule-based / Procedural*):** Uso de templates estáticos preenchidos estocasticamente por geradores de números ou bibliotecas sintéticas (como Faker), transformações afins determinísticas em imagens (rotações, cortes, inversões), substituições léxicas por dicionários e **perturbações adversárias** de ruído;
2. **Simulação em Ambientes Virtuais (*Simulation / Sim2Real*):** Criação de mundos físicos ou lógicos digitais parametrizados (motores gráficos como CARLA para direção autônoma ou simuladores de física para robótica e jogos) nos quais agentes interagem, experimentam e coletam telemetria de ações em ambientes de risco zero.

### Em linguagem simples

É a fabricação de dados falsos usando programas de computador comuns e simulações de videogame. Em vez de contratar pessoas ou mandar uma IA escrever textos, você usa regras fixas (como gerar 10.000 nomes e endereços falsos em um molde de nota fiscal) ou coloca um carro autônomo para dirigir dentro de um simulador de computador para aprender a desviar de pedestres sem colocar vidas em risco no mundo real.

### Escopo e distinções

Diferencia-se da síntese de dados baseada em LLMs. A síntese tradicional opera por regras lógicas determinísticas, equações físicas de cinemática ou distribuições probabilísticas conhecidas. Não sofre do risco de alucinação linguística, mas é restrita a domínios cujas regras possam ser programadas formalmente.

## 🧩 Problema que resolve

Resolve a escassez de dados para **eventos raros e perigosos**. Coletar dados reais de acidentes de carro na rodovia, falhas catastróficas em reatores nucleares ou movimentações financeiras de fraudes milionárias no mundo físico é arriscado, caro ou ilegal. A simulação gera milhões de cenários de emergência com custo mínimo e sem consequências materiais.

## 💡 Intuição

Pense no treinamento de astronautas da NASA:

- Você não coloca um astronauta novato em um foguete real com combustível verdadeiro para ele descobrir sozinho o que fazer se um motor pegar fogo na decolagem (**treinamento com dados reais arriscados**).
- Você o coloca dentro de um **simulador de gravidade e cabine espacial virtual** em terra firme. Os engenheiros inserem panes simuladas no sistema de oxigênio mil vezes. O astronauta desenvolve reflexos perfeitos no ambiente virtual antes de subir ao espaço (**metodologia Sim2Real**).

## ⚙️ Como funciona

O ciclo de síntese tradicional articula-se por regras algorítmicas de código:

### Etapas

1. **Definição de Regras e Gramáticas:** Mapeia-se a estrutura formal do dado pretendido (ex.: um esquema de transação de cartão de crédito ou equações de geometria euclidiana).
2. **Preenchimento Procedural:** Bibliotecas automáticas geram milhões de instâncias combinando variáveis aleatórias dentro de parâmetros predefinidos (ex.: AlphaGeometry da DeepMind treinado com 100 milhões de diagramas sintéticos).
3. **Aumento por Perturbação Adversária:**
   - Adiciona-se ruído estocástico imperceptível aos dados (como alterar o brilho, adicionar neve digital ou modificar pixels estratégicos em imagens);
   - A rede aprende a ser imune a ruídos e tentativas de ataques de classificação.
4. **Execução em Motor de Simulação:** Em robótica e direção autônoma (CARLA, Waymo SimulationCity), o agente opera em um motor gráfico 3D; o simulador calcula a física de atrito, iluminação e colisões e cospe logs de sensores (câmeras, LIDAR).
5. **Transferência Sim2Real:** Aplica-se técnicas de adaptação de domínio para garantir que a rede neural treinada no videogame virtual continue funcionando quando conectada aos sensores mecânicos do robô físico.

### Entradas e saídas

- **Entradas:** Modelos CAD, regras gramaticais de negócios e restrições de física do ambiente.
- **Saídas:** Datasets massivos de telemetria, imagens corrompidas ou formulários sintéticos limpos.

## 📐 Formulação matemática

No aumento por perturbação adversária para tornar um classificador $f_\theta$ robusto, o objetivo formula-se como uma otimização min-max (Goodfellow et al., 2014):

$$\min_\theta \mathbb{E}_{(x, y) \sim \mathcal{D}} \left[ \max_{\|\delta\| \le \epsilon} \mathcal{L}\Big(f_\theta(x + \delta), y\Big) \right]$$

Onde:

- $\delta$ é o ruído perturbador injetado sob uma restrição de magnitude $\epsilon$;
- O estudo seminal do **One Pixel Attack** (Su et al., 2017) comprovou que alterar a cor de apenas **1 único pixel** foi suficiente para fazer redes neurais profundas errarem $67{,}97\%$ das imagens do CIFAR-10, justificando o uso de perturbações no dataset de treino para fechar essas vulnerabilidades.

## 🧱 Hipóteses e condições de validade

- A simulação virtual deve espelhar com fidelidade suficiente a dinâmica matemática da realidade; se houver uma lacuna de fidelidade (*reality gap*), o modelo treinado na simulação sofrerá falha catastrófica no primeiro contato com o mundo real.

## ✅ Quando usar

- Direção autônoma (Waymo, Tesla), controle de braços robóticos industriais e drones.
- Geração preliminar de dados bancários de teste antes de obter autorização para lidar com dados sob sigilo bancário real.
- Problemas com sintaxes formais rígidas (como geração de expressões matemáticas, circuitos lógicos ou diagramas geométricos).

## 🚫 Quando não usar

- Em tarefas que exigem raciocínio aberto de conversação humana, interpretação de humor ou redação de ensaios literários, onde regras procedurais estáticas são incapazes de modelar a complexidade linguística.

## ⚠️ Limitações e armadilhas

- **O abismo de realidade (*Reality Gap*):** O robô aprende a empilhar caixas no simulador gráfico perfeito, mas falha no armazém físico real porque a iluminação do sol refletiu na esteira ou porque a poeira alterou o atrito das garras.
- **Vieses de simplificação em templates:** Formulários gerados por Faker tendem a ter distribuições uniformes artificiais (nomes sempre comuns, CEPs sempre válidos), deixando de treinar a IA para lidar com as loucuras e erros de digitação de clientes reais.

## 🔍 Comparações

| Modalidade | Custo de Geração | Realismo em Linguagem | Risco de Alucinação | Domínio Ideal |
|---|---|---|---|---|
| **Regras e Templates** | Quase zero | Muito baixo e rígido | **Zero (segue o molde)** | Dados transacionais e sintaxes |
| **Simulação Física** | Alto em desenvolvimento | Não aplicável | **Zero (segue a física do motor)**| Robótica e Carros autônomos |
| **Síntese por IA (LLM)** | Médio a Alto em tokens | **Máximo e fluente** | Alto (requer verificadores) | Diálogos, resumos e código |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma equipe de engenharia precisa treinar o sistema de visão de um trator autônomo para colher maçãs em pomares.

- *Problema:* É primavera e não há maçãs maduras para fotografar no campo real.
- *Solução por Simulação:* Os engenheiros constroem um pomar virtual em um motor gráfico 3D. Eles simulam macieiras com maçãs de diferentes tamanhos, adicionam chuva virtual, simulam o sol em 30 ângulos diferentes e geram **200.000 fotos sintéticas perfeitas**. O modelo de visão computacional é treinado no computador durante a primavera; quando o outono chega e as primeiras maçãs reais amadurecem, o trator entra no campo já sabendo identificá-las com precisão cirúrgica.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/qualidade-e-conformidade-de-dados.md|Qualidade e Conformidade de Dados]]

### Complementos

- [[redes/ai-engineering/conceitos/sintese-de-instrucoes-e-self-instruct.md|Síntese de Instruções e Self-Instruct]]

### Alternativas

- Coleta empírica manual de dados no mundo físico.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/verificacao-e-filtragem-de-dados.md|Verificação e Filtragem de Dados]]
- [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|Colapso do Modelo e Riscos de Dados Sintéticos]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 380–386
- **Evidência:** Chip Huyen aborda métodos tradicionais de síntese, detalha templates gerados por bibliotecas como Faker, cita o uso de 100 milhões de dados sintéticos no AlphaGeometry da DeepMind (Trinh et al., 2024), analisa perturbações adversárias como o One Pixel Attack (Su et al., 2017) e examina plataformas de simulação física como CARLA e Waymo SimulationCity.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Quais são as duas abordagens canônicas que compõem a síntese tradicional de dados anterior aos LLMs?
2. Como a geração baseada em regras e templates auxilia na conformidade e privacidade antes da liberação de dados reais?
3. O que é o desafio da transferência *Sim2Real* na aplicação de simulações virtuais para robótica física?
4. O que demonstrou a pesquisa seminal do *One Pixel Attack* (Su et al., 2017) sobre a robustez de redes neurais profundas?
5. De que maneira plataformas como CARLA e SimulationCity viabilizam o treinamento de veículos autônomos para eventos raros?
6. Como a DeepMind utilizou dados procedurais sintéticos no treinamento do modelo AlphaGeometry?
7. Quais são os limites estruturais que impedem o uso de métodos procedurais tradicionais em tarefas de geração de linguagem aberta?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Síntese de Instruções e Self-Instruct

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 386–391

## 📝 Definição

### Definição formal

A **Síntese de Instruções e Self-Instruct** (*Instruction Data Synthesis and Self-Instruct*) é o conjunto de metodologias semi-supervisionadas e automatizadas nas quais um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]] avançado é utilizado como gerador de dados para produzir pares rotulados de alta qualidade compostos por `(instrução, resposta)`, ampliando massivamente o acervo de treinamento para [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|SFT]] a partir de um pequeno núcleo inicial de exemplos humanos (*seed tasks*). 

Abrange duas estratégias primárias de geração:

1. **Self-Instruct Clássico (Wang et al., 2022; Alpaca, 2023):** O modelo ingere tarefas sementes humanas, sintetiza novas instruções não vistas, avalia sua novidade e gera as respectivas respostas ideais;
2. **Instrução Reversa (*Reverse Instruction*):** Inverte-se o fluxo de criação: toma-se um documento longo e de alta qualidade factual comprovada (livros, artigos científicos, Wikipedia) e instrui-se a IA a deduzir a pergunta ou comando que provocaria a geração daquele texto como resposta, contornando alucinações nas respostas.

### Em linguagem simples

É usar uma IA inteligente para criar as tarefas que outra IA vai usar para estudar. Em vez de pagar milhares de reais para redatores escreverem 50.000 perguntas e respostas perfeitas, você escreve apenas 100 exemplos iniciais com carinho (as sementes) e manda um modelo como o GPT-4 inventar milhares de outras perguntas parecidas e respondê-las. Outro truque genial é a instrução reversa: pegar um texto bom de verdade (como uma página da enciclopédia) e pedir para a IA adivinhar qual pergunta gerou aquele texto.

### Escopo e distinções

Diferencia-se da simples paráfrase. O Self-Instruct induz a criação de **novas tarefas inéditas**, expandindo a cobertura operacional de formatos e intenções. Constitui o alicerce fundamental do pipeline de treinamento de modelos de código aberto líderes como Llama 3 e Nemotron.

## 🧩 Problema que resolve

Resolve o estrangulamento financeiro e humano do Ajuste Fino Supervisionado (SFT). Anotar dados de instrução de alta complexidade (especialmente matemática, código e raciocínio formal) exige profissionais com pós-graduação e pode custar até 25 dólares por exemplo individual. A síntese por IA reduz esse custo para centavos e acelera o tempo de produção de meses para poucas horas.

## 💡 Intuição

Pense em um professor universitário experiente criando uma apostila de exercícios para seus monitores:

- O professor escreve à mão as primeiras 10 questões originais na lousa (**as tarefas semente**).
- Ele entrega a lousa para um assistente brilhante (**o modelo professor**) e diz: *"Crie 500 exercícios inéditos que exijam o mesmo tipo de raciocínio destas 10 questões, resolva todos eles com explicações passo a passo e monte um simulado completo para os calouros da graduação"*.

## ⚙️ Como funciona

O framework **Self-Instruct** opera através de um loop contínuo de geração, filtragem e desduplicação:

### Etapas

1. **Definição da Semente Humana:** Inicia-se com um acervo enxuto de alta diversidade (o Self-Instruct original usou apenas 175 tarefas humanas; o Alpaca usou 52.000 amostras geradas a partir dessa semente).
2. **Amostragem de Contexto:** O algoritmo sorteia estocasticamente 3 ou 4 tarefas semente e as insere em um prompt estruturado.
3. **Geração de Novas Instruções:** O modelo lê os exemplos e sintetiza uma instrução inédita, determinando autonomamente se a tarefa exige entradas complementares (ex.: um texto para resumir) ou apenas o comando.
4. **Poda e Filtragem de Qualidade:**
   - Descarta-se instruções muito curtas ou muito longas;
   - Descarta-se instruções idênticas ou com alta sobreposição léxica (*ROUGE-L*) com tarefas já salvas no banco;
   - Descarta-se comandos que contenham palavras de baixa utilidade.
5. **Geração da Resposta Ideal:** O modelo gera a resposta para a instrução recém-aprovada.
6. **Acúmulo e Auto-Alimentação:** O novo par `(instrução, resposta)` é anexado ao conjunto de dados e pode ser sorteado como semente para rodadas futuras.

### Entradas e saídas

- **Entradas:** 100 a 200 tarefas sementes humanas e acesso a uma API de modelo de fundação avançado.
- **Saídas:** Dezenas ou centenas de milhares de pares rotulados prontos para consumo por algoritmos de SFT.

## 📐 Formulação matemática

No método de **Instrução Reversa**, evita-se que o modelo alucine na resposta ao inverter a probabilidade condicional: Dada uma passagem factual perfeita $Y^* \in \mathcal{D}_{\text{humano}}$ (ex.: um parágrafo da Wikipedia), o modelo otimiza a geração do comando $X$:

$$X \sim P_{\text{LLM}}(\cdot \mid Y^*)$$

O par resultante $(X, Y^*)$ é garantido como sendo $100\%$ livre de alucinações na resposta, pois a resposta $Y^*$ foi redigida por humanos.
No pipeline de código do **Llama 3** (Dubey et al., 2024), a síntese automatizada integrou retrotradução com teste formal: Amostras sintéticas geradas passaram por validação de linter e execução de testes unitários:

$$\text{Filtro}(X, Y) = \begin{cases} \text{Aprovado}, & \text{se } \text{Linter}(Y) = 0 \;\; \land \;\; \text{ExecutaTestes}(Y) = \text{Sucesso} \\ \text{Reprovado}, & \text{caso contrário} \end{cases}$$

Onde cerca de $20\%$ das soluções de código que falharam inicialmente foram corrigidas autonomamente pelo próprio modelo através de prompts de auto-correção contendo o traceback de erro, alimentando uma base final de mais de $2{,}7 \text{ milhões}$ de exemplos de código sintético.

## 🧱 Hipóteses e condições de validade

- A qualidade intrínseca do modelo gerador dita a utilidade do dataset sintetizado; utilizar modelos de baixa capacidade como geradores povoa a base com erros sutis de lógica e vícios estilísticos.

## ✅ Quando usar

- Geração massiva de dados para ajuste fino de assistentes conversacionais e copilotos de programação.
- Expansão de janelas de contexto longo: fatiar documentos de 128K tokens em pedaços de 8K, gerar pares de perguntas e respostas sobre cada pedaço e utilizar o documento integral como contexto de treino.

## 🚫 Quando não usar

- Em domínios onde o modelo professor comprovadamente alucina com alta frequência e não existem ferramentas de verificação formal para auditar os resultados gerados.

## ⚠️ Limitações e armadilhas

- **Violação de Termos de Uso:** Provedores comerciais de ponta (como OpenAI) impõem restrições em seus contratos de serviço que proíbem explicitamente utilizar as saídas de seus modelos para treinar modelos concorrentes diretos.
- **Vício de verbosidade e clichês:** Dados gerados por LLMs tendem a incorporar preâmbulos artificiais (ex.: `"Com certeza! Aqui está..."`), que precisam ser higienizados antes do treino final.

## 🔍 Comparações

| Dimensão | Anotação Humana Clássica | Self-Instruct Tradicional | Instrução Reversa |
|---|---|---|---|
| **Custo financeiro** | Altíssimo ($10 a $25 por dado) | Muito baixo (centavos por dado) | Muito baixo |
| **Velocidade** | Semanas a meses | Horas a dias | Horas a dias |
| **Risco de alucinação** | Mínimo | Moderado na resposta | **Zero na resposta (usa base humana)**|
| **Escalabilidade** | Linear com orçamento humano | **Exponencial** | **Exponencial** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

A equipe do projeto **Alpaca** (Stanford, 2023) precisava criar um assistente instruído a partir do Llama 1 de 7B (que era apenas um modelo base de completação).
Eles pegaram as 175 sementes do **Self-Instruct** original. Em um script automatizado disparado contra a API do GPT-3 (text-davinci-003):

- O script gerou 52.000 novas conversas sobre culinária, código, história e tarefas do cotidiano;
- Filtrou duplicatas usando similaridade léxica de ROUGE;
- O custo total da fatura da API foi de menos de US$ 500.

Ao treinar o Llama de 7B com essa base sintética, o modelo transformou-se instantaneamente em um assistente conversacional fluido e educado, provando a viabilidade de criar modelos instruídos sem equipes gigantescas de rotuladores humanos.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]

### Complementos

- [[redes/ai-engineering/conceitos/verificacao-e-filtragem-de-dados.md|Verificação e Filtragem de Dados]]
- [[redes/ai-engineering/conceitos/destilacao-de-modelos-teacher-student.md|Destilação de Modelos (Teacher-Student)]]

### Alternativas

- Anotação manual humana via crowdsourcing.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|Colapso do Modelo e Riscos de Dados Sintéticos]]
- [[redes/ai-engineering/conceitos/cadeia-de-pensamento.md|Cadeia de Pensamento (Chain-of-Thought - CoT)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 386–391
- **Evidência:** Chip Huyen aborda a evolução da síntese de dados a partir do Self-Instruct (Wang et al., 2022) e do Alpaca (Taori et al., 2023), detalha a técnica de instrução reversa (Köksal et al., 2023; Li et al., 2023) e formaliza o pipeline industrial de síntese de código do Llama 3 (Dubey et al., 2024), que produziu mais de 2,7 milhões de exemplos verificados por linters e testes unitários.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é a metodologia Self-Instruct e como ela viabiliza a expansão de datasets a partir de poucas sementes humanas?
2. Como funciona a técnica de Instrução Reversa (*Reverse Instruction*) e qual problema de alucinação factual ela contorna?
3. Como o projeto Alpaca da Universidade de Stanford exemplificou a eficiência de custo da síntese de instruções via IA?
4. Quais foram as três etapas principais integradas no pipeline de síntese de código do Llama 3 (geração, testes e auto-correção)?
5. Qual é o papel das métricas de sobreposição de texto (como ROUGE) na etapa de filtragem do algoritmo Self-Instruct?
6. De que maneira dados sintéticos podem ser utilizados para treinar modelos a operarem com janelas de contexto muito maiores do que as originais?
7. Quais são as restrições legais e contratuais frequentemente impostas por grandes provedores comerciais sobre os dados sintetizados por suas APIs?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Verificação e Filtragem de Dados

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 391–393, 401

## 📝 Definição

### Definição formal

A **Verificação e Filtragem de Dados** (*Data Verification and Filtering*) é o estágio do pipeline de engenharia de conjuntos de dados no qual amostras brutas ou geradas sinteticamente são submetidas a baterias de testes determinísticos, analíticos e semânticos para identificar, podar e descartar registros corrompidos, errôneos, factualmente incoerentes ou de baixo valor informativo antes de sua incorporação aos dados de treino de um [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelo de fundação]]. 

A verificação opera sobre três modalidades fundamentais de auditoria:

1. **Verificação Funcional Determinística:** Execução real de amostras de código e consultas estruturadas em interpretadores e suítes de testes unitários isoladas ([[redes/ai-engineering/conceitos/correcao-funcional.md|correção funcional]]);
2. **Verificadores Baseados em IA (*AI Verifiers*):** Modelos especializados ou classificadores treinados para auditar consistência factual e atribuir pontuações de utilidade;
3. **Filtragem Heurística e Poda (*Data Pruning*):** Regras determinísticas de superfície (limites de caracteres, padrões de regex, balanceamento de classes e métricas de complexidade informacional).

### Em linguagem simples

É a "fiscalização sanitária" dos dados de treino. Não basta coletar textos ou mandar a IA inventar milhares de perguntas; é preciso conferir se o que foi gerado está certo antes de deixar o modelo estudar por aquele material. Códigos de programação passam por compiladores reais para ver se rodam; textos passam por IAs examinadoras e filtros que cortam frases muito curtas, repetitivas ou que contenham erros óbvios.

### Escopo e distinções

Diferencia-se da avaliação final do modelo. Aqui, o objeto de teste **não é o modelo treinado, mas o dado de treino em si**. Conecta-se à disciplina de poda de dados (*data pruning*), que busca selecionar o menor subconjunto representativo que maximiza o aprendizado da rede.

## 🧩 Problema que resolve

Resolve a contaminação do modelo por dados sintéticos alucinados ou textos da web corrompidos. Treinar um modelo com dados sintéticos sem verificação funciona como um amplificador de erros: o modelo base assimila alucinações como fatos reais e aprende padrões de código quebrados, tornando o ajuste fino inútil ou destrutivo.

## 💡 Intuição

Pense em uma fábrica de alimentos que produz barras de cereais:

- Os ingredientes chegam do caminhão do fornecedor (**dados brutos ou sintéticos**).
- Antes de misturar os cereais na masseira, o lote passa por uma esteira com detectores de metal (**filtros determinísticos**), sensores ópticos que ejetam grãos estragados (**verificadores de IA**) e análises químicas de laboratório (**testes funcionais**). Apenas os ingredientes aprovados entram na receita final.

## ⚙️ Como funciona

O processo opera através de filtros sequenciais em cascata de complexidade crescente:

### Etapas

1. **Filtros Heurísticos de Superfície:**
   - Descarta amostras vazias, com tamanho inferior a um limiar (ex.: menos de 5 palavras) ou extensas demais para o contexto;
   - Remove amostras onde a resposta gerada é apenas a repetição literal da pergunta;
   - Descarta textos com densidade anormal de símbolos de formatação ou caracteres quebrados.
2. **Verificação Funcional em Ambiente Seguro (Sandbox):**
   - Para amostras de programação: o código passa por linters estáticos (como Flake8) e é executado contra testes unitários; amostras que levantam exceções são ejetadas ou enviadas para auto-correção.
3. **Auditoria por Verificadores de IA:**
   - Um modelo neural avalia a [[redes/ai-engineering/conceitos/consistencia-factual.md|consistência factual]] do par `(contexto, resposta)`;
   - Classificadores de tópicos confirmam se a amostra pertence ao domínio de interesse do produto.
4. **Poda de Dados Baseada em Dificuldade (*Data Pruning*):**
   - Calcula-se o valor informativo de cada exemplo; amostras triviais que o modelo já domina com perda zero são descartadas para liberar capacidade de treinamento para exemplos mais difíceis.

### Entradas e saídas

- **Entradas:** Dataset bruto consolidado ou fluxo de dados sintéticos recém-gerados.
- **Saídas:** Conjunto de dados purificado, com taxa de erros reduzida e alta densidade informativa.

## 📐 Formulação matemática

A poda de dados (*Data Pruning*, Sorscher et al., Meta, 2022) seleciona um subconjunto $\mathcal{S}^* \subset \mathcal{D}$ com tamanho $|\mathcal{S}^*| = K < |\mathcal{D}|$ que minimiza o erro de generalização através de uma métrica de pontuação informacional $s(x)$:

$$\mathcal{S}^* = \arg\max_{\mathcal{S} \subset \mathcal{D}, |\mathcal{S}| = K} \sum_{x \in \mathcal{S}} s(x)$$

Onde a pontuação $s(x)$ pode derivar da margem de erro, da perplexidade sob o modelo base ou da distância no espaço de embeddings. Os autores comprovaram que a poda inteligente de dados permite quebrar a lei de potência clássica de escalonamento (*power law scaling*), atingindo o mesmo nível de acurácia com uma ordem de grandeza a menos de dados de treino.

## 🧱 Hipóteses e condições de validade

- Para verificação de código, deve existir um interpretador e uma suíte de asserções executáveis e idempotentes.
- Para filtros de IA, o modelo verificador deve possuir acurácia significativamente maior do que o modelo que sintetizou a amostra original para não aprovar alucinações sutis.

## ✅ Quando usar

- Mandatório na curadoria de qualquer conjunto de dados sintéticos produzidos por LLMs para evitar o [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|colapso do modelo]].
- Na preparação de dados raspados da internet para remoção de lixo textual antes de procedimentos de finetuning corporativo.

## 🚫 Quando não usar

- Não aplique podas agressivas sobre categorias de dados que representam eventos raros de cauda longa que o modelo precisa obrigatoriamente aprender a responder em produção.

## ⚠️ Limitações e armadilhas

- **Filtros heurísticos excessivamente restritivos:** Configurar regras rígidas de palavras proibidas que acabam descartando perguntas médicas ou legais perfeitamente legítimas contendo palavras sensíveis.
- **Custo computacional de verificadores neurais:** Usar modelos pesados de IA para auditar individualmente 10 milhões de amostras pode gerar custos de computação que superam o orçamento do próprio treinamento final.

## 🔍 Comparações

| Método de Verificação | Custo de Execução | Taxa de Falso Positivo | Aplicabilidade |
|---|---|---|---|
| **Heurísticas e Regex** | Quase zero (CPU) | Alta (regras rígidas demais) | Estrutura de texto e comprimento |
| **Execução Funcional (Sandbox)** | Baixo (tempo de CPU) | **Zero (o código roda ou não roda)**| Código, SQL e Matemática |
| **Verificadores por IA** | Moderado a Alto (GPUs) | Baixa a Média (depende do juiz) | Factualidade e estilo de prosa |
| **Poda Baseada em Perda (*Pruning*)**| Médio | Baixa | Otimização de volume de treino |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O time de engenharia da Meta sintetiza 3 milhões de problemas de programação para treinar o Llama 3.

- As funções são geradas por um LLM. Em vez de salvar os arquivos diretamente no banco de treino, cada função é despachada para um ambiente isolado (*sandbox*).
- O sistema roda um **linter estático** e detecta que $15\%$ das funções esqueceram de importar módulos como `math` ou `sys`.
- As funções que passam no linter são executadas contra 5 **testes unitários** automatizados. Cerca de $20\%$ falham na execução de casos com números negativos.
- Apenas as funções que compilam e passam em $100\%$ dos testes unitários são aprovadas para o dataset final. A base resultante é pura, imune a erros de compilação e pronta para ensinar o modelo a programar com rigor.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/qualidade-e-conformidade-de-dados.md|Qualidade e Conformidade de Dados]]

### Complementos

- [[redes/ai-engineering/conceitos/correcao-funcional.md|Correção Funcional (pass@k)]]
- [[redes/ai-engineering/conceitos/sintese-de-instrucoes-e-self-instruct.md|Síntese de Instruções e Self-Instruct]]

### Alternativas

- Treinamento cego sobre dados brutos sem etapas de auditoria intermediária.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|Colapso do Modelo e Riscos de Dados Sintéticos]]
- [[redes/ai-engineering/conceitos/inspecao-e-deduplicacao-de-dados.md|Inspeção e Deduplicação de Dados]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 391–393, 401
- **Evidência:** Chip Huyen discute a verificação de dados através de corretude funcional e verificadores por IA, apresenta as heurísticas clássicas de descarte do Self-Instruct (Wang et al., 2022) e analisa as métricas de poda de dados (data pruning) comprovadas por Sorscher et al. (Meta, 2022) para acelerar o aprendizado em ordens de magnitude.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Qual é a função da etapa de Verificação e Filtragem de Dados dentro da engenharia de conjuntos de dados?
2. Por que a verificação funcional por execução em interpretadores é a abordagem de maior autoridade para dados de programação?
3. Quais são as heurísticas clássicas de filtragem de superfície utilizadas no artigo seminal do Self-Instruct?
4. O que é a técnica de Poda de Dados (*Data Pruning*) e como o estudo da Meta (Sorscher et al., 2022) comprovou que ela pode quebrar leis de escala tradicionais?
5. Como os verificadores baseados em IA atuam na identificação de alucinações em amostras textuais sintéticas?
6. Qual é o perigo de se adotar filtros de regex e heurísticas excessivamente rígidas na preparação de datasets corporativos?
7. Por que dados sintéticos que contêm auto-correções baseadas em feedback de execução são especialmente valiosos para o treinamento de modelos de raciocínio?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Colapso do Modelo e Riscos de Dados Sintéticos

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 393–395

## 📝 Definição

### Definição formal

O **Colapso do Modelo e Riscos de Dados Sintéticos** compreende o conjunto de patologias estatísticas, epistêmicas e de governança que emergem quando [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]] são treinados ou ajustados a partir de conjuntos de dados compostos majoritária ou recursivamente por saídas geradas por outros sistemas de IA, estruturando-se em quatro vulnerabilidades principais:

1. **Colapso do Modelo (*Model Collapse*, Shumailov et al., 2023):** O processo degenerativo cumulativo no qual o treinamento sobre dados de gerações prévias de modelos faz com que a rede perca gradualmente a variância das caudas longas da distribuição real, esquecendo eventos raros e convergindo para estados matemáticos de entropia nula e saídas repetitivas;
2. **Imitação Superficial (*Superficial Imitation*, Gudibande et al., 2023):** A tendência de modelos ajustados com dados de destilação imitarem com maestria a prosa, o tom solene e o formato do modelo professor, mas falharem completamente em capacidade de raciocínio profundo e em factualidade;
3. **Amplificação de Vieses (*Bias Amplification*, Taori & Hashimoto, 2023):** A distorção cumulativa onde preconceitos e desbalanceamentos presentes na saída do modelo inicial são multiplicados a cada nova iteração do ciclo de dados;
4. **Ofuscação de Linhagem (*Obscure Data Lineage*):** A perda de rastreabilidade jurídica e de segurança, tornando impossível auditar se dados sintéticos herdaram violações de propriedade intelectual, PII vazada ou contaminação de benchmarks presentes nos pesos opacos do modelo gerador.

### Em linguagem simples

São os efeitos colaterais perigosos de alimentar a IA com comida artificial feita por outras IAs. Primeiro, a IA pode sofrer a síndrome da "xerox da xerox" (o colapso do modelo), ficando burra, esquecendo fatos raros e falando sempre as mesmas coisas. Segundo, ela aprende a ser um papagaio elegante: fala como um doutor educado, mas erra as contas básicas de matemática. E terceiro, se a IA que gerou os dados leu livros protegidos por direitos autorais sem permissão, o seu modelo herdará esses problemas jurídicos sem que você consiga auditar a origem.

### Escopo e distinções

Não significa que dados sintéticos sejam inúteis. Pelo contrário: dados sintéticos são vitais para o avanço da indústria. O conceito estabelece as **condições de contorno e limites de segurança** dentro dos quais a síntese pode ser aplicada, exigindo a injeção permanente de dados humanos e mecanismos externos de verificação formal.

## 🧩 Problema que resolve

Identificar esses riscos protege empresas de construírem produtos frágeis baseados em métricas de avaliação ilusórias. Evita que equipes invistam orçamentos massivos em destilação cega de modelos proprietários apenas para descobrir que o modelo resultante falha em cenários reais de estresse corporativo.

## 💡 Intuição

Pense em uma comunidade de contadores de histórias isolada em uma ilha:

- Na primeira geração, os habitantes contam histórias reais vividas no mar, na floresta e na vila, cheias de detalhes raros e aventuras imprevisíveis (**dados humanos reais**).
- Na terceira geração, ninguém mais vai ao mar; as pessoas passam o dia apenas recontando os resumos das histórias que ouviram dos pais (**treinamento recursivo com dados sintéticos**).
- Com o tempo, as lendas sobre tempestades raras e animais estranhos são esquecidas porque quase ninguém falava sobre eles; as histórias tornam-se todas iguais, previsíveis e infantis (**Colapso do Modelo**).

## ⚙️ Como funciona

O processo degenerativo atua ao longo de sucessivos ciclos de re-treinamento:

### Etapas

1. **Amostragem Tendenciosa:** Modelos de fundação operam por amostragem probabilística, favorecendo eventos de alta probabilidade ($p(x) \approx \max$) e gerando raramente eventos de cauda longa ($p(x) \to 0$).
2. **Alimentação da Próxima Geração:** O modelo $M_{n+1}$ é treinado sobre as saídas sintetizadas do modelo $M_n$.
3. **Erosão das Caudas Longas:** Como as saídas do modelo $M_n$ já não continham eventos raros em quantidade suficiente, o modelo $M_{n+1}$ passa a atribuir probabilidade zero a esses eventos raros.
4. **Acúmulo de Erros e Colapso Tardio (*Late Collapse*):** Em poucas gerações recursivas, a perda de densidade faz o modelo colapsar, emitindo sequências incompreensíveis ou repetindo monotonicamente o mesmo parágrafo para qualquer pergunta.
5. **A Ilusão da Destilação:** Um modelo de 7B treinado sobre saídas do GPT-4 aprende rapidamente a usar palavras formais, preâmbulos gentis e estruturação em tópicos; em avaliações subjetivas rápidas ele parece tão inteligente quanto o GPT-4, mas testes objetivos comprovam que sua capacidade factual não aumentou.

### Entradas e saídas

- **Entradas:** Dados sintéticos recursivos não filtrados ou gerados por modelos opacos.
- **Saídas:** Modelos degradados com colapso de variância, alucinações persistentes e riscos de litígio jurídico.

## 📐 Formulação matemática

O estudo de Shumailov et al. (2023/2024) formaliza o colapso precoce (*early collapse*) e tardio (*late collapse*) de estimadores de densidade. 
Seja $X_0 \sim p_0(x)$ o dataset original humano e seja $p_{n+1}(x)$ a distribuição ajustada sobre amostras de $p_n(x)$. Para um estimador gaussiano univariado $\mathcal{N}(\mu, \sigma^2)$, a variância amostral encolhe monotonicamente a cada geração recursiva $n$:

$$\mathbb{E}[\sigma_{n+1}^2] = \frac{M - 1}{M} \mathbb{E}[\sigma_n^2] \implies \lim_{n \to \infty} \mathbb{E}[\sigma_n^2] = 0$$

Onde $M$ é o número de amostras no lote de treino. A variância colapsa para zero, o que significa que o modelo perde a capacidade de representar qualquer diversidade além da média aritmética bruta.
Pesquisas contemporâneas (Gerstgrasser et al., 2024) comprovam que o colapso é evitado se e somente se uma fração constante de dados humanos limpos $\alpha \in (0, 1)$ for mantida na mistura de treino:

$$p_{\text{treino}}(x) = \alpha \, p_{\text{humano}}(x) + (1 - \alpha) \, p_{\text{sintético}}(x)$$

## 🧱 Hipóteses e condições de validade

- O colapso afeta fortemente modelos que treinam recursivamente sobre a totalidade de seus próprios dados sem curadoria; a injeção de dados sintéticos específicos que passam por verificadores formais determinísticos (como código compilado) não sofre a mesma taxa de degeneração.

## ✅ Quando usar

- Auditoria de risco metodológico e governança de dados em empresas que pretendem criar modelos fundacionais ou bases de clientes sintéticas.
- Diretriz para impedir que equipes descartem equipes humanas de rotulagem em favor de automação sintética cega de 100%.

## 🚫 Quando não usar

- Não utilize o risco de colapso como justificativa para banir totalmente dados sintéticos: dados sintéticos verificados por compiladores e testes unitários são seguros e essenciais para a indústria.

## ⚠️ Limitações e armadilhas

- **A armadilha da avaliação por juízes de IA:** Juízes neurais sofrem do [[redes/ai-engineering/conceitos/vieses-de-avaliacao-por-ia.md|viés de verbosidade e auto-preferência]], elogiando modelos que imitam a forma superficial do professor e mascarando a ausência de raciocínio real do modelo aluno.
- **Poluição acidental da web:** Modelos de scraping que coletam a internet após 2023 já estão consumindo dados sintéticos sem saber, exigindo filtros sofisticados de detecção de IA na origem.

## 🔍 Comparações

| Patologia de Dados Sintéticos | Mecanismo Primário | Efeito Prático no Modelo | Contramedida Canônica |
|---|---|---|---|
| **Colapso de Modelo** | Treinamento recursivo em dados de IA | Perda de caudas longas e repetição monótona | Injeção obrigatória de novos dados humanos |
| **Imitação Superficial** | Cópia do estilo formal do professor | Texto bonito com raciocínio lógico quebrado | Testes em benchmarks fora de distribuição |
| **Ofuscação de Linhagem** | O modelo professor memorizou e cuspiu dados com direitos autorais | Risco de processos legais por violação de propriedade intelectual | Rastreabilidade e curadoria de dados de treino |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O estudo empírico de Gudibande et al. (2023) colocou à prova a "falsa promessa de imitar LLMs proprietários": Pesquisadores treinaram um modelo de 7B parâmetros alimentado exclusivamente com conversas geradas pelo ChatGPT.

- Nos testes conversacionais comuns avaliados por humanos leigos, o modelo tirou notas altíssimas: ele falava de forma simpática, dizia `"Com certeza, posso te ajudar!"` e organizava tudo em tópicos impecáveis.
- Contudo, ao submeter o mesmo modelo a testes de **factualidade histórica e resolução lógica** (como GSM-8K e HumanEval), o desempenho foi medíocre e não superou o modelo base original. O modelo havia aprendido a imitar a casca elegante da conversa, mas continuava oco em capacidade de raciocínio.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/sintese-de-instrucoes-e-self-instruct.md|Síntese de Instruções e Self-Instruct]]

### Complementos

- [[redes/ai-engineering/conceitos/destilacao-de-modelos-teacher-student.md|Destilação de Modelos (Teacher-Student)]]
- [[redes/ai-engineering/conceitos/verificacao-e-filtragem-de-dados.md|Verificação e Filtragem de Dados]]

### Alternativas

- Manutenção de pipelines baseados estritamente em curadoria de dados de autoria humana documentada.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/alucinacao-em-modelos-de-fundacao.md|Alucinação em Modelos de Fundação]]
- [[redes/ai-engineering/conceitos/gargalos-de-escala.md|Gargalos de Escala: Dados e Energia]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 393–395
- **Evidência:** Chip Huyen aborda as quatro limitações críticas de dados gerados por IA, cita a pesquisa de Gudibande et al. (2023) sobre a ilusão de imitação, o artigo da Nature de Shumailov et al. (2023/2024) formalizando o Model Collapse por recursão matemática, o trabalho de Taori & Hashimoto sobre amplificação de viés e o perigo de ofuscação de linhagem de direitos autorais.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é o fenômeno do Colapso do Modelo (*Model Collapse*) e qual é o mecanismo probabilístico que o causa?
2. O que demonstrou a pesquisa de Gudibande et al. (2023) sobre a "falsa promessa" de se imitar modelos proprietários avançados?
3. Por que modelos de linguagem treinados via destilação superficial tendem a enganar avaliadores humanos em testes informais?
4. Como o treinamento recursivo com dados sintéticos atua sobre as caudas longas da distribuição estatística da linguagem?
5. Qual é o papel da preservação de dados de origem humana genuína na contenção e prevenção do colapso do modelo?
6. De que forma a ofuscação de linhagem de dados sintéticos gera riscos jurídicos de propriedade intelectual e direitos autorais?
7. Como os vieses algorítmicos podem ser amplificados ao longo de sucessivas gerações de modelos alimentadas por dados sintéticos?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Destilação de Modelos (Teacher-Student)

**Rede:** `ai-engineering`   **Área:** `modelagem`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 395–396

## 📝 Definição

### Definição formal

A **Destilação de Modelos** (*Model Distillation* ou *Knowledge Distillation*, Hinton et al., 2015) é a técnica de compressão e transferência de conhecimento no qual um modelo compacto e de menor complexidade computacional (**Aluno / *Student***) é treinado para reproduzir o comportamento preditivo, o raciocínio ou as distribuições de probabilidade de saída geradas por um modelo substancialmente maior, mais poderoso e computacionalmente pesado (**Professor / *Teacher***), mantendo uma fração expressiva do desempenho do modelo original com menor latência e custo reduzido de inferência.

### Em linguagem simples

É o treinamento de mestre e aprendiz. O professor é uma IA gigantesca, pesada e caríssima (como um modelo de 70 bilhões de parâmetros). O aluno é uma IA levinha e rápida (como um modelo de 7 bilhões ou menos). Você faz o aluno observar milhares de respostas dadas pelo professor até que o aluno aprenda a resolver as mesmas tarefas quase com a mesma perfeição, mas gastando dez vezes menos memória e respondendo muito mais rápido.

### Escopo e distinções

Na era clássica do aprendizado profundo, a destilação era feita comparando os vetores de *logits* contínuos suaves do professor diretamente com os do aluno (como no DistilBERT, Sanh et al., 2019). Na era dos modelos de fundação via API, a destilação opera predominantemente através de **dados sintéticos de caixa-preta**: o professor gera textos, explicações passo a passo e códigos, e o aluno passa por [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|SFT]] sobre essas saídas.

## 🧩 Problema que resolve

Resolve a inviabilidade econômica de se implantar modelos massivos em produção para tarefas repetitivas. Servir um modelo de 70B ou 175B parâmetros para atender milhões de consultas diárias gera faturas astronômicas de nuvem e latência inaceitável para usuários móveis. A destilação transfere as competências centrais daquele domínio para um modelo leve que cabe em hardware comercial ou dispositivos de borda (*edge*).

## 💡 Intuição

Pense em um consultor executivo internacional com 40 anos de experiência (o modelo professor) que cobra R$ 5.000,00 por hora de consultoria. A empresa contrata um jovem analista dedicado e inteligente (o modelo aluno) para acompanhar o consultor durante três meses. O analista anota como o mestre analisa balanços, copia seus modelos de relatório e absorve suas técnicas essenciais. Ao final do trimestre, o consultor é dispensado e o analista assume a rotina diária da empresa: ele cobra um salário normal, entrega os pareceres muito mais rápido e acerta $95\%$ das mesmas coisas que o consultor cobraria uma fortuna para fazer.

## ⚙️ Como funciona

O processo articula-se em três etapas de curadoria e transferência:

### Etapas

1. **Seleção do Modelo Professor:** Escolhe-se o modelo mais competente disponível no mercado (ex.: GPT-4o, Claude 3.5 Sonnet ou um Llama 3-70B).
2. **Geração do Corpus de Transferência:**
   - Despacha-se milhares de prompts variados e complexos para o modelo professor;
   - O professor gera respostas contendo explicações encadeadas (*Chain-of-Thought*), formatações estruturadas e códigos depurados.
3. **Treinamento do Modelo Aluno:** O modelo de fundação menor (ex.: Llama 3-8B ou Mistral-7B) é submetido a ajuste fino supervisionado sobre os dados gerados pelo professor.
4. **Bootstrapping Inverso (Caso Nemotron-4):** Em cenários avançados de pesquisa, o processo pode se inverter: modelos menores atuam como professores parciais para gerar volumes massivos de dados sintéticos que alimentam um modelo aluno que é, na verdade, **maior** que o professor (como no Nemotron-4 340B da NVIDIA, que usou o Mixtral 8x7B para sintetizar seus dados).

### Entradas e saídas

- **Entradas:** Conhecimento latente do modelo professor e prompts de especialização.
- **Saídas:** Modelo aluno comprimido, otimizado para inferência de alta velocidade e baixo custo.

## 📐 Formulação matemática

Na destilação clássica por concordância de probabilidades de Hinton et al., a função de perda balanceia a perda de entropia cruzada com os dados reais ($y$) e a divergência de Kullback-Leibler em relação às probabilidades do professor suavizadas por uma temperatura de destilação $T$:

$$\mathcal{L}_{\text{distil}} = (1 - \alpha) \mathcal{L}_{\text{CE}}\Big(p_{\text{aluno}}, y\Big) + \alpha T^2 \mathcal{D}_{\text{KL}}\left( \text{softmax}\left(\frac{z_{\text{professor}}}{T}\right) \;\Bigg\|\; \text{softmax}\left(\frac{z_{\text{aluno}}}{T}\right) \right)$$

Onde $z$ representa os logits brutos e $\alpha$ regula o peso relativo entre o dado real e a imitação do professor.
Na destilação contemporânea baseada puramente em texto sintético gerado por APIs fechadas (sem acesso aos logits do professor), a perda colapsa na perda de SFT padrão sobre a sequência $Y_{\text{professor}}$ gerada pelo professor:

$$\mathcal{L}_{\text{SFT\_aluno}}(\theta) = -\sum_{j=1}^M \log P\Big(y_{j, \text{professor}} \;\Big|\; X, y_{<j, \text{professor}}; \theta\Big)$$

O caso do **DistilBERT** (Sanh et al., 2019) comprovou que é possível reduzir o tamanho do BERT em $40\%$, torná-lo $60\%$ mais rápido na inferência e preservar $97\%$ de sua capacidade de compreensão de linguagem.

## 🧱 Hipóteses e condições de validade

- A licença comercial do modelo professor deve autorizar explicitamente o uso de suas saídas para treinar outros modelos; violar termos de serviço de APIs fechadas gera passivos contratuais e riscos de bloqueio.
- As saídas do professor devem passar por [[redes/ai-engineering/conceitos/verificacao-e-filtragem-de-dados.md|verificação de dados]] para não transferir alucinações e preconceitos para o aluno.

## ✅ Quando usar

- Quando a empresa precisa reduzir custos operacionais de API em até $80\%$ a $90\%$ migrando de um modelo comercial fechado para um modelo próprio leve hospedado internamente.
- Aplicações com restrições extremas de latência de resposta que demandam modelos de menos de 8 bilhões de parâmetros rodando localmente.

## 🚫 Quando não usar

- Se a tarefa exigir conhecimento enciclopédico aberto massivo sobre milhões de tópicos mundiais dispersos que simplesmente não cabem fisicamente no número reduzido de parâmetros do modelo aluno.

## ⚠️ Limitações e armadilhas

- **O risco da imitação oca:** Conforme advertido pelo conceito de [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|imitação superficial]], o modelo aluno pode aprender a falar com o mesmo vocabulário pomposo do professor sem herdar a sua capacidade real de raciocinar sobre fatos novos.
- **Transmissão de vieses do professor:** Todos os pontos cegos e alucinações sistemáticas do modelo professor são internalizados como verdades absolutas pelo modelo aluno.

## 🔍 Comparações

| Característica | Modelo Professor (Teacher) | Modelo Aluno Destilado (Student) |
|---|---|---|
| **Escala de parâmetros** | Gigantesca (70B a centenas de bilhões) | Compacta (1B a 8B parâmetros) |
| **Custo por milhão de tokens** | Alto | **Extremamente baixo** |
| **Latência por token (TPOT)** | Mais lenta | **Ultrarrápida** |
| **Hospedagem em Edge** | Impossível em celulares comuns | **Perfeita para notebooks e dispositivos locais** |
| **Generalização fora de domínio** | Ampla e profunda | Focada nas tarefas destiladas |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

O portal de notícias BuzzFeed precisava de um modelo de IA para gerar quizzes e artigos criativos em escala massiva para milhões de visitantes simultâneos.

- Usar a API do **GPT-3 (text-davinci-003)** diretamente em todas as requisições de milhões de usuários gerava uma fatura mensal de nuvem proibitiva.
- A equipe gerou milhares de exemplos perfeitos de quizzes utilizando o GPT-3 como **modelo professor**.
- Em seguida, pegou o modelo aberto e leve **Flan-T5** como **modelo aluno** e aplicou ajuste fino supervisionado com adaptadores LoRA sobre esses dados do professor.
- O resultado foi um modelo leve proprietário que reduziu o custo de inferência em **80%**, mantendo o mesmo estilo descontraído e engajador do modelo maior.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/ajuste-fino-supervisionado.md|Ajuste Fino Supervisionado (SFT)]]

### Complementos

- [[redes/ai-engineering/conceitos/sintese-de-instrucoes-e-self-instruct.md|Síntese de Instruções e Self-Instruct]]
- [[redes/ai-engineering/conceitos/fases-de-inferencia-prefill-e-decode.md|Fases de Inferência: Prefill e Decode]]

### Alternativas

- Quantização pura sem re-treino ou podas diretas de parâmetros.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/colapso-do-modelo-e-riscos-de-dados-sinteticos.md|Colapso do Modelo e Riscos de Dados Sintéticos]]
- [[redes/ai-engineering/conceitos/quantizacao.md|Quantização]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 395–396
- **Evidência:** Chip Huyen formaliza a destilação de conhecimento baseada em Hinton et al. (2015), cita os ganhos históricos do DistilBERT (Sanh et al., 2019), analisa a destilação do Alpaca a partir do text-davinci-003, o caso corporativo do BuzzFeed com Flan-T5 e demonstra o bootstrapping em larga escala do Nemotron-4 340B da NVIDIA treinado a partir do Mixtral 8x7B.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é Destilação de Modelos e qual é a analogia central do paradigma Professor-Aluno?
2. Quais são os benefícios de negócio em termos de custo de infraestrutura e latência proporcionados pela destilação?
3. Como o caso do DistilBERT (Sanh et al., 2019) quantificou empiricamente os trade-offs de tamanho, velocidade e retenção de capacidade?
4. Qual é a diferença técnica entre a destilação clássica via divergência de logits e a destilação moderna baseada em dados sintéticos de texto?
5. Por que as licenças comerciais de modelos de fundação frequentemente proíbem o uso de suas saídas para destilação de modelos concorrentes?
6. Como o projeto Nemotron-4 da NVIDIA ilustrou que um modelo aluno pode, em certos cenários, ser maior do que o modelo professor que gerou os dados?
7. Qual é o perigo da "imitação superficial" no processo de destilação de modelos de linguagem?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

# 🧠 Inspeção e Deduplicação de Dados

**Rede:** `ai-engineering`   **Área:** `dados`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 8 — Dataset Engineering
- Localização: Páginas 396–403

## 📝 Definição

### Definição formal

A **Inspeção e Deduplicação de Dados** (*Data Inspection and Deduplication*) compreende o conjunto de intervenções analíticas, empíricas e probabilísticas aplicadas na etapa de processamento de dados para treinamento e ajuste fino de [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|modelos de fundação]]:

1. **Inspeção Manual de Dados (*Manual Data Inspection*):** A auditoria direta, visual e exploratória de amostras individuais, distribuições de tokens, pares verbo-objeto e anomalias estatísticas conduzida por humanos para identificar padrões de erro tácitos e falhas sistêmicas de formatação;
2. **Deduplicação de Dados (*Data Deduplication*):** O processo algorítmico de detecção e purgação de redundâncias textuais idênticas ou quase-idênticas em três níveis de granularidade — **documental integral** (documentos repetidos), **intra-documental** (parágrafos repetidos dentro da mesma página) e **cruzada** (citações, termos legais repetidos ou templates compartilhados) —, implementado através de buscas exatas, comparação de $n$-grams, redução de dimensionalidade e técnicas de espalhamento probabilístico como **MinHash** e **Filtros de Bloom**.

### Em linguagem simples

É o ato indispensável de "olhar para os seus dados com os próprios olhos" e passar um pente fino para deletar coisas repetidas. Olhar 15 minutos de dados ensina mais do que passar um dia inteiro chutando parâmetros no código. A deduplicação garante que a mesma frase ou resposta não apareça dezenas de vezes no material de estudo da IA, impedindo que ela decore respostas prontas e fique enviesada.

### Escopo e distinções

Não serve apenas para diminuir o tamanho do arquivo em disco. A literatura técnica comprova que dados repetidos induzem o modelo à **memorização mecânica prejudicial**, amplificam vieses estatísticos indesejados e causam vazamento entre treino e teste (**contaminação de dados**).

## 🧩 Problema que resolve

Resolve a distorção da distribuição de probabilidades aprendida pela rede neural. Se um anúncio ou texto repetitivo aparecer 100 vezes no dataset, a atenção do modelo aprenderá que aquelas palavras específicas são universalmente importantes, distorcendo o raciocínio em novos contextos. Um estudo da Anthropic demonstrou que repetir apenas **$0{,}1\%$ dos dados 100 vezes** faz um modelo de 800M parâmetros degradar seu aprendizado para o nível de um modelo de 400M.

## 💡 Intuição

Pense em estudar para uma prova de biologia lendo uma pilha de resumos xerocados:

- Se alguém acidentalmente tirou 50 cópias idênticas da mesma página sobre "células vegetais" e misturou no meio do seu fichário, você passará metade do tempo de estudo relendo exatamente as mesmas três frases sobre clorofila (**dados duplicados**).
- Seu cérebro ficará exausto, você gastará tempo à toa e deixará de estudar zoologia e anatomia humana (**perda de capacidade de generalização**). A deduplicação joga as 49 cópias repetidas no lixo antes de você abrir o fichário.

## ⚙️ Como funciona

O pipeline opera articulando análise humana preliminar com algoritmos de espalhamento em escala:

### Etapas

1. **Inspeção Exploratória Manual:**
   - O engenheiro plota gráficos de dispersão de tokens, comprimentos de entrada e saída e relações sintáticas (como a distribuição de pares verbo-substantivo);
   - Lê manualmente dezenas de exemplos aleatórios para checar se a formatação faz sentido e se a instrução não contradiz a resposta.
2. **Detecção de Duplicatas Exatas:**
   - Aplica-se hashing criptográfico direto (como SHA-256) linha por linha ou documento por documento para eliminar registros idênticos em tempo $\mathcal{O}(N)$.
3. **Detecção de Quase-Duplicatas (*Near-Deduplication* com MinHash e LSH):**
   - Fatiam-se os textos em pequenos pedaços de palavras (*shingles* ou $n$-grams);
   - O algoritmo **MinHash** projeta esses conjuntos de palavras em assinaturas numéricas compactas;
   - Agrupam-se textos com assinaturas parecidas usando **Locality-Sensitive Hashing (LSH)** em buckets de candidatos prováveis;
   - Calcula-se a similaridade de Jaccard apenas entre candidatos do mesmo bucket; se a sobreposição for superior ao limiar (ex.: $\ge 80\%$), o documento duplicado é descartado.
4. **Filtragem por Filtros de Bloom:**
   - Estrutura de dados probabilística ultra-eficiente em memória que testa instantaneamente se um n-gram ou frase já foi vista anteriormente na esteira de dados.

### Entradas e saídas

- **Entradas:** Base bruta de texto não tratado com potenciais cópias e redundâncias.
- **Saídas:** Acervo purificado contendo apenas instâncias informacionalmente únicas.

## 📐 Formulação matemática

A similaridade entre dois documentos $A$ e $B$ representados por seus conjuntos de $n$-gramas $S(A)$ e $S(B)$ é medida pelo **Coeficiente de Similaridade de Jaccard**:

$$J(A, B) = \frac{|S(A) \cap S(B)|}{|S(A) \cup S(B)|}$$

O algoritmo **MinHash** utiliza uma família de $K$ funções hash independentes $h_k$ ($k \in \{1, \dots, K\}$). A probabilidade de duas assinaturas hash colidirem é matematicamente idêntica à similaridade de Jaccard:

$$P\Big(\min(h_k(S(A))) = \min(h_k(S(B)))\Big) = J(A, B)$$

Permitindo estimar a similaridade de textos com milhões de caracteres em tempo constante $\mathcal{O}(K)$ através da comparação de vetores compactos de assinaturas, dispensando a comparação par a par quadrática $\mathcal{O}(N^2)$.

## 🧱 Hipóteses e condições de validade

- O limiar de similaridade de corte de Jaccard (ex.: 0.8 ou 0.9) deve ser calibrado para o domínio; em áreas como direito, dois contratos com cláusulas idênticas podem divergir apenas em uma linha crucial de valor monetário, exigindo preservação cuidadosa.

## ✅ Quando usar

- Pré-processamento obrigatório em qualquer dataset coletado da internet para pré-treino continuado ou ajuste fino.
- Higienização de bases de dados de produtos de comércio eletrônico, onde descrições de itens quase idênticos poluem o catálogo.
- Prevenção de vazamento entre conjunto de treino e conjunto de teste de avaliação.

## 🚫 Quando não usar

- Em dados transacionais onde repetições idênticas de compras representam frequências estatísticas reais indispensáveis para o cálculo de probabilidade do negócio.

## ⚠️ Limitações e armadilhas

- **Falsos Positivos em Filtros de Bloom:** Filtros de Bloom possuem probabilidade controlada de falsos positivos (dizer que um texto já existia quando ele era inédito), exigindo dimensionamento correto da matriz de bits.
- **Ignorar a inspeção manual:** Confiar cegamente em scripts automatizados de limpeza e nunca olhar para 10 exemplos brutos no terminal.

## 🔍 Comparações

| Método de Deduplicação | Complexidade Temporal | O que detecta? | Custo Computacional |
|---|---|---|---|
| **Comparação Par a Par Bruta**| $\mathcal{O}(N^2)$ (Inviável na escala) | Qualquer similaridade exata | Proibitivo para bases grandes |
| **Hash Exato (SHA-256/MD5)** | $\mathcal{O}(N)$ | Apenas duplicatas $100\%$ idênticas | **Quase zero (CPU)** |
| **MinHash + LSH** | $\mathcal{O}(N)$ amortizado | **Quase-duplicatas (paráfrases, cópias parciais)** | Baixo a Moderado |
| **Filtro de Bloom** | $\mathcal{O}(N)$ constante | Redundâncias em fluxos de tokens | **Mínimo em memória RAM** |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Uma loja virtual quer treinar um modelo para categorizar produtos a partir do título. Na base coletada, constam as seguintes entradas:

- Linha 1: `{item: lápis, cor: vermelho} -> Preço: R$ 20,00`
- Linha 2: `{item: compasso, cor: verde} -> Preço: R$ 2,00`
- Linha 3: `{item: lápis, cor: vermelho} -> Preço: R$ 20,00`
- Linha 4: `{item: lápis, cor: vermelho} -> Preço: R$ 20,00`
- Linha 5: `{item: lápis, cor: verde} -> Preço: R$ 1,00`

Se treinado com essas repetições, a atenção do modelo vicia e passa a assumir que "tudo o que for vermelho precisa custar 20 reais", gerando uma correlação espúria grotesca.
Ao rodar o **algoritmo de deduplicação**, as linhas 3 e 4 são ejetadas imediatamente. O modelo passa a aprender a relação equilibrada entre os materiais e as cores sem nenhum viés de frequência induzido por repetição mecânica.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/curadoria-de-dados-e-o-trio-de-ouro.md|Curadoria de Dados e o Trio de Ouro]]
- [[redes/ai-engineering/conceitos/qualidade-e-conformidade-de-dados.md|Qualidade e Conformidade de Dados]]

### Complementos

- [[redes/ai-engineering/conceitos/verificacao-e-filtragem-de-dados.md|Verificação e Filtragem de Dados]]

### Alternativas

- Treinamento em dados com redundâncias brutas naturais.

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/contaminacao-de-dados-em-benchmarks.md|Contaminação de Dados em Benchmarks]]
- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 8 — Dataset Engineering
- **Localização:** Páginas 396–403
- **Evidência:** Chip Huyen destaca a citação célebre de Greg Brockman (OpenAI) sobre o valor da inspeção manual, analisa os gráficos de distribuição verbo-objeto de Peng et al. (2023), documenta as três formas de duplicatas e o experimento da Anthropic (Hernandez et al., 2022) comprovando a queda de escala por repetições, e detalha métodos probabilísticos como MinHash e filtros de Bloom.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. Por que a inspeção manual direta de dados é considerada por líderes de engenharia como a atividade de maior relação valor-prestígio em IA?
2. Quais são os três níveis estruturais nos quais a duplicação de dados pode se manifestar em um corpus textual?
3. Como a repetição desbalanceada de exemplos induz o modelo a aprender correlações espúrias e vieses de frequência?
4. Qual foi o impacto métrico demonstrado pelo estudo da Anthropic (Hernandez et al., 2022) ao repetir apenas 0,1% dos dados 100 vezes?
5. Como o algoritmo MinHash utiliza funções de espalhamento e o coeficiente de Jaccard para detectar quase-duplicatas em tempo linear?
6. De que forma a presença de duplicatas entre o conjunto de treinamento e o conjunto de teste causa contaminação de avaliação?
7. Qual é a função dos Filtros de Bloom no pré-processamento de fluxos contínuos de tokens para desduplicação?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.

*Nota gerada a partir do capítulo Capítulo 8 — Dataset Engineering. A interpretação final deve ser revisada pelo estudante.*
