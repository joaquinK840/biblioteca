# Clase que representa una reserva de un libro por un usuario
class Reserva:
    # Constructor: crea una reserva con identificadores y fecha
    def __init__(
        self,
        reserva_id: str,
        user_id: str,
        isbn: str,
        fecha_reserva: str,
    ):
        self.reserva_id = reserva_id   # ID único de la reserva
        self.user_id = user_id         # ID del usuario que reserva
        self.isbn = isbn               # ISBN del libro reservado
        self.fecha_reserva = fecha_reserva  # Fecha en que se realiza la reserva
