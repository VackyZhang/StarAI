from config import base_config
from data.download.download_stock import download_stock
from data.prepare.prepare_stock import prepare_stock

if __name__ == "__main__":
    symbol = "000001.SZ"
    start_date = "2023-01-05"
    end_date = "2023-01-10"

    base_config["data_source"] = "tushare"  # 强制使用 tushare

    print(f"[Download] 下载 {symbol} 数据...")
    csv_path = download_stock(symbol, start_date, end_date, overwrite=True)
    if not csv_path:
        print("[❌] 下载失败，跳过清洗流程")
        exit()

    print(f"[Prepare] 清洗 {symbol} 数据...")
    df = prepare_stock(symbol, overwrite=True)
    print(df.head())
