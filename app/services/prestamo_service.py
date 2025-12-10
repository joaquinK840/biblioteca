import csv
import os
from datetime import date
from typing import List, Optional

from app.models.libro_model import Libro
from app.models.prestamo_model import Prestamo
from app.services.libro_service import LibroService
from app.services.reserva_service import \
    ReservaService  # to process reservations
from app.services.user_service import UsuarioService
from app.utils.structures.pila import Pila
from app.utils.libros.inventario import Inventario

CSV_PATH = "app/db/data/prestamos.csv"


# Loan service: CRUD, returns, and history (Stack)
class PrestamoService:
    """Service for loan management.

    Provides CRUD over prestamos.csv and utilities such as history (Stack)
    and return registration that affects book stock and reservations.
    """

    @staticmethod
    # Create the CSV if it doesn't exist (including headers)
    def _ensure_file_exists():
        """Create the loans CSV file if it does not exist.

        Parameters: none.
        Returns: None (side effect: creates file with header).
        """
        if not os.path.exists(CSV_PATH):
            with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        "prestamo_id",
                        "user_id",
                        "isbn",
                        "fecha_prestamo",
                        "fecha_devolucion",
                        "devuelto",
                    ]
                )

    @staticmethod
    # Read all loans from CSV and return the list
    def cargar_prestamos() -> List[Prestamo]:
        """Read all loans from the CSV and return a list of Prestamo.

        Parameters: none.
        Returns: List[Prestamo].
        """
        PrestamoService._ensure_file_exists()
        prestamos: List[Prestamo] = []
        with open(CSV_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                prestamos.append(
                    Prestamo(
                        prestamo_id=row["prestamo_id"],
                        user_id=row["user_id"],
                        isbn=row["isbn"],
                        fecha_prestamo=row["fecha_prestamo"],
                        fecha_devolucion=row["fecha_devolucion"] or None,
                        devuelto=row["devuelto"],
                    )
                )
        return prestamos

    @staticmethod
    # Overwrite the CSV with the provided loans list
    def guardar_prestamos(prestamos: List[Prestamo]):
        """Overwrite the loans CSV with the given list.

        Parameters:
        - prestamos: List[Prestamo]
        Returns: None (side effect: writes file).
        """
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = [
                "prestamo_id",
                "user_id",
                "isbn",
                "fecha_prestamo",
                "fecha_devolucion",
                "devuelto",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for p in prestamos:
                writer.writerow(p.__dict__)

    @staticmethod
    # Generate a new sequential ID based on existing ones
    def _generar_id(prestamos: List[Prestamo]) -> str:
        """Generate a new sequential ID for a loan based on the existing list.

        Parameters:
        - prestamos: current list of Prestamo
        Returns: str with the new id.
        """
        if not prestamos:
            return "1"
        ultimo = max(int(p.prestamo_id) for p in prestamos)
        return str(ultimo + 1)

    # CRUD básico

    @staticmethod
    # Return all loans
    def listar() -> List[Prestamo]:
        """Return all loans (list)."""
        return PrestamoService.cargar_prestamos()

    @staticmethod
    # Find a loan by ID, or None if it doesn't exist
    def obtener_por_id(prestamo_id: str) -> Optional[Prestamo]:
        """Find a loan by its prestamo_id.

        Parameters:
        - prestamo_id: str
        Returns: Prestamo or None.
        """
        for p in PrestamoService.cargar_prestamos():
            if p.prestamo_id == prestamo_id:
                return p
        return None

    @staticmethod
    # Create a loan if user/book exist and there's stock
    def crear(user_id: str, isbn: str) -> Optional[Prestamo]:
        """Create a new loan if user and book exist and there is stock.

        Parameters:
        - user_id: str
        - isbn: str
        Returns: Created Prestamo or None if it fails (user/book does not exist or out of stock).
        Effects: decrements book.stock and saves changes.
        """
        # Validate user
        if not UsuarioService.obtener_por_id(user_id):
            return None  # usuario no existe

        # Validate book and stock
        libro = LibroService.obtener_por_isbn(isbn)
        if not libro:
            return None  # libro no existe

        if libro.stock <= 0:
            # no hay stock, debería crearse una reserva
            return None

        prestamos = PrestamoService.cargar_prestamos()
        nuevo_id = PrestamoService._generar_id(prestamos)

        nuevo = Prestamo(
            prestamo_id=nuevo_id,
            user_id=user_id,
            isbn=isbn,
            fecha_prestamo=str(date.today()),
            fecha_devolucion=None,
            devuelto="0",
        )

        # decrease stock and save book
        libro.stock -= 1
        LibroService.actualizar(isbn, libro)

        prestamos.append(nuevo)
        PrestamoService.guardar_prestamos(prestamos)
        return nuevo

    @staticmethod
    # Register return: mark returned, set date, update stock and reservations
    def registrar_devolucion(prestamo_id: str) -> Optional[Prestamo]:
        """Register the return of a loan.

        Parameters:
        - prestamo_id: str
        Returns: Updated Prestamo or None if it does not exist.
        Effects:
        - marks as returned, updates fecha_devolucion, increases book stock,
          saves loans and triggers assignment of the next reservation.
        """
        prestamos = PrestamoService.cargar_prestamos()
        prestamo_encontrado = None

        for i, p in enumerate(prestamos):
            if p.prestamo_id == prestamo_id:
                prestamo_encontrado = p
                if p.devuelto == "1":
                    return p  # already returned
                p.devuelto = "1"
                p.fecha_devolucion = str(date.today())
                prestamos[i] = p
                break

        if not prestamo_encontrado:
            return None

        # increase book stock
        libro = LibroService.obtener_por_isbn(prestamo_encontrado.isbn)
        if libro:
            libro.stock += 1
            LibroService.actualizar(libro.isbn, libro)

        PrestamoService.guardar_prestamos(prestamos)

        # =====================
        # Binary search integration (Inventory ordered by ISBN)
        # =====================
        try:
            inventario = Inventario()
            # cargar todos los libros y mantener lista ordenada por inserción
            libros_actuales = LibroService.cargar_libros()
            for l in libros_actuales:
                inventario.agregar_libro(l)

            # buscar por ISBN en inventario ordenado
            libro_en_inventario = inventario.buscar_binaria(prestamo_encontrado.isbn)

            # si se encuentra, procedemos a verificar/atender reservas FIFO
            if libro_en_inventario is not None:
                ReservaService.asignar_siguiente_reserva(prestamo_encontrado.isbn)
            else:
                # si no se encuentra, no asignamos reserva (consistencia del inventario)
                # En un escenario real, se podría loguear/alertar; aquí mantenemos silencioso
                pass
        except Exception:
            # en caso de cualquier error en la fase de verificación binaria,
            # mantenemos el flujo original para no bloquear la devolución
            ReservaService.asignar_siguiente_reserva(prestamo_encontrado.isbn)

        return prestamo_encontrado

    @staticmethod
    # Delete a loan by ID; True if removed
    def eliminar(prestamo_id: str) -> bool:
        """Delete a loan by id.

        Parameters:
        - prestamo_id: str
        Returns: True if deleted, False if not found.
        """
        prestamos = PrestamoService.cargar_prestamos()
        nuevos = [p for p in prestamos if p.prestamo_id != prestamo_id]
        if len(nuevos) == len(prestamos):
            return False
        PrestamoService.guardar_prestamos(nuevos)
        return True

    # 🔹 Loan history per user using Stack (project requirement)

    @staticmethod
    # Build a Stack with a user's chronological loan history
    def historial_por_usuario(user_id: str) -> Pila:
        """Build and return a Stack with a user's loan history.

        Parameters:
        - user_id: str
        Returns: Stack with Prestamo objects pushed chronologically.
        """
        prestamos = PrestamoService.cargar_prestamos()
        pila = Pila()
        # push in chronological order
        prestamos_usuario = [
            p for p in prestamos if p.user_id == user_id
        ]
        prestamos_usuario.sort(key=lambda p: p.fecha_prestamo)
        for p in prestamos_usuario:
            pila.push(p)
        return pila
