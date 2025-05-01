# data/download.py
# 修复模拟数据生成中类型错误的问题
import os
import pandas as pd
import numpy as np

def fake_download_stock(symbol: str, start: str, end: str, save_dir='data/raw/'):
    """
    伪造的股票数据下载函数（替代真实接口）
    """
    dates = pd.date_range(start, end)
    n = len(dates)
    df = pd.DataFrame({
        'date': dates,
        'open': 10 + 0.1 * np.arange(n),
        'high': 10.5 + 0.05 * np.random.randn(n),
        'low': 9.8 + 0.05 * np.random.randn(n),
        'close': 10 + 0.05 * np.arange(n),
        'volume': np.random.randint(80000, 120000, size=n)
    })
    os.makedirs(save_dir, exist_ok=True)
    df.to_csv(os.path.join(save_dir, f"{symbol}.csv"), index=False)
    print(f"[Download] {symbol} data saved to {save_dir}")
    return df
