import matplotlib.pyplot as plt
import numpy as np

dets = []
conds = []

for i in range(50):
    # [1, 1-eps]
    # [0, 1    ]
    eps = 2.0 ** -i
    A = np.array([
        [1/eps, 1],
        [0,   eps],
    ], dtype=float)
    dets.append(1.0)
    conds.append(np.linalg.cond(A))

plt.semilogy(dets, label="determinantes")
plt.semilogy(conds, label="condiciones")
plt.legend()
plt.show()
