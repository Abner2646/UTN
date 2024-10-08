class Color:
    def __init__(self,rojo:int=255, verde:int=255, azul:int=255) -> None: ##?? Está bien sobrecargar los metodos así?
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul

    #SETTERS
    def variar(self, val:int) -> None:
        '''modifica cada componente de color sumándole si es
        posible, un valor dado. Si sumándole el valor dado a una o varias
        componentes se supera el valor 255, dicha componente queda en 255. Si el
        argumento es negativo la operación es la misma pero en ese caso el mínimo
        valor que puede tomar una componente, es 0.'''
        #Rojo
        if self.__rojo + val <= 255:
            self.__rojo += val
        elif self.__rojo + val < 0:
            self.__rojo = 0
        else:
            self.__rojo = 255

        #Verde
        if self.__verde + val <= 255:
            self.__verde += val
        elif self.__verde + val < 0:
            self.__verde = 0
        else:
            self.__verde = 255

        #Azul
        if self.__azul + val <= 255:
            self.__azul += val
        elif self.__azul + val < 0:
            self.__verde = 0
        else:
            self.__verde = 255

    def variarRojo(self, val:int) -> None:
        if self.__rojo + val <= 255:
            self.__rojo += val
        elif self.__rojo + val < 0:
            self.__rojo = 0
        else:
            self.__rojo = 255
    
    def variarVerde(self, val:int) -> None:
        if self.__verde + val <= 255:
            self.__verde += val
        elif self.__verde + val < 0:
            self.__verde = 0
        else:
            self.__verde = 255

    def variarAzul(self, val:int) -> None:
        if self.__azul + val <= 255:
            self.__azul += val
        elif self.__azul + val < 0:
            self.__azul = 0
        else:
            self.__azul = 255

    def establecerRojo(self, valor:int) -> None:
        self.__rojo = valor
    
    def establecerVerde(self,valor:int) -> None:
        self.__verde = valor

    def establecerAzul(self,valor:int) -> None:
        self.__azul = valor

    def copiar(self, otroColor:'Color') -> 'Color':
        self.__rojo = otroColor.obtenerRojo()
        self.__verde = otroColor.obtenerVerde()
        self.__azul = otroColor.obtenerAzul()

    #GETTERS
    def obtenerRojo(self) -> int:
        return self.__rojo
    
    def obtenerVerde(self) -> int:
        return self.__verde
    
    def obtenerAzul(self) -> int:
        return self.__azul
    
    #[...] acá faltan los esRojo, esGris que no sé cual es el condicional que determina un color :(

    def esNegro(self) -> bool:
        return self.__rojo == 0 and self.__verde == 0 and self.__azul == 0
    
    def complemento(self) -> 'Color':
        '''retorna un nuevo objeto con el color complemento del color
        del objeto que recibe el mensaje para alcanzar el color blanco.'''
        rojo = 255 - self.__rojo
        verde = 255 - self.__verde
        azul = 255 - self.__azul
        return Color(rojo, verde, azul)
    
    def esIgualQue(self, otroColor:'Color') -> bool:
        '''retorna el valor verdadero si ambos objetos son equivalentes'''
        if self.__rojo == otroColor.obtenerRojo() and self.__verde == otroColor.obtenerVerde() and self.__azul == otroColor.obtenerAzul():
            return True
        else:
            return False
        
    def clonar(self) -> 'Color':
        ''' devuelve un nuevo color con el mismo estado interno que el color que recibe el mensaje.'''
        return Color(self.__rojo, self.__verde, self.__azul)
    
    def toString(self) -> str:
        return f"Rojo: {self.__rojo}, Verde: {self.__verde}, Azul: {self.__azul}."
    
class Borde:
    def __init__(self, grosor:int, color:'Color') -> None:
        self.__grosor = grosor
        self.__color = color

    #COMANDOS:
    def copiarValores(borde:'Borde') -> None:
        self.__grosor = borde.__grosor
        self.__color = borde.__grosor
    
    def obtenerGrosor(self) -> int:
        return self.__grosor
    
    def obtenerColor(self) -> 'Color':
        return self.__color
    
    def clonar(self) -> 'Color':
        return Color(self.__grosor, self.__color)
    
    def esIgualQue(self, borde:'Borde') -> bool:
        return self.__color == borde.__color and self.__color == borde.__color
    
#--------------------------FIN PUNTO 2
    
#Clase tester del punto 3
class Tester:
    def testerx():
        C1 = Color(150, 150, 150)
        C2 = Color(150, 150, 150)
        B1 = Borde(1,C1)
        B2 = Borde(1,C2)
        print(C1 == C2)
        print(B1 == B2)
        print(C1.esIgualQue(C2))
        print(B1.esIgualQue(B2))

if __name__ == '__main__':
    Tester.testerx()