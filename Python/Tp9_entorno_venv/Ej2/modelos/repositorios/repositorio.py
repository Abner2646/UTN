from modelos.repositorios.repositorioSocios import RepositorioSocios

repositorio = None

def crear_repositorio():
    global repositorio
    if repositorio is None:
        repositorio = RepositorioSocios #!!
    return repositorio