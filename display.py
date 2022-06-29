import matplotlib.pyplot as plt
import numpy as np

import StateD
import agent


def display_Q(data):
    plt.imshow(data)
    plt.show()


def strategy_display(qtable):
    NT = StateD.constant.Ntrain
    qhis = agent.strategy(qtable)
    print(qhis)
    print(qhis[45])
    x = []
    y = []
    for i in range(NT):
        x.append(qhis[i][0])
        y.append(qhis[i][1])

    print(x)

    plt.ion()  # 开启交互模式
    plt.subplots()
    plt.scatter(qhis[:][0],qhis[:][1])

    for n in range(NT):
        plt.clf()  # 清空画布
        plt.xlim(30, 60)  # 因为清空了画布，所以要重新设置坐标轴的范围
        plt.ylim(40, 70)
        plt.scatter(qhis[n][0], qhis[n][1])
        plt.pause(0.1)
    plt.ioff()
    plt.show()


if __name__ == '__main__':
    a = np.loadtxt("Qtable_100_100.csv", delimiter=",")
    # print(agent.strategy(a))
    strategy_display(a)
