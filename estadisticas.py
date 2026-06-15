def pais_mayor_poblacion(paises):
  """
  Calcula el país con mayor población.
  
  Args:
    paises (list): Lista de diccionarios con información de países.
  """
  # Mostrar título de la estadística
  print("\nMayor población:")

  # Inicializar la variable con el primer país
  mayor = paises[0]

  # Recorrer la lista de países
  for pais in paises:
    # Comparar si la población del país actual es mayor que la del país guardado hasta el momento
    if pais["poblacion"] > mayor["poblacion"]:
      # Si el país actual tiene más población, actualizar la variable
      mayor = pais

  # Mostrar el resultado
  print(f"El país con mayor población es {mayor['nombre']} con {mayor['poblacion']} habitantes.")

def pais_menor_poblacion(paises):
  """
  Calcula el país con menor población.
  
  Args:
    paises (list): Lista de diccionarios con información de países.
  """
  # Mostrar título de la estadística
  print("\nMenor población:")

  # Inicializar la variable con el primer país
  menor = paises[0]

  # Recorrer la lista de países
  for pais in paises:
    # Comparar si la población del país actual es menor que la del país guardado hasta el momento
    if pais["poblacion"] < menor["poblacion"]:
      # Si el país actual tiene menos población, actualizar la variable
      menor = pais

  # Mostrar el resultado
  print(f"El país con menor población es {menor['nombre']} con {menor['poblacion']} habitantes.")

def promedio_poblacion(paises):
  """
  Calcula el promedio de población de todos los países.
  
  Args:
    paises (list): Lista de diccionarios con información de países.
  """
  # Mostrar título de la estadística
  print("\nPromedio población:")

  # Inicializar el acumulador
  acumulador = 0
  
  # Recorrer la lista de países
  for pais in paises:
    # Sumar la población del país actual al acumulador
    acumulador += pais["poblacion"]

  # Calcular el promedio
  promedio = round((acumulador / len(paises)), 2)

  # Mostrar el resultado
  print(f"El promedio de población por país es de {promedio} habitantes.")

def promedio_superficie(paises):
  """
  Calcula el promedio de superficie de todos los países.
  
  Args:
    paises (list): Lista de diccionarios con información de países.
  """
  # Mostrar título de la estadística
  print("\nPromedio superficie:")

  # Inicializar el acumulador
  acumulador = 0

  # Recorrer la lista de países
  for pais in paises:
    # Sumar la superficie del país actual al acumulador
    acumulador += pais["superficie"]

  # Calcular el promedio
  promedio = round((acumulador / len(paises)), 2)

  # Mostrar el resultado
  print(f"El promedio de superficie es de {promedio} km2.")

def paises_por_continente(paises):
  """
  Cuenta la cantidad de países por continente.
  
  Args:
    paises (list): Lista de diccionarios con información de países.
  """
  # Mostrar título de la estadística
  print("\nCantidad de países por continente:")

  # Inicializar el diccionario
  continentes = {}

  # Recorrer la lista de países
  for pais in paises:
    # Obtener el continente del país
    continente = pais["continente"]

    # Si el continente no está en el diccionario, inicializarlo con 0
    if continente not in continentes:
      continentes[continente] = 0

    # Incrementar el contador del continente
    continentes[continente] += 1

  # Recorrer el diccionario y mostrar los resultados
  for continente, cantidad in continentes.items():
    print(f"- {continente}: {cantidad} país(es)")

def mostrar_estadisticas(paises):
  """
  Muestra las estadísticas de la lista de países.
  
  Args:
    paises (list): Lista de diccionarios con información de países.
  """
  # Mostrar título de las estadísticas
  print("\n--- ESTADÍSTICAS ---")

  # Verificar si la lista está vacía
  if not paises:
    # Si la lista está vacía, mostrar un mensaje y retornar
    print("No hay países registrados.")
    return

  # Si la lista no está vacía, mostrar las estadísticas
  else:
    # Mostrar país con mayor población
    pais_mayor_poblacion(paises)

    # Mostrar país con menor población
    pais_menor_poblacion(paises)

    # Calcular y mostrar el promedio de población
    promedio_poblacion(paises)

    # Calcular y mostrar el promedio de superficie
    promedio_superficie(paises)

    # Contar y mostrar la cantidad de países por continente
    paises_por_continente(paises)