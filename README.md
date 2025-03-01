================================================================= REFLEJO SIMPLE ==============================================================================================

 este código crea un "agente" que se mueve a lo largo de una ruta, evitando obstáculos. El agente comienza en el punto (0, 0) y sigue una serie de puntos hasta llegar al final.
 Si se encuentra con un obstáculo en su camino, como en las posiciones (2, 0) o (4, 0), cambia de dirección para evitarlo. Además, si llega al final de la ruta, empieza a retroceder.
 El agente sigue moviéndose de un lado a otro, repitiendo este proceso de forma continua, reaccionando ante los obstáculos cada vez que los encuentra, y con un pequeño retraso de 1 segundo entre cada movimiento.
 Esto simula el comportamiento de un agente que patrulla constantemente, ajustando su camino para no chocar con los obstáculos.

 ============================================================== ESTADO INTERNO ==============================================================================================

Este código simula un agente explorador que recorre un mapa, buscando celdas accesibles que aún no ha visitado. El mapa está representado por una matriz de valores,
donde 1 indica que la celda es accesible y 0 significa que es un obstáculo. El agente comienza en la posición (0, 0) y su objetivo es explorar el mapa, moviéndose a celdas
vecinas que no haya visitado y que sean accesibles. El agente tiene cuatro posibles direcciones para moverse: arriba, abajo, izquierda y derecha. En cada movimiento, el agente
elige aleatoriamente una de esas direcciones y verifica si la celda adyacente es válida (es decir, si está dentro de los límites del mapa y es accesible). Si el agente puede moverse a una nueva celda, 
la marca como visitada y continúa explorando. Si el agente no puede moverse, se detiene y muestra un mensaje indicando que ya no hay más celdas accesibles o que está atascado. Al finalizar, 
el agente imprime todas las posiciones que ha visitado. El proceso de exploración sigue ocurriendo hasta que ya no pueda avanzar más.

 ============================================================== BASADOS EN META ==============================================================================================

Este código implementa un algoritmo de búsqueda en amplitud (BFS) para encontrar la ruta más corta en un laberinto, desde un punto de inicio hasta un punto meta. El laberinto es una matriz donde 0 representa una celda accesible,
1 es una pared o bloqueada, y 'M' es la meta, es decir, el objetivo del agente. El agente comienza en la celda (0, 0) y su objetivo es llegar a la celda (4, 4) (la meta). Para hacer esto,
el algoritmo BFS explora el laberinto de manera que primero revisa las celdas cercanas y luego se adentra más en el laberinto, asegurando que encuentra la ruta más corta.
El algoritmo comienza en el punto de inicio y utiliza una cola (implementada con deque) para mantener un registro de las celdas por explorar y el camino recorrido hasta ese punto.
A medida que explora, marca las celdas visitadas para evitar ciclos o recorrer la misma celda más de una vez. En cada paso, el algoritmo intenta moverse en una de las cuatro direcciones posibles 
(arriba, abajo, izquierda y derecha). Si llega a la meta, devuelve el camino seguido; si no puede encontrar una ruta, devuelve None.
Si se encuentra una ruta válida, el programa imprime las coordenadas de cada paso que sigue el agente desde el inicio hasta la meta.
Si no es posible encontrar un camino, muestra el mensaje "No se encontró una ruta válida".

 ============================================================== BASADOS EN UTILIDAD ==============================================================================================

Este código implementa un algoritmo de búsqueda para encontrar la ruta óptima en un entorno representado por una matriz, donde cada celda tiene un valor que puede ser positivo, negativo o cero.
El objetivo es encontrar la ruta que maximice la "utilidad", que es la suma de los valores de las celdas por las que pasa el agente, desde un punto de inicio hasta un destino específico. 
El algoritmo utiliza una búsqueda con prioridad (heapq) para explorar el entorno, donde las rutas con mayor utilidad se exploran primero.
El entorno está representado como una matriz, y cada celda tiene un valor asociado que puede representar, por ejemplo, un coste o beneficio de pasar por ahí. 
El agente comienza en el punto (0, 0) y se dirige hacia el destino (3, 3). A medida que avanza, el algoritmo evalúa las celdas vecinas (arriba, abajo, izquierda, derecha)
y calcula la utilidad acumulada de cada posible camino. Para asegurarse de explorar siempre la ruta con mayor utilidad, utiliza una cola de prioridad (min-heap) donde las rutas con mayor utilidad acumulada tienen prioridad.

El algoritmo explora las celdas hasta encontrar el destino. Una vez que llega al destino, devuelve el camino seguido y la utilidad total de ese camino.
Si no se encuentra un camino válido, el algoritmo devuelve un mensaje indicando que no se pudo encontrar un camino. En resumen, 
el código busca optimizar la ruta del agente basándose en la utilidad de las celdas, priorizando las rutas con mayor valor acumulado.




