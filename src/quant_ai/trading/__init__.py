# quant_ai/trading/__init__.py

"""
交易接口模块：封装不同交易系统的接入方式，包括模拟交易和真实交易。
"""

from .broker_base import BrokerBase
from .mock import MockBroker
from .jqdatasdk import JQBroker

__all__ = [
    "BrokerBase",
    "MockBroker",
    "JQBroker",
]
