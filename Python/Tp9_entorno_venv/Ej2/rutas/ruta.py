from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorio import crear_repositorio #!!
from modelos.entidades.socio import Socio #!!

repo_socio = crear_repositorio() #!!
bp_socio = Blueprint("bp_socio", __name__) #!!

@bp_socio.route("/socio", methods=["GET"]) #!!
def obtener_socios():
    socios = repo_socio.obtenerTodos() #!!
    return jsonify([socio.toDiccionario() for socio in socios])
