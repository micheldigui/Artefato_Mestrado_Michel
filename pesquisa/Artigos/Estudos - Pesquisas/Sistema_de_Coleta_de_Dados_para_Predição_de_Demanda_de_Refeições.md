---
source_file: "Sistema_de_Coleta_de_Dados_para_Predição_de_Demanda_de_Refeições.pdf"
original_rel_path: "Trabalhos\Artigos\Estudos - Pesquisas\Sistema_de_Coleta_de_Dados_para_Predição_de_Demanda_de_Refeições.pdf"
category: "Artigos_Estudos"
extension: ".pdf"
sha256: "3a4302e80a199c249b9d0a1756b4aeb984cdd1aa57900d2afa1756183080057b"
extracted_at: "2026-09-20T00:55:12.534589"
---

## Sistema de Coleta de Dados para Predição de Demanda de Refeições

Este documento descreve o passo a passo para configurar e utilizar o sistema desenvolvido em Python (Flask) para coletar as variáveis necessárias à predição da demanda de refeições no IFSP Itaquaquecetuba.

Objetivo: Coletar e armazenar dados sobre reservas de refeições, cardápios, eventos do calendário acadêmico e previsões climáticas para posterior uso em modelos de Machine Learning.

## 1. Pré-requisitos

- Python 3.8+: Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em python.org. ·
- pip: O gerenciador de pacotes do Python, geralmente instalado junto com o Python. ·
- Ambiente Virtual (Recomendado): É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto. ·

## 2. Configuração do Ambiente

Abra um terminal ou prompt de comando na pasta onde você deseja criar o projeto.

- Criar Pasta do Projeto: bash mkdir coleta\_dados\_ifsp cd coleta\_dados\_ifsp 1.
- Criar e Ativar Ambiente Virtual: 2.
- No Linux/macOS: bash python3 -m venv venv source venv/bin/activate ◦
- No Windows: bash python -m venv venv .\venv\Scripts\activate (Você verá (venv) no início do prompt indicando que o ambiente está ativo) ◦
- Instalar Dependências: Crie um arquivo chamado requirements.txt na pasta raiz do projeto ( coleta\_dados\_ifsp/ ) com o seguinte conteúdo: txt Flask FlaskSQLAlchemy # Adicione outras dependências se necessário no futuro, como python-dotenv Em seguida, instale as dependências: bash pip install -r requirements.txt 3.

## 3. Estrutura do Projeto

Organize os arquivos do projeto conforme a estrutura abaixo. Os códigos para cada arquivo serão fornecidos nas seções seguintes.

<!-- image -->

Observação: A pasta instance/ e o arquivo database.db serão criados automaticamente quando você executar a aplicação pela primeira vez.

## 4. Código Fonte

A seguir, o conteúdo de cada arquivo Python e HTML necessário para o sistema.

Observação: Crie os diretórios ( src , src/models , src/routes , src/static/css , src/static/ js , src/templates , src/templates/student , src/templates/admin ) conforme a estrutura definida na seção 3 antes de criar os arquivos.

## 4.1. Backend (Python/Flask)

## src/models/database.py

```
# Conteúdo do arquivo 02_backend_database_setup.py from flask_sqlalchemy import SQLAlchemy db = SQLAlchemy()
```

## src/models/models.py

```
# Conteúdo do arquivo 03_backend_models.py from datetime import datetime from .database import db # Importa o objeto db do arquivo database.py no mesmo diretório class Menu (db.Model): __tablename__ = 'menus' id = db.Column(db.Integer, primary_key= True ) date = db.Column(db.Date, unique= True , nullable= False ) main_dish = db.Column(db.String(200), nullable= False ) description = db.Column(db.Text, nullable= True ) is_available = db.Column(db.Boolean, default= True , nullable= False ) reservations = db.relationship('Reservation', backref='menu', lazy= True ) def __repr__(self): return f'<Menu { self.date.strftime("%Y-%m%d ") } - { self.main_dish } >' class Reservation (db.Model): __tablename__ = 'reservations' id = db.Column(db.Integer, primary_key= True ) student_code = db.Column(db.String(100), nullable= False ) menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable= False ) reservation_timestamp = db.Column(db.DateTime, nullable= False , default=datetime.utcnow) attended = db.Column(db.Boolean, nullable= True ) # Pode ser atualizado depois # Garante que um aluno não possa reservar o mesmo menu duas vezes __table_args__ = (db.UniqueConstraint('student_code', 'menu_id', name='_student_menu_uc'),) def __repr__(self): return f'<Reservation { self.student_code } for Menu ID { self.menu_id } >'
```

```
class CalendarEvent (db.Model): __tablename__ = 'calendar_events' id = db.Column(db.Integer, primary_key= True ) date = db.Column(db.Date, nullable= False ) description = db.Column(db.String(255), nullable= False ) type = db.Column(db.String(50), nullable= False ) # Ex: 'FERIADO', 'EVENTO', 'SUSPENSAO_AULA' def __repr__(self): return f'<CalendarEvent { self.date.strftime("%Y-%m%d ") } - { self.description } >' class WeatherData (db.Model): __tablename__ = 'weather_data' id = db.Column(db.Integer, primary_key= True ) date = db.Column(db.Date, unique= True , nullable= False ) max_temp_forecast = db.Column(db.Float, nullable= True ) rain_forecast = db.Column(db.Boolean, nullable= True ) forecast_timestamp = db.Column(db.DateTime, nullable= False , default=datetime.utcnow) def __repr__(self): return f'<WeatherData { self.date.strftime("%Y-%m%d ") } >'
```

