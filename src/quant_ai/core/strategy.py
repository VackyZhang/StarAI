# src/quant_ai/core/strategy.py

"""
策略模块：定义基础策略结构和示例策略实现
"""

from abc import ABC, abstractmethod
import pandas as pd


class BaseStrategy(ABC):
    """
    抽象策略基类，所有策略需继承此类
    """

    def __init__(self, config: dict = None):
        self.config = config or {}

    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        """
        根据输入数据生成交易信号

        参数:
            data (pd.DataFrame): 输入的市场数据

        返回:
            pd.Series: 交易信号（1=买入，-1=卖出，0=观望）
        """
        pass


class MovingAverageCrossStrategy(BaseStrategy):
    """
    简单的均线交叉策略示例
    """

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        short_window = self.config.get("short_window", 5)
        long_window = self.config.get("long_window", 20)

        short_ma = data["close"].rolling(window=short_window).mean()
        long_ma = data["close"].rolling(window=long_window).mean()

        signal = pd.Series(0, index=data.index)
        signal[short_ma > long_ma] = 1
        signal[short_ma < long_ma] = -1
        return signal


# 兼容导入方式 from quant_ai.core.strategy import Strategy
Strategy = MovingAverageCrossStrategy
