# app/models/libro2_model.py

class Libro2:
    def __init__(self, isbn, titulo, autor, peso, valor, stock, paginas, editorial, idioma):
        # Copy all fields same as Libro
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.peso = float(peso)
        self.valor = int(valor)
        self.stock = int(stock)
        self.paginas = int(paginas)
        self.editorial = editorial
        self.idioma = idioma

        # Add the new column here
        self.estanteria = 0   # default: unassigned
