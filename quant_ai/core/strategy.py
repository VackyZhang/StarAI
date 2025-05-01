### 交易策略
### 定义不同的交易策略，比如均值回归策略、动量策略。

import pandas as pd

def mean_reversion_strategy(df: pd.DataFrame, window: int):
    """均值回归策略：价格低于均线买入，高于均线卖出"""
    df["SMA"] = df["Close"].rolling(window=window).mean()
    df["Signal"] = 0
    df.loc[df["Close"] < df["SMA"], "Signal"] = 1
    df.loc[df["Close"] > df["SMA"], "Signal"] = -1
    return df