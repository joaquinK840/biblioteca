# app/routes/libro_routes.py
from fastapi import APIRouter
from typing import List
from app.controllers.crudLibros import LibroController
from app.schemas.libro_schema import LibroCreate, LibroUpdate, LibroOut
from app.schemas.estanteria_schema import EstanteriaResponse
from app.schemas.estanteria2_schema import EstanteriasOptimasResponse

router = APIRouter(prefix="/libros", tags=["Books"])

# ============================================
# STATIC ROUTES (must go BEFORE /{isbn})
# ============================================

@router.get("/", response_model=List[LibroOut])
def listar():
    """List all books"""
    return LibroController.listar_libros()


@router.get("/buscar", response_model=List[LibroOut])
def buscar_lineal(q: str):
    """Search books by title or author using linear search.
    
    Parameters:
    - q: query string (case-insensitive).
    Returns: list of matching books.
    """
    return LibroController.buscar_lineal(q)


@router.get("/ordenados/isbn", response_model=List[LibroOut])
def obtener_libros_ordenados_isbn():
    """Get books sorted by ISBN (Insertion Sort)"""
    return LibroController.libros_ordenados_isbn()


@router.get("/ordenados/precio", response_model=List[LibroOut])
def obtener_libros_ordenados_precio():
    """Get books sorted by price (Merge Sort)"""
    return LibroController.libros_ordenados_precio()


@router.get("/estanteria/deficiente", response_model=List[EstanteriaResponse])
def estanteria_deficiente():
    """Detect 4-book combinations > 8 kg (Brute Force)"""
    return LibroController.estanteria_deficiente()


@router.get("/estanteria/optima", response_model=EstanteriasOptimasResponse)
def estanteria_optima():
    """Compute optimal shelf <= 8 kg (Backtracking)"""
    return LibroController.estanteria_optima()


@router.get("/autor/{autor}/valor-total")
def valor_total(autor: str):
    """Calculate total value of books by author (Stack recursion)"""
    return LibroController.valor_total_autor(autor)


@router.get("/autor/{autor}/peso-promedio")
def peso_promedio(autor: str):
    """Calculate average weight of books by author (Tail recursion)"""
    return LibroController.peso_promedio_autor(autor)


# ============================================
# DYNAMIC ROUTES (must go AT THE END)
# ============================================

@router.get("/{isbn}", response_model=LibroOut)
def obtener(isbn: str):
    """Get a book by ISBN"""
    return LibroController.obtener_libro(isbn)


@router.post("/", response_model=LibroOut)
def crear(data: LibroCreate):
    """Create a new book"""
    return LibroController.crear_libro(data)


@router.put("/{isbn}", response_model=LibroOut)
def actualizar(isbn: str, data: LibroUpdate):
    """Update an existing book"""
    return LibroController.actualizar_libro(isbn, data)


@router.delete("/{isbn}")
def eliminar(isbn: str):
    """Delete a book by ISBN"""
    return LibroController.eliminar_libro(isbn)
