from fastapi import Body, FastAPI, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, FileResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List


app = FastAPI()

movies: List[Movie] = []


class Movie(BaseModel):
    id: int
    title: str
    year: int
    category: str


class MovieCreate(BaseModel):
    id: int
    title: str = Field(min_length=5, max_length=15)
    year: int = Field(ge=1900, le=2024)
    category: str = Field(min_length=5, max_length=20)

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 4,
                "title": "The Matrix",
                "year": 1999,
                "category": "Sci-Fi"
            }
        }
    }

@validator('title')
def validate_title(cls, value):
    if not value.isalnum():
        raise ValueError('Title must be alphanumeric')
    return value

class MovieUpdate(BaseModel):
    title: str
    year: int
    category: str


@app.get('/', tags=['Home'])
def home():
    return PlainTextResponse(content='Welcome to the Movie API!')


@app.get('/movies', tags=['Home'])
def get_movies() -> List[Movie]:
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)


@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie['id'] == id:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={})


@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=5, max_length=20)) -> Movie | dict:
    for movie in movies:
        if movie.category == category:
            return JSONResponse(content=movie.model_dump())
    return JSONResponse(content={})


@app.post('/movies', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie)
    content = [movie.model_dump() for movie in movies]
    return JSONResponse(content=content)
    # return RedirectResponse(url='/movies', status_code=303)


@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.year = movie.year
            item.category = movie.category
            content = [movie.model_dump() for movie in movies]
            return JSONResponse(content=content)


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
            content = [movie.model_dump() for movie in movies]
            return JSONResponse(content=content)

@app.get('/get_file')
def get_file():
    return FileResponse(path='sample.txt', media_type='text/plain', filename='sample.txt')