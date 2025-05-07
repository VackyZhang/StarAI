# quant_ai/data/datasource.py

"""
数据源模块：对外提供统一的历史数据读取接口，内部调用 download/download_stock.py。
"""

import os
import pandas as pd
from config import base_config
from data.download.download_stock import download_stock
from common.logger import get_logger

logger = get_logger("DataSource")

def get_price_data(symbol: str, start: str, end: str, overwrite: bool = False) -> pd.DataFrame:
    """
    获取指定股票的历史数据，并返回 pd.DataFrame（内部自动调用下载模块）。

    参数:
        symbol (str): 股票代码，例如 "000001.SZ"
        start (str): 起始日期，格式 "YYYY-MM-DD"
        end (str): 结束日期，格式 "YYYY-MM-DD"
        overwrite (bool): 是否强制重新下载

    返回:
        pd.DataFrame: 包含历史行情数据（带有 'date' 列）
    """
    logger.info(f"加载历史数据: {symbol} from {start} to {end}")
    csv_path = download_stock(symbol, start, end, overwrite=overwrite)

    if not csv_path or not os.path.exists(csv_path):
        logger.error(f"❌ 文件不存在: {csv_path}")
        return pd.DataFrame()

    df = pd.read_csv(csv_path, parse_dates=["date"])
    df = df.sort_values("date").reset_index(drop=True)
    return df
