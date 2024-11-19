from flask import Flask
from rutas.ruta import bp_libro

app = Flask(__name__)
app.register_blueprint(bp_libro)

if __name__ == "__main__":
    app.run(debug=True)
