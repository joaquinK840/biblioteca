class Prestamo:
    def __init__(
        self,
        prestamo_id: str,
        user_id: str,
        isbn: str,
        fecha_prestamo: str,
        fecha_devolucion: str | None = None,
        devuelto: str = "0",
    ):
        self.prestamo_id = prestamo_id
        self.user_id = user_id
        self.isbn = isbn
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        # guardamos como "0"/"1" en CSV para que sea simple
        self.devuelto = devuelto
