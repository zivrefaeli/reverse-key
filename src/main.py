from fastapi import FastAPI, Request
from logger import logger

app = FastAPI()


@app.middleware("http")
async def logs_middleware(request: Request, call_next):
    response = await call_next(request)
    logger.debug(f"{request.method} {request.url} {response.status_code}")
    return response


@app.get("/")
def index() -> str:
    return "Hello World"


@app.post("/hello")
def say_hi(name: str) -> str:
    return f"Hello {name}"
