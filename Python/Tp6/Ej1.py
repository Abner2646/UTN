class Fecha:
    def __init__(self, dia:int, mes:int, anio:int):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
    DIAS_X_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #COMANDOS

    def establecerDia(self, dia:int):
        self.__dia = dia

    def establecerMes(self, mes:int):
        self.__mes = mes

    def establecerAnio(self, anio:int):
        self.__anio = anio

    #CONSULTAS
    def obtenerDia(self):
        return self.__dia
    
    def obtenerMes(self):
        return self.__mes
    
    def obtenerAnio(self):
        return self.__anio
    
    def obtenerFecha(self):
        print(f"La fecha es: {self.__dia}, {self.__mes}, {self.__anio}")
    
    def esAnterior(self, otraFecha):
        '''Compara self contra otraFecha'''
        #A < A
        if self.__anio < otraFecha.__anio:
            return True
        #A > A
        if self.__anio > otraFecha.__anio:
            return False
        #A == A
        if self.__anio == otraFecha.__anio:
            #M < M
            if self.__mes < otraFecha.__mes:
                return True
            if self.__mes > otraFecha.__mes:
                return False
            if self.__mes == otraFecha.__mes:
                if self.__dia < otraFecha.__dia:
                    return True
                if self.__dia > otraFecha.__dia:
                    return False
                if self.__dia == otraFecha.__dia:
                    return False
    
    def diaSiguiente(self):
        self.sumarDias(1)
    
    def sumarDias(self, cantDias:int):
        for i in range(cantDias):
            if self.__dia + 1 > self.DIAS_X_MES[self.__mes - 1]:
                if self.__mes == 12:
                    self.__mes = 1
                    self.__anio += 1
                    self.__dia = 1
                else:
                    self.__mes += 1
                    self.__dia = 1
            else:
                self.__dia += 1

class Libro:
    def __init__(self, nombre:str, autor:str, editorial:str, categoria:chr) -> None:
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria

    #CONSULTAS
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerAutor(self) -> str:
        return self.__autor
    
    def obtenerEditorial(self) -> str:
        return self.__editorial
        
    def obtenerCategoria(self) -> str:
        return self.__categoria

    def toString(self) -> str:
        return (f"Libro: {self.__nombre}, Autor: {self.__autor}, Editorial: {self.__editorial}, Categoría: {self.__categoria}.")

class Socio:
    def __init__(self, nombre, fechaNacimiento, fechaPenalizacion) -> None:
        self.__nombre = nombre
        self.__nacimiento = fechaNacimiento
        self.__fechaPenalizacion = fechaPenalizacion

    #COMNADOS
    def establecerNombre(self, nombre:str) -> None:
        self.__nombre = nombre
    
    def establecerFechaNacimiento(self, fecha:Fecha):
        self.__fechaNacimiento = fecha

    def establecerPenalizacion(self, fechaHasta:Fecha):
        '''actualiza el atributo de instancia fechaPenalizacion'''
        self.__fechaPenalizacion = fechaHasta
    
    #CONSULTAS
    def estaHabilitado(self, fecha:Fecha) -> bool: #!!...
        '''retorna True cuando no tiene fechaPenalizacion o cuando ésta es anterior a la fecha recibida en el parámetro'''
        #3 días si se atraso menos de una semana
        #5 días si se atrasó menos de 21 días
        #10 días si se atrasó +21 días
        #Si el libro tiene categoría A los días se suplican
        if self.__fechaPenalizacion == None:
            return True
        elif self.__fechaPenalizacion < fecha:
            True
        else:
            return False

    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self) -> Fecha:
        return self.__nacimiento
    
    def obtenerFechaDevolucion(self) -> Fecha:
        return self.__fechaDEvolucion
    
    def obtenerFechaPenalizacion(self) -> Fecha:
        return self.__fechaPenalizacion
    
    def toString(self) -> str:
        return f"Socio: {self.__nombre}, Nacimiento: {self.__fechaNacimiento}, Penalización hasta: {self.__fechaPenalizacion}"

class Prestamo:
    def __init__ (self, libro:Libro, fechaPrestamo:Fecha, dias:int, Socio:Socio):
        self.__libro = libro
        self.__fechaPrestamo = fechaPrestamo
        self.__dias = dias
        self.__socio = Socio
    
    #COMANDOS
    def establecerFechaDevolucion(self, fechaDev:Fecha): #!!
        '''recibe como parámetro la fecha en la que
        efectivamente se realizó la devolución del libro, y controla si el socio debe
        recibir una penalización, en caso afirmativo se le asigna al socio la fecha de
        penalización'''
        if self.__fechaPrestamo + 10 < fechaDev:
            Socio.establecerPenalizacion(fechaDev.sumarDias(10))

        #en caso afirmativo se le asigna al socio la fecha de penalización

    #CONSULTAS
    def obtenerLibro(self) -> Libro:
        return self.__libro
    
    def obtenerFechaPrestamo(self) -> Fecha:
        return self.__fechaPrestamo
    
    def obtenerFechaDevolucion(self) -> Fecha: #!!
        return self.__fe
    
    def estaAtrasado(self, fecha:Fecha) -> Fecha: #!!
        return 0

    def pensalizacion(self) -> Fecha: #!!
        return 0

class TesterPrestamo:
    def testearPrestamo():
        fecha1 = Fecha(1, 1, 2024)





if __name__ == "__main__":
    TesterPrestamo.testearPrestamo()



#Dudas:
#No sé sobrescribir métodos ni constructores
#No sé la sintaxis de herencia
#¿Qué pasa cuando en el diagrama del enunciado hay atributos de clase que no están en el constructor
#No sé hacer try excepts
#Ecuals? Qué es?

#Tiene una clase -> 
#Usa otra clase -> 
#__variavle (privada)
#_variable (protegida) (para que pueda heredar)
#super() es para acceder al constructor¿ o variables¿ de la clase base
#Qué pasa si llamo a una función de la clase fecha pero no inicialice la fecha actual?

#Prompt.
#Recorda que soy argentino, no escribas variables innecesariamente en inglés. Ej: La variable "matrix" yo la suelo escribir "matriz"
#No escribas con acentos.
#Escribí para cada metodo de clase, excepto para los getters, una breve descripción usando docstring


#class Tester:
    #def tester():
        #Ingresar las fechas:
        #fecha1 = Fecha(1, 1, 3000)
        #fecha2 = Fecha(1, 1, 2000)

        #esAnterior
        #if fecha1.esAnterior(fecha2) == True:
        #    print("Es anterior.")
        #else:
        #    print("No es anterior.")
        
        #diaSiguiente
        #fecha1.diaSiguiente() #Actualiza fecha
        #fecha1.obtenerFecha() #Muestra fecha

        #sumarDias
        #fecha1.sumarDias(365) #Actualiza fecha
        #fecha1.obtenerFecha() #Muestra fecha