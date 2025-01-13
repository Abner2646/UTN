''''Crear clases que funcionen como repositorio de objetos, es decir, cada clase entidad
tendrá una clase repositorio que manipule una colección de sus objetos.'''

from modelos.entidades.curso import Curso
import json

class RepoCurso:
    PATH = "data/cursos.json"
    
    def __init__(self):
        self.cursos: list['Curso'] = self.cargarCursos()

    def cargarCursos(self):
        """
        Metodo para cargar cursos al inicializarse el repositorio
        """
        lista: list['Curso'] = []
        try:
            
            with open(RepoCurso.PATH, 'r') as file:
                cursos_data = json.load(file)
                for curso in cursos_data:
                    lista.append(Curso.from_dict(curso)) #!!
            
        except FileNotFoundError:
            print('No se encontró el archivo')

        return lista
    
    def guardarCursos(self):
        try:
            lista = [curso.to_dict() for curso in self.cursos]
        
            with open(RepoCurso.PATH, 'w') as file:
                json.dump(lista, file, indent=4)

        except FileNotFoundError:
            print('No se encontró el archivo')
    
    def getCursos(self)->list['Curso']:
        return self.cursos
    
    def getCurso(self, id:int)->Curso:
        for curso in self.cursos:
            if curso.get_id() == id:
                return curso
    
    def existe(self, otroCurso: Curso)->bool:
        for curso in self.cursos:
            if curso == otroCurso:
                return True
        return False
    
    def existeID(self,id: int)->bool:
        for curso in self.cursos:
            if curso.get_id() == id:
                return True
        return False
    
    def agregarCurso(self, nuevoCurso:Curso):
        if not isinstance(nuevoCurso, Curso):
            raise ValueError('El objeto no es un curso')
        if self.existe(nuevoCurso):
            raise ValueError('El curso ya existe')
        self.cursos.append(nuevoCurso)
        self.guardarCursos()

    def eliminarPorId(self, id:int):
        for curso in self.cursos:
            if curso.get_id() == id:
                self.cursos.remove(curso)
                self.guardarCursos()
                return True
        return False
