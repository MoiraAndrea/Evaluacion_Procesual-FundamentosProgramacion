import os
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

def registrar_producto(productos):
    """Registra un nuevo producto aplicando validaciones de formato y duplicados."""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    
    # Validación del código del producto (ej. PROD-001)
    while True:
        codigo = input("Ingrese el código del producto (ej. PROD-001): ").strip().upper()
        if not codigo:
            print("El código del producto no debe estar vacío[span_7](start_span)[span_7](end_span).")
            continue
        if not (codigo.startswith("PROD-") and len(codigo) > 5):
            print("Formato inválido. Debe respetar el formato establecido (ej. PROD-001)[span_8](start_span)[span_8](end_span).")
            continue
        if codigo in productos:
            print("Error: Ya existe un producto registrado con ese código (duplicado)[span_9](start_span)[span_9](end_span).")
            continue
        break

    # Validación del nombre del producto
    while True:
        nombre = input("Ingrese el nombre o descripción del producto: ").strip()
        if not nombre:
            print("El nombre del producto no debe estar vacío[span_10](start_span)[span_10](end_span).")
            continue
        break

    # Validación del precio unitario (> 0)
    while True:
        try:
            precio = float(input("Ingrese el precio unitario (> 0): "))
            if precio <= 0:
                print("El precio unitario debe ser un número mayor que cero[span_11](start_span)[span_11](end_span).")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido[span_12](start_span)[span_12](end_span).")

    # Validación de la cantidad disponible (>= 0)
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible (>= 0): "))
            if cantidad < 0:
                print("La cantidad disponible debe ser un número entero igual o mayor que cero[span_13](start_span)[span_13](end_span).")
                continue
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido[span_14](start_span)[span_14](end_span).")

    # Almacenamiento en el diccionario y persistencia
    productos[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    guardar_datos(productos)
    print(f"¡Producto '{nombre}' registrado y guardado con éxito!")

def consultar_productos(productos):
    """Muestra el listado de todos los productos registrados."""
    print("\n--- CONSULTAR PRODUCTOS REGISTRADOS ---")
    if not productos:
        print("No hay productos registrados en el inventario.")
        return
    
    print(f"{'CÓDIGO':<12} | {'NOMBRE/DESCRIPCIÓN':<25} | {'PRECIO ($)':<12} | {'CANTIDAD':<10}")
    print("-" * 65)
    for codigo, datos in productos.items():
        print(f"{codigo:<12} | {datos['nombre']:<25} | {datos['precio']:<12.2f} | {datos['cantidad']:<10}")

def actualizar_cantidad(productos):
    """Actualiza la cantidad disponible verificando existencias y evitando negativos."""
    print("\n--- ACTUALIZAR CANTIDAD DISPONIBLE ---")
    if not productos:
        print("No hay productos registrados para actualizar.")
        return

    codigo = input("Ingrese el código del producto a actualizar: ").strip().upper()
    if codigo not in productos:
        print("Error: El producto no se encuentra previamente registrado[span_15](start_span)[span_15](end_span).")
        return

    print(f"Producto seleccionado: {productos[codigo]['nombre']} | Stock actual: {productos[codigo]['cantidad']}")

    while True:
        try:
            opcion = input("¿Desea (1) sumar/restar al stock actual o (2) establecer un nuevo stock directo? (1/2): ").strip()
            if opcion not in ['1', '2']:
                print("Opción inválida. Ingrese 1 o 2.")
                continue
            
            valor = int(input("Ingrese la cantidad numérica: "))
            
            if opcion == '1':
                nueva_cantidad = productos[codigo]['cantidad'] + valor
            else:
                nueva_cantidad = valor

            if nueva_cantidad < 0:
                print("Error: La operación no debe generar cantidades negativas en el inventario[span_16](start_span)[span_16](end_span).")
                continue

            productos[codigo]['cantidad'] = nueva_cantidad
            guardar_datos(productos)
            print(f"¡Stock actualizado con éxito! Nueva cantidad disponible: {nueva_cantidad}")
            break
        except ValueError:
            print("Error: Ingrese un valor numérico entero válido[span_17](start_span)[span_17](end_span).")

def menu():
    """Controla el flujo del menú interactivo en consola."""
    productos = cargar_datos()
    while True:
        print("\n==========================================")
        print("   SISTEMA DE GESTIÓN DE INVENTARIO - PFU ")
        print("==========================================")
        print("1. Registrar un nuevo producto")
        print("2. Consultar los productos registrados")
        print("3. Actualizar la cantidad disponible de un producto")
        print("4. Salir del programa")
        
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if opcion == 1:
                registrar_producto(productos)
            elif opcion == 2:
                consultar_productos(productos)
            elif opcion == 3:
                actualizar_cantidad(productos)
            elif opcion == 4:
                print("Saliendo del sistema de gestión. ¡Hasta luego!")
                break
            else:
                print("Opción fuera de rango. Seleccione un número entre 1 y 4.")
        except ValueError:
            print("Error: Entrada no válida. Ingrese un número entero correspondiente al menú[span_18](start_span)[span_18](end_span).")

if __name__ == "__main__":
    menu()