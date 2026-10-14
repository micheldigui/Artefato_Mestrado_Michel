# 🧠 Modelo Multimodal

**Rede:** `ai-engineering`   **Área:** `modelagem`

## 📚 Origem do conteúdo

Esta nota foi construída a partir da fonte abaixo. A fonte é metadado de rastreabilidade e não representa um nó conceitual no grafo.

- AI Engineering: Building Applications with Foundation Models — Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- Localização: Páginas 8–10

## 📝 Definição

### Definição formal

Um **Modelo Multimodal** (*Large Multimodal Model* — LMM) é uma arquitetura de inteligência artificial capaz de processar, correlacionar, mapear em um espaço vetorial compartilhado ou gerar dados pertencentes a múltiplas modalidades perceptivas distintas (como texto, imagens estáticas, vídeo, áudio ou estruturas moleculares).

### Em linguagem simples

É um modelo de inteligência artificial que não apenas lê e escreve textos, mas também consegue "enxergar" fotos, "ouvir" sons e cruzar todas essas informações ao mesmo tempo para resolver uma dúvida ou gerar um conteúdo.

### Escopo e distinções

Rompe com a compartimentação histórica da pesquisa em inteligência artificial, que mantinha áreas isoladas para Processamento de Linguagem Natural (NLP), Visão Computacional (CV) e Processamento de Áudio. Um modelo multimodal integra os sinais em uma representação conjunta unificada.

## 🧩 Problema que resolve

O mundo real e as interfaces corporativas não são puramente textuais. Usuários lidam com notas fiscais digitalizadas, gráficos estatísticos, gravações de voz e fotos de produtos. Modelos puramente de texto exigiam múltiplos sistemas intermediários frágeis de conversão (como OCRs externos e softwares isolados de transcrição). O modelo multimodal elimina intermediários e analisa o dado visual ou auditivo em seu formato nativo com compreensão de contexto.

## 💡 Intuição

Imagine um especialista em segurança que analisa uma filmagem de câmera. Se ele apenas pudesse ler uma transcrição textual feita por terceiros dizendo "um homem entrou na sala com um objeto metálico", ele perderia nuances cruciais. Ao enxergar diretamente o vídeo e ouvir os ruídos simultaneamente com seus próprios olhos e ouvidos, ele consegue julgar com precisão superior se o objeto era uma chave de fenda ou uma arma.

## ⚙️ Como funciona

O modelo projeta entradas sensoriais heterogêneas no mesmo espaço representacional:

### Etapas

1. **Codificação sensorial:** Imagens, sons ou textos passam por codificadores dedicados (*encoders* de visão ou áudio) que dividem os dados em blocos ou fragmentos (*patches*).
2. **Projeção dimensional:** Os dados visuais ou auditivos são convertidos em representações vetoriais compatíveis com os tokens de texto.
3. **Fusão contextual:** A camada neural de atenção processa conjuntamente os tokens de imagem e de texto.
4. **Decodificação e geração:** O modelo gera a próxima unidade preditiva (geralmente tokens de texto ou vetores de coordenadas para delimitação de objetos).

### Entradas e saídas

- **Entradas:** Combinações simultâneas de imagens, prompts textuais, áudio ou documentos diagramados.
- **Saídas:** Respostas em texto descritivo, extrações estruturadas, respostas a perguntas sobre imagens ou imagens sintetizadas.

## 📐 Formulação matemática

O modelo autoregressivo multimodal estende a probabilidade condicional para incorporar uma sequência de entrada composta por tokens de texto $X_{\text{texto}}$ e representações projetadas de imagens $X_{\text{imagem}}$:

$$P(Y \mid X_{\text{texto}}, X_{\text{imagem}}) = \prod_{t=1}^T P\Big(y_t \mid y_{<t}, X_{\text{texto}}, X_{\text{imagem}}; \theta\Big)$$

Em modelos de alinhamento contrastivo como o CLIP (Radford et al., 2021), maximiza-se a similaridade de cosseno entre o vetor da imagem $I_k$ e o vetor do texto correspondente $T_k$ no espaço compartilhado de dimensão $d$:

$$\text{Sim}(I_k, T_k) = \frac{\langle I_k, T_k \rangle}{\|I_k\| \|T_k\|}$$

## 🧱 Hipóteses e condições de validade

- Existência de dados pareados de alta qualidade (como pares imagem-legenda na internet) para ensinar ao modelo a relação semântica entre modalidades durante o pré-treinamento.
- Recursos de memória gráfica substancialmente superiores para processar sequências extensas de tokens visuais sem estourar o limite de VRAM.

## ✅ Quando usar

