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

# FastAPI application entrypoint
app = FastAPI(title="CSV Library API")

# CORS: allow frontend requests (restrict origins in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify concrete domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files: CSS/JS/images under /static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# HTML templates via Jinja2 (folder app/templates)
templates = Jinja2Templates(directory="app/templates")


# ============================================
# VIEW ROUTES (HTML Templates)
# ============================================

# View: homepage (dashboard)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Homepage - Dashboard"""
    return templates.TemplateResponse("index.html", {"request": request})


# View: books management
@app.get("/templates/libros", response_class=HTMLResponse)
def vista_libros(request: Request):
    """Books management view"""
    return templates.TemplateResponse("libros.html", {"request": request})


# View: users management
@app.get("/templates/usuarios", response_class=HTMLResponse)
def vista_usuarios(request: Request):
    """Users management view"""
    return templates.TemplateResponse("usuarios.html", {"request": request})


# View: loans management
@app.get("/templates/prestamos", response_class=HTMLResponse)
def vista_prestamos(request: Request):
    """Loans management view"""
    return templates.TemplateResponse("prestamos.html", {"request": request})


# View: reservations management
@app.get("/templates/reservas", response_class=HTMLResponse)
def vista_reservas(request: Request):
    """Reservations management view"""
    return templates.TemplateResponse("reservas.html", {"request": request})


# View: shelves module
@app.get("/templates/estanterias", response_class=HTMLResponse)
def vista_estanterias(request: Request):
    """Shelves module view"""
    return templates.TemplateResponse("estanterias.html", {"request": request})


# API routers: register JSON endpoints
# (books, users, loans, reservations, shelves)
app.include_router(libros_router)
app.include_router(user_router)
app.include_router(prestamos_router)
app.include_router(reservas_router)
app.include_router(estanterias_router)
