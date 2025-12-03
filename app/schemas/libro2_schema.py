# app/schemas/libro2_schema.py
from pydantic import BaseModel

class Libro2Schema(BaseModel):
    isbn: str
    titulo: str
    autor: str
    peso: float
    valor: int
    stock: int
    paginas: int
    editorial: str
    idioma: str
    estanteria: int
