import math
from random import random
import numpy as np

def maybe_bitflip(theta_x):
    if random() < theta_x:
        return [[0, 1], [1, 0]]
    return [[1, 0], [0, 1]]

def maybe_phaseflip(theta_z):
    if random() < theta_z:
        return [[0, 1], [1, 0]]
    return [[1, 0], [0, -1]]

def maybe_randomrotation(theta_x, theta_y, theta_z):
    matrix = np.array([[1,0],[0,1]])
    if random()*np.pi < theta_x:
        matrix = matrix @ np.array([[np.cos(random()*theta_x/2), -1j * np.sin(random()*theta_x/2)],
                                    [-1j * np.sin(random()*theta_x/2), np.cos(random()*theta_x/2)]])
    if random()*np.pi < theta_y:
        matrix = matrix @ np.array([[np.cos(random()*theta_y/2), -np.sin(random()*theta_y/2)],
                                    [np.sin(random()*theta_y/2),  np.cos(random()*theta_y/2)]])
    if random()*np.pi < theta_z:
        matrix = matrix @ np.array([[np.exp(-1j * random()*theta_z / 2), 0],
                                    [0, np.exp(1j * random()*theta_z / 2)]])
    return matrix.tolist()

def maybe_flip(protocol, theta_x, theta_y, theta_z):
    if protocol == 0: return maybe_bitflip(theta_x)
    if protocol == 1: return maybe_phaseflip(theta_z)
    if protocol == 2: return maybe_randomrotation(theta_x, theta_y, theta_z)