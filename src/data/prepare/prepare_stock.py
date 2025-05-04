"""
prepare_stock.py

主数据准备流程模块：
- 从 raw 数据中读取指定股票数据
- 进行缺失值处理等基础清洗
- 保存为 processed 数据供训练/回测使用
"""

import os
import pandas as pd
from config import base_config
from common.logger import get_logger
from common.data_utils import fill_missing
from common.file_utils import save_csv
from common.paths import ensure_dir
from data.prepare.preprocessor import normalize_df

logger = get_logger("PrepareStock")


def prepare_stock(symbol: str, overwrite: bool = False) -> pd.DataFrame:
    """
    清洗指定股票数据（包括缺失值处理等），保存到 processed/ 文件夹。

    Args:
        symbol (str): 股票代码，如 '000001.SZ'
        overwrite (bool): 是否覆盖已存在的清洗结果

    Returns:
        pd.DataFrame: 清洗后的数据
    """
    raw_dir = os.path.join(base_config["data_dir"], "raw")
    processed_dir = os.path.join(base_config["data_dir"], "processed")
    raw_path = os.path.join(raw_dir, f"{symbol}.csv")
    out_path = os.path.join(processed_dir, f"{symbol}.csv")

    ensure_dir(processed_dir)

    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Missing raw data file: {raw_path}")

    if os.path.exists(out_path) and not overwrite:
        logger.info(f"读取已有清洗结果: {out_path}")
        return pd.read_csv(out_path, parse_dates=["date"], index_col="date")

    logger.info(f"清洗数据: {symbol}")
    df = pd.read_csv(raw_path, parse_dates=["date"], index_col="date")

    df = fill_missing(df, method="ffill")

    # （可选）加入更多预处理逻辑
    df = normalize_df(df)

    save_csv(df, out_path)
    logger.info(f"✅ 清洗完成: {out_path}")
    return df
