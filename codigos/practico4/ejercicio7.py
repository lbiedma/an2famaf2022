import sys
sys.path.append("/home/lbiedma/Documents/facu/numerico_ii/an2famaf2022/codigos")
import numpy as np

from practico1.ejercicio3 import sol_trsupcol
from ejercicio3 import qrgivens

def sol_cuadmin(A, b):
    m, n = A.shape
    # Asumimos que A tiene rango completo
    p = min(m, n)
    y_sol = np.zeros(n)
    Q, R = qrgivens(A)
    q = Q.T @ b
    # I = {1, ..., p} -> :p
    y_sol[:p] = sol_trsupcol(R[:p, :p], q[:p])
    # J = {1, ..., n} \ I = {p + 1, ..., n} -> p:
    residuo = np.linalg.norm(q[p:])

    return y_sol, residuo

A = np.array([[1, 1], [0.5, 0], [0, 0.5]], dtype=float)
b = np.ones(3)

y_sol, residuo = sol_cuadmin(A, b)
print(y_sol)
print(residuo)
