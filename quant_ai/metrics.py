### 策略评估
### 计算 Sharpe Ratio、最大回撤等评估指标。

import numpy as np

def sharpe_ratio(returns: pd.Series) -> float:
    """计算夏普比率"""
    return returns.mean() / returns.std() * np.sqrt(252)

def max_drawdown(df: pd.DataFrame) -> float:
    """计算最大回撤"""
    cumulative_max = df["Close"].cummax()
    drawdown = (df["Close"] - cumulative_max) / cumulative_max
    return drawdown.min()
