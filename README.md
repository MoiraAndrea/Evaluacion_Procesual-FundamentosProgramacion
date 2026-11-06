# EVALUACIÓN PROCESUAL 
PROGRAMACIÓN FUNDAMENTAL PFU-111
GRUPO 2

# Integrantes:

 | Integrante | Usuario de GitHub | Rol / Función |
| :--- | :--- | :--- |  
| Claudio Yamil Torres Calle | [@salva451](https://github.com/salva451) | Programador |
| Cesar Nayib Luis Sumi Urbina | [@ClaudioYamil](https://github.com/ClaudioYamil) | Programador |
| Moira Andrea Yampa Guerra | [@MoiraAndrea](https://github.com/MoiraAndrea) | Programador |
| Nicolás Sebastián López Chino | [@nicmax06](https://github.com/nicmax06) | Redactor |
| Pedro Efrain Rada Saramani | [@nicmax06](https://github.com/nicmax06) | Redactor |


# Proyecto: Sistema de Gestión Modernizada

## Descripción del Proyecto
Este proyecto consiste en un prototipo funcional desarrollado en Python para modernizar el sistema de gestión de inventario de una distribuidora comercial. La solución reemplaza la administración manual mediante hojas de cálculo y archivos de texto desorganizados por una aplicación interactiva en consola, incorporando validaciones de datos, manejo seguro de errores y persistencia de información.

## Problema que Busca Resolver
La distribuidora comercial presentaba inconsistencias debido al uso de un sistema legado sin mecanismos de validación. Lo que provocaba.
- Registro de productos duplicados.
- Cantidades inconsistentes o negativas.
- Errores de formato en los códigos y datos de los productos.
- Riesgo de pérdida o corrupción de datos.

## Funcionalidades Implementadas
- **Menú Interactivo en Consola:** Navegación sencilla y estructurada mediante ciclos y condicionales.
- **Registro de Nuevos Productos:** Captura de código, nombre, precio unitario y cantidad disponible.
- **Consulta de Productos:** Listado y visualización del inventario registrado en el sistema.
- **Actualización de Existencias:** Modificación del stock de productos registrados sin permitir saldos negativos.
- **Validación Rigurosa de Datos:** 
  - Formato de código obligatorio (ej. `PROD-001`).
  - Precios estrictamente mayores a cero (>0).
  - Cantidades enteras mayores o iguales a cero (0).
  - Restricción de duplicidad en códigos de producto.
- **Manejo de Excepciones:** Control de errores con bloques `try-except` para evitar el cierre inesperado del programa ante entradas inválidas.
- **Persistencia de Datos:** Lectura y escritura de registros en archivos de texto/CSV para conservar la información entre ejecuciones.

## Instrucciones Básicas de Ejecución

### Pasos para Ejecutar
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/MoiraAndrea/Evaluacion_Procesual-FundamentosProgramacion


CÓDIGO FUENTE (FINAL):

https://github.com/MoiraAndrea/Evaluacion_Procesual-FundamentosProgramacion/commit/31c6b1211ca32a09f29353772e4b22fabe9df05c



VALIDACIONES :

https://github.com/MoiraAndrea/Evaluacion_Procesual-FundamentosProgramacion/commit/ecfdef8dd2fcb42d66dacf05ad930d918516cb7e
