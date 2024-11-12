'''Crea una clase Libro que contenga los atributos de tipo elemental (titulo, autor y género de
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
    @classmethod
    def fromDiccionario(self, data:dict):  #Retorna un objeto de tipo Direccion con los valores pasados en el parametro "data"
        return Libro(data["titulo"], data["autor"], data["genero"], data["anio"], data["ISBN"])

    def __init__(self, titulo:str, autor:str, genero:str, anio:int, ISBN:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anio = anio
        self.__ISBN = ISBN

    def toDiccionario(self): #Retorna un diccionario con los valores de instancia
        return {"titulo":self.__titulo, "autor":self.__autor, "genero":self.__genero, "anio":self.__anio, "ISBN":self.__ISBN}

    def to_json(self):
        """
        Metodo que convierte los datos del libro en un diccionario y luego en un json
        Returns:
            _type_: _description_
        """
        dicc = {
            'titulo': self.__titulo,
            'autor': self.__autor,
            'genero': self.__genero,
            'año_publicacion': self.__anio,
            'isbn': self.__ISBN
        }
        return json.dumps(dicc,ensure_ascii = False)


class Tester:
    @staticmethod
    def test():
        #Carga los datos del JSON en objetos de clase Libro


        #muestra por pantalla valores de los objetos de clase Libro.


class Tester:
    def cargarMostrar(self, libros_json):
            with open(libros_json, "r" ,encoding="utf-8") as archivo: #Lee "libros.json" y lo llama archivo | "archivo es de tipo json"
                data = json.load(archivo) #Carga el archivo en una variable "data" | "data" es de tipo diccionario
                for i in data:
                    print(i)
                    
    def buscarXaño(self, libros_json):
        #Pide un año al usuario y lo pasa a entero
        año = int(input("Ingrese el año: "))
        print(f"Libros encontrados por año {año}:")

        with open(libros_json, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)

            # Buscar libros que coincidan con el año
            for i in data:
                if 'año' in i and i['año'] == año:
                    print(i)
                
if _name_ == "_main_":
    libros_json = "c:/Users/AMDRYZEN7/Desktop/Programacion 2/PRACTICA/tp8/punto 1/libros.json"
    Tester().cargarMostrar(libros_json)
    Tester().buscarXaño(libros_json)