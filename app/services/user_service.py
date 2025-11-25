import csv
import os
from typing import List, Optional
from app.models.user_model import Usuario

CSV_PATH = "app/db/data/usuarios.csv"

class UsuarioService:

    @staticmethod
    def _ensure_file_exists():
        """Crear archivo si no existe"""
        if not os.path.exists(CSV_PATH):
            with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["user_id", "nombre", "correo", "telefono"])

    @staticmethod
    def cargar_usuarios() -> List[Usuario]:
        UsuarioService._ensure_file_exists()
        usuarios = []
        with open(CSV_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                usuarios.append(Usuario(**row))
        return usuarios

    @staticmethod
    def guardar_usuarios(usuarios: List[Usuario]):
        with open(CSV_PATH, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["user_id", "nombre", "correo", "telefono"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for u in usuarios:
                writer.writerow(u.__dict__)

    @staticmethod
    def obtener_por_id(user_id: str) -> Optional[Usuario]:
        for u in UsuarioService.cargar_usuarios():
            if u.user_id == user_id:
                return u
        return None

    @staticmethod
    def crear(usuario: Usuario):
        usuarios = UsuarioService.cargar_usuarios()

        # evitar duplicados
        if any(u.user_id == usuario.user_id for u in usuarios):
            return None

        usuarios.append(usuario)
        UsuarioService.guardar_usuarios(usuarios)
        return usuario

    @staticmethod
    def actualizar(user_id: str, data: Usuario):
        usuarios = UsuarioService.cargar_usuarios()
        for i, u in enumerate(usuarios):
            if u.user_id == user_id:
                usuarios[i] = data
                UsuarioService.guardar_usuarios(usuarios)
                return data
        return None

    @staticmethod
    def eliminar(user_id: str):
        usuarios = UsuarioService.cargar_usuarios()
        nuevos = [u for u in usuarios if u.user_id != user_id]
        if len(nuevos) == len(usuarios):
            return False
        UsuarioService.guardar_usuarios(nuevos)
        return True
