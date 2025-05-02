# 提供统一 download_stock 接口，按 config 配置选择 akshare/tushare
from config import base_config
from download.akshare_api import fetch_stock_akshare
from download.tushare_api import fetch_stock_tushare

def download_stock(symbol: str, start: str, end: str):
    source = base_config.get("data_source", "akshare").lower()
    if source == "tushare":
        return fetch_stock_tushare(symbol, start, end)
    return fetch_stock_akshare(symbol, start, end)
