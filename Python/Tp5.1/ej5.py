import random

class Especie:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre
        self.__machos = 0
        self.__hembras = 0
        self.__ritmo = 0

    #COMANDOS
    def establecerHembras(self, cantHembras:int) -> None:
        '''Controla que el parámetro sea positivo, en caso contrario no modifica el valor del atributo'''
        try:
            # 1. Verifica si el valor es numérico
            if not isinstance(cantHembras, int): #isinstance devuelve True o False
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

    def establecerMachos (self, cantMachos:int) -> None:
        try:
            # 1. Verifica si el valor es numérico
            if not isinstance(cantMachos, int): #isinstance devuelve True o False
                raise TypeError("El valor debe ser un número entero.")
            
            # 2. Verifica si el valor es negativo
            if cantMachos < 0:
                raise ValueError("La cantidad de hembras no puede ser negativa.")
            
            # Si pasa todas las validaciones, asigna el valor
            self.__machos = cantMachos

        except TypeError as te:
            print(f"Error de tipo: {te}")
        except ValueError as ve:
            print(f"Error de valor: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def establecerRitmo(self, ritmo:float) -> None:
        self.__ritmo = ritmo

    def actualizarHembras (self, cantHembras:int) -> None:
        '''Los comandos actualizarMachos y actualizarHembras
        suman el valor del parámetro al atributo de instancia. Pueden recibir un parámetro
        negativo, pero el valor del atributo nunca debe ser menor a 0. '''
        self.__hembras += cantHembras
        if self.__hembras < 0:
            self.__hembras = 0
    
    def actualizarMachos (self, cantMachos:int) -> None:
        '''Los comandos actualizarMachos y actualizarHembras
        suman el valor del parámetro al atributo de instancia. Pueden recibir un parámetro
        negativo, pero el valor del atributo nunca debe ser menor a 0. '''
        self.__machos += cantMachos
        if self.__machos < 0:
            self.__machos = 0

    def actualizarRitmo (self, ritmo:float) -> None:
        '''No se especifiac en la consigna qué debería hacer este método.
        Simplemente cambia el rimo de instancia al pasado por parametro.'''
        self.__ritmo = ritmo

    #CONSULTAS
    def obtenerMachos(self) -> int:
        return self.__machos
    
    def obtenerHembras(self) -> int:
        self.__hembras

    def obtenerRitmo(self) -> float:
            return self.__ritmo

    def poblacionActual(self) -> int:
        '''Retorna el total de ejemplares de la especie.'''
        return self.__machos + self.__hembras
    
    def poblacionEstimada(self, años:float) -> float:
        '''Retoran el estimado de ejemplares que va a hacer de una especie en la cantidad de años que se pasaron
        por parametro.'''
        return self.__machos + self.__hembras + (self.__ritmo * años)

    def añosParaPoblacion(self, poblacion:int) -> float:
        #No se especifica que función debería hacer este método
        return 0

    def riesgo(self) -> str:
        '''Retorna “verde” si el ritmo de crecimiento es positivo, “amarillo” si es nulo y “rojo” si es negativo'''
        if self.__ritmo > 0:
            return "verde"
        if self.__ritmo < 0:
            return "rojo"
        else:
            return "amrillo"
        
    def masHembras(self) -> bool:
        #No se especifica que función debería hacer este método
        return 0
    
    def mayorRitmo(self, otraEspecie:'Especie') -> 'Especie': #!!??
        '''Devuelve la referencia al objeto con mayor ritmo de crecimiento.'''
        if self.__ritmo > otraEspecie.__ritmo:
            return self
        else:
            return otraEspecie
        
    def clonar(self) -> 'Especie': #!! No sé cómo se hace un clon si no es con alguna palabra reservada
        '''Devuelve un nuevo objeto Epecia con el mismo estado interno del objeto que recibe el mensaje.'''
        return Especie(self.__nombre)

    def toString(self) -> None:
        return(f"{self.__nombre}, Machos: {self.__machos}, Hembras: {self.__hembras}, Ritmo: {self.__ritmo}.")



class Tester:
    @staticmethod
    def testear():
        '''Escriba una clase tester que verifique los servicios provistos por Especie con
        valores ingresados por el usuario para nombre y ritmo y generados al azar
        para machos y hembras dentro de un rango establecido'''

        nombre = input("Ingrese un nombre: ")
        ritmo = input("Ingrese ritmo: ")
        print("")

        #Crear el objeto1
        e1 = Especie(nombre)
        e1.establecerRitmo(ritmo)
        e1.establecerHembras(random.randint(1, 100))
        e1.establecerMachos(random.randint(1, 100))
        print(f"Especie creada con las características: {e1.toString()}")
        print("")

        #Establecer:
        print("Probando actualizar valores: ")
        e1.establecerHembras(50)
        e1.establecerMachos(50)
        e1.establecerRitmo(10)
        print(f"Valores actuales: {e1.toString()}")
        print("")

        #Actualizar
        print("Probando actualizar: ")
        e1.establecerHembras(75)
        e1.establecerMachos(75)
        e1.establecerRitmo(15)
        print(f"Valores actuales: {e1.toString()}")
        print("")

        #Poblacion actual
        print("Probando poblacion actual: ")
        print(f"Poblacion actual: {e1.poblacionActual()}")
        print(f"Valores actuales: {e1.toString()}")
        print("")

        #Riesgo
        print("Probando riesgo: ")
        print (f"Riesgo: {e1.riesgo()}")
        print("")

        #Clonar 
        print("Probando clonar: ")
        e2 = e1.clonar()
        print(f"Valores actuales de e2: {e2.toString()}")
        print("")

        #Establecer (para modificar la segunda especie)


        #mayorRitmo
        print("Probando mayor ritmo: ")
        print(f"El objeto de mayor ritmo es: {e1.mayorRitmo(e2).toString()}")


if __name__ == "__main__":
    Tester.testear()