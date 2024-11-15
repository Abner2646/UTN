#Path: modelos/repositorios

'''Crear los archivos que gestionen las
colecciones de objetos de las clases declaradas en el punto anterior. Son las
clases que cargan los datos en memoria y gestionan los datos almacenados en
los archivos, y el archivo “repositorios.py” que declara una variable para cada
clase de repositorio y contiene una función que se encarga de inicializar los
repositorios en esas variables cuando inicia la aplicación.'''

from modelos.entidades.libro import Libro

class RepositorioLibros:
    __libros__ = []

    def __init__(self):
        pass

    def repositorioLibro(self):
        pass

    #-
    def cargarTodos(self):
        pass

    #-
    def guardarTodos(self):
        pass

    def obtenerTodos(self) -> list:
        pass

    def existe(self, libro:'Libro') -> bool:
        pass

    def existeISBN(slef, isbn:int) -> bool:
        pass
    
    def agregarNuevo(self, nuevoLibro:'Libro'):
        pass

    def modificarPorISBN(self, isbn:int, titulo:str, autor:str, genero:str, anio:int):
        pass

    def eliminarPorISBN(self, isbn:int):
        pass

