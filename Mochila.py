
# 3. PROGRAMACION DINAMICA - MOCHILA

def mochilaPG(w, O):
    #O (contiene: [0] id, [1] valor, [2] peso)
    M = [[0 for _ in range(w + 1)] for _ in range(len(O))]

    for i in range(len(O)):
        for j in range(w + 1):
            peso = O[i][2]
            valor = O[i][1]
            if (i == 0 and peso > j):
                M[i][j] = 0
            else: 
                if (i == 0):
                    M[i][j] = valor
                elif (peso > j):
                    M[i][j] = M[i - 1][j]
                else:
                    M[i][j] = max(M[i - 1][j], M[i - 1][j - peso] + valor)

    # Reconstrucción de la solución (bottom-up)
    R = []
    wActual = w
    i = len(O) - 1

    while (i > 0 and wActual > 0):
        if (M[i][wActual] > M[i - 1][wActual]):
            R.append(O[i][0]) #id
            wActual -= O[i][2] #peso
        i -= 1

    if (i == 0 and wActual >= O[0][2]):
        R.append(O[0][0])
    return R[::-1]# Retornar los objetos seleccionados y ordenados como Objetos

#Pruebas con diferentes capacidades y objetos

objetos = [('A', 20, 4), ('B', 10, 6), ('C', 12, 3), ('D', 18, 5), ('E', 8, 2), ('F', 22, 7)]
peso = 18
resultado = mochilaPG(peso, objetos)
print(f"Objetos originales: {len(objetos)}")
print(f"Cantidad de objetos a robar: {len(resultado)}")
print(f"Objetos seleccionados en función de su costo para peso {peso}: {resultado}\n")
