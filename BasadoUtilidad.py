import heapq

entorno = [
    [1, 2, 3, 4],
    [0, -1, -2, 5],
    [1, 3, 1, 2],
    [2, 2, 3, 1]
]

inicio = (0, 0)  
destino = (3, 3)  

def calcular_utilidad(camino, entorno):
    utilidad = 0
    for (x, y) in camino:
        utilidad += entorno[x][y]
    return utilidad

def buscar_ruta_optima(entorno, inicio, destino):
    filas, columnas = len(entorno), len(entorno[0])

    movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    cola = [(entorno[inicio[0]][inicio[1]], [inicio])]  
    visitados = set()  

    while cola:
        utilidad_acumulada, camino = heapq.heappop(cola)
        x, y = camino[-1]

        if (x, y) == destino:
            return camino, utilidad_acumulada

        if (x, y) in visitados:
            continue
        visitados.add((x, y))

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and (nx, ny) not in visitados:
                nuevo_camino = list(camino)
                nuevo_camino.append((nx, ny))
                nueva_utilidad = utilidad_acumulada + entorno[nx][ny]
                heapq.heappush(cola, (nueva_utilidad, nuevo_camino))

    return None, 0  

camino_optimo, utilidad_optima = buscar_ruta_optima(entorno, inicio, destino)

if camino_optimo:
    print(f"Recorrido óptimo: {camino_optimo}")
    print(f"Utilidad del camino óptimo: {utilidad_optima}")
else:
    print("No se encontró un camino válido.")
