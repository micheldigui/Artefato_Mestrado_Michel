---
source_file: "Análise de Relevância de Variáveis e Coluna Alvo.pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Análise de Relevância de Variáveis e Coluna Alvo.pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "ef6c90dda9b44d4f12c920333a710fe76c2a33eeaf7de1a6c7caf918d8a32634"
extracted_at: "2026-09-20T00:50:40.178416"
---

## Análise de Relevância de Variáveis e Coluna Alvo

Este documento analisa a relevância das variáveis mencionadas pelo usuário (identificador do aluno, curso, semestre) e revisita a definição da coluna alvo para a predição de demanda de refeições.

## 1. Variáveis Descartadas na Agregação Diária

O dataset dref\_adaptado.csv foi construído para prever a demanda agregada diária de refeições. As variáveis individuais como MATRÍCULA IQ (identificador do aluno) e TURMA (que implica curso e semestre) do dataset original dref.xlsx não foram incluídas diretamente como colunas no dref\_adaptado.csv pelas seguintes razões no contexto do objetivo atual:

## 1.1. Identificador do Aluno ( MATRÍCULA IQ )

## Relevância para Demanda Agregada Diária: ·

- O identificador único de cada aluno não é, por si só, uma feature preditiva para o número total de refeições em um dia. Ele foi fundamental no dataset original para registrar reservas e consumos individuais, permitindo assim o cálculo da coluna actual\_demand (total de refeições servidas por dia) no dref\_adaptado.csv . ◦
- Relevância para Outros Tipos de Predição: ·
- Seria essencial se o objetivo fosse prever o comportamento individual de um aluno (ex: probabilidade de um aluno específico reservar uma refeição) ou para personalizar recomendações. ◦

## 1.2. Curso e Semestre (implícito na TURMA )

## Relevância para Demanda Agregada Diária: ·

- Potencial: Você está correto ao observar que diferentes cursos e semestres podem ter hábitos distintos (horários de pico, frequência no campus, adesão ao refeitório). Mudanças de hábitos ao longo do tempo também podem variar entre esses grupos. ◦
- **Desafios para Inclusão no Modelo Agregado Atual ( dref\_adaptado.csv ): ◦
- Nível de Agregação: A TURMA está no nível de cada registro de refeição no dref.xlsx . Para usar no dref\_adaptado.csv (que é diário), precisaríamos agregar essa informação. Como? Poderíamos tentar features como "curso predominante do dia" ou "percentual de alunos do 1º ano presentes", mas isso exigiria dados adicionais de matrícula e horários por turma para ser significativo. ▪
- Dimensionalidade vs. Tamanho do Dataset: O dref\_adaptado.csv possui um histórico diário relativamente curto (23 dias no exemplo). Adicionar muitas features derivadas de TURMA (ex: uma feature para cada curso/semestre) poderia levar a um overfitting do modelo, onde ele aprende o ruído dos dados de treinamento mas não generaliza bem para novos dias. ▪
- Complexidade: A interpretação e o impacto dessas features agregadas por turma na demanda total diária poderiam ser complexos de isolar sem um volume de dados maior. ▪
- Alternativas Implementadas: As features day\_of\_week e event\_type (NORMAL, FERIADO, EVENTO\_ESCOLAR, PERIODO\_PROVAS, FIM\_DE\_SEMANA) no dref\_adaptado.csv já tentam capturar parte da variação da atividade geral no campus que poderia ser influenciada pela composição das turmas presentes. ◦
- Relevância para Outros Tipos de Predição: ·
- Seria muito relevante para análises de segmentação da demanda (ex: qual curso consome mais?) ou para modelos que tentam prever a demanda de forma mais granular (ex: demanda por tipo de curso). ◦

Conclusão sobre Variáveis Descartadas (para o modelo agregado atual): Para um modelo inicial focado na predição da demanda total diária e com um histórico de dados limitado, a abordagem de focar em features diárias mais gerais (data, cardápio, clima, eventos, lags de demanda) é uma simplificação razoável e um bom ponto de partida. As informações de MATRÍCULA IQ e TURMA foram cruciais para construir a variável alvo actual\_demand no nível diário. A não inclusão direta delas como features preditoras no modelo agregado diário visa evitar complexidade excessiva e overfitting com dados limitados. No entanto, elas guardam um potencial analítico e preditivo grande para modelos mais detalhados ou com outros objetivos.

## 2. Coluna Alvo ( actual\_demand ) e Predição para o Dia Seguinte

## Definição da Coluna Alvo ( actual\_demand ): ·

- No dataset dref\_adaptado.csv , a coluna actual\_demand representa o número histórico real de refeições que foram efetivamente servidas em cada dia passado. Este é o valor que queremos que nossos modelos aprendam a prever. ◦
- Ela é derivada da contagem de refeições marcadas como "SERVIDA" no dataset original dref.xlsx para cada data. ◦

## O que o Modelo Prevê (para o "dia seguinte") : ·

- Quando treinamos um modelo de machine learning (como XGBoost, LightGBM, etc.) usando actual\_demand como alvo (y) e as outras colunas como features (X), o modelo aprende a relação entre essas features e a demanda histórica. ◦
- Para prever a demanda para o "dia seguinte" (ou qualquer dia futuro), nós alimentamos o modelo treinado com as features conhecidas ou estimadas para esse dia futuro . Por exemplo: ◦
- day\_of\_week do dia seguinte (conhecido). ▪
- month do dia seguinte (conhecido). ▪
- main\_dish planejado para o dia seguinte (conhecido). ▪
- max\_temp\_forecast e rain\_forecast (previsão do tempo para o dia seguinte). ▪
- event\_type para o dia seguinte (conhecido, ex: NORMAL, FERIADO). ▪
- Valores de lag\_1d , lag\_2d , etc., que seriam as demandas reais dos dias imediatamente anteriores ao "dia seguinte" (conhecidas no momento da predição). ▪
- O output do modelo para essas features futuras é a predição da demanda para o "dia seguinte". ◦

## Relação com o "Quantitativo de Refeições a Serem Preparadas": ·

- A predição de demanda gerada pelo modelo é a estimativa mais provável do número de refeições que serão consumidas. ◦
- Para decidir o quantitativo a ser preparado, a gestão do refeitório normalmente usaria essa predição como base e poderia adicionar uma margem de segurança (para evitar falta de comida) ou fazer ajustes com base em fatores não capturados pelo modelo. ◦

Conclusão sobre a Coluna Alvo: A coluna actual\_demand está corretamente definida como a variável alvo para o treinamento dos modelos de predição. O objetivo é que os modelos aprendam a partir dos dados históricos para, então, serem capazes de estimar essa mesma actual\_demand para datas futuras, fornecendo assim a base para o planejamento do quantitativo de refeições.