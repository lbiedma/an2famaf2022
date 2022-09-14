import numpy as np

def dlup(A):
    n = A.shape[0]
    p = np.arange(n)

    for jdx in range(n-1):
        # Ubicar maximo desde la columna hacia abajo
        kmax = np.argmax(np.abs(A[jdx:n, jdx])) + jdx
        if kmax != jdx:
            # Pivoteo p y A
            par_index = [kmax, jdx]
            p[[jdx, kmax]] = p[par_index]
            A[[jdx, kmax], :] = A[par_index, :]

        # Vector de multiplicadores
        A[jdx+1:n, jdx] = A[jdx+1:n, jdx] / A[jdx, jdx]
        # Para aplicar el vector de multiplicadores en vez de usar un for, podemos hacer un producto exterior
        A[jdx+1:n, jdx+1:n] -= np.outer(A[jdx+1:n, jdx], A[jdx, jdx+1:n])

    # Parte triangular superior
    U = np.triu(A)
    # Parte triangular inferior sin diagonal + identidad
    L = np.tril(A, -1) + np.eye(n)

    return p, L, U

# Pruebo con la matriz del ejercicio 10
A = np.array([
    [2, 10, 8, 8, 6],
    [1, 4, -2, 4, -1],
    [0, 2, 3, 2, 1],
    [3, 8, 3, 10, 9],
    [1, 4, 1, 2, 1],
], dtype=float)

B = A.copy()
p, L, U = dlup(A)
print(L @ U)
print(B[p, :])
