# Vercel Python runtime: expose an `app` (ASGI) for frameworks like FastAPI.
from fastapi import FastAPI
from api.routers import hello, goodbye

app = FastAPI(title="Vercel + FastAPI", description="Vercel + FastAPI", version="1.0.0")

app.include_router(hello.router)
app.include_router(goodbye.router)
