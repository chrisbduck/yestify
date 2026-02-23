from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def hello(name: str = "world"):
    return JSONResponse({"message": f"Hello, {name}!"})
