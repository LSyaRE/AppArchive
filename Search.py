import os 

class Search:


    def buscarCoincidencias(self,archivo,content):
        
        archivoAbierto = os.open(f"./{archivo}.txt",flags = os.O_RDWR | os.O_CREAT)
        os.lseek(archivoAbierto, 0, 0)
        str = os.read(archivoAbierto, os.path.getsize(archivoAbierto))
        numeroCoincidencias=str.decode().count(content)
        os.close(archivoAbierto)
        
        return numeroCoincidencias




