import numpy as np

def cholesky(A):
    """Implementación del algoritmo de descomposición de Cholesky, versión producto exterior.
    Dado un arreglo bidimensional A, devuelve G triangular superior tal que G.T @ G = A.

    Esta función actúa sobre el arreglo A, por lo que al terminar la función el mismo se va a
    modificar. Para poder mantener A, es posible definir G como una copia de A, pero hay que
    realizar otras operaciones para terminar de tener una matriz triangular superior.

    """
    n = A.shape[0]
    G = np.zeros((n, n))

    assert np.array_equal(A, A.T), "La matriz no es simétrica"
        
    for idx in range(n):
        if A[idx, idx] <= 0:
            print("A no es definida positiva")
            break
        G[idx, idx] = np.sqrt(A[idx, idx]) # = A[idx, idx] ** 0.5
        # J = {i + 1, n} -> Python idx+1:n
        G[idx, idx+1:n] = A[idx, idx+1:n] / G[idx, idx]
        A[idx+1:n, idx+1:n] = A[idx+1:n, idx+1:n] - np.outer(G[idx, idx+1:n], G[idx, idx+1:n])

    return G

# Podemos probar el algoritmo con las siguientes líneas
A = np.array([
    [4, 2, 6],
    [2, 2, 5],
    [6, 5, 29],
], dtype=float)
G = cholesky(A)
print(G.T @ G)
