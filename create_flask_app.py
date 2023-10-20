import os
import tkinter as tk
from tkinter import filedialog

def criar_estrutura(projeto, caminho_base, secret_key):
    # Lista de diretórios a serem criados
    diretorios = [
        caminho_base,
        os.path.join(caminho_base, projeto, "app"),
        os.path.join(caminho_base, projeto, "app", "blueprints", "restapi"),
        os.path.join(caminho_base, projeto, "app", "ext"),
        os.path.join(caminho_base, projeto, "app", "models"),
        os.path.join(caminho_base, projeto, "app", "templates"),
        os.path.join(caminho_base, projeto, "app", "static", "img"),
        os.path.join(caminho_base, projeto, "app", "static", "js"),
        os.path.join(caminho_base, projeto, "app", "static", "css"),
        os.path.join(caminho_base, projeto, "app", "tests"),
        os.path.join(caminho_base, projeto, "app", "controllers"),
        os.path.join(caminho_base, projeto, "app", "helpers"),
        os.path.join(caminho_base, projeto,  "app", "templates", "components", "dumps"),
        os.path.join(caminho_base, projeto,  "app", "templates", "components", "macros"),
        os.path.join(caminho_base, projeto, "app", "static", "img"),
    ]

    # Crie os diretórios
    for diretorio in diretorios:
        os.makedirs(diretorio, exist_ok=True)

    # Crie os arquivos
    arquivos = [
        os.path.join(caminho_base, projeto,  "app", "blueprints", "views.py"),
        os.path.join(caminho_base, projeto,  "app", "blueprints", "__init__.py"),
        os.path.join(caminho_base, projeto,  "app", "blueprints", "restapi", "__init__.py"),
        os.path.join(caminho_base, projeto,  "app", "blueprints", "restapi", "resources.py"),
        os.path.join(caminho_base, projeto,  "app", "ext", "__init__.py"),
        os.path.join(caminho_base, projeto,  "app", "ext", "configuration.py"),
        os.path.join(caminho_base, projeto,  "app", "ext", "database.py"),
        os.path.join(caminho_base, projeto,  "app", "models", "__init__.py"),
        os.path.join(caminho_base, projeto,  "app", "models", "model.py"),
        os.path.join(caminho_base, projeto,  "app", "templates", "base.html"),
        os.path.join(caminho_base, projeto,  "app", "app.py"),
        os.path.join(caminho_base, projeto,  "app", "__init__.py"),
        os.path.join(caminho_base, projeto, ".env"),
        os.path.join(caminho_base, projeto, ".gitignore"),
        os.path.join(caminho_base, projeto, "settings.toml"),
        os.path.join(caminho_base, projeto, "app", "controllers", "__init__.py"),
        os.path.join(caminho_base, projeto, "app", "static", "js", "main.js"),
        os.path.join(caminho_base, projeto, "app", "static", "css", "styles.css"),
        os.path.join(caminho_base, projeto, "app", "helpers", "__init__.py"),
        os.path.join(caminho_base, projeto, "app", "ext", "auth.py")
    ]

    for arquivo in arquivos:
        with open(arquivo, "w") as f:
            pass

    # Adicione o código Dynaconf a configuration.py
    with open(os.path.join(caminho_base, projeto, "app", "ext", "configuration.py"), "a") as f:
        f.write('# Configuração Dynaconf\n')
        f.write('from importlib import import_module\n')
        f.write('from dynaconf import FlaskDynaconf\n')
        f.write('\n')
        f.write('def load_extensions(app):\n')
        f.write('   for extension in app.config.get("EXTENSIONS"):\n')
        f.write('       mod = import_module(extension)\n')
        f.write('       mod.init_app(app)\n')
        f.write('\n')
        f.write('def init_app(app):\n')
        f.write('    FlaskDynaconf(app)\n')

    # Adicione o código SQLAlchemy a app.py
    with open(os.path.join(caminho_base, projeto, "app", "ext", "database.py"), "a") as f:
        f.write('# Configuração SQLAlchemy\n')
        f.write('from flask_sqlalchemy import SQLAlchemy\n')
        f.write('\n')
        f.write('db = SQLAlchemy()')
        f.write('\n\n')
        f.write('def init_app(app):\n')
        f.write('    db.init_app(app)\n')
        
    # Adicione o código Flask_login a auth.py
    with open(os.path.join(caminho_base, projeto, "app", "ext", "auth.py"), "a") as f:
        f.write('# Configuração Flask_login\n')
        f.write('from flask_login import LoginManager\n')
        f.write('\nlogin_manager = LoginManager()\n')
        f.write('\ndef init_app(app):\n')
        f.write('    login_manager.init_app(app)\n')
        f.write('    login_manager.login_view = "auth.login" \n')

    # Adicione o código Factory a app.py
    with open(os.path.join(caminho_base, projeto, "app", "app.py"), "a") as f:
        f.write('# Arquivo principal da aplicacao\n')
        f.write('from flask import Flask\n')
        f.write('from app.ext import configuration\n')
        f.write('\n')
        f.write('\ndef minimal_app():\n')
        f.write('    app = Flask(__name__)\n')
        f.write('    configuration.init_app(app)\n')
        f.write('\n')
        f.write('    return app\n\n')
        f.write('\ndef create_app():\n')
        f.write('    app = minimal_app()\n')
        f.write('    configuration.load_extensions(app)\n')
        f.write('\n')
        f.write('    return app\n\n')

    # Adicione o código Settings a toml.py
    with open(os.path.join(caminho_base, projeto, "settings.toml"), "a") as f:
        f.write('[default]\n')
        f.write(f'SECRET_KEY="{secret_key}"\n')
        f.write(f'EXTENSIONS=[\n')
        f.write(f'  "app.ext.database",\n')
        f.write(f'  "app.blueprints.views",\n')
        f.write(f']\n')
        f.write('\n')
        f.write('FLASK_DEBUG=true\n')
        f.write('SQLALCHEMY_DATABASE_URI= "sqlite:///store.db"\n')

    # Adicione o código Routes a views.py
    with open(os.path.join(caminho_base, projeto, "app", "blueprints", "views.py"), "a") as f:
        f.write('\n\n')
        f.write(f'def init_app(app):\n')
        f.write('   # registre seus blueprints ex.: app.register_blueprint(modulo)\n\n')
        f.write('   @app.route("/")\n')
        f.write('   def index():\n')
        f.write('       return {"Hello":"World"}\n\n')

    # Adicione o código Requeriments a requirements.txt
    with open(os.path.join(caminho_base, projeto, "requirements.txt"), "a") as f:
        f.write('Flask\n')
        f.write('Flask-SQLAlchemy\n')
        f.write('dynaconf\n')
        f.write('python-dotenv\n')
        f.write('flask-login\n')
    
    # Adicione o código Env a .env
    with open(os.path.join(caminho_base, projeto, ".env"), "a") as f:
        f.write('FLASK_ENV=development\n')
        f.write('FLASK_DEBUG=true\n')
        f.write(f'FLASK_APP=app/app.py')

    print(f"Estrutura do projeto '{projeto}' criada com sucesso em '{caminho_base}'.")

    print(f"Acesse a pasta {caminho_base}/{projeto}")

    print('Crie o ambiente virtual de sua escolha ex: "python -m venv venv"\n')
    print('Acesse o ambiente virtual criado ex: "venv/script/activate.ps1"\n')
    print('Instale as bibliotecas com o comando "pip install -r requirements.txt"\n')

    print("Rode o projeto com 'flask run'")

# Cria uma janela de diálogo para o usuário escolher o diretório
root = tk.Tk()
root.withdraw()  # Esconde a janela principal
projeto = input("Digite o nome do projeto Flask: ").strip()
secret_key = input("Escolha uma chave secreta: ").strip()

# Solicita ao usuário escolher o diretório base
caminho_base = filedialog.askdirectory(title="Escolha o diretório base para o projeto")

# Verifica se o usuário cancelou a seleção do diretório
if not caminho_base:
    print("Seleção de diretório cancelada. Encerrando o script.")
else:
    criar_estrutura(projeto, caminho_base, secret_key)