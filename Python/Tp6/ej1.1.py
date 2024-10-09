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

class Libro:
    def __init__(self, nombre:str, autor:str, editorial:str, categoria:str) -> None:
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria

    def obtenerNombre(self):
        return self.__nombre
    
    def obtenerAutor(self):
        return self.__autor
    
    def obtenerEditorial(self):
        return self.__autor
    
    def obtenerCategoria(self):
        return self.__categoria
    
class Socio:
    def __init__(self, nombre:str, nacimiento:'Fecha') -> None:
        self.__nombre = nombre
        self.__fechaNacimiento = nacimiento
        self.__fechaPenalizacion = None

    #COMANDOS
    def establecerNombre(self, nombre:str) -> None:
        self.__nombre = nombre

    def establecerFechaNacimiento(self, fecha:'Fecha') -> None:
        self.__fechaNacimiento = fecha
    
    def establecerPenalizacion (self, fechaHasta:'Fecha') -> None:
        '''En el caso que el libro se haya devuelto fuera del plazo permitido se calcula
        una penalización al socio, que puede ser de 3 días si se atrasó menos de una
        semana (menos de 7 días), 5 días si se atrasó menos de tres semanas (menos de
        21 días) y 10 días si se atrasó 3 semanas o más (21 días o más). Además, si el libro
        tiene categoría A los días de penalización se duplican'''
        pass
    
    #CONSULTAS
    def estaHabilitado(self, fecha:'Fecha') -> bool:
        if self.__fechaPenalizacion == None or self.__fechaPenalizacion.esAnterior(fecha):
            return True
        else:
            return False
    
    def obtnerNombre(self) -> str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self) -> 'Fecha':
        return self.__fechaNacimiento
    
    def obtenerFechaPenalizacion(self) -> 'Fecha':
        return self.__fechaPenalizacion
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Fecha de Nacimiento: {self.__fechaNacimiento.toString()}"
    
class Prestamo:
    def __init__(self, libro:'Libro', fechaPrestamo:'Fecha', cantDias:int, socio:'Socio') -> None:
        self.__libro = libro
        self.__fechaPrestamos = fechaPrestamo
        self.__dias = cantDias
        self.__socio = socio
        self.__fechaDevolucion = None

    #COMANDOS:
    def establecerFechaDevolucion(self, fechaDev:'Fecha') -> None:
        self.__fechaDevolucion = fechaDev

    #CONSULTAS:
    def obtenerLibro(self) -> 'Libro':
        return self.__libro
    
    def obtenerFechaPrestamo(self) -> 'Fecha':
        return self.__fechaPrestamos
    
    def 