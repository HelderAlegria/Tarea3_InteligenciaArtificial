from collections import deque

laberinto = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 'M']
]

inicio = (0, 0)
meta = (4, 4)  

direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

def es_valida(fila, col):
    """Verifica si una celda está dentro del laberinto y es accesible."""
    return 0 <= fila < 5 and 0 <= col < 5 and laberinto[fila][col] != 1

def bfs(laberinto, inicio, meta):
    """Busca la ruta más corta utilizando BFS y devuelve la ruta seguida."""
    cola = deque([(inicio, [inicio])])
    visitados = set()
    visitados.add(inicio)

    while cola:
        (fila, col), camino = cola.popleft()

        if (fila, col) == meta:
            return camino

        for direccion in direcciones:
            nueva_fila, nueva_col = fila + direccion[0], col + direccion[1]

            if es_valida(nueva_fila, nueva_col) and (nueva_fila, nueva_col) not in visitados:
                visitados.add((nueva_fila, nueva_col))
                nuevo_camino = camino + [(nueva_fila, nueva_col)]
                cola.append(((nueva_fila, nueva_col), nuevo_camino))

    return None  

camino = bfs(laberinto, inicio, meta)

if camino:
    print("Ruta más corta seguida por el agente:")
    for paso in camino:
        print(paso)
else:
    print("No se encontró una ruta válida.")
