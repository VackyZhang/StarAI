### 技术指标计算
### 提供常见的技术分析指标，如 SMA（简单移动平均）、EMA（指数移动平均）等。

import pandas as pd

def sma(df: pd.DataFrame, window: int) -> pd.Series:
    """计算简单移动平均（SMA）"""
    return df["Close"].rolling(window=window).mean()

def ema(df: pd.DataFrame, span: int) -> pd.Series:
    """计算指数移动平均（EMA）"""
    return df["Close"].ewm(span=span, adjust=False).mean()