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
