# Resumo de Produção Própria: Souza & Orsi (2024) — SIMPROFI (Origem do Projeto)

## Referência Completa
**Autores:** Souza, M. S.; Orsi, R. N.
**Título:** Sustentabilidade na mesa: redução do desperdício alimentar em uma Instituição de Ensino com previsão de demanda por aprendizado de máquina.
**Ano:** 2024
**Evento:** XIX Simpósio dos Programas de Mestrado Profissional (SIMPROFI) – São Paulo/SP – 05 a 07 de novembro de 2024.
**Publicação:** Revista H-Tec Humanidades e Tecnologia, v. 11, Ed. Especial XIX SIMPROFI.
**Caminho Local:** `d:\PROJETOS\PRODUTO_MESTRADO\docs\artigos\Meus Artigos\relato_tecnico_simprof24.pdf`

## Resumo
Este é o **artigo inaugural do projeto de Dissertação** — o primeiro relato técnico publicado. Apresenta a versão inicial (v0) do produto: um sistema de previsão de demanda simples baseado em **Regressão Linear**, alimentado pelos dados de reservas online e consumo do IFSP – Campus Itaquaquecetuba. O relato já documenta a gravidade do problema: **30% de desperdício** nas refeições preparadas, equivalendo a **R$ 172.500,00 desperdiçados** de um orçamento de R$ 575.000,00 (37% do orçamento total do campus).

## Principais Tópicos
- **Diagnóstico Financeiro:** Desperdício de 30% = R$172.500/ano só em alimentos jogados fora.
- **Solução Inicial (v0):** Formulário online para reserva antecipada dos alunos + pipeline Python (Pandas, Scikit-learn) + Regressão Linear.
- **Limitação Identificada:** A regressão linear identificou padrões mas revelou a necessidade de variáveis adicionais (clima, histórico de presenças, calendário, períodos de prova) para aumentar a acurácia — motivação direta para os avanços dos artigos seguintes (SIMPROF 2025, SINGEP 2025).

## Pertinência para o Projeto
**Essencial — Produção Própria (Artigo Fundador).** É a publicação de origem que estabelece o contexto do problema, justifica a escolha do IFSP-ITQ como campo de pesquisa e documenta os dados financeiros (30% de desperdício, R$172.500) que fundamentam toda a motivação da Dissertação. **Deve aparecer como referência primária na seção de Contexto/Problema da Dissertação.** É o "ponto zero" da trajetória metodológica que evolui para modelos híbridos de Ensemble no SINGEP 2025.
