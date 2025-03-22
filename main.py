from fastapi import FastAPI
from gpxindex.index import GPXIndex

app = FastAPI()
index = GPXIndex("/home/gpxbaikal/gpxbot/mindex")

@app.get("/v1/")
async def search(tokens: str):
    return index.search(tokens)
