from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "hello world"}


@app.get("/info")
async def read_root():
    return {"message": "Here there are infos about this project"}


@app.get("/greet")
async def greet(name: Optional[str] = "user", age: Optional[int] = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}


class UserModel(BaseModel):
    username: str
    password: str


@app.post("/register")
async def registerUser(userdata: UserModel):
    return {"username": userdata.username, "password": userdata.password}

