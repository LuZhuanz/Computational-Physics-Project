import numpy as np
import StateD


def choose_action(state_e):  # 由Q表格选择策略,羊群策略记入action
    if state_e.position[0] == 0:  # 考虑边界上的情况
        if state_e.position[1] == 0:
            if state_e.Qlearning[0][1] == 0 and state_e.Qlearning[1][0] == 0:
                split_1 = 0.5
            else:
                split_1 = state_e.Qlearning[0][1] / (state_e.Qlearning[0][1] + state_e.Qlearning[1][0])
            seed = np.random.random()  # 根据不同方向的奖励函数分配随机行走的概率权重，初始为完全随机
            if split_1 < seed:
                action = [1, 0]
            else:
                action = [0, 1]
        elif state_e.position[1] == StateD.constant.size - 1:
            if state_e.Qlearning[StateD.constant.size - 1][1] == 0 and state_e.Qlearning[StateD.constant.size - 2][
                0] == 0:
                split_1 = 0.5
            else:
                split_1 = state_e.Qlearning[0][StateD.constant.size - 2] / (
                        state_e.Qlearning[0][StateD.constant.size - 2] + state_e.Qlearning[1][
                    StateD.constant.size - 1])
            seed = np.random.random()
            if split_1 < seed:
                action = [1, 0]
            else:
                action = [0, -1]
        else:
            Qsum = state_e.Qlearning[0][int(state_e.position[1]) + 1] + state_e.Qlearning[0][
                int(state_e.position[1]) - 1] + \
                   state_e.Qlearning[1][int(state_e.position[1])]
            split_1 = state_e.Qlearning[0][int(state_e.position[1]) + 1] / Qsum
            split_2 = (state_e.Qlearning[0][int(state_e.position[1]) + 1] + state_e.Qlearning[1][
                int(state_e.position[1])]) / Qsum
            seed = np.random.random()
            if seed < split_1:
                action = [0, 1]
            elif seed < split_2:
                action = [1, 0]
            else:
                action = [0, 1]
    elif state_e.position[0] == StateD.constant.size - 1:
        if state_e.position[1] == 0:
            if state_e.Qlearning[StateD.constant.size - 1][1] == 0 and state_e.Qlearning[StateD.constant.size - 2][
                0] == 0:
                split_1 = 0.5
            else:
                split_1 = state_e.Qlearning[StateD.constant.size - 1][1] / (
                        state_e.Qlearning[StateD.constant.size - 1][1] +
                        state_e.Qlearning[StateD.constant.size - 2][0])
            seed = np.random.random()
            if split_1 < seed:
                action = [-1, 0]
            else:
                action = [0, 1]
        elif state_e.position[1] == StateD.constant.size - 1:
            if state_e.Qlearning[StateD.constant.size - 1][StateD.constant.size - 2] == 0 and \
                    state_e.Qlearning[StateD.constant.size - 1][StateD.constant.size - 2] == 0:
                split_1 = 0.5
            else:
                split_1 = state_e.Qlearning[StateD.constant.size - 1][StateD.constant.size - 2] / (
                        state_e.Qlearning[StateD.constant.size - 1][StateD.constant.size - 2] +
                        state_e.Qlearning[StateD.constant.size - 2][StateD.constant.size - 1])
            seed = np.random.random()
            if split_1 < seed:
                action = [-1, 0]
            else:
                action = [0, -1]
        else:
            if state_e.Qlearning[StateD.constant.size - 1][int(state_e.position[1]) + 1] == 0 and \
                    state_e.Qlearning[StateD.constant.size - 1][int(state_e.position[1]) - 1] == 0 and \
                    state_e.Qlearning[StateD.constant.size - 2][int(state_e.position[1])] == 0:
                split_1 = 1 / 3
                split_2 = 2 / 3
            else:
                Qsum = state_e.Qlearning[StateD.constant.size - 1][int(state_e.position[1]) + 1] + \
                       state_e.Qlearning[StateD.constant.size - 1][int(state_e.position[1]) - 1] + \
                       state_e.Qlearning[StateD.constant.size - 2][int(state_e.position[1])]
                split_1 = state_e.Qlearning[StateD.constant.size - 1][int(state_e.position[1]) + 1] / Qsum
                split_2 = (state_e.Qlearning[StateD.constant.size - 1][int(state_e.position[1]) + 1] +
                           state_e.Qlearning[StateD.constant.size - 2][int(state_e.position[1])]) / Qsum
            seed = np.random.random()
            if seed < split_1:
                action = [0, 1]
            elif seed < split_2:
                action = [-1, 0]
            else:
                action = [0, 1]
    else:
        if state_e.position[1] == 0:
            Qsum = state_e.Qlearning[int(state_e.position[0]) - 1][0] + state_e.Qlearning[int(state_e.position[0])][1] + \
                   state_e.Qlearning[int(state_e.position[0]) + 1][0]
            if Qsum == 0:
                split_1 = 1 / 3
                split_2 = 2 / 3
            else:
                split_1 = state_e.Qlearning[int(state_e.position[0]) - 1][0] / Qsum
                split_2 = split_1 + state_e.Qlearning[int(state_e.position[0])][1] / Qsum
            seed = np.random.random()
            if seed < split_1:
                action = [-1, 0]
            elif seed < split_2:
                action = [0, 1]
            else:
                action = [1, 0]
        elif state_e.position[1] == StateD.constant.size - 1:
            Qsum = state_e.Qlearning[int(state_e.position[0]) - 1][StateD.constant.size - 1] + \
                   state_e.Qlearning[int(state_e.position[0])][StateD.constant.size - 2] + \
                   state_e.Qlearning[int(state_e.position[0]) + 1][StateD.constant.size - 1]
            if Qsum == 0:
                split_1 = 1 / 3
                split_2 = 2 / 3
            else:
                split_1 = state_e.Qlearning[int(state_e.position[0]) - 1][StateD.constant.size - 1] / Qsum
                split_2 = split_1 + state_e.Qlearning[int(state_e.position[0])][StateD.constant.size - 2] / Qsum
            seed = np.random.random()
            if seed < split_1:
                action = [-1, 0]
            elif seed < split_2:
                action = [0, -1]
            else:
                action = [1, 0]
        else:

            Qsum = state_e.Qlearning[int(state_e.position[0]) - 1][int(state_e.position[1])] + \
                   state_e.Qlearning[int(state_e.position[0])][int(state_e.position[1]) + 1] + \
                   state_e.Qlearning[int(state_e.position[0]) + 1][
                       int(state_e.position[1])] + state_e.Qlearning[int(state_e.position[0])][
                       int(state_e.position[1]) - 1]
            if Qsum == 0:
                split_1 = 0.25
                split_2 = 0.5
                split_3 = 0.75
            else:
                split_1 = state_e.Qlearning[int(state_e.position[0]) - 1][int(state_e.position[1])] / Qsum
                split_2 = state_e.Qlearning[int(state_e.position[0])][int(state_e.position[1]) + 1] / Qsum + split_1
                split_3 = state_e.Qlearning[int(state_e.position[0]) + 1][int(state_e.position[1])] / Qsum + split_2

            seed = np.random.random()
            if seed < split_1:
                action = [-1, 0]
            elif seed < split_2:
                action = [0, 1]
            elif seed < split_3:
                action = [1, 0]
            else:
                action = [0, -1]

    return action


