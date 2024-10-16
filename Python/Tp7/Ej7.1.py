from abc import ABC, abstractmethod
from datetime import datetime

class Empresa:
    def __init__(self):
        self.empleados = []

    def agregarEmpleado(self, empleado: 'Empleado'):
        self.empleados.append(empleado)

    def mostrarEmpleados(self):
        for empleado in self.empleados:
            print(empleado)

    def empleadoConMasClientes(self) -> 'EmpleadoAComision':
        # Suponemos que solo los empleados a comisión tienen clientes.
        empleados_comision = [emp for emp in self.empleados if isinstance(emp, EmpleadoAComision)]
        if not empleados_comision:
            return None
        return max(empleados_comision, key=lambda emp: emp.obtenerCantClientesCaptados())

    def esIgualQue(self, otra_empresa: 'Empresa') -> bool:
        return set(self.empleados) == set(otra_empresa.empleados)

class Empleado(ABC):
    @abstractmethod
    def __init__(self, dni: str, nombre: str, apellido: str, anioIngreso: int):
        self._dni = dni
        self._nombre = nombre
        self._apellido = apellido
        self._anioIngreso = anioIngreso

    # SETTERS:
    def establecerDni(self, dni: int):
        self._dni = dni

    def establecerNombre(self, nombre: str):
        self._nombre = nombre

    def establecerApellido(self, apellido: str):
        self._apellido = apellido

    def establecerAnioIngreso(self, anioIngreso: int):
        self._anioIngreso = anioIngreso

    # GETTERS:
    @abstractmethod
    def obtenerSalario(self) -> float:
        pass

    def nombreCompleto(self) -> str:
        return f"{self._nombre} {self._apellido}"

    def antiguedadEnAnios(self) -> int:
        anio_actual = datetime.now().year
        return anio_actual - self._anioIngreso

    def __str__(self):
        return f"Empleado: {self.nombreCompleto()}, DNI: {self._dni}, Antigüedad: {self.antiguedadEnAnios()} años"

class EmpleadoAComision(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, salarioMinimo: float, cantClientesCaptados: int, montoPorCliente: float):
        super().__init__(dni, nombre, apellido, anioIngreso)
        self.__salarioMinimo = salarioMinimo
        self.__cantClientesCaptados = cantClientesCaptados
        self.__montoPorCliente = montoPorCliente

    def obtenerSalario(self) -> float:
        salario_por_clientes = self.__cantClientesCaptados * self.__montoPorCliente
        return max(salario_por_clientes, self.__salarioMinimo)

    def obtenerCantClientesCaptados(self) -> int:
        return self.__cantClientesCaptados

class EmpleadoSalarioFijo(Empleado):
    # Atributos de clase:
    __PORC_2_A_5 = 0.05
    __PORC_MAS_DE_5 = 0.1
    __ANIO_LIMITE_INFERIOR = 2
    __ANIO_LIMITE_SUPERIOR = 5

    def __init__(self, dni, nombre, apellido, anioIngreso, sueldoBasico: float):
        super().__init__(dni, nombre, apellido, anioIngreso)
        self.__sueldoBasico = sueldoBasico

    def obtenerSalario(self) -> float:
        return self.__sueldoBasico * (1 + self.obtenerPorcentajeAdicional())

    def obtenerPorcentajeAdicional(self) -> float:
        antiguedad = self.antiguedadEnAnios()
        if antiguedad < EmpleadoSalarioFijo.__ANIO_LIMITE_INFERIOR:
            return 0
        elif antiguedad <= EmpleadoSalarioFijo.__ANIO_LIMITE_SUPERIOR:
            return EmpleadoSalarioFijo.__PORC_2_A_5
        else:
            return EmpleadoSalarioFijo.__PORC_MAS_DE_5

class Tester:
    @staticmethod
    def test():
        empresa = Empresa()
        e1 = EmpleadoAComision("123", "Pedro", "Perez", 2023, 500000, 100, 20)
        e2 = EmpleadoAComision("234", "Ana", "Gonzalez", 2020, 400000, 50, 30)
        e3 = EmpleadoSalarioFijo("345", "Maria", "Alvarez", 2015, 800000)
        e4 = EmpleadoSalarioFijo("456", "Matias", "Perez", 2018, 700000)

        empresa.agregarEmpleado(e1)
        empresa.agregarEmpleado(e2)
        empresa.agregarEmpleado(e3)
        empresa.agregarEmpleado(e4)

        print("Empleados de la empresa:")
        empresa.mostrarEmpleados()

        print("\nEmpleado con más clientes captados:")
        print(empresa.empleadoConMasClientes())

        empresa2 = Empresa()
        empresa2.agregarEmpleado(e1)
        empresa2.agregarEmpleado(e2)
        empresa2.agregarEmpleado(e3)
        empresa2.agregarEmpleado(e4)

        print("\n¿Son iguales las dos empresas?")
        print(empresa.esIgualQue(empresa2))

        e2 = e1
        print("\nComparación de empleados:")
        print(e1 == e2)

if __name__ == "__main__":
    Tester.test()
