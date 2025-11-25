from pydantic import BaseModel

class LibroBase(BaseModel):
    titulo: str
    autor: str
    peso: float
    valor: int
    stock: int
    paginas: int
    editorial: str
    idioma: str

class LibroCreate(LibroBase):
    isbn: str

class LibroUpdate(LibroBase):
    pass

class LibroOut(LibroBase):
    isbn: str
