from fastapi import FastAPI
from app.routes.libro_routes import router as libros_router

app = FastAPI(title="CSV Library API")

app.include_router(libros_router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
