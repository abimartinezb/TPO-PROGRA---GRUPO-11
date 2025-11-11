
# 2. GREEDY

def SeleccionarActividades(A):
    if not A: 	
        return []

    A.sort(key=lambda x: x[2])

    R = [A[0]]
    ultimoFin = A[0][2]

    for i in range(1, len(A)):
        if A[i][1] >= ultimoFin:
            R.append(A[i])
            ultimoFin = A[i][2]
    return R


#Caso de Prueba
act1 = [('A', 2, 6), ('B', 0, 3), ('C', 13, 17), ('D', 3, 6), ('E', 4, 12), ('F', 8, 9), ('G', 5, 9), ('H', 8, 11), ('I', 18, 22), ('J', 17, 20), ('K', 10, 12)]
resultado = SeleccionarActividades(act1)
print(f"Actividades originales: {len(act1)}")
print(f"Máximo de actividades no superpuestas: {len(resultado)}")
print(f"Actividades seleccionadas: {resultado}\n")
