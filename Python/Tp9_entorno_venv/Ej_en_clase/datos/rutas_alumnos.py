from flask import Blueprint, request,jsonify
from modelos.repositorios

bp_alumnos = Blueprint("pb_alumnos", __name__)

@bp_alumnos.route("/alumnos", methods = ["GET"])
def obtener_todos_los_alumnos():
