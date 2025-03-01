import random
import time

ruta = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
obstaculos = [(2, 0), (4, 0)] 

class AgenteReflejo:
    def __init__(self, ruta, obstaculos):
        self.ruta = ruta
        self.posicion = ruta[0]  
        self.obstaculos = obstaculos
        self.direccion = 1  

   
