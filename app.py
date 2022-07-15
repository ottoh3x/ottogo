from fastapi import FastAPI
import datetime
from .gogoanime import *
import json

app = FastAPI()

@app.get('/recently/{page}')
def recently(page: int):
    return {
        "message": "Hello my friend"
    }

@app.get("/")
def main():
    return {
        "message": "Hello my friend"
    }
