import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import agent  # 智能体模块
import StateD  # 类型声明
import environment  # 环境操作模块





if __name__ == '__main__':
    print(StateD.state.position)
    StateD.state.position = [23, 45]
    print(StateD.state.position)
