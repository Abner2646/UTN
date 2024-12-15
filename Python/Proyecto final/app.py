from flask import Flask
from rutas import bp_curso

app = Flask(__name__)
app.register_blueprint(bp_curso)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

