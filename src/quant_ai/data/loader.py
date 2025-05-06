# src/quant_ai/data/loader.py

"""
数据加载模块：为策略回测和训练提供数据支持。
"""

import pandas as pd
from pathlib import Path
from common.paths import DATA_PROCESSED_DIR

def load_data(symbol: str, split: str = "train") -> pd.DataFrame:
    """
    加载预处理后的数据。

    参数:
        symbol (str): 股票代码，如 '000001.SZ'
        split (str): 数据集分割（train, val, test）

    返回:
        pd.DataFrame: 加载的数据
    """
    file_path = Path(DATA_PROCESSED_DIR) / symbol / f"{split}.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"未找到数据文件: {file_path}")
    return pd.read_csv(file_path)
