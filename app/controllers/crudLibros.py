# app/controllers/crudLibros.py
from fastapi import HTTPException

from app.models.libro_model import Libro
from app.schemas.libro_schema import LibroCreate, LibroOut, LibroUpdate
from app.services.libro_service import LibroService


# Controlador de libros: orquesta llamadas a LibroService y valida respuestas
class LibroController:

    @staticmethod
    # Lista todos los libros disponibles
    def listar_libros():
        """Listar todos los libros.

        Parámetros: ninguno.
        Retorna: List[Libro].
        """
        return LibroService.cargar_libros()

    @staticmethod
    # Obtiene un libro por ISBN o lanza 404 si no existe
    def obtener_libro(isbn: str):
        """Obtener un libro por ISBN.

        Parámetros:
        - isbn: str
        Retorna: Libro si existe.
        Lanza: HTTPException 404 si no se encuentra.
        """
        libro = LibroService.obtener_por_isbn(isbn)
        if not libro:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return libro

    @staticmethod
    # Crea un libro nuevo a partir del schema de entrada
    def crear_libro(data: LibroCreate):
        """Crear un libro nuevo.

        Parámetros:
        - data: LibroCreate
        Retorna: Libro creado.
        Lanza: HTTPException 400 si el ISBN ya existe.
        """
        libro = Libro(**data.dict())
        nuevo = LibroService.crear(libro)
        if not nuevo:
            raise HTTPException(status_code=400, detail="El ISBN ya existe")
        return nuevo

    @staticmethod
    # Actualiza un libro por ISBN con los datos del schema
    def actualizar_libro(isbn: str, data: LibroUpdate):
        """Actualizar un libro por ISBN.

        Parámetros:
        - isbn: str
        - data: LibroUpdate
        Retorna: Libro actualizado.
        Lanza: HTTPException 404 si no se encuentra.
        """
        libro_actualizado = Libro(
            isbn=isbn,
            **data.dict()
        )
        actualizado = LibroService.actualizar(isbn, libro_actualizado)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return actualizado

    @staticmethod
    # Elimina un libro por ISBN; retorna mensaje de éxito
    def eliminar_libro(isbn: str):
        """Eliminar un libro por ISBN.

        Parámetros:
        - isbn: str
        Retorna: dict con mensaje de éxito.
        Lanza: HTTPException 404 si no se encuentra.
        """
        eliminado = LibroService.eliminar(isbn)
        if not eliminado:
            raise HTTPException(status_code=404, detail="Libro no encontrado")
        return {"message": "Libro eliminado"}
    
    @staticmethod
    # Devuelve libros ordenados por ISBN (insertion sort)
    def libros_ordenados_isbn():
        """Devolver libros ordenados por ISBN.

        Parámetros: ninguno.
        Retorna: lista ordenada o HTTPException 404 si no hay libros.
        """
        libros = LibroService.ordernar_por_isbn()
        if not libros:
            raise HTTPException(status_code=404, detail="No hay libros para ordenar")
        return libros
    
    @staticmethod
    # Devuelve libros ordenados por precio/valor (merge sort)
    def libros_ordenados_precio():
        """Devolver libros ordenados por precio/valor.

        Parámetros: ninguno.
        Retorna: lista ordenada o HTTPException 404 si no hay libros.
        """
        libros = LibroService.obtener_por_precio()
        if not libros:
            raise HTTPException(status_code=404, detail="No hay libros para ordenar")
        return libros
    
    @staticmethod
    # Devuelve combinaciones deficientes (fuerza bruta)
    def estanteria_deficiente():
        """Detectar combinaciones deficientes (fuerza bruta).

        Parámetros: ninguno.
        Retorna: lista de combinaciones o HTTPException 404 si no hay datos.
        """
        libros = LibroService.estanteria_deficiente()
        if not libros:
            raise HTTPException(status_code=404, detail="No hay libros para organizar")
        return libros
    
    @staticmethod
    # Devuelve estanterías óptimas (backtracking) adaptadas al schema
    def estanteria_optima():    
        """Calcular y devolver estanterías óptimas (backtracking).

        Parámetros: ninguno.
        Retorna: EstanteriasOptimasResponse o HTTPException 404 si no hay datos.
        """
        libros = LibroService.estanteria_optima()
        if not libros:
            raise HTTPException(status_code=404, detail="No hay libros para organizar")
        return libros
    
    @staticmethod
    # Suma de valor de libros por autor (recursión tipo pila)
    def valor_total_autor(autor: str):
        """Calcular valor total de libros de un autor.

        Parámetros:
        - autor: str
        Retorna: dict con 'autor', 'valor_total' y 'libros' o HTTPException 404 si no hay coincidencias.
        """
        resultado = LibroService.valor_total_por_autor(autor)
        if resultado is None:
            raise HTTPException(status_code=404, detail="Autor no encontrado")
        return {"autor": autor, **resultado}

    @staticmethod
    # Promedio de peso de libros por autor (tail recursion)
    def peso_promedio_autor(autor: str):
        """Calcular peso promedio de libros de un autor.

        Parámetros:
        - autor: str
        Retorna: dict con 'autor', 'peso_promedio' y 'libros' o HTTPException 404 si no hay coincidencias.
        """
        resultado = LibroService.peso_promedio_por_autor(autor)
        if resultado is None:
            raise HTTPException(status_code=404, detail="Autor no encontrado")
        return {"autor": autor, **resultado}

    @staticmethod
    # Búsqueda lineal de libros por título/autor en inventario general
    def buscar_lineal(texto: str):
        """Búsqueda lineal por título o autor en inventario general.

        Parámetros:
        - texto: str (consulta)
        Retorna: List[Libro] o HTTPException 404 si no hay coincidencias.
        """
        resultados = LibroService.buscar_lineal(texto)
        if not resultados:
            raise HTTPException(status_code=404, detail="Sin coincidencias para la búsqueda")
        return resultados
