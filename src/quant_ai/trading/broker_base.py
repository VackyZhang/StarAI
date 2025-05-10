# quant_ai/trading/broker_base.py

"""
交易代理基类：定义标准交易接口，包括下单、撤单、查询等操作。
"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class BrokerBase(ABC):
    """
    交易代理抽象基类：用于统一模拟交易与实盘交易接口定义。
    """

    @abstractmethod
    def buy(self, symbol: str, price: float, volume: int) -> Dict[str, Any]:
        """买入操作"""
        pass

    @abstractmethod
    def sell(self, symbol: str, price: float, volume: int) -> Dict[str, Any]:
        """卖出操作"""
        pass

    @abstractmethod
    def cancel_order(self, order_id: str) -> bool:
        """撤销订单"""
        pass

    @abstractmethod
    def get_account_info(self) -> Dict[str, Any]:
        """获取账户信息"""
        pass

    @abstractmethod
    def get_open_orders(self) -> list:
        """查询当前未成交订单"""
        pass
