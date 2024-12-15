''''Crear clases que funcionen como repositorio de objetos, es decir, cada clase entidad
tendrá una clase repositorio que manipule una colección de sus objetos.'''

from modelos.entidades.curso import Curso
from modelos.entidades.estudiante import Estudiante
from modelos.entidades.instructor import Instructor
import json

class RepoInstructores:
    PATH = "data/instructores.json"
    
    def __init__(self):
        self.instructores: list['Instructor'] = self.cargarInstructor()

    def cargarInstructor(self):
        """
        Metodo para cargar instructores al inicializarse el repositorio
        """
        lista: list['Instructor'] = []
        try:
            
            with open(RepoInstructores.PATH, 'r') as file:
                instructores_data = json.load(file)
                for instructor in instructores_data:
                    lista.append(Instructor.from_dict(instructor))

        except FileNotFoundError:
            print('No se encontró el archivo')

        return lista
    
    def guardarInstructor(self):
        try:
            lista = [instructor.to_dict() for instructor in self.instructores]
        
            with open(RepoInstructores.PATH, 'w') as file:
                json.dump(lista, file, indent=4)
                
        except FileNotFoundError:
            print('No se encontró el archivo')

    def getInstructores(self)->list['Instructor']:
        '''Devuelve una lista de instructores'''
        return self.instructores
    
    def getInstructorPorDni(self, dni:int)->Instructor:
        '''Devuelve un instructor'''
        for instructor in self.instructores:
            if instructor.get_dni() == dni:
                return instructor
    
    def existe(self, otroInstructor: Instructor)->bool:
        for instructor in self.instructores:
            if instructor == otroInstructor:
                return True
        return False
    
    def existeDni(self,dni: int)->bool:
        for instructor in self.instructores:
            if instructor.get_dni() == dni:
                return True
        return False
    
    def agregarInstructor(self, nuevoInstructor:Instructor):
        if not isinstance(nuevoInstructor, Instructor):
            raise ValueError('El objeto no es un instructor')
        if self.existe(nuevoInstructor):
            raise ValueError('El instructor ya existe')
        self.instructores.append(nuevoInstructor)
        self.guardarInstructor()

    def eliminarPorId(self, dni:int):
        for instructor in self.instructores:
            if instructor.get_dni() == dni:
                self.instructores.remove(instructor)
                self.guardarInstructor()
                return True
        return False
