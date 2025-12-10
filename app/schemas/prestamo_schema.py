from pydantic import BaseModel
from datetime import date

class PrestamoBase(BaseModel):
    """Base attributes for a loan request."""
    user_id: str
    isbn: str

class PrestamoCreate(PrestamoBase):
    # Loan date can be calculated in the service (today)
    pass

class PrestamoUpdate(BaseModel):
    # Only updated when registering the return
    fecha_devolucion: date
    devuelto: bool

class PrestamoOut(BaseModel):
    """Response model for loan details."""
    prestamo_id: str
    user_id: str
    isbn: str
    fecha_prestamo: date
    fecha_devolucion: date | None = None
    devuelto: bool
