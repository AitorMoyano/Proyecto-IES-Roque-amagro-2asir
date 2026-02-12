from flask import Blueprint, current_app

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    conn = current_app.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipos")
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return "OK"
