import pandas as pd
from quant_ai.data_loader import load_stock_data

# 获取数据
df = load_stock_data("AAPL", "2023-01-01", "2024-01-01")
print(df.head())