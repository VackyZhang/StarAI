"""
测试策略模块：验证 BaseStrategy 是否能正确生成固定买入信号。
"""

import pandas as pd
from quant_ai.core.strategy import BaseStrategy

def test_generate_signals():
    strategy = BaseStrategy()
    data = pd.DataFrame({
        "price": [100, 101, 102]
    })

    signals = strategy.generate_signals(data)

    assert isinstance(signals, pd.Series)
    assert len(signals) == len(data)
    assert all(signals == 1)  # 固定策略应全为买入信号
