from fastapi import FastAPI
import datetime
from .gogoanime import *
import json

app = FastAPI()

@app.get('/recently/{page}')
def recently(page: int):
    recently = GogoanimeParser.get_recently_uploaded(page=page)
    return json.loads(recently)

@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }
