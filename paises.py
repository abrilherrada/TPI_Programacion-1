from validaciones import validar_nombre, validar_poblacion, validar_superficie, validar_continente, validar_opcion_menu, validar_rango

def mostrar_pais(pais):
  """
  Muestra la información de un país en un formato legible.
  
  Args:
    pais (dict): Diccionario con la información del país.
  """
  print(
    f"- Nombre: {pais['nombre']} | "
    f"Población: {pais['poblacion']} | "
    f"Superficie: {pais['superficie']} | "
    f"Continente: {pais['continente']}"
  )

def agregar_pais(paises):
  """
  Agrega un nuevo país a la lista de países.
  
  Args:
    paises (list): Lista de diccionarios con la información de los países.
  """
  # Título para dar contexto al usuario
  print("\n--- AGREGAR PAÍS ---")

  # Bucle para solicitar dato hasta que sea válido
  while True:
    # Intentar obtener nombre válido
    try:
      # Solicitar nombre, normalizarlo y validarlo
      nombre = input("\nIngrese el nombre del país: ").strip().title()
      validar_nombre(nombre)

      # Si el nombre es válido, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Recorrer la lista de países
  for pais in paises:
    # Comparar nombres ignorando mayúsculas/minúsculas
    if pais["nombre"].lower() == nombre.lower():
      # Si el país ya existe, mostrar mensaje
      print("\nEl país ya existe.")
      # Retornar False para indicar que no se realizó ningún cambio
      return False

  # Bucle para solicitar datos del país hasta que sean válidos
  while True:
    # Intentar obtener datos válidos
    try:
      # Solicitar población, validarla y convertirla a entero
      poblacion = input("\nIngrese la población del país: ")
      validar_poblacion(poblacion)
      poblacion = int(poblacion)

      # Si la población es válida, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Bucle para solicitar datos del país hasta que sean válidos
  while True:
    # Intentar obtener datos válidos
    try:
      # Solicitar superficie, validarla y convertirla a entero
      superficie = input("\nIngrese la superficie del país: ")
      validar_superficie(superficie)
      superficie = int(superficie)

      # Si la superficie es válida, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Bucle para solicitar datos del país hasta que sean válidos
  while True:
    # Intentar obtener datos válidos
    try:
      # Solicitar continente, normalizarlo y validarlo
      continente = input("\nIngrese el continente del país: ").strip().title()
      validar_continente(continente)

      # Si el continente es válido, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Crear diccionario con los datos del nuevo país
  nuevo_pais = {
    "nombre": nombre,
    "poblacion": poblacion,
    "superficie": superficie,
    "continente": continente
  }

  # Agregar el nuevo país a la lista
  paises.append(nuevo_pais)

  # Mostrar mensaje de éxito y los datos del país agregado
  print("\nPaís agregado correctamente:")
  mostrar_pais(nuevo_pais)

  # Retornar True para indicar que se realizó un cambio
  return True

