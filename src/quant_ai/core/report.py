# src/quant_ai/core/report.py

import pandas as pd
from common.logger import get_logger

logger = get_logger("Report")

class ReportGenerator:
    """
    回测结果报告生成器
    """

    def __init__(self):
        pass

    def generate(self, trades: pd.DataFrame, save_path: str = None) -> pd.DataFrame:
        """
        生成回测报告并可选保存为 CSV。

        参数:
            trades (pd.DataFrame): 包含交易记录的数据
            save_path (str, optional): 如果指定，则将报告保存至该路径

        返回:
            pd.DataFrame: 包含收益、波动等统计的报告
        """
        logger.info("📊 开始生成回测报告")

        report = pd.DataFrame({
            "total_trades": [len(trades)],
            "total_return": [trades["price"].pct_change().sum()],
            "max_price": [trades["price"].max()],
            "min_price": [trades["price"].min()]
        })

        if save_path:
            report.to_csv(save_path, index=False)
            logger.info(f"✅ 报告已保存至: {save_path}")

        return report
