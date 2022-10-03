import matplotlib.pyplot as plt
import numpy as np

N = 1000

def tranfbola(A):
    theta = np.linspace(0, 2 * np.pi, N)

    xx = np.cos(theta)
    yy = np.sin(theta)

    vectores = np.zeros((2, N))
    vectores[0, :] = xx
    vectores[1, :] = yy

    tranfbola = A @ vectores
    plt.plot(xx, yy, label="bola unidad")
    plt.plot(tranfbola[0, :], tranfbola[1, :], label="bola transformada")
    plt.axis("equal")
    plt.show()

A = np.array([
    [1000, 999],
    [999, 998],
], dtype=float)
tranfbola(A)
