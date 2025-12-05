from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from app.routes.libro_routes import router as libros_router
from app.routes.user_routes import router as user_router
from app.routes.prestamos_routes import router as prestamos_router
from app.routes.reservas_routes import router as reservas_router
from app.routes.estanterias import router as estanterias_router

app = FastAPI(title="CSV Library API")

# Configuración CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios concretos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates HTML con Jinja2
templates = Jinja2Templates(directory="app/templates")


# ============================================
# RUTAS DE VISTAS (Templates HTML)
# ============================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Página principal - Dashboard"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/templates/libros", response_class=HTMLResponse)
def vista_libros(request: Request):
    """Vista de gestión de libros"""
    return templates.TemplateResponse("libros.html", {"request": request})


@app.get("/templates/usuarios", response_class=HTMLResponse)
def vista_usuarios(request: Request):
    """Vista de gestión de usuarios"""
    return templates.TemplateResponse("usuarios.html", {"request": request})


@app.get("/templates/prestamos", response_class=HTMLResponse)
def vista_prestamos(request: Request):
    """Vista de gestión de préstamos"""
    return templates.TemplateResponse("prestamos.html", {"request": request})


@app.get("/templates/reservas", response_class=HTMLResponse)
def vista_reservas(request: Request):
    """Vista de gestión de reservas"""
    return templates.TemplateResponse("reservas.html", {"request": request})


@app.get("/templates/estanterias", response_class=HTMLResponse)
def vista_estanterias(request: Request):
    """Vista de módulo de estanterías"""
    return templates.TemplateResponse("estanterias.html", {"request": request})


# ============================================
# ROUTERS API (Endpoints JSON)
# ============================================
app.include_router(libros_router)
app.include_router(user_router)
app.include_router(prestamos_router)
app.include_router(reservas_router)
app.include_router(estanterias_router)
