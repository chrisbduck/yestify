# Vercel Python runtime: expose an `app` (ASGI) for frameworks like FastAPI.
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/hello")
def hello(name: str = "world"):
    return JSONResponse({"message": f"Hello, {name}!"})
