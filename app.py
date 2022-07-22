import uvicorn
from gogoanime import *
from fastapi import FastAPI
import json
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/api/recently/{page}')
async def recently(page: int):
    recently = GogoanimeParser.get_recently_uploaded(page=page)
    return json.loads(recently)


@app.get('/api/popular/{page}')
async def popular(page: int):
    popular = GogoanimeParser.popular(page=page)
    return json.loads(popular)

@app.get('/api/new-season/{page}')
async def newseason(page: int):
    newseason = GogoanimeParser.newSeason(page=page)
    return json.loads(newseason)

@app.get('/api/movies/{page}')
async def movies(page: int):
    movies = GogoanimeParser.movies(page=page)
    return json.loads(movies)

@app.get('/api/search/{key}/{page}')
async def search(key: str ,page: int):
    search = GogoanimeParser.search(key=key,page=page)
    return search


@app.get('/api/category/{genre}/{page}')
async def genre(genre: str, page: int):
    genre = GogoanimeParser.genre(genre_name=genre, page=page)
    return genre


@app.get('/api/details/{animeid}')
async def details(animeid: str):
    detail = GogoanimeParser.details(animeid=animeid)
    return detail


@app.get('/api/{animeid}/episode/{episode_num}')
async def episode(animeid: str, episode_num: int):
    episode = GogoanimeParser.episode(animeid=animeid, episode_num=episode_num)
    return episode


@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
