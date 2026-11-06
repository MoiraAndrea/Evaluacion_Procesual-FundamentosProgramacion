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

def registrar_producto(productos):
    codigo = input("Codigo (ejemplo PROD-001): ").strip().upper()
    if not codigo_valido(codigo):
        print("El codigo debe tener el formato PROD-001.")
        return
    if codigo in productos:
        print("Ya existe un producto con ese codigo.")
        return

    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacio.")
        return

    try:
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad disponible: "))
        if precio <= 0 or cantidad < 0:
            raise ValueError
    except ValueError:
        print("El precio debe ser mayor que cero y la cantidad un entero no negativo.")
        return

    productos[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    guardar_datos(productos)
    print("Producto registrado correctamente.")


def consultar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return

    for codigo, producto in productos.items():
        print(f"{codigo} | {producto['nombre']} | ${producto['precio']:.2f} | "
              f"Cantidad: {producto['cantidad']}")


def actualizar_cantidad(productos):
    codigo = input("Codigo del producto: ").strip().upper()
    if codigo not in productos:
        print("El producto no esta registrado.")
        return

    try:
        cantidad = int(input("Nueva cantidad disponible: "))
        if cantidad < 0:
            raise ValueError
    except ValueError:
        print("La cantidad debe ser un entero mayor o igual que cero.")
        return

    productos[codigo]["cantidad"] = cantidad
    guardar_datos(productos)
    print("Cantidad actualizada correctamente.")


def mostrar_menu():
    print("\n--- INVENTARIO ---")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Actualizar cantidad")
    print("4. Salir")


def main():
    productos = cargar_datos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_producto(productos)
        elif opcion == "2":
            consultar_productos(productos)
        elif opcion == "3":
            actualizar_cantidad(productos)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    main()

