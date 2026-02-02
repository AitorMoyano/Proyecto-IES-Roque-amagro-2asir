import subprocess
from datetime import datetime

ORIGEN = "/home/usuario/datos/"
USUARIO_REMOTO = "backupuser"
HOST_REMOTO = "192.168.1.50"
DESTINO_REMOTO = "/srv/backups/cliente1"

LOGS = "/var/log/backup_rsync.log"

def backup_rsync():
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    comando = [
        "rsync",
        "-avz",
        "--delete",
        ORIGEN,
        f"{USUARIO_REMOTO}@{HOST_REMOTO}:{DESTINO_REMOTO}"
    ]

    try:
        resultado = subprocess.run(
            comando,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        with open(LOGS, "a") as log:
            log.write(f"[{fecha}] BACKUP OK\n")
            log.write(resultado.stdout)

        return True

    except subprocess.CalledProcessError as e:
        with open(LOGS, "a") as log:
            log.write(f"[{fecha}] ERROR\n")
            log.write(e.stderr)

        return False


if __name__ == "__main__":
    if backup_rsync():
        print("Backup remoto realizado correctamente")
    else:
        print("Error en el backup remoto")
