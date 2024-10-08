'''Un organizador de eventos nos pide diseñar un sistema simple para gestionar los
eventos. El sistema debe permitir registrar eventos, participantes y organizadores, y
asignar participantes a eventos y organizadores a eventos.
Requerimientos
Evento: Cada evento tiene un nombre, una fecha y una descripción. Los eventos
pueden tener múltiples participantes y un organizador asignado.
Participante: Cada participante tiene un nombre, una dirección de correo electrónico
y un número de teléfono. Los participantes pueden registrarse en uno o más
eventos.
Organizador: Cada organizador tiene un nombre, una dirección de correo electrónico
y una especialidad (por ejemplo, planificación de eventos, catering, músico, DJ, etc.).
Cada organizador puede estar a cargo de uno o más eventos.'''

class Fecha:
    __DIAS_X_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Dias de cada mes año NO bisiesto
    __DIAS_X_MES_B = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Dias de cada mes año bisiesto

    def __init__(self, dia:int, mes:int, año:int) -> None:
        self.__dia = dia
        self.__mes = mes
        self.__año = año

    def establecerDia (self, dia:int) -> None:
        self.__dia = dia

    #SETTERS
    def establecerMes(self, mes:int) -> None:
        self.__mes = mes

    def establecerAño(self, año:int) -> None:
        self.__año = año

    #GETTERS
    def fechaValida(self) -> bool:
        '''Si la fecha es valida retorna True.'''
        #Verifica primero si es bisiesto
        #Ser divisible por 4. No ser divisible por 100, a menos que sea divisible por 400
        if (self.__año % 4 == 0 and self.__año % 100 != 0) or (self.__año % 400 == 0): #Es bisiesto
            if (self.__dia < Fecha.__DIAS_X_MES_B[self.__mes - 1]) and (self.__mes <= 12):
                return True
            else:
                return False
        else: #NO es bisiesto
            if (self.__dia < Fecha.__DIAS_X_MES[self.__mes - 1]) and (self.__mes <= 12):
                return True
            else:
                return False

    def obtenerDia(self) -> int:
        return self.__dia
    
    def obtenerMes(self) -> int:
        return self.__mes
    
    def obtenerAño(self) -> int:
        return self.__año
    
    def diaSiguiente(self) -> 'Fecha': #!!??
        '''retorna una nueva fecha con los valores del día siguiente a la
        fecha que recibe el mensaje'''
        #Inicializo variables auxiliares
        dia = self.__dia
        mes = self.__mes
        año = self.__año

        if (self.__año % 4 == 0 and self.__año % 100 != 0) or (self.__año % 400 == 0): #Si es biciesto
            if dia < Fecha.__DIAS_X_MES_B[self.__mes - 1]: #Si no supera los días del mes
                dia += 1
            elif self.__mes + 1 <= 12:
                mes += 1
                dia = 1
            else:
                año += 1
                mes = 1
                dia = 1
            return Fecha(dia, mes, año)

        else: #Si NO es biciesto
            if dia < Fecha.__DIAS_X_MES[self.__mes - 1]: #Si no supera los días del mes
                dia += 1
            elif self.__mes + 1 <= 12:
                mes += 1
                dia = 1
            else:
                año += 1
                mes = 1
                dia = 1
        return Fecha(dia, mes, año)
    
    def sumaDias(self, cantDias:int) -> 'Fecha':
        '''retorna la fecha que resulta de sumar la cantidad de días recibida
        por parámetro a la fecha que recibe el mensaje'''
        #Inicializo variables auxiliares
        dia = self.__dia
        mes = self.__mes
        año = self.__año
        
        for i in range(cantDias):
            if (self.__año % 4 == 0 and self.__año % 100 != 0) or (self.__año % 400 == 0): #Es biciesto
                if dia < Fecha.__DIAS_X_MES_B[self.__mes - 1]: #Si no supera los días del mes
                    dia += 1
                elif self.__mes + 1 <= 12:
                    mes += 1
                    dia = 1
                else:
                    año += 1
                    mes = 1
                    dia = 1

            else: #Si NO es biciesto
                if dia < Fecha.__DIAS_X_MES[self.__mes - 1]: #Si no supera los días del mes
                    dia += 1
                elif self.__mes + 1 <= 12:
                    mes += 1
                    dia = 1
                else:
                    año += 1
                    mes = 1
                    dia = 1
        return Fecha(dia, mes, año)
        
    def esAnterior (self, otraFecha) -> bool:
        '''retorna verdadero si la fecha que recibe el mensaje es anterior a
        la fecha pasada por parámetro, y falso en caso contrario.'''
        #Si son iguales
        if self.__año == otraFecha.obtenerAño() and self.__mes == otraFecha.obtenerMes() and self.__dia == otraFecha.obtenerAño():
            return False
        
        #Si el año es menor
        if self.__año < otraFecha.obtenerAño():
            return True
        elif self.__año > otraFecha.obtenerAño():
            return False
        
        #Si el mes es menor (a esta altura el año es igual)
        if self.__mes < otraFecha.obtenerMes():
            return True
        elif self.__mes > otraFecha.obtenerMes():
            return False

        #Si el dia es menor (mes y año sabemos que son iguales)
        if self.__dia < otraFecha.obtenerDia():
            return True
        else:
            return False
    
    def esIgualQue(self, otraFecha:'Fecha') -> bool:
        if self.__año == otraFecha.obtenerAño() and self.__mes == otraFecha.obtenerMes() and self.__dia == otraFecha.obtenerAño():
            return True
        else:
            return False
        
    def toString(self) -> str:
        return f"Día: {self.__dia}, Mes: {self.__mes}, Año: {self.__año}."

