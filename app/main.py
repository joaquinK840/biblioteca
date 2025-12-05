from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from app.routes.libro_routes import router as libros_router
from app.routes.user_routes import router as user_router
from app.routes.prestamos_routes import router as prestamos_router
from app.routes.reservas_routes import router as reservas_router
from app.routes.estanterias import router as estanterias_router

app = FastAPI(title="CSV Library API")

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates HTML
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Routers API
app.include_router(libros_router)
app.include_router(user_router)
app.include_router(prestamos_router)
app.include_router(reservas_router)
app.include_router(estanterias_router)
