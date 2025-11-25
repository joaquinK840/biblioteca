from fastapi import HTTPException
from app.schemas.reserva_schema import ReservaCreate
from app.services.reserva_service import ReservaService


class ReservaController:

    @staticmethod
    def listar_reservas():
        return ReservaService.listar()

    @staticmethod
    def obtener_reserva(reserva_id: str):
        reserva = ReservaService.obtener_por_id(reserva_id)
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva no encontrada")
        return reserva

    @staticmethod
    def crear_reserva(data: ReservaCreate):
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
        eliminado = ReservaService.eliminar(reserva_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Reserva no encontrada")
        return {"message": "Reserva eliminada"}

    @staticmethod
    def ver_cola_por_libro(isbn: str):
        cola = ReservaService.cola_por_libro(isbn)
        return cola.to_list()
