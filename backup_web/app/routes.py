from flask import Blueprint, render_template
from . import mysql

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/equipos')
def equipos():
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM equipos")
    equipos = cursor.fetchall()
    cursor.close()
    return render_template('equipos.html', equipos=equipos)
