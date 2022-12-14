from fastapi import FastAPI
import uvicorn
from mylib.logic import querydb
from mylib.connect_db import *

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Pokedex"}

@app.get("/query")
async def query():
    """Execute a SQL query"""
    result = querydb()
    return {"result": result}

@app.get("/query/{cat}/{name}")
async def query_custom(cat: str, name:str):
    """Execute a SQL query"""
    result = querydb(cat,name)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")