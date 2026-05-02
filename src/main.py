
# Importaciones necesarias
from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse, PlainTextResponse, FileResponse
from pydantic import BaseModel, Field, validator
from typing import List
from src.routers.movie_router import movie_router

# Instancia principal de la aplicación FastAPI
app = FastAPI()

app.include_router(movie_router)

# Ruta principal de bienvenida
@app.get('/', tags=['Home'])
def home():
    # Devuelve un mensaje de bienvenida en texto plano
    return PlainTextResponse(content='Welcome to the Movie API!')

# Obtener todas las películas
app.include_router(prefix='/movies', router=movie_router)

