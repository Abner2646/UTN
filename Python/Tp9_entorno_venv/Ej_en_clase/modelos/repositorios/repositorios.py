from ...modelos.repositorios.repositorio_alumnos import RepositorioAlumno

repo_alumnos = None

def obtenerRepoAlumnos() -> 'RepositorioAlumno':
    global repo_alumnos
    if not isinstance (repo_alumnos, 'RepositorioAlumno'):
        repo_alumnos = RepositorioAlumno()
    return repo_alumnos

