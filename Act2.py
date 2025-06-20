import pandas as pd
from fastapi import FastAPI, Query


app= FastAPI()
df = pd.read_excel('BDAlumnos.xlsx', engine='openpyxl')


# -------------------------------------------- PATH ----------------------------------------------------------------
@app.get("/alumno/nombre/{nombre}")
async def get_by_nombre(nombre: str):
    result = df[df["NOMBRE"].str.contains(nombre, case=False)]
    return result.to_dict(orient='records')

@app.get("/alumno/edad/{edad}")
async def get_by_edad(edad: int):
    result = df[df["EDAD"] == edad]
    return result.to_dict(orient='records')

@app.get("/alumno/facultad/{facultad}")
async def get_by_facultad(facultad: str):
    result = df[df["FACULTAD"].str.contains(facultad, case=False)]
    return result.to_dict(orient='records')

@app.get("/alumno/inscripcion/{tipo}")
async def get_by_inscripcion(tipo: str):
    result = df[df["INSCRIPCION"].str.contains(tipo, case=False)]
    return result.to_dict(orient='records')

@app.get("/alumno/grado/{grado}")
async def get_by_grado(grado: str):
    result = df[df["GRADO"].astype(str) == grado]
    return result.to_dict(orient='records')

@app.get("/alumno/carrera/{carrera}")
async def get_by_carrera(carrera: str):
    result = df[df["CARRERA"].str.contains(carrera, case=False)]
    return result.to_dict(orient='records')

@app.get("/alumno/correo/{correo}")
async def get_by_correo(correo: str):
    result = df[df["CORREO"].str.contains(correo, case=False)]
    return result.to_dict(orient='records')

@app.get("/alumno/materia/{materia}")
async def get_by_materia(materia: str):
    result = df[df["MATERIA"].str.contains(materia, case=False)]
    return result.to_dict(orient='records')

@app.get("/alumno/genero/{genero}")
async def get_by_genero(genero: str):
    result = df[df["GENERO"].str.upper() == genero.upper()]
    return result.to_dict(orient='records')


# ------------------------------------------------------ QUERY -----------------------------------------------------------

@app.get("/buscar")
async def buscar(
    nombre: str = Query(None),
    carrera: str = Query(None),
    edad: int = Query(None),
    genero: str = Query(None),
    facultad: str = Query(None)
):
    filtro = df
    if nombre:
        filtro = filtro[filtro["NOMBRE"].str.contains(nombre, case=False)]
    if carrera:
        filtro = filtro[filtro["CARRERA"].str.contains(carrera, case=False)]
    if edad:
        filtro = filtro[filtro["EDAD"] == edad]
    if genero:
        filtro = filtro[filtro["GENERO"].str.upper() == genero.upper()]
    if facultad:
        filtro = filtro[filtro["FACULTAD"].str.contains(facultad, case=False)]

    return filtro.to_dict(orient='records')


@app.get("/Edad/Nombre/id/")
async def userclass(nombre: str = Query(...)):
    df[df["NOMBRE"].str.contains(nombre, case=False)]
    if not df.empty:
        return df.iloc[0].to_dict()  # Primer registro
    else:
        return {"mensaje": "No se encontraron resultados"}

    
    
@app.get("/buscar1")
async def buscar1(nombre: str = Query(None), edad: int = Query(None)): ...

@app.get("/buscar2")
async def buscar2(carrera: str = Query(None), genero: str = Query(None)): ...

@app.get("/buscar3")
async def buscar3(correo: str = Query(None), facultad: str = Query(None)): ...

@app.get("/buscar4")
async def buscar4(grado: str = Query(None), materia: str = Query(None)): ...

@app.get("/buscar5")
async def buscar5(inscripcion: str = Query(None), genero: str = Query(None)): ...

@app.get("/buscar6")
async def buscar6(nombre: str = Query(None), carrera: str = Query(None), genero: str = Query(None)): ...

@app.get("/buscar7")
async def buscar7(facultad: str = Query(None), edad: int = Query(None), grado: str = Query(None)): ...

@app.get("/buscar8")
async def buscar8(correo: str = Query(None), nombre: str = Query(None)): ...

@app.get("/buscar9")
async def buscar9(matricula: int = Query(None), carrera: str = Query(None)): ...

@app.get("/buscar10")
async def buscar10(materia: str = Query(None), inscripcion: str = Query(None), edad: int = Query(None)): ...

