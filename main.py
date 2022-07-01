import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

import agent  # 智能体模块
import StateD  # 类型声明
import environment  # 环境操作模块
import train  # 训练模块
import display  # 结果打印

if __name__ == '__main__':
    T1 = time.time()
    train.updateq()
    T2 = time.time()
    print('程序运行时间:%s秒' % (T2 - T1))
    
