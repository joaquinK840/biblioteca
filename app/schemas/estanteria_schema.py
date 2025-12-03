from typing import List, Optional
from pydantic import BaseModel

class EstanteriaResponse(BaseModel):
    libros: List[str]
    peso_total: float 
