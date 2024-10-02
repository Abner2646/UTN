class Fecha:
    def __init__(self, dia:int, mes:int, anio:int):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
    DIAS_X_MES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # COMANDOS
    def establecerDia(self, dia:int):
        self.__dia = dia

    def establecerMes(self, mes:int):
        self.__mes = mes

    def establecerAnio(self, anio:int):
        self.__anio = anio

    # CONSULTAS
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
        if self.__anio < otraFecha.__anio:
            return True
        if self.__anio > otraFecha.__anio:
            return False
        if self.__anio == otraFecha.__anio:
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

    # CONSULTAS
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

    # COMANDOS
    def establecerNombre(self, nombre:str) -> None:
        self.__nombre = nombre
    
    def establecerFechaNacimiento(self, fecha:Fecha):
        self.__nacimiento = fecha

    def establecerPenalizacion(self, fechaHasta:Fecha):
        '''actualiza el atributo de instancia fechaPenalizacion'''
        self.__fechaPenalizacion = fechaHasta
    
    # CONSULTAS
    def estaHabilitado(self, fecha:Fecha) -> bool:
        '''retorna True cuando no tiene fechaPenalizacion o cuando ésta es anterior a la fecha recibida en el parámetro'''
        if self.__fechaPenalizacion == None:
            return True
        elif self.__fechaPenalizacion.esAnterior(fecha):
            return True
        else:
            return False

    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self) -> Fecha:
        return self.__nacimiento
    
    def obtenerFechaPenalizacion(self) -> Fecha:
        return self.__fechaPenalizacion
    
    def toString(self) -> str:
        return f"Socio: {self.__nombre}, Nacimiento: {self.__nacimiento.obtenerFecha()}, Penalización hasta: {self.__fechaPenalizacion.obtenerFecha()}"


class Prestamo:
    def __init__ (self, libro:Libro, fechaPrestamo:Fecha, dias:int, socio:Socio):
        self.__libro = libro
        self.__fechaPrestamo = fechaPrestamo
        self.__dias = dias
        self.__socio = socio
        self.__fechaDevolucion = None  # Nueva variable para la fecha de devolución

    # COMANDOS
    def establecerFechaDevolucion(self, fechaDev:Fecha):
        '''Controla si el socio debe recibir una penalización, en caso afirmativo se le asigna.'''
        self.__fechaDevolucion = fechaDev
        if self.__fechaPrestamo.esAnterior(fechaDev) and (self.__fechaPrestamo.sumarDias(self.__dias) < fechaDev):
            self.__socio.establecerPenalizacion(fechaDev.sumarDias(10))

    # CONSULTAS
    def obtenerLibro(self) -> Libro:
        return self.__libro
    
    def obtenerFechaPrestamo(self) -> Fecha:
        return self.__fechaPrestamo
    
    def obtenerFechaDevolucion(self) -> Fecha:
        return self.__fechaDevolucion
    
    def estaAtrasado(self) -> bool:
        '''Devuelve True si la fecha de devolución es posterior a la fecha de plazo'''
        return self.__fechaDevolucion is not None and self.__fechaPrestamo.sumarDias(self.__dias) < self.__fechaDevolucion


class TesterPrestamo:
    @staticmethod
    def testearPrestamo():
        fechaPrestamo = Fecha(1, 1, 2024)
        fechaDevolucion = Fecha(15, 1, 2024)
        libro = Libro("El Quijote", "Cervantes", "Planeta", 'A')
        socio = Socio("Juan", fechaPrestamo, None)
        prestamo = Prestamo(libro, fechaPrestamo, 10, socio)
        
        prestamo.establecerFechaDevolucion(fechaDevolucion)
        print(prestamo.obtenerFechaDevolucion().obtenerFecha())
        print(socio.toString())


if __name__ == "__main__":
    TesterPrestamo.testearPrestamo()
