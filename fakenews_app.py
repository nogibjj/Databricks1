from ast import Str
from tkinter.font import names
from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb
import pandas as pd

app = FastAPI()

from databricks import sql
import os


@app.get("/")
async def root():
    """ Return an article and its identity from the database """
    return {"Is it real or fake": "hello News World!"}


@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

@app.get("/realnews")
async def realnews():
    """print news"""
    authors = querydb("SELECT author FROM default.nyt WHERE label == 'Real'")
    return {"Authentic Author": authors}

@app.get("/fakenews")
async def fakenews():
    """print news"""
    authors = querydb("SELECT author FROM default.nyt WHERE label == 'Fake'")
    return {"Fake Author": authors}

@app.get("/news/{num}")
async def news(num: int):
    """print news"""
    content = querydb(f"SELECT text FROM (Select ROW_NUMBER() OVER (order by title) as Row_Number, * from default.nyt) as tbl Where tbl.Row_Number == {num}")
    return {"text": content}

@app.get("/news/{num}/{labelanswer}")
async def news(num: int, labelanswer: str):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
        ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT label FROM (Select ROW_NUMBER() OVER (order by title) as Row_Number, * from default.nyt) as tbl Where tbl.Row_Number == {num}")
            result = []
            for row in cursor:
                for field in row:
                    result.append(field)
            if labelanswer in result:
                return {"Correct! You have a good sense of news!"}
            return {"Wrong! Guess Again!"}

@app.get("/query")
async def query():
    """Execute a SQL query"""

    result = querydb()
    return {"result": result}
    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")