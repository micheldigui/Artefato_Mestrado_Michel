---
source_file: "Documentação__Integração_dos_Algoritmos_de_Predição.pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Documentação__Integração_dos_Algoritmos_de_Predição.pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "1915346dc33183638d6d228d491a4a6d5e4c8dc18126e584d726ca57c1020a4c"
extracted_at: "2026-09-20T00:52:05.350419"
---

## Documentação: Integração dos Algoritmos de Predição

Este documento descreve como integrar os scripts de treinamento e predição de demanda com o sistema Flask de coleta de dados, utilizando a abordagem híbrida recomendada.

## 1. Visão Geral da Abordagem Híbrida

A integração segue um fluxo desacoplado:

- Sistema Flask: Continua coletando dados (reservas, cardápios, eventos, clima) e armazenando no banco de dados SQLite ( instance/database.db ). 1.
- Script de Treinamento ( train\_model.py ): Executado offline (manualmente ou agendado), lê dados históricos do banco, treina um modelo de Machine Learning (XGBoost neste exemplo) e salva o modelo treinado em um arquivo. 2.
- Script de Predição ( predict\_demand.py ): Executado offline (manualmente ou agendado), carrega o modelo treinado, busca dados futuros necessários (cardápio, clima, eventos) e dados históricos recentes (para lags) do banco, gera as previsões de demanda e salva essas previsões em uma nova tabela predictions no banco de dados. 3.
- Sistema Flask (Visualização): Uma nova página no painel administrativo ( /admin/ previsoes ) lê a tabela predictions e exibe as previsões mais recentes para o administrador. 4.

## 2. Configuração e Instalação

Siga estes passos para adicionar os componentes de predição ao seu projeto Flask existente ( coleta\_dados\_ifsp/ ).

## 2.1. Estrutura de Arquivos Adicional

Certifique-se de que sua estrutura de projeto inclua os novos diretórios e arquivos:

```
coleta_dados_ifsp/ ├── venv/ ├── src/ │ ├── models/
```

<!-- image -->

- Substitua o arquivo src/models/models.py pelo conteúdo de 18\_backend\_models\_updated.py . ·
- Substitua o arquivo src/routes/admin.py pelo conteúdo de 21\_backend\_admin\_routes\_updated.py . ·
- Crie o diretório scripts/ na raiz do projeto. ·
- Coloque o conteúdo de 19\_script\_train\_model.py no arquivo scripts/ train\_model.py . ·
- Coloque o conteúdo de 20\_script\_predict\_demand.py no arquivo scripts/ predict\_demand.py . ·
- Crie o diretório models/ na raiz do projeto (ele será usado para salvar os modelos treinados). ·
- Crie o arquivo src/templates/admin/view\_predictions.html com o conteúdo de 22\_frontend\_admin\_view\_predictions.html . ·

## 2.2. Novas Dependências

Adicione as seguintes bibliotecas ao seu arquivo requirements.txt :

```
Flask Flask-SQLAlchemy SQLAlchemy # Adicionado explicitamente para os scripts pandas scikit-learn xgboost joblib
```

Instale/Atualize as dependências (com o ambiente virtual ativado):

```
pip install -r requirements.txt
```

## 3. Atualização do Banco de Dados

A modificação no arquivo src/models/models.py (adição da classe Prediction ) requer que a nova tabela predictions seja criada no banco de dados.

O script src/main.py já contém a linha db.create\_all() dentro do contexto da aplicação. Portanto, ao executar a aplicação Flask pela primeira vez após atualizar models.py , a tabela predictions deve ser criada automaticamente no arquivo instance/database.db .

# Na pasta raiz coleta\_dados\_ifsp/, com venv ativo: python src/main.py

Verifique os logs no terminal. Você deve ver as mensagens sobre a criação das tabelas. Se a tabela não for criada, pode ser necessário usar migrações de banco de dados (como Flask-Migrate) para gerenciar alterações no esquema, especialmente em bancos de dados mais complexos ou em produção.

## 4. Executando os Scripts de Treinamento e Predição

Esses scripts devem ser executados a partir da pasta raiz do projeto ( coleta\_dados\_ifsp/ ) ou diretamente da pasta scripts/ , garantindo que o ambiente virtual esteja ativo.

## 4.1. Treinamento ( train\_model.py )

Este script treina o modelo com base nos dados históricos presentes no banco.

- Pré-requisito: Ter dados históricos suficientes nas tabelas menus , reservations , calendar\_events , weather\_data . ·
- Execução (a partir da pasta scripts/ ): bash cd scripts python train\_model.py ·
- Resultado: O script salvará o modelo treinado (e o pré-processador) na pasta models/ (ex: ../models/demand\_predictor.joblib ). ·
- Frequência: Execute este script periodicamente (ex: semanalmente, mensalmente) ou sempre que houver uma quantidade significativa de novos dados históricos para re-treinar o modelo. ·

