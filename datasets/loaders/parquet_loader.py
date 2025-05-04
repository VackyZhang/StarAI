"""
parquet_loader.py

从 Parquet 文件中加载数据，支持通过配置文件路径加载。
"""

import os
import pandas as pd
from datasets.configs.dataset_config import DATASET_CONFIG
from common.logger import get_logger

logger = get_logger("ParquetLoader")


def load_dataset(name: str, split: str = "train", index_col: str = "date") -> pd.DataFrame:
    """
    从 Parquet 文件加载数据，并返回 DataFrame。

    参数:
        name (str): 数据集名称，如 "000001.SZ"
        split (str): 数据集切分，如 "train", "test"
        index_col (str): 设置 DataFrame 的索引列，默认为 "date"

    返回:
        pd.DataFrame: 返回加载的数据集
    """
    data_dir = DATASET_CONFIG["processed_dir"]
    file_path = os.path.join(data_dir, name, f"{split}.parquet")

    if not os.path.exists(file_path):
        logger.error(f"❌ 找不到文件: {file_path}")
        raise FileNotFoundError(f"无法加载数据集：{file_path}")

    try:
        df = pd.read_parquet(file_path)
        df.set_index(index_col, inplace=True)
        logger.info(f"✅ 加载 Parquet 数据集: {file_path}")
        return df
    except Exception as e:
        logger.exception(f"📛 加载 Parquet 失败: {file_path}")
        raise e