def strategy(Qtable):  # 根据学习得到的Q表格判断运动的最佳路线
    position = [int(StateD.constant.size / 2), int(StateD.constant.size / 2)]  # 初始位置
    pos_history = [position]
    for i in range(StateD.constant.Ntrain):
        Qtable[position[0]][position[1]] = Qtable[position[0]][position[1]] - 1
        if position[0] == 0:  # 考虑边界条件
            if position[1] == 0:
                qr = Qtable[1][0]
                qu = Qtable[0][1]
                ql = 0
                qd = 0
            elif position[1] == StateD.constant.size - 1:
                qr = Qtable[1][StateD.constant.size - 1]
                qd = Qtable[0][StateD.constant.size - 2]
                ql = 0
                qu = 0
            else:
                qr = Qtable[1][position[1]]
                qu = Qtable[0][position[1] + 1]
                qd = Qtable[0][position[1] - 1]
                ql = 0
        elif position[0] == StateD.constant.size - 1:
            if position[1] == 0:
                ql = Qtable[StateD.constant.size - 2][0]
                qu = Qtable[StateD.constant.size - 1][1]
                qr = 0
                qd = 0
            elif position[1] == StateD.constant.size - 1:
                ql = Qtable[StateD.constant.size - 2][StateD.constant.size - 1]
                qd = Qtable[StateD.constant.size - 1][StateD.constant.size - 2]
                qr = 0
                qu = 0
            else:
                ql = Qtable[StateD.constant.size - 2][position[1]]
                qu = Qtable[StateD.constant.size - 1][position[1] + 1]
                qd = Qtable[StateD.constant.size - 1][position[1] - 1]
                ql = 0
        else:
            ql = Qtable[position[0] - 1][position[1]]
            qr = Qtable[position[0] + 1][position[1]]
            qu = Qtable[position[0]][position[1] + 1]
            qd = Qtable[position[0]][position[1] - 1]
        if ql == max(ql, qr, qu, qd):
            position[0] = position[0] - 1
        elif qr == max(ql, qr, qu, qd):
            position[0] = position[0] + 1
        elif qu == max(ql, qr, qu, qd):
            position[1] = position[1] + 1
        else:
            position[1] = position[1] - 1
        pos_history.append(position)
        print(position)
    return pos_history
