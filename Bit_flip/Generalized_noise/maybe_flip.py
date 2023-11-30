from random import random

def maybe_flip(flipping_probability):
    if random() < flipping_probability:
        return [[0, 1], [1, 0]]
    return [[1, 0], [0, 1]]