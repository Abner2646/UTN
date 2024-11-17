#Path: modelos/repositorios

'''Crear los archivos que gestionen las
colecciones de objetos de las clases declaradas en el punto anterior. Son las
clases que cargan los datos en memoria y gestionan los datos almacenados en
los archivos, y el archivo “repositorios.py” que declara una variable para cada
clase de repositorio y contiene una función que se encarga de inicializar los
repositorios en esas variables cuando inicia la aplicación.'''

#from modelos.entidades.libro import Libro
#Clase añadida manualmente porque no me la dejaba importar
class Libro:
    @staticmethod
    def fromDic(cls, data:dict) -> Libro:
        return Libro(data["titulo"], data["autor"], data["genero"], data["anio"], data["isbnos"])


    def __init__(self, titulo:str, autor:str, genero:str, anio:int, isbn:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio = anio
        self.__isbn = isbn

    
    #Consultar triviales:
    def obtenerTitulo(self):
        return self.__titulo
    
    def obtenerAutor(self):
        return self.__autor
    
    def obtenerGenero(self):
        return self.__genero
    
    def obtenerAnio(self):
        return self.__anio
    
    def obtenerISBN(self):
        return self.__isbn


    #Comandos triviales:
    def establecerNombre(self, titulo:str):
        self.__titulo = titulo

    def establecerAutor(self, autor:str):
        self.__autor = autor

    def establecerGenero(self, genero:str):
        self.__genero = genero

    def establecerAnio(self, anio:int):
        self.__anio = anio

    def establecerISBN(self, isbn:int):
        self.__isbn = isbn

    #Otros metodos:
    def esIgual(self, otro:'Libro') -> bool:
        return self.__titulo == otro.__titulo and self.__autor == otro.__autor and self.__genero == otro.__genero and self.__anio == otro.__anio and self.__isbn == otro.__isbn

    def toString(self) -> str:
        return f"Libro: {self.__titulo}, Autor: {self.__autor}, Genero: {self.__genero}, Año: {self.__anio}, ISBN: {self.__isbn}"

    def toDic(self) -> dict:
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "anio": self.__anio,
            "isbnos": self.__isbn
        }


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

