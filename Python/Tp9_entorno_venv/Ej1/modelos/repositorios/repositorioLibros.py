import json #E
from modelos.entidades.libro import Libro

class RepositorioLibros():
    ruta_json = r'C:/Users/Abner/Desktop/UTN1/Python/Tp9_entorno_venv/Ej1/datos/libros.json' ##!!??

    def __init__(self): #Esto queda estandarizado
        self.lista = []
        self.cargar_todos()

    def cargar_todos(self):
        try:
            with open(self.ruta_json, "r", encoding='utf-8') as archivo:
                libros = json.load(archivo) #Ojo con el nombre de la variable
                for libro in libros: #Ojo con el nombre de la variable
                    self.lista.append(Libro.fromDic(libro)) #Ojo con el nombre de la Clase
        except FileNotFoundError:
            return []

    def guardar_todos(self):
        lista = [libro.to_dict() for libro in self.lista] #Las dos variables iguales
        with open(self.ruta_json, "w") as archivo:
            json.dump(lista, archivo)

    def obtener_todos(self):
        return self.lista
    
    def existe(self, isbn: int) -> bool:
        return any(libro.obtenerISBN() == isbn for libro in self.lista)

    
    def existeISBN(self, ISBN:int) -> bool:
        for libro in self.lista:
            if libro.isbn == ISBN:
                return True
        return False
    
    def agregar(self, libro:'Libro'):
        if self.existe(libro):
            raise Exception("El libro ya existe") #Ojo con los comentarios
        self.lista.append(libro)
        self.guardar_todos()

    def eliminar(self, libro:'Libro'):
        if not self.existe(libro):
            raise Exception("El socio no existe")
        self.lista.remove(libro)
        self.guardar_todos()

    def modificar(self, isbn:int, titulo:str, autor:str, genero:str, anio_publicacion:int, cantidad_ejemplares:int):
        for libro in self.lista:
            if libro.obtenerISBN == isbn:
                libro.titulo = titulo
                libro.autor = autor
                libro.genero = genero
                libro.anio_publicacion = anio_publicacion
                libro.cantidad_ejemplares = cantidad_ejemplares
                self.guardar_todos()
                return
