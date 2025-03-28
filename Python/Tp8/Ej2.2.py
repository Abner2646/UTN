'''Crea una clase Contacto que permita gestionar la información de los contactos (nombre,
apellido, teléfono, correo electrónico y dirección, todo en formato string). En la clase
implementa los métodos para serializar/deserializar el objeto utilizando los métodos
toDiccionario() y fromDiccionario(dic: dict) vistos en clase.
En la clase tester:
a. Crea objetos de la clase Contacto y almacenarlos en una lista
b. Guarda esa lista completa en un archivo JSON “contactos.json”.
c. En una nueva lista vacía almacena los objetos reconstruidos a partir del archivo
JSON.
d. Pedile al usuario una letra para buscar los contactos cuyo apellido comienza con esa
letra, y mostrá el resultado de la búsqueda por pantalla. '''

import json

class Contacto:
    @classmethod
    def fromDic(self, data:dict) -> "Contacto":
        return Contacto(data["nombre"], data["apellido"], data["telefono"], data["mail"], data["direccion"])

    def __init__(self, nombre:str, apellido:str, telefono:str, mail:str, direccion:str):
        self.__nombre =nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__mail = mail
        self.__direccion = direccion

    def toDic(self) -> dict:
        return {
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "telefono": self.__telefono,
            "mail": self.__mail,
            "direccion": self.__direccion
        }

    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerApellido(self) -> str:
        return self.__apellido

class Tester:
    @staticmethod
    def test():
        #A) Crea objetos de la clase Contacto y los almacena en una lista
        c1 = Contacto("Abner", "Grgurich", "291", "a@gmail", "9 de Julio")
        c2 = Contacto("Maria", "Sanzio", "351", "m@hotmail", "Av. Del Libertador")
        c3 = Contacto("Pedro", "Peralta", "421", "p@outlook", "Santa Fe")
        contactos = [c1, c2, c3]


        #B) Guarda la lista completa en un archivo JSON
        contactos_json = r"C:\Users\Abner\Desktop\UTN1\Python\Tp8\contactos.json"
        with open(contactos_json, "w", encoding="utf-8") as file:
            #Devuelve un json con el str del diccionario del parametro
                json.dump([i.toDic() for i in contactos], file, ensure_ascii=False, indent=4)


        #C) En una nueva lista vacía almacena los objetos reconstruidos a partir del archivo JSON.
        lista = []
        with open(contactos_json, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                lista.append(Contacto.fromDic(item))


        #D) Pedile al usuario una letra para buscar los contactos cuyo apellido comienza con esa letra, y mostrá el resultado de la búsqueda por pantalla
        letra = input("Ingrese una letra para buscar contactos por apellido: ")

        for c in lista: #Recorre la lista de objetos
            if c.obtenerApellido()[0] == letra:
                print(c.obtenerApellido()) #Muestra el nombre del objeto



if __name__ == "__main__":
    Tester.test()

#OBSERVACIONES:
#Con qué nombre uso a los objetos de la lista de objetos regenerada?
