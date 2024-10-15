'''Una concesionaria de automóviles vende una gran variedad de vehículos. Cada
vehículo tiene una marca, modelo, patente, color, año de fabricación, precio y un
determinado kilometraje. Además, se registra el tipo de combustible que utiliza
(nafta, diésel o eléctrico). Los autos, además de las características generales de un
vehículo, tienen una cantidad específica de puertas y algunos cuentan con aire
acondicionado. Por otro lado, las motos tienen un ancho de manubrio y una
cilindrada particular.'''

class Veiculo:
    '''Cada vehículo tiene una marca, modelo, patente, color, año de fabricación, precio y un
    determinado kilometraje. Además, se registra el tipo de combustible que utiliza (nafta, diésel o eléctrico).'''
    def __init__(self, marca:str, modelo:str, patente:str, color:str, anoFabric:int, precio:float, km:int) -> None:
        self._marca = marca
        self._modelo = modelo
        self._patente = patente
        self._color = color
        self._anoFabric = anoFabric
        self._precio = precio
        self._km = km

    def obtenerMarca(self):
        return self._marca
    
    def obtenerModelo(self):
        return self._modelo
    
    def obtenerPatente(self):
        return self._patente
    
    def obtenerColor(self):
        return self._color
    
    def obtenerAnoFabricacion(self):
        return self._anoFabric
    
    def obtenerPrecio(self):
        return self._precio
    
    def obtenerKilometraje(self):
        return self._km

class Auto(Veiculo):
    def __init__(self, marca, modelo, patente, color, anoFabric, precio, km):
        super().__init__(marca, modelo, patente, color, anoFabric, precio, km)

class Moto(Veiculo):
    def __init__(self, marca, modelo, patente, color, anoFabric, precio, km):
        super().__init__(marca, modelo, patente, color, anoFabric, precio, km)


class Tester:
    def test():
        a1 = Auto("Marca", "Modelo", "Patente", "Color", 2000, 100, 2)
        print(a1.obtenerMarca())

if __name__ == "__main__":
    Tester.test()