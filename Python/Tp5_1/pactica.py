from Ej1 import Atleta #Tiene que setar en la misma carpeta!!

class Persona:
    def __init__(self, edad:int, nombre:str, dni:int=10):
        self.__edad=edad
        self.__nombre=nombre
        self.__dni=dni

    def toString(self):
        return f'Persona(edad={self.__edad}, nombre="{self.__nombre}", dni={self.__dni})'

class Tester:
    def test():
        p = Persona(25, 'Juan')
        print(p) #Si no está el __str__ imprime el espacio en memoria

if __name__ == "__main__":
    Tester.test()