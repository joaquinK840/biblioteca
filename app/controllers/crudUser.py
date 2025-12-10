from fastapi import HTTPException

from app.models.user_model import Usuario
from app.schemas.user_schema import UsuarioCreate, UsuarioOut, UsuarioUpdate
from app.services.user_service import UsuarioService


# Users controller: orchestrates UsuarioService and handles HTTP errors
class UsuarioController:

    @staticmethod
    # List all users
    def listar_usuarios():
        """List all users.

        Parameters: none.
        Returns: List[Usuario].
        """
        return UsuarioService.cargar_usuarios()

    @staticmethod
    # Get a user by ID or 404 if not found
    def obtener_usuario(user_id: str):
        """Get a user by ID.

        Parameters:
        - user_id: str
        Returns: Usuario if it exists.
        Raises: HTTPException 404 if not found.
        """
        usuario = UsuarioService.obtener_por_id(user_id)
        if not usuario:
            raise HTTPException(status_code=404, detail="User not found")
        return usuario

    @staticmethod
    # Create a user from the input schema
    def crear_usuario(data: UsuarioCreate):
        """Create a new user.

        Parameters:
        - data: UsuarioCreate
        Returns: Created Usuario.
        Raises: HTTPException 400 if the ID already exists.
        """
        usuario = Usuario(**data.dict())
        nuevo = UsuarioService.crear(usuario)
        if not nuevo:
            raise HTTPException(status_code=400, detail="ID already exists")
        return nuevo

    @staticmethod
    # Update a user by ID using schema data
    def actualizar_usuario(user_id: str, data: UsuarioUpdate):
        """Update a user by ID.

        Parameters:
        - user_id: str
        - data: UsuarioUpdate
        Returns: Updated Usuario.
        Raises: HTTPException 404 if not found.
        """
        usuario_actualizado = Usuario(
            user_id=user_id,
            **data.dict()
        )
        actualizado = UsuarioService.actualizar(user_id, usuario_actualizado)
        if not actualizado:
            raise HTTPException(status_code=404, detail="User not found")
        return actualizado

    @staticmethod
    # Delete a user by ID; return success message
    def eliminar_usuario(user_id: str):
        """Delete a user by ID.

        Parameters:
        - user_id: str
        Returns: dict with success message.
        Raises: HTTPException 404 if not found.
        """
        eliminado = UsuarioService.eliminar(user_id)
        if not eliminado:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted"}