## 4.2. Predição ( predict\_demand.py )

Este script carrega o modelo treinado e gera previsões para os próximos dias, salvandoas na tabela predictions .

## Pré-requisitos: ·

- O modelo treinado ( demand\_predictor.joblib ) deve existir na pasta models/ . ◦
- Dados futuros relevantes (cardápios, eventos, clima para o período de predição) devem ter sido inseridos no sistema Flask e estarem presentes no banco de dados. ◦
- Execução (a partir da pasta scripts/ ): bash cd scripts python predict\_demand.py ·
- Resultado: A tabela predictions no banco de dados será populada (ou atualizada) com as previsões de demanda para o horizonte definido (padrão: 14 dias). ·
- Frequência: Execute este script regularmente (ex: diariamente) para manter as previsões atualizadas. Idealmente, agende sua execução. ·

## 4.3. Agendamento (Exemplo com cron no Linux)

Para automatizar a execução dos scripts, você pode usar o cron .

- Abra o editor do crontab: crontab -e 1.
- Adicione linhas como estas (ajuste os caminhos e horários): 2.

```
```crontab
```

## Exemplo: Treinar todo domingo às 02:00

0 2 * * 0 /path/to/coleta\_dados\_ifsp/venv/bin/python /path/to/coleta\_dados\_ifsp/ scripts/train\_model.py &gt;&gt; /path/to/logs/train\_model.log 2&gt;&amp;1

## Exemplo: Gerar predições todo dia às 03:00

0 3 * * * /path/to/coleta\_dados\_ifsp/venv/bin/python /path/to/coleta\_dados\_ifsp/ scripts/predict\_demand.py &gt;&gt; /path/to/logs/predict\_demand.log 2&gt;&amp;1 `` * Substitua /path/to/coleta\_dados\_ifsp/ pelo caminho absoluto do seu projeto. * Certifique-se de usar o interpretador Python do seu ambiente virtual ( venv/bin/ python ). * Redirecionar a saída ( &gt;&gt; ... 2&gt;&amp;1`) para arquivos de log é recomendado para monitorar a execução.

## 5. Visualizando as Predições no Sistema

- Execute a aplicação Flask: bash # Na pasta raiz coleta\_dados\_ifsp/, com venv ativo: python src/main.py 1.
- Acesse o painel administrativo no navegador (normalmente http://localhost:5000/ admin ). 2.
- No dashboard ou na navegação, procure por um link para "Visualizar Previsões" (ou acesse diretamente http://localhost:5000/admin/previsoes ). 3.
- A página exibirá uma tabela com as previsões de demanda para os próximos dias, lidas da tabela predictions . 4.

## 6. Explicação dos Arquivos Modificados/Novos

- src/models/models.py : Adicionada a classe Prediction que mapeia a nova tabela predictions no banco de dados. ·
- src/routes/admin.py : ·
- Importado o modelo Prediction . ◦
- Adicionada a nova rota @admin\_bp.route("/previsoes") (função view\_predictions ). ◦
- Essa função consulta a tabela predictions para buscar previsões futuras e, opcionalmente, a demanda real para comparação. ◦
- Renderiza o novo template view\_predictions.html , passando os dados das previsões. ◦
- src/templates/admin/view\_predictions.html : Novo template HTML que recebe a lista de objetos Prediction e os exibe em uma tabela formatada. ·
- scripts/train\_model.py : Script Python independente que: ·
- Conecta ao banco de dados. ◦
- Carrega dados históricos. ◦
- Realiza engenharia de features (lags, data, etc.). ◦
- Pré-processa os dados (OneHotEncoding para categóricas). ◦
- Treina um modelo XGBoost usando um Pipeline do Scikit-learn. ◦
- Salva o pipeline treinado (modelo + pré-processador) usando joblib . ◦
- scripts/predict\_demand.py : Script Python independente que: ·
- Carrega o pipeline treinado ( .joblib ). ◦
- Busca dados futuros (cardápio, clima, eventos) e históricos recentes (para lags) do banco. ◦
- Realiza a mesma engenharia de features dos dados futuros. ◦
- Usa o pipeline carregado para gerar as previsões. ◦
- Conecta ao banco de dados e insere/atualiza as previsões na tabela predictions . ◦

Esta documentação fornece os passos essenciais para a integração. Pode ser necessário ajustar caminhos, queries SQL, features e hiperparâmetros do modelo conforme a evolução dos seus dados e requisitos.