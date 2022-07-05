from ArchivoRandom import ArchivoRandom
from Search import Search

class Main:
    
    __archivo= ArchivoRandom()
    __search= Search()  

    def __init__(self):
        pass

    def archivoRandom(self,nombre):
        self.__archivo.crearArchivo(nombre)
        self.__archivo.escribir()


    def buscarPalabra(self,nombreArchivo,palabra):
        return self.__search.buscarCoincidencias(nombreArchivo,palabra)

   
main = Main()

main.archivoRandom("globo")
answer =main.buscarPalabra("globo","hola")
print (answer)
