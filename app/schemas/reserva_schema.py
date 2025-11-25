from pydantic import BaseModel
from datetime import date

class ReservaBase(BaseModel):
    user_id: str
    isbn: str

class ReservaCreate(ReservaBase):
    # fecha_reserva se calcula en el servicio
    pass

class ReservaOut(BaseModel):
    reserva_id: str
    user_id: str
    isbn: str
    fecha_reserva: date
