# FastAPI: Guía Completa

FastAPI es un framework moderno y rápido para construir APIs con Python 3.7+ basado en las anotaciones de tipo estándar de Python. Es ideal para crear servicios web de alto rendimiento y fácil mantenimiento.

## ¿Por qué usar FastAPI?

- **Rápido**: Alto rendimiento, comparable a NodeJS y Go.
- **Fácil de usar**: Sintaxis simple y clara.
- **Validación automática**: Usa Pydantic para validar datos.
- **Documentación automática**: Swagger UI y ReDoc generados automáticamente.

## Instalación

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

## Estructura Básica de un Proyecto

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## Ejecutar el Servidor

```bash
uvicorn main:app --reload
```

- `main`: nombre del archivo (sin `.py`)
- `app`: instancia de FastAPI
- `--reload`: recarga automática al guardar cambios

## Rutas y Métodos

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

- Métodos: `@app.get`, `@app.post`, `@app.put`, `@app.delete`, etc.

## Parámetros de Consulta y Path

- **Path**: `/items/{item_id}`
- **Query**: `/items/3?q=algo`

## Validación de Datos con Pydantic

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return item
```

## Documentación Automática

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Comandos Útiles

- Instalar dependencias: `pip install fastapi uvicorn`
- Ejecutar servidor: `uvicorn main:app --reload`
- Ver documentación: `/docs` o `/redoc`

## Recursos

- [Documentación oficial](https://fastapi.tiangolo.com/es/)
- [Ejemplos de FastAPI](https://github.com/tiangolo/fastapi/tree/master/examples)

---


