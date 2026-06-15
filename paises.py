def mostrar_pais(pais):
    print(
        f"- Nombre: {pais['nombre']} | "
        f"Población: {pais['poblacion']} | "
        f"Superficie: {pais['superficie']} | "
        f"Continente: {pais['continente']}"
    )

def agregar_pais(paises):
  while True:
    try:
      nombre = input("Ingrese el nombre del país: ").strip().title()
      # VALIDAR

      poblacion = input("Ingrese la población del país: ")
      # VALIDAR
      poblacion = int(poblacion)

      superficie = input("Ingrese la superficie del país: ")
      # VALIDAR
      superficie = float(superficie)

      continente = input("Ingrese el continente del país: ").strip().title()
      # VALIDAR
      break

    except ValueError as e:
      print(f"Error: {e}")
      continue

  existe = False

  for pais in paises:
    if pais["nombre"].lower() == nombre.lower():
      existe = True
      break

  if existe:
    print("El país ya existe.")
    return None
  else:
    paises.append({
      "nombre": nombre,
      "poblacion": poblacion,
      "superficie": superficie,
      "continente": continente
    })
    print("País agregado correctamente:")
    mostrar_pais({
      "nombre": nombre,
      "poblacion": poblacion,
      "superficie": superficie,
      "continente": continente
    })

def actualizar_pais(paises):
  while True:
    try:
      nombre = input("Ingrese el nombre del país que desea actualizar: ").strip().title()
      # VALIDAR
      break

    except ValueError as e:
      print(f"Error: {e}")
      continue

  pais = None

  for item in paises:
    if item["nombre"].lower() == nombre.lower():
      pais = item
      break

  if pais is None:
    print("No se encontró el país.")
    return None

  while True:
    try:
      opcion = input("""
        ¿Qué valor desea actualizar?
          1. Población
          2. Superficie
          3. Población y superficie
          
        Opción seleccionada: """)
      # VALIDAR
      break

    except ValueError as e:
      print(f"Error: {e}")
      continue

  match opcion:
    case "1":
      while True:
        try:
          poblacion = input("Ingrese la nueva población del país: ")
          # VALIDAR
          poblacion = int(poblacion)
          pais["poblacion"] = poblacion
          break

        except ValueError as e:
          print(f"Error: {e}")
          continue

    case "2":
      while True:
        try:
          superficie = input("Ingrese la nueva superficie del país: ")
          # VALIDAR
          superficie = float(superficie)
          pais["superficie"] = superficie
          break

        except ValueError as e:
          print(f"Error: {e}")
          continue

    case "3":
      while True:
        try:
          poblacion = input("Ingrese la nueva población del país: ")
          # VALIDAR
          poblacion = int(poblacion)

          superficie = input("Ingrese la nueva superficie del país: ")
          # VALIDAR
          superficie = float(superficie)

          pais["poblacion"] = poblacion
          pais["superficie"] = superficie
          break

        except ValueError as e:
          print(f"Error: {e}")
          continue

  print("País actualizado correctamente:")
  mostrar_pais(pais)

def buscar_pais(paises):
  while True:
    try:
      nombre = input("Ingrese el nombre del país que desea buscar: ").strip().title()
      # VALIDAR
      break

    except ValueError as e:
      print(f"Error: {e}")
      continue

  resultados = False

  print("Resultados:")

  for pais in paises:
    if nombre.lower() in pais["nombre"].lower():
      resultados = True
      mostrar_pais(pais)

  if not resultados:
    print("No se encontró el país.")

def filtrar_paises(paises):
  while True:
    try:
      opcion = input("""
        ¿Qué valor desea filtrar?
          1. Continente
          2. Rango de población
          3. Rango de superficie
        Ingrese una opción: """)
      # VALIDAR
      break

    except ValueError as e:
      print(f"Error: {e}")
      continue

  match opcion:
    case "1":
      while True:
        try:
          continente = input("Ingrese el continente: ").strip().title()
          # VALIDAR
          break

        except ValueError as e:
          print(f"Error: {e}")
          continue

      resultados = False
      print("Resultados:")

      for pais in paises:
        if pais["continente"].lower() == continente.lower():
          resultados = True
          mostrar_pais(pais)

      if not resultados:
        print("No se encontraron países en ese continente.")

    case "2":
      while True:
        try:
          poblacion_min = input("Ingrese el límite inferior de población: ")
          poblacion_max = input("Ingrese el límite superior de población: ")
          # VALIDAR
          poblacion_min = int(poblacion_min)
          poblacion_max = int(poblacion_max)
          break

        except ValueError as e:
          print(f"Error: {e}")
          continue

      resultados = False
      print("Resultados:")

      for pais in paises:
        if pais["poblacion"] >= poblacion_min and pais["poblacion"] <= poblacion_max:
          resultados = True
          mostrar_pais(pais)

      if not resultados:
        print("No se encontraron países en ese rango de población.")

    case "3":
      while True:
        try:
          superficie_min = input("Ingrese el límite inferior de superficie: ")
          superficie_max = input("Ingrese el límite superior de superficie: ")
          # VALIDAR
          superficie_min = float(superficie_min)
          superficie_max = float(superficie_max)
          break

        except ValueError as e:
          print(f"Error: {e}")
          continue

      resultados = False
      print("Resultados:")

      for pais in paises:
        if pais["superficie"] >= superficie_min and pais["superficie"] <= superficie_max:
          resultados = True
          mostrar_pais(pais)

      if not resultados:
        print("No se encontraron países en ese rango de superficie.")

def ordenar_paises(paises):
  while True:
    try:
      opcion = input("""
        ¿Por cuál valor desea ordenar?
          1. Nombre
          2. Población
          3. Superficie
        Ingrese una opción: """)
      # VALIDAR
      break

    except ValueError as e:
      print(f"Error: {e}")
      continue

  while True:
    try:
      orden = input("""
        ¿En qué orden desea ordenar?
          1. Ascendente
          2. Descendente
        Ingrese una opción: """)
      # VALIDAR
      break

    except ValueError as e:
      print(f"Error: {e}")
      continue

  if opcion == "1":
    criterio = "nombre"
  elif opcion == "2":
    criterio = "poblacion"
  elif opcion == "3":
    criterio = "superficie"

  ascendente = True if orden == "1" else False

  for i in range(len(paises)):
    for j in range(len(paises) - 1 - i):

      if ascendente:
        if paises[j][criterio] > paises[j + 1][criterio]:
          paises[j], paises[j + 1] = paises[j + 1], paises[j]
      else:
        if paises[j][criterio] < paises[j + 1][criterio]:
          paises[j], paises[j + 1] = paises[j + 1], paises[j]

  print("Paises ordenados:")
  for pais in paises:
    mostrar_pais(pais)