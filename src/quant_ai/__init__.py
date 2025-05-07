# quant_ai/__init__.py

"""
quant_ai 包初始化模块：统一导出核心模块接口，便于外部使用。
"""

from . import config
from .core import BacktestEngine, BaseStrategy, ExecutionEngine, ReportGenerator
from .data import datasource, loader, preprocessor
from .risk import risk_manager
from .trading import broker_base, jqdatasdk, mock

__all__ = [
    "config",
    "BacktestEngine",
    "BaseStrategy",
    "ExecutionEngine",
    "ReportGenerator",
    "datasource",
    "loader",
    "preprocessor",
    "risk_manager",
    "broker_base",
    "jqdatasdk",
    "mock"
]
