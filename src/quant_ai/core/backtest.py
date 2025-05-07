# quant_ai/core/backtest.py

"""
回测模块：执行完整的策略回测流程，连接数据加载、信号生成、执行、结果分析。
"""

from quant_ai.core.strategy import BaseStrategy
from quant_ai.core.execution import ExecutionEngine
from quant_ai.core.report import ReportGenerator
from quant_ai.config import backtest_config
from quant_ai.data.loader import load_data
from common.logger import get_logger

logger = get_logger("Backtest")

class BacktestEngine:
    def __init__(self, strategy: BaseStrategy = None):
        self.config = backtest_config
        self.strategy = strategy or BaseStrategy()
        self.execution = ExecutionEngine()
        self.report = ReportGenerator()

    def run(self):
        symbol = self.config.get("symbol", "000001.SZ")
        start = self.config.get("start_date")
        end = self.config.get("end_date")

        logger.info(f"📈 开始回测: {symbol} {start}~{end}")
        df = load_data(symbol=symbol, start=start, end=end)
        if df.empty:
            logger.error("❌ 数据加载失败")
            return None

        signals = self.strategy.generate_signals(df)
        trades = self.execution.execute(df, signals)
        report = self.report.generate(trades)

        logger.info("✅ 回测完成")
        return report
