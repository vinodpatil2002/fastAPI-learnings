from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "hello world"}


@app.get("/info")
async def read_root():
    return {"message": "Here there are infos about this project"}


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"message": f"Hello {name}"}
