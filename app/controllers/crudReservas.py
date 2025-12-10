from fastapi import HTTPException

from app.schemas.reserva_schema import ReservaCreate
from app.services.reserva_service import ReservaService


# Controlador de reservas: usa ReservaService y maneja errores HTTP
class ReservaController:

    @staticmethod
    # Lista todas las reservas
    def listar_reservas():
        """Listar todas las reservas.

        Parámetros: ninguno.
        Retorna: List[Reserva].
        """
        return ReservaService.listar()

    @staticmethod
    # Obtiene una reserva por ID o 404 si no existe
    def obtener_reserva(reserva_id: str):
        """Obtener una reserva por ID.

        Parámetros:
        - reserva_id: str
        Retorna: Reserva si existe.
        Lanza: HTTPException 404 si no se encuentra.
        """
        reserva = ReservaService.obtener_por_id(reserva_id)
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva no encontrada")
        return reserva

    @staticmethod
    # Crea una reserva validando usuario/libro y stock
    def crear_reserva(data: ReservaCreate):
        """Crear una nueva reserva.

        Parámetros:
        - data: ReservaCreate (user_id, isbn).
        Retorna: Reserva creada.
        Lanza: HTTPException 400 si la creación no es válida.
        """
        nueva = ReservaService.crear(
            user_id=data.user_id,
            isbn=data.isbn,
        )
        if not nueva:
            raise HTTPException(
                status_code=400,
                detail="No se pudo crear la reserva (usuario/libro inválido o el libro aún tiene stock)",
            )
        return nueva

    @staticmethod
    # Elimina una reserva por ID; retorna mensaje de éxito
    def eliminar_reserva(reserva_id: str):
        """Eliminar una reserva por ID.

        Parámetros:
        - reserva_id: str
        Retorna: dict con mensaje de éxito.
        Lanza: HTTPException 404 si no se encuentra.
        """
        eliminado = ReservaService.eliminar(reserva_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Reserva no encontrada")
        return {"message": "Reserva eliminada"}

    @staticmethod
    # Devuelve la cola FIFO de reservas para un libro
    def ver_cola_por_libro(isbn: str):
        """Ver la cola de reservas para un libro.

        Parámetros:
        - isbn: str
        Retorna: lista de reservas en orden FIFO.
        """
        cola = ReservaService.cola_por_libro(isbn)
        return cola.to_list()
