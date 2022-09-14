import numpy as np

def dlu(A):
    n = A.shape[0]

    for jdx in range(n-1):
        # Vector de multiplicadores
        A[jdx+1:n, jdx] = A[jdx+1:n, jdx] / A[jdx, jdx]
        # Para aplicar el vector de multiplicadores en vez de usar un for, podemos hacer un producto exterior
        A[jdx+1:n, jdx+1:n] -= np.outer(A[jdx+1:n, jdx], A[jdx, jdx+1:n])

    # Parte triangular superior
    U = np.triu(A)
    # Parte triangular inferior sin diagonal + identidad
    L = np.tril(A, -1) + np.eye(n)

    return L, U

A = 4 * np.eye(5) - np.diag(np.ones(4), -1) - np.diag(np.ones(4), 1)
B = A.copy()

L, U = dlu(A)

print(L @ U)
print(B)

print(np.allclose(L @ U, B))
print(L, U)
