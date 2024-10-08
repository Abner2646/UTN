'''Un club de deportes está organizando un torneo de atletismo, y nos pide que le
ayudemos a gestionar la información de los participantes y las disciplinas. El sistema
debe permitir registrar a los participantes y las disciplinas en las que compiten.
Cada Participante tiene un nombre, una edad y una nacionalidad.
Un Participante puede competir en varias Disciplinas.
Cada Disciplina tiene un nombre (como carreras de 100 metros, carreras de 400
metros, salto de longitud, salto en alto, lanzamiento de jabalina, etc.) y una
descripción (que explica las reglas o características de esa disciplina).
Varios Participantes pueden competir en la misma Disciplina, y un Participante
puede competir en varias disciplinas.
Se pide:
A. Diseñar el diagrama UML de las clases.
B. Implementar las clases en python.
C. Desarrollar una clase tester que pida al usuario los datos para registrar las
disciplinas, y los datos de los participantes. Luego debe permitir al usuario
ver todos los participantes inscriptos en una disciplina y las disciplinas en las
que participa cada competidor. '''

class Participante:
    def __init__(self, nombre:str, edad:int, nacionalidad:str) -> None:
        '''Cada Participante tiene un nombre, una edad y una nacionalidad.
        Un Participante puede competir en varias Disciplinas'''
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplinas = []

    #SETTERS:
    def establecerDisciplina(self, disciplina:'Disciplina') -> None:
        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)    
            disciplina.agregarParticipante(self)

    #GETTERS:
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEdad(self) -> int:
        return self.__edad
    
    def obtenerDisciplinas(self):
        return [disciplina.obtenerNombre() for disciplina in self.__disciplinas]


class Disciplina:
    '''Cada Disciplina tiene un nombre (como carreras de 100 metros, carreras de 400
    metros, salto de longitud, salto en alto, lanzamiento de jabalina, etc.) y una
    descripción (que explica las reglas o características de esa disciplina).'''
    def __init__(self, nombre:str, descripcion:str) -> None:
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes = []

    #SETTER:
    def agregarParticipante(self, participante:'Participante') -> None:
        if participante not in self.__participantes:
            self.__participantes.append(participante)

    #GETTERS:
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerDescripcion(self) -> str:
        return self.__descripcion
    
    def obtenerParticipantes(self):
        return [participante.obtenerNombre() for participante in self.__participantes]


class Tester:
    def testerx():
        '''Desarrollar una clase tester que pida al usuario los datos para registrar las
        disciplinas, y los datos de los participantes. Luego debe permitir al usuario
        ver todos los participantes inscriptos en una disciplina y las disciplinas en las
        que participa cada competidor.'''

        #Pido los datos y creo los Participantes
        Nombre = input("Ingrese el nombre del participante 1: ")
        Edad = int(input("Ingrese la edad: "))
        Nacionalidad = input("Ingrese la nacionalidad: ")
        P1 = Participante(Nombre, Edad, Nacionalidad)
        print("")

        Nombre = input("Ingrese el nombre del participante 2: ")
        Edad = int(input("Ingrese la edad: "))
        Nacionalidad = input("Ingrese la nacionalidad: ")
        P2 = Participante(Nombre, Edad, Nacionalidad)
        print("")

        #Pido los datos y creo las Disciplinas
        Nombre = input("Ingrese nombre de la Disciplina 1: ")
        Descripcion = input("Ingrse la descripcion de la disciplina: ")
        D1 = Disciplina(Nombre, Descripcion)
        print("")

        Nombre = input("Ingrese nombre de la Disciplina 2: ")
        Descripcion = input("Ingrse la descripcion de la disciplina: ")
        D2 = Disciplina(Nombre, Descripcion)
        print("")

        #Agregarle al P1 las dos disciplinas
        print("Agregando disciplinas al P1... ")
        P1.establecerDisciplina(D1)
        P1.establecerDisciplina(D2)
        print("")

        #Mostrar las disciplinas que tiene el P1
        print("Disciplinas del Participante 1: ")
        print(P1.obtenerDisciplinas())
        print("")

        #Mostrar participantes de la disciplina 2
        print("Mostrar participantes de la disciplina 1: ")
        print(D1.obtenerParticipantes())

if __name__ == "__main__":
    Tester.testerx()