## src/routes/student.py

```
# Conteúdo do arquivo 05_backend_student_routes.py from flask import Blueprint, render_template, request, flash, redirect, url_for from src.models.database import db from src.models.models import Menu, Reservation from datetime import date, timedelta student_bp = Blueprint("student", __name__, template_folder="../templates/ student") @student_bp.route("/reservar", methods=["GET", "POST"]) def reserve(): if request.method == "POST": student_code = request.form.get("student_code") menu_id = request.form.get("menu_id") if not student_code or not menu_id: flash("Código do aluno e seleção de cardápio são obrigatórios.", "error") return redirect(url_for("student.reserve")) try : menu_id = int(menu_id) # Verificar se o menu existe e está disponível menu = Menu.query.get(menu_id) if not menu or not menu.is_available: flash("Cardápio selecionado não está disponível.", "error")
```

```
return redirect(url_for("student.reserve")) # Verificar se o aluno já reservou este menu existing_reservation = Reservation.query.filter_by(student_code=student_code, menu_id=menu_id).first() if existing_reservation: flash("Você já reservou este cardápio.", "warning") return redirect(url_for("student.reserve")) # Criar nova reserva new_reservation = Reservation(student_code=student_code, menu_id=menu_id) db.session.add(new_reservation) db.session.commit() flash(f"Reserva para { menu.date.strftime(\" %d /%m/%Y \" )} ( {menu.main_dish} ) realizada com sucesso!", "success") except ValueError: flash("ID do cardápio inválido.", "error") except Exception as e: db.session.rollback() flash(f"Erro ao processar a reserva: { e } ", "error") return redirect(url_for("student.reserve")) # GET Request: Mostrar cardápios disponíveis para reserva (ex: próximos 14 dias) today = date.today() end_date = today + timedelta(days=14) available_menus = Menu.query.filter( Menu.date >= today, Menu.date <= end_date, Menu.is_available == True ).order_by(Menu.date).all() return render_template("reserve.html", menus=available_menus)
```

## src/routes/admin.py

```
# Conteúdo do arquivo 06_backend_admin_routes.py from flask import Blueprint, render_template, request, flash, redirect, url_for, Response from src.models.database import db from src.models.models import Menu, Reservation, CalendarEvent, WeatherData from datetime import datetime, date, timedelta # Adicionado date e timedelta import csv import io admin_bp = Blueprint("admin", __name__, template_folder="../templates/admin") # --- Funções Auxiliares ---
```

```
def parse_date(date_str): """Tenta converter uma string para objeto date (YYYY-MM-DD).""" try : return datetime.strptime(date_str, '%Y-%m%d ').date() # Converte para date except ( ValueError , TypeError ): return None # --- Rotas de Administração --- @admin_bp.route("/") def dashboard(): """Página inicial do painel administrativo.""" today = date.today() # Usar date.today() reservations_today = Reservation.query.join(Menu).filter(Menu.date == today).count() # Passar a função datetimeformat para o template se necessário from jinja2 import pass_context @pass_context def datetimeformat(context, value, format=' %d /%m/%Y'): if isinstance(value, str): # Tentar converter string para date se necessário (pode não ser ideal aqui) try : value = datetime.strptime(value, '%Y-%m%d ').date() except ValueError : return value # Retorna a string original se falhar if isinstance(value, date): return value.strftime(format) return value # Adicionar a função ao ambiente Jinja do Blueprint ou App admin_bp.add_app_template_filter(datetimeformat) return render_template("dashboard.html", reservations_today=reservations_today) # --- Gerenciamento de Cardápios --- @admin_bp.route("/cardapios", methods=["GET", "POST"]) def manage_menus(): """Gerenciar (listar, adicionar, editar) cardápios.""" if request.method == "POST": # Adicionar novo cardápio date_str = request.form.get("date") main_dish = request.form.get("main_dish") description = request.form.get("description") is_available = request.form.get("is_available") == "on" menu_date = parse_date(date_str) if not menu_date or not main_dish: flash("Data e Prato Principal são obrigatórios.", "error") else : # Verificar se já existe cardápio para esta data existing_menu = Menu.query.filter_by(date=menu_date).first() if existing_menu:
```

