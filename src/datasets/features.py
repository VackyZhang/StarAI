"""
features.py

特征构造模块：添加技术指标（如 MA、MACD）等。
"""

import pandas as pd


def add_technical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    添加基础技术指标到原始数据中。

    当前支持：
    - MA_5（5日均线）
    - MA_10（10日均线）

    Args:
        df (pd.DataFrame): 原始数据

    Returns:
        pd.DataFrame: 添加特征后的数据
    """
    df = df.copy()
    df["MA_5"] = df["close"].rolling(window=5).mean()
    df["MA_10"] = df["close"].rolling(window=10).mean()

    # 可选：丢弃含 NA 的开头部分
    df = df.dropna()

    return df
