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
    
class Tester:
    @staticmethod
    def TestearFecha():
        #Establecer fecha
        dia = int(input("Ingrese un día: "))
        mes = int(input("Ingrese un mes: "))
        año = int(input("Ingrese un año: "))
        fecha1 = Fecha(dia, mes, año)
        print(fecha1.toString())

        #Establecer fecha dato por dato
        fecha1.establecerDia(5)
        fecha1.establecerMes(5)
        fecha1.establecerAño(2025)
        print(fecha1.toString())

        #Probar Fecha Valida:
        if fecha1.fechaValida():
            print("Fecha valida.")
        else:
            print("Fecha invalida.")

        #Probar obtener dia, mes y año por separado:
        print(f"Día: {fecha1.obtenerDia()}")
        print(f"Mes: {fecha1.obtenerMes()}")
        print(f"Año: {fecha1.obtenerAño()}")

        #Creo la fechca 2 y pruebo sumarDias()
        print("Probando fecha2. SumarDias: ")
        fecha2 = fecha1.sumaDias(5)
        print(fecha2.toString())

        #Pruebo diaSiguiente()
        print("Probando fecha2. diaSiguiente: ")
        fecha2 = fecha1.diaSiguiente()
        print(fecha2.toString())

        #Pruebo esAnterior()
        if fecha2.esAnterior(fecha1):
            print("Es anterior.")
        else:
            print("No es anterior.")


        #Pruebo esIgual()
        if fecha1.esIgualQue(fecha2):
            print("Es igual.")
        else:
            print("No es igual.")

if __name__ == "__main__":
    Tester.TestearFecha()