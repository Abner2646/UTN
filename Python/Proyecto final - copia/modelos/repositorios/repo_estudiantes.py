''''Crear clases que funcionen como repositorio de objetos, es decir, cada clase entidad
tendrá una clase repositorio que manipule una colección de sus objetos.'''

from modelos.entidades.estudiante import Estudiante
import json

class RepoEstudiante:
    PATH = "data/estudiantes.json"
    
    def __init__(self):
        self.estudiantes: list['Estudiante'] = self.cargarEstudiante()


    def agregarEstudianteDesdeDict(self, datos_estudiante: dict):
        try:
            nuevo_estudiante = Estudiante.from_dict(datos_estudiante)
            self.agregarEstudiante(nuevo_estudiante)
        except ValueError as e:
            raise ValueError(f"Error al agregar estudiante: {e}")


    def cargarEstudiante(self):
        """
        Metodo para cargar estudiantes al inicializarse el repositorio
        """
        lista: list['Estudiante'] = []
        try:
            
            with open(RepoEstudiante.PATH, 'r') as file:
                estudiantes_data = json.load(file)
                for estudiante in estudiantes_data:
                    lista.append(Estudiante.from_dict(estudiante))
        except FileNotFoundError:
            print('No se encontró el archivo')
        return lista
    
    def guardarEstudiantes(self):
        try:
            lista = [estudiante.to_dict() for estudiante in self.estudiantes]
        
            with open(RepoEstudiante.PATH, 'w') as file:
                json.dump(lista, file, indent=4)
                
        except FileNotFoundError:
            print('No se encontró el archivo')
    
    def getEstudiantes(self)->list['Estudiante']:
        return self.estudiantes
    
    def getEstudiante(self, dni:int)->Estudiante:
        for estudiante in self.estudiantes:
            if estudiante.get_dni() == dni:
                return estudiante
    
    def existe(self, otroEstudiante: Estudiante)->bool:
        for estudiante in self.estudiantes:
            if estudiante == otroEstudiante:
                return True
        return False
    
    def existeDni(self,dni: int)->bool:
        for estudiante in self.estudiantes:
            if estudiante.get_dni() == dni:
                return True
        return False
    
    def agregarEstudiante(self, nuevoEstudiante:Estudiante):
        if not isinstance(nuevoEstudiante, Estudiante):
            raise ValueError('El objeto no es un estudiante')
        if self.existe(nuevoEstudiante):
            raise ValueError('El estudiante ya existe')
        self.estudiantes.append(nuevoEstudiante)
        self.guardarEstudiantes()

    def eliminarPorDni(self, dni:int):
        for estudiante in self.estudiantes:
            if estudiante.get_dni() == dni:
                self.estudiantes.remove(estudiante)
                self.guardarEstudiantes()
                return True
        return False
