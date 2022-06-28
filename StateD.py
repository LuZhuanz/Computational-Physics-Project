import numpy as np


class state:  # 初始化状态类
    position = np.zeros(2)  # 智能体位置
    energy = 0  # 智能体能量
    egrass = np.zeros([100, 100])  # 草地能量
    eterrian = np.zeros([100, 100])  # 地形损耗
    Qlearning = np.zeros([100, 100])  # 回报函数表


class action:  # 初始化动作类
    move = np.zeros(2)
