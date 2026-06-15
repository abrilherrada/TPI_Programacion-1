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