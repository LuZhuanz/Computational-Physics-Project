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


def step(action, state):  # 按指令行动后反应
    state.position = state.position + action.move
    GrassEnergy = 0.1 * state.egrass(state.position)
    TerrainEnergy = state.energy * state.eterrian
    state.energy = state.energy + GrassEnergy - TerrainEnergy
    state.egrass[state.position] = state.egrass[state.position] * 0.9
    return state
