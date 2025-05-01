# examples/run_prepare_data.py
# 运行示例：下载并准备股票数据，存入 data/processed/

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.download import fake_download_stock
from data.prepare import prepare_stock

symbol = '000001.SZ'
fake_download_stock(symbol, '2022-01-01', '2023-01-01')
df = prepare_stock(symbol)
print(df.head())
