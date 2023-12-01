import numpy as np

def rz(phi):
    return [[np.exp(-1j * phi/2), 0],
                [0, np.exp(1j * phi/2)]]