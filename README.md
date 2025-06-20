# API - Get por PATH y QUERY

Este proyecto implementa una API usando **FastAPI** y **Pandas**, cargando una base de datos de alumnos desde un archivo `BDAlumnos.csv`.

## Estructura del Proyecto

```
Get_por_PATH_y_QUERY/
├── main.py
├── BDAlumnos.csv
└── README.md
```

---

## Cómo ejecutar la API?

1. Instala las dependencias necesarias:

```bash
pip install fastapi uvicorn pandas
```

2. Ejecuta el servidor de desarrollo:

```bash
uvicorn Act2:app --reload
```

3. Abre tu navegador y visita:

```
http://127.0.0.1:8000/docs
```

Allí encontrarás la documentación interactiva generada automáticamente por FastAPI.

---

##  Endpoints implementados

###  GET por **PATH**

Busca un alumno por un valor exacto o parcial en uno de los siguientes campos:

| Ruta | Descripción |
|------|-------------|
| `/alumno/matricula/{matricula}` | Buscar por matrícula |
| `/alumno/nombre/{nombre}` | Buscar por nombre (parcial) |
| `/alumno/edad/{edad}` | Buscar por edad exacta |
| `/alumno/facultad/{facultad}` | Buscar por facultad |
| `/alumno/inscripcion/{tipo}` | Buscar por tipo de inscripción |
| `/alumno/grado/{grado}` | Buscar por grado |
| `/alumno/carrera/{carrera}` | Buscar por carrera |
| `/alumno/correo/{correo}` | Buscar por correo (parcial) |
| `/alumno/materia/{materia}` | Buscar por materia |
| `/alumno/genero/{genero}` | Buscar por género |

**Ejemplos:**

```
GET /alumno/nombre/Alejandro
GET /alumno/edad/21
GET /alumno/carrera/Ingeniería
```

---

### GET por **QUERY**

Permite realizar búsquedas combinadas con filtros opcionales.

| Ruta | Parámetros disponibles |
|------|------------------------|
| `/buscar` | nombre, carrera, edad, genero, facultad |
| `/buscar1` | nombre, edad |
| `/buscar2` | carrera, genero |
| `/buscar3` | correo, facultad |
| `/buscar4` | grado, materia |
| `/buscar5` | inscripcion, genero |
| `/buscar6` | nombre, carrera, genero |
| `/buscar7` | facultad, edad, grado |
| `/buscar8` | correo, nombre |
| `/buscar9` | matricula, carrera |
| `/buscar10` | materia, inscripcion, edad |

**Ejemplos:**

```
GET /buscar?nombre=María&carrera=Informática
GET /buscar2?carrera=Matemáticas&genero=F
GET /buscar10?materia=Álgebra&edad=19
```
