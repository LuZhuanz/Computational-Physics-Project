import numpy as np


def choose_action(state):  # 由Q表格选择策略,羊群策略记入action
    if state.position[0] == 0:
        if state.position[1] == 0:
            if state.Qlearning[0][1] == 0 and state.Qlearning[1][0] == 0:
                split_1 = 0.5
            else:
                split_1 = state.Qlearning[0][1] / (state.Qlearning[0][1] + state.Qlearning[1][0])
            seed = np.random.random()
            if split_1 < seed:
                action = [1, 0]
            else:
                action = [0, 1]
        elif state.position[1] == 99:
            if state.Qlearning[99][1] == 0 and state.Qlearning[98][0] == 0:
                split_1 = 0.5
            else:
                split_1 = state.Qlearning[0][98] / (state.Qlearning[0][98] + state.Qlearning[1][99])
            seed = np.random.random()
            if split_1 < seed:
                action = [1, 0]
            else:
                action = [0, -1]
        else:
            Qsum = state.Qlearning[0][state.position[1] + 1] + state.Qlearning[0][state.position[1] - 1] + \
                   state.Qlearning[1][state.position[1]]
            split_1 = state.Qlearning[0][state.position[1] + 1] / Qsum
            split_2 = (state.Qlearning[0][state.position[1] + 1] + state.Qlearning[1][state.position[1]]) / Qsum
            seed = np.random.random()
            if seed < split_1:
                action = [0, 1]
            elif seed < split_2:
                action = [1, 0]
            else:
                action = [0, 1]
    elif state.position[0] == 99:
        if state.position[1] == 0:
            if state.Qlearning[99][1] == 0 and state.Qlearning[98][0] == 0:
                split_1 = 0.5
            else:
                split_1 = state.Qlearning[99][1] / (state.Qlearning[99][1] + state.Qlearning[98][0])
            seed = np.random.random()
            if split_1 < seed:
                action = [-1, 0]
            else:
                action = [0, 1]
        elif state.position[1] == 99:
            if state.Qlearning[99][98] == 0 and state.Qlearning[99][98] == 0:
                split_1 = 0.5
            else:
                split_1 = state.Qlearning[99][98] / (state.Qlearning[99][98] + state.Qlearning[98][99])
            seed = np.random.random()
            if split_1 < seed:
                action = [-1, 0]
            else:
                action = [0, -1]
        else:
            if state.Qlearning[99][state.position[1] + 1] == 0 and state.Qlearning[99][state.position[1] - 1] == 0 and \
                    state.Qlearning[98][state.position[1]] == 0:
                split_1 = 1 / 3
                split_2 = 2 / 3
            else:
                Qsum = state.Qlearning[99][state.position[1] + 1] + state.Qlearning[99][state.position[1] - 1] + \
                       state.Qlearning[98][state.position[1]]
                split_1 = state.Qlearning[99][state.position[1] + 1] / Qsum
                split_2 = (state.Qlearning[99][state.position[1] + 1] + state.Qlearning[98][state.position[1]]) / Qsum
            seed = np.random.random()
            if seed < split_1:
                action = [0, 1]
            elif seed < split_2:
                action = [-1, 0]
            else:
                action = [0, 1]
    else:
        Qsum = state.Qlearning[state.position[0] - 1][state.position[1]] + \
               state.Qlearning[state.position[0]][state.position[1] + 1] + state.Qlearning[state.position[0] + 1][
                   state.position[1]] + state.Qlearning[state.position[0]][state.position[1] - 1]
        if Qsum == 0:
            split_1 = 0.25
            split_2 = 0.5
            split_3 = 0.75
        else:
            split_1 = state.Qlearning[state.position[0] - 1][state.position[1]] / Qsum
            split_2 = state.Qlearning[state.position[0]][state.position[1] + 1] / Qsum + split_1
            split_3 = state.Qlearning[state.position[0] + 1][state.position[1]] / Qsum + split_2
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


