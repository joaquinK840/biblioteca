from fastapi import HTTPException

from app.models.user_model import Usuario
from app.schemas.user_schema import UsuarioCreate, UsuarioOut, UsuarioUpdate
from app.services.user_service import UsuarioService


class UsuarioController:

    @staticmethod
    def listar_usuarios():
        """Listar todos los usuarios.

        Parámetros: ninguno.
        Retorna: List[Usuario].
        """
        return UsuarioService.cargar_usuarios()

    @staticmethod
    def obtener_usuario(user_id: str):
        """Obtener un usuario por ID.

        Parámetros:
        - user_id: str
        Retorna: Usuario si existe.
        Lanza: HTTPException 404 si no se encuentra.
        """
        usuario = UsuarioService.obtener_por_id(user_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario

    @staticmethod
    def crear_usuario(data: UsuarioCreate):
        """Crear un nuevo usuario.

        Parámetros:
        - data: UsuarioCreate
        Retorna: Usuario creado.
        Lanza: HTTPException 400 si el ID ya existe.
        """
        usuario = Usuario(**data.dict())
        nuevo = UsuarioService.crear(usuario)
        if not nuevo:
            raise HTTPException(status_code=400, detail="El ID ya existe")
        return nuevo

    @staticmethod
    def actualizar_usuario(user_id: str, data: UsuarioUpdate):
        """Actualizar un usuario por ID.

        Parámetros:
        - user_id: str
        - data: UsuarioUpdate
        Retorna: Usuario actualizado.
        Lanza: HTTPException 404 si no se encuentra.
        """
        usuario_actualizado = Usuario(
            user_id=user_id,
            **data.dict()
        )
        actualizado = UsuarioService.actualizar(user_id, usuario_actualizado)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return actualizado

    @staticmethod
    def eliminar_usuario(user_id: str):
        """Eliminar un usuario por ID.

        Parámetros:
        - user_id: str
        Retorna: dict con mensaje de éxito.
        Lanza: HTTPException 404 si no se encuentra.
        """
        eliminado = UsuarioService.eliminar(user_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"message": "Usuario eliminado"}
