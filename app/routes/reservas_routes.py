from fastapi import APIRouter
from app.controllers.crudReservas import ReservaController
from app.schemas.reserva_schema import ReservaCreate

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.get("/")
def listar_reservas():
    """List all reservations"""
    return ReservaController.listar_reservas()


@router.get("/{reserva_id}")
def obtener_reserva(reserva_id: str):
    """Get a reservation by ID"""
    return ReservaController.obtener_reserva(reserva_id)


@router.post("/")
def crear_reserva(data: ReservaCreate):
    """Create a new reservation"""
    return ReservaController.crear_reserva(data)


@router.delete("/{reserva_id}")
def eliminar_reserva(reserva_id: str):
    """Delete a reservation by ID"""
    return ReservaController.eliminar_reserva(reserva_id)


@router.get("/cola/{isbn}")
def ver_cola(isbn: str):
    """View the reservation queue for a book (FIFO)"""
    return ReservaController.ver_cola_por_libro(isbn)
