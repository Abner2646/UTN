class Temax:
    @classmethod
    def nada(cls):
        '''Estafunción retorna 0'''
        return 0
    
    def __init__(self, numero:int, nombre:str, enunciado:str):
        if not isinstance(numero, int):
            raise ValueError
        if not isinstance (nombre, str):
            raise ValueError
        if not isinstance(enunciado, str):
            raise ValueError
        self.__numero = numero
        self.__nombre = nombre
        self.__enunciado = enunciado

    def obtenerNumero(self) -> int:
        return self.__numero
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEnunciado (self) -> str:
        return self.__enunciado
    
    #SETTERS:
    def establecerNumero(self, numero) -> str:
        self.__numero = numero

    def establecerNombre (self, nombre:str) -> str:
        self.__nombre = nombre

    def establecerEnunciado (self, enunciado) -> str:
        self.__enunciado = enunciado
