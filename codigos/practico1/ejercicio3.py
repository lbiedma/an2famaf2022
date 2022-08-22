import numpy as np

def sol_trsupcol(A, b):
    """ Función que resuelve un sistema triangular superior por columnas """
    # Comenzamos con una copia de b
    x = b.copy()
    # Como no necesitamos realizar trabajo si los últimos elementos
    # de b son cero, buscamos el último elemento no nulo, sumamos 1
    # teniendo en cuenta que el range llega hasta k - 1
    k = np.max(np.nonzero(b)) + 1
    # range(k) :k
    
    for j in reversed(range(k)):
        x[j] = x[j] / A[j, j]
        # I = {0, ..., j-1} -> 0:j
        # No debemos modificar x[j] porque ya lo hicimos arriba
        x[0:j] = x[0:j] - A[0:j, j] * x[j]

    return x


def test_sol_trsupcol():
    A = np.array([
        [9, 2, 4],
        [0, -6, 3],
        [0, 0, 5],
    ], dtype=float)
    b = np.array([18, -2, 7], dtype=float)

    x = sol_trsupcol(A, b)
    n = A.shape[0]
    print(A @ x - b)
    # Usando assert podemos asegurar que nuestro programa funciona bien
    assert np.allclose(
        np.zeros(n), A @ x - b
    ), "Los vectores no coinciden"

test_sol_trsupcol()
