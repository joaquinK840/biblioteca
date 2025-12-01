from typing import List, Optional
from pydantic import BaseModel

class EstanteriaResponse2(BaseModel):
    libros: List[str]
    peso_total: float 
    precio_total: Optional[int]