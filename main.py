from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', tags=['Home'])
def home():
    return "Hello world"


@app.get('/movies', tags=['Home'])
def home():
    return HTMLResponse(content="<h1>Movies</h1><p>List of movies will be here.</p>", status_code=200)