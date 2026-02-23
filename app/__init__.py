from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:12345@localhost/backup_system"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "clave-super-secreta"

    db.init_app(app)

    # Registrar rutas
    from .routes import routes
    app.register_blueprint(routes)

    return app
