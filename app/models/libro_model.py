# Represents a book in the catalog
class Libro:
    # Constructor: sets basic data and normalizes types
    def __init__(self, isbn, titulo, autor, peso, valor, stock, paginas, editorial, idioma):
        self.isbn = isbn            # Unique book identifier
        self.titulo = titulo        # Book title
        self.autor = autor          # Author(s)
        self.peso = float(peso)     # Weight in kg (float)
        self.valor = int(valor)     # Price/value (int)
        self.stock = int(stock)     # Available units (int)
        self.paginas = int(paginas) # Number of pages (int)
        self.editorial = editorial  # Publisher
        self.idioma = idioma        # Language
        