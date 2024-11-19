from flask import Blueprint, jsonify, request
from modelos.repositorios.repositorioLibros import RepositorioLibros #!! Importo repositorio
from modelos.entidades.libro import Libro #!! Importo la clase

bp_libro = Blueprint("libros", __name__) #!!

repo_libro = RepositorioLibros() #!!

# a) consultar todos los libros registrados (GET)
@bp_libro.route('/libros', methods=['GET'])
def obtenerTodos():
    libros = repo_libro.obtener_todos()
    return jsonify([libro.to_dict() for libro in libros])

# b) buscar un libro en particular por ISBN (GET)
@bp_libro.route('/libros/<int:isbn>', methods=['GET'])
def obtenerPorISBN(isbn):
    for libro in repo_libro.obtener_todos():
        if libro.obtenerISBN() == isbn:
            return jsonify(libro.to_dict()) 
    return jsonify({'mensaje': 'Libro no encontrado'}), 404

# c) agregar un nuevo libro (POST)
@bp_libro.route('/libros',  methods=['POST'])
def agregar():
    try:
        datos = request.json
        isbn = datos['isbn']
        titulo = datos['titulo']
        autor = datos['autor']
        genero = datos['genero']
        anio_publicacion = datos['anio_publicacion']
        cantidad_ejemplares = datos['cantidad_ejemplares']

        # Verificar si el libro con el mismo ISBN ya existe
        if repo_libro.existe(isbn):
            return jsonify({'mensaje': 'El libro con este ISBN ya existe'}), 409
        
        # Crear el nuevo libro si no existe
        nuevoLibro = Libro(isbn, titulo, autor, genero, anio_publicacion, cantidad_ejemplares)
        repo_libro.agregar(nuevoLibro)
        return jsonify({'mensaje': 'Libro agregado'}), 201
    except ValueError as e:
        return jsonify({'mensaje': str(e)}), 400

#