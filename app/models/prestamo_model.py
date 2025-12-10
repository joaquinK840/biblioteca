# Clase que representa un préstamo de un libro a un usuario
class Prestamo:
    # Constructor: crea un préstamo con identificadores y fechas
    def __init__(
        self,
        prestamo_id: str,
        user_id: str,
        isbn: str,
        fecha_prestamo: str,
        fecha_devolucion: str | None = None,
        devuelto: str = "0",
    ):
        self.prestamo_id = prestamo_id  # ID único del préstamo
        self.user_id = user_id          # ID del usuario que toma el libro
        self.isbn = isbn                # ISBN del libro prestado
        self.fecha_prestamo = fecha_prestamo  # Fecha en que se presta
        self.fecha_devolucion = fecha_devolucion  # Fecha de devolución (puede ser None)
        # Estado de devolución: "0" no devuelto, "1" devuelto (para CSV)
        self.devuelto = devuelto
