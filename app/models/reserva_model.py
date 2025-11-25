class Reserva:
    def __init__(
        self,
        reserva_id: str,
        user_id: str,
        isbn: str,
        fecha_reserva: str,
    ):
        self.reserva_id = reserva_id
        self.user_id = user_id
        self.isbn = isbn
        self.fecha_reserva = fecha_reserva
