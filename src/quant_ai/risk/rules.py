# quant_ai/risk/rules.py

"""
风控规则模块：定义通用风控规则接口和具体实现。
"""

from abc import ABC, abstractmethod
import pandas as pd
from common.logger import get_logger

logger = get_logger("RiskRules")


class RiskRule(ABC):
    """
    风控规则基类：所有规则必须实现 apply 接口。
    """

    @abstractmethod
    def apply(self, data: pd.DataFrame, signals: pd.Series) -> pd.Series:
        """
        应用风控规则。

        参数:
            data (pd.DataFrame): 市场数据
            signals (pd.Series): 原始策略信号

        返回:
            pd.Series: 应用规则后的信号
        """
        pass


class MaxPositionRule(RiskRule):
    """
    最大持仓风控规则：当仓位超过阈值时禁止继续加仓（允许减仓）。
    """

    def __init__(self, max_position: int = 1):
        self.max_position = max_position

    def apply(self, data: pd.DataFrame, signals: pd.Series) -> pd.Series:
        logger.info(f"🚧 应用最大持仓限制: 不超过 {self.max_position}")

        position = 0
        filtered = []

        for signal in signals:
            if signal == 1 and position >= self.max_position:
                filtered.append(0)
            else:
                filtered.append(signal)
                position += signal  # 支持 signal = -1 做减仓

        return pd.Series(filtered, index=signals.index)


class StopLossRule(RiskRule):
    """
    止损规则（占位实现）：当价格下跌超过阈值则发出清仓信号。
    （注意：当前为示例实现，不含真实逻辑）
    """

    def __init__(self, threshold: float = 0.05):
        self.threshold = threshold

    def apply(self, data: pd.DataFrame, signals: pd.Series) -> pd.Series:
        logger.info(f"🚧 应用止损规则：阈值 {self.threshold}")
        # 示例：返回原始信号（暂不处理止损逻辑）
        return signals


# 默认规则实例（可选）
default_max_position_rule = MaxPositionRule()

__all__ = [
    "RiskRule",
    "MaxPositionRule",
    "StopLossRule",
    "default_max_position_rule"
]
