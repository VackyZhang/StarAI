# quant_ai/core/backtest.py

"""
回测模块：执行基于历史数据的策略回测流程，包括初始化、数据加载、策略执行、结果收集等。
"""

from common.logger import get_logger
from quant_ai.core.strategy import Strategy
from quant_ai.core.execution import ExecutionEngine
from quant_ai.core.report import ReportGenerator
from quant_ai.config import backtest_config
from quant_ai.data.loader import load_data

logger = get_logger("Backtest")


class BacktestEngine:
    """
    回测引擎类：封装完整的回测流程。
    """

    def __init__(self, config=None):
        self.config = config or backtest_config
        self.strategy = Strategy(config_name="strategy")
        self.execution = ExecutionEngine()
        self.logger = logger
        self.results = []

    def run(self):
        """
        执行回测。
        """
        self.logger.info("📈 启动回测流程...")

        # 加载数据
        symbol = self.config["symbol"]
        df = load_data(symbol=symbol, start=self.config["start_date"], end=self.config["end_date"])
        if df.empty:
            self.logger.error("❌ 数据加载失败，终止回测。")
            return

        for _, row in df.iterrows():
            signal = self.strategy.generate_signal(row)
            result = self.execution.execute(signal, row)
            self.results.append(result)

        ReportGenerator.generate(self.results)
        self.logger.info("✅ 回测完成。")

    def get_results(self):
        return self.results
