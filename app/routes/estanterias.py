from fastapi import APIRouter
from app.controllers.estanteria_controller import EstanteriaController

router = APIRouter(prefix="/estanteria", tags=["Estanterías"])

@router.get("/deficiente")
def estanteria_deficiente():
    """
    Algoritmo de fuerza bruta:
    - Todas las combinaciones de 4 libros cuyo peso > 8kg
    """
    return EstanteriaController.estanteria_deficiente()


@router.get("/optima")
def estanteria_optima():
    """
    Algoritmo de backtracking:
    - Combina libros para maximizar el valor total
    - Sin exceder peso de 8kg
    """
    return EstanteriaController.estanteria_optima()
