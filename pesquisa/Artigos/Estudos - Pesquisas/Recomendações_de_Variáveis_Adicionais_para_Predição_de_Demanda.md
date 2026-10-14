---
source_file: "Recomendações_de_Variáveis_Adicionais_para_Predição_de_Demanda.pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Recomendações_de_Variáveis_Adicionais_para_Predição_de_Demanda.pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "e7cfe2f17da7816c2f947dad8e5a7bce519448f2b10d1b079b3cea9ed250b62e"
extracted_at: "2026-09-20T00:52:20.979578"
---

## Recomendações de Variáveis Adicionais para Predição de Demanda no IFSP

Com base na análise da literatura (sintetizada em sintese\_variaveis\_algoritmos.md ) e considerando as variáveis que você já coleta ( Data da refeição , Código do aluno , Série , Curso ), recomendo fortemente a coleta e utilização das seguintes variáveis adicionais para melhorar a acurácia da predição de demanda de refeições com duas semanas de antecedência:

## Variáveis Altamente Recomendadas

Estas variáveis tendem a ter um impacto significativo nos modelos preditivos e são frequentemente citadas na literatura:

## Histórico de Demanda Agregada: 1.

- Descrição: Quantidade total de refeições efetivamente reservadas ou servidas em cada dia passado. ◦
- Justificativa: É um dos preditores mais fortes. Padrões passados de consumo são essenciais para prever o futuro. É crucial ter o histórico diário agregado. ◦
- Coleta: Manter um registro diário do número total de reservas confirmadas ou refeições servidas. ◦

## Dia da Semana: 2.

- Descrição: Identificar o dia da semana (segunda, terça, ..., sexta). ◦
- Justificativa: O consumo pode variar significativamente dependendo do dia da semana devido a horários de aulas ou outras rotinas. ◦
- Coleta: Facilmente derivado da Data da refeição . ◦

## Calendário Acadêmico e Eventos: 3.

- Descrição: Marcar dias que são feriados (nacionais, locais, pontos facultativos), início e fim de semestre, períodos de férias, semanas de provas, eventos especiais no campus (palestras, feiras, competições) que possam alterar a presença normal dos alunos. ◦
- Justificativa: Eventos e feriados causam grandes desvios na demanda normal e precisam ser explicitamente informados ao modelo. ◦
- Coleta: Obter o calendário acadêmico oficial e registrar eventos relevantes com antecedência. ◦
- Cardápio Específico (Características Principais): 4.
- Descrição: Registrar informações sobre o prato principal ou características marcantes do cardápio do dia (ex: "Frango Assado", "Feijoada", "Opção Vegetariana Principal", etc.). ◦
- Justificativa: A popularidade de certos pratos influencia diretamente a adesão dos alunos. O modelo pode aprender quais cardápios geram mais ou menos demanda. ◦
- Coleta: Obter o planejamento de cardápios com a mesma antecedência da necessidade de predição (2 semanas). ◦

## Variáveis Recomendadas (Potencialmente Úteis)

Estas variáveis podem agregar valor dependendo da disponibilidade e facilidade de coleta:

- Condições Climáticas (Previstas): 1.
- Descrição: Temperatura máxima prevista, previsão de chuva (sim/não ou intensidade) para o dia da refeição. ◦
- Justificativa: Condições climáticas extremas (muito calor, chuva forte) podem influenciar a decisão dos alunos de permanecer no campus para a refeição. ◦
- Coleta: Utilizar serviços de previsão do tempo que ofereçam dados com 2 semanas de antecedência para Itaquaquecetuba. ◦
- Número de Alunos Esperados no Campus (se disponível): 2.
- Descrição: Alguma estimativa do número total de alunos esperados no campus naquele dia (talvez baseado no total de matriculados por curso/série com aulas naquele dia). ◦
- Justificativa: Modela a população potencial que pode reservar a refeição. ◦
- Coleta: Pode ser derivado dos dados de matrícula e horários, mas pode ser complexo de estimar com precisão. ◦

## Variáveis a Considerar (Menor Prioridade Inicial)

- Turno do Aluno: 1.
- Descrição: Manhã, Tarde, Noite. ◦
- Justificativa: Alunos de diferentes turnos podem ter padrões de consumo distintos. ◦
- Coleta: Provavelmente associado ao Curso ou Série . ◦

## Comparação com Variáveis Atuais

- Data da refeição : Essencial, já coletada. Permite derivar Dia da Semana, Mês, etc. ·
- Código do aluno : Útil para análises individuais, mas para a predição agregada (quantitativo total), o histórico agregado (item 1) é mais direto. Pode ser usado para criar features agregadas por Série ou Curso . ·
- Série e Curso : Já coletadas. Podem ser usadas para identificar padrões de grupos específicos, embora o impacto na predição agregada precise ser avaliado. ·

Próximos Passos: Sugiro focar na coleta e estruturação das variáveis Altamente Recomendadas , especialmente o Histórico de Demanda Agregada e informações do Calendário/Eventos e Cardápio . Estas, combinadas com a data, já formam uma base sólida para iniciar a modelagem preditiva.