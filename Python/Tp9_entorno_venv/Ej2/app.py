from flask import Flask
from rutas.ruta import bp_socio #Guarda con esto, también camiarlo

app = Flask(__name__)
app.register_blueprint(bp_socio) #Cambiar esto por bp_loQCorresponda

if __name__ == "__main__":
    app.run(debug=True)
    