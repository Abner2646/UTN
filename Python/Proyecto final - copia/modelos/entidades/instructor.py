class Instructor:
    def __init__(self, dni:int, nombre:str, apellido:str, email:str):
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un dato de tipo entero.")
        if not isinstance(nombre, str) or not nombre.isalpha():
            raise ValueError("El nombre debe ser un dato de tipo string y solo puede contener letras.")
        if not isinstance(apellido, str) or not apellido.isalpha():
            raise ValueError("El apellido debe ser un dato de tipo string y solo puede contener letras.")
        if not isinstance(email, str) or not "@" in email:
            raise ValueError("El email debe ser un dato de tipo string y debe contener un '@'.")
        
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__cursoQueDicta = []

    #GETTERS triviales:
    def get_dni(self) -> int:
        return self.__dni
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_apellido(self) -> str:
        return self.__apellido
    
    def get_email(self) -> str:
        return self.__email
    
    #SETTERS triviales:
    def set_dni(self, dni:int):
        if not isinstance(dni, int):
            raise ValueError("El DNI debe ser un dato de tipo entero.")
        self.__dni = dni

    def set_nombre(self, nombre:str):
        if not isinstance(nombre, str) or not nombre.isalpha():
            raise ValueError("El nombre debe ser un dato de tipo string y solo puede contener letras.")
        self.__nombre = nombre

    def set_apellido(self, apellido:str):
        if not isinstance(apellido, str) or not apellido.isalpha():
            raise ValueError("El apellido debe ser un dato de tipo string y solo puede contener letras.")
        self.__apellido = apellido

    def set_email(self, email:str):
        if not isinstance(email, str) or not "@" in email:
            raise ValueError("El email debe ser un dato de tipo string y debe contener un '@'.")
        self.__email = email

    def set_cursoQueDicta(self, cursoQueDicta) -> None:
        if not isinstance(cursoQueDicta, (list, int)):
            raise ValueError("El curso debe ser un dato de tipo entero.")
        if isinstance(cursoQueDicta, int):
            self.__cursoQueDicta.append(cursoQueDicta)
        else:
            for curso in cursoQueDicta:
                if not isinstance(curso, int):
                    raise ValueError("Todos los elementos de la lista de cursos debe ser de tipo entero.")
                self.__cursoQueDicta.append(curso)

    #Otros metodos:
    def to_dict(self):
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "email": self.__email,
            "cursoQueDicta": self.__cursoQueDicta
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        if not isinstance(data, dict):
            raise ValueError("El dato debe ser un diccionario.")
        if "dni" not in data or "nombre" not in data or "apellido" not in data or "email" not in data:
            raise ValueError("El diccionario debe contener las claves 'dni', 'nombre', 'apellido', y 'email'.")

        #Creo una instancia de Instructor y paso por parametro los valores del diccionario
        return cls(data["dni"], nombre=data["nombre"], apellido=data["apellido"], email=data["email"])

    def __str__(self):
        return f"DNI: {self.__dni}, Nombre: {self.__nombre} {self.__apellido}, Email: {self.__email}"