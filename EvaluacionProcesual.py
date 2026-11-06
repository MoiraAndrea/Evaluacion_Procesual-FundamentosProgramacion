import csv

ARCHIVO = "inventario.csv"

def cargar_datos():
    productos = {}
    try:
        with open(ARCHIVO, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                codigo = fila["codigo"]
                productos[codigo] = {
                    "nombre": fila["nombre"],
                    "precio": float(fila["precio"]),
                    "cantidad": int(fila["cantidad"])
                }
    except FileNotFoundError:
        pass
    except (KeyError, ValueError):
        print("El archivo de inventario tiene datos invalidos.")
    return productos
