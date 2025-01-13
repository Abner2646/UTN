from modelos.repositorios.repo_curso import RepoCurso
from modelos.repositorios.repo_instrcutor import RepoInstructores
from modelos.repositorios.repo_estudiantes import RepoEstudiante

repo_curso = None
repo_instructor = None
repo_estudiante = None

def getRepoCurso():
    global repo_curso
    if repo_curso == None:
        repo_curso = RepoCurso()
    return repo_curso

def getRepoInstructor():
    global repo_instructor
    if repo_instructor == None:
        repo_instructor = RepoInstructores()
    return repo_instructor

def getRepoEstudiante():
    global repo_estudiante
    if repo_estudiante == None:
        repo_estudiante = RepoEstudiante()
    return repo_estudiante
