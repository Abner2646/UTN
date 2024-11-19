class Libro:
    def __init__(self, isbn: int, titulo: str, autor: str, genero: str, anio_publicacion: int, cantidad_ejemplares: int):
        if not isinstance(isbn, int):
            raise ValueError("ISBN debe ser un entero.")
        if not isinstance(titulo, str):
            raise ValueError("Título debe ser una cadena.")
        if not isinstance(autor, str):
            raise ValueError("Autor debe ser una cadena.")
        if not isinstance(genero, str):
            raise ValueError("Género debe ser una cadena.")
        if not isinstance(anio_publicacion, int):
            raise ValueError("Año de publicación debe ser un entero.")
        
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.cantidad_ejemplares = 0

    # Getters:
    def obtenerISBN(self) -> int:
        return self.isbn
    
    def obtenerTitulo(self) -> str:
        return self.titulo
    
    def obtenerAutor(self) -> str:
        return self.autor
    
    def obtenerGenero(self) -> str:
        return self.genero
    
    def obtenerAnioPublicacion(self) -> int:
        return self.anio_publicacion
    
    def obtenerCantidadEjemplares(self) -> int:
        return self.cantidad_ejemplares
    
    # Setters:
    def establecerISBN(self, isbn: int):
        if not isinstance(isbn, int):
            raise ValueError("ISBN debe ser un entero.")
        self.isbn = isbn

    def establecerTitulo(self, titulo: str):
        if not isinstance(titulo, str):
            raise ValueError("Título debe ser una cadena.")
        self.titulo = titulo

    def establecerAutor(self, autor: str):
        if not isinstance(autor, str):
            raise ValueError("Autor debe ser una cadena.")
        self.autor = autor

    def establecerGenero(self, genero: str):
        if not isinstance(genero, str):
            raise ValueError("Género debe ser una cadena.")
        self.genero = genero

    def establecerAnioPublicacion(self, anio_publicacion: int):
        if not isinstance(anio_publicacion, int):
            raise ValueError("Año de publicación debe ser un entero.")
        self.anio_publicacion = anio_publicacion

    def establecerCantidadEjemplares(self, cantidad_ejemplares: int):
        if not isinstance(cantidad_ejemplares, int):
            raise ValueError("Cantidad de ejemplares debe ser un entero.")
        self.cantidad_ejemplares = cantidad_ejemplares

    @classmethod
    def fromDic(cls, dic: dict) -> 'Libro':
        return cls(
            dic['isbn'],
            dic['titulo'],
            dic['autor'],
            dic['genero'],
            dic['anio_publicacion'],
            dic['cantidad_ejemplares']
        )

    def __str__(self) -> str:
        return f"Libro(ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año de Publicación: {self.anio_publicacion}, Cantidad de Ejemplares: {self.cantidad_ejemplares})"
    
    def to_dict(self) -> dict:
        return {
            'isbn': self.isbn,
            'titulo': self.titulo,
            'autor': self.autor,
            'genero': self.genero,
            'anio_publicacion': self.anio_publicacion,
            'cantidad_ejemplares': self.cantidad_ejemplares
        }
    
    def esIgual(self, otro):
        return self.isbn == otro.isbn
