from backups import backup_rsync

def lanzar_backup_desde_web():
    resultado = backup_rsync()
    # guardar resultado en BBDD
