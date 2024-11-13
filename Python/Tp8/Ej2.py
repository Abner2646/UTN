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
from contacto import Contacto

class Tester:
    def run(self):
        contacto1=Contacto('Juan','Perez',123456)
        contacto2=Contacto('Maria','Gomez',654321)
        contacto3=Contacto('Carlos','Lopez',987654)
        contacto4=Contacto('Ana','Martinez',456789)
        listaContactos=[contacto1,contacto2,contacto3,contacto4]
        
        with open("contactos.json","w") as file:
            contactos_dict = []
            for contacto in listaContactos:
                contactos_dict.append(contacto.to_dicc()) #Agrega los diccionarios de los objetos a una nueva lista
            json.dump(contactos_dict, file) #Agrega la lista a el archivo json
            
        with open("contactos.json", "r") as file:
            contactos_reconstruidos = []
            contactos_dict = json.load(file) #Le carga los diccionarios que están en "file"
            for contacto in contactos_dict:
                contactos_reconstruidos.append(Contacto.from_dicc(contacto)) #Crea los nuevos contactos a partir de los diccionarios
                
        letra = input("Ingrese una letra para buscar contactos por apellido: ")
        contactos_filtrados = []
        for contacto in contactos_reconstruidos:
            if contacto.apellido.startswith(letra): #startswith es letra en la posicion 0
                contactos_filtrados.append(contacto)
            
        print("Contactos encontrados:")
        for contacto in contactos_filtrados:
            print(f"{contacto.nombre} {contacto.apellido} - {contacto.telefono}")
        

if __name__ == "__main__":
    Tester.run()
