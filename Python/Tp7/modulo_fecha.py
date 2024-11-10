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
