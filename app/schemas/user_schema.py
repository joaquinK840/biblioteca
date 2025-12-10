from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    """Base attributes for a user entity."""
    nombre: str
    correo: EmailStr
    telefono: str

class UsuarioCreate(UsuarioBase):
    """Payload to create a new user."""
    user_id: str

class UsuarioUpdate(UsuarioBase):
    """Payload to update an existing user."""
    pass

class UsuarioOut(UsuarioBase):
    """Response model for user data (includes user_id)."""
    user_id: str
