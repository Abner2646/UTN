from flask import Flask
from .rutas.rutas import bp_prestamo #Guarda con esto, también camiarlo

app = Flask(__name__)
app.register_blueprint(bp_prestamo) #Cambiar esto por bp_loQCorresponda

if __name__ == "__main__":
    app.run(debug=True)