import numpy as np
from numpy.random import random


def EnvironmentCreate():  # 初始化环境
    size = 100
    E_0 = 10
    env = np.zeros([size, size])
    for i in range(size):
        for j in range(size):
            env[i][j] = E_0 * random()
    return env


def EnvironmentStore(env):  # 保存环境
    np.savetxt('environmentgrass.txt', env)


def step(action, state):
    state.position = state.position + action.move
    return 0
