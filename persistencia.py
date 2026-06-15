# Importar librería csv
import csv

#CONSTANTES
# Constante de nombre de archivo
ARCHIVO_PAISES = "paises.csv"
# Constante de campos del archivo
CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

def cargar_paises():
  """
  Carga los países desde el archivo CSV.
  
  Returns:
    list: Lista de diccionarios con los países.
  """
  # Inicializar lista de países
  paises = []

  # Intentar cargar los países desde el archivo
  try:
    # Abrir el archivo en modo lectura
    with open(ARCHIVO_PAISES, "r", encoding="utf-8") as archivo:
      # Leer el archivo como diccionarios
      lector = csv.DictReader(archivo)

      # Recorrer cada fila del archivo
      for fila in lector:
        # Agregar cada país a la lista
        paises.append({
          "nombre": fila["nombre"],
          "poblacion": int(fila["poblacion"]),
          "superficie": int(fila["superficie"]),
          "continente": fila["continente"]
        })

  # Si hay un error de formato, mostrarlo
  except ValueError as e:
    print(f"Error de formato en el archivo CSV: {e}")

  # Si el archivo no existe, crearlo
  except FileNotFoundError:
    with open(ARCHIVO_PAISES, "w", newline="", encoding="utf-8") as archivo:
      escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
      escritor.writeheader()

  # Si hay otro error inesperado, mostrarlo
  except Exception as e:
    print(f"Error inesperado al cargar los países: {e}")

  # Retornar la lista de países
  return paises

def guardar_paises(paises):
  """
  Guarda los países en el archivo CSV.
  
  Args:
    paises (list): Lista de diccionarios con los países.
  """
  # Intentar guardar los países en el archivo
  try:
    # Abrir el archivo en modo escritura
    with open(ARCHIVO_PAISES, "w", newline="", encoding="utf-8") as archivo:
      # Escribir el archivo como diccionarios
      escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
      # Escribir el encabezado
      escritor.writeheader()
      # Escribir los países
      escritor.writerows(paises)

  # Si el archivo está abierto en otro programa, mostrar error
  except PermissionError:
    print("Error al guardar los países: No se puede escribir en el archivo porque está siendo utilizado por otro programa.")

  # Si hay un error inesperado, mostrarlo
  except Exception as e:
    print(f"Error inesperado al guardar los países: {e}")