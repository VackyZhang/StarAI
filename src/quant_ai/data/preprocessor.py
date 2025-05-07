# quant_ai/data/preprocessor.py

"""
数据预处理模块：提供标准的数据清洗、缺失值填充、特征缩放等操作，用于回测和训练前的数据准备。
"""

import pandas as pd
from common.logger import get_logger
from common.data_utils import fill_missing

logger = get_logger("Preprocessor")


class DataPreprocessor:
    def __init__(self, method: str = "ffill", normalize: bool = True):
        """
        初始化预处理器。

        参数:
            method (str): 缺失值填充方式，如 'ffill', 'bfill', 'zero'
            normalize (bool): 是否执行标准化
        """
        self.method = method
        self.normalize = normalize

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        执行预处理，包括缺失值处理和标准化。

        参数:
            df (pd.DataFrame): 输入原始数据

        返回:
            pd.DataFrame: 处理后的数据
        """
        if df is None or df.empty:
            logger.warning("⚠️ 输入数据为空，跳过预处理。")
            return df

        logger.info("🧼 开始数据清洗与预处理...")

        df = fill_missing(df, method=self.method)

        if self.normalize:
            numeric_cols = df.select_dtypes(include="number").columns
            logger.info(f"📊 执行归一化列: {list(numeric_cols)}")
            df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].mean()) / df[numeric_cols].std(ddof=0)

        logger.info("✅ 预处理完成。")
        return df
