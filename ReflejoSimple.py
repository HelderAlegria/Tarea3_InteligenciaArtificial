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

    def mover(self):
        """Mover el agente y cambiar dirección si detecta un obstáculo o llega al final de la ruta."""
        indice_actual = self.ruta.index(self.posicion)
        
        siguiente_indice = indice_actual + self.direccion

        if siguiente_indice < 0:  
            siguiente_indice = 0
            self.direccion = 1  
        elif siguiente_indice >= len(self.ruta):  
            siguiente_indice = len(self.ruta) - 1
            self.direccion = -1  
        
        siguiente_posicion = self.ruta[siguiente_indice]

        if siguiente_posicion in self.obstaculos:
            print(f"¡Obstáculo detectado en {siguiente_posicion}! Cambiando dirección.")
            self.direccion *= -1  
            siguiente_posicion = self.ruta[siguiente_indice + self.direccion]

        self.posicion = siguiente_posicion
        print(f"El agente se mueve a {self.posicion}.")

    def patrullar(self):
        """Patrullar por la ruta indefinidamente, reaccionando a obstáculos."""
        while True:
            self.mover()
            time.sleep(1)  

agente = AgenteReflejo(ruta, obstaculos)
agente.patrullar()
