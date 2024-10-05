class Especie:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__machos = 0
        self.__hembras = 0
        self.__ritmo = 0

    #COMANDOS
    def establecerHembras(self, cantHembras:int) -> None:
        '''Los comandos establecerMachos y establecerHembras controlan que el parámetro sea positivo,
        en caso contrario no modifican el valor del atributo'''
        try:
            # 1. Verifica si el valor es numérico
            if not isinstance(cantHembras, int):
                raise TypeError("El valor debe ser un número entero.")
            
            # 2. Verifica si el valor es negativo
            if cantHembras < 0:
                raise ValueError("La cantidad de hembras no puede ser negativa.")
            
            # Si pasa todas las validaciones, asigna el valor
            self.__hembras = cantHembras

        except TypeError as te:
            print(f"Error de tipo: {te}")
        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def mostrar(self) -> None:
        print(f"Especie: {self.__nombre}, Machos: {self.__machos}, Hembras: {self.__hembras}")