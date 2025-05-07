# quant_ai/core/report.py

"""
报告模块：基于交易记录输出性能指标与可视化。
"""

import pandas as pd
from common.logger import get_logger

logger = get_logger("Report")

class ReportGenerator:
    def __init__(self):
        pass

    def generate(self, trades: pd.DataFrame) -> dict:
        logger.info("📊 生成回测报告")
        report = {
            "total_trades": trades["signal"].count(),
            "total_volume": trades["trade"].sum(),
            "mean_price": trades["close"].mean()
        }
        logger.info(f"📄 回测报告摘要: {report}")
        return report
