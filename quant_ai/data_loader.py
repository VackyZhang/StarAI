### 数据获取模块
### 负责从不同的数据源获取市场数据，并进行数据清洗。

import pandas as pd
import yfinance as yf

def load_stock_data(symbol: str, start: str, end: str) -> pd.DataFrame:
    """获取股票历史数据"""
    stock = yf.download(symbol, start=start, end=end)
    stock['Return'] = stock['Close'].pct_change()
    return stock