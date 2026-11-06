import csv 
ARCHIVO = "inventario.csv"

def cargar_datos():
    """Recupera los productos almacenados previamente en el archivo CSV."""
    productos = {}
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    codigo = row["codigo"]
                    productos[codigo] = {
                        "nombre": row["nombre"],
                        "precio": float(row["precio"]),
                        "cantidad": int(row["cantidad"])
                    }
        except Exception as e:
            print(f"Error al cargar los datos del archivo: {e}")
    return productos

def guardar_datos(productos):
    """Guarda de forma persistente los productos en un archivo CSV."""
    try:
        with open(ARCHIVO, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["codigo", "nombre", "precio", "cantidad"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for codigo, datos in productos.items():
                writer.writerow({
                    "codigo": codigo,
                    "nombre": datos["nombre"],
                    "precio": datos["precio"],
                    "cantidad": datos["cantidad"]
                })
    except Exception as e:
        print(f"Error al guardar los datos en el archivo: {e}")
