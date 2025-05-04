import matplotlib.pyplot as plt

def plot_data(df, title="Data Plot"):
    """
    绘制 DataFrame 数据的可视化图表
    """
    df.plot()
    plt.title(title)
    plt.show()