```
flash(f"Já existe um cardápio cadastrado para { date_str } . Edite-o se necessário.", "warning") else : try : new_menu = Menu( date=menu_date, main_dish=main_dish, description=description, is_available=is_available ) db.session.add(new_menu) db.session.commit() flash("Novo cardápio adicionado com sucesso!", "success") except Exception as e: db.session.rollback() flash(f"Erro ao adicionar cardápio: { e } ", "error") return redirect(url_for("admin.manage_menus")) # GET: Listar cardápios (ex: dos últimos 7 dias e próximos 30) start_date = date.today() - timedelta(days=7) end_date = date.today() + timedelta(days=30) menus = Menu.query.filter(Menu.date >= start_date, Menu.date <= end_date).order_by(Menu.date.desc()).all() return render_template("manage_menus.html", menus=menus) @admin_bp.route("/cardapios/editar/<int:menu_id>", methods=["GET", "POST"]) def edit_menu(menu_id): """Editar um cardápio existente.""" menu = Menu.query.get_or_404(menu_id) if request.method == "POST": date_str = request.form.get("date") main_dish = request.form.get("main_dish") description = request.form.get("description") is_available = request.form.get("is_available") == "on" menu_date = parse_date(date_str) if not menu_date or not main_dish: flash("Data e Prato Principal são obrigatórios.", "error") else : # Verificar se a nova data já está ocupada por OUTRO cardápio existing_menu = Menu.query.filter(Menu.date == menu_date, Menu.id != menu_id).first() if existing_menu: flash(f"Já existe outro cardápio cadastrado para { date_str } .", "warning") else : try : menu.date = menu_date menu.main_dish = main_dish menu.description = description menu.is_available = is_available
```

```
db.session.commit() flash("Cardápio atualizado com sucesso!", "success") return redirect(url_for("admin.manage_menus")) except Exception as e: db.session.rollback() flash(f"Erro ao atualizar cardápio: { e } ", "error") # Se houve erro ou warning, renderiza o form novamente com os dados atuais return render_template("edit_menu.html", menu=menu) # Supondo que exista um template edit_menu.html # GET: Mostrar formulário de edição return render_template("edit_menu.html", menu=menu) @admin_bp.route("/cardapios/deletar/<int:menu_id>", methods=["POST"]) def delete_menu(menu_id): """Deletar um cardápio (cuidado com as reservas associadas!).""" menu = Menu.query.get_or_404(menu_id) try : # Opcional: Verificar se existem reservas antes de deletar ou tratar o erro de FK if menu.reservations: flash("Não é possível deletar cardápio com reservas associadas.", "error") return redirect(url_for("admin.manage_menus")) db.session.delete(menu) db.session.commit() flash("Cardápio deletado com sucesso!", "success") except Exception as e: db.session.rollback() flash(f"Erro ao deletar cardápio: { e } ", "error") return redirect(url_for("admin.manage_menus")) @admin_bp.route("/cardapios/toggle/<int:menu_id>", methods=["POST"]) def toggle_menu_availability(menu_id): """Ativar/Desativar um cardápio para reservas.""" menu = Menu.query.get_or_404(menu_id) try : menu.is_available = not menu.is_available db.session.commit() status = "ativado" if menu.is_available else "desativado" flash(f"Cardápio { status } com sucesso!", "success") except Exception as e: db.session.rollback() flash(f"Erro ao alterar disponibilidade: { e } ", "error") return redirect(url_for("admin.manage_menus")) # --- Importação de Calendário --- @admin_bp.route("/calendario/importar", methods=["GET", "POST"]) def import_calendar(): """Importar eventos do calendário via arquivo CSV.""" if request.method == "POST": if "calendar_file" not in request.files: flash("Nenhum arquivo selecionado.", "error")
```

```
return redirect(request.url) file = request.files["calendar_file"] if fi le.filename == "": flash("Nenhum arquivo selecionado.", "error") return redirect(request.url) if fi le and fi le.filename.endswith(".csv"): try : # Tentar detectar encoding comum (UTF-8 ou Latin-1) try : stream_content = file.stream.read().decode("utf-8") except UnicodeDecodeError : file.stream.seek(0) # Voltar ao início do stream stream_content = file.stream.read().decode("latin-1") stream = io.StringIO(stream_content, newline= None ) csv_reader = csv.reader(stream) header = next(csv_reader) # Pula o cabeçalho # Espera colunas: date, description, type if header != ["date", "description", "type"]: flash("Formato de cabeçalho inválido. Use: date,description,type", "error") return redirect(request.url) count_added = 0 count_skipped = 0 for row in csv_reader: if len(row) == 3: event_date_str, description, event_type = row event_date = parse_date(event_date_str) if event_date and description and event_type: # Opcional: Verificar se já existe evento para essa data antes de adicionar existing_event = CalendarEvent.query.filter_by(date=event_date, description=description, type=event_type).first() if not existing_event: new_event = CalendarEvent(date=event_date, description=description, type=event_type) db.session.add(new_event) count_added += 1 else : count_skipped += 1 else : count_skipped += 1 # Linha inválida else : count_skipped += 1 # Linha com número incorreto de colunas db.session.commit() flash(f" { count_added } eventos importados com sucesso. { count_skipped } linhas ignoradas (inválidas ou duplicadas).", "success")
```

