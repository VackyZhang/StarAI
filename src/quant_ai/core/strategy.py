"""
策略模块：定义基础策略框架及具体实现，用于生成交易信号。
"""

from quant_ai.config import strategy_config

class BaseStrategy:
    def __init__(self, config=None):
        self.config = config or strategy_config

    def generate_signal(self, data_row):
        raise NotImplementedError("请实现 generate_signal 方法")

class Strategy(BaseStrategy):
    def generate_signal(self, data_row):
        price = data_row["close"]
        return 1 if price > 100 else -1
