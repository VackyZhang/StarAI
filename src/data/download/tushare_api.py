"""
Tushare 股票数据接口封装

功能说明：
- 拉取股票日线数据
- 标准化字段为 ["date", "open", "high", "low", "close", "volume"]
"""

import tushare as ts
import pandas as pd
from common.logger import get_logger
from config import tushare_token

logger = get_logger("TushareAPI")

# 初始化 Tushare 客户端
ts.set_token(tushare_token)
pro = ts.pro_api()


def fetch_stock_tushare(symbol: str, start: str, end: str) -> pd.DataFrame:
    """
    使用 Tushare 获取日线行情，并进行字段标准化

    参数:
        symbol: 股票代码，如 "000001.SZ"
        start: 开始日期，格式 "YYYY-MM-DD"
        end: 结束日期，格式 "YYYY-MM-DD"

    返回:
        DataFrame，包含 date、open、high、low、close、volume
    """
    try:
        df = pro.daily(
            ts_code=symbol,
            start_date=start.replace("-", ""),
            end_date=end.replace("-", "")
        )

        if df.empty or "trade_date" not in df.columns:
            logger.warning(f"Tushare 返回数据为空或缺少日期列: {symbol}")
            return pd.DataFrame()

        df["date"] = pd.to_datetime(df["trade_date"])
        df.rename(columns={
            "open": "open",
            "high": "high",
            "low": "low",
            "close": "close",
            "vol": "volume"
        }, inplace=True)

        # 保留所需字段（不设为索引，供写入 CSV）
        return df[["date", "open", "high", "low", "close", "volume"]].sort_values("date")

    except Exception as e:
        logger.error(f"Tushare 获取股票数据失败: {e}")
        return pd.DataFrame()
