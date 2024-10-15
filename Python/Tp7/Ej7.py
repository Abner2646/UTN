from modulo_fecha import Fecha

class Empleado:
    '''A la empresa le interesa poder agregar y eliminar empleados, consultar sus salarios,
    y consultar de los empleados a comisión que tiene, cual es el que posee más
    clientes captados.'''
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
    def consultarComision(self) -> float:
        return self._comision

    def mayorComision(self) -> 'Empleado': #!!
        '''Retorna el empleado de mayor comision'''
        pass

class EmpleadoComision:
    '''Los empleados a comisión tienen un salario mínimo, un número de clientes captados
    y un monto a cobrar por cada cliente captado. El salario se obtiene multiplicando los
    clientes captados por el monto por cliente. Si el salario obtenido por los clientes
    captados no llega a cubrir el salario mínimo, cobrará el salario mínimo.'''
    

class EmpleadoFijo:
    '''Los empleados con salario fijo tienen un sueldo básico y un porcentaje adicional en
    función del número de años que llevan la empresa:
    ● Menos de 2 años: Nada.
    ● De 2 a 5 años: 5% más.
    ● Más de 5 años: 10% más.'''

