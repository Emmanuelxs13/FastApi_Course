from fastapi import Body, FastAPI
from fastapi.responses import HTMLResponse

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


@app.get('/', tags=['Home'])
def home():
    return "Hello world"


@app.get('/movies', tags=['Home'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    return {"error": "Movie not found"}


@app.get('/movies/', tags=['Movies'])
def get_movie_by_category(category: str, year: int):
    for movie in movies:
        if movie['category'] == category:
            return movie
        return []


@app.post('/movies', tags=['Movies'])
def create_movie(id: int = Body(), title: str = Body(), year: int = Body(), category: str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "year": year,
        "category": category
    })
