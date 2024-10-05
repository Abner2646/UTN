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
#----------------------------------
class Tester:
    def testearColor():
        #Crear color
        print("Probando crear color:")
        color1 = Color(100, 100, 100)
        print(color1.toString())
        print("")

        #Probando variar colores uno x uno
        print("Probando variar colores uno x uno: ")
        color1.establecerRojo(20)
        color1.establecerVerde(20)
        color1.establecerAzul(20)
        print(color1.toString())
        print("")

        #Probar variar
        print("Probando variar: ")
        color1.variar(20)
        print(color1.toString())
        print("")

        #Probar establecer uno x uno
        print("Probando establecer uno x uno:")
        color1.establecerRojo(71)
        color1.establecerVerde(71)
        color1.establecerAzul(71)
        print(color1.toString())
        print("")

        #Probar copiar()
        print("Probando copiar:")
        color2 = Color() #Creo color 2 con todos los valores por defecto
        color2.copiar(color1)
        print(color2.toString())
        print("")

        #Probar complemento
        print("Probando complemento: ")
        color2 = color2.complemento()
        print(color2.toString())
        print("")

        #Probar esIgualQue:
        print("Probando esIgualQue:")
        if color1.esIgualQue(color2):
            print("Es igual.")
        else:
            print("NO es igual.")
        print("")
        
        #Probando clonar()
        print("Probando clonar(): ")
        color1 = color2.clonar()
        print("Deverían ser iguales: ")
        print(color1.toString())
        print(color2.toString())

class Tester4:
    def tester4B():
        color_1 = Color()
        color_2 = Color(70, 70, 70)
        color_3 = Color(255, 255, 255)
        igualdad1 = color_1.esIgualQue(color_2)
        igualdad2 = color_2.esIgualQue(color_3)
        color_4 = color_1
        color_5 = color_2.clonar()


#----------------------------------

if __name__ == '__main__':
    Tester.testearColor()


#HACER:
#-Ir con la notebook con chat gpt iniciado en modo incógnito
#-Ver cómo hago el grafico de tablas
#-Pregunatar a Damian si vamos a tener que dibujar diagramas o solo código

#SETTER: copiar(otroObjeto):
#copia los atributos de otra instancia en esta

#GETTER: clonar():
#devuelve un objeto igual al self