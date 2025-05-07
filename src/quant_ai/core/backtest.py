# quant_ai/core/backtest.py

"""
回测模块：执行基于历史数据的策略回测流程，包括初始化、数据加载、策略执行、结果收集等。
"""

import pandas as pd
from common.logger import get_logger
from quant_ai.core.strategy import BaseStrategy
from quant_ai.core.execution import ExecutionEngine
from quant_ai.core.report import ReportGenerator
from quant_ai.config import backtest_config
from quant_ai.data.loader import load_data

logger = get_logger("Backtest")


class BacktestEngine:
    """
    回测引擎类，用于执行策略回测流程。
    """

    def __init__(self, config=None):
        self.config = config or backtest_config
        self.strategy = BaseStrategy()
        self.execution = ExecutionEngine()
        self.report = ReportGenerator()
        self.data = None

    def load_data(self):
        """
        加载历史市场数据。
        """
        symbol = self.config["symbol"]
        start = self.config["start_date"]
        end = self.config["end_date"]

        logger.info(f"📊 加载数据: {symbol} ({start} ~ {end})")
        self.data = load_data(symbol=symbol, start=start, end=end)

    def run_backtest(self):
        """
        执行完整的回测流程。
        """
        if self.data is None:
            self.load_data()

        if self.data is None or len(self.data) == 0:
            logger.error("❌ 数据加载失败，终止回测。")
            return

        logger.info("⚙️ 运行策略生成交易信号")
        signals = self.strategy.generate_signals(self.data)

        logger.info("💼 执行交易信号")
        trades = self.execution.execute(self.data, signals)

        logger.info("📄 生成回测报告")
        self.report.generate(trades)
        logger.info("✅ 回测流程完成")
