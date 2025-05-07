# tests/quant_ai/core/test_backtest.py

"""
BacktestEngine 单元测试：验证回测流程是否能正确执行并生成结果。
"""

import pandas as pd
from quant_ai.core.backtest import BacktestEngine


def test_backtest_run():
    class DummyStrategy:
        def generate_signal(self, row):
            return 1  # 始终买入

    class DummyExecutionEngine:
        def execute(self, signal, row):
            return {"signal": signal, "price": row["price"]}

    class DummyReportGenerator:
        @staticmethod
        def generate(results):
            assert isinstance(results, list)
            assert all("signal" in r and "price" in r for r in results)

    engine = BacktestEngine()
    engine.strategy = DummyStrategy()
    engine.execution = DummyExecutionEngine()
    engine.report = DummyReportGenerator()

    # 修复点：使用 DataFrame 而非 list
    engine.data = pd.DataFrame([{"price": 100}, {"price": 101}])

    engine.run_backtest()