- Análise de documentos ricos (PDFs escaneados com tabelas complexas, formulários manuscritos, faturas).
- Aplicações de suporte técnico que exigem que o usuário envie uma foto do equipamento quebrado.
- Sistemas de catalogação automática de comércio eletrônico a partir de fotografias de produtos.

## 🚫 Quando não usar

- Aplicações de processamento exclusivo de texto sem enriquecimento visual ou sonoro, onde o uso de LMMs apenas encarece a inferência e eleva o tempo de resposta (*TTFT*).

## ⚠️ Limitações e armadilhas

- **Alucinação perceptual:** O modelo pode "ver" textos ou objetos que não estão presentes na imagem se for fortemente influenciado pela sugestão contida no prompt de texto.
- **Consumo severo de tokens:** Uma única imagem de média resolução pode ser convertida internamente em centenas ou milhares de tokens, consumindo rapidamente a janela de contexto e o orçamento financeiro.

## 🔍 Comparações

| Dimensão | Modelo Unimodal (Texto) | Modelo Multimodal (LMM) |
|---|---|---|
| **Domínio perceptivo** | Exclusivamente texto | Texto, Visão, Áudio |
| **Arquitetura** | Processador de sequência de tokens | Codificadores cruzados com projeção compartilhada |
| **Custo de inferência** | Menor por requisição | Mais elevado devido aos tokens visuais |
| **Flexibilidade documental** | Exige OCR prévio para ler PDFs | Lê o documento visualmente de forma nativa |

## 🧪 Exemplo mental

**Exemplo didático construído a partir do conceito.**

Um auditor de seguros recebe uma foto de um para-choque amassado acompanhada da mensagem: `"O dano afeta a integridade do radiador?"`. 
Um modelo unimodal de texto precisaria de uma descrição textual subjetiva do usuário. O **modelo multimodal** recebe a fotografia e a pergunta juntas, analisa a profundidade visual do amassado na lataria, identifica que o impacto não atingiu a grade interna frontal e responde: `"Não, o impacto concentrou-se na camada plástica superior externa do para-choque"`.

## 🔗 Relações no grafo

### Pré-requisitos

- [[redes/ai-engineering/conceitos/modelo-de-fundacao.md|Modelo de Fundação]]
- [[redes/ai-engineering/conceitos/tokenizacao.md|Tokenização e Vocabulário]]

### Complementos

- [[redes/ai-engineering/conceitos/auto-supervisao.md|Auto-supervisão]]

### Alternativas

- Pipelines encadeados clássicos (OCR óptico separado enviando texto para um LLM simples).

### Conceitos relacionados

- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]]
- [[redes/ai-engineering/conceitos/rag.md|Geração Aumentada de Recuperação (RAG)]]

- [[redes/ai-engineering/conceitos/adaptacao-de-modelos.md|Adaptação de Modelos]]
- [[redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md|Geração Aumentada de Recuperação (RAG)]]

## 📚 Evidência nas fontes consultadas

- **Fonte:** AI Engineering: Building Applications with Foundation Models
- **Capítulo:** Capítulo 1 — Introduction to Building AI Applications with Foundation Models
- **Localização:** Páginas 8–10
- **Evidência:** O texto define os modelos multimodais de fundação, citando sistemas como GPT-4V, Claude 3 e Gemini, e destaca o papel pioneiro do modelo de embedding conjunto CLIP treinado por supervisão de linguagem natural em 400 milhões de pares texto-imagem.
- **Confiança:** Alta

## ❓ Perguntas de revisão

1. O que é um Large Multimodal Model (LMM) e como ele supera a compartimentação histórica da pesquisa de IA?
2. Como funciona o treinamento contrastivo do CLIP para criar um espaço vetorial compartilhado entre texto e imagem?
3. Quais vantagens operacionais decorrem de processar um documento PDF diretamente como imagem em vez de aplicar um OCR tradicional?
4. Qual é o impacto do processamento de imagens no consumo de tokens e na janela de contexto de um modelo multimodal?
5. O que caracteriza a alucinação perceptual em sistemas multimodais?
6. Quais modalidades sensoriais além de texto e visão vêm sendo progressivamente incorporadas a modelos de fundação?
7. Em quais circunstâncias de negócio o uso de um modelo multimodal é um desperdício de recursos financeiros em comparação a um modelo de texto puro?

## 📌 Notas pessoais

- [ ] Reescrever o conceito com minhas próprias palavras.
- [ ] Criar ou resolver um exemplo.
- [ ] Relacionar este conceito a outro assunto.
- [ ] Registrar uma dúvida.
- [ ] Revisar após alguns dias.
