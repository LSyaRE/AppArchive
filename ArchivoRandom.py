import random
import string
from tkinter import Variable

class ArchivoRandom:
  def __init__(self) -> None:
    self.nombre='str'
  def random_caracter(self):
    lista=[]
    for x in range(0,10000):
      x=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(0,12))
      lista.append(x)
    return lista

  def crearArchivo(self, nombre):
    self.nombre = nombre
    archivo=open(f"{self.nombre}.txt",'w')
    archivo.close()

  def escribir(self):
    archivo=open(f"{self.nombre}.txt",'a')
    for i in self.random_caracter():
      archivo.write(i+' ')



