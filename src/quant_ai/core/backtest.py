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
    def __init__(self, config=None):
        self.config = config or backtest_config
        self.strategy = Strategy()
        self.execution = ExecutionEngine()
        self.report_generator = ReportGenerator()

    def run(self):
        logger.info("📈 启动回测流程...")

        symbol = self.config["symbol"]
        df = load_data(symbol=symbol, start=self.config["start_date"], end=self.config["end_date"])
        if df.empty:
            logger.error("❌ 数据加载失败，终止回测。")
            return

        signals = df["close"].apply(self.strategy.generate_signal)
        trades = self.execution.execute(df, signals)
        self.report_generator.generate(trades)

        logger.info("✅ 回测完成。")
