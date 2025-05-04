"""
通用数据处理工具模块：
- 缺失值填充（多种策略支持）
- 安全保存 CSV 文件
"""

import os
import pandas as pd
from common.paths import ensure_dir


def fill_missing(df: pd.DataFrame, method: str = "ffill") -> pd.DataFrame:
    """
    填充缺失值。

    参数:
        df: 输入的 DataFrame。
        method: 填充方法，可选:
            - "ffill": 向前填充
            - "bfill": 向后填充
            - "mean": 按列均值填充
            - "median": 按列中位数填充
            - "mode": 按众数填充（仅取第一行）

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
    else:
        raise ValueError(f"不支持的填充方法: {method}")


def save_dataframe(df: pd.DataFrame, path: str, index: bool = False, encoding: str = "utf-8") -> None:
    """
    保存 DataFrame 到 CSV 文件，自动创建目录。

    参数:
        df: 要保存的 DataFrame。
        path: 保存路径。
        index: 是否保留索引。
        encoding: 编码格式，默认 utf-8。
    """
    ensure_dir(os.path.dirname(path))
    df.to_csv(path, index=index, encoding=encoding)
