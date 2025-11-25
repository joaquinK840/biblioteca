from pydantic import BaseModel, EmailStr

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: str

class UsuarioCreate(UsuarioBase):
    user_id: str

class UsuarioUpdate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    user_id: str
