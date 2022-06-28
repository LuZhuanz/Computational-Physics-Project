import numpy as np
from numpy.random import random
import StateD


def EnvironmentCreate(E_0):  # 初始化环境
    size = 100
    env = np.zeros([StateD.constant.size, StateD.constant.size])
    for i in range(StateD.constant.size):
        for j in range(StateD.constant.size):
            env[i][j] = E_0 * random()
    return env


def EnvironmentStore(env):  # 保存环境
    np.savetxt('environmentgrass.txt', env)


def step(action, state):  # 按指令行动后反应，智能体与环境交互
    state.position = np.add(state.position, action)
    print(state.position)
    GrassEnergy = 0.1 * state.egrass[state.position[0]][state.position[1]]
    print(GrassEnergy)
    TerrainEnergy = np.multiply(state.energy, state.eterrian)
    print(TerrainEnergy)
    state.energy = state.energy + GrassEnergy - TerrainEnergy
    state.egrass[state.position] = state.egrass[state.position] * 0.9
    reward = GrassEnergy - TerrainEnergy
    return state, reward