```
except Exception as e: db.session.rollback() flash(f"Erro ao processar o arquivo CSV: { e } ", "error") return redirect(url_for("admin.import_calendar")) else : flash("Formato de arquivo inválido. Use CSV.", "error") return redirect(request.url) # GET: Mostrar formulário de upload # Opcional: Listar eventos existentes events = CalendarEvent.query.order_by(CalendarEvent.date.desc()).limit(20).all() return render_template("import_calendar.html", events=events) # --- Entrada de Dados Climáticos --- @admin_bp.route("/clima", methods=["GET", "POST"]) def input_weather(): """Registrar previsão do tempo para datas futuras.""" if request.method == "POST": date_str = request.form.get("date") max_temp_str = request.form.get("max_temp_forecast") rain_forecast = request.form.get("rain_forecast") == "on" weather_date = parse_date(date_str) max_temp = None if max_temp_str: try : max_temp = float(max_temp_str) except ValueError : flash("Temperatura máxima inválida.", "error") return redirect(url_for("admin.input_weather")) if not weather_date: flash("Data inválida.", "error") else : try : # Verificar se já existe previsão para esta data, se sim, atualiza weather_entry = WeatherData.query.filter_by(date=weather_date).first() if weather_entry: weather_entry.max_temp_forecast = max_temp weather_entry.rain_forecast = rain_forecast weather_entry.forecast_timestamp = datetime.utcnow() flash("Previsão do tempo atualizada com sucesso!", "success") else : new_weather = WeatherData( date=weather_date, max_temp_forecast=max_temp, rain_forecast=rain_forecast ) db.session.add(new_weather) flash("Previsão do tempo registrada com sucesso!", "success") db.session.commit()
```

```
except Exception as e: db.session.rollback() flash(f"Erro ao registrar/atualizar previsão do tempo: { e } ", "error") return redirect(url_for("admin.input_weather")) # GET: Mostrar formulário e talvez previsões recentes recent_weather = WeatherData.query.order_by(WeatherData.date.desc()).limit(10).all() return render_template("input_weather.html", recent_weather=recent_weather) # --- Visualização de Reservas (Opcional) --- @admin_bp.route("/reservas") def view_reservations(): """Listar todas as reservas (pode precisar de paginação).""" # Exemplo simples, sem paginação reservations = Reservation.query.join(Menu).order_by(Menu.date.desc(), Reservation.reservation_timestamp.desc()).all() # Criar um template view_reservations.html para exibir isso # return render_template("view_reservations.html", reservations=reservations) # Por enquanto, apenas retornar uma resposta simples return Response("Página de visualização de reservas a ser implementada.")
```

```
src/main.py
```

```
# Conteúdo do arquivo 04_backend_main.py import sys import os # Garantir que o diretório raiz do projeto esteja no sys.path # NÃO ALTERE AS PRÓXIMAS DUAS LINHAS! sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) from flask import Flask from src.models.database import db # Importa db de src.models.database # Importar Blueprints das rotas from src.routes.student import student_bp from src.routes.admin import admin_bp def create_app(): app = Flask(__name__, instance_relative_config= True , template_folder='templates', # Especifica pasta de templates static_folder='static' # Especifica pasta de estáticos ) # Configuração da Aplicação app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "uma-chave-secretamuito-forte-trocar-depois") # Mude em produção! # Configuração do Banco de Dados SQLite
```

```
# O banco será criado na pasta 'instance' na raiz do projeto db_path = os.path.join(app.instance_path, "database.db") app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:/// { db_path } " app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Criar pasta 'instance' se não existir try : os.makedirs(app.instance_path) except OSError : pass # Pasta já existe # Inicializar o SQLAlchemy com o app db.init_app(app) # Registrar Blueprints (rotas) app.register_blueprint(student_bp, url_prefix='/aluno') # Prefixo para rotas de aluno app.register_blueprint(admin_bp, url_prefix='/admin') # Prefixo para rotas de admin # Criar tabelas do banco de dados dentro do contexto da aplicação with app.app_context(): print("Criando tabelas do banco de dados (se não existirem)...") # Importar modelos aqui para garantir que sejam registrados no SQLAlchemy from src.models import models db.create_all() print("Tabelas criadas.") @app.route("/") def index(): # Redireciona para a página de reserva do aluno por padrão from flask import redirect, url_for return redirect(url_for("student.reserve")) # Redireciona para /aluno/reservar return app # Ponto de entrada para execução direta (para desenvolvimento) if __name__ == "__main__": app = create_app() # Executa o servidor de desenvolvimento Flask # host='0.0.0.0' permite acesso de outras máquinas na rede # debug=True ativa o modo de depuração (NÃO USE EM PRODUÇÃO) app.run(host="0.0.0.0", port=5000, debug= True )
```

## src/\_\_init\_\_.py

Este arquivo pode permanecer vazio. Ele serve para indicar ao Python que o diretório src é um pacote.

src/models/\_\_init\_\_.py Este arquivo pode permanecer vazio.

## src/routes/\_\_init\_\_.py

Este arquivo pode permanecer vazio.

## 4.2. Frontend (HTML/Jinja2 Templates)

## src/templates/base.html

