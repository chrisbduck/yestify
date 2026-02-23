# Vercel Python runtime: expose an `app` (ASGI) for frameworks like FastAPI.
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Vercel + FastAPI", description="Vercel + FastAPI", version="1.0.0")

@app.get("/api/hello")
def hello(name: str = "world"):
    return JSONResponse({"message": f"Hello, {name}!"})
