class Cancion: #LISTO
    def __init__(self, codigo:int, nombre:str, duracion:int, genero:str) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__genero = genero

    def reproducir(self) -> str:
        return f"Se está reproduciendo {self.__nombre}"
    
    def obtenerNombre(self) -> str:
        return self.__nombre

class Playlist: #LISTO
    def __init__(self, codigo:int, nombre:str) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__canciones = []

    #SETTERS:
    def agregarCancion(self, cancion:'Cancion') -> None:
        self.__canciones.append(cancion)

    def eliminarCancion(self, cancion: 'Cancion') -> None:
        if cancion in self.__canciones:
            self.__canciones.remove(cancion)
        else:
            print(f"La canción {cancion} no está en la playlist.")

    #GETTERS:
    def obtenerNombre (self) -> str:
        return self.__nombre
    
    def obtenerCodigo(self) -> int:
        return self.__codigo

class Pais:
    def __init__(self, codigo:int, nombre:str, cantidadDispositivos:int) -> None:
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantidadDispositivos = cantidadDispositivos

    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerCantidadDispositivos(self) -> int:
        return self.__cantidadDispositivos

class Suscripcion: #!!
    def __init__(self, nombre:str, email:str, telefono:str, pais:'Pais') -> None:
        self._nombre = nombre
        self._email = email
        self._telefono = telefono
        self.__pais = pais
        self.__misPlaylists = []

    #SETTERS:
    def crearPlaylist(self, nombrePlaylist: str):
        nueva_playlist = Playlist(nombrePlaylist)  # Crea un objeto Playlist
        self.__misPlaylists.append(nueva_playlist)  # Añade la nueva playlist a la lista

    def agregarCancionPlaylist(self, playlist:'Playlist', cancion:'Cancion'):
        if playlist in self.__misPlaylists:
            playlist.agregarCancion(cancion)

    #GETTERS:
    def obtenerPlaylists(self) -> list:
        pass

    def reproducirMusica(self): #Si se cumple X condición hace algo
        pass

    def reproducirCancion(self): 
        pass

class SuscripcionGratuita(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:str, pais:'Pais'):
        super().__init__ (nombre, email, telefono, pais)
        self.__tiempoSinPublicidad = 0

    def reproducirMusica(self, cancion:'Cancion'): #!!
        if self.__tiempoSinPublicidad > 30:
            print(f"Sonando {cancion.obtenerNombre()}...")
        else:
            SuscripcionGratuita.interrumpirConPublicidad()
            self.__tiempoSinPublicidad = 0

    def interrumpirConPublicidad(self): #!!
        print("Sonando publicidad...")

class SuscripcionPaga(Suscripcion):
    def __init__(self, nombre:str, email:str, telefono:str, pais:'Pais', maxDispositivos:int, dispositivos:int):
        super().__init__(nombre, email, telefono, pais)
        self.__maxDispositivos = maxDispositivos
        self.__dispositivos = dispositivos

    def reproducirMusica(self):
        return super().reproducirMusica()
    
    def dispositivos(self) -> list: #!!
        pass