```
<!-- Conteúdo do arquivo 07_frontend_base.html --> <!doctype html> < html lang="pt-BR"> < head > < meta charset="utf-8"> < meta name="viewport" content="width=device-width, initial-scale=1, shrink-tofit=no"> < title >{% block title %}Sistema de Reserva de Refeições - IFSP{% endblock %}</ title > <!-- Adicionar link para CSS (Bootstrap ou customizado) se desejar --> < link rel="stylesheet" href="{{ url_for("static", filename="css/style.css") }}"> < style > body { font-family : sans-serif ; margin : 20px; background-color : #f4f4f4; } nav { background-color : #333; padding : 10px 0; margin-bottom : 20px; } nav ul { list-style : none ; padding : 0; margin : 0; text-align : center ; } nav ul li { display : inline ; margin : 0 15px; } nav ul li a { color : white ; text-decoration : none ; font-weight : bold ; } nav ul li a :hover { text-decoration : underline ; } . container { background-color : white ; padding : 20px; border-radius : 8px; box-shadow : 0 0 10px rgba(0,0,0,0.1); } h1 , h2 { color : #333; } .fl ash-messages { list-style : none ; padding : 0; margin-bottom : 15px; } .fl ash-messages li { padding : 10px; margin-bottom : 10px; border-radius : 4px; } .fl ash-success { background-color : #d4edda; color : #155724; border : 1px solid #c3e6cb; } .fl ash-error { background-color : #f8d7da; color : #721c24; border : 1px solid #f5c6cb; } .fl ash-warning { background-color : #fff3cd; color : #856404; border : 1px solid #ffeeba; } table { width : 100%; border-collapse : collapse ; margin-top : 15px; } th , td { border : 1px solid #ddd; padding : 8px; text-align : left ; } th { background-color : #f2f2f2; } tr :nth-child( even ) { background-color : #f9f9f9; } form label { display : block ; margin-top : 10px; font-weight : bold ; } form input [ type = text ], form input [ type = date ], form input [ type = number ], form textarea , form select { width : calc(100% - 22px); padding : 10px; margin-top : 5px;
```

```
border : 1px solid #ccc; border-radius : 4px; } form input [ type = checkbox ] { margin-right : 5px; } form button { background-color : #5cb85c; color : white ; padding : 10px 15px; border : none ; border-radius : 4px; cursor : pointer ; margin-top : 15px; font-size : 1em; } form button :hover { background-color : #4cae4c; } . button-delete { background-color : #d9534f; } . button-delete :hover { background-color : #c9302c; } . button-toggle { background-color : #f0ad4e; margin-left : 5px; } . button-toggle :hover { background-color : #ec971f; } . button-edit { background-color : #337ab7; margin-left : 5px; } . button-edit :hover { background-color : #286090; } . action-buttons form { display : inline-block ; margin : 0; } </ style > </ head > < body > < nav > < ul > < li >< a href="{{ url_for("student.reserve") }}">Reservar Refeição</ a ></ li > < li >< a href="{{ url_for("admin.dashboard") }}">Painel Admin</ a ></ li > <!-- Adicionar mais links de navegação se necessário --> </ ul > </ nav > < div class="container"> {% with messages = get_flashed_messages(with_categories=true) %} {% if messages %} < ul class="flash-messages"> {% for category, message in messages %} < li class="flash-{{ category }}">{{ message }}</ li > {% endfor %} </ ul > {% endif %} {% endwith %} {% block content %} {% endblock %} </ div > <!-- Adicionar link para JS se desejar --> < script src="{{ url_for("static", filename="js/script.js") }}"></ script > </ body > </ html >
```

## src/templates/student/reserve.html

```
<!-- Conteúdo do arquivo 08_frontend_student_reserve.html --> {% extends "base.html" %} {% block title %}Reservar Refeição{% endblock %} {% block content %} < h2 >Reservar Refeição</ h2 > < form method="post" action="{{ url_for("student.reserve") }}"> < label for="student_code">Seu Código de Aluno:</ label > < input type="text" id="student_code" name="student_code" required> < label for="menu_id">Selecione o Cardápio:</ label > {% if menus %} < select id="menu_id" name="menu_id" required> < option value="" disabled selected>-- Escolha uma data/cardápio --</ option > {% for menu in menus %} < option value="{{ menu.id }}"> {{ menu.date.strftime("%d/%m/%Y") }} - {{ menu.main_dish }} {% if menu.description %}({{ menu.description }}){% endif %} </ option > {% endfor %} </ select > {% else %} < p >Nenhum cardápio disponível para reserva no momento.</ p > {% endif %} < button type="submit" {% if not menus %}disabled{% endif %}>Confirmar Reserva</ button > </ form > {% endblock %}
```

## src/templates/admin/dashboard.html

```
<!-- Conteúdo do arquivo 09_frontend_admin_dashboard.html --> {% extends "base.html" %} {% block title %}Painel Admin{% endblock %} {% block content %} < h2 >Painel de Controle Administrativo</ h2 > < p >Bem-vindo(a) à área administrativa.</ p > {# Usar o filtro datetimeformat definido no admin.py #}
```

