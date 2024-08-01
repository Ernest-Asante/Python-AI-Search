from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()



@app.get("/items")
async def read_item(item):
    return  item