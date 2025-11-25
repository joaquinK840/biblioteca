from pydantic import BaseModel
from datetime import date

class PrestamoBase(BaseModel):
    user_id: str
    isbn: str

class PrestamoCreate(PrestamoBase):
    # fecha de préstamo se puede calcular en el servicio (hoy)
    pass

class PrestamoUpdate(BaseModel):
    # solo se actualizará al registrar devolución
    fecha_devolucion: date
    devuelto: bool

class PrestamoOut(BaseModel):
    prestamo_id: str
    user_id: str
    isbn: str
    fecha_prestamo: date
    fecha_devolucion: date | None = None
    devuelto: bool
