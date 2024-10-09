class PolizaInmueble:
    def __init__(self, numero:int, incendio:float, explosion:float, robo:float) -> None:
        self._numero = numero
        self._incendio = incendio
        self._explosion = explosion
        self._robo = robo
    
    #GETTERS:
    def costoPoliza(self) -> float: #!!
        self.__costoPoliza = self._incendio + self._explosion + self._robo
        return self.__costoPoliza

    def __str__(self) -> str:
        return f"Poliza Inmueble: Numero={self.__numero}, Incendio={self.__incendio}, Explosion={self.__explosion}, Robo={self.__robo}"
    
    def obtenerNumero(self) -> str:
        return self._numero


class PolizaInmuebleEscolar(PolizaInmueble):
    def __init__(self, numero:int, incendio:float, explosion:float, robo:float, cantPersonas:int, montoEquipamiento:int, montoMobiliario:float, montoPersona:float) -> None:
        super().__init__(numero, incendio, explosion, robo)
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoMobiliario = montoMobiliario
        self.__montoPersona = montoPersona

    #GETTERS
    def costoPoliza(self) -> float:
        return self.__costoPoliza + self.__montoEquipamiento + self.__montoMobiliario + (self.__montoPersona * self.__cantPersonas)
    
    def __str__(self) -> str:
        return f"Poliza Inmueble Escolar: Numero={self.__numero}, Incendio={self.__incendio}, Explosion={self.__explosion}, Robo={self.__robo}, CantPersonas={self.__cantPersonas}, Monto Equipamiento={self.__montoEquipamiento}, Monto Mobiliario={self.__montoMobiliario}, Monto Persona={self.__montoPersona}"
    

class Aseguradora:
    def __init__(self) -> None:
        self._seguros = []
    
    def insertar(self, poliza:'PolizaInmueble') -> None:
        self._seguros.append(poliza)

    # Método para eliminar una póliza si existe
    def eliminar(self, poliza: 'PolizaInmueble') -> None:
        for i in self._seguros:
            if i.obtenerNumero() == poliza._numero:  # Comparamos por número de póliza
                self._seguros.remove(i)
                break

    # Método para verificar si existe una póliza
    def existePoliza(self, poliza: 'PolizaInmueble') -> bool:
        return any(p._numero == poliza._numero for p in self._seguros)

    def costoTotal(self):
        pass

    def esIgual(self, aseguradora:'Aseguradora') -> bool: #!!!!
        pass

class Tester:
    def __init__(self):
        self.aseguradora = Aseguradora()
    
    def probarInsertar(self):
        print("Probando insertar pólizas...")
        poliza1 = PolizaInmueble(1, 1000, 500, 200)
        poliza2 = PolizaInmuebleEscolar(2, 1200, 600, 300, 50, 10000, 5000, 200)
        self.aseguradora.insertar(poliza1)
        self.aseguradora.insertar(poliza2)
        print("Pólizas insertadas.")
    
    def probarEliminar(self):
        print("\nProbando eliminar pólizas...")
        poliza1 = PolizaInmueble(1, 1000, 500, 200)
        print(f"Antes de eliminar, costo total: {self.aseguradora.costoTotal()}")
        self.aseguradora.eliminar(poliza1)
        print(f"Después de eliminar póliza 1, costo total: {self.aseguradora.costoTotal()}")
    
    def probarExistePoliza(self):
        print("\nProbando existencia de pólizas...")
        poliza1 = PolizaInmueble(1, 1000, 500, 200)
        poliza3 = PolizaInmueble(3, 1500, 700, 400)
        existe1 = self.aseguradora.existePoliza(poliza1)
        existe3 = self.aseguradora.existePoliza(poliza3)
        print(f"Poliza 1 existe: {existe1}")  # Esperado: False, porque la eliminamos en el paso anterior
        print(f"Poliza 3 existe: {existe3}")  # Esperado: False, porque nunca la insertamos
    
    def probarCostoTotal(self):
        print("\nProbando cálculo del costo total...")
        costo = self.aseguradora.costoTotal()
        print(f"Costo total de las pólizas: {costo}")  # Debería reflejar el costo de la póliza escolar que queda
    
    def probarEsIgual(self):
        print("\nProbando igualdad de aseguradoras...")
        # Creamos otra aseguradora con las mismas pólizas
        aseguradora2 = Aseguradora()
        poliza2 = PolizaInmuebleEscolar(2, 1200, 600, 300, 50, 10000, 5000, 200)
        aseguradora2.insertar(poliza2)
        sonIguales = self.aseguradora.esIgual(aseguradora2)
        print(f"Las aseguradoras son iguales: {sonIguales}")  # Esperado: True

        # Probamos con una póliza diferente
        poliza3 = PolizaInmueble(3, 1500, 700, 400)
        aseguradora2.insertar(poliza3)
        sonIguales = self.aseguradora.esIgual(aseguradora2)
        print(f"Las aseguradoras son iguales después de insertar una póliza diferente: {sonIguales}")  # Esperado: False
    
    def run_tests(self):
        self.probarInsertar()
        self.probarCostoTotal()
        self.probarEliminar()
        self.probarExistePoliza()
        self.probarEsIgual()

# Ejecutar el tester
tester = Tester()
tester.run_tests()
