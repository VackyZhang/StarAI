"""
回测报告模块：处理回测结果，生成统计报告。
"""

import pandas as pd
from common.logger import get_logger

logger = get_logger("Report")

class ReportGenerator:
    def __init__(self, config=None):
        self.config = config or {}

    def generate(self, trades: pd.DataFrame) -> dict:
        if trades.empty:
            logger.warning("⚠️ 无交易记录，无法生成报告。")
            return {}

        total = trades["trade"].sum()
        count = trades["trade"].count()
        report = {
            "total_profit": total,
            "trade_count": count,
            "average_trade": total / count if count > 0 else 0
        }

        logger.info(f"📊 回测报告: {report}")
        return report
