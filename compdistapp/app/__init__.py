# app/__init__.py
import os
import logging
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin

# Instancia as extensões da aplicação
db = SQLAlchemy()
migrate = Migrate()
auth = HTTPBasicAuth()
admin = Admin(name='Super App', template_mode='bootstrap4')

def create_app():
    app = Flask("Comp Dist")

    # Carregar configuração
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.py')
    app.config.from_pyfile(config_path)

    # Configuração do logger
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(filename=os.path.join(log_dir, 'app.log'), level=logging.INFO)
    log = logging.getLogger()

    # Inicializa as extensões
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    # Importa e registra blueprints
    from .views.auth_views import auth_bp
    from .views.admin_views import custom_admin_bp, ProfileView  # Importa ProfileView
    from .models.profile import Profile
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(custom_admin_bp, url_prefix='/admin')

    # Adiciona a ProfileView ao admin
    admin.add_view(ProfileView(Profile, db.session))

    return app
