# Trabajo Final - Programación 2

## Descripción del Proyecto

La aplicación está diseñada para gestionar entidades como **Alumnos**, **Cursos** e **Instructores**. La estructura está basada en el uso de repositorios en formato **JSON** para almacenar y organizar los datos de cada entidad.

## Interpretación de la Consigna

Para cumplir con la consigna del trabajo final, interpreté que cada entidad debe tener un identificador (**id**) que funcione como "clave primaria" para distinguirla únicamente y permitir su interacción con otras clases. Esto facilita, por ejemplo, asignar a cada **Curso** un **Instructor** o varios **Estudiantes** de manera clara y ordenada.


## Lógica de Vinculación entre Entidades

En los métodos implementados para **crear** cada entidad, no se incluye por defecto la posibilidad de vincularlas directamente con otras entidades. Es necesario primero **crear** las entidades de forma independiente y, posteriormente, utilizar rutas específicas para establecer las relaciones entre ellas.

- **Lenguaje**: Python
- **Formato de almacenamiento**: JSON
- **Framework/API**: Flask

© Abner Grgurich - Programación 2 - 2024
