from pydantic import BaseModel
from datetime import date

class ReservaBase(BaseModel):
    """Base attributes for a reservation request."""
    user_id: str
    isbn: str

class ReservaCreate(ReservaBase):
    # Reservation date is calculated in the service
    pass

class ReservaOut(BaseModel):
    """Response model for reservation details."""
    reserva_id: str
    user_id: str
    isbn: str
    fecha_reserva: date
