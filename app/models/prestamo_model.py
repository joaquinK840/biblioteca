# Represents a loan of a book to a user
class Prestamo:
    # Constructor: creates a loan with identifiers and dates
    def __init__(
        self,
        prestamo_id: str,
        user_id: str,
        isbn: str,
        fecha_prestamo: str,
        fecha_devolucion: str | None = None,
        devuelto: str = "0",
    ):
        self.prestamo_id = prestamo_id  # Unique loan ID
        self.user_id = user_id          # ID of the user borrowing the book
        self.isbn = isbn                # ISBN of the borrowed book
        self.fecha_prestamo = fecha_prestamo  # Loan date
        self.fecha_devolucion = fecha_devolucion  # Return date (may be None)
        # Return status: "0" not returned, "1" returned (CSV-friendly)
        self.devuelto = devuelto
