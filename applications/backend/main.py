from fastapi import FastAPI
from .routers import health, items

app = FastAPI()

app.include_router(health.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}