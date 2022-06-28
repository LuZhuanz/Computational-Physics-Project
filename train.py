import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import agent  # 智能体模块
import StateD  # 类型声明
import environment  # 环境操作模块


def training(i, j):
    N = StateD.constant.size
    testate = StateD.state  # 初始化智能体
    testate.position = [i, j]
    testate.energy = StateD.constant.E_0
    ep_state = testate
    q_sum = 0

    for i in range(StateD.constant.Ntrain):
        ep_reward = 0
        q_count = 0
        q_state = 0
        while True:
            ep_action = agent.choose_action(testate)
            ep_state, reward = environment.step(ep_action, ep_state)
            ep_reward = ep_reward + reward
            q_count = q_count + 1
            q_add = np.power(StateD.constant.gamma, q_count) * reward
            q_state = q_state + q_add

            if q_add < 0.02:
                break
        q_sum = q_sum + q_state
    q_solution = q_sum / StateD.constant.Ntrain
    return q_solution


def whole_training():
    new_Qlearning = np.zeros([StateD.constant.size, StateD.constant.size])
    for i in range(StateD.constant.size):
        for j in range(StateD.constant.size):
            new_q = training(i, j)
            new_Qlearning[i][j] = new_q
    return new_Qlearning