```
< p >Total de reservas para hoje ({{ "now"|datetimeformat("%d/%m/%Y") }}): < strong >{{ reservations_today }}</ strong ></ p > < h3 >Ações Rápidas:</ h3 > < ul > < li >< a href="{{ url_for("admin.manage_menus") }}">Gerenciar Cardápios</ a ></ li > < li >< a href="{{ url_for("admin.import_calendar") }}">Importar Calendário/ Eventos</ a ></ li > < li >< a href="{{ url_for("admin.input_weather") }}">Registrar Previsão do Tempo</ a ></ li > < li >< a href="{{ url_for("admin.view_reservations") }}">Visualizar Todas as Reservas</ a ></ li > </ ul > {% endblock %}
```

## src/templates/admin/manage\_menus.html

```
<!-- Conteúdo do arquivo 10_frontend_admin_manage_menus.html --> {% extends "base.html" %} {% block title %}Gerenciar Cardápios{% endblock %} {% block content %} < h2 >Gerenciar Cardápios</ h2 > < h3 >Adicionar Novo Cardápio</ h3 > < form method="post" action="{{ url_for("admin.manage_menus") }}"> < label for="date">Data:</ label > < input type="date" id="date" name="date" required> < label for="main_dish">Prato Principal:</ label > < input type="text" id="main_dish" name="main_dish" required> < label for="description">Descrição Adicional (Opcional):</ label > < textarea id="description" name="description" rows="2"></ textarea > < label for="is_available">Disponível para Reserva?</ label > < input type="checkbox" id="is_available" name="is_available" checked> < button type="submit">Adicionar Cardápio</ button > </ form > < hr style="margin: 30px 0;"> < h3 >Cardápios Cadastrados (Recentes e Futuros)</ h3 > {% if menus %} < table > < thead >
```

```
< tr > < th >Data</ th > < th >Prato Principal</ th > < th >Descrição</ th > < th >Disponível?</ th > < th >Reservas</ th > < th >Ações</ th > </ tr > </ thead > < tbody > {% for menu in menus %} < tr > < td >{{ menu.date.strftime("%d/%m/%Y") }}</ td > < td >{{ menu.main_dish }}</ td > < td >{{ menu.description or "-" }}</ td > < td >{{ "Sim" if menu.is_available else "Não" }}</ td > < td >{{ menu.reservations|length }}</ td > < td class="action-buttons"> < form method="post" action="{{ url_for("admin.toggle_menu_availability", menu_id=menu.id) }}" style="display: inline;"> < button type="submit" class="button-toggle">{{ "Desativar" if menu.is_available else "Ativar" }}</ button > </ form > < a href="{{ url_for("admin.edit_menu", menu_id=menu.id) }}" class="button-edit" style="text-decoration: none; padding: 10px 15px; color: white; border-radius: 4px;">Editar</ a > < form method="post" action="{{ url_for("admin.delete_menu", menu_id=menu.id) }}" style="display: inline;" onsubmit="return confirm("Tem certeza que deseja deletar este cardápio? Esta ação não pode ser desfeita.");"> < button type="submit" class="button-delete">Deletar</ button > </ form > </ td > </ tr > {% endfor %} </ tbody > </ table > {% else %} < p >Nenhum cardápio cadastrado neste período.</ p > {% endif %} {% endblock %}
```

## src/templates/admin/edit\_menu.html

```
<!-- Conteúdo do arquivo 14_frontend_admin_edit_menu.html --> {% extends "base.html" %} {% block title %}Editar Cardápio{% endblock %}
```

```
{% block content %} < h2 >Editar Cardápio - {{ menu.date.strftime("%d/%m/%Y") }}</ h2 > < form method="post" action="{{ url_for("admin.edit_menu", menu_id=menu.id) }}"> < label for="date">Data:</ label > {# Permitir edição da data pode ser complexo se já houver reservas. Considere desabilitar ou adicionar lógica extra #} < input type="date" id="date" name="date" value="{{ menu.date.strftime("%Y%m-%d") }}" required> < label for="main_dish">Prato Principal:</ label > < input type="text" id="main_dish" name="main_dish" value="{{ menu.main_dish }}" required> < label for="description">Descrição Adicional (Opcional):</ label > < textarea id="description" name="description" rows="2">{{ menu.description or "" }}</ textarea > < label for="is_available">Disponível para Reserva?</ label > < input type="checkbox" id="is_available" name="is_available" {% if menu.is_available %}checked{% endif %}> < button type="submit">Salvar Alterações</ button > < a href="{{ url_for("admin.manage_menus") }}" style="margin-left: 10px;">Cancelar</ a > </ form > {% endblock %}
```

## src/templates/admin/import\_calendar.html

```
<!-- Conteúdo do arquivo 11_frontend_admin_import_calendar.html --> {% extends "base.html" %} {% block title %}Importar Calendário/Eventos{% endblock %} {% block content %} < h2 >Importar Calendário/Eventos (CSV)</ h2 > < p >Faça o upload de um arquivo CSV para adicionar eventos ao calendário. O arquivo deve ter as seguintes colunas no cabeçalho: < strong >date,description,type</ strong >.</ p > < p >Formato da data: < strong >YYYY-MM-DD</ strong >.</ p > < p >Exemplo de linha:</ p > < code >2024-12-25,Feriado Nacional,FERIADO</ code >< br > < code >2024-11-15,Semana de Provas,PERIODO_PROVAS</ code > < form method="post" enctype="multipart/form-data" action="{{ url_for("admin.import_calendar") }}">
```

