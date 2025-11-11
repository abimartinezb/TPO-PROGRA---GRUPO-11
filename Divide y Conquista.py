import math

# 1. DIVIDE Y CONQUISTA

def distancia(p1, p2):
    """Calcula la distancia euclidiana entre dos puntos."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def fuerza_bruta(puntos):
    """Resuelve el problema por fuerza bruta cuando hay pocos puntos."""
    min_dist = float('inf')
    par_min = (None, None)
    n = len(puntos)
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = distancia(puntos[i], puntos[j])
            if d < min_dist:
                min_dist = d
                par_min = (puntos[i], puntos[j])
    return min_dist, par_min


def par_mas_cercano_rec(Px, Py):
    """Algoritmo recursivo de Divide y Conquista."""
    n = len(Px)

    # Caso base
    if n <= 3:
        return fuerza_bruta(Px)

    # 1) Dividir
    mid = n // 2
    x_med = Px[mid][0]

    Qx = Px[:mid]
    Rx = Px[mid:]

    Qy = [p for p in Py if p[0] < x_med]
    Ry = [p for p in Py if p[0] >= x_med]

    # 2) Conquistar
    d_izq, par_izq = par_mas_cercano_rec(Qx, Qy)
    d_der, par_der = par_mas_cercano_rec(Rx, Ry)

    if d_izq <= d_der:
        d_min = d_izq
        par_min = par_izq
    else:
        d_min = d_der
        par_min = par_der

    # 3) Combinar (Strip)
    strip = [p for p in Py if abs(p[0] - x_med) < d_min]

    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d = distancia(strip[i], strip[j])
            if d < d_min:
                d_min = d
                par_min = (strip[i], strip[j])

    return d_min, par_min


def par_mas_cercano(puntos):
    """Función principal que ordena los puntos y llama al recursivo."""
    Px = sorted(puntos, key=lambda p: p[0])
    Py = sorted(puntos, key=lambda p: p[1])
    return par_mas_cercano_rec(Px, Py)


# Ejemplos de prueba

if __name__ == "__main__":

    # Ejemplo 1: pocos puntos simples
    puntos1 = [(1, 2), (3, 4), (5, 1)]
    print("Ejemplo 1:", par_mas_cercano(puntos1))

    # Ejemplo 2: puntos cercanos
    puntos2 = [(0, 0), (1, 1), (1.1, 1.2), (5, 5)]
    print("Ejemplo 2:", par_mas_cercano(puntos2))

    # Ejemplo 3: conjunto más grande
    puntos3 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print("Ejemplo 3:", par_mas_cercano(puntos3))

    # Ejemplo 4: puntos con coordenadas negativas
    puntos4 = [(-1, -1), (-2, -3), (4, 0), (0, 0)]
    print("Ejemplo 4:", par_mas_cercano(puntos4))

    # Ejemplo 5: puntos alineados en eje x
    puntos5 = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    print("Ejemplo 5:", par_mas_cercano(puntos5))
