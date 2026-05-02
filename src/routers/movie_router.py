

from ast import List

from fastapi import Path, Query, APIRouter

from fastapi.responses import JSONResponse

from src.models.movie_model import Movie, MovieCreate, MovieUpdate

# Lista global para almacenar las películas (como base de datos en memoria)
movies: List[Movie] = []

movie_router = APIRouter()

@movie_router.get('/', tags=['Movies'])
def get_movies() -> List[Movie]:
    # Devuelve la lista de películas en formato JSON
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)

# Obtener una película por ID


@movie_router.get('/{id}', tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    # Busca la película por su ID
    for movie in movies:
        if movie.id == id:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={})


# Obtener una película por categoría
@movie_router.get('/by_category', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:
    # Busca la primera película que coincida con la categoría
    for movie in movies:
        if movie.category == category:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={})


# Crear una nueva película
@movie_router.post('/', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    # Convierte MovieCreate a Movie antes de guardar
    new_movie = Movie(**movie.model_dump())
    movies.append(new_movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)
    # return RedirectResponse(url='/movies', status_code=303)


# Actualizar una película existente
@movie_router.put('/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    # Busca la película por ID y actualiza sus datos
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.year = movie.year
            item.category = movie.category
            content = [movie.model_dump() for movie in movies]
            return JSONResponse(content=content)


# Eliminar una película por ID
@movie_router.delete('/{id}', tags=['Movies'])
def delete_movie(id: int) -> List[Movie]:
    # Elimina la película que coincida con el ID
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
            content = [movie.model_dump() for movie in movies]
            return JSONResponse(content=content)