```
< label for="calendar_file">Selecione o arquivo CSV:</ label > < input type="file" id="calendar_file" name="calendar_file" accept=".csv" required> < button type="submit">Importar Eventos</ button > </ form > < hr style="margin: 30px 0;"> < h3 >Eventos Recentes/Próximos</ h3 > {# Opcional: Listar eventos existentes #} {% if events %} < table > < thead >< tr >< th >Data</ th >< th >Descrição</ th >< th >Tipo</ th ></ tr ></ thead > < tbody > {% for event in events %} < tr > < td >{{ event.date.strftime("%d/%m/%Y") }}</ td > < td >{{ event.description }}</ td > < td >{{ event.type }}</ td > </ tr > {% endfor %} </ tbody > </ table > {% else %} < p >Nenhum evento cadastrado recentemente.</ p > {% endif %} {% endblock %}
```

## src/templates/admin/input\_weather.html

```
<!-- Conteúdo do arquivo 12_frontend_admin_input_weather.html --> {% extends "base.html" %} {% block title %}Registrar Previsão do Tempo{% endblock %} {% block content %} < h2 >Registrar/Atualizar Previsão do Tempo</ h2 > < p >Insira a previsão do tempo para uma data futura. Se já existir uma previsão para a data, ela será atualizada.</ p > < form method="post" action="{{ url_for("admin.input_weather") }}"> < label for="date">Data:</ label > < input type="date" id="date" name="date" required> < label for="max_temp_forecast">Temperatura Máxima Prevista (°C) (Opcional):</ label > < input type="number" step="0.1" id="max_temp_forecast"
```

```
name="max_temp_forecast"> < label for="rain_forecast">Haverá Chuva?</ label > < input type="checkbox" id="rain_forecast" name="rain_forecast"> < button type="submit">Salvar Previsão</ button > </ form > < hr style="margin: 30px 0;"> < h3 >Previsões Recentes Registradas</ h3 > {% if recent_weather %} < table > < thead > < tr > < th >Data</ th > < th >Temp. Máx (°C)</ th > < th >Chuva?</ th > < th >Registrado em</ th > </ tr > </ thead > < tbody > {% for weather in recent_weather %} < tr > < td >{{ weather.date.strftime("%d/%m/%Y") }}</ td > < td >{{ weather.max_temp_forecast if weather.max_temp_forecast is not none else "-" }}</ td > < td >{{ "Sim" if weather .rain_forecast else "Não" }}</ td > < td >{{ weather.forecast_timestamp.strftime("%d/%m/%Y %H:%M") }} UTC</ td > </ tr > {% endfor %} </ tbody > </ table > {% else %} < p >Nenhuma previsão do tempo registrada recentemente.</ p > {% endif %} {% endblock %}
```

## 4.3. Arquivos Estáticos (Opcional)

## src/static/css/style.css

Este arquivo pode conter regras CSS customizadas se você não quiser usar os estilos inline no base.html . Por exemplo:

```
/* Exemplo de CSS customizado */ body {
```

```
font-family : Arial, sans-serif ; line-height : 1.6; margin : 0; background-color : #f9f9f9; } . container { max-width : 960px; margin : 20px auto ; padding : 20px; background-color : #fff; border-radius : 8px; box-shadow : 0 2px 4px rgba(0,0,0,0.1); } /* ... mais estilos ... */
```

## src/static/js/script.js

Este arquivo pode conter JavaScript para interatividade no frontend, se necessário.

```
// Exemplo de JavaScript document.addEventListener("DOMContentLoaded", function () { console.log("Sistema de Reservas Carregado."); // Adicionar interatividade aqui, se necessário });
```

## 4.4. Exemplo de Arquivo CSV para Calendário

## calendar\_example.csv

Crie este arquivo na raiz do projeto ( coleta\_dados\_ifsp/ ) para ter um exemplo de como formatar os dados para importação.

```
date,description, type 2024-10-12,Nossa Senhora Aparecida,FERIADO 2024-11-02,Finados,FERIADO 2024-11-15,Proclamação da República,FERIADO 2024-11-18,Início Semana de Provas,PERIODO_PROVAS 2024-11-22,Fim Semana de Provas,PERIODO_PROVAS 2024-12-20,Evento de Fim de Ano,EVENTO 2024-12-25,Natal,FERIADO
```

## 5. Executando a Aplicação

