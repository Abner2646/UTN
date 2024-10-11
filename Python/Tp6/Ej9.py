from modulo_fecha import Fecha

class Atraccion:
    '''Atracción: Cada atracción tiene un nombre, un tipo (por ejemplo, montaña rusa, casa
    embrujada), un nivel de emoción (bajo, medio, alto) y una estatura mínima requerida
    (por ejemplo: 1,40). Las atracciones pueden funcionar en uno o más turnos
    (“mañana”, “tarde” o “noche”). '''
    '''Nombre, tipo, estatura mínima, nivel de emoción y turnos de funcionamiento'''
    def __init__(self, nombre:str, estaturaMinima:float, emocion:str, turnos:str) -> None:
        self.__nombre = nombre
        self.__estaturaMinima = estaturaMinima
        self.__emocion = emocion
        self.__turnos = turnos

    #GETTERS:
    def obtenerNombre (self) -> str:
        return self.__nombre
        
    def obtenerEstaturaMinima(self) -> float:
        return self.__estaturaMinima
    
    def obtenerEmocion(self) -> str:
        return self.__emocion
    
    def otenerTurnos(self) -> str:
        return self.__turnos

class Visitante:
    '''Visitante: Cada visitante tiene un nombre, una edad, una altura y una dirección de
    correo electrónico. Los visitantes pueden comprar entradas y disfrutar de las
    atracciones, y llevan un registro de las atracciones a las que pudieron ingresar'''
    def __init__(self, nombre:str, edad:int, altura:float, email:str) -> None:
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura
        self.__email = email
        self.__entradas = []

    #SETTERS:
    def comprarEntradas(self, entrada:'Entradas') -> None:
        self.__entradas.append(entrada)

    def disfrutarAtraccion(self, atraccion:'Atraccion', guia:'Guia') -> None: #Pasa previamente por la autorización del guia
        if guia.autorizar(self, atraccion):
            print("Estoy disfrutando la atracción!!")

    #GETTERS:
    def obtenerAltura(self) -> float:
        return self.__altura

class Entradas:
    '''Entrada: Cada entrada tiene un número de entrada, una fecha y un tipo (VIP). Cada entrada está asociada a un visitante'''
    def __init__(self, numEntrada:int, fecha:'Fecha', vip:bool, visitante:'Visitante') -> None:
        self.__numEntrada = numEntrada
        self.__fecha = fecha
        self.__vip = vip
        self.__visitante = visitante #Cada entrada está asociada a un visitante

    #GETTERS:
    def obtenerNumEntrada(self) -> int:
        return self.__numEntrada
    
    def obtenerFecha (self) -> 'Fecha':
        return self.__fecha
    
    def obtenerTipoEntrada(self) -> bool:
        return self.__vip
    
    def obtenerVisitante(self) -> 'Visitante':
        return self.__visitante

class Guia:
    '''Guía de Aventura: Cada guía tiene un nombre y un turno de trabajo (“mañana”,
    “tarde” o “noche”). Los guías deben autorizar al visitante cada vez que desee utilizar
    una atracción en base a su estatura.'''
    def __init__(self, nombre:str, turno:str) -> None:
        self.__nombre = nombre
        self.__turno = turno

    #GETTER:
    def autorizar(self, visitante:'Visitante', atraccion:'Atraccion') -> bool:
        '''Retorna true o flase dependiendo si autoriza o no al visitante usar la atracción'''
        return visitante.obtenerAltura() > atraccion.obtenerEstaturaMinima()
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerTurno(self) -> str:
        return self.__turno
    

class Tester:
    def test_clases():
        #Test de la clase Atraccion
        atraccion = Atraccion("Playa", 1.50, "alta", "mañana, tarde")
        assert atraccion.obtenerNombre() == "Playa"
        assert atraccion.obtenerEstaturaMinima() == 1.50
        assert atraccion.obtenerEmocion() == "alta"
        assert atraccion.otenerTurnos() == "mañana, tarde"
        
        #Test de la clase Visitante
        visitante = Visitante("Juan", 30, 1.80, "juan@example.com")
        visitante.comprarEntradas(Entradas(1, Fecha(1, 1, 2022), True, visitante))
        assert visitante.obtenerAltura() == 1.80
        
        #Test de la clase Entrada
        entrada = Entradas(1, Fecha(1, 1, 2022), True, visitante)
        assert entrada.obtenerNumEntrada() == 1
        assert entrada.obtenerFecha().obtenerDia() == 1
        assert entrada.obtenerFecha().obtenerMes() == 1
        assert entrada.obtenerFecha().obtenerAño() == 2022
        assert entrada.obtenerTipoEntrada() == True
        assert entrada.obtenerVisitante().obtenerAltura() == 1.80
        
        #Test de la clase Guia
        guia = Guia("Maria", "mañana")
        assert guia.autorizar(visitante, atraccion) == True
        assert guia.obtenerNombre() == "Maria"
        assert guia.obtenerTurno() == "mañana"

        print("Todos los tests pasaron")

if __name__ == "__main__":
    Tester.test_clases()