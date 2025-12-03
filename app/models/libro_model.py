class Libro:
    def __init__(self, isbn, titulo, autor, peso, valor, stock, paginas, editorial, idioma,estanteria):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.peso = float(peso)
        self.valor = int(valor)
        self.stock = int(stock)
        self.paginas = int(paginas)
        self.editorial = editorial
        self.idioma = idioma
        self.estanteria = int(estanteria)
