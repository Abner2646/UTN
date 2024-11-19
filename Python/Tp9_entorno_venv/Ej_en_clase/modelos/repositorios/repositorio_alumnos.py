from ...modelos.entidades.alumno import Alumno
import json

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
