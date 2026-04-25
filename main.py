from fastapi import FastAPI
from fastapi.responses import HTMLResponse

movies = [

    {
        "id": 1,
        "title": "Inception",
        "year": 2010,
        "genre": "Sci-Fi"
    },
    {
        "id": 2,
        "title": "The Godfather",
        "year": 1972,
        "genre": "Crime"
    },
    {
        "id": 3,
        "title": "Spirited Away",
        "year": 2001,
        "genre": "Animation"
    }

]

app = FastAPI()


@app.get('/', tags=['Home'])
def home():
    return "Hello world"


@app.get('/movies', tags=['Home'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['Home'])
def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return {"error": "Movie not found"}
