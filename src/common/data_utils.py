"""
数据处理工具模块：
- 缺失值填充（支持多种策略）
- 数据归一化 & 标准化
"""

import pandas as pd


def fill_missing(df: pd.DataFrame, method: str = "ffill") -> pd.DataFrame:
    """
    填充缺失值。

    参数:
        df: 输入的 DataFrame。
        method: 填充方法，支持 'ffill', 'bfill', 'mean', 'median', 'mode', 'zero'。

    返回:
        填充后的 DataFrame。
    """
    if method == "ffill":
        return df.ffill()
    elif method == "bfill":
        return df.bfill()
    elif method == "mean":
        return df.fillna(df.mean(numeric_only=True))
    elif method == "median":
        return df.fillna(df.median(numeric_only=True))
    elif method == "mode":
        return df.fillna(df.mode().iloc[0])
    elif method == "zero":
        return df.fillna(0)
    else:
        raise ValueError(f"不支持的填充方法: {method}")


def normalize(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    对指定列进行归一化处理（最小-最大缩放到 [0, 1]）。

    参数:
        df: 输入 DataFrame。
        columns: 需要归一化的列名列表。

    返回:
        新的 DataFrame。
    """
    df = df.copy()
    for col in columns:
        min_val, max_val = df[col].min(), df[col].max()
        if max_val - min_val == 0:
            df[col] = 0
        else:
            df[col] = (df[col] - min_val) / (max_val - min_val)
    return df


def standardize(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
    对指定列进行标准化（z-score）。

    参数:
        df: 输入 DataFrame。
        columns: 需要标准化的列名列表。

    返回:
        新的 DataFrame。
    """
    df = df.copy()
    for col in columns:
        mean, std = df[col].mean(), df[col].std()
        if std == 0:
            df[col] = 0
        else:
            df[col] = (df[col] - mean) / std
    return df