- Certifique-se de que o ambiente virtual está ativo. (Você deve ver (venv) no início do prompt do terminal). 1.
- Navegue até a pasta raiz do projeto ( coleta\_dados\_ifsp/ ) no terminal. 2.
- Execute o script principal: bash python src/main.py 3.
- Você verá mensagens indicando que o servidor Flask está rodando, incluindo algo como: ``` 4.
- Running on http://127.0.0.1:5000 ◦
- Running on http://[seu\_ip\_local]:5000 (Press CTRL+C to quit) ◦
- Restarting with stat ◦
- Debugger is active! ◦
- Debugger PIN: xxx-xxx-xxx Criando tabelas do banco de dados (se não existirem)... Tabelas criadas. `` *(A primeira vez que executar , ele criará o arquivo instance/database.db`)* ◦
- Acesse a aplicação no seu navegador: Abra o navegador e vá para http:// 127.0.0.1:5000 ou http://localhost:5000 . 5.

## 6. Utilizando o Sistema

## 6.1. Interface do Aluno ( /aluno/reservar )

- Esta é a página inicial padrão. ·
- O aluno deve inserir seu Código de Aluno (defina um padrão ou sistema para esses códigos). ·
- O aluno seleciona a Data e o Cardápio desejado na lista suspensa (apenas cardápios futuros e marcados como disponíveis aparecerão). ·
- Ao clicar em "Confirmar Reserva", o sistema registra a reserva no banco de dados. ·
- Mensagens de sucesso, aviso (reserva duplicada) ou erro serão exibidas. ·

## 6.2. Interface Administrativa ( /admin/... )

Acesse o painel administrativo navegando para http://localhost:5000/admin .

- Dashboard ( /admin/ ): ·
- Página inicial com links rápidos para outras seções administrativas. ◦
- Mostra um exemplo de estatística (total de reservas para o dia atual). ◦

## Gerenciar Cardápios ( /admin/cardapios ): ·

- Adicionar: Preencha o formulário com Data, Prato Principal, Descrição (opcional) e marque se está disponível para reserva. Clique em "Adicionar Cardápio". ◦
- Listar: A tabela mostra os cardápios recentes e futuros. ◦
- Ativar/Desativar: Use o botão "Ativar" ou "Desativar" para controlar se um cardápio aparece na lista de reserva dos alunos. ◦
- Editar: Clique no botão "Editar" para modificar os detalhes de um cardápio existente (uma nova página /admin/cardapios/editar/&lt;id&gt; será carregada). ◦
- Deletar: Clique no botão "Deletar". Atenção: Por padrão, não é possível deletar um cardápio que já possui reservas associadas. ◦
- Importar Calendário/Eventos ( /admin/calendario/importar ): ·
- Prepare um arquivo .csv com as colunas date,description,type (veja calendar\_example.csv ). ◦
- Clique em "Escolher arquivo", selecione o CSV e clique em "Importar Eventos". ◦
- O sistema adicionará os eventos ao banco de dados, ignorando duplicatas. ◦
- Uma lista dos eventos recentes/próximos importados é exibida. ◦
- Registrar Previsão do Tempo ( /admin/clima ): ·
- Selecione a Data para a qual a previsão se aplica. ◦
- Insira a Temperatura Máxima Prevista (opcional). ◦
- Marque a caixa "Haverá Chuva?" se aplicável. ◦
- Clique em "Salvar Previsão". Se já existir uma previsão para a data, ela será atualizada. ◦
- Uma lista das previsões recentes registradas é exibida. ◦

## Visualizar Todas as Reservas ( /admin/reservas ): ·

- Esta rota está definida no código ( admin.py ), mas o template HTML ( view\_reservations.html ) não foi criado neste exemplo. Seria necessário criar este template para exibir uma tabela com todas as reservas feitas, possivelmente com filtros por data ou aluno. ◦

## 7. Acessando os Dados

Os dados coletados ficam armazenados no arquivo instance/database.db . Este é um arquivo de banco de dados SQLite.

Você pode acessar esses dados de várias maneiras:

- Programaticamente (Python): Usar scripts Python com SQLAlchemy (como nos exemplos de algoritmos anteriores) para ler os dados das tabelas menus , reservations , calendar\_events e weather\_data . 1.
- Ferramentas de Banco de Dados: Utilizar ferramentas gráficas como o DB Browser for SQLite (gratuito e multiplataforma) para abrir o arquivo database.db , visualizar as tabelas, executar consultas SQL e exportar os dados (ex: para CSV). 2.

## 8. Próximos Passos e Melhorias

- Autenticação: Implementar um sistema de login para a área administrativa. ·
- Validação: Adicionar validações mais robustas nos formulários (backend e frontend). ·
- Interface: Melhorar a interface do usuário com CSS (ex: Bootstrap) e JavaScript. ·
- Paginação: Adicionar paginação nas listas (cardápios, reservas, eventos) se o volume de dados crescer muito. ·
- Relatórios: Criar páginas administrativas para visualizar relatórios e estatísticas de reservas. ·
- API Clima: Integrar com uma API de previsão do tempo para buscar dados climáticos automaticamente. ·
- Deployment: Configurar a aplicação para rodar em um servidor de produção (ex: usando Gunicorn/Nginx ou serviços de hospedagem como PythonAnywhere, Heroku, etc.). Lembre-se de desativar o modo debug em produção. ·

Este documento fornece um guia inicial. Adapte e expanda o sistema conforme as necessidades específicas do IFSP Itaquaquecetuba.