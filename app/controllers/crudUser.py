from fastapi import HTTPException
from app.schemas.user_schema import UsuarioCreate, UsuarioUpdate, UsuarioOut
from app.models.user_model import Usuario
from app.services.user_service import UsuarioService

class UsuarioController:

    @staticmethod
    def listar_usuarios():
        return UsuarioService.cargar_usuarios()

    @staticmethod
    def obtener_usuario(user_id: str):
        usuario = UsuarioService.obtener_por_id(user_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario

    @staticmethod
    def crear_usuario(data: UsuarioCreate):
        usuario = Usuario(**data.dict())
        nuevo = UsuarioService.crear(usuario)
        if not nuevo:
            raise HTTPException(status_code=400, detail="El ID ya existe")
        return nuevo

    @staticmethod
    def actualizar_usuario(user_id: str, data: UsuarioUpdate):
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
        eliminado = UsuarioService.eliminar(user_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"message": "Usuario eliminado"}
