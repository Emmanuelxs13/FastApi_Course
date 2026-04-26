from fastapi import Body, FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional,List

movies = [

    {
        "id": 1,
        "title": "Inception",
        "year": 2010,
        "category": "Sci-Fi"
    },
    {
        "id": 2,
        "title": "The Godfather",
        "year": 1972,
        "category": "Crime"
    },
    {
        "id": 3,
        "title": "Spirited Away",
        "year": 2001,
        "category": "Animation"
    }

]

app = FastAPI()

class Movie(BaseModel):
    id: int
    title: str
    year: int
    category: str

class MovieUpdate(BaseModel):
    title: str
    year:int
    category: str

@app.get('/', tags=['Home'])
def home():
    return "Hello world"


@app.get('/movies', tags=['Home'])
def get_movies() -> List[Movie]:
    return movies


@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int) -> Movie:
    for movie in movies:
        if movie['category'] == category:
            return movie
        return []


@app.post('/movies', tags=['Movies'])
def create_movie(movie: Movie) -> List[Movie]:
    movies.append(movie.model_dump())
    return movies



@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['year'] = movie.year
            item['category'] = movie.category
            return movies


@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return movies
 