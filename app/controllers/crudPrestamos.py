from fastapi import HTTPException
from app.schemas.prestamo_schema import PrestamoCreate, PrestamoUpdate
from app.services.prestamo_service import PrestamoService


class PrestamoController:

    @staticmethod
    def listar_prestamos():
        return PrestamoService.listar()

    @staticmethod
    def obtener_prestamo(prestamo_id: str):
        prestamo = PrestamoService.obtener_por_id(prestamo_id)
        if not prestamo:
            raise HTTPException(status_code=404, detail="Préstamo no encontrado")
        return prestamo

    @staticmethod
    def crear_prestamo(data: PrestamoCreate):
        nuevo = PrestamoService.crear(
            user_id=data.user_id,
            isbn=data.isbn,
        )
        if not nuevo:
            raise HTTPException(
                status_code=400,
                detail="No se pudo crear el préstamo (usuario/libro inválido o sin stock)",
            )
        return nuevo

    @staticmethod
    def registrar_devolucion(prestamo_id: str):
        actualizado = PrestamoService.registrar_devolucion(prestamo_id)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Préstamo no encontrado")
        return actualizado

    @staticmethod
    def eliminar_prestamo(prestamo_id: str):
        eliminado = PrestamoService.eliminar(prestamo_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Préstamo no encontrado")
        return {"message": "Préstamo eliminado"}

    @staticmethod
    def historial_usuario(user_id: str):
        pila = PrestamoService.historial_por_usuario(user_id)
        # devolvemos como lista (LIFO: último préstamo primero)
        return pila.to_list()
