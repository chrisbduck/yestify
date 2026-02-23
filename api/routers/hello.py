from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/api/hello")
def hello(name: str = "world"):
    return JSONResponse({"message": f"Hello, {name}!"})
