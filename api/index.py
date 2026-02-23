# Vercel Python runtime: expose an `app` (ASGI) for frameworks like FastAPI.
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

app = FastAPI(title="Vercel + FastAPI", description="Vercel + FastAPI", version="1.0.0")

router = APIRouter()

@router.get("/hello")
def hello(name: str = "world"):
    return JSONResponse({"message": f"Hello, {name}!"})

@router.get("/goodbye")
def goodbye(name: str = "world"):
    return JSONResponse({"message": f"Goodbye, {name}!"})

app.include_router(router, prefix="/api")