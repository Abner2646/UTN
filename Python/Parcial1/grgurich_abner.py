from abc import ABC, abstractmethod

class Entrenador:
    def __init__(self, DNI: int, nombre: str, apellido: str, mail: str, especialidad: str):
        """
        Constructor para la clase Entrenador. Valida los tipos de datos de los atributos.
        """
        if not isinstance(DNI, int):
            raise TypeError("El DNI debe ser un entero")
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string")
        if not isinstance(apellido, str):
            raise TypeError("El apellido debe ser un string")
        if not isinstance(mail, str):
            raise TypeError("El mail debe ser un string")
        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser un string")
        
        self.__DNI = DNI
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__especialidad = especialidad

    # SETTERS:
    def establecerDNI(self, dni: int):
        """Establece el DNI del entrenador, validando que sea entero."""
        if not isinstance(dni, int):
            raise TypeError("El DNI debe ser un entero")
        self.__DNI = dni

    def establecerNombre(self, nombre: str):
        """Establece el nombre del entrenador, validando que sea un string."""
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string")
        self.__nombre = nombre

    def establecerApellido(self, apellido: str):
        """Establece el apellido del entrenador, validando que sea un string."""
        if not isinstance(apellido, str):
            raise TypeError("El apellido debe ser un string")
        self.__apellido = apellido

    def establecerMail(self, mail: str):
        """Establece el mail del entrenador, validando que sea un string."""
        if not isinstance(mail, str):
            raise TypeError("El mail debe ser un string")
        self.__mail = mail

    def establecerEspecialidad(self, especialidad: str):
        """Establece la especialidad del entrenador, validando que sea un string."""
        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser un string")
        self.__especialidad = especialidad

    # GETTERS:
    def obtenerDNI(self) -> int:
        """Devuelve el DNI del entrenador."""
        return self.__DNI

    def obtenerNombre(self) -> str:
        """Devuelve el nombre del entrenador."""
        return self.__nombre

    def obtenerApellido(self) -> str:
        """Devuelve el apellido del entrenador."""
        return self.__apellido

    def obtenerMail(self) -> str:
        """Devuelve el mail del entrenador."""
        return self.__mail

    def obtenerEspecialidad(self) -> str:
        """Devuelve la especialidad del entrenador."""
        return self.__especialidad

    def __str__(self):
        """Devuelve una cadena representativa del entrenador."""
        return f"Entrenador: {self.__nombre} {self.__apellido} - DNI: {self.__DNI} - Mail: {self.__mail} - Especialidad: {self.__especialidad}"


class Clase(ABC):
    @abstractmethod
    def __init__(self, nombre: str, duracion: int, horaInicio: str, horaFin: str, precio: float):
        """
        Constructor abstracto para la clase base Clase.
        Valida los tipos de los atributos comunes a todas las clases.
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string")
        if not isinstance(duracion, int):
            raise TypeError("La duración debe ser un entero")
        if not isinstance(horaInicio, str):
            raise TypeError("La hora de inicio debe ser un string")
        if not isinstance(horaFin, str):
            raise TypeError("La hora de fin debe ser un string")
        if not isinstance(precio, float):
            raise TypeError("El precio debe ser un número decimal")

        self._nombre = nombre
        self._duracion = duracion
        self._horaInicio = horaInicio
        self._horaFin = horaFin
        self._precio = precio

    # SETTERS
    def establecerEntrenador(self, entrenador: 'Entrenador'):
        """Establece el entrenador de la clase, validando que sea de tipo Entrenador."""
        if not isinstance(entrenador, Entrenador):
            raise TypeError("El entrenador debe ser una instancia de la clase Entrenador")
        self._entrenador = entrenador

    def establecerNombre(self, nombre: str):
        """Establece el nombre de la clase."""
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un string")
        self._nombre = nombre

    def establecerDuracion(self, duracion: int):
        """Establece la duración de la clase."""
        if not isinstance(duracion, int):
            raise TypeError("La duración debe ser un entero")
        self._duracion = duracion

    def establecerHoraInicio(self, horaInicio: str):
        """Establece la hora de inicio de la clase."""
        if not isinstance(horaInicio, str):
            raise TypeError("La hora de inicio debe ser un string")
        self._horaInicio = horaInicio

    def establecerHoraFin(self, horaFin: str):
        """Establece la hora de fin de la clase."""
        if not isinstance(horaFin, str):
            raise TypeError("La hora de fin debe ser un string")
        self._horaFin = horaFin

    def establecerPrecio(self, precio: float):
        """Establece el precio de la clase."""
        if not isinstance(precio, float):
            raise TypeError("El precio debe ser un número decimal")
        self._precio = precio

    # GETTERS
    def obtenerNombre(self) -> str:
        """Devuelve el nombre de la clase."""
        return self._nombre

    def obtenerDuracion(self) -> int:
        """Devuelve la duración de la clase."""
        return self._duracion

    def obtenerHoraInicio(self) -> str:
        """Devuelve la hora de inicio de la clase."""
        return self._horaInicio

    def obtenerHoraFin(self) -> str:
        """Devuelve la hora de fin de la clase."""
        return self._horaFin

    def obtenerPrecio(self) -> float:
        """Devuelve el precio de la clase."""
        return self._precio

    @abstractmethod
    def hayLugar(self) -> bool:
        """Método abstracto que indica si hay lugar en la clase."""
        pass

    @abstractmethod
    def obtenerDescripcion(self) -> str:
        """Método abstracto para obtener la descripción de la clase."""
        pass


class ClaseGrupal(Clase):
    def __init__(self, nombre: str, duracion: int, horaInicio: str, horaFin: str, precio: float, maxParticipantes: int):
        super().__init__(nombre, duracion, horaInicio, horaFin, precio)
        if not isinstance(maxParticipantes, int):
            raise TypeError("El máximo de participantes debe ser un entero")
        self.__maxParticipantes = maxParticipantes
        self.__cantInscriptos = 0

    # SETTERS
    def establecerMaxParticipantes(self, maxParticipantes: int):
        """Establece el máximo de participantes para la clase grupal."""
        if not isinstance(maxParticipantes, int):
            raise TypeError("El máximo de participantes debe ser un entero")
        self.__maxParticipantes = maxParticipantes

    def establecerCantInscriptos(self, cantInscriptos: int):
        """Establece la cantidad de inscriptos, validando que no supere el máximo permitido."""
        if not isinstance(cantInscriptos, int):
            raise TypeError("La cantidad de inscriptos debe ser un entero")
        if cantInscriptos > self.__maxParticipantes:
            raise ValueError("La cantidad de inscriptos no puede superar el máximo de participantes")
        self.__cantInscriptos = cantInscriptos

    def registrarInscripto(self):
        """Registra un nuevo inscripto si hay lugar en la clase."""
        if self.hayLugar():
            self.__cantInscriptos += 1

    # GETTERS
    def obtenerMaxParticipantes(self) -> int:
        """Devuelve el máximo de participantes de la clase grupal."""
        return self.__maxParticipantes

    def obtenerCantInscriptos(self) -> int:
        """Devuelve la cantidad actual de inscriptos."""
        return self.__cantInscriptos

    def hayLugar(self) -> bool:
        """Indica si hay lugar en la clase grupal."""
        return self.__cantInscriptos < self.__maxParticipantes

    def obtenerDescripcion(self) -> str:
        """Devuelve la descripción de la clase grupal."""
        return (f"Clase Grupal: {self._nombre} - Duración: {self._duracion} horas - "
                f"Hora de Inicio: {self._horaInicio} - Hora de Fin: {self._horaFin} - "
                f"Precio: {self._precio} - Inscriptos: {self.__cantInscriptos}/{self.__maxParticipantes}")


class ClaseIndividual(Clase):
    def __init__(self, nombre: str, duracion: int, horaInicio: str, horaFin: str, precio: float, ocupada: bool):
        """
        Constructor para las clases individuales. Añade el estado de ocupación.
        """
        super().__init__(nombre, duracion, horaInicio, horaFin, precio)  # Llama al constructor de la clase base
        if not isinstance(ocupada, bool):
            raise TypeError("El estado de ocupación debe ser un booleano")
        self.__ocupada = ocupada

    def obtenerDescripcion(self) -> str:
        """Devuelve la descripción de la clase individual."""
        estado = "Ocupada" if not self.hayLugar() else "Libre"
        return (f"Clase Individual: {self._nombre} - Duración: {self._duracion} horas - "
                f"Hora de Inicio: {self._horaInicio} - Hora de Fin: {self._horaFin} - "
                f"Precio: {self._precio} - Estado: {estado}")

    def hayLugar(self) -> bool:
        """Indica si la clase individual está libre (no ocupada)."""
        return not self.__ocupada

    def establecerInscripto(self):
        """Registra la clase como ocupada si está libre."""
        if self.hayLugar():
            self.__ocupada = True


class Tester:
    @staticmethod
    def test_entrenador():
        try:
            print("Probando clase Entrenador...")
            entrenador = Entrenador(12345678, "Juan", "Pérez", "juan.perez@mail.com", "CrossFit")
            assert entrenador.obtenerDNI() == 12345678
            assert entrenador.obtenerNombre() == "Juan"
            assert entrenador.obtenerApellido() == "Pérez"
            assert entrenador.obtenerMail() == "juan.perez@mail.com"
            assert entrenador.obtenerEspecialidad() == "CrossFit"
            print("Test Entrenador pasó con éxito.\n")
        except Exception as e:
            print(f"Test Entrenador falló: {e}\n")

    @staticmethod
    def test_clase_grupal():
        try:
            print("Probando clase ClaseGrupal...")
            clase_grupal = ClaseGrupal("Yoga", 60, "10:00", "11:00", 15.0, 20)
            assert clase_grupal.obtenerNombre() == "Yoga"
            assert clase_grupal.obtenerDuracion() == 60
            assert clase_grupal.obtenerHoraInicio() == "10:00"
            assert clase_grupal.obtenerHoraFin() == "11:00"
            assert clase_grupal.obtenerPrecio() == 15.0
            assert clase_grupal.obtenerMaxParticipantes() == 20
            assert clase_grupal.obtenerCantInscriptos() == 0

            clase_grupal.registrarInscripto()
            assert clase_grupal.obtenerCantInscriptos() == 1
            assert clase_grupal.hayLugar() is True

            for _ in range(19):
                clase_grupal.registrarInscripto()

            assert clase_grupal.obtenerCantInscriptos() == 20
            assert clase_grupal.hayLugar() is False

            print("Test ClaseGrupal pasó con éxito.\n")
        except Exception as e:
            print(f"Test ClaseGrupal falló: {e}\n")

    @staticmethod
    def test_clase_individual():
        try:
            print("Probando clase ClaseIndividual...")
            clase_individual = ClaseIndividual("Personal Trainer", 45, "15:00", "15:45", 30.0, False)
            assert clase_individual.obtenerNombre() == "Personal Trainer"
            assert clase_individual.obtenerDuracion() == 45
            assert clase_individual.obtenerHoraInicio() == "15:00"
            assert clase_individual.obtenerHoraFin() == "15:45"
            assert clase_individual.obtenerPrecio() == 30.0
            assert clase_individual.hayLugar() is True

            clase_individual.establecerInscripto()
            assert clase_individual.hayLugar() is False

            print("Test ClaseIndividual pasó con éxito.\n")
        except Exception as e:
            print(f"Test ClaseIndividual falló: {e}\n")

