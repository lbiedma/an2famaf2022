import matplotlib.pyplot as plt
import numpy as np

def transformacion_bola_unidad():
    """
    Esta función nos permite generar una matriz SDP aleatoria y
    visualizar cómo afecta a la bola unidad.
    """
    # definir mi matriz aleatoria SDP
    A = np.random.randn(2, 2)
    A = A @ A.T

    # Genero bola unidad
    r = np.linspace(0, 2 * np.pi, 100)
    cosenos = np.cos(r)
    senos = np.sin(r)

    # Genero transformación de la bola unidad
    y_0 = np.zeros(100)
    y_1 = np.zeros(100)
    for i in range(100):
        res = A @ np.array([cosenos[i], senos[i]])
        y_0[i] = res[0]
        y_1[i] = res[1]

    # Grafico ambas
    plt.plot(cosenos, senos, label="bola unidad")
    plt.plot(y_0, y_1, label="transformacion")
    plt.legend()
    plt.axis("equal")
    plt.show()

transformacion_bola_unidad()
