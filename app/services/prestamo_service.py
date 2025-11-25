import csv
import os
from datetime import date
from typing import List, Optional

from app.models.prestamo_model import Prestamo
from app.models.libro_model import Libro
from app.services.libro_service import LibroService
from app.services.user_service import UsuarioService
from app.structures.pila import Pila
from app.services.reserva_service import ReservaService  # para procesar reservas

CSV_PATH = "app/db/data/prestamos.csv"


class PrestamoService:

    @staticmethod
    def _ensure_file_exists():
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
    def cargar_prestamos() -> List[Prestamo]:
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
    def guardar_prestamos(prestamos: List[Prestamo]):
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
    def _generar_id(prestamos: List[Prestamo]) -> str:
        if not prestamos:
            return "1"
        ultimo = max(int(p.prestamo_id) for p in prestamos)
        return str(ultimo + 1)

    # CRUD básico

    @staticmethod
    def listar() -> List[Prestamo]:
        return PrestamoService.cargar_prestamos()

    @staticmethod
    def obtener_por_id(prestamo_id: str) -> Optional[Prestamo]:
        for p in PrestamoService.cargar_prestamos():
            if p.prestamo_id == prestamo_id:
                return p
        return None

    @staticmethod
    def crear(user_id: str, isbn: str) -> Optional[Prestamo]:
        # Validar usuario
        if not UsuarioService.obtener_por_id(user_id):
            return None  # usuario no existe

        # Validar libro y stock
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

        # disminuir stock y guardar libro
        libro.stock -= 1
        LibroService.actualizar(isbn, libro)

        prestamos.append(nuevo)
        PrestamoService.guardar_prestamos(prestamos)
        return nuevo

    @staticmethod
    def registrar_devolucion(prestamo_id: str) -> Optional[Prestamo]:
        prestamos = PrestamoService.cargar_prestamos()
        prestamo_encontrado = None

        for i, p in enumerate(prestamos):
            if p.prestamo_id == prestamo_id:
                prestamo_encontrado = p
                if p.devuelto == "1":
                    return p  # ya estaba devuelto
                p.devuelto = "1"
                p.fecha_devolucion = str(date.today())
                prestamos[i] = p
                break

        if not prestamo_encontrado:
            return None

        # aumentar stock del libro
        libro = LibroService.obtener_por_isbn(prestamo_encontrado.isbn)
        if libro:
            libro.stock += 1
            LibroService.actualizar(libro.isbn, libro)

        PrestamoService.guardar_prestamos(prestamos)

        # Verificar reservas pendientes (cola) y asignar si hay
        ReservaService.asignar_siguiente_reserva(prestamo_encontrado.isbn)

        return prestamo_encontrado

    @staticmethod
    def eliminar(prestamo_id: str) -> bool:
        prestamos = PrestamoService.cargar_prestamos()
        nuevos = [p for p in prestamos if p.prestamo_id != prestamo_id]
        if len(nuevos) == len(prestamos):
            return False
        PrestamoService.guardar_prestamos(nuevos)
        return True

    # 🔹 Historial de préstamos por usuario usando Pila (requisito del proyecto)

    @staticmethod
    def historial_por_usuario(user_id: str) -> Pila:
        prestamos = PrestamoService.cargar_prestamos()
        pila = Pila()
        # apilamos en orden cronológico
        prestamos_usuario = [
            p for p in prestamos if p.user_id == user_id
        ]
        prestamos_usuario.sort(key=lambda p: p.fecha_prestamo)
        for p in prestamos_usuario:
            pila.push(p)
        return pila
