from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/api/goodbye")
def goodbye(name: str = "world"):
    return JSONResponse({"message": f"Goodbye, {name}!"})
