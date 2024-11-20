import json
from datetime import datetime
from modelos.entidades.socio import Socio

class RepositorioSocios:
    def __init__(self): #Estandarizar constructor
        self.socios = []
        self.cargarTodos() 

    def repositorioSocios(self): #Estandarizar esto
        try:
            with open('./socio.json', 'r', encoding='utf-8') as archivo:
                socio = json.load(archivo)
                for socio in socio:
                    self.socios.append(Socio.fromDiccionario(socio))
        except FileNotFoundError:
            pass

    def guardarTodos(self):
        try:
            with open('./socio.json', 'w') as archivo:
                socios = [socio.toDiccionario() for socio in self.socios]
                json.dump(socios, archivo)
        except FileNotFoundError:
            return False
        
    def obtenerTodos(self) -> list:
        return self.socios
    
    def existe(self, socio:'Socio') -> bool:
        return socio in self.socios
    
    def existeDNI(self, dni:int) -> bool:
        return any(socio.dni == dni for socio in self.socios)
    
    def agregar(self, nuevoSocio:'Socio'):
        if not self.existe(nuevoSocio):
            self.socios.append(nuevoSocio)
            self.guardarTodos()

    def modificarPorDni(self, dni:int, nombre:str, apellido:str, mail:str, fecha_nacimiento:datetime):
        for socio in self.socios:
            if socio.dni == dni:
                socio.nombre = nombre
                socio.apellido = apellido
                socio.mail = mail
                socio.fecha_nacimiento = fecha_nacimiento
                self.guardarTodos()

    def eliminarPorDni(self, dni:int):
        for socio in self.socios:
            if socio.dni == dni:
                self.socios.remove(socio)
                self.guardarTodos()

