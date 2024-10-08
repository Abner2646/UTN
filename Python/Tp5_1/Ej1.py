class Atleta:
    __MAX_VALOR = 100
    __MIN_VALOR = 1
    __entrenamiento = 0
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__energia = self.__class__.__MAX_VALOR
        self.__destreza = self.__class__.__MIN_VALOR

    #COMANDOS
    def entrenar(self) -> None:
        '''Cuando un atleta entrena,
        consume 5 unidades de energía. Cada cinco
        entrenamientos el atleta mejora en 1 punto su destreza, que al crearse comienza
        con su valor en el mínimo predeterminado'''
        if self.__energia - 5 >= self.__class__.__MIN_VALOR:
            self.__energia -= 5
            print(f"Energía actual: {self.__energia}")
            self.__entrenamiento += 1
            if self.__entrenamiento % 5 == 0:
                self.__destreza += 1
        else:
            print("El atleta no puede entrenar, necesita más energía.")

    def descansar(self) -> None:
        '''Recupera 20 de energía.'''
        if self.__energia >= 95:
            print("Energía actualizada a al máximo!")
            self.__energia = self.__class__.__MAX_VALOR
        else:
            self.__energia += 20
            print("Energía actualizada a al máximo!")

    #CONSULTAS
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEnergia(self) -> int:
        return self.__energia
    
    def obtenerDestreza(self) -> int:
        return self.__destreza
    
    def toString(self):
        return (f"Estado actual: Nombre:{self.__nombre}, Destreza: {self.__destreza}, Energia: {self.__energia}")


class Tester:
    @staticmethod
    def testearTodo():
        a1 = Atleta("Abner")
        print(a1.toString())

        a1.entrenar()
        print(a1.toString())

        a1.descansar()
        print(a1.toString())

        print(f"Destreza: {a1.obtenerDestreza()}")
        print(f"Energia: {a1.obtenerEnergia()}")
        print(f"Nombre: {a1.obtenerNombre()}")

if __name__ == '__main__':
    Tester.testearTodo()