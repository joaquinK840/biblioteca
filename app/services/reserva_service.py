import csv
import os
from datetime import date
from typing import List, Optional

from app.models.reserva_model import Reserva
from app.services.libro_service import LibroService
from app.services.user_service import UsuarioService
from app.utils.structures.cola import Cola

CSV_PATH = "app/db/data/reservas.csv"


# Reservation service: CRUD and automatic assignment (FIFO)
class ReservaService:

    @staticmethod
    # Create the CSV if it doesn't exist (with header)
    def _ensure_file_exists():
        """Create the reservations CSV file if it does not exist.

        Parameters: none.
        Returns: None (side effect: creates file).
        """
        if not os.path.exists(CSV_PATH):
            with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["reserva_id", "user_id", "isbn", "fecha_reserva"])

    @staticmethod
    # Read all reservations from CSV and return the list
    def cargar_reservas() -> List[Reserva]:
        """Read all reservations from CSV and return a list of Reserva.

        Parameters: none.
        Returns: List[Reserva].
        """
        ReservaService._ensure_file_exists()
        reservas: List[Reserva] = []
        with open(CSV_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                reservas.append(
                    Reserva(
                        reserva_id=row["reserva_id"],
                        user_id=row["user_id"],
                        isbn=row["isbn"],
                        fecha_reserva=row["fecha_reserva"],
                    )
                )
        return reservas

    @staticmethod
    # Overwrite the CSV with the provided reservations list
    def guardar_reservas(reservas: List[Reserva]):
        """Save the complete reservations list to the CSV (overwrites).

        Parameters:
        - reservas: List[Reserva]
        Returns: None (side effect: writes file).
        """
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["reserva_id", "user_id", "isbn", "fecha_reserva"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for r in reservas:
                writer.writerow(r.__dict__)

    @staticmethod
    # Generate a new sequential ID based on existing reservations
    def _generar_id(reservas: List[Reserva]) -> str:
        """Generate a new sequential id for reservations.

        Parameters:
        - reservas: current list of Reserva
        Returns: new id as str.
        """
        if not reservas:
            return "1"
        ultimo = max(int(r.reserva_id) for r in reservas)
        return str(ultimo + 1)

    # CRUD básico

    @staticmethod
    # Return all reservations
    def listar() -> List[Reserva]:
        """Return all reservations."""
        return ReservaService.cargar_reservas()

    @staticmethod
    # Find a reservation by ID, or None if it doesn't exist
    def obtener_por_id(reserva_id: str) -> Optional[Reserva]:
        """Find reservation by reserva_id.

        Parameters:
        - reserva_id: str
        Returns: Reserva or None.
        """
        for r in ReservaService.cargar_reservas():
            if r.reserva_id == reserva_id:
                return r
        return None

    @staticmethod
    # Create a reservation only if user/book exist and stock is zero
    def crear(user_id: str, isbn: str) -> Optional[Reserva]:
        """Create a new reservation only if the user and book exist and there is no stock.

        Parameters:
        - user_id: str
        - isbn: str
        Returns: Created Reserva or None if creation is not valid.
        Effects: writes to CSV.
        """
        # Validar usuario
        if not UsuarioService.obtener_por_id(user_id):
            return None

        # Validar libro
        libro = LibroService.obtener_por_isbn(isbn)
        if not libro:
            return None

        # Only allow reservation if stock is 0 
        if libro.stock > 0:
            return None

        reservas = ReservaService.cargar_reservas()
        nuevo_id = ReservaService._generar_id(reservas)

        nueva = Reserva(
            reserva_id=nuevo_id,
            user_id=user_id,
            isbn=isbn,
            fecha_reserva=str(date.today()),
        )

        reservas.append(nueva)
        ReservaService.guardar_reservas(reservas)
        return nueva

    @staticmethod
    # Delete a reservation by ID; True if removed
    def eliminar(reserva_id: str) -> bool:
        """Delete a reservation by id.

        Parameters:
        - reserva_id: str
        Returns: True if deleted, False if it does not exist.
        """
        reservas = ReservaService.cargar_reservas()
        nuevas = [r for r in reservas if r.reserva_id != reserva_id]
        if len(nuevas) == len(reservas):
            return False
        ReservaService.guardar_reservas(nuevas)
        return True

    # 🔹 Reservations queue per book (FIFO), project requirement

    @staticmethod
    # Build a FIFO Queue with reservations for a given book
    def cola_por_libro(isbn: str) -> Cola:
        """Build and return a Queue (FIFO) with reservations for the given book.

        Parameters:
        - isbn: str
        Returns: Queue with Reserva objects in arrival order.
        """
        reservas = ReservaService.cargar_reservas()
        cola = Cola()
        reservas_libro = [r for r in reservas if r.isbn == isbn]
        # the order in the CSV is already the arrival order
        for r in reservas_libro:
            cola.enqueue(r)
        return cola

    @staticmethod
    # Assign the next reservation when a book is returned (FIFO)
    def asignar_siguiente_reserva(isbn: str):
        """Assign the next pending reservation when a book is returned.

        Parameters:
        - isbn: str
        Returns: Assigned Reserva or None if there are no reservations.
        Effects:
        - removes the reservation from CSV and automatically creates a loan for that user.
        """
        # Note: intentional local import to avoid circular dependency
        # between ReservaService and PrestamoService.
        from app.services.prestamo_service import PrestamoService

        reservas = ReservaService.cargar_reservas()
        reservas_libro = [r for r in reservas if r.isbn == isbn]

        if not reservas_libro:
            return None

        # FIFO: take the oldest reservation
        reservas_libro.sort(key=lambda r: r.fecha_reserva)
        siguiente = reservas_libro[0]

        # Remove it from the file
        nuevas = [r for r in reservas if r.reserva_id != siguiente.reserva_id]
        ReservaService.guardar_reservas(nuevas)

        # Automatically create a loan for the reservation's user
        PrestamoService.crear(siguiente.user_id, isbn)

        return siguiente
