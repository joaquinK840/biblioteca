from fastapi import APIRouter
from app.controllers.crudPrestamos import PrestamoController
from app.schemas.prestamo_schema import PrestamoCreate, PrestamoUpdate

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])


@router.get("/")
def listar_prestamos():
    """Listar todos los préstamos"""
    return PrestamoController.listar_prestamos()


@router.get("/{prestamo_id}")
def obtener_prestamo(prestamo_id: str):
    """Obtener un préstamo por ID"""
    return PrestamoController.obtener_prestamo(prestamo_id)


@router.post("/")
def crear_prestamo(data: PrestamoCreate):
    """Crear un nuevo préstamo"""
    return PrestamoController.crear_prestamo(data)


@router.put("/devolver/{prestamo_id}")
def registrar_devolucion(prestamo_id: str):
    """Registrar devolución de un préstamo"""
    return PrestamoController.registrar_devolucion(prestamo_id)


@router.delete("/{prestamo_id}")
def eliminar_prestamo(prestamo_id: str):
    """Eliminar un préstamo por ID"""
    return PrestamoController.eliminar_prestamo(prestamo_id)


@router.get("/historial/{user_id}")
def historial_usuario(user_id: str):
    """Ver historial de préstamos de un usuario (LIFO)"""
    return PrestamoController.historial_usuario(user_id)
