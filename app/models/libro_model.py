# Clase que representa un libro del catálogo
class Libro:
    # Constructor: define datos básicos y normaliza tipos
    def __init__(self, isbn, titulo, autor, peso, valor, stock, paginas, editorial, idioma):
        self.isbn = isbn            # Identificador único del libro
        self.titulo = titulo        # Título del libro
        self.autor = autor          # Autor o autores
        self.peso = float(peso)     # Peso en kg (float)
        self.valor = int(valor)     # Precio/valor (int)
        self.stock = int(stock)     # Unidades disponibles (int)
        self.paginas = int(paginas) # Número de páginas (int)
        self.editorial = editorial  # Editorial
        self.idioma = idioma        # Idioma del libro
        