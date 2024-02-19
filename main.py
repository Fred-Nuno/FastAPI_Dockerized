from fastapi import FastAPI
from os import environ


app = FastAPI()

@app.get("/")
def index():
    return {"Message":f"Hello, World from FastAPI! Secret_Key is: {environ['MY_SECRET_KEY']}."}