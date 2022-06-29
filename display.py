import matplotlib.pyplot as plt
import numpy as np

import StateD
import agent


def display_Q(data):
    plt.imshow(data)
    plt.show()


def strategy_display(qtable):
    qhis = agent.strategy(qtable)
    NT = StateD.constant.Ntrain
    plt.ion()  # 开启交互模式
    plt.subplots()

    for n in range(NT):
        plt.clf()  # 清空画布
        plt.xlim(0, 100)  # 因为清空了画布，所以要重新设置坐标轴的范围
        plt.ylim(0, 100)
        plt.scatter(qhis[0][n], qhis[1][n])
        plt.pause(0.2)
    plt.ioff()
    plt.show()


if __name__ == '__main__':
    a = np.loadtxt("Qtable_100_100.csv", delimiter=",")
    print(agent.strategy(a))
    strategy_display(a)
