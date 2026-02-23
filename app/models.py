from . import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)

class Equipo(db.Model):
    __tablename__ = "equipos"

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(45), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    sistema_operativo = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)

class TareaBackup(db.Model):
    __tablename__ = "tareas_backup"

    id = db.Column(db.Integer, primary_key=True)
    equipos_id = db.Column(db.Integer, db.ForeignKey("equipos.id"))
    tipo = db.Column(db.String(50), nullable=False)
    ruta_origen = db.Column(db.String(255), nullable=False)
    frecuencia = db.Column(db.String(50), nullable=False)
    hora = db.Column(db.Time, nullable=False)
    activo = db.Column(db.Boolean, default=True)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)

class Copia(db.Model):
    __tablename__ = "copias"

    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey("equipos.id"))
    tarea_id = db.Column(db.Integer, db.ForeignKey("tareas_backup.id"))
    ruta_backup = db.Column(db.String(255), nullable=False)
    tamano = db.Column(db.BigInteger)
    estado = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

class Log(db.Model):
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    equipo_id = db.Column(db.Integer, db.ForeignKey("equipos.id"))
    accion = db.Column(db.String(100), nullable=False)
    detalle = db.Column(db.Text)
