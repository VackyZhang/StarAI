# quant_ai/core/report.py

"""
回测报告模块：用于统计策略表现并输出指标。
"""

import pandas as pd
from typing import Dict

class ReportGenerator:
    def __init__(self, trades: pd.DataFrame):
        self.trades = trades

    def generate_summary(self) -> Dict:
        """
        生成基本回测统计信息
        """
        pnl = self.trades["pnl"].sum()
        total_trades = len(self.trades)
        win_rate = (self.trades["pnl"] > 0).mean()

        return {
            "Total PnL": round(pnl, 2),
            "Number of Trades": total_trades,
            "Win Rate": round(win_rate * 100, 2)
        }

    def to_dataframe(self) -> pd.DataFrame:
        return self.trades.copy()
