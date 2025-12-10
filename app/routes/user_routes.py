from fastapi import APIRouter
from app.controllers.crudUser import UsuarioController
from app.schemas.user_schema import UsuarioCreate, UsuarioUpdate

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/")
def listar():
    """List all users"""
    return UsuarioController.listar_usuarios()

@router.get("/{user_id}")
def obtener(user_id: str):
    """Get a user by ID"""
    return UsuarioController.obtener_usuario(user_id)

@router.post("/")
def crear(data: UsuarioCreate):
    """Create a new user"""
    return UsuarioController.crear_usuario(data)

@router.put("/{user_id}")
def actualizar(user_id: str, data: UsuarioUpdate):
    """Update a user by ID"""
    return UsuarioController.actualizar_usuario(user_id, data)

@router.delete("/{user_id}")
def eliminar(user_id: str):
    """Delete a user by ID"""
    return UsuarioController.eliminar_usuario(user_id)
