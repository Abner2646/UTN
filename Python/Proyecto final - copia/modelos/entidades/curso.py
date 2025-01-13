from .estudiante import Estudiante
from .instructor import Instructor

class Curso:
    def  __init__(self, id:int, nombre:str, descripcion:str, duracion:int):
        self.__id = id
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__duracion = duracion
        self.__instructor = None
        self.__estudiantes = []

    #GETTERS triviales:
    def get_id(self) -> int:
        return self.__id
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_descripcion(self) -> str:
        return self.__descripcion
    
    def get_duracion(self) -> int:
        return self.__duracion
    
    #SETTERS triviales:
    def set_id(self, id:int):
        if not isinstance(id, int):
            raise ValueError("El ID debe ser un dato de tipo entero.")
        self.__id = id

    def set_nombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un dato de tipo string.")
        self.__nombre = nombre

    def set_descripcion(self, descripcion:str):
        if not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser un dato de tipo string.")
        self.__descripcion = descripcion

    def set_duracion(self, duracion:int):
        if not isinstance(duracion, int):
            raise ValueError("La duración debe ser un dato de tipo entero.")
        self.__duracion = duracion

    #Otros metodos:
    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "descripcion": self.__descripcion,
            "duracion": self.__duracion
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        if not isinstance(data, dict):
            raise ValueError("El dato debe ser un diccionario.")
        return cls(
            id=data["id"],
            nombre=data["nombre"],
            descripcion=data["descripcion"],
            duracion=data["duracion"]
        )

    def __str__(self):
        return f"ID: {self.__id}, Nombre: {self.__nombre}, Descripción: {self.__descripcion}, Duración: {self.__duracion} horas"
    