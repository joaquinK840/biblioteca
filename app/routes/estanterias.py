from fastapi import APIRouter
from app.controllers.estanteria_controller import EstanteriaController

router = APIRouter(prefix="/estanteria", tags=["Estanterías"])

@router.get("/deficiente")
def estanteria_deficiente():
    """Combinations of 4 books > 8 kg (brute force)"""
    """
    Brute force algorithm:
    - All combinations of 4 books whose weight > 8 kg
    """
    return EstanteriaController.estanteria_deficiente()


@router.get("/optima")
def estanteria_optima():
    """Best value combination without exceeding 8 kg (backtracking)"""
    """
    Backtracking algorithm:
    - Combine books to maximize total value
    - Without exceeding 8 kg
    """
    return EstanteriaController.estanteria_optima()
