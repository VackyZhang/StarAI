# 使用 tushare 下载 A 股历史行情数据（需 token）
import tushare as ts
import pandas as pd
from config import tushare_token

def fetch_stock_tushare(symbol: str, start: str, end: str) -> pd.DataFrame:
    ts.set_token(tushare_token)
    pro = ts.pro_api()
    df = pro.daily(
        ts_code=symbol,
        start_date=start.replace("-", ""),
        end_date=end.replace("-", "")
    )
    df.rename(columns={"trade_date": "date"}, inplace=True)
    df["date"] = pd.to_datetime(df["date"])
    df.sort_values("date", inplace=True)
    df = df[["date", "open", "high", "low", "close", "vol"]]
    df.rename(columns={"vol": "volume"}, inplace=True)
    return df
