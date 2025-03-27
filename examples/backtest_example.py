import pandas as pd
from quant_ai.data_loader import load_stock_data
from quant_ai.strategies import mean_reversion_strategy
from quant_ai.backtest import backtest

# 获取数据
df = load_stock_data("AAPL", "2023-01-01", "2024-01-01")

# 运行策略
df = mean_reversion_strategy(df, window=20)

# 运行回测
final_return = backtest(df)
print(f"策略最终收益率: {final_return:.2f}")