from fastapi import Body, FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List

movies: List[Movie] = []

app = FastAPI()


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
class MovieUpdate(BaseModel):
    title: str
    year: int
    category: str


@app.get('/', tags=['Home'])
def home():
    return "Hello world"


@app.get('/movies', tags=['Home'])
def get_movies() -> List[Movie]:
    return [movie.model_dump() for movie in movies]


@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return movie.model_dump()
    return []


@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int) -> Movie:
    for movie in movies:
        if movie['category'] == category:
            return movie.model_dump()
        return []


@app.post('/movies', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie)
    return [movie.model_dump() for movie in movies]


@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['year'] = movie.year
            item['category'] = movie.category
            return [movie.model_dump() for movie in movies]


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return [movie.model_dump() for movie in movies]
