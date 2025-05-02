# 使用 akshare 下载 A 股历史行情数据（前复权）
import akshare as ak
import pandas as pd

def fetch_stock_akshare(symbol: str, start: str, end: str) -> pd.DataFrame:
    raw_symbol = symbol.split('.')[0]
    df = ak.stock_zh_a_hist(
        symbol=raw_symbol,
        period="daily",
        start_date=start.replace("-", ""),
        end_date=end.replace("-", ""),
        adjust="qfq"
    )
    df.rename(columns={
        "日期": "date", "开盘": "open", "最高": "high",
        "最低": "low", "收盘": "close", "成交量": "volume"
    }, inplace=True)
    df = df[["date", "open", "high", "low", "close", "volume"]]
    df["date"] = pd.to_datetime(df["date"])
    return df
