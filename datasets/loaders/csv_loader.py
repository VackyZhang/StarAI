"""
csv_loader.py

从处理好的 CSV 文件加载数据，并返回 pandas DataFrame。
"""

import os
import pandas as pd
from datasets.configs.dataset_config import DATASET_CONFIG
from common.logger import get_logger

logger = get_logger("CsvLoader")


def load_dataset(name: str, split: str = "train", index_col: str = "date") -> pd.DataFrame:
    """
    加载指定数据集的指定切分（如 train/val/test）

    参数:
        name (str): 数据集名称（如 "000001.SZ"）
        split (str): 数据集切分，如 "train"、"val"、"test"
        index_col (str): 设置 DataFrame 的索引列，默认为 "date"

    返回:
        pd.DataFrame: 加载后的数据集
    """
    data_dir = DATASET_CONFIG.get("processed_dir", "data/processed")
    path = os.path.join(data_dir, name, f"{split}.csv")

    if not os.path.exists(path):
        logger.error(f"❌ 数据文件不存在: {path}")
        raise FileNotFoundError(f"无法加载数据集: {path}")

    try:
        df = pd.read_csv(path, parse_dates=[index_col], index_col=index_col)
        logger.info(f"✅ 加载数据集: {name}/{split}")
        return df
    except Exception as e:
        logger.exception(f"📛 加载数据集失败: {path}")
        raise e
