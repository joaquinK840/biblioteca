# app/routes/libro_routes.py
from fastapi import APIRouter
from typing import List
from app.controllers.crudLibros import LibroController
from app.schemas.libro_schema import LibroCreate, LibroUpdate, LibroOut
from app.schemas.estanteria_schema import EstanteriaResponse
from app.schemas.estanteria2_schema import EstanteriasOptimasResponse

router = APIRouter(prefix="/libros", tags=["Libros"])

# ============================================
# RUTAS ESTÁTICAS (deben ir ANTES de /{isbn})
# ============================================

@router.get("/", response_model=List[LibroOut])
def listar():
    """Listar todos los libros"""
    return LibroController.listar_libros()


@router.get("/buscar", response_model=List[LibroOut])
def buscar_lineal(q: str):
    """Buscar libros por título o autor usando búsqueda lineal.
    
    Parámetros:
    - q: cadena de consulta (case-insensitive).
    Retorna: lista de libros coincidentes.
    """
    return LibroController.buscar_lineal(q)


@router.get("/ordenados/isbn", response_model=List[LibroOut])
def obtener_libros_ordenados_isbn():
    """Obtener libros ordenados por ISBN (Insertion Sort)"""
    return LibroController.libros_ordenados_isbn()


@router.get("/ordenados/precio", response_model=List[LibroOut])
def obtener_libros_ordenados_precio():
    """Obtener libros ordenados por precio (Merge Sort)"""
    return LibroController.libros_ordenados_precio()


@router.get("/estanteria/deficiente", response_model=List[EstanteriaResponse])
def estanteria_deficiente():
    """Detectar combinaciones de 4 libros > 8 Kg (Fuerza Bruta)"""
    return LibroController.estanteria_deficiente()


@router.get("/estanteria/optima", response_model=EstanteriasOptimasResponse)
def estanteria_optima():
    """Calcular estantería óptima <= 8 Kg (Backtracking)"""
    return LibroController.estanteria_optima()


@router.get("/autor/{autor}/valor-total")
def valor_total(autor: str):
    """Calcular valor total de libros por autor (Recursión de Pila)"""
    return LibroController.valor_total_autor(autor)


@router.get("/autor/{autor}/peso-promedio")
def peso_promedio(autor: str):
    """Calcular peso promedio de libros por autor (Recursión de Cola)"""
    return LibroController.peso_promedio_autor(autor)


# ============================================
# RUTAS DINÁMICAS (deben ir AL FINAL)
# ============================================

@router.get("/{isbn}", response_model=LibroOut)
def obtener(isbn: str):
    """Obtener un libro por ISBN"""
    return LibroController.obtener_libro(isbn)


@router.post("/", response_model=LibroOut)
def crear(data: LibroCreate):
    """Crear un nuevo libro"""
    return LibroController.crear_libro(data)


@router.put("/{isbn}", response_model=LibroOut)
def actualizar(isbn: str, data: LibroUpdate):
    """Actualizar un libro existente"""
    return LibroController.actualizar_libro(isbn, data)


@router.delete("/{isbn}")
def eliminar(isbn: str):
    """Eliminar un libro por ISBN"""
    return LibroController.eliminar_libro(isbn)
