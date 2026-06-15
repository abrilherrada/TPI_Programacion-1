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
    ValueError: Si la superficie está vacía, no es un número o es menor o igual a 0.
  """
  if not superficie.strip():
    raise ValueError("La superficie no puede estar vacía.")
  elif not superficie.replace(".", "").isdigit():
    raise ValueError("La superficie debe ser un número.")
  elif float(superficie) <= 0:
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