from fastapi import APIRouter
from app.controllers.crudReservas import ReservaController
from app.schemas.reserva_schema import ReservaCreate

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.get("/")
def listar_reservas():
    """Listar todas las reservas"""
    return ReservaController.listar_reservas()


@router.get("/{reserva_id}")
def obtener_reserva(reserva_id: str):
    """Obtener una reserva por ID"""
    return ReservaController.obtener_reserva(reserva_id)


@router.post("/")
def crear_reserva(data: ReservaCreate):
    """Crear una nueva reserva"""
    return ReservaController.crear_reserva(data)


@router.delete("/{reserva_id}")
def eliminar_reserva(reserva_id: str):
    """Eliminar una reserva por ID"""
    return ReservaController.eliminar_reserva(reserva_id)


@router.get("/cola/{isbn}")
def ver_cola(isbn: str):
    """Ver la cola de reservas para un libro (FIFO)"""
    return ReservaController.ver_cola_por_libro(isbn)
