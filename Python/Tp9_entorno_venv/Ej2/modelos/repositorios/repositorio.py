from modelos.repositorios.repositorio_prestamo import LaClase #!!

repositorio = None

def crear_repositorio():
    global repositorio
    if repositorio is None:
        repositorio = Repositorio_de_clase_creada_anteriormente() #!!
    return repositorio