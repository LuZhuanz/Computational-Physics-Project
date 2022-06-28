import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import environment as env

if __name__ == '__main__':
    print(env.EnvironmentCreate())
    plt.figure()
    sns.heatmap(data=env.EnvironmentCreate())
    plt.title("hhh")
    plt.show()
    env.EnvironmentStore(env.EnvironmentCreate())
