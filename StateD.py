import numpy as np


class constant:  # 程序常数
    Ntrain = 100  # 蒙特卡洛游走次数
    gamma = 0.9  # 奖励衰减系数
    size = 100  # 地图大小
    E_0 = 10  # 地图能量参数


class state:  # 初始化状态类
    position = np.zeros(2)  # 智能体位置
    energy = 0  # 智能体能量
    egrass = np.zeros([constant.size, constant.size])  # 草地能量
    eterrian = np.zeros([constant.size, constant.size])  # 地形损耗
    Qlearning = np.zeros([constant.size, constant.size])  # 回报函数表


class action:  # 初始化动作类
    move = np.zeros(2)
    done = 0


class qtable:
    Qlearning = np.zeros([constant.size, constant.size])  # 回报函数表
