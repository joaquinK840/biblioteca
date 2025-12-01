from fastapi import HTTPException
from app.schemas.libro_schema import LibroCreate, LibroUpdate, LibroOut
from app.models.libro_model import Libro
from app.services.libro_service import LibroService

class LibroController:

    @staticmethod
    def listar_libros():
        return LibroService.cargar_libros()

    @staticmethod
    def obtener_libro(isbn: str):
        libro = LibroService.obtener_por_isbn(isbn)
        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return libro

    @staticmethod
    def crear_libro(data: LibroCreate):
        libro = Libro(**data.dict())
        nuevo = LibroService.crear(libro)
        if not nuevo:
            raise HTTPException(status_code=400, detail="El ISBN ya existe")
        return nuevo

    @staticmethod
    def actualizar_libro(isbn: str, data: LibroUpdate):
        libro_actualizado = Libro(
            isbn=isbn,
            **data.dict()
        )
        actualizado = LibroService.actualizar(isbn, libro_actualizado)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return actualizado

    @staticmethod
    def eliminar_libro(isbn: str):
        eliminado = LibroService.eliminar(isbn)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return {"message": "Libro eliminado"}
    
    @staticmethod
    def libros_ordenados_isbn():
        libros = LibroService.ordernar_por_isbn()
        if not libros:
            raise HTTPException(status_code=404, detail="No hay libros para ordenar")
        return libros
    
    @staticmethod
    def libros_ordenados_precio():
        libros = LibroService.obtener_por_precio()
        if not libros:
            raise HTTPException(status_code=404, detail="No hay libros para ordenar")
        return libros
    
    @staticmethod
    def estanteria_deficiente():
        libros = LibroService.estanteria_deficiente()
        if not libros:
            raise HTTPException(status_code=404, detail="No hay libros para organizar")
        return libros
    
    @staticmethod
    def estanteria_optima():    
        libros = LibroService.estanteria_optima()
        if not libros:
            raise HTTPException(status_code=404, detail="No hay libros para organizar")
        return libros