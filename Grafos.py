import math

def floyd_warshall(dist):
    n = len(dist)
    # copia para no modificar la original
    d = [fila[:] for fila in dist]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d

# Nodos en orden: D, N, S, O, E
INF = math.inf
nodos = ["D", "N", "S", "O", "E"]

# Matriz de adyacencia inicial (minutos)
D = [
    [0, 7, 9, 3, 10],
    [7, 0, 15, INF, 2],
    [9, 15, 0, 4, 4],
    [3, INF, 4, 0, 8],
    [10, 2, 4, 8, 0],
]

resultado = floyd_warshall(D)

# Mostrar tabla final formateada
anchos = [1] + [max(3, len(n)) for n in nodos]
fila_header = "    " + "  ".join(f"{n:>3}" for n in nodos)
print(fila_header)
for i, fila in enumerate(resultado):
    celdas = []
    for v in fila:
        celdas.append("∞".rjust(3) if v == INF else f"{int(v):>3}")
    print(f"{nodos[i]:>3} " + "  ".join(celdas))
