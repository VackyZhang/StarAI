"""
数据加载模块：提供统一接口加载处理好的 CSV 数据为 pandas DataFrame
"""
import os
import pandas as pd
from datasets.configs.dataset_config import DATASET_CONFIG

def load_dataset(name: str, split: str = "train") -> pd.DataFrame:
    data_dir = DATASET_CONFIG["processed_dir"]
    path = os.path.join(data_dir, name, f"{split}.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(f"找不到数据文件: {path}")
    return pd.read_csv(path)
