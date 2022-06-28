import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import agent  # 智能体模块
import StateD  # 类型声明
import environment  # 环境操作模块

Ntrain = 1000  # 蒙特卡洛游走次数
gamma = 0.9  # 奖励衰减系数


def training():
    testate = StateD.state  # 初始化智能体
    testate.position = [50, 50]
    testate.energy = 10
    rewards = []
    ma_rewards = []
    ep_state = testate

    for i in range(Ntrain):
        ep_reward = 0
        q_count = 0
        q_state = 0
        while True:
            ep_action = agent.choose_action(ep_state)
            ep_state, reward = environment.step(ep_action, ep_state)
            ep_reward = ep_reward + reward
            q_count = q_count + 1
            q_add = np.power(gamma, q_count) * reward
            q_state = q_state + q_add

            if q_add < 0.02:
                break



if __name__ == '__main__':
    print(StateD.state.position)
    StateD.state.position = [23, 45]
    print(StateD.state.position)
