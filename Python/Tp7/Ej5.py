'''En un sistema de administración de personal se tienen tres categorías:
administrativos, programadores y personal de mantenimiento. Cada uno de ellos
posee nombre, apellido y DNI. Los administrativos tienen número de legajo y
posición. Los programadores tienen número de legajo y proyecto al que son
asignados. El personal de mantenimiento tiene legajo, y el nombre del área a la que
son asignados.
a. Realice un diagrama UML completo que represente la jerarquía de clases.
b. Implementar las clases en python.'''

class Empleado:
    def __init__(self, nombre:str, apellido:str, dni:int, numLegajo:int) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._numLegajo = numLegajo
    
    def obtenerNombre(self) -> str:
        return self._nombre
    
    def obtenerApelido(self) -> str:
        return self._apellido
    
    def obtenerDni(self) -> int:
        return self._dni
    
    def obtenerNumLegajo(self) -> int:
        return self._numLegajo

class Asministrativo(Empleado):
    '''Los administrativos tienen número de legajo y posición'''
    def __init__(self, nombre:str, apellido:str, dni:int, numLegajo:int, posicion:str) -> None:
        super().__init__ (nombre, apellido, dni)
        self.__numLegajo = numLegajo
        self.__posicion = posicion

    def obtenerPosicion(self) -> str:
        return self.__posicion

class Progrmador(Empleado):
    '''Los programadores tienen número de legajo y proyecto al que son asignados.'''
    def __init__(self, nombre, apellido, dni, numLegajo, proyecto):
        super().__init__(nombre, apellido, dni)
        self.__numLegajo = numLegajo
        self.__proyecto = proyecto

    def obtenerProyecto(self) -> str:
        return self.__proyecto

class Mantenimiento(Empleado):
    '''El personal de mantenimiento tiene legajo, y el nombre del área a la que son asignados.'''
    def __init__(self, nombre, apellido, dni, numLegajo, area):
        super().__init__(nombre, apellido, dni)
        self.__numLegajo = numLegajo
        self.__area = area

    def obtenerArea(self) -> str:
        return self.__area

