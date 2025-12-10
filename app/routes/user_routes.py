from fastapi import APIRouter
from app.controllers.crudUser import UsuarioController
from app.schemas.user_schema import UsuarioCreate, UsuarioUpdate

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/")
def listar():
    """Listar todos los usuarios"""
    return UsuarioController.listar_usuarios()

@router.get("/{user_id}")
def obtener(user_id: str):
    """Obtener un usuario por ID"""
    return UsuarioController.obtener_usuario(user_id)

@router.post("/")
def crear(data: UsuarioCreate):
    """Crear un nuevo usuario"""
    return UsuarioController.crear_usuario(data)

@router.put("/{user_id}")
def actualizar(user_id: str, data: UsuarioUpdate):
    """Actualizar un usuario por ID"""
    return UsuarioController.actualizar_usuario(user_id, data)

@router.delete("/{user_id}")
def eliminar(user_id: str):
    """Eliminar un usuario por ID"""
    return UsuarioController.eliminar_usuario(user_id)
