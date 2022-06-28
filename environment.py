import numpy as np
from numpy.random import random


def EnvironmentCreate():
    size = 100
    E_0 = 10
    env = np.zeros([size, size])
    for i in range(size):
        for j in range(size):
            env[i][j] = E_0 * random()
    return env


def EnvironmentStore(env):
    np.savetxt('environmentgrass.txt', env)

def step(action):
