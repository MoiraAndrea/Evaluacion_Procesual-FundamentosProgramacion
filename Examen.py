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

