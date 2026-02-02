import subprocess

ARCHIVO_BACKUP = "/backups/backup_local_20260201_120000.tar.gz"
DESTINO = "/home/usuario/restaurado"

def restaurar_backup():
    comando = [
        "tar",
        "-xzf",
        ARCHIVO_BACKUP,
        "-C",
        DESTINO
    ]

    try:
        subprocess.run(comando, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    if restaurar_backup():
        print("Restauración completada")
    else:
        print("Error al restaurar el backup")
