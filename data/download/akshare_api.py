"""
AkShare 股票数据接口封装

功能说明：
- 拉取股票日线数据
- 标准化字段为 ["date", "open", "high", "low", "close", "volume"]
"""

import akshare as ak
import pandas as pd
from common.logger import get_logger

logger = get_logger("AkShareAPI")

def fetch_stock_akshare(symbol: str, start: str, end: str) -> pd.DataFrame:
    """
    使用 AkShare 获取指定股票的历史行情
    """
    try:
        df = ak.stock_zh_a_hist(
            symbol=symbol,
            period="daily",
            start_date=start,
            end_date=end,
            adjust="qfq"
        )

        if df.empty or "日期" not in df.columns:
            logger.warning(f"AkShare 返回数据为空或缺少日期列: {symbol}")
            return pd.DataFrame()

        df.rename(columns={
            "日期": "date",
            "开盘": "open",
            "最高": "high",
            "最低": "low",
            "收盘": "close",
            "成交量": "volume",
        }, inplace=True)
        df["date"] = pd.to_datetime(df["date"])
        df.set_index("date", inplace=True)
        return df[["open", "high", "low", "close", "volume"]].sort_index()

    except Exception as e:
        logger.error(f"AkShare 获取股票数据失败: {e}")
        return pd.DataFrame()
