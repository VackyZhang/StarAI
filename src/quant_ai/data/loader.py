# quant_ai/data/loader.py

"""
数据加载模块：封装多格式数据加载能力，支持 CSV、Parquet、JSON、内存对象等。
"""

import pandas as pd
from pathlib import Path
from common.logger import get_logger
from common.file_utils import load_csv, load_parquet, load_json

logger = get_logger("DataLoader")


class DataLoader:
    def __init__(self):
        pass

    def load(self, source, fmt="csv", **kwargs) -> pd.DataFrame:
        """
        加载指定格式的数据文件或结构。

        参数:
            source: 文件路径（str/Path）或内存对象
            fmt: 数据格式，如 'csv', 'parquet', 'json', 'dataframe'

        返回:
            pd.DataFrame: 加载的数据
        """
        logger.info(f"📥 加载数据，格式={fmt}，路径/对象={source}")

        if fmt == "csv":
            return load_csv(source, **kwargs)
        elif fmt == "parquet":
            return load_parquet(source, **kwargs)
        elif fmt == "json":
            return load_json(source, **kwargs)
        elif fmt == "dataframe":
            if isinstance(source, pd.DataFrame):
                return source.copy()
            else:
                raise ValueError("源对象不是有效的 DataFrame")
        else:
            raise ValueError(f"不支持的数据格式: {fmt}")
