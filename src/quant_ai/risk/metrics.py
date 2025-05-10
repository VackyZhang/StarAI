# quant_ai/risk/metrics.py

"""
风险指标模块：提供评估策略表现的常用指标，如累计收益、最大回撤、夏普比率等。
"""

import pandas as pd
import numpy as np

__all__ = [
    "RiskMetrics",
    "compute_cumulative_returns",
    "compute_max_drawdown",
    "compute_sharpe_ratio",
    "compute_daily_returns"
]


class RiskMetrics:
    def __init__(self, trades: pd.DataFrame, risk_free_rate: float = 0.0):
        """
        风险指标计算器。

        参数:
            trades (pd.DataFrame): 包含 'trade' 列的交易记录
            risk_free_rate (float): 年化无风险利率，默认为 0.0
        """
        self.trades = trades
        self.risk_free_rate = risk_free_rate
        self.daily_returns = compute_daily_returns(trades)
        self.cumulative_returns = compute_cumulative_returns(trades)

    def max_drawdown(self) -> float:
        return compute_max_drawdown(self.cumulative_returns)

    def sharpe_ratio(self) -> float:
        return compute_sharpe_ratio(self.daily_returns, self.risk_free_rate)

    def summary(self) -> dict:
        """
        返回所有指标的汇总结果。
        """
        return {
            "max_drawdown": self.max_drawdown(),
            "sharpe_ratio": self.sharpe_ratio(),
            "cumulative_return": self.cumulative_returns.iloc[-1] if not self.cumulative_returns.empty else 0.0
        }


def compute_daily_returns(trades: pd.DataFrame) -> pd.Series:
    """
    计算每日收益率。

    参数:
        trades (pd.DataFrame): 包含 'trade' 列的交易记录

    返回:
        pd.Series: 每日收益率序列
    """
    return trades["trade"]


def compute_cumulative_returns(trades: pd.DataFrame) -> pd.Series:
    """
    计算累计收益。

    参数:
        trades (pd.DataFrame): 包含 'trade' 列的交易数据

    返回:
        pd.Series: 累计收益序列
    """
    result = trades["trade"].cumsum()
    result.name = "cumulative"
    return result


def compute_max_drawdown(cumulative_returns: pd.Series) -> float:
    """
    计算最大回撤。

    参数:
        cumulative_returns (pd.Series): 累计收益序列

    返回:
        float: 最大回撤（正值）
    """
    peak = cumulative_returns.cummax()
    drawdown = cumulative_returns - peak
    max_dd = drawdown.min()
    return abs(max_dd)


def compute_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    计算夏普比率。

    参数:
        returns (pd.Series): 每日收益率序列
        risk_free_rate (float): 无风险利率，默认 0.0

    返回:
        float: 夏普比率
    """
    excess_returns = returns - risk_free_rate
    mean_return = excess_returns.mean()
    std_return = excess_returns.std(ddof=1)

    if std_return == 0:
        return 0.0

    return mean_return / std_return
