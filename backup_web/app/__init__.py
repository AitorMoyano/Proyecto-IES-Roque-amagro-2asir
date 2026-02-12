from flask import Flask
import mysql.connector

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['DB_HOST'] = 'localhost'
    app.config['DB_USER'] = 'root'
    app.config['DB_PASSWORD'] = '12345'
    app.config['DB_NAME'] = 'backup_system'

    # Función para obtener conexión
    def get_db_connection():
        return mysql.connector.connect(
            host=app.config['localhost'],
            user=app.config['root'],
            password=app.config['12345'],
            database=app.config['backupweb']
        )

    # Guardamos la función en la app para usarla en las rutas
    app.get_db_connection = get_db_connection

    # Registrar rutas
    from .routes import routes
    app.register_blueprint(routes)

    return app
