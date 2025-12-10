from pydantic import BaseModel

class LibroBase(BaseModel):
    """Base attributes for a book entity."""
    titulo: str
    autor: str
    peso: float
    valor: int
    stock: int
    paginas: int
    editorial: str
    idioma: str
    

class LibroCreate(LibroBase):
    """Payload to create a new book."""
    isbn: str

class LibroUpdate(LibroBase):
    """Payload to update an existing book."""
    pass

class LibroOut(LibroBase):
    """Response model for book data (includes ISBN)."""
    isbn: str
