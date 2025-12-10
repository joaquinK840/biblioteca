# Represents a user in the system
class Usuario:
    # Constructor: creates a user with contact details
    def __init__(self, user_id, nombre, correo, telefono):
        self.user_id = user_id  # Unique user ID
        self.nombre = nombre    # Full name
        self.correo = correo    # Email address
        self.telefono = telefono  # Contact phone
