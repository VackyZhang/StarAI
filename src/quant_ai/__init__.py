# quant_ai/__init__.py

"""
量化AI框架：集成量化交易的核心模块，包括数据处理、策略执行、风险管理与交易等。
"""

from .core import (
    backtest,
    execution,
    report,
    strategy
)

from .data import (
    datasource,
    loader,
    preprocessor
)

from .risk import risk_manager
from .trading import broker_base, jqdatasdk, mock

__all__ = [
    "backtest",
    "execution",
    "report",
    "strategy",
    "datasource",
    "loader",
    "preprocessor",
    "risk_manager",
    "broker_base",
    "jqdatasdk",
    "mock"
]
