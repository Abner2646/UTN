from flask import Blueprint, request, jsonify
from modelos.repositorios.repositorios import getRepoCurso
from modelos.repositorios.repositorios import getRepoEstudiante
from modelos.repositorios.repositorios import getRepoInstructor
from modelos.entidades.curso import Curso
from flask import jsonify, make_response

repo_curso = getRepoCurso()
repo_estudiante = getRepoEstudiante()
repo_instructor = getRepoInstructor()
bp_curso = Blueprint("bp_curso", __name__)

#---------------------De los cursos
#Obtener todos los cursos.
@bp_curso.route('/cursos', methods=["GET"])
def get_cursos():
    return jsonify([curso.to_dict() for curso in repo_curso.getCursos()])

#Obtener un curso por ID.
@bp_curso.route('/cursos/<int:id>', methods=["GET"])
def get_curso(id):
    curso = repo_curso.getCurso(id)
    return jsonify(curso.to_dict()) if curso else jsonify({"error": "Curso no encontrado"}), 404

#Crear un nuevo curso.
@bp_curso.route('/cursos', methods=["POST"])
def crear_curso():
    try:
        datos = request.get_json()
        
        # Validar que los datos requeridos estén presentes
        if not all(key in datos for key in ['id', 'nombre', 'descripcion', 'duracion']):
            return jsonify({
                "error": "Faltan datos requeridos. Se necesita: id, nombre, descripcion y duracion"
            }), 400
        
        #Validar que no haya otro curso con el mismo id
        if repo_curso.existeID(datos['id']):
            return jsonify({"error": "Ya existe un curso con ese ID"}), 400
        
        # Crear nuevo curso
        nuevo_curso = Curso(
            id=datos['id'],
            nombre=datos['nombre'],
            descripcion=datos['descripcion'],
            duracion=datos['duracion']
        )
        
        # Agregar al repositorio
        repo_curso.agregarCurso(nuevo_curso)
        
        return jsonify({
            "mensaje": "Curso creado exitosamente",
            "curso": nuevo_curso.to_dict()
        }), 201
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Error interno del servidor"})

#Eliminar un curso por id
@bp_curso.route('/cursos/<int:id>', methods=["DELETE"])
def eliminar_curso(id):
    repo = getRepoCurso()
    if repo.existeID(id):
        if repo.eliminarPorId(id):
            return (jsonify({"mensaje": f"Curso con ID {id} eliminado exitosamente"}), 200)
    else:
        return (jsonify({"error": f"No se encontró un curso con el ID {id}"}), 404)


#Actualizar un curso
from flask import request, jsonify, make_response
from modelos.entidades.curso import Curso

@bp_curso.route('/cursos/<int:id>', methods=["PUT"])
def actualizar_curso(id):
    repo = getRepoCurso()
    
    # Verificar si el curso existe
    curso_existente = repo.getCurso(id)
    if not curso_existente:
        return make_response(jsonify({"error": f"No se encontró un curso con el ID {id}"}), 404)

    # Obtener los datos del curso desde el request
    datos = request.get_json()
    if not datos:
        return make_response(jsonify({"error": "No se enviaron datos para actualizar"}), 400)
    
    try:
        # Actualizar los atributos del curso existente con los datos recibidos
        if "nombre" in datos:
            curso_existente.set_nombre(datos["nombre"])
        if "descripcion" in datos:
            curso_existente.set_descripcion(datos["descripcion"])
        if "duracion" in datos:
            curso_existente.set_duracion(int(datos["duracion"]))
        
        # Guardar los cambios en el repositorio
        repo.guardarCursos()
        
        return make_response(jsonify({"mensaje": f"Curso con ID {id} actualizado exitosamente"}), 200)
    
    except Exception as e:
        return make_response(jsonify({"error": f"Error al actualizar el curso: {str(e)}"}))

#---------------------De los estudiantes

from flask import jsonify, make_response
from modelos.entidades.estudiante import Estudiante

#Crear un estudiante
@bp_curso.route('/estudiantes', methods=["POST"])
def crear_estudiante():
    try:
        datos = request.get_json()
        
        # Validar que los datos requeridos estén presentes
        if not all(key in datos for key in ['dni', 'nombre', 'apellido', 'email']):
            return jsonify({
                "error": "Faltan datos requeridos. Se necesita: dni, nombre, apellido e email"
            }), 400
        
        # Crear nuevo estudiante
        nuevo_estudiante = Estudiante(
            dni=datos['dni'],
            nombre=datos['nombre'],
            apellido=datos['apellido'],
            email=datos['email']
        )
        
        # Agregar al repositorio
        repo_estudiante.agregarEstudiante(nuevo_estudiante)
        
        return jsonify({
            "mensaje": "Estudiante creado exitosamente",
            "estudiante": nuevo_estudiante.to_dict()
        }), 201
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


#Obtener todos los estudiantes:
@bp_curso.route('/estudiantes/', methods=["GET"])
def get_estudiantes():
    try:
        estudiantes_en_curso = [
            estudiante.to_dict() 
            for estudiante in repo_estudiante.getEstudiantes() 
        ]
        return jsonify(estudiantes_en_curso), 200
    except Exception as e:
        return jsonify({"error": str(e)})


#Obtener todos los estudiantes de UN curso
@bp_curso.route('/estudiantes/<int:idCurso>', methods=["GET"])
def get_estudiantes_por_curso(idCurso):
    try:
        estudiantes_en_curso = [
            estudiante.to_dict() 
            for estudiante in repo_estudiante.getEstudiantes() 
            if idCurso in estudiante.get_cursoQueToma()
        ]
        return jsonify(estudiantes_en_curso), 200
    except Exception as e:
        return jsonify({"error": str(e)})


#Asignar un curso al estudiante
@bp_curso.route('/estudiantes/set_curso/<int:idCurso>/<int:idEstudiante>', methods=["PUT"])
def set_cursoDelEstudiante(idCurso: int, idEstudiante: int):
    try:
        # Buscar el estudiante por su ID
        estudiante = repo_estudiante.getEstudiante(idEstudiante)
        if not estudiante:
            return jsonify({"error": "Estudiante no encontrado"}), 404

        # Asignar el curso al estudiante
        estudiante.set_cursoQueToma(idCurso)

        # Guardar los cambios en el repositorio
        repo_estudiante.guardarEstudiantes()

        return jsonify({"mensaje": "Curso asignado exitosamente", "estudiante": estudiante.to_dict()}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400



#Actualizar estudiante
@bp_curso.route('/estudiantes/<int:dni>', methods=["PUT"])
def actualizar_estudiante(dni):
    repo = getRepoEstudiante()
    
    # Verificar si el estudiante existe
    estudiante_existente = repo.getEstudiante(dni)
    if not estudiante_existente:
        return make_response(jsonify({"error": f"No se encontró un estudiante con el ID {dni}"}), 404)
    #Actualiza los valores del estudiante
    # Obtener datos del request
    nuevos_datos = request.get_json()

    try:
        # Actualizar los atributos del estudiante existente
        if 'nombre' in nuevos_datos:
            estudiante_existente.set_nombre(nuevos_datos['nombre'])
        if 'apellido' in nuevos_datos:
            estudiante_existente.set_apellido(nuevos_datos['apellido'])
        if 'email' in nuevos_datos:
            estudiante_existente.set_email(nuevos_datos['email'])
        if 'curso' in nuevos_datos:
            estudiante_existente.set_cursoQueToma(nuevos_datos['curso'])
        
        # Guardar los cambios en el repositorio
        repo.guardarEstudiantes()
        
        return make_response(jsonify({"mensaje": "Estudiante actualizado exitosamente"}), 200)
    
    except Exception as e:
        return make_response(jsonify({"error": f"Error al actualizar estudiante: {str(e)}"}), 400)


#Eliminar estudiante
@bp_curso.route('/estudiantes/<int:dni>', methods=["DELETE"])
def eliminar_estudiante(dni):
    repo = getRepoEstudiante()
    if repo.existeDni(dni):
        repo.eliminarPorDni(dni)
        return (jsonify({"mensaje": f"Estudiante con DNI {dni} eliminado exitosamente"}), 200)


#---------------------De los instrcutores

from modelos.entidades.instructor import Instructor

#Crear un instructor
@bp_curso.route('/instructores', methods=["POST"])
def crear_instructor():
    try:
        datos = request.get_json()
        
        # Validar que los datos requeridos estén presentes
        if not all(key in datos for key in ['dni', 'nombre', 'apellido', 'email']):
            return jsonify({
                "error": "Faltan datos requeridos. Se necesita: dni, nombre, apellido e email"
            }), 400
        
        # Crear nuevo instructor
        nuevo_instructor = Instructor(
            dni=datos['dni'],
            nombre=datos['nombre'],
            apellido=datos['apellido'],
            email=datos['email']
        )
        
        # Agregar al repositorio
        repo_instructor.agregarInstructor(nuevo_instructor)
        
        return jsonify({
            "mensaje": "Instructor creado exitosamente",
            "instructor": nuevo_instructor.to_dict()
        }), 201
        
    except:
        return jsonify({"error": str(e)}), 400 #!!e

#Obtener todos los instructores
@bp_curso.route('/instructores', methods=["GET"])
def get_instructores():
    return jsonify([instructor.to_dict() for instructor in repo_instructor.getInstructores()])

#Obtener instrcutor por dni
@bp_curso.route('/instructores/<int:dni>', methods=["GET"])
def get_instructor_por_dni(dni):
    instructor = repo_instructor.getInstructorPorDni(dni)
    if instructor:
        return jsonify(instructor.to_dict())

#Asignarle un curso al instructor
@bp_curso.route('/instructor/<int:idCurso>/<int:dniInstructor>', methods=["PUT"])
def set_cursoDelInstructor(idCurso: int, dniInstructor: int):
    try:
        # Buscar el instructor por su DNI
        instructor = repo_instructor.getInstructorPorDni(dniInstructor)
        if not instructor:
            return jsonify({"error": "Instructor no encontrado"}), 404
        
        #Un curso solo puede tener un Instructor, por eso:
        #Verificar que no haya otro instructor que sea instructor en el mismo curso
        if idCurso in instructor.to_dict().get('cursoQueDicta'):
            return jsonify({"error": "Ya hay un instructor en este curso"}), 400

        # Asignar el curso al instructor
        instructor.set_cursoQueDicta(idCurso)

        # Guardar los cambios en el repositorio
        repo_instructor.guardarInstructor()

        return jsonify({"mensaje": "Curso asignado exitosamente", "instructor": instructor.to_dict()}), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


#Actualizar instrcutor
@bp_curso.route('/instructores/<int:dni>', methods=["PUT"])
def actualizar_instructor(dni):
    repo = getRepoInstructor()
    
    # Verificar si el instructor existe
    instructor_existente = repo.getInstructorPorDni(dni)
    if not instructor_existente:
        return make_response(jsonify({"error": f"No se encontró un instructor con el DNI {dni}"}), 404)
    #Actualiza los valores del instrcutor
    # Obtener datos del request
    nuevos_datos = request.get_json()

    try:
        # Actualizar los atributos del instructor existente
        if 'nombre' in nuevos_datos:
            instructor_existente.set_nombre(nuevos_datos['nombre'])
        if 'apellido' in nuevos_datos:
            instructor_existente.set_apellido(nuevos_datos['apellido'])
        if 'email' in nuevos_datos:
            instructor_existente.set_email(nuevos_datos['email'])
        if 'curso' in nuevos_datos:
            instructor_existente.set_cursoQueDicta(nuevos_datos['curso'])
        if 'cursoQueDicta' in nuevos_datos:
            instructor_existente.set_cursoQueDicta(nuevos_datos['cursoQueDicta']) #Se le puede pasar un entero o una lista a set_cursoQueDicta
        
        # Guardar los cambios en el repositorio
        repo.guardarInstructor()
        
        return make_response(jsonify({"mensaje": "Instructor actualizado exitosamente"}), 200)
    
    except Exception as e:
        return make_response(jsonify({"error": f"Error al actualizar instructor: {str(e)}"}), 400)


#Eliminar instrcutor
@bp_curso.route('/instructores/<int:dni>', methods=["DELETE"])
def eliminar_instructor(dni:int):
    repo = getRepoInstructor()
    if repo.existeDni(dni):
        repo.eliminarPorId(dni)
        return (jsonify({"mensaje": f"Instructor con DNI {dni} eliminado exitosamente"}), 200)
    else:
        return (jsonify({"error": f"No se encontró un instructor con el DNI {dni}"}), 404)