from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {
        "message": "Welcome to my first FastAPI app"
    }

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {
        "hello": name
    }