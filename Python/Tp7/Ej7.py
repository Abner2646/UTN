from modulo_fecha import Fecha
from abc import ABC, abstractmethod

'''Tengo error en 'agregar empleado', un empleado no puede agregar a otro, es un error conceptual'''

class Empleado(ABC):
    @abstractmethod
    #número de DNI, nombre, apellido y fecha de ingreso
    def __init__(self, dni:str, nombre:str, fechaIngreso:'Fecha'):
        self._dni = dni
        self._nombre = nombre
        self._fechaIngreso = fechaIngreso
        self._salario = 0
        self._comision = 0
        self._empleados = []
        
    #SETTERS:
    def agregarEmpelado(self, empleado:'Empleado') -> None:
        self._empleados.append(empleado)

    def eliminarEmpleado(self, empleado:'Empleado') -> None:
        if empleado in self._empleados:
            self._empleados.remove(empleado)

    #GETTERS:
    def obtenerSueldo(self) -> float:
        pass

    def mayorComision(self) -> 'Empleado': #!!
        '''Retorna el empleado de mayor comision'''
        pass

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, fechaIngreso, salarioMinimo, clientesCaptados, cobrarXcliente):
        super().__init__(dni, nombre, fechaIngreso)
        self.__salarioMinimo = salarioMinimo
        self.__clientesCaptados = clientesCaptados
        self.__cobrarXcliente = cobrarXcliente

    def obtenerSueldo(self) -> float:
        if self.__salarioMinimo < self.__clientesCaptados * self.__cobrarXcliente:
            return self.__salarioMinimo
        else:
            return self.__clientesCaptados * self.__cobrarXcliente

class EmpleadoFijo(Empleado):
    def __init__(self, dni, nombre, fechaIngreso, sueldoBasico, anosAntiguedad):
        super().__init__(dni, nombre, fechaIngreso)
        self.__sueldoBasico = sueldoBasico
        self.__anosAntiguedad = anosAntiguedad

    def obtenerSueldo(self) -> float:
        if self.__anosAntiguedad < 2:
            return self.__sueldoBasico
        if self.__anosAntiguedad > 2 and self.__anosAntiguedad < 5:
            return self.__anosAntiguedad * 1.05
        if self.__anosAntiguedad > 5:
            return self.__anosAntiguedad * 1.1
    
class Tester:
    def testerx():
        print("Creando empleados")
        e1 = EmpleadoComision("12345678", "Juan", Fecha(20, 10, 2000), 10000, 50, 500)
        e2 = EmpleadoFijo("87654321", "Ana", Fecha(15, 5, 2005), 8000, 3)
        print("Empleados creados :)")
        print("")
        
        print("Agregando empleados")
        e1.agregarEmpleado(e2)
        print("Empleados agregados :)")
        print("")
        
        print("Empleados:")
        for empleado in e1._empleados:
            print(f"DNI: {empleado._dni}, Nombre: {empleado._nombre}, Sueldo: {empleado.obtenerSueldo()}")
            print("")
        
        print("Empleado con mayor comision:")
        print(f"DNI: {e1.mayorComision()._dni}, Nombre: {e1.mayorComision()._nombre}")
        print("")
        
        print("Eliminando empleado")
        e1.eliminarEmpleado(e2)
        print("Empleado eliminado :)")
        print("")
        
        print("Empleados:")
        for empleado in e1._empleados:
            print(f"DNI: {empleado._dni}, Nombre: {empleado._nombre}, Sueldo: {empleado.obtenerSueldo()}")
            print("")
        
        print("Empleado con mayor comision:")
        print(f"DNI: {e1.mayorComision()._dni}, Nombre: {e1.mayorComision()._nombre}")
        print("")

if __name__ == "__main__":
    Tester.testerx()