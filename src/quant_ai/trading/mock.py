# quant_ai/trading/mock.py

"""
模拟交易模块：提供一个本地模拟的交易代理，实现买卖、账户查询等功能。
"""

import uuid
import pandas as pd
from typing import Any, Dict, List
from quant_ai.trading.broker_base import BrokerBase


class MockBroker(BrokerBase):
    """
    模拟交易代理，实现基础买卖逻辑和账户状态管理。
    """

    def __init__(self, initial_cash: float = 1_000_000):
        self.cash = initial_cash
        self.positions = {}  # symbol -> volume
        self.orders = {}     # order_id -> order_dict

    def _generate_order_id(self) -> str:
        return str(uuid.uuid4())

    def buy(self, symbol: str, price: float, volume: int) -> Dict[str, Any]:
        cost = price * volume
        if self.cash < cost:
            return {"status": "rejected", "reason": "insufficient cash"}

        self.cash -= cost
        self.positions[symbol] = self.positions.get(symbol, 0) + volume

        order_id = self._generate_order_id()
        order = {
            "id": order_id,
            "symbol": symbol,
            "price": price,
            "volume": volume,
            "side": "buy",
            "status": "filled"
        }
        self.orders[order_id] = order
        return order

    def sell(self, symbol: str, price: float, volume: int) -> Dict[str, Any]:
        held = self.positions.get(symbol, 0)
        if held < volume:
            return {"status": "rejected", "reason": "insufficient position"}

        self.cash += price * volume
        self.positions[symbol] -= volume

        order_id = self._generate_order_id()
        order = {
            "id": order_id,
            "symbol": symbol,
            "price": price,
            "volume": volume,
            "side": "sell",
            "status": "filled"
        }
        self.orders[order_id] = order
        return order

    def cancel_order(self, order_id: str) -> bool:
        if order_id in self.orders and self.orders[order_id]["status"] != "filled":
            self.orders[order_id]["status"] = "canceled"
            return True
        return False

    def get_account_info(self) -> Dict[str, Any]:
        return {
            "cash": self.cash,
            "positions": self.positions.copy(),
            "equity": self.cash  # 简化：忽略持仓市值
        }

    def get_open_orders(self) -> List[Dict[str, Any]]:
        return [o for o in self.orders.values() if o["status"] != "filled"]

    def execute(self, signals: pd.Series, data: pd.DataFrame) -> pd.DataFrame:
        """
        批量执行策略信号，生成模拟交易记录。

        参数:
            signals (pd.Series): 每日买入（1）/卖出（-1）/持有（0）信号
            data (pd.DataFrame): 对应的市场数据，必须包含 'close'

        返回:
            pd.DataFrame: 每日交易金额记录
        """
        trades = pd.DataFrame(index=signals.index)
        trades["signal"] = signals
        trades["price"] = data["close"]
        trades["trade"] = trades["signal"] * trades["price"]
        return trades
