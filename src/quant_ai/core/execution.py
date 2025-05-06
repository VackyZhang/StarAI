# src/quant_ai/core/execution.py

"""
执行模块：模拟订单执行流程（撮合引擎）
"""

import pandas as pd


class ExecutionEngine:
    """
    执行引擎：根据信号执行交易，计算持仓和资金变化
    """

    def __init__(self, initial_cash: float = 100000.0):
        self.initial_cash = initial_cash
        self.cash = initial_cash
        self.position = 0
        self.history = []

    def execute(self, data: pd.DataFrame, signals: pd.Series) -> pd.DataFrame:
        """
        执行策略信号，并计算交易记录和资产变化

        参数:
            data (pd.DataFrame): 市场数据，需包含 'close'
            signals (pd.Series): 策略生成的信号序列

        返回:
            pd.DataFrame: 包含资产变化记录的 DataFrame
        """
        records = []
        for date, signal in signals.items():
            price = data.at[date, "close"]
            action = "HOLD"

            if signal == 1 and self.cash >= price:
                self.position += 1
                self.cash -= price
                action = "BUY"
            elif signal == -1 and self.position > 0:
                self.position -= 1
                self.cash += price
                action = "SELL"

            value = self.cash + self.position * price
            records.append({
                "date": date,
                "price": price,
                "signal": signal,
                "action": action,
                "cash": self.cash,
                "position": self.position,
                "portfolio_value": value,
            })

        return pd.DataFrame(records).set_index("date")
