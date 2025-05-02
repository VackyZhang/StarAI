# 演示从下载到数据准备的完整流程（本地测试用）
import os
from data.download.download_stock import download_stock
from data.prepare.prepare_stock import prepare_stock
from config import base_config

symbol = "000001.SZ"
start = "2022-01-01"
end = "2022-12-31"

# 下载数据
df_raw = download_stock(symbol, start, end)
raw_dir = os.path.join(base_config["data_dir"], "raw")
os.makedirs(raw_dir, exist_ok=True)
df_raw.to_csv(os.path.join(raw_dir, f"{symbol}.csv"), index=False)

# 数据准备（填充缺失值）
df_ready = prepare_stock(symbol, overwrite=True)
print(df_ready.head())
