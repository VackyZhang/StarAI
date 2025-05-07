# quant_ai/core/__init__.py

"""
quant_ai.core 模块初始化：汇总回测核心模块，包括策略、执行器、报告生成器等。
"""

from .backtest import BacktestEngine
from .strategy import BaseStrategy
from .execution import ExecutionEngine
from .report import ReportGenerator

__all__ = [
    "BacktestEngine",
    "BaseStrategy",
    "ExecutionEngine",
    "ReportGenerator"
]