class Evento:
    '''Cada evento tiene un nombre, una fecha y una descripción. Los eventos
    pueden tener múltiples participantes y un organizador asignado.'''
    def __init__(self, nombre:str, fecha:'Fecha', descripcion:str) -> None:
        self.__nombre = nombre
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__participantes = []

    #SETTERS
    def asignarOrganizador(self, oganizador:'Organizador') -> None:
        self.__organizador = Organizador

    def asignarParticipante(self, participante:'Participante') -> None:
        self.__participantes.append(participante)

    def obtenerNombre(self):
        return self.__nombre
    
    def mostrarParticipantes(self):
        return [participante.obtenerNombre() for participante in self.__participantes]

class Participante:
    '''Cada participante tiene un nombre y un DNI. Los participantes pueden registrarse en uno o más
    eventos.'''
    def __init__(self, nombre:str, dni:int) -> None:
        self.__nombre = nombre
        self.__dni = dni
        self.__eventos = []

    #SETTER
    def agregarEvento(self, evento:'Evento') -> None:
        self.__eventos.append(evento)

    #GETTERS
    def obtenerNombre(self) -> None:
        return self.__nombre
    
    def eventos(self): #!!
        '''Retorna los eventos en los que está este participante.'''
        return [evento.obtenerNombre() for evento in self.__eventos]

class Organizador:
    '''Cada organizador tiene un nombre y un DNI.
    Cada organizador puede estar a cargo de uno o más eventos.'''
    def __init__(self, nombre:str, dni:int) -> None:
        self.__nombre = nombre
        self.__dni = dni
        self.__eventos = []

    #SETTERS
    def agregarEvento(self, evento:'Evento') -> None:
        self.__eventos.append(evento)

    #GETTERS
    def obtenerEventos(self): #
        '''Retorna los eventos que tiene a cargo el organizador.'''
        return [evento.obtenerNombre() for evento in self.__eventos]

class Tester:
    def testerTodo():
        # Creo los objetos
        Fecha1 = Fecha(1,1,2024)
        Fecha2 = Fecha(2,2,2024)
        Fecha3 = Fecha(25,12,2024)

        E1 = Evento("Cumpleanios", Fecha1, "Descrip...")
        E2 = Evento("Casamiento", Fecha2, "Descrip...")
        E3 = Evento("Navidad", Fecha3, "Descrip...")

        P1 = Participante("Abner", 44110066)
        P2 = Participante("Juan", 44110067)
        P3 = Participante("Pedro", 44110068)

        O1 = Organizador("Messi", 10101010)
        O2 = Organizador("CR7", 11111111)
        O3 = Organizador("Ronaldo", 12121212)
        print("Se crearon los objetos correctamente :)")

        # Agregar participantes a los eventos
        E1.asignarParticipante(P1)
        E1.asignarParticipante(P2)
        E1.asignarParticipante(P3)
        E2.asignarParticipante(P1)
        E2.asignarParticipante(P2)
        E3.asignarParticipante(P1)
        print("Se añadieron los participantes a los eventos correctamente :)")

        # Agregar eventos a los participantes
        P1.agregarEvento(E1)
        P2.agregarEvento(E1)
        P3.agregarEvento(E1)
        P1.agregarEvento(E2)
        P2.agregarEvento(E2)
        P1.agregarEvento(E3)
        print("Se añadieron los eventos a los participantes correctamente :)")

        # Agregar eventos a los organizadores
        O1.agregarEvento(E1)
        O2.agregarEvento(E1)
        O3.agregarEvento(E1)
        O1.agregarEvento(E2)
        O2.agregarEvento(E2)
        O1.agregarEvento(E3)
        print("Se añadieron los eventos a los organizadores correctamente :)")

        # Mostrar los eventos en los que está el participante 1 (P1)
        print(P1.eventos())

        # Mostrar los eventos que tiene un organizador
        print(f"Eventos del organizador 1: {O1.obtenerEventos()}")

        # Mostrar los participantes que tiene un evento (E1)
        print(f"Mostrar participantes del evento E1: {E1.mostrarParticipantes()}")

if __name__ == "__main__":
    Tester.testerTodo()
