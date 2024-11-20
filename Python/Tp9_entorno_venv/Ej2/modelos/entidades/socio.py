from datetime import datetime

class Socio:
    @classmethod
    def fromDiccionario(cls, dic:dict) -> 'Socio':
        return Socio(dic['dni'], dic['nombre'], dic['apellido'], dic['mail'], dic['fecha_nacimiento'])

    def __init__(self, dni:int, nombre:str, apellido:str, mail:str, fecha_nacimiento:'datetime'):
        if not isinstance(dni, int):
            raise ValueError("DNI debe ser un número entero.")
        if not isinstance(nombre, str):
            raise ValueError("Nombre debe ser una cadena de caracteres.")
        if not isinstance(apellido, str):
            raise ValueError("Apellido debe ser una cadena de caracteres.")
        if not isinstance(mail, str):
            raise ValueError("Mail debe ser una cadena de caracteres.")
        if not isinstance(fecha_nacimiento, datetime):
            raise ValueError("Fecha de nacimiento debe ser una instancia de datetime.")
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.fecha_nacimiento = fecha_nacimiento

    
    #SETTERS triviales:
    def establecerDni(self, dni:int):
        self.dni = dni

    def establecerNombre(self, nombre:str):
        self.nombre = nombre

    def establecerApellido(self, apellido:str):
        self.apellido = apellido

    def establecerMail(self, mail:str):
        self.mail = mail

    def establecerFechaNacimiento(self, fecha_nacimiento:'datetime'):
        self.fecha_nacimiento = fecha_nacimiento

    #GETTERS triviales:
    def obtenerDni(self) -> int:
        return self.dni
    
    def obtenerNombre(self) -> str:
        return self.nombre
    
    def obtenerApellido(self) -> str:
        return self.apellido
    
    def obtenerMail(self) -> str:
        return self.mail
    
    def obtenerFechaNacimiento(self) -> 'datetime':
        return self.fecha_nacimiento
    
    #Métodos adicionales:
    def esIgual(self, otro:'Socio') -> bool:
        return self.dni == otro.dni and self.nombre == otro.nombre and self.apellido == otro.apellido and self.mail == otro.mail and self.fecha_nacimiento == otro.fecha_nacimiento
    def __str__(self):
        return f"Socio(DNI: {self.dni}, Nombre: {self.nombre}, Apellido: {self.apellido}, Mail: {self.mail}, Fecha de Nacimiento: {self.fecha_nacimiento})"
    
    def toDiccionario(self) -> dict:
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "mail": self.mail,
            "fecha_nacimiento": self.fecha_nacimiento.strftime("%d/%m/%Y")
        }