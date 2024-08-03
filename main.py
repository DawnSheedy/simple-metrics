from fastapi import FastAPI

app = FastAPI()

@app.get("/sm-service")
async def root():
    return {"message": "Hello World"}