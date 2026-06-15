# Constante de continentes
CONTINENTES = ["África", "América", "Antártida", "Asia", "Europa", "Oceanía"]

def validar_nombre(nombre):
  """
  Valida que el nombre no esté vacío y que contenga solo letras.
  
  Args:
    nombre (str): El nombre a validar.
  
  Raises:
    ValueError: Si el nombre está vacío o contiene caracteres no alfabéticos.
  """
  if not nombre.strip():
    raise ValueError("El nombre no puede estar vacío.")
  elif not nombre.replace(" ", "").isalpha():
    raise ValueError("El nombre debe contener solo letras.")

def validar_poblacion(poblacion):
  """
  Valida que la población no esté vacía y que sea un número entero mayor a 0.
  
  Args:
    poblacion (str): La población a validar.
  
  Raises:
    ValueError: Si la población está vacía, no es un número entero o es menor o igual a 0.
  """
  if not poblacion.strip():
    raise ValueError("La población no puede estar vacía.")
  elif not poblacion.isdigit():
    raise ValueError("La población debe ser un número entero.")
  elif int(poblacion) <= 0:
    raise ValueError("La población debe ser mayor a 0.")

def validar_superficie(superficie):
  """
  Valida que la superficie no esté vacía y que sea un número mayor a 0.
  
  Args:
    superficie (str): La superficie a validar.
  
  Raises:
    ValueError: Si la superficie está vacía, no es un número entero o es menor o igual a 0.
  """
  if not superficie.strip():
    raise ValueError("La superficie no puede estar vacía.")
  elif not superficie.isdigit():
    raise ValueError("La superficie debe ser un número.")
  elif int(superficie) <= 0:
    raise ValueError("La superficie debe ser mayor a 0.")

def validar_continente(continente):
  """
  Valida que el continente no esté vacío y que sea uno de los continentes válidos.
  
  Args:
    continente (str): El continente a validar.
  
  Raises:
    ValueError: Si el continente está vacío o no es válido.
  """
  if not continente.strip():
    raise ValueError("El continente no puede estar vacío.")
  elif continente not in CONTINENTES:
    raise ValueError("El continente no es válido.\nIngrese África, América, Antártida, Asia, Europa o Oceanía.")

def validar_opcion_menu(opcion, rango):
  """
  Valida que la opción del menú no esté vacía y que sea un número entero dentro del rango especificado.
  
  Args:
    opcion (str): La opción a validar.
    rango (tuple): El rango de valores válidos (min, max).
  
  Raises:
    ValueError: Si la opción está vacía, no es un número entero o está fuera del rango.
  """
  if not opcion.strip():
    raise ValueError("La opción no puede estar vacía.")
  elif not opcion.isdigit():
    raise ValueError("La opción debe ser un número entero.")
  elif int(opcion) < rango[0] or int(opcion) > rango[1]:
    raise ValueError(f"El valor ingresado debe ser un número entre {rango[0]} y {rango[1]}.")

def validar_rango(numero1, numero2):
  """
  Valida que los números no estén vacíos y que sean números enteros mayores o iguales a 0.
  También valida que el primer número sea menor o igual al segundo.
  
  Args:
    numero1 (str): El primer número a validar.
    numero2 (str): El segundo número a validar.
  
  Raises:
    ValueError: Si los números están vacíos, no son números enteros o son menores a 0, o si el primer número es mayor al segundo.
  """
  if not numero1.strip() or not numero2.strip():
    raise ValueError("Los números no pueden estar vacíos.")
  elif not numero1.isdigit() or not numero2.isdigit():
    raise ValueError("Los valores deben ser números enteros.")
  elif int(numero1) < 0 or int(numero2) < 0:
    raise ValueError("Los números no pueden ser menores a 0.")
  elif int(numero1) > int(numero2):
    raise ValueError("El primer número debe ser menor o igual al segundo.")