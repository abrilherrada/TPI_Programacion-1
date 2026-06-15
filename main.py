# Importaciones de módulos
from persistencia import cargar_paises, guardar_paises
from validaciones import validar_opcion_menu
from paises import agregar_pais, actualizar_pais, buscar_pais, filtrar_paises, ordenar_paises
from estadisticas import mostrar_estadisticas

def mostrar_menu():
  """
  Muestra el menú principal y retorna la opción seleccionada.
  
  Returns:
    str: La opción seleccionada por el usuario.
  """
  # Título para dar contexto al usuario
  print("\n=== MENÚ PRINCIPAL ===")

  # Solicitar opción al usuario
  opcion = input("""
    Elige una opción:
      1. Agregar país
      2. Actualizar país
      3. Buscar país
      4. Filtrar países
      5. Ordenar países
      6. Mostrar estadísticas
      7. Salir
    
    Opción seleccionada: """)

  # Retornar la opción seleccionada
  return opcion

def salir():
  """
  Muestra un mensaje de despedida y retorna False para salir del sistema.
  
  Returns:
    bool: False para indicar que el sistema debe detenerse.
  """
  # Título para dar contexto al usuario
  print("\n--- SALIR DEL SISTEMA ---")

  # Mensaje de despedida
  print("Gracias por usar el sistema de gestión de países.\n")

  # Retornar False para indicar que el sistema debe detenerse
  return False

# BLOQUE PRINCIPAL

# Título para dar contexto al usuario
print("\n===== SISTEMA DE GESTIÓN DE PAÍSES =====\n")

# Variables globales
# Lista para almacenar los países cargados desde el archivo csv
paises = cargar_paises()
# Variable para controlar el ciclo del sistema
sistema_activo = True

# Bucle principal del sistema
while sistema_activo:
  # Intentar ejecutar el menú y las operaciones
  try:
    # Mostrar el menú y obtener la opción seleccionada
    opcion = mostrar_menu().strip()
    # Validar la opción seleccionada
    validar_opcion_menu(opcion, (1, 7))

    # Procesar la opción seleccionada
    match opcion:
      # Agregar país
      case "1":
        # Intentar agregar un país
        if agregar_pais(paises):
          # Si hubo cambios, guardar los países actualizados
          guardar_paises(paises)

      # Actualizar país
      case "2":
        # Intentar actualizar un país
        if actualizar_pais(paises):
          # Si hubo cambios, guardar los países actualizados
          guardar_paises(paises)

      # Buscar país
      case "3":
        buscar_pais(paises)

      # Filtrar países
      case "4":
        filtrar_paises(paises)

      # Ordenar países
      case "5":
        ordenar_paises(paises)

      # Mostrar estadísticas
      case "6":
        mostrar_estadisticas(paises)

      # Salir
      case "7":
        sistema_activo = salir()

  # Manejar errores de entrada
  except ValueError as error:
    print(f"Error de entrada: {error}")

  # Manejar errores inesperados
  except Exception as error:
    print(f"Error inesperado: {error}")