import pytest
from quant_ai.core.backtest import BacktestEngine


def test_backtest_run(monkeypatch):
    class DummyStrategy:
        def generate_signal(self, row):
            return 1

    class DummyExecutionEngine:
        def execute(self, signal, row):
            return {"signal": signal, "price": row["price"]}

    class DummyReportGenerator:
        @staticmethod
        def generate(results):
            assert isinstance(results, list)

    engine = BacktestEngine()
    engine.strategy = DummyStrategy()
    engine.execution = DummyExecutionEngine()
    engine.report = DummyReportGenerator()

    engine.data = [{"price": 100}, {"price": 101}]
    engine.run_backtest()
