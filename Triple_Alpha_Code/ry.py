import numpy as np

def ry(theta):
    return [[np.cos(theta/2), -np.sin(theta/2)],
                [np.sin(theta/2), np.cos(theta/2)]]
