from tkinter import YView
import numpy as np

def egauss(A, b):
    n = A.shape[0]

    U = A.copy()
    y = b.copy()
    m = np.zeros(n)

    for jdx in range(n-1):
        # Vector de multiplicadores
        m[jdx+1:n] = U[jdx+1:n, jdx] / U[jdx, jdx]
        # Para aplicar el vector de multiplicadores en vez de usar un for, podemos hacer un producto exterior
        # U[jdx+1:n, jdx:n] = U[jdx+1:n, jdx:n] - np.outer(m[jdx+1:n], U[jdx, jdx:n]) esta linea y la de abajo son lo mismo
        U[jdx+1:n, jdx:n] -= np.outer(m[jdx+1:n], U[jdx, jdx:n])
        # Actualizamos y
        y[jdx+1:n] -= m[jdx+1:n] * y[jdx]

    return U, y

# Podemos probar rapido este codigo con una matriz diagonal dominante
# y con linalg.solve
A = 4 * np.eye(5) - np.diag(np.ones(4), -1) - np.diag(np.ones(4), 1)
b = np.ones(5)
print(np.linalg.solve(A, b))

U, y = egauss(A, b)
print(np.linalg.solve(U, y)) # Esta linea nos deberia dar lo mismo que el print de arriba si todo anda bien

print(U)
print(y)