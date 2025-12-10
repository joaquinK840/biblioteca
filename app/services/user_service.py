import csv
import os
from typing import List, Optional

from app.models.user_model import Usuario

CSV_PATH = "app/db/data/usuarios.csv"

# User service: CSV-based CRUD
class UsuarioService:

    @staticmethod
    # Create the CSV if it doesn't exist (with header)
    def _ensure_file_exists():
        """Create the CSV file if it does not exist.
        
        Parameters: none.
        Returns: None. (side effect: creates the file with header if missing)
        """
        if not os.path.exists(CSV_PATH):
            with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["user_id", "nombre", "correo", "telefono"])

    @staticmethod
    # Read all users from CSV and return the list
    def cargar_usuarios() -> List[Usuario]:
        """Load all users from the CSV.

        Parameters: none.
        Returns: list of Usuario (may be empty).
        """
        UsuarioService._ensure_file_exists()
        usuarios = []
        with open(CSV_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                usuarios.append(Usuario(**row))
        return usuarios

    @staticmethod
    # Overwrite the CSV with the provided users list
    def guardar_usuarios(usuarios: List[Usuario]):
        """Save the complete users list to the CSV (overwrites).

        Parameters:
        - usuarios: List[Usuario] to serialize.
        Returns: None (side effect: writes the file).
        """
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["user_id", "nombre", "correo", "telefono"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for u in usuarios:
                writer.writerow(u.__dict__)

    @staticmethod
    # Find a user by ID, or None if it doesn't exist
    def obtener_por_id(user_id: str) -> Optional[Usuario]:
        """Find a user by their user_id.

        Parameters:
        - user_id: user identifier (str).
        Returns: Usuario if found, otherwise None.
        """
        for u in UsuarioService.cargar_usuarios():
            if u.user_id == user_id:
                return u
        return None

    @staticmethod
    # Create a user if there's no duplicate user_id
    def crear(usuario: Usuario):
        """Create a new user if there is no other with the same user_id.

        Parameters:
        - usuario: Usuario instance to create.
        Returns: the created Usuario or None if a duplicate already exists.
        """
        usuarios = UsuarioService.cargar_usuarios()

        # avoid duplicates
        if any(u.user_id == usuario.user_id for u in usuarios):
            return None

        usuarios.append(usuario)
        UsuarioService.guardar_usuarios(usuarios)
        return usuario

    @staticmethod
    # Update the user with that ID using provided data
    def actualizar(user_id: str, data: Usuario):
        """Update a user identified by user_id with the provided data.

        Parameters:
        - user_id: id of the user to update.
        - data: Usuario instance with the new data.
        Returns: Updated Usuario or None if it does not exist.
        """
        usuarios = UsuarioService.cargar_usuarios()
        for i, u in enumerate(usuarios):
            if u.user_id == user_id:
                usuarios[i] = data
                UsuarioService.guardar_usuarios(usuarios)
                return data
        return None

    @staticmethod
    # Delete by ID; returns True if found and removed
    def eliminar(user_id: str):
        """Delete a user by user_id.

        Parameters:
        - user_id: id of the user to delete.
        Returns: True if deleted, False if not found.
        """
        usuarios = UsuarioService.cargar_usuarios()
        nuevos = [u for u in usuarios if u.user_id != user_id]
        if len(nuevos) == len(usuarios):
            return False
        UsuarioService.guardar_usuarios(nuevos)
        return True
