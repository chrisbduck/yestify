from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def goodbye(name: str = "world"):
    return JSONResponse({"message": f"Goodbye, {name}!"})
