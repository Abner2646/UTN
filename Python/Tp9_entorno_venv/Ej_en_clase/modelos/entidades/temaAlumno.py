from modelos.entidades.temax import Temax
from .alumno import Alumno
from .tema import Tema

class TemaAlumno:
    def __init__(self, alumno:'Alumno', tema:'Tema'):
        self.__alumno = alumno
        self.__tema = tema

    #GETTERS
    def obtenerAlumno(self) -> 'Alumno':
        return self.__alumno
    
    def obtenerTema(self) -> 'Tema':
        return self.__tema
    
    #SETTERS
    def establecerAlumno(self, alumno):
        self.__alumno = alumno

    def establecerTema (self, tema):
        self.__tema = tema

