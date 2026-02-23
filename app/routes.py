from flask import Blueprint, render_template
from .models import Usuario, Equipo, TareaBackup, Copia, Log

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    total_usuarios = Usuario.query.count()
    total_equipos = Equipo.query.count()
    total_tareas = TareaBackup.query.count()
    total_copias = Copia.query.count()
    total_logs = Log.query.count()

    return render_template(
        "index.html",
        total_usuarios=total_usuarios,
        total_equipos=total_equipos,
        total_tareas=total_tareas,
        total_copias=total_copias,
        total_logs=total_logs,
    )
