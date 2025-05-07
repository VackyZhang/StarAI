# quant_ai/data/datasource.py

"""
数据源接口模块：封装从外部数据源下载并加载为 DataFrame 的逻辑。
"""

import pandas as pd
from common.logger import get_logger
from data.download.download_stock import download_stock

logger = get_logger("DataSource")


class DataSource:
    """
    数据源类：封装股票数据下载与读取逻辑
    """

    def __init__(self):
        pass

    def get_data(self, symbol: str, start: str, end: str) -> pd.DataFrame:
        """
        获取指定时间区间的股票数据。

        参数:
            symbol (str): 股票代码
            start (str): 起始日期 (YYYY-MM-DD)
            end (str): 结束日期 (YYYY-MM-DD)

        返回:
            pd.DataFrame: 股票数据表（包含日期、开盘价、收盘价等）
        """
        logger.info(f"获取数据: {symbol} ({start} ~ {end})")
        path = download_stock(symbol, start, end, overwrite=False)
        if not path:
            logger.warning(f"⚠️ 无法获取数据文件: {symbol}")
            return pd.DataFrame()

        try:
            df = pd.read_csv(path, parse_dates=["date"])
            df = df.set_index("date").sort_index()
            return df
        except Exception as e:
            logger.exception(f"读取数据失败: {path}")
            return pd.DataFrame()
