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
    def __init__ (self, nombre:str, autor:str, editorial:str, categoria:str):
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria

    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerAutor(self) -> str:
        return self.__autor
    
    def obtenerEditorial(self) -> str:
        return self.__editorial
    
    def obtenerCategoria(self) -> str:
        return self.__categoria
    
    def toString(self) -> str:
        return f"Nombre: {self.__nombre}, Autor: {self.__autor}, Editorial: {self.__editorial}, Categoria: {self.__categoria}."
    
class Socio:
    def __init__(self, nombre:str, nacimiento:'Fecha') -> None:
        self.__nombre = nombre
        self.__fechaNacimiento = nacimiento
    
    #SETTERS
    def establecerNombre(self, nombre:str) -> None:
        self.__nombre = nombre

    def establecerFechaNacimiento (self, fecha:'Fecha') -> None:
        self.__fechaNacimiento = fecha

    def establecerPenalizacion (self, fechaHasta:'Fecha') -> None:
        self.__fechaPenalizacion = fechaHasta


    #GETTERS:
    def estaHabilitado (self, fecha:'Fecha') -> bool:
        '''retorna True cuando no tiene
        fechaPenalizacion o cuando ésta es anterior a la fecha recibida en el
        parámetro.'''
        if self.__fechaPenalizacion == None or self.__fechaPenalizacion < fecha:
            return True
        else:
            return False

    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self) -> 'Fecha':
        return self.__fechaNacimiento
    
    def obtenerFechaPenalizacion(self) -> 'Fecha':
        '''Devuelve la fecha hasta la que está penalizado.'''
        return self.__fechaPenalizacion

    def toString(self) -> str:
        return f"Nombre: {self.__nombre}, Fecha Nacimiento: {self.__fechaNacimiento}, Penalizado hasta: {self.__fechaPenalizacion}."
    
class Prestamo:
    def __init__(self, libro:'Libro', fechaPrestamo:'Fecha', cantDias:int, socio:'Socio') -> None:
        self.__libro = libro
        self.__socio = socio
        self.__fechaPrestamo = fechaPrestamo
        self.__dias = cantDias
        self.__fechaDevolucion = None

    #SETTERS
    def establecerFechaDevolucion(self, fechaDev:'Fecha'): #!!
        '''recibe como parámetro la fecha en la que
        efectivamente se realizó la devolución del libro, y controla si el socio debe
        recibir una penalización, en caso afirmativo se le asigna al socio la fecha de
        penalización.'''

    #GETTERS
    def obtenerLibro(self) -> 'Libro':
        return self.__libro
    
    def obtenerFechaPrestamo(self) -> 'Fecha':
        '''Retorna la fecha en la ques e hizo el prestamos.'''
        return self.__fechaPrestamo
    
    def obtenerFechaDevolucion(self) ->'Fecha':
        '''retorna la fecha en la que efectivamente se realizó la devolución del libro'''
        return self.__fechaDevolucion
    def estaAtrasado (self, fecha:'Fecha') -> bool:
        ''' recibe como parámetro la fecha actual y retorna verdadero si el
        libro no se devolvió y ya debería haberse devuelto de acuerdo a la fecha de
        préstamo y la cantidad de días'''
        if fecha.esAnterior(self.__fechaDevolucion):
            return True
        else:
            return False

    def penalizacion(self) -> 'Fecha': #!!??
        '''calcula la cantidad de días de penalización y devuelve la fecha
        hasta la que corresponde aplicar la penalización, a partir de la fecha de
        devolución, que tiene que estar ligada. La penalización es de 3 días si se
        atrasó menos de una semana, 5 días si se atrasó menos de tres semanas y
        10 días si se atrasó 3 semanas o más. Si el libro tiene categoría A los días de
        penalización se duplican.
        A. Implemente el diagrama completo.
        B. Implemente una clase tester para verificar los servicios de la clase Préstamo,
        algunos casos con valores fijos y otros casos pidiendo datos al usuario.'''

    def toString(self) -> str:
        return f"Libro: {self.__libro}, Socio: {self.__socio}, Fecha Prestamo: {self.__fechaPrestamo}, Fecha Devolucion: {self.obtenerFechaDevolucion()}"
    
class Tester:
    def testerx():
        fechaPrestamo = Fecha (1,1,2024)
        fechaDevolucion = Fecha(1, 1, 2024)
        Libro1 = Libro ("El principito", "Antoine", "Estampa", "A")
        Socio1 = Socio ("Abner", fechaPrestamo, fechaDevolucion, )
        Prestamo1 = Prestamo(Libro1, )



if __name__ == "__main__":
    Tester.testerx()
    
