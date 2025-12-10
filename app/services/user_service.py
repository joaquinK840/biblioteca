import csv
import os
from typing import List, Optional

from app.models.user_model import Usuario

CSV_PATH = "app/db/data/usuarios.csv"

# Servicio de usuarios: CRUD sobre CSV
class UsuarioService:

    @staticmethod
    # Crea el CSV si no existe (cabecera incluida)
    def _ensure_file_exists():
        """Crear el archivo CSV si no existe.
        
        Parámetros: ninguno.
        Retorna: None. (efecto lateral: crea el archivo con cabecera si falta)
        """
        if not os.path.exists(CSV_PATH):
            with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["user_id", "nombre", "correo", "telefono"])

    @staticmethod
    # Lee todos los usuarios del CSV y retorna la lista
    def cargar_usuarios() -> List[Usuario]:
        """Cargar todos los usuarios desde el CSV.

        Parámetros: ninguno.
        Retorna: lista de Usuario (puede estar vacía).
        """
        UsuarioService._ensure_file_exists()
        usuarios = []
        with open(CSV_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                usuarios.append(Usuario(**row))
        return usuarios

    @staticmethod
    # Sobrescribe el CSV con la lista de usuarios proporcionada
    def guardar_usuarios(usuarios: List[Usuario]):
        """Guardar la lista completa de usuarios en el CSV (sobrescribe).

        Parámetros:
        - usuarios: List[Usuario] a serializar.
        Retorna: None (efecto lateral: escribe el archivo).
        """
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["user_id", "nombre", "correo", "telefono"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for u in usuarios:
                writer.writerow(u.__dict__)

    @staticmethod
    # Busca un usuario por su ID, o None si no existe
    def obtener_por_id(user_id: str) -> Optional[Usuario]:
        """Buscar un usuario por su user_id.

        Parámetros:
        - user_id: identificador del usuario (str).
        Retorna: Usuario si se encuentra, otherwise None.
        """
        for u in UsuarioService.cargar_usuarios():
            if u.user_id == user_id:
                return u
        return None

    @staticmethod
    # Crea un usuario si no hay duplicado de user_id
    def crear(usuario: Usuario):
        """Crear un nuevo usuario si no existe otro con el mismo user_id.

        Parámetros:
        - usuario: instancia Usuario a crear.
        Retorna: el Usuario creado o None si ya existe duplicado.
        """
        usuarios = UsuarioService.cargar_usuarios()

        # evitar duplicados
        if any(u.user_id == usuario.user_id for u in usuarios):
            return None

        usuarios.append(usuario)
        UsuarioService.guardar_usuarios(usuarios)
        return usuario

    @staticmethod
    # Actualiza el usuario con ese ID usando los datos dados
    def actualizar(user_id: str, data: Usuario):
        """Actualizar un usuario identificado por user_id con los datos proporcionados.

        Parámetros:
        - user_id: id del usuario a actualizar.
        - data: instancia Usuario con los nuevos datos.
        Retorna: Usuario actualizado o None si no existe.
        """
        usuarios = UsuarioService.cargar_usuarios()
        for i, u in enumerate(usuarios):
            if u.user_id == user_id:
                usuarios[i] = data
                UsuarioService.guardar_usuarios(usuarios)
                return data
        return None

    @staticmethod
    # Elimina por ID; retorna True si lo encontró y borró
    def eliminar(user_id: str):
        """Eliminar un usuario por user_id.

        Parámetros:
        - user_id: id del usuario a eliminar.
        Retorna: True si se eliminó, False si no se encontró.
        """
        usuarios = UsuarioService.cargar_usuarios()
        nuevos = [u for u in usuarios if u.user_id != user_id]
        if len(nuevos) == len(usuarios):
            return False
        UsuarioService.guardar_usuarios(nuevos)
        return True
