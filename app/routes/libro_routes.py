# app/routes/libro_routes.py
from fastapi import APIRouter
from typing import List
from app.controllers.crudLibros import LibroController
from app.schemas.libro_schema import LibroCreate, LibroUpdate, LibroOut
from app.schemas.estanteria_schema import EstanteriaResponse
from app.schemas.estanteria2_schema import EstanteriasOptimasResponse

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

@router.get("/estanteria/deficiente", response_model=List[EstanteriaResponse])
def estanteria_deficiente():
    return LibroController.estanteria_deficiente()

@router.get("/estanteria/optima", response_model=EstanteriasOptimasResponse)
def estanteria_optima():
    return LibroController.estanteria_optima()

@router.get("/autor/{autor}/valor-total")
def valor_total(autor: str):
    return LibroController.valor_total_autor(autor)

@router.get("/autor/{autor}/peso-promedio")
def peso_promedio(autor: str):
    return LibroController.peso_promedio_autor(autor)
