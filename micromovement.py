import numpy as np
import matplotlib.pylab as plt
import random as rdm
import matplotlib.animation as animation

h = 0.01  # 空间步长
tau = 1  # 时间步长
NS = 75  # 羊只数
NT = 10000  # 总时长
N = 1000  # 空间格数
temph = 0.5  # 最高温度
templ = 0.0000001  # 最低温度

sheepx = np.zeros([NS, NT], dtype='float')
sheepy = np.zeros([NS, NT], dtype='float')  # 创建用于储存每只羊在任意时刻xy坐标的数组

occupy = np.zeros([N + 1, N + 1], dtype='int')  # 创建用于防止两只羊重合的数组

sheepx[0, 0] = h * rdm.randint(0, N)
sheepy[0, 0] = h * rdm.randint(0, N)  # 随机设定头羊初始位置

occupy[int(sheepx[0, 0] / h), int(sheepy[0, 0] / h)] = 1  # 占据头羊位置

for i in range(1, NS):  # 随机给每只羊赋予位置
    sheepx[i, 0] = h * rdm.randint(0, N)
    sheepy[i, 0] = h * rdm.randint(0, N)

    if occupy[int(sheepx[i, 0] / h), int(sheepy[i, 0] / h)] == 0:  # 防止两只羊重合
        occupy[int(sheepx[i, 0] / h), int(sheepy[i, 0] / h)] = 1
    else:
        i = i - 1


def grass(x, y):  # 定义草场
    g = (x - 1.0) * (0.3 * x - 2.0) * (0.5 * x - 3.0) * (0.4 * x - 4.0) + (y - 1.0) * (0.3 * y - 2.0) * (
            0.5 * y - 3.0) * (0.4 * y - 4.0)
    return g


leader_sheepxold = sheepx[0, 0]
leader_sheepyold = sheepy[0, 0]
grassold = grass(leader_sheepxold, leader_sheepyold)  # 设定头羊运动初始条件

for j in range(1, NT):
    leader_sheepxnew = leader_sheepxold + h * rdm.randint(-10, 10)
    leader_sheepynew = leader_sheepyold + h * rdm.randint(-10, 10)
    grassnew = grass(leader_sheepxnew, leader_sheepynew)
    jd = rdm.random()
    temp = np.minimum(templ + ((temph - templ) / NT) * j, temph - ((temph - templ) / NT) * j)

    if (grassnew - grassold) < 0:  # 退火模拟头羊运动
        occupy[int(leader_sheepxold / h), int(leader_sheepyold / h)] = 0
        leader_sheepxold = leader_sheepxnew
        leader_sheepyold = leader_sheepynew
        grassold = grassnew
    elif jd < np.exp(-(grassnew - grassold) / temp):
        occupy[int(leader_sheepxold / h), int(leader_sheepyold / h)] = 0
        leader_sheepxold = leader_sheepxnew
        leader_sheepyold = leader_sheepynew
        grassold = grassnew

    sheepx[0, j] = leader_sheepxold  # 储存头羊轨迹
    sheepy[0, j] = leader_sheepyold
    occupy[int(sheepx[0, j] / h), int(sheepy[0, j] / h)] = 1

    for i in range(1, NS):  # 对每一只羊，由其与头羊的作用计算其轨迹
        sheepx[i, j] = sheepx[i, j - 1] + (int((sheepx[0, j] - sheepx[i, j - 1]) * 10 * rdm.random())) * h
        sheepy[i, j] = sheepy[i, j - 1] + (int((sheepy[0, j] - sheepy[i, j - 1]) * 10 * rdm.random())) * h

        if occupy[int(sheepx[i, j] / h), int(sheepy[i, j] / h)] == 0:
            occupy[int(sheepx[i, j] / h), int(sheepy[i, j] / h)] = 1
        else:
            for k in range(0, 1000):  # 若发现格点上已有羊，则随机往四周让开
                sheepx[i, j] = sheepx[i, j] + h * (rdm.randint(0, 1) * 2 - 1)
                sheepy[i, j] = sheepy[i, j] + h * (rdm.randint(0, 1) * 2 - 1)

                if sheepx[i, j] < 0:  # 防止羊走出边界
                    sheepx[i, j] = sheepx[i, j] + h
                if sheepy[i, j] < 0:
                    sheepy[i, j] = sheepy[i, j] + h
                if sheepx[i, j] > 10:
                    sheepx[i, j] = sheepx[i, j] - h
                if sheepy[i, j] > 10:
                    sheepx[i, j] = sheepx[i, j] - h

                if occupy[int(sheepx[i, j] / h), int(sheepy[i, j] / h)] == 0:
                    occupy[int(sheepx[i, j] / h), int(sheepy[i, j] / h)] = 1
                break
for i in range(0, 75):
    print(sheepx[i, 9999])

"""
plt.ion()  # 开启交互模式
plt.subplots()

for n in range(NT):
    plt.clf()  # 清空画布
    plt.xlim(0, 10)  # 因为清空了画布，所以要重新设置坐标轴的范围
    plt.ylim(0, 10)
    plt.scatter(sheepx[:][n], sheepy[:][n])
    plt.pause(0.2)
plt.ioff()
plt.show()
"""
fig = plt.figure()
ax = fig.add_subplot(1, 1)

# create the first plot
point, = ax.plot([], [], 'r.')
point2, = ax.plot([], [], '.')
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])


def update_point(n, x, y, point):
    point2.set_data([x[0:n], y[0:n]])
    point.set_data([x[n], y[n]])
    # point.set_array([255,0,0])
    return point


ani = animation.FuncAnimation(fig, update_point, 99, fargs=(x, y, point))
ani.save('test5.gif', writer='pillow')
plt.show()
