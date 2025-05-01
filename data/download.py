# data/download.py
# 统一封装股票数据下载逻辑，支持 akshare 和 tushare
# 数据默认保存在 data/raw/{symbol}.csv，可配置数据源
# 配置来源：config/base.yaml 或 .env 中的 TUSHARE_TOKEN

import os
import pandas as pd
from config import base_config, tushare_token

def download_stock(symbol: str, start: str, end: str, save_dir='data/raw/') -> pd.DataFrame:
    """
    主调用函数，根据 config 配置的数据源，自动选择下载方式。
    """
    source = base_config.get('data_source', 'akshare')

    if source == 'tushare':
        df = _download_from_tushare(symbol, start, end)
    else:
        df = _download_from_akshare(symbol, start, end)

    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{symbol}.csv")
    df.to_csv(save_path, index=False)
    print(f"[Download] {symbol} data saved to {save_path}")
    return df


# =====================
# AKSHARE 实现
# =====================
def _download_from_akshare(symbol: str, start: str, end: str) -> pd.DataFrame:
    import akshare as ak
    # symbol 要去掉 .SZ / .SH 后缀
    raw_symbol = symbol.split('.')[0]
    df = ak.stock_zh_a_hist(
        symbol=raw_symbol,
        period="daily",
        start_date=start.replace('-', ''),
        end_date=end.replace('-', ''),
        adjust="qfq"
    )
    df.rename(columns={
        '日期': 'date', '开盘': 'open', '最高': 'high', '最低': 'low',
        '收盘': 'close', '成交量': 'volume'
    }, inplace=True)
    df = df[['date', 'open', 'high', 'low', 'close', 'volume']]
    df['date'] = pd.to_datetime(df['date'])
    return df


# =====================
# TUSHARE 实现
# =====================
def _download_from_tushare(symbol: str, start: str, end: str) -> pd.DataFrame:
    import tushare as ts
    ts.set_token(tushare_token)
    pro = ts.pro_api()
    ts_code = _symbol_to_ts_code(symbol)

    df = pro.daily(ts_code=ts_code, start_date=start.replace('-', ''), end_date=end.replace('-', ''))
    df.rename(columns={
        'trade_date': 'date'
    }, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values('date', inplace=True)
    df = df[['date', 'open', 'high', 'low', 'close', 'vol']]
    df.rename(columns={'vol': 'volume'}, inplace=True)
    return df


def _symbol_to_ts_code(symbol: str) -> str:
    return symbol  # 默认直接返回原始格式，如 000001.SZ

