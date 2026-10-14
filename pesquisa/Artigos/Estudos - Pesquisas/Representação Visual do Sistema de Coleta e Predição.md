---
source_file: "Representação Visual do Sistema de Coleta e Predição.pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Representação Visual do Sistema de Coleta e Predição.pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "53ad623ae794ee2d254e5b2b331600048184948a2f971235a6f5578c8dbf44a1"
extracted_at: "2026-09-20T00:53:20.146980"
---

## Representação Visual do Sistema de Coleta e Predição

Este documento compila as representações visuais do sistema de coleta de dados e predição de demanda de refeições, incluindo diagramas de arquitetura, fluxo de dados e mockups das interfaces de usuário.

## 1. Diagrama de Arquitetura

O diagrama abaixo ilustra os principais componentes do sistema e como eles se conectam:

- Usuários: Aluno e Administrador. ·
- Frontend: Interfaces web acessadas via navegador. ·
- Backend: Aplicação Flask que processa requisições e interage com o banco. ·
- Banco de Dados: SQLite armazenando todos os dados. ·
- Processamento Offline (ML): Scripts Python para treinamento e predição. ·

(O diagrama arquitetura\_sistema.png será anexado separadamente)

## 2. Diagrama de Fluxo de Dados

Este diagrama mostra como os dados se movem através do sistema:

- Entrada de dados pelos usuários (formulários, CSV). ·
- Armazenamento no banco de dados pela aplicação Flask. ·
- Leitura de dados históricos e futuros pelos scripts de ML. ·
- Geração e salvamento do modelo treinado. ·
- Geração e salvamento das predições no banco de dados. ·
- Leitura e exibição das predições pela interface administrativa. ·

(O diagrama  fl uxo\_dados.png será anexado separadamente)

## 3. Mockups das Interfaces de Usuário

A seguir, descrições textuais (mockups) das principais interfaces do sistema.

## 3.1. Interface de Reserva do Aluno ( /aluno/reservar )

Título da Página:

## Reservar Refeição

## Layout:

- Navegação Superior: Links para "Reservar Refeição" e "Painel Admin". ·
- Conteúdo Principal (Container Branco): ·
- Título: &lt;h2&gt;Reservar Refeição&lt;/h2&gt; ◦
- Mensagens Flash: Área para exibir mensagens de sucesso, erro ou aviso (ex: "Reserva realizada com sucesso!"). ◦
- Formulário de Reserva: ◦
- Campo "Seu Código de Aluno": ▪
- Rótulo: Seu Código de Aluno: ▪
- Input de Texto ( &lt;input type="text" name="student\_code"&gt; ), obrigatório. ▪
- Campo "Selecione o Cardápio": ▪
- Rótulo: Selecione o Cardápio: ▪
- Dropdown ( &lt;select name="menu\_id"&gt; ), obrigatório. ▪
- Opção Padrão: -- Escolha uma data/cardápio -- (desabilitada). ▪
- Opções Dinâmicas: Lista de cardápios disponíveis (Data - Prato Principal (Descrição)), obtidos do backend. ▪
- Observação: Se não houver cardápios, exibir a mensagem "Nenhum cardápio disponível para reserva no momento." e desabilitar o botão. ▪
- Botão "Confirmar Reserva": ▪
- Botão de Submit ( &lt;button type="submit"&gt; ). ▪
- Desabilitado se não houver cardápios disponíveis. ▪

## Estilo Visual (Baseado no base.html ):

- Fundo cinza claro, container principal branco com sombra. ·
- Navegação com fundo escuro e links brancos. ·
- Formulário com rótulos acima dos campos. ·
- Campos de input e select com largura total e bordas arredondadas. ·
- Botão verde com texto branco. ·
- Mensagens flash coloridas (verde para sucesso, vermelho para erro, amarelo para aviso). ·

## 3.2. Painel Administrativo ( /admin/ )

Título da Página:

Painel Admin

## Layout:

- Navegação Superior: Links para "Reservar Refeição" e "Painel Admin". ·
- Conteúdo Principal (Container Branco): ·
- Título: &lt;h2&gt;Painel de Controle Administrativo&lt;/h2&gt; ◦
- Mensagens Flash: Área para exibir mensagens. ◦
- Mensagem de Boas-vindas: Bem-vindo(a) à área administrativa. ◦
- Estatística Rápida: ◦
- Texto: Total de reservas para hoje (DD/MM/YYYY): [Número] (Número obtido do backend). ▪
- Seção "Ações Rápidas": ◦
- Título: &lt;h3&gt;Ações Rápidas:&lt;/h3&gt; ▪
- Lista de Links ( &lt;ul&gt; ): ▪
- &lt;li&gt;&lt;a href="/admin/cardapios"&gt;Gerenciar Cardápios&lt;/a&gt;&lt;/li&gt; ▪
- &lt;li&gt;&lt;a href="/admin/calendario/importar"&gt;Importar Calendário/ Eventos&lt;/a&gt;&lt;/li&gt; ▪
- &lt;li&gt;&lt;a href="/admin/clima"&gt;Registrar Previsão do Tempo&lt;/a&gt;&lt;/li&gt; ▪
- &lt;li&gt;&lt;a href="/admin/previsoes"&gt;Visualizar Previsões de Demanda&lt;/a&gt;&lt;/li&gt; ▪
- &lt;li&gt;&lt;a href="/admin/reservas"&gt;Visualizar Todas as Reservas&lt;/a&gt;&lt;/ li&gt; (Link para funcionalidade futura/opcional) ▪

## Estilo Visual (Baseado no base.html ):

- Consistente com a interface do aluno (fundo cinza, container branco, navegação escura). ·
- Links de ação rápida apresentados como uma lista clara. ·

## 3.3. Visualizar Previsões de Demanda ( /admin/previsoes )

Título da Página:

## Visualizar Previsões de Demanda

## Layout:

- Navegação Superior: Links para "Reservar Refeição" e "Painel Admin". ·
- Conteúdo Principal (Container Branco): ·
- Título: &lt;h2&gt;Previsões de Demanda de Refeições&lt;/h2&gt; ◦
- Mensagens Flash: Área para exibir mensagens (ex: "Erro ao buscar previsões..."). ◦
- Descrição: A tabela abaixo mostra as previsões de demanda geradas pelo modelo para os próximos dias. ◦

## Tabela de Previsões: ◦

- Renderizada se houver previsões ( {% if predictions %} ). ▪
- Cabeçalho: ▪
- &lt;th&gt;Data da Previsão&lt;/th&gt; ▪
- &lt;th&gt;Demanda Prevista&lt;/th&gt; ▪
- &lt;th&gt;Demanda Real (se disponível)&lt;/th&gt; ▪
- &lt;th&gt;Versão do Modelo&lt;/th&gt; ▪
- &lt;th&gt;Gerado em (UTC)&lt;/th&gt; ▪

## Corpo da Tabela ( &lt;tbody&gt; ): ▪

- Loop através das previsões ( {% for prediction in predictions %} ). ▪
- Cada linha ( &lt;tr&gt; ) contém: ▪
- Data da Previsão (formatada DD/MM/YYYY). ▪
- Demanda Prevista (número inteiro). ▪
- Demanda Real (número inteiro, ou "-" se não disponível - busca no actual\_demand\_data ). ▪
- Versão do Modelo (string, ou "N/A"). ▪
- Timestamp de Geração (formatado DD/MM/YYYY HH:MM:SS). ▪

## Mensagem Alternativa: ◦

- Exibida se não houver previsões ( {% else %} ). ▪
- Texto: Nenhuma previsão encontrada para o período selecionado. ▪
- Texto: Certifique-se de que o script de predição ( predict\_demand.py ) foi executado recentemente. ▪

## Estilo Visual (Baseado no base.html ):

- Consistente com as outras páginas (fundo cinza, container branco, navegação escura). ·
- Tabela com bordas, cabeçalho destacado e linhas alternadas (se definido no CSS base). ·