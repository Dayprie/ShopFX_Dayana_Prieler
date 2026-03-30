import os
import shutil
from datetime import datetime


origen = "C:/Users/sprie/OneDrive/Documentos/Informatica estudio/origen_php"


destino = "C:/Users/sprie/Music/backup_php"

if not os.path.exists(origen):
    print("ERROR: La carpeta origen no existe:", origen)
    exit()


if not os.path.exists(destino):
    os.makedirs(destino)

prefijo = "backup_"
contador = 0

print("Iniciando proceso...\n")


for archivo in os.listdir(origen):
    if archivo.endswith(".php"):
        ruta_origen = os.path.join(origen, archivo)

        fecha = datetime.now().strftime("%Y%m%d_%H%M%S")
        nuevo_nombre = f"{prefijo}{fecha}_{archivo}"

        ruta_destino = os.path.join(destino, nuevo_nombre)

        shutil.copy2(ruta_origen, ruta_destino)

        print(f"✔ Archivo copiado: {archivo} → {nuevo_nombre}")
        contador += 1

print(f"\nProceso finalizado. Archivos procesados: {contador}")