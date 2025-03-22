from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home(tokens: str):
    return {"data": tokens}
