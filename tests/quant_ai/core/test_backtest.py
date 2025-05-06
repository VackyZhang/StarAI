import pytest
from quant_ai.core.backtest import BacktestEngine

def test_backtest_run():
    engine = BacktestEngine()
    engine.run()
    results = engine.get_results()
    assert isinstance(results, list)
