# datasets/preprocessor.py
# 数据预处理函数，包括缺失值填充与归一化

def fill_missing(df):
    return df.ffill().bfill()

def normalize(df):
    return (df - df.min()) / (df.max() - df.min())
