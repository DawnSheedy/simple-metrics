from fastapi import FastAPI

app = FastAPI()

@app.get("/sm-service")
async def root():
    return {"message": "Hello World"}

@app.get("/sm-service/status")
async def root():
    return {"status": "OK"}