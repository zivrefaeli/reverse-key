from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index() -> str:
    return "Hello World"


@app.post("/hello")
def say_hi(name: str) -> str:
    return f"Hello {name}"
