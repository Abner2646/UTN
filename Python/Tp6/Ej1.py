from Tp5_1.ej2 import Fecha

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
        fechaPrestamo = None

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
    
    def obtenerFechaDevolucion(self) ->'Fecha': #!!
        '''retorna la fecha en la que efectivamente se realizó la devolución del libro'''

    def estaAtrasado (self, fecha:'Fecha') -> bool: #!!
        return
    

    def penalizacion(self) -> 'Fecha': #!!
        pass

    def toString(self) -> str:
        return f"Libro: {self.__libro}, Socio: {self.__socio}, Fecha Prestamo: {self.__fechaPrestamo}, Fecha Devolucion: {self.obtenerFechaDevolucion()}"
    
    