def actualizar_pais(paises):
  """
  Permite actualizar los datos de un país existente.
  
  Args:
    paises (list): Lista de diccionarios con los países.
  """
  # Título para dar contexto al usuario
  print("\n--- ACTUALIZAR PAÍS ---")

  # Verificar si hay países registrados
  if not paises:
    # Si no hay países, mostrar mensaje y retornar
    print("\nNo hay países registrados.")
    return

  # Bucle para solicitar el nombre del país hasta que sea válido
  while True:
    # Intentar obtener el nombre del país
    try:
      # Solicitar el nombre del país, normalizarlo y validarlo
      nombre = input("\nIngrese el nombre del país que desea actualizar: ").strip().title()
      validar_nombre(nombre)

      # Si el nombre es válido, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Variable para almacenar el país buscado
  pais = None

  # Buscar el país en la lista
  for item in paises:
    # Comparar nombres ignorando mayúsculas/minúsculas
    if item["nombre"].lower() == nombre.lower():
      # Si se encuentra el país, asignarlo a la variable y salir del bucle
      pais = item
      break

  # Si el país no se encontró, mostrar mensaje y retornar
  if pais is None:
    print("\nNo se encontró el país.")

    # Retornar False para indicar que no se realizó ningún cambio
    return False

  # Bucle para solicitar la opción de actualización hasta que sea válida
  while True:
    # Intentar obtener la opción de actualización
    try:
      # Solicitar la opción de actualización y validarla
      opcion = input("""
        ¿Qué valor desea actualizar?
          1. Población
          2. Superficie
          3. Población y superficie
          
        Opción seleccionada: """)
      validar_opcion_menu(opcion, (1, 3))

      # Si la opción es válida, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Procesar la opción seleccionada
  match opcion:
    # Actualizar población
    case "1":
      # Bucle para solicitar la población hasta que sea válida
      while True:
        # Intentar obtener la población
        try:
          # Solicitar la población, validarla y normalizarla
          poblacion = input("\nIngrese la nueva población del país: ")
          validar_poblacion(poblacion)
          poblacion = int(poblacion)

          # Actualizar la población del país
          pais["poblacion"] = poblacion

          # Mostrar mensaje de éxito y salir del bucle
          print("\nPoblación actualizada correctamente:")
          break

        # Si hay un error de validación, mostrarlo y continuar el bucle
        except ValueError as e:
          print(f"Error de entrada: {e}")
          continue

    # Actualizar superficie
    case "2":
      # Bucle para solicitar la superficie hasta que sea válida
      while True:
        # Intentar obtener la superficie
        try:
          # Solicitar la superficie, validarla y normalizarla
          superficie = input("\nIngrese la nueva superficie del país: ")
          validar_superficie(superficie)
          superficie = int(superficie)

          # Actualizar la superficie del país
          pais["superficie"] = superficie

          # Mostrar mensaje de éxito y salir del bucle
          print("\nSuperficie actualizada correctamente:")
          break

        # Si hay un error de validación, mostrarlo y continuar el bucle
        except ValueError as e:
          print(f"Error de entrada: {e}")
          continue

    # Actualizar población y superficie
    case "3":
      # Bucle para solicitar la población hasta que sea válida
      while True:
        # Intentar obtener la población
        try:
          # Solicitar la población, validarla y normalizarla
          poblacion = input("\nIngrese la nueva población del país: ")
          validar_poblacion(poblacion)
          poblacion = int(poblacion)

          # Si la población es válida, salir del bucle
          break

        # Si hay un error de validación, mostrarlo y continuar el bucle
        except ValueError as e:
          print(f"Error de entrada: {e}")
          continue

      # Bucle para solicitar la superficie hasta que sea válida
      while True:
        # Intentar obtener la superficie
        try:
          # Solicitar la superficie, validarla y normalizarla
          superficie = input("\nIngrese la nueva superficie del país: ")
          validar_superficie(superficie)
          superficie = int(superficie)

          # Si la superficie es válida, salir del bucle
          break

        # Si hay un error de validación, mostrarlo y continuar el bucle
        except ValueError as e:
          print(f"Error de entrada: {e}")
          continue

      # Actualizar la población y superficie del país
      pais["poblacion"] = poblacion
      pais["superficie"] = superficie

      # Mostrar mensaje de éxito
      print("\nPoblación y superficie actualizadas correctamente:")

  # Mostrar país actualizado
  mostrar_pais(pais)

  # Retornar True para indicar que se realizó un cambio
  return True

def buscar_pais(paises):
  """
  Busca un país por nombre.
  
  Args:
    paises (list): Lista de países.
  """
  # Título para dar contexto al usuario
  print("\n--- BUSCAR PAÍS ---")

  # Verificar si hay países registrados
  if not paises:
    # Si no hay países, mostrar mensaje y retornar
    print("\nNo hay países registrados.")
    return

  # Bucle para solicitar el nombre del país hasta que sea válido
  while True:
    # Intentar obtener el nombre del país
    try:
      # Solicitar el nombre del país, normalizarlo y validarlo
      nombre = input("\nIngrese el nombre del país que desea buscar: ").strip().title()
      validar_nombre(nombre)

      # Si el nombre es válido, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Bandera para indicar si se encontraron resultados
  resultados = False

  # Mostrar título de los resultados
  print("\nResultados:")

  # Recorrer la lista de países
  for pais in paises:
    # Para cada país, verificar si el nombre ingresado es parte del nombre del país
    if nombre.lower() in pais["nombre"].lower():
      # Si se encuentra una coincidencia, marcar que se encontraron resultados y mostrar el país
      resultados = True
      mostrar_pais(pais)

  # Si no se encontraron coincidencias, mostrar un mensaje
  if not resultados:
    print("No se encontraron coincidencias.")

