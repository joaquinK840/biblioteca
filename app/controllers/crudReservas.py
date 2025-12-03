from fastapi import HTTPException

from app.schemas.reserva_schema import ReservaCreate
from app.services.reserva_service import ReservaService


class ReservaController:

    @staticmethod
    def listar_reservas():
        """Listar todas las reservas.

        Parámetros: ninguno.
        Retorna: List[Reserva].
        """
        return ReservaService.listar()

    @staticmethod
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
    def ver_cola_por_libro(isbn: str):
        """Ver la cola de reservas para un libro.

        Parámetros:
        - isbn: str
        Retorna: lista de reservas en orden FIFO.
        """
        cola = ReservaService.cola_por_libro(isbn)
        return cola.to_list()
