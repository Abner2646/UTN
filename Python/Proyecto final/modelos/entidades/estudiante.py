class Estudiante:
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
        self.__cursoQueToma = []

    #GETTERS triviales:
    def get_dni(self) -> int:
        return self.__dni
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_apellido(self) -> str:
        return self.__apellido
    
    def get_email(self) -> str:
        return self.__email
    
    def get_cursoQueToma(self) -> int:
        return self.__cursoQueToma
    
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

    def set_cursoQueToma(self, cursoQueToma:int) -> None:
        if not isinstance(cursoQueToma, int):
            raise ValueError("El curso debe ser un dato de tipo entero.")
        self.__cursoQueToma.append(cursoQueToma)

    def eliminarCursoQueToma(self, cursoQueToma) -> None:
        if not isinstance(cursoQueToma, int):
            raise ValueError("El curso debe ser un dato de tipo entero.")
        if cursoQueToma in self.__cursoQueToma:
            self.__cursoQueToma.remove(cursoQueToma)
        else:
            raise ValueError("El estudiante no toma el curso indicado.")

    #Otros metodos:
    def to_dict(self):
        return {
            "dni": self.__dni,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "email": self.__email,
            "cursoQueToma": self.__cursoQueToma
        }
    @classmethod
    def from_dict(cls, data: dict):
        if not isinstance(data, dict):
            raise ValueError("El dato debe ser un diccionario.")
        if "dni" not in data or "nombre" not in data or "apellido" not in data or "email" not in data:
            raise ValueError("El diccionario debe contener las claves 'dni', 'nombre', 'apellido', y 'email'.")

        # Crear una instancia de Estudiante
        estudiante = cls(data["dni"], nombre=data["nombre"], apellido=data["apellido"], email=data["email"])

        # Cargar los cursos si están presentes en el diccionario
        if "cursoQueToma" in data and isinstance(data["cursoQueToma"], list):
            for curso in data["cursoQueToma"]:
                estudiante.set_cursoQueToma(curso)

        return estudiante



    def __str__(self):
        return f"DNI: {self.__dni}, Nombre: {self.__nombre} {self.__apellido}, Email: {self.__email}"