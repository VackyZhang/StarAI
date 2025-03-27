### 回测引擎
### 实现一个基础回测系统，用于测试策略。

import pandas as pd

def backtest(df: pd.DataFrame) -> float:
    """简单回测：计算策略的累计收益率"""
    df["Strategy Return"] = df["Signal"].shift(1) * df["Return"]
    cumulative_return = (1 + df["Strategy Return"]).cumprod()
    return cumulative_return.iloc[-1]