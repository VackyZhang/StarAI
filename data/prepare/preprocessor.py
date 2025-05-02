# 数据预处理模块：处理缺失值、归一化等
import pandas as pd

def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    return df.ffill().bfill()

def normalize(df: pd.DataFrame) -> pd.DataFrame:
    return (df - df.min()) / (df.max() - df.min())
