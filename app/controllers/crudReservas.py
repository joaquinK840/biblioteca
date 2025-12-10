from fastapi import HTTPException

from app.schemas.reserva_schema import ReservaCreate
from app.services.reserva_service import ReservaService


# Reservations controller: uses ReservaService and handles HTTP errors
class ReservaController:

    @staticmethod
    # List all reservations
    def listar_reservas():
        """List all reservations.

        Parameters: none.
        Returns: List[Reserva].
        """
        return ReservaService.listar()

    @staticmethod
    # Get a reservation by ID or 404 if not found
    def obtener_reserva(reserva_id: str):
        """Get a reservation by ID.

        Parameters:
        - reserva_id: str
        Returns: Reserva if it exists.
        Raises: HTTPException 404 if not found.
        """
        reserva = ReservaService.obtener_por_id(reserva_id)
        if not reserva:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return reserva

    @staticmethod
    # Create a reservation validating user/book and stock
    def crear_reserva(data: ReservaCreate):
        """Create a new reservation.

        Parameters:
        - data: ReservaCreate (user_id, isbn).
        Returns: Created Reserva.
        Raises: HTTPException 400 if creation is not valid.
        """
        nueva = ReservaService.crear(
            user_id=data.user_id,
            isbn=data.isbn,
        )
        if not nueva:
            raise HTTPException(
                status_code=400,
                detail="Could not create reservation (invalid user/book or the book still has stock)",
            )
        return nueva

    @staticmethod
    # Delete a reservation by ID; return success message
    def eliminar_reserva(reserva_id: str):
        """Delete a reservation by ID.

        Parameters:
        - reserva_id: str
        Returns: dict with success message.
        Raises: HTTPException 404 if not found.
        """
        eliminado = ReservaService.eliminar(reserva_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Reservation not found")
        return {"message": "Reservation deleted"}

    @staticmethod
    # Return the FIFO queue of reservations for a book
    def ver_cola_por_libro(isbn: str):
        """View the reservation queue for a book.

        Parameters:
        - isbn: str
        Returns: list of reservations in FIFO order.
        """
        cola = ReservaService.cola_por_libro(isbn)
        return cola.to_list()
