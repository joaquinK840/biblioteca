import csv
import os
from datetime import date
from typing import List, Optional

from app.models.libro_model import Libro
from app.models.prestamo_model import Prestamo
from app.services.libro_service import LibroService
from app.services.reserva_service import \
    ReservaService  # para procesar reservas
from app.services.user_service import UsuarioService
from app.utils.structures.pila import Pila
from app.utils.libros.inventario import Inventario

CSV_PATH = "app/db/data/prestamos.csv"


# Servicio de préstamos: CRUD, devoluciones y historial (Pila)
class PrestamoService:
    """Servicio para gestión de préstamos.

    Provee CRUD sobre prestamos.csv y utilidades como historial (Pila)
    y registro de devoluciones que afectan el stock y reservas.
    """

    @staticmethod
    # Crea el CSV si no existe (cabeceras incluidas)
    def _ensure_file_exists():
        """Crear el archivo CSV de préstamos si no existe.

        Parámetros: ninguno.
        Retorna: None (efecto lateral: crea archivo con cabecera).
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
    # Lee todos los préstamos del CSV y retorna la lista
    def cargar_prestamos() -> List[Prestamo]:
        """Leer todos los préstamos desde el CSV y devolver una lista de Prestamo.

        Parámetros: ninguno.
        Retorna: List[Prestamo].
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
    # Sobrescribe el CSV con la lista de préstamos proporcionada
    def guardar_prestamos(prestamos: List[Prestamo]):
        """Sobrescribir el CSV de préstamos con la lista dada.

        Parámetros:
        - prestamos: List[Prestamo]
        Retorna: None (efecto lateral: escribe archivo).
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
    # Genera un ID secuencial nuevo basado en los existentes
    def _generar_id(prestamos: List[Prestamo]) -> str:
        """Generar un nuevo ID secuencial para un préstamo a partir de la lista existente.

        Parámetros:
        - prestamos: lista actual de Prestamo
        Retorna: str con el nuevo id.
        """
        if not prestamos:
            return "1"
        ultimo = max(int(p.prestamo_id) for p in prestamos)
        return str(ultimo + 1)

    # CRUD básico

    @staticmethod
    # Devuelve todos los préstamos
    def listar() -> List[Prestamo]:
        """Devolver todos los préstamos (lista)."""
        return PrestamoService.cargar_prestamos()

    @staticmethod
    # Busca un préstamo por su ID, o None si no existe
    def obtener_por_id(prestamo_id: str) -> Optional[Prestamo]:
        """Buscar un préstamo por su prestamo_id.

        Parámetros:
        - prestamo_id: str
        Retorna: Prestamo o None.
        """
        for p in PrestamoService.cargar_prestamos():
            if p.prestamo_id == prestamo_id:
                return p
        return None

    @staticmethod
    # Crea un préstamo si usuario y libro existen y hay stock
    def crear(user_id: str, isbn: str) -> Optional[Prestamo]:
        """Crear un nuevo préstamo si usuario y libro existen y hay stock.

        Parámetros:
        - user_id: str
        - isbn: str
        Retorna: Prestamo creado o None si falla (usuario/libro no existe o sin stock).
        Efectos: decrementa book.stock y guarda cambios.
        """
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
    # Registra devolución: marca devuelto, fecha, actualiza stock y reservas
    def registrar_devolucion(prestamo_id: str) -> Optional[Prestamo]:
        """Registrar la devolución de un préstamo.

        Parámetros:
        - prestamo_id: str
        Retorna: Prestamo actualizado o None si no existe.
        Efectos:
        - marca devuelto, actualiza fecha_devolucion, incrementa stock del libro,
          guarda préstamos y dispara asignación de siguiente reserva.
        """
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

        # =====================
        # Integración búsqueda binaria (Inventario ordenado por ISBN)
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
    # Elimina un préstamo por ID; True si lo borró
    def eliminar(prestamo_id: str) -> bool:
        """Eliminar un préstamo por id.

        Parámetros:
        - prestamo_id: str
        Retorna: True si se eliminó, False si no se encontró.
        """
        prestamos = PrestamoService.cargar_prestamos()
        nuevos = [p for p in prestamos if p.prestamo_id != prestamo_id]
        if len(nuevos) == len(prestamos):
            return False
        PrestamoService.guardar_prestamos(nuevos)
        return True

    # 🔹 Historial de préstamos por usuario usando Pila (requisito del proyecto)

    @staticmethod
    # Construye una Pila con el historial cronológico de un usuario
    def historial_por_usuario(user_id: str) -> Pila:
        """Construir y devolver una Pila con el historial de préstamos de un usuario.

        Parámetros:
        - user_id: str
        Retorna: Pila con objetos Prestamo apilados cronológicamente.
        """
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
