from typing import List
from pydantic import BaseModel

class EstanteriaOptima(BaseModel):
    """Optimal shelf assignment with totals."""
    estanteria: int
    libros: List[str]
    peso_total: float
    precio_total: float

class EstanteriasOptimasResponse(BaseModel):
    """Response container for multiple optimal shelf results."""
    resultado: List[EstanteriaOptima]
