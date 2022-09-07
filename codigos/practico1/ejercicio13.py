from ejercicio12 import cholesky
import numpy as np

def calor(N):
    # Genero diagonal
    A = np.diag(2 * np.ones(N))
    # Agrego subdiagonal
    A = A + np.diag(-1 * np.ones(N - 1), -1)
    # Agrego supradiagonal
    A = A + np.diag(-1 * np.ones(N - 1), 1) 

    return A

A = calor(100)
G = cholesky(A)
print(G.T @ G)
