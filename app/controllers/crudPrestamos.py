from fastapi import HTTPException

from app.schemas.prestamo_schema import PrestamoCreate, PrestamoUpdate
from app.services.prestamo_service import PrestamoService


# Loans controller: uses PrestamoService and handles HTTP errors
class PrestamoController:

    @staticmethod
    # List all loans
    def listar_prestamos():
        """Get all loans.

        Parameters: none.
        Returns: List[Prestamo] (list of loans).
        """
        return PrestamoService.listar()

    @staticmethod
    # Get a loan by ID or 404 if not found
    def obtener_prestamo(prestamo_id: str):
        """Get a loan by its ID.

        Parameters:
        - prestamo_id: str
        Returns: Prestamo if it exists.
        Raises: HTTPException 404 if not found.
        """
        prestamo = PrestamoService.obtener_por_id(prestamo_id)
        if not prestamo:
            raise HTTPException(status_code=404, detail="Loan not found")
        return prestamo

    @staticmethod
    # Create a loan validating user/book/stock
    def crear_prestamo(data: PrestamoCreate):
        """Create a new loan.

        Parameters:
        - data: PrestamoCreate (user_id, isbn).
        Returns: Created Prestamo.
        Raises: HTTPException 400 if creation fails (invalid user/book or out of stock).
        """
        nuevo = PrestamoService.crear(
            user_id=data.user_id,
            isbn=data.isbn,
        )
        if not nuevo:
            raise HTTPException(
                status_code=400,
                detail="Could not create loan (invalid user/book or out of stock)",
            )
        return nuevo

    @staticmethod
    # Register return and trigger reservation assignment
    def registrar_devolucion(prestamo_id: str):
        """Register the return of a loan.

        Parameters:
        - prestamo_id: str
        Returns: Updated Prestamo.
        Raises: HTTPException 404 if the loan does not exist.
        """
        actualizado = PrestamoService.registrar_devolucion(prestamo_id)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Loan not found")
        return actualizado

    @staticmethod
    # Delete a loan by ID; return success message
    def eliminar_prestamo(prestamo_id: str):
        """Delete a loan by ID.

        Parameters:
        - prestamo_id: str
        Returns: dict with success message.
        Raises: HTTPException 404 if not found.
        """
        eliminado = PrestamoService.eliminar(prestamo_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Loan not found")
        return {"message": "Loan deleted"}

    @staticmethod
    # Return user's loan history as a list (LIFO)
    def historial_usuario(user_id: str):
        """Get a user's loan history.

        Parameters:
        - user_id: str
        Returns: list of loans in LIFO order (last first).
        """
        pila = PrestamoService.historial_por_usuario(user_id)
        # return as list (LIFO: latest loan first)
        return pila.to_list()
