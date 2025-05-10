# src/quant_ai/risk/__init__.py

"""
风控模块接口：暴露常用的风险管理组件。
"""

from .risk_manager import RiskManager
from .rules import RiskRule, MaxPositionRule
from .metrics import RiskMetrics

__all__ = [
    "RiskManager",
    "RiskRule",
    "MaxPositionRule",
    "RiskMetrics",
]
