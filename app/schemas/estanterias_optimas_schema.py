from typing import List
from pydantic import BaseModel

class EstanteriaOptima(BaseModel):
    estanteria: int
    libros: List[str]
    peso_total: float
    precio_total: float

class EstanteriasOptimasResponse(BaseModel):
    resultado: List[EstanteriaOptima]
