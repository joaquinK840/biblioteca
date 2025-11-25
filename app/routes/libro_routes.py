from fastapi import APIRouter
from typing import List
from app.controllers.crudLibros import LibroController
from app.schemas.libro_schema import LibroCreate, LibroUpdate, LibroOut

router = APIRouter(prefix="/libros", tags=["Libros"])

@router.get("/", response_model=List[LibroOut])
def listar():
    return LibroController.listar_libros()

@router.get("/{isbn}", response_model=LibroOut)
def obtener(isbn: str):
    return LibroController.obtener_libro(isbn)

@router.post("/", response_model=LibroOut)
def crear(data: LibroCreate):
    return LibroController.crear_libro(data)

@router.put("/{isbn}", response_model=LibroOut)
def actualizar(isbn: str, data: LibroUpdate):
    return LibroController.actualizar_libro(isbn, data)

@router.delete("/{isbn}")
def eliminar(isbn: str):
    return LibroController.eliminar_libro(isbn)

@router.get("/ordenados/isbn", response_model=List[LibroOut])
def obtener_libros_ordenados_isbn():
    return LibroController.libros_ordenados_isbn()

@router.get("/ordenados/precio", response_model=List[LibroOut])
def obtener_libros_ordenados_precio():
    return LibroController.libros_ordenados_precio()