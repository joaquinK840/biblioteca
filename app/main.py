from fastapi import FastAPI
from app.routes.libro_routes import router as libros_router
from app.routes.user_routes import router as user_router
from app.routes.prestamos_routes import router as prestamos_router
from app.routes.reservas_routes import router as reservas_router

app = FastAPI(title="CSV Library API")

app.include_router(libros_router)
app.include_router(user_router)
app.include_router(prestamos_router)
app.include_router(reservas_router)


@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
