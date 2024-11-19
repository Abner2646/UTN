from flask import Blueprint, request,jsonify
from ..modelos.repositorios import obtenerRepoAlumnos #!!

repositorio_alumnos = obtenerRepoAlumnos()

bp_alumnos = Blueprint("pb_alumnos", __name__) #Que pija es esta instanca de bp?

@bp_alumnos.route("/alumnos", methods = ["GET"]) #Establezco una ruta para consultar por los alumnos en tipo GET
def obtener_todos_los_alumnos():
    lsita_dicc = []
    for alumno in repositorio_alumnos.obtenerTodos()