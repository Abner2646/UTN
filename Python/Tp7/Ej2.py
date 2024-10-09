class Propietario:
    def __init__(self, nombre:str, dni:int) -> None:
        self.__nombre = nombre
        self.__dni = dni

class Inmueble:
    def __init__(self, codigo:int, domicilio:str, propietario:'Propietario', metrosCuadrados:int, estado:int) -> None:
        self._codigo = codigo
        self._domicilio = domicilio
        self._propietario = propietario
        self._metrosCuadrados = metrosCuadrados
        self._estado = estado

    #GETTERS:
    def costoAlquiler(self, base:int) -> float: #No se especifica a partir de qué datos se debería calcular el precio
        return base
    
    def precioVenta(self, m2:float) -> float: #No se especifica a partir de qué datos se debería calcular el precio
        return m2

class Departamento(Inmueble):
    def __init__(self, codigo:int, domicilio:str, propietario:'Propietario', metrosCuadrados:int, estado:int, gastosComunes:float, cochera:bool) -> None:
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        self.__gastosComunes = gastosComunes
        self.__cochera = cochera

    #GETTERS:
    def costoAlquiler(self, base: int) -> float:
        return super().costoAlquiler(base)
    
    def precioVenta(self, m2: float) -> float:
        return super().precioVenta(m2)
    
class Quinta(Inmueble):
    def __init__(self, codigo: int, domicilio: str, propietario: Propietario, metrosCuadrados: int, estado: int, metrosParque:int) -> None:
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        self.__metrosParque = metrosParque

    #GETTERS:
    def costoAlquiler(self, base: int) -> float:
        return super().costoAlquiler(base)
    
    def precioVenta(self, m2: float) -> float:
        return super().precioVenta(m2)
    
class Tester:
    def testerx():
        print("Creando p1")
        p1 = Propietario("Juan", 34567890)
        print("Creando d1")
        d1 = Departamento(1234, "Calle 123", p1, 100, 1, 10000, True)
        print("Creando q1")
        q1 = Quinta(5678, "Calle 456", p1, 150, 1, 50)
        print("Todo creado :)")
        print("")

        print("DEPARATAMENTO:")
        print(f"Costo alquiler: ${d1.costoAlquiler(1000)}")
        print(f"Precio venta: ${d1.precioVenta(15)}")
        print("")

        print("QUINTA:")
        print(f"Costo alquiler: ${q1.costoAlquiler(500)}")
        print(f"Precio venta: ${q1.precioVenta(20)}")


if __name__ == "__main__":
    Tester.testerx()