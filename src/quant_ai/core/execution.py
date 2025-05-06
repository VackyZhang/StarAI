"""
执行模块：根据策略生成的信号执行交易，生成交易记录。
"""

import pandas as pd
from common.logger import get_logger

logger = get_logger("Execution")

class ExecutionEngine:
    def __init__(self, config=None):
        self.config = config or {}

    def execute(self, data: pd.DataFrame, signals: pd.Series) -> pd.DataFrame:
        records = []
        for date, signal in signals.items():
            price = data.loc[date, "close"]
            trade = {
                "date": date,
                "signal": signal,
                "price": price,
                "trade": signal * price,
            }
            records.append(trade)
            logger.debug(f"[TRADE] {trade}")
        return pd.DataFrame(records)
