# quant_ai/data/loader.py

"""
数据加载模块：统一封装常见数据格式的加载逻辑，支持 CSV、Parquet、JSON、Pickle、Feather 等。
"""

import os
import pandas as pd
from common.logger import get_logger

logger = get_logger("DataLoader")


def load_data(
    path_or_buffer,
    file_type: str = None,
    **kwargs
) -> pd.DataFrame:
    """
    通用数据加载函数。

    参数:
        path_or_buffer (str or buffer or pd.DataFrame): 文件路径、文件对象或内存数据
        file_type (str): 文件类型（可选，如果未提供则自动根据文件后缀推断）
        kwargs: 透传给具体读取函数的参数

    返回:
        pd.DataFrame: 加载后的数据
    """
    if isinstance(path_or_buffer, pd.DataFrame):
        logger.info("📄 输入为 DataFrame，直接返回。")
        return path_or_buffer.copy()

    if not isinstance(path_or_buffer, str):
        raise ValueError("path_or_buffer 必须是 str、文件对象或 DataFrame。")

    path = path_or_buffer
    if not os.path.exists(path):
        logger.error(f"❌ 路径不存在: {path}")
        return pd.DataFrame()

    # 自动推断文件类型
    ext = os.path.splitext(path)[-1].lower()
    file_type = file_type or ext.lstrip(".")

    try:
        if file_type in ["csv"]:
            df = pd.read_csv(path, **kwargs)
        elif file_type in ["parquet"]:
            df = pd.read_parquet(path, **kwargs)
        elif file_type in ["json"]:
            df = pd.read_json(path, **kwargs)
        elif file_type in ["pkl", "pickle"]:
            df = pd.read_pickle(path, **kwargs)
        elif file_type in ["feather"]:
            df = pd.read_feather(path, **kwargs)
        else:
            logger.error(f"⚠️ 不支持的文件类型: {file_type}")
            return pd.DataFrame()

        logger.info(f"✅ 成功加载数据: {path} ({file_type})，行数: {len(df)}")
        return df

    except Exception as e:
        logger.exception(f"⚠️ 加载数据失败: {e}")
        return pd.DataFrame()
