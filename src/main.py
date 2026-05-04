
# Importaciones necesarias
from fastapi import FastAPI 
from fastapi.responses import PlainTextResponse
from fastapi.requests import Request
from fastapi.responses import JSONResponse, Response
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import http_error_handler


# Instancia principal de la aplicación FastAPI
app = FastAPI()

# app.add_middleware(http_error_handler)
@app.middleware('http')
async def http_error_handler(request, call_next) -> Response | JSONResponse:
    print('Middleware is running....')
    return await call_next(request)
    
# app.include_router(movie_router)

# Ruta principal de bienvenida
@app.get('/', tags=['Home'])
def home():
    # Devuelve un mensaje de bienvenida en texto plano
    return PlainTextResponse(content='Welcome to the Movie API!')

# Obtener todas las películas
app.include_router(prefix='/movies', router=movie_router)

