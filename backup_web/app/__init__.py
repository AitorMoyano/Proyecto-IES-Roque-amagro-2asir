from flask import Flask
from flask_mysql_connector import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clave_super_secreta'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'backupuser'
    app.config['MYSQL_PASSWORD'] = 'TuPasswordSegura'
    app.config['MYSQL_DATABASE'] = 'backup_system'

    mysql.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
