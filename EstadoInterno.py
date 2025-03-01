import random


mapa = [
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1]
]

direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class AgenteExplorador:
    def __init__(self, mapa):
        self.mapa = mapa
        self.posicion = (0, 0)  
        self.visitadas = set()  
        self.visitadas.add(self.posicion)  

    def es_valida(self, nueva_posicion):
        """Verifica si la nueva posición es válida (dentro del mapa y accesible)."""
        fila, col = nueva_posicion
        return 0 <= fila < len(self.mapa) and 0 <= col < len(self.mapa[0]) and self.mapa[fila][col] == 1

    def mover(self):
        """Intenta mover al agente a una nueva posición no visitada y válida."""
        random.shuffle(direcciones)

        for direccion in direcciones:
            nueva_posicion = (self.posicion[0] + direccion[0], self.posicion[1] + direccion[1])

            if self.es_valida(nueva_posicion) and nueva_posicion not in self.visitadas:
                self.posicion = nueva_posicion
                self.visitadas.add(self.posicion)
                print(f"El agente se mueve a {self.posicion}")
                return True  
            
        print(f"El agente no puede moverse desde {self.posicion}")
        return False

    def explorar(self):
        """Explorar el mapa hasta que no haya más celdas por visitar o no pueda moverse."""
        while True:
            if not self.mover():
                print("No hay más celdas accesibles por explorar o el agente está atascado.")
                break

        print("Exploración completada.")
        print(f"Posiciones visitadas: {sorted(self.visitadas)}")


agente = AgenteExplorador(mapa)
agente.explorar()
