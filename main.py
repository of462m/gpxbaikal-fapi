from fastapi import FastAPI
from gpxindex.index import GPXIndex

app = FastAPI()
index = GPXIndex("/var/db/mindex")

@app.get("/v1/")
async def search(tokens: str):
    return index.search(tokens)


if __name__ == "__main__":
    print(index.search_by_coords(53.63772,108.80937))