def filtrar_paises(paises):
  """
  Filtra la lista de países según una opción seleccionada.
  
  Args:
    paises (list): Lista de países.
  """
  # Título para dar contexto al usuario
  print("\n--- FILTRAR PAÍSES ---")

  # Verificar si hay países registrados
  if not paises:
    # Si no hay países, mostrar mensaje y retornar
    print("\nNo hay países registrados.")
    return

  # Bucle para solicitar la opción de filtrado hasta que sea válida
  while True:
    # Intentar obtener la opción de filtrado
    try:
      # Solicitar la opción de filtrado y validarla
      opcion = input("""
        ¿Qué valor desea filtrar?
          1. Continente
          2. Rango de población
          3. Rango de superficie
        Ingrese una opción: """)
      validar_opcion_menu(opcion, (1, 3))

      # Si la opción es válida, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Procesar la opción seleccionada
  match opcion:
    # Filtrar por continente
    case "1":
      # Bucle para solicitar el continente hasta que sea válido
      while True:
        # Intentar obtener el continente
        try:
          # Solicitar el continente, normalizarlo y validarlo
          continente = input("\nIngrese el continente: ").strip().title()
          validar_continente(continente)

          # Si el continente es válido, salir del bucle
          break

        # Si hay un error de validación, mostrarlo y continuar el bucle
        except ValueError as e:
          print(f"Error de entrada: {e}")
          continue

      # Bandera para indicar si se encontraron resultados
      resultados = False

      # Mostrar el título de los resultados
      print("\nResultados:")

      # Recorrer la lista de países
      for pais in paises:
        # Verificar si el continente del país coincide con el continente buscado (ignorando mayúsculas/minúsculas)
        if pais["continente"].lower() == continente.lower():
          # Marcar que se encontró al menos un resultado
          resultados = True
          # Mostrar los datos del país
          mostrar_pais(pais)

      # Si no se encontraron resultados, mostrar un mensaje
      if not resultados:
        print("No se encontraron países en ese continente.")

    # Filtrar por rango de población
    case "2":
      # Bucle para solicitar el rango de población hasta que sea válido
      while True:
        # Intentar obtener el rango de población
        try:
          # Solicitar los valores mínimos y máximos del rango de población, validarlos y normalizarlos
          poblacion_min = input("\nIngrese el límite inferior de población: ")
          poblacion_max = input("Ingrese el límite superior de población: ")
          validar_rango(poblacion_min, poblacion_max)
          poblacion_min = int(poblacion_min)
          poblacion_max = int(poblacion_max)

          # Si el rango es válido, salir del bucle
          break

        # Si hay un error de validación, mostrarlo y continuar el bucle
        except ValueError as e:
          print(f"Error de entrada: {e}")
          continue

      # Bandera para indicar si se encontraron resultados
      resultados = False

      # Mostrar el título de los resultados
      print("\nResultados:")

      # Recorrer la lista de países
      for pais in paises:
        # Verificar si la población del país está dentro del rango especificado
        if pais["poblacion"] >= poblacion_min and pais["poblacion"] <= poblacion_max:
          # Marcar que se encontró al menos un resultado
          resultados = True
          # Mostrar los datos del país
          mostrar_pais(pais)

      # Si no se encontraron resultados, mostrar un mensaje
      if not resultados:
        print("No se encontraron países en ese rango de población.")

    # Filtrar por rango de superficie
    case "3":
      # Bucle para solicitar el rango de superficie hasta que sea válido
      while True:
        # Intentar obtener el rango de superficie
        try:
          # Solicitar los valores mínimos y máximos del rango de superficie, validarlos y normalizarlos
          superficie_min = input("\nIngrese el límite inferior de superficie: ")
          superficie_max = input("Ingrese el límite superior de superficie: ")
          validar_rango(superficie_min, superficie_max)
          superficie_min = int(superficie_min)
          superficie_max = int(superficie_max)

          # Si el rango es válido, salir del bucle
          break

        # Si hay un error de validación, mostrarlo y continuar el bucle
        except ValueError as e:
          print(f"Error de entrada: {e}")
          continue

      # Bandera para indicar si se encontraron resultados
      resultados = False

      # Mostrar el título de los resultados
      print("\nResultados:")

      # Recorrer la lista de países
      for pais in paises:
        # Verificar si la superficie del país está dentro del rango especificado
        if pais["superficie"] >= superficie_min and pais["superficie"] <= superficie_max:
          # Marcar que se encontró al menos un resultado
          resultados = True
          # Mostrar los datos del país
          mostrar_pais(pais)

      # Si no se encontraron resultados, mostrar un mensaje
      if not resultados:
        print("No se encontraron países en ese rango de superficie.")

def ordenar_paises(paises):
  """
  Ordena la lista de países según el criterio y orden seleccionados por el usuario.
  
  Args:
    paises (list): Lista de diccionarios con los datos de los países.
  """
  # Título para dar contexto al usuario
  print("\n--- ORDENAR PAÍSES ---")

  # Verificar si hay países registrados
  if not paises:
    # Si no hay países, mostrar mensaje y retornar
    print("\nNo hay países registrados.")
    return

  # Bucle para solicitar la opción de ordenamiento hasta que sea válida
  while True:
    # Intentar obtener la opción de ordenamiento
    try:
      # Solicitar la opción de ordenamiento y validarla
      opcion = input("""
        ¿Por cuál valor desea ordenar?
          1. Nombre
          2. Población
          3. Superficie
        Ingrese una opción: """)
      validar_opcion_menu(opcion, (1, 3))

      # Si la opción es válida, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Bucle para solicitar el orden hasta que sea válido
  while True:
    # Intentar obtener el orden
    try:
      # Solicitar el orden y validarlo
      orden = input("""
        ¿En qué orden desea ordenar?
          1. Ascendente
          2. Descendente
        Ingrese una opción: """)
      validar_opcion_menu(orden, (1, 2))

      # Si el orden es válido, salir del bucle
      break

    # Si hay un error de validación, mostrarlo y continuar el bucle
    except ValueError as e:
      print(f"Error de entrada: {e}")
      continue

  # Crear una copia de la lista de países para no modificar la original
  paises_ordenados = paises.copy()

  # Determinar el criterio de ordenamiento
  if opcion == "1":
    criterio = "nombre"
  elif opcion == "2":
    criterio = "poblacion"
  elif opcion == "3":
    criterio = "superficie"

  # Determinar si el orden es ascendente o descendente
  ascendente = True if orden == "1" else False

  # Ordenar la lista de países con el algoritmo bubble sort
  # Recorrer la lista de países
  for i in range(len(paises_ordenados) - 1):
    # Recorrer la lista de países para comparar elementos y ordenar
    for j in range(len(paises_ordenados) - 1 - i):

      # Si el orden es ascendente, ordena de menor a mayor
      if ascendente:
        if paises_ordenados[j][criterio] > paises_ordenados[j + 1][criterio]:
          paises_ordenados[j], paises_ordenados[j + 1] = paises_ordenados[j + 1], paises_ordenados[j]

      # Si el orden es descendente, ordena de mayor a menor
      else:
        if paises_ordenados[j][criterio] < paises_ordenados[j + 1][criterio]:
          paises_ordenados[j], paises_ordenados[j + 1] = paises_ordenados[j + 1], paises_ordenados[j]

  # Mostrar título de la lista ordenada
  print("\nPaíses ordenados:")
  # Mostrar cada país de la lista ordenada
  for pais in paises_ordenados:
    mostrar_pais(pais)