from typing import List, Optional
from pydantic import BaseModel

class EstanteriaResponse(BaseModel):
    """Response for unsafe shelf combinations (brute force)."""
    libros: List[str]
    peso_total: float 
