from fastapi import HTTPException

from app.schemas.prestamo_schema import PrestamoCreate, PrestamoUpdate
from app.services.prestamo_service import PrestamoService


class PrestamoController:

    @staticmethod
    def listar_prestamos():
        """Obtener todos los préstamos.

        Parámetros: ninguno.
        Retorna: List[Prestamo] (lista de préstamos).
        """
        return PrestamoService.listar()

    @staticmethod
    def obtener_prestamo(prestamo_id: str):
        """Obtener un préstamo por su ID.

        Parámetros:
        - prestamo_id: str
        Retorna: Prestamo si existe.
        Lanza: HTTPException 404 si no se encuentra.
        """
        prestamo = PrestamoService.obtener_por_id(prestamo_id)
        if not prestamo:
            raise HTTPException(status_code=404, detail="Préstamo no encontrado")
        return prestamo

    @staticmethod
    def crear_prestamo(data: PrestamoCreate):
        """Crear un nuevo préstamo.

        Parámetros:
        - data: PrestamoCreate (user_id, isbn).
        Retorna: Prestamo creado.
        Lanza: HTTPException 400 si la creación falla (usuario/libro inválido o sin stock).
        """
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
        """Registrar la devolución de un préstamo.

        Parámetros:
        - prestamo_id: str
        Retorna: Prestamo actualizado.
        Lanza: HTTPException 404 si no existe el préstamo.
        """
        actualizado = PrestamoService.registrar_devolucion(prestamo_id)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Préstamo no encontrado")
        return actualizado

    @staticmethod
    def eliminar_prestamo(prestamo_id: str):
        """Eliminar un préstamo por ID.

        Parámetros:
        - prestamo_id: str
        Retorna: dict con mensaje de éxito.
        Lanza: HTTPException 404 si no se encuentra.
        """
        eliminado = PrestamoService.eliminar(prestamo_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Préstamo no encontrado")
        return {"message": "Préstamo eliminado"}

    @staticmethod
    def historial_usuario(user_id: str):
        """Obtener historial de préstamos de un usuario.

        Parámetros:
        - user_id: str
        Retorna: lista de préstamos en orden LIFO (último primero).
        """
        pila = PrestamoService.historial_por_usuario(user_id)
        # devolvemos como lista (LIFO: último préstamo primero)
        return pila.to_list()
