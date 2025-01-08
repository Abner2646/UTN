''' Crea una clase Libro que contenga los atributos de tipo elemental (titulo, autor y género de
tipo string, año de publicación e ISBN de tipo entero) y que contenga métodos para
serializar/deserializar el objeto utilizando los métodos toDiccionario() y fromDiccionario(dic:
dict) vistos en clase.
Crea de forma manual un archivo JSON “libros.json” que contenga información de varios
libros (título, autor, género, año de publicación, ISBN) en formato JSON.
En la clase tester:
a. Carga los datos del JSON en objetos de clase Libro y muestra por pantalla valores
de los objetos de clase Libro.
b. Pedile al usuario un año de publicación para buscar todos los libros publicados ese
año, y mostrá por pantalla los resultados de la búsqueda.  '''

import json

class Libro:
    def __init__(self, titulo:str, autor:str, genero:str, anio:int, isbn:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio = anio
        self.__isbn = isbn

    @classmethod
    def fromDiccionario(self, data:dict) -> 'Libro':
        return Libro(data["titulo"], data["autor"], data["genero"], data["anio"], data["isbn"])
    
    def toDiccionario(self) -> dict:
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "genero": self.__genero,
            "anio": self.__anio,
            "isbn": self.__isbn
        }
    
class Tester:
    def test():
        #INCISO A----------------------
        #Importar el json
        libros_json = r"C:\Users\Abner\Desktop\UTN1\Python\Tp8\libros.json"
        with open(libros_json,"r" ,encoding="utf-8") as archivo: #Lee "libros.json" y lo llama archivo | "archivo es una variable de tipo json"
            data = json.load(archivo) #Carga el archivo en una variable "data" | "data" es de tipo diccionario
            for i in data.values(): #Itera sobre los valores del diccionario
                print(i)

        #INCISO B----------------------
        #Pedile al usuario un año de publicación para buscar todos los libros publicados ese año
        anioUsuario = int(input("Ingrese un anio: "))

        #Si anioUsuario es igual al año de publicación de uno de los libros mostrar lso valores del libro:
        '''for i in data.values(): #Itera sobre los valores del diccionario
            if i == anioUsuario:
                print(i) #Imprime el valor'''

        #Este ciclo itera sobre las claves
        for i in data:
            if data.get("anio") == anioUsuario:
                print(i)


if __name__ == "__main__":
    Tester.test()