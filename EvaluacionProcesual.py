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

def guardar_datos(productos):
    with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["codigo", "nombre", "precio", "cantidad"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for codigo, producto in productos.items():
            escritor.writerow({
                "codigo": codigo,
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": producto["cantidad"]
            })


def codigo_valido(codigo):
    return (
        codigo.startswith("PROD-")
        and len(codigo) == 8
        and codigo[5:].isdigit()
    )

