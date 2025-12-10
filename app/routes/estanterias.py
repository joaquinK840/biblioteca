from fastapi import APIRouter
from app.controllers.estanteria_controller import EstanteriaController

router = APIRouter(prefix="/estanteria", tags=["Estanterías"])

@router.get("/deficiente")
def estanteria_deficiente():
    """Combinaciones de 4 libros > 8 kg (fuerza bruta)"""
    """
    Algoritmo de fuerza bruta:
    - Todas las combinaciones de 4 libros cuyo peso > 8kg
    """
    return EstanteriaController.estanteria_deficiente()


@router.get("/optima")
def estanteria_optima():
    """Mejor combinación por valor sin exceder 8 kg (backtracking)"""
    """
    Algoritmo de backtracking:
    - Combina libros para maximizar el valor total
    - Sin exceder peso de 8kg
    """
    return EstanteriaController.estanteria_optima()
