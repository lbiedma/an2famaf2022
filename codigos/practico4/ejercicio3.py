import numpy as np

def givens(a, b):
    c = a / np.sqrt(a**2 + b**2)
    s = b / np.sqrt(a**2 + b**2)

    return c, s

def qrgivens(A):
    m, n = A.shape
    Q = np.eye(m)
    R = A.copy()
    rango = min(m-1, n)

    for jdx in range(rango):
        for idx in range(jdx+1, m):
            # calculo givens
            c, s = givens(R[jdx, jdx], R[idx, jdx])
            rot = np.array([
                [c, s],
                [-s, c]
            ])
            indices = [jdx, idx]
            R[indices, :] = rot @ R[indices, :]
            Q[:, indices] = Q[:, indices] @ rot.T

    return Q, R

