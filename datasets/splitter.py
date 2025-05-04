"""
splitter.py

数据集拆分模块，支持按比例拆分为 train/val/test。
"""

import pandas as pd


def split_by_ratio(df: pd.DataFrame, split_ratio=(0.8, 0.2), target_column="close"):
    """
    按比例拆分为训练集和验证集

    Args:
        df (pd.DataFrame): 原始数据
        split_ratio (tuple): 比例，如 (0.8, 0.2)
        target_column (str): 预测目标列

    Returns:
        tuple: X_train, y_train, X_val, y_val
    """
    total = len(df)
    train_end = int(total * split_ratio[0])

    features = df.drop(columns=[target_column])
    target = df[target_column]

    X_train = features.iloc[:train_end]
    y_train = target.iloc[:train_end]

    X_val = features.iloc[train_end:]
    y_val = target.iloc[train_end:]

    return X_train, y_train, X_val, y_val
