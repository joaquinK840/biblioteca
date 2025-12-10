# Clase que representa un usuario del sistema
class Usuario:
    # Constructor: crea un usuario con datos de contacto
    def __init__(self, user_id, nombre, correo, telefono):
        self.user_id = user_id  # ID único del usuario
        self.nombre = nombre    # Nombre completo
        self.correo = correo    # Correo electrónico
        self.telefono = telefono  # Teléfono de contacto
