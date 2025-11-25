import csv
import os
from datetime import date
from typing import List, Optional

from app.models.reserva_model import Reserva
from app.services.libro_service import LibroService
from app.services.user_service import UsuarioService
from app.structures.cola import Cola

CSV_PATH = "app/db/data/reservas.csv"


class ReservaService:

    @staticmethod
    def _ensure_file_exists():
        if not os.path.exists(CSV_PATH):
            with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["reserva_id", "user_id", "isbn", "fecha_reserva"])

    @staticmethod
    def cargar_reservas() -> List[Reserva]:
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
    def guardar_reservas(reservas: List[Reserva]):
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["reserva_id", "user_id", "isbn", "fecha_reserva"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for r in reservas:
                writer.writerow(r.__dict__)

    @staticmethod
    def _generar_id(reservas: List[Reserva]) -> str:
        if not reservas:
            return "1"
        ultimo = max(int(r.reserva_id) for r in reservas)
        return str(ultimo + 1)

    # CRUD básico

    @staticmethod
    def listar() -> List[Reserva]:
        return ReservaService.cargar_reservas()

    @staticmethod
    def obtener_por_id(reserva_id: str) -> Optional[Reserva]:
        for r in ReservaService.cargar_reservas():
            if r.reserva_id == reserva_id:
                return r
        return None

    @staticmethod
    def crear(user_id: str, isbn: str) -> Optional[Reserva]:
        # Validar usuario
        if not UsuarioService.obtener_por_id(user_id):
            return None

        # Validar libro
        libro = LibroService.obtener_por_isbn(isbn)
        if not libro:
            return None

        # Solo permitir reserva si el stock es 0 (requisito del proyecto)
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
    def eliminar(reserva_id: str) -> bool:
        reservas = ReservaService.cargar_reservas()
        nuevas = [r for r in reservas if r.reserva_id != reserva_id]
        if len(nuevas) == len(reservas):
            return False
        ReservaService.guardar_reservas(nuevas)
        return True

    # 🔹 Cola de reservas por libro (FIFO), requisito del proyecto

    @staticmethod
    def cola_por_libro(isbn: str) -> Cola:
        reservas = ReservaService.cargar_reservas()
        cola = Cola()
        reservas_libro = [r for r in reservas if r.isbn == isbn]
        # el orden en el CSV ya es el orden de llegada
        for r in reservas_libro:
            cola.enqueue(r)
        return cola

    @staticmethod
    def asignar_siguiente_reserva(isbn: str):
        """
        Cuando un libro se devuelve, esta función se llama para ver si hay
        reservas pendientes. Si las hay, se toma la primera en la cola.
        La creación del nuevo préstamo se podría hacer aquí o en otro nivel.
        Aquí solo consumimos la reserva y dejamos listo el dato.
        """
        from app.services.prestamo_service import PrestamoService  # import local para evitar ciclo

        reservas = ReservaService.cargar_reservas()
        reservas_libro = [r for r in reservas if r.isbn == isbn]

        if not reservas_libro:
            return None

        # FIFO: tomamos la reserva más antigua
        reservas_libro.sort(key=lambda r: r.fecha_reserva)
        siguiente = reservas_libro[0]

        # Eliminarla del archivo
        nuevas = [r for r in reservas if r.reserva_id != siguiente.reserva_id]
        ReservaService.guardar_reservas(nuevas)

        # Crear préstamo automáticamente para el usuario de la reserva
        PrestamoService.crear(siguiente.user_id, isbn)

        return siguiente
