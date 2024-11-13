import json

class Contacto:
    @classmethod
    def fromDic(self, data: dict) -> "Contacto":
        return Contacto(data["nombre"], data["apellido"], data["telefono"], data["mail"], data["direccion"])

    def __init__(self, nombre: str, apellido: str, telefono: str, mail: str, direccion: str):
        self.__nombre = nombre
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

    def __str__(self):
        return f"{self.__nombre} {self.__apellido} - Tel: {self.__telefono}, Email: {self.__mail}, Dirección: {self.__direccion}"


class Tester:
    @staticmethod
    def test():
        # A) Crear objetos de la clase Contacto y almacenarlos en una lista
        c1 = Contacto("Abner", "Grgurich", "291", "a@gmail", "9 de Julio")
        c2 = Contacto("Maria", "Sanzio", "351", "m@hotmail", "Av. Del Libertador")
        c3 = Contacto("Pedro", "Peralta", "421", "p@outlook", "Santa Fe")
        contactos = [c1, c2, c3]

        # B) Guardar la lista completa en un archivo JSON
        contactos_json = r"C:\Users\Abner\Desktop\UTN1\Python\Tp8\contactos.json"
        with open(contactos_json, "w", encoding="utf-8") as file:
            json.dump([i.toDic() for i in contactos], file, ensure_ascii=False, indent=4)

        # C) Cargar los contactos desde el archivo JSON y reconstruir los objetos
        lista = []
        with open(contactos_json, "r", encoding="utf-8") as file:
            data = json.load(file)
            for item in data:
                lista.append(Contacto.fromDic(item))

        # D) Buscar contactos por la primera letra del apellido
        letra = input("Ingrese una letra para buscar contactos por apellido: ").upper()
        resultados = [str(c) for c in lista if c.obtenerApellido().upper().startswith(letra)]
        
        if resultados:
            print("Contactos encontrados:")
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontraron contactos con esa letra inicial en el apellido.")


if __name__ == "__main__":
    Tester.test()
