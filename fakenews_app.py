from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb
from databricks import sql
import os

app = FastAPI()

@app.get("/")
async def root():
    """ Return an article and its identity from the database """
    return {"Welcome to the News World!": "Please choose a number from 1 to 2088 to see the news and guess its identity!"}

@app.get("/news/{num}")
async def news(num: int):
    """print news"""
    content = querydb(f"SELECT text FROM (Select ROW_NUMBER() OVER (order by title) as Row_Number, * from default.nyt) as tbl Where tbl.Row_Number == {num}")
    return {"Please guess whether this news is 'Real' or 'Fake'!":content}

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
            return {"Are you sure?? Guess Again!"}

@app.get("/realnews")
async def realnews():
    """print news authors"""
    authors = querydb("SELECT author FROM default.nyt WHERE label == 'Real'")
    return {"Authentic Authors": authors}

@app.get("/fakenews")
async def fakenews():
    """print news authors"""
    authors = querydb("SELECT author FROM default.nyt WHERE label == 'Fake'")
    return {"Fake Authors": authors}

@app.get("/query")
async def query():
    """Execute a SQL query"""

    result = querydb()
    return {"result": result}
    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")