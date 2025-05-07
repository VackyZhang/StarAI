# src/quant_ai/core/backtest.py

from common.logger import get_logger
from quant_ai.core.strategy import BaseStrategy
from quant_ai.core.execution import ExecutionEngine
from quant_ai.core.report import ReportGenerator
from quant_ai.config import backtest_config
from quant_ai.data.loader import load_data

logger = get_logger("Backtest")


class BacktestEngine:
    def __init__(self, config=None):
        self.config = config or backtest_config
        self.strategy = BaseStrategy()
        self.execution = ExecutionEngine()
        self.report = ReportGenerator()
        self.data = None

    def load_data(self):
        symbol = self.config["symbol"]
        start = self.config["start_date"]
        end = self.config["end_date"]
        self.data = load_data(symbol, start=start, end=end)

    def run_backtest(self):
        if self.data is None:
            self.load_data()

        if self.data is None or len(self.data) == 0:
            logger.error("❌ 数据加载失败，终止回测。")
            return

        results = []
        for _, row in self.data.iterrows():
            signal = self.strategy.generate_signal(row)
            result = self.execution.execute(signal, row)
            results.append(result)

        self.report.generate(results)
        logger.info("✅ 回测完成。")
