from fastapi import APIRouter
from app.controllers.crudPrestamos import PrestamoController
from app.schemas.prestamo_schema import PrestamoCreate, PrestamoUpdate

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])


@router.get("/")
def listar_prestamos():
    """List all loans"""
    return PrestamoController.listar_prestamos()


@router.get("/{prestamo_id}")
def obtener_prestamo(prestamo_id: str):
    """Get a loan by ID"""
    return PrestamoController.obtener_prestamo(prestamo_id)


@router.post("/")
def crear_prestamo(data: PrestamoCreate):
    """Create a new loan"""
    return PrestamoController.crear_prestamo(data)


@router.put("/devolver/{prestamo_id}")
def registrar_devolucion(prestamo_id: str):
    """Register a loan return"""
    return PrestamoController.registrar_devolucion(prestamo_id)


@router.delete("/{prestamo_id}")
def eliminar_prestamo(prestamo_id: str):
    """Delete a loan by ID"""
    return PrestamoController.eliminar_prestamo(prestamo_id)


@router.get("/historial/{user_id}")
def historial_usuario(user_id: str):
    """View a user's loan history (LIFO)"""
    return PrestamoController.historial_usuario(user_id)
