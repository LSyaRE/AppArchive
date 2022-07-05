import random
import string
from tkinter import Variable

class PalabrasAleatorias:
  def __init__(self) -> None:
    self.nombre='str'
  def random_caracter(self):
    lista=[]
    for x in range(0,8):
      x=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(0,12))
      lista.append(x)
    return lista

  def creararchivo(self, nombre):
    archivo=open(f"{self.nombre}.txt",'w')
    archivo.close()

  def escribir(self):
    archivo=open(f"{self.nombre}.txt",'a')
    for i in self.random_caracter():
      archivo.write(i+' ')

aleatorio=PalabrasAleatorias()
aleatorio.creararchivo('nombre')
aleatorio.escribir()


