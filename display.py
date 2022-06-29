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
    plt.scatter(qhis[:][0], qhis[:][1])

    for n in range(NT):
        plt.clf()  # 清空画布
        plt.xlim(30, 60)  # 因为清空了画布，所以要重新设置坐标轴的范围
        plt.ylim(40, 70)
        plt.scatter(qhis[n][0], qhis[n][1])
        plt.pause(0.1)
    plt.ioff()
    plt.show()


def strategy_display_2():
    qhis = [[51, 50],
              [51, 51],
              [51, 52],
              [52, 52],
              [52, 51],
              [52, 50],
              [52, 49],
              [53, 49],
              [53, 48],
              [54, 48],
              [55, 48],
              [55, 47],
              [55, 46],
              [54, 46],
              [53, 46],
              [52, 46],
              [52, 47],
              [51, 47],
              [51, 48],
              [50, 48],
              [50, 49],
              [49, 49],
              [48, 49],
              [48, 50],
              [47, 50],
              [47, 51],
              [46, 51],
              [46, 52],
              [45, 52],
              [45, 53],
              [45, 54],
              [46, 54],
              [47, 54],
              [47, 55],
              [47, 56],
              [47, 57],
              [47, 58],
              [46, 58],
              [45, 58],
              [44, 58],
              [43, 58],
              [42, 58],
              [42, 57],
              [43, 56],
              [43, 55],
              [43, 54],
              [42, 54],
              [41, 54],
              [40, 54],
              [40, 55],
              [41, 55],
              [41, 56],
              [40, 56],
              [39, 56],
              [38, 56],
              [37, 56],
              [36, 56],
              [36, 57],
              [35, 57],
              [35, 56],
              [34, 56],
              [34, 55],
              [35, 55],
              [36, 55],
              [37, 54],
              [37, 53],
              [37, 52],
              [36, 52],
              [36, 53],
              [35, 53],
              [34, 53],
              [33, 53],
              [33, 54],
              [34, 54],
              [35, 54],
              [35, 53],
              [35, 52],
              [34, 52],
              [33, 52],
              [32, 52],
              [31, 52],
              [31, 53],
              [30, 54],
              [29, 54],
              [28, 54],
              [29, 55],
              [30, 55],
              [30, 56],
              [30, 57],
              [30, 58],
              [31, 58],
              [31, 59],
              [32, 59],
              [33, 59],
              [34, 59],
              [34, 60]]
    NT = 100
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
    strategy_display_2()
