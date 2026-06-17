# Trabajo Práctico Integrador de Programación I: Gestión de Países

## Información institucional

**Universidad:** Universidad Tecnológica Nacional

**Carrera:** Tecnicatura Universitaria en Programación

**Materia:** Programación I

**Comisión:** 13 y 23

**Tutores:** Sofía Fernández, Juan Sarmiento

**Docentes:** Ariel Enferrel, Martín A. García, Cinthia Rigoni

**Año:** 2026

---

## Integrantes

- Abril Herrada (comisión 13)
- Erik Riberi (comisión 23)

---

## Descripción del proyecto

Este proyecto fue desarrollado como Trabajo Práctico Integrador de la materia Programación I.

Consiste en una aplicación de consola desarrollada en Python que permite gestionar información sobre distintos países mediante operaciones de carga, actualización, consulta, filtrado, ordenamiento y análisis de datos.

La aplicación utiliza estructuras de datos dinámicas, funciones, modularización y archivos CSV para implementar persistencia de la información entre distintas ejecuciones del programa.

---

## Descripción del programa

El sistema permite:

- Agregar nuevos países con su nombre, continente, población y superficie
- Actualizar los datos de población y superficie de un país existente
- Buscar un país por nombre mediante coincidencia parcial o exacta
- Filtrar países por:
  - continente
  - rango de población
  - rango de superficie
- Ordenar países de forma ascendente o descendente por:
  - nombre
  - población
  - superficie
- Obtener estadísticas básicas:
  - país con mayor población
  - país con menor población
  - promedio de población
  - promedio de superficie
  - cantidad de países por continente
- Almacenar la información de forma persistente mediante archivos CSV

---

## Estructura del proyecto

```text
TPI_Programacion-1/
│
├── main.py
├── estadisticas.py
├── paises.csv
├── paises.py
├── persistencia.py
├── validaciones.py
└── README.md
```

### Descripción de los módulos

**main.py**

- Control principal del programa
- Menú de usuario
- Integración de todos los módulos

**paises.py**

- Gestión de países
- Altas, actualizaciones, búsquedas, filtros y ordenamientos

**persistencia.py**

- Lectura y escritura de datos en el archivo CSV
- Manejo de errores relacionados con archivos

**validaciones.py**

- Validación de datos ingresados por el usuario
- Control de formatos y rangos

**estadisticas.py**

- Cálculo de indicadores estadísticos
- Generación de reportes básicos

**paises.csv**

- Almacenamiento persistente de la información

---

## Librerías utilizadas

El proyecto utiliza únicamente módulos estándar de Python.

### csv

Se utiliza el módulo `csv`, incluido en la biblioteca estándar de Python, para la lectura y escritura del archivo CSV que se utiliza como mecanismo de persistencia de datos.

No se utilizaron librerías externas de terceros.

---

## Instrucciones de uso

### Requisitos

- Python 3.10 o superior

### Ejecución

Según la configuración del sistema operativo, ejecutar el siguiente comando desde la carpeta raíz del proyecto:

```bash
python main.py
```

o

```bash
python3 main.py
```

---

## Ejemplos de uso

### Agregar un país

**Entrada**

```text
Nombre: Argentina
Población: 46000000
Superficie: 2780400
Continente: América
```

**Salida**

```text
País agregado correctamente:

- Nombre: Argentina | Población: 46000000 | Superficie: 2780400 | Continente: América
```

---

### Buscar un país

**Entrada**

```text
Argentina
```

**Salida**

```text
Resultados:

- Nombre: Argentina | Población: 46000000 | Superficie: 2780400 | Continente: América
```

---

### Mostrar estadísticas

**Salida**

```text
--- ESTADÍSTICAS ---

Mayor población:
El país con mayor población es China con 1412000000 habitantes.

Menor población:
El país con menor población es Australia con 27000000 habitantes.

Promedio población:
El promedio de población por país es de 215100000.0 habitantes.

Promedio superficie:
El promedio de superficie es de 4222896.9 km2.

Cantidad de países por continente:
- América: 3 país(es)
- Europa: 2 país(es)
- Asia: 2 país(es)
- África: 2 país(es)
- Oceanía: 1 país(es)
```

---

## Participación de los integrantes

### Abril Herrada

- Diseño general de la solución
- Implementación del módulo de persistencia
- Implementación del módulo de gestión de países
- Pruebas del sistema
- Documentación

### Erik Riberi

- Diseño general de la solución
- Implementación del módulo de validaciones
- Implementación del módulo de estadísticas
- Integración del módulo principal
- Documentación

---

## Informe del proyecto

Enlace al informe:

[Agregar enlace]

---

## Video demostrativo

Enlace al video de presentación:

[Video de presentación y demostración](https://drive.google.com/file/d/1bvqcTnOay1LUIynMwTCK1eHwzj89du0J/view)

---

## Informe

Documentación del proyecto:

[Informe del proyecto](https://drive.google.com/file/d/1YpHqwIa9wc2PBrLWlT7hglQUku-zo8MF/view?usp=sharing)

---

## Repositorio del proyecto

Repositorio GitHub:

[Repositorio de GitHub](https://github.com/abrilherrada/TPI_Programacion-1)
