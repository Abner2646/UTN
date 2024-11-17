#from modelos.entidades.alumno import Alumno
import json

class Alumno:
    __ultimoID = 0

    @classmethod
    def generarNuevoID(cls) -> int:
        '''Retorna el nuevo ID (incrementa 1 al anterior)'''
        cls.__ultimoID += 1
        return cls.__ultimoID
    
    @classmethod
    def obtenerUltimoID(cls) -> int:
        return cls.__ultimoID
    
    @classmethod
    def establecerUltimoID(cls, id:int):
        '''Se usa para establecer el último ID cuando ya haya alumnos cargados en el archivo de alumnos'''
        cls.__ultimoID = id

    @classmethod
    def fromDiccionario(cls, dicc:dict) -> "Alumno":
        if "id" in dicc:
            return cls(dicc["legajo"], dicc["apellido"], dicc["nombre"], dicc["id"])
        else:
            return cls(dicc["legajo"], dicc["apellido"], dicc["nombre"])
    
    def __init__(self, legajo:int, apellido:str, nombre:str, id:int=None):
        if not isinstance(legajo, int) or legajo<0:
            raise ValueError
        if not isinstance(apellido, str):
            raise ValueError
        
        if not isinstance(nombre, str):
            raise ValueError
        if id != None:
            self.__id = id
        else:
            self.__id = Alumno.generarNuevoID()

        self.__legajo = legajo
        self.__apellido = apellido
        self.__nombre = nombre

    #Consultar triviales
    def obtenerID(self) -> int:
        return self.__id
    
    def obtenerLegajo(self) -> int:
        return self.__legajo
    
    def obtenerApellido(self) -> str:
        return self.__apellido
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def establecerNombre(self, nombre:str):
        self.__nombre = nombre

    def establecarApellido(self, apellido):
        self.__apellido = apellido

    def establecerLegajo(self, legajo:int):
        self.__legajo = legajo


class RepositorioAlumno:
    __ruta_archivo = "datos.alumnos.json"
    def __init__(self):
        self.__alumnos = self.__cargarTodos()

    def __cargarTodos(self) -> list:
        #Leer todo el contenido del archivo
        #convertirlo en lista de diccionarios
        #convertir la lista de diccionarios en lista de objetos Alumno
        lista_objetos = []
        try:
            lista_dic = []
            with open(RepositorioAlumno.__ruta_archivo, "r", encoding="UTF8") as archivo:
                diccionarioDatos = json.load(archivo)
            lista_dic = diccionarioDatos["alumnos"]
            Alumno.establecerUltimoID(diccionarioDatos["ultimoID"])
            for dic in lista_dic:
                lista_objetos.append(Alumno.fromDiccionario(dic))
        except:
            print("Error al abrir el archivo alumnos.json.")
        return lista_objetos
    
    def __guardarTodos(self):
        with open(RepositorioAlumno.__ruta_archivo, "w", encoding="UTF8") as archivo:
            diccionarioDatos = {
                "ultimoID": Alumno.obtenerID(),
                "alumnos": self.__alumnos
            }
            json.dump(diccionarioDatos, archivo)

    def obtenerTodos(self) -> list:
        return self.__alumnos
    
    def existeAlumnoConLegajo(self, legajo:int) -> bool:
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                return True
        return False
    
    def agregar(self, alumno:'Alumno'):
        if not self.existeAlumnoConLegajo(alumno.obtenerLegajo()):
            self.__alumnos.append(alumno)
            self.__guardarTodos()

    def obtenerAlumnoPorLegajo(self, legajo:int) -> Alumno:
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                return alumno
        return None

    def modificarLegajoPorDatos(self, legajo:int, apellido:str, nombre:str):
        #buscar el alumno a modificar
        alum = self.obtenerAlumnoPorLegajo(legajo)
        #reemplazar nombre y apellido
        if alum is not None:
            alum.establecarApellido(apellido)
            alum.establecerNombre(nombre)
        #guardar
        self.__guardarTodos()

    def modificarLegajoPorObjeto(self, alumno:'Alumno'):
        if self.existeAlumnoConLegajo(alumno.obtenerLegajo()):
            alumno_a_modificar = self.obtenerAlumnoPorLegajo(alumno.obtenerLegajo())
            alumno_a_modificar.establecarApellido(alumno.obtenerApellido())
            alumno_a_modificar.establecerNombre(alumno.obtenerNombre())
            alumno_a_modificar.establecerLegajo(alumno.obtenerLegajo())
    
    def eliminarPorLegajo(self, legajo:int):
        for alumno in self.__alumnos:
            if legajo == alumno.obtenerLegajo():
                self.__alumnos.remove(alumno)
