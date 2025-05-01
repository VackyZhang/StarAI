# datasets/factors.py
# 构建基础量化因子，如动量、波动率、换手率等
# 可用于因子选股、多因子模型或 ML 特征

import pandas as pd
import numpy as np

def momentum_factor(df: pd.DataFrame, window: int = 20) -> pd.Series:
    """
    动量因子：当前价格相较于过去 N 天的涨幅
    """
    return df['close'] / df['close'].shift(window) - 1

def volatility_factor(df: pd.DataFrame, window: int = 20) -> pd.Series:
    """
    波动率因子：收益率的标准差
    """
    returns = df['close'].pct_change()
    return returns.rolling(window).std()

def turnover_factor(df: pd.DataFrame, window: int = 20) -> pd.Series:
    """
    换手率因子：成交量相对平均成交量
    """
    return df['volume'] / df['volume'].rolling(window).mean()

def add_factors(df: pd.DataFrame, window: int = 20) -> pd.DataFrame:
    """
    将常用因子添加到 DataFrame 中
    """
    df = df.copy()
    df['factor_momentum'] = momentum_factor(df, window)
    df['factor_volatility'] = volatility_factor(df, window)
    df['factor_turnover'] = turnover_factor(df, window)
    return df
