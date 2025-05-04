"""
preprocessor.py

数据预处理工具模块：
- 包含常用的特征填充、归一化、移动窗口等处理逻辑
"""

import pandas as pd


def normalize_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    简单归一化处理（0-1缩放），仅适用于训练特征演示

    Args:
        df (pd.DataFrame): 输入原始数据

    Returns:
        pd.DataFrame: 归一化后的数据
    """
    df_norm = df.copy()
    for col in df_norm.columns:
        if pd.api.types.is_numeric_dtype(df_norm[col]):
            min_val = df_norm[col].min()
            max_val = df_norm[col].max()
            if min_val != max_val:
                df_norm[col] = (df_norm[col] - min_val) / (max_val - min_val)
    return df_norm
