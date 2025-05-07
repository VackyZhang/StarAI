# src/data/download/download_stock.py

"""
统一股票数据下载模块，支持 akshare / tushare 自动切换。
"""

import os
from config import base_config
from common.logger import get_logger
from common.paths import ensure_dir
from common.file_utils import save_csv
from common.data_utils import fill_missing
from data.download.akshare_api import fetch_stock_akshare
from data.download.tushare_api import fetch_stock_tushare

logger = get_logger("DownloadStock")


def download_stock(symbol: str, start: str, end: str, overwrite: bool = False) -> str | None:
    """
    下载股票数据并保存到 data/raw/ 下，返回保存路径（若失败则返回 None）。

    参数:
        symbol (str): 股票代码，如 "000001.SZ"
        start (str): 起始日期，格式为 "YYYY-MM-DD"
        end (str): 结束日期，格式为 "YYYY-MM-DD"
        overwrite (bool): 若为 True 则强制重新下载

    返回:
        str | None: 下载成功的 CSV 文件路径，失败返回 None
    """
    data_dir = os.path.join(base_config["data_dir"], "raw")
    save_path = os.path.join(data_dir, f"{symbol}.csv")
    ensure_dir(data_dir)

    if os.path.exists(save_path) and not overwrite:
        logger.info(f"已存在文件，跳过下载: {save_path}")
        return save_path

    source = base_config.get("data_source", "akshare")
    logger.info(f"开始下载 {symbol} 数据（{source}）: {start} ~ {end}")

    if source == "akshare":
        df = fetch_stock_akshare(symbol, start, end)
    else:
        df = fetch_stock_tushare(symbol, start, end)

    if df is None or df.empty:
        logger.warning(f"⚠️ 下载失败或无数据: {symbol}")
        return None

    df = fill_missing(df, method="ffill")

    if "date" not in df.columns:
        df = df.reset_index()

    save_csv(df, save_path)
    logger.info(f"✅ 下载完成并保存: {save_path}")
    return save_path
