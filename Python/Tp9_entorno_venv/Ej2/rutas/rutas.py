from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorio import crear_repositorio #!!
from modelos.entidades.prestamo import Prestamo #!!

repo_prestamo = crear_repositorio() #!!
bp_prestamo = Blueprint("bp_prestamo", __name__) #!!

@bp_prestamo.route("/prestamos", methods=["GET"]) #!!
def obtener_prestamos(): #!!