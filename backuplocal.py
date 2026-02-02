import os
import subprocess
from datetime import datetime

# Configuración
ORIGEN = "/home/usuario/datos"
DESTINO = "/backups"
NOMBRE = "backup_local"

# Fecha
fecha = datetime.now().strftime("%Y%m%d_%H%M%S")

archivo_backup = f"{DESTINO}/{NOMBRE}_{fecha}.tar.gz"

def hacer_backup():
    try:
        os.makedirs(DESTINO, exist_ok=True)

        comando = [
            "tar",
            "-czf",
            archivo_backup,
            ORIGEN
        ]

        subprocess.run(comando, check=True)

        return True, archivo_backup

    except subprocess.CalledProcessError as e:
        return False, str(e)


if __name__ == "__main__":
    ok, resultado = hacer_backup()

    if ok:
        print(f"Backup creado correctamente: {resultado}")
    else:
        print(f"Error en el backup: {resultado}")
