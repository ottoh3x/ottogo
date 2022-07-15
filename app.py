from fastapi import FastAPI
import datetime
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
