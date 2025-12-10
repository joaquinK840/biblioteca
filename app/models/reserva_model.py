# Represents a reservation of a book by a user
class Reserva:
    # Constructor: creates a reservation with identifiers and date
    def __init__(
        self,
        reserva_id: str,
        user_id: str,
        isbn: str,
        fecha_reserva: str,
    ):
        self.reserva_id = reserva_id   # Unique reservation ID
        self.user_id = user_id         # ID of the user reserving
        self.isbn = isbn               # ISBN of the reserved book
        self.fecha_reserva = fecha_reserva  # Date the reservation is